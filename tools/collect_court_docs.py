"""tools/collect_court_docs.py

Searches for court documents (indictments, judgments, sentencing memos)
related to existing wiki operations. Saves to raw/case-documents/ and
optionally creates wiki/cases/ stubs.

Usage:
    python tools/collect_court_docs.py                    # all operations
    python tools/collect_court_docs.py --slug operation-endgame
    python tools/collect_court_docs.py --top 20           # top N by priority
    python tools/collect_court_docs.py --dry-run           # search without saving
    python tools/collect_court_docs.py --force             # ignore 30-day cooldown
    python tools/collect_court_docs.py --create-stubs      # also create wiki/cases/ stubs

Data sources:
    1. CourtListener REST API (US federal cases) - primary
    2. DOJ press release PDF link extraction
    3. UNODC SHERLOC (international cases) - secondary
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, quote_plus, urljoin
from urllib.request import Request, urlopen

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_CASE_DIR = PROJECT_ROOT / "raw" / "case-documents"
WIKI_CASES_DIR = PROJECT_ROOT / "wiki" / "cases"
WIKI_OPS_DIR = PROJECT_ROOT / "wiki" / "operations"
STATE_FILE = Path(__file__).resolve().parent / ".court_doc_state.json"

# Ensure directories exist
RAW_CASE_DIR.mkdir(parents=True, exist_ok=True)
WIKI_CASES_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Windows cp949 safety (L8)
# ---------------------------------------------------------------------------
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

COURTLISTENER_API = "https://www.courtlistener.com/api/rest/v4/search/"
COURTLISTENER_DELAY = 1.0  # seconds between requests
SHERLOC_DELAY = 2.0
DOJ_DELAY = 1.5
MAX_BACKOFF = 32  # max exponential backoff seconds
TODAY = datetime.now().strftime("%Y-%m-%d")
COOLDOWN_DAYS = 30

# US-related lead agencies (for priority scoring)
US_AGENCIES = frozenset({
    "fbi-cyber-division", "us-doj", "us-secret-service", "fbi",
    "doj", "usss", "us-doj-ccips", "irs-ci",
})

# Non-Western agencies (lower court doc accessibility)
LOW_ACCESS_AGENCIES = frozenset({
    "china-mps", "russia-mvd", "iran-fata", "north-korea",
})

# Case number patterns in body text
CASE_NUMBER_RE = re.compile(
    r"\b(\d{1,2}:\d{2}-(?:cr|cv|mj)-\d{3,6}(?:-\w+)?)\b", re.IGNORECASE
)

# Defendant name patterns (e.g., "United States v. Doe" or "v. Doe et al.")
DEFENDANT_RE = re.compile(
    r"(?:United States|U\.S\.|Government)\s+v\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
    re.IGNORECASE,
)

# Proper name pattern for extracting names from target_entity
PROPER_NAME_RE = re.compile(
    r"\b([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){1,3})\b"
)

# Document type classification keywords
DOC_TYPE_KEYWORDS: dict[str, list[str]] = {
    "indictment": ["indictment", "superseding indictment", "charged", "grand jury"],
    "complaint": ["criminal complaint", "complaint and affidavit", "affidavit"],
    "sentencing-memo": ["sentencing memorandum", "sentencing memo", "sentence"],
    "judgment": ["judgment", "judgement", "order of forfeiture", "conviction"],
    "plea-agreement": ["plea agreement", "guilty plea", "plea deal"],
}

# Frontmatter parser (reuse project's own)
sys.path.insert(0, str(PROJECT_ROOT))
try:
    from frontmatter import Post, load as fm_load
except ImportError:
    # Minimal fallback
    @dataclass
    class Post:  # type: ignore[no-redef]
        metadata: dict[str, Any] = field(default_factory=dict)
        content: str = ""

    def fm_load(path: str | Path) -> Post:
        text = Path(path).read_text(encoding="utf-8")
        fm_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
        match = fm_re.match(text)
        if not match:
            return Post({}, text)
        # Minimal YAML-like parse
        return Post({}, text)


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_state() -> dict[str, Any]:
    """Load persistent state tracking searched operations."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {"operations": {}, "documents": []}
    return {"operations": {}, "documents": []}


def save_state(state: dict[str, Any]) -> None:
    """Save state to disk."""
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def is_recently_searched(state: dict[str, Any], slug: str) -> bool:
    """Check if operation was searched within COOLDOWN_DAYS."""
    ops = state.get("operations", {})
    if slug not in ops:
        return False
    last_search = ops[slug].get("last_search", "")
    if not last_search:
        return False
    try:
        last_dt = datetime.strptime(last_search, "%Y-%m-%d")
        return (datetime.now() - last_dt).days < COOLDOWN_DAYS
    except ValueError:
        return False


def mark_searched(state: dict[str, Any], slug: str, doc_count: int) -> None:
    """Record that an operation has been searched."""
    if "operations" not in state:
        state["operations"] = {}
    state["operations"][slug] = {
        "last_search": TODAY,
        "doc_count": doc_count,
    }


def is_duplicate_doc(state: dict[str, Any], source_url: str) -> bool:
    """Check if a document URL has already been saved."""
    known = {d.get("source_url", "") for d in state.get("documents", [])}
    return source_url in known


def record_document(state: dict[str, Any], doc_meta: dict[str, str]) -> None:
    """Record a saved document in state."""
    if "documents" not in state:
        state["documents"] = []
    state["documents"].append(doc_meta)


# ---------------------------------------------------------------------------
# Operation loading and parsing
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class OperationInfo:
    """Immutable container for operation metadata relevant to court doc search."""
    slug: str
    title: str
    aliases: tuple[str, ...]
    target_entity: str
    lead_agency: str
    enforcement_type: tuple[str, ...]
    status: str
    outcome: str
    timeframe_announced: str
    timeframe_start: str
    indictments: int
    body_text: str
    case_numbers: tuple[str, ...]
    defendant_names: tuple[str, ...]
    priority_score: int


def _strip_wikilink(val: str) -> str:
    """Remove [[ ]] wikilink markers and display text."""
    if not isinstance(val, str):
        return str(val) if val else ""
    val = val.strip()
    if val.startswith("[[") and val.endswith("]]"):
        inner = val[2:-2]
        if "|" in inner:
            return inner.split("|", 1)[0]
        return inner
    return val


def _get_str(meta: dict[str, Any], key: str, default: str = "") -> str:
    """Safely get a string from metadata dict."""
    val = meta.get(key, default)
    if val is None:
        return default
    return str(val).strip()


def _get_list(meta: dict[str, Any], key: str) -> list[str]:
    """Safely get a list of strings from metadata."""
    val = meta.get(key, [])
    if isinstance(val, list):
        return [str(v).strip() for v in val if v]
    if isinstance(val, str) and val:
        return [val.strip()]
    return []


def _get_nested_int(meta: dict[str, Any], *keys: str, default: int = 0) -> int:
    """Get integer from nested dict path."""
    current: Any = meta
    for k in keys:
        if isinstance(current, dict):
            current = current.get(k, default)
        else:
            return default
    try:
        return int(current)
    except (ValueError, TypeError):
        return default


def load_operation(slug: str) -> OperationInfo | None:
    """Load operation frontmatter and extract search-relevant fields."""
    filepath = WIKI_OPS_DIR / f"{slug}.md"
    if not filepath.exists():
        return None

    try:
        post = fm_load(filepath)
    except Exception:
        return None

    meta = post.metadata
    body = post.content or ""

    # Extract fields
    title = _get_str(meta, "title")
    aliases = tuple(_get_list(meta, "aliases"))
    target_entity = _get_str(meta, "target_entity")
    lead_agency_raw = _get_str(meta, "lead_agency")
    lead_agency = _strip_wikilink(lead_agency_raw)
    enforcement_type = tuple(_get_list(meta, "enforcement_type"))
    status = _get_str(meta, "status")
    outcome = _get_str(meta, "outcome")

    # Timeframe
    timeframe = meta.get("timeframe", {})
    if isinstance(timeframe, dict):
        timeframe_announced = _get_str(timeframe, "announced")
        timeframe_start = _get_str(timeframe, "start")
    else:
        timeframe_announced = ""
        timeframe_start = ""

    # Results
    indictments = _get_nested_int(meta, "results", "indictments")

    # Extract case numbers from body
    case_numbers = tuple(CASE_NUMBER_RE.findall(body))

    # Extract defendant names from body and target_entity
    defendant_matches = DEFENDANT_RE.findall(body)
    # Also extract from target_entity if it has names
    if target_entity:
        target_defendants = DEFENDANT_RE.findall(target_entity)
        defendant_matches = list(set(defendant_matches + target_defendants))
    # Also extract proper names from target_entity (persons, not places/orgs)
    if target_entity:
        _skip_names = {
            "silk road", "dark web", "dread pirate", "operation",
            "botnet", "ransomware", "malware", "infrastructure",
            "marketplace", "network", "group", "team",
        }
        for name in PROPER_NAME_RE.findall(target_entity):
            if name.lower() not in _skip_names and name not in defendant_matches:
                parts = name.split()
                if len(parts) >= 2:
                    defendant_matches.append(name)
                    # Add surname for relevance matching (not for queries)
                    surname = parts[-1]
                    if len(surname) >= 4 and surname not in defendant_matches:
                        defendant_matches.append(surname)
    defendant_names = tuple(dict.fromkeys(defendant_matches))  # dedupe, preserve order

    # Calculate priority score
    score = _calculate_priority(
        enforcement_type=enforcement_type,
        lead_agency=lead_agency,
        defendant_names=defendant_names,
        body=body,
        indictments=indictments,
        status=status,
    )

    return OperationInfo(
        slug=slug,
        title=title,
        aliases=aliases,
        target_entity=target_entity,
        lead_agency=lead_agency,
        enforcement_type=enforcement_type,
        status=status,
        outcome=outcome,
        timeframe_announced=timeframe_announced,
        timeframe_start=timeframe_start,
        indictments=indictments,
        body_text=body,
        case_numbers=case_numbers,
        defendant_names=defendant_names,
        priority_score=score,
    )


def _calculate_priority(
    enforcement_type: tuple[str, ...],
    lead_agency: str,
    defendant_names: tuple[str, ...],
    body: str,
    indictments: int,
    status: str,
) -> int:
    """Score operations by likelihood of findable court documents."""
    score = 0

    # +3: enforcement_type includes "indictment" or "arrest"
    enforcement_set = {e.lower().strip() for e in enforcement_type}
    if "indictment" in enforcement_set or "arrest" in enforcement_set:
        score += 3

    # +2: US lead agency
    agency_lower = lead_agency.lower().replace(" ", "-")
    if any(us in agency_lower for us in US_AGENCIES):
        score += 2

    # +2: body mentions specific defendant names
    if defendant_names:
        score += 2

    # +1: body mentions "sentenced" or "convicted"
    body_lower = body.lower()
    if "sentenced" in body_lower or "convicted" in body_lower:
        score += 1

    # +1: indictments > 0
    if indictments > 0:
        score += 1

    # -2: status is "ongoing" or "classified"
    if status.lower() in ("ongoing", "classified"):
        score -= 2

    # -1: non-Western lead agency
    if any(la in agency_lower for la in LOW_ACCESS_AGENCIES):
        score -= 1

    return score


def list_all_operation_slugs() -> list[str]:
    """List all operation slugs from wiki/operations/."""
    slugs: list[str] = []
    for f in sorted(WIKI_OPS_DIR.iterdir()):
        if f.suffix == ".md" and f.name != "_index.md":
            slugs.append(f.stem)
    return slugs


# ---------------------------------------------------------------------------
# Search query builder
# ---------------------------------------------------------------------------

def build_queries(op: OperationInfo) -> list[tuple[str, str]]:
    """Build search queries for an operation. Returns list of (label, query)."""
    queries: list[tuple[str, str]] = []

    # Exact case numbers first (highest precision)
    for cn in op.case_numbers:
        queries.append(("case_number", cn))

    # Defendant names (use full multi-word names for API queries)
    seen_queries: set[str] = set()
    for name in op.defendant_names:
        # Only query multi-word names (single surnames are too broad for API)
        if " " not in name or len(name) < 6:
            continue
        q = f'"{name}" (indictment OR sentenced OR convicted OR guilty)'
        if q not in seen_queries:
            queries.append(("defendant", q))
            seen_queries.add(q)

    # Operation name + legal terms
    clean_title = op.title.replace("--", "").replace("  ", " ").strip()
    queries.append((
        "operation_name",
        f'"{clean_title}" (indictment OR sentenced OR convicted)',
    ))

    # Aliases
    for alias in op.aliases[:3]:  # limit to 3 aliases
        clean_alias = alias.strip()
        if clean_alias and clean_alias.lower() != clean_title.lower():
            queries.append((
                "alias",
                f'"{clean_alias}" (indictment OR sentenced OR convicted)',
            ))

    # Target entity if short enough to be useful
    if op.target_entity and len(op.target_entity) < 80:
        entity_clean = re.sub(r"\(.*?\)", "", op.target_entity).strip()
        if entity_clean and entity_clean.lower() not in clean_title.lower():
            queries.append((
                "target",
                f'"{entity_clean}" cybercrime',
            ))

    # Direct operation name without legal terms (broader fallback)
    # Only if title is specific enough (not generic like "Botnet Takedown")
    title_words = [w for w in clean_title.split() if len(w) > 3]
    if len(title_words) >= 2:
        # Extract the most distinctive part of the title
        for alias in op.aliases[:2]:
            alias_clean = alias.strip()
            if len(alias_clean) > 6 and alias_clean.lower() not in clean_title.lower():
                queries.append((
                    "broad_alias",
                    f'"{alias_clean}" cybercrime court',
                ))

    return queries


# ---------------------------------------------------------------------------
# CourtListener API
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CourtDocument:
    """Immutable container for a court document result."""
    case_name: str
    court: str
    date_filed: str
    source_url: str
    snippet: str
    document_type: str
    case_number: str
    query_label: str


def _classify_document_type(text: str) -> str:
    """Classify document type from snippet/title text."""
    text_lower = text.lower()
    for doc_type, keywords in DOC_TYPE_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            return doc_type
    return "judgment"  # default


def _http_get_json(url: str, timeout: int = 30) -> dict[str, Any] | None:
    """Fetch JSON from URL with error handling."""
    req = Request(url, headers={
        "User-Agent": "CyberCrimeIC-WikiBot/1.0 (research; +https://github.com)",
        "Accept": "application/json",
    })
    try:
        with urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except HTTPError as e:
        if e.code == 429:
            raise  # let caller handle rate limit
        print(f"    [WARN] HTTP {e.code} from {url}")
        return None
    except (URLError, OSError, json.JSONDecodeError) as e:
        print(f"    [WARN] Request failed: {e}")
        return None


def _http_get_html(url: str, timeout: int = 30) -> str | None:
    """Fetch HTML from URL with error handling."""
    req = Request(url, headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml",
    })
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (HTTPError, URLError, OSError) as e:
        print(f"    [WARN] HTML fetch failed: {e}")
        return None


def search_courtlistener(
    query: str,
    query_label: str,
    date_after: str = "",
) -> list[CourtDocument]:
    """Search CourtListener API for court opinions matching query."""
    params = f"q={quote_plus(query)}&type=o&format=json&order_by=dateFiled+desc"
    if date_after:
        params += f"&filed_after={quote_plus(date_after)}"

    url = f"{COURTLISTENER_API}?{params}"
    backoff = 1

    for attempt in range(4):
        try:
            data = _http_get_json(url)
            break
        except HTTPError as e:
            if e.code == 429 and attempt < 3:
                wait = min(backoff * 2, MAX_BACKOFF)
                print(f"    [WARN] Rate limited, backing off {wait}s...")
                time.sleep(wait)
                backoff = wait
                continue
            return []
    else:
        return []

    if data is None:
        return []

    results: list[CourtDocument] = []
    for item in data.get("results", []):
        case_name = item.get("caseName", "") or item.get("case_name", "") or ""
        court = item.get("court", "") or ""
        date_filed = item.get("dateFiled", "") or item.get("date_filed", "") or ""
        abs_url = item.get("absolute_url", "") or ""
        snippet = item.get("snippet", "") or ""

        # Clean HTML from snippet
        snippet = re.sub(r"<[^>]+>", "", snippet).strip()
        snippet = html.unescape(snippet)

        # Build full URL
        if abs_url and not abs_url.startswith("http"):
            source_url = f"https://www.courtlistener.com{abs_url}"
        elif abs_url:
            source_url = abs_url
        else:
            continue

        doc_type = _classify_document_type(f"{case_name} {snippet}")
        case_num_match = CASE_NUMBER_RE.search(f"{case_name} {snippet}")
        case_number = case_num_match.group(1) if case_num_match else ""

        results.append(CourtDocument(
            case_name=case_name,
            court=court,
            date_filed=date_filed,
            source_url=source_url,
            snippet=snippet[:500],
            document_type=doc_type,
            case_number=case_number,
            query_label=query_label,
        ))

    return results


# ---------------------------------------------------------------------------
# DOJ press release PDF extraction
# ---------------------------------------------------------------------------

def extract_doj_pdfs(press_release_url: str) -> list[dict[str, str]]:
    """Extract PDF links from a DOJ press release page."""
    body = _http_get_html(press_release_url)
    if body is None:
        return []

    # Find all justice.gov PDF links
    pdf_re = re.compile(
        r'href=["\']([^"\']*justice\.gov[^"\']*\.pdf)["\']',
        re.IGNORECASE,
    )
    matches = pdf_re.findall(body)

    # Also check for relative PDF links
    rel_pdf_re = re.compile(
        r'href=["\'](/[^"\']*\.pdf)["\']',
        re.IGNORECASE,
    )
    rel_matches = rel_pdf_re.findall(body)
    for rel in rel_matches:
        full = urljoin(press_release_url, rel)
        if "justice.gov" in full and full not in matches:
            matches.append(full)

    results: list[dict[str, str]] = []
    for pdf_url in matches:
        # Try to extract doc type from URL
        url_lower = pdf_url.lower()
        doc_type = "indictment"  # default
        for dtype, keywords in DOC_TYPE_KEYWORDS.items():
            if any(kw.replace(" ", "-") in url_lower or kw.replace(" ", "_") in url_lower
                   for kw in keywords):
                doc_type = dtype
                break

        results.append({
            "pdf_url": pdf_url,
            "source_page": press_release_url,
            "document_type": doc_type,
        })

    return results


# ---------------------------------------------------------------------------
# UNODC SHERLOC search
# ---------------------------------------------------------------------------

def search_sherloc(query: str) -> list[dict[str, str]]:
    """Search UNODC SHERLOC case law database (HTML scraping)."""
    url = (
        "https://sherloc.unodc.org/cld/v3/sherloc/cldb/search.html"
        f"?q={quote_plus(query)}"
    )

    body = _http_get_html(url)
    if body is None:
        return []

    # Check for Cloudflare/bot protection
    if "Just a moment" in body or "challenge-platform" in body:
        print("    [WARN] SHERLOC returned Cloudflare challenge page")
        return []

    results: list[dict[str, str]] = []

    # Parse search results from HTML (basic regex extraction)
    # SHERLOC result items typically have case titles and links
    case_re = re.compile(
        r'<a[^>]*href=["\']([^"\']*cldb/case[^"\']*)["\'][^>]*>(.*?)</a>',
        re.IGNORECASE | re.DOTALL,
    )
    for href, case_title in case_re.findall(body):
        case_title_clean = re.sub(r"<[^>]+>", "", case_title).strip()
        case_title_clean = html.unescape(case_title_clean)
        if not case_title_clean:
            continue

        full_url = href if href.startswith("http") else urljoin(url, href)
        results.append({
            "case_name": case_title_clean,
            "source_url": full_url,
            "source": "SHERLOC",
        })

    return results


# ---------------------------------------------------------------------------
# Relevance filtering
# ---------------------------------------------------------------------------

def is_relevant(doc: CourtDocument, op: OperationInfo) -> bool:
    """Filter CourtListener results for relevance to the operation.

    CourtListener snippets are often empty, so we rely heavily on case_name
    matching against known defendants and operation terms.
    """
    combined = f"{doc.case_name} {doc.snippet}".lower()

    # If we searched by exact case number, it is almost certainly relevant
    if doc.query_label == "case_number":
        return True

    # Check for defendant name in the case title (highest signal)
    # "United States v. Ulbricht" -> matches defendant "Ulbricht"
    has_defendant_in_case = False
    for name in op.defendant_names:
        if len(name) < 4:
            continue
        if name.lower() in doc.case_name.lower():
            has_defendant_in_case = True
            break

    # If a known defendant appears in the case name of a "v." case,
    # this is almost certainly relevant (even without snippet/cyber terms)
    if has_defendant_in_case and " v. " in doc.case_name.lower():
        return True

    # Check for operation-related terms
    op_terms = [op.title.lower()]
    op_terms.extend(a.lower() for a in op.aliases)
    if op.target_entity:
        # Add significant words from target_entity
        for word in op.target_entity.lower().split():
            if len(word) > 4 and word not in ("and", "the", "from", "with"):
                op_terms.append(word)

    # At least one operation-related term must appear (use word fragments)
    has_op_term = False
    for term in op_terms:
        words = [w for w in term.split() if len(w) > 3]
        if any(w in combined for w in words):
            has_op_term = True
            break

    # Defendant name anywhere in combined text
    has_defendant = any(
        name.lower() in combined
        for name in op.defendant_names
        if len(name) > 3
    )

    # Cyber/crime terms as secondary filter
    cyber_terms = [
        "cyber", "hack", "ransomware", "malware", "botnet", "phishing",
        "fraud", "computer", "dark web", "darknet", "cryptocurrency",
        "bitcoin", "identity theft", "wire fraud", "conspiracy",
        "silk road", "narcotics", "money laundering", "forfeiture",
        "dark market", "carding", "ddos", "extortion",
    ]
    has_cyber = any(t in combined for t in cyber_terms)

    # Relevance: (operation term OR defendant) AND cyber terms
    # OR: just operation term alone if it is specific enough (>8 chars)
    if (has_op_term or has_defendant) and has_cyber:
        return True

    # Fallback: strong op_term match alone
    if has_op_term:
        for term in op_terms:
            if len(term) > 8 and term in combined:
                return True

    return False


# ---------------------------------------------------------------------------
# File output
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def make_raw_filename(doc: CourtDocument) -> str:
    """Generate raw/case-documents/ filename: YYYY-MM-DD_court_slug.md"""
    date_part = doc.date_filed or TODAY
    # Normalize date to YYYY-MM-DD
    date_part = date_part[:10]
    if len(date_part) < 10:
        date_part = TODAY

    court_slug = slugify(doc.court) if doc.court else "unknown-court"
    case_slug = slugify(doc.case_name)[:50] if doc.case_name else "unknown-case"

    return f"{date_part}_{court_slug}_{case_slug}.md"


def save_raw_document(doc: CourtDocument, operation_slug: str) -> Path:
    """Save a court document to raw/case-documents/."""
    filename = make_raw_filename(doc)
    filepath = RAW_CASE_DIR / filename

    # Avoid overwrite
    if filepath.exists():
        # Append counter
        stem = filepath.stem
        for i in range(2, 100):
            alt = RAW_CASE_DIR / f"{stem}-{i}.md"
            if not alt.exists():
                filepath = alt
                break

    content = f"""---
title: "{doc.case_name}"
court: "{doc.court}"
case_number: "{doc.case_number}"
document_type: "{doc.document_type}"
date_filed: "{doc.date_filed}"
source_url: "{doc.source_url}"
related_operation: "{operation_slug}"
collection_date: "{TODAY}"
auto_collected: true
---

## {doc.case_name}

{doc.snippet}
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


def make_case_slug(doc: CourtDocument) -> str:
    """Generate a wiki/cases/ slug from a court document."""
    name = doc.case_name
    # Remove common prefixes
    for prefix in ["United States of America", "United States", "U.S."]:
        name = name.replace(prefix, "us")
    return slugify(name)


def create_case_stub(doc: CourtDocument, operation_slug: str) -> Path | None:
    """Create a wiki/cases/ stub for a court document."""
    case_slug = make_case_slug(doc)
    filepath = WIKI_CASES_DIR / f"{case_slug}.md"

    if filepath.exists():
        return None  # Don't overwrite existing pages

    content = f"""---
type: case
title: "{doc.case_name}"
case_number: "{doc.case_number}"
jurisdiction: "{doc.court}"
jurisdiction_country: ""
case_type: "prosecution"
status: "indicted"
crime_charged: []
defendants: []
related_operation: "[[{operation_slug}]]"
ic_elements:
  mlat_requests: []
  extradition: ""
  evidence_from_abroad: []
  foreign_arrests: []
  asset_freezing: []
cooperating_agencies: []
legal_frameworks_invoked: []
mechanisms_used: []
key_legal_issues: []
precedent_value: ""
source_count: 0
sources: []
created: {TODAY}
updated: {TODAY}
---

> [!info] Stub
> This page was auto-created from CourtListener search results.
> It will be expanded when the court document is fully reviewed.

## Summary

{doc.snippet}

## Source

- [{doc.case_name}]({doc.source_url})
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

@dataclass
class RunStats:
    """Mutable run statistics (not shared across threads)."""
    operations_searched: int = 0
    documents_found: int = 0
    documents_saved: int = 0
    duplicates_skipped: int = 0
    zero_result_operations: int = 0
    errors: int = 0
    stubs_created: int = 0


def process_operation(
    op: OperationInfo,
    state: dict[str, Any],
    stats: RunStats,
    dry_run: bool = False,
    create_stubs: bool = False,
) -> list[CourtDocument]:
    """Search for court documents for a single operation."""
    print(f"\nProcessing: {op.slug} (score: {op.priority_score})")

    queries = build_queries(op)
    if not queries:
        print("  No viable search queries generated")
        stats.zero_result_operations += 1
        return []

    # Date filter: if we know when the operation started, limit search
    date_after = ""
    if op.timeframe_start and len(op.timeframe_start) >= 4:
        # Search from 1 year before operation start
        try:
            year = int(op.timeframe_start[:4])
            date_after = f"{year - 1}-01-01"
        except ValueError:
            pass

    all_results: list[CourtDocument] = []
    seen_urls: set[str] = set()

    # CourtListener searches
    for label, query in queries:
        print(f"  CourtListener [{label}]: q={query[:60]}...")
        try:
            results = search_courtlistener(query, label, date_after)
        except Exception as e:
            print(f"    [ERR] {e}")
            stats.errors += 1
            continue

        relevant = [r for r in results if is_relevant(r, op)]
        new_results = [
            r for r in relevant
            if r.source_url not in seen_urls
        ]
        for r in new_results:
            seen_urls.add(r.source_url)

        filtered_out = len(results) - len(relevant)
        deduped = len(relevant) - len(new_results)
        print(f"    {len(results)} raw -> {len(relevant)} relevant "
              f"({filtered_out} filtered, {deduped} deduped) -> {len(new_results)} new")

        all_results.extend(new_results)
        time.sleep(COURTLISTENER_DELAY)

    # SHERLOC search (if non-US operation or no CourtListener results)
    is_us_led = any(us in op.lead_agency.lower() for us in US_AGENCIES)
    if not is_us_led or not all_results:
        sherloc_query = f"{op.title} cybercrime"
        print(f"  SHERLOC: q={sherloc_query[:60]}...")
        try:
            sherloc_results = search_sherloc(sherloc_query)
            print(f"    {len(sherloc_results)} results")
            # SHERLOC results are informational only (different format)
            if sherloc_results:
                for sr in sherloc_results[:3]:
                    print(f"    -> {sr.get('case_name', 'N/A')}")
        except Exception as e:
            print(f"    [ERR] SHERLOC: {e}")
        time.sleep(SHERLOC_DELAY)

    stats.documents_found += len(all_results)

    if not all_results:
        stats.zero_result_operations += 1
        print("  No relevant court documents found")
    else:
        # Save or report results
        for doc in all_results:
            # Check for duplicates in state
            if is_duplicate_doc(state, doc.source_url):
                stats.duplicates_skipped += 1
                print(f"    [SKIP] Duplicate: {doc.case_name[:50]}")
                continue

            print(f"    [{doc.document_type}] {doc.case_name[:60]} "
                  f"({doc.court}, {doc.date_filed})")

            if not dry_run:
                try:
                    filepath = save_raw_document(doc, op.slug)
                    record_document(state, {
                        "source_url": doc.source_url,
                        "case_name": doc.case_name,
                        "operation": op.slug,
                        "saved_to": str(filepath.relative_to(PROJECT_ROOT)),
                        "date": TODAY,
                    })
                    stats.documents_saved += 1
                    print(f"      -> Saved: {filepath.name}")

                    if create_stubs:
                        stub_path = create_case_stub(doc, op.slug)
                        if stub_path:
                            stats.stubs_created += 1
                            print(f"      -> Stub: {stub_path.name}")
                except Exception as e:
                    print(f"      [ERR] Save failed: {e}")
                    stats.errors += 1
            else:
                print(f"      (dry-run, not saving)")

    stats.operations_searched += 1
    if not dry_run:
        mark_searched(state, op.slug, len(all_results))

    return all_results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search for court documents related to wiki operations.",
    )
    parser.add_argument(
        "--slug", type=str, default="",
        help="Process a single operation by slug",
    )
    parser.add_argument(
        "--top", type=int, default=0,
        help="Process top N operations by priority score",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Search without saving files",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Ignore 30-day cooldown for re-searching",
    )
    parser.add_argument(
        "--create-stubs", action="store_true",
        help="Create wiki/cases/ stub pages for found documents",
    )
    parser.add_argument(
        "--doj-url", type=str, default="",
        help="Extract PDF links from a DOJ press release URL",
    )
    args = parser.parse_args()

    start_time = datetime.now()
    print(f"=== Court Document Collector === {start_time.isoformat()}")

    # DOJ PDF extraction mode
    if args.doj_url:
        print(f"\nExtracting PDFs from DOJ press release: {args.doj_url}")
        pdfs = extract_doj_pdfs(args.doj_url)
        if pdfs:
            for p in pdfs:
                print(f"  [{p['document_type']}] {p['pdf_url']}")
        else:
            print("  No PDFs found")
        return

    state = load_state()

    # Determine which operations to process
    if args.slug:
        slugs = [args.slug]
        print(f"Single operation mode: {args.slug}")
    else:
        all_slugs = list_all_operation_slugs()
        print(f"Loaded {len(all_slugs)} operations", end="")

        if args.top > 0:
            # Load all and sort by priority
            print(f" (scoring for top {args.top}...)")
            ops_with_scores: list[tuple[int, str]] = []
            for s in all_slugs:
                op = load_operation(s)
                if op:
                    ops_with_scores.append((op.priority_score, s))
            ops_with_scores.sort(key=lambda x: x[0], reverse=True)
            slugs = [s for _, s in ops_with_scores[:args.top]]

            print(f"\nTop {len(slugs)} by priority score:")
            for score, s in ops_with_scores[:args.top]:
                print(f"  {score:+3d}  {s}")
        else:
            print(" (processing all)")
            slugs = all_slugs

    stats = RunStats()
    skipped_cooldown = 0

    for slug in slugs:
        # Cooldown check
        if not args.force and is_recently_searched(state, slug):
            skipped_cooldown += 1
            continue

        op = load_operation(slug)
        if op is None:
            print(f"\n[WARN] Could not load operation: {slug}")
            continue

        try:
            process_operation(
                op, state, stats,
                dry_run=args.dry_run,
                create_stubs=args.create_stubs,
            )
        except KeyboardInterrupt:
            print("\n\n[INTERRUPTED] Saving state...")
            if not args.dry_run:
                save_state(state)
            break
        except Exception as e:
            print(f"\n[ERR] Failed processing {slug}: {e}")
            traceback.print_exc()
            stats.errors += 1

    # Save state
    if not args.dry_run:
        save_state(state)
        print(f"\nState saved to {STATE_FILE}")

    # Summary
    elapsed = datetime.now() - start_time
    print(f"\n=== Results ===")
    print(f"  Operations searched: {stats.operations_searched}")
    if skipped_cooldown:
        print(f"  Skipped (cooldown):  {skipped_cooldown}")
    print(f"  Documents found:     {stats.documents_found}")
    if not args.dry_run:
        print(f"  Documents saved:     {stats.documents_saved}")
    print(f"  Duplicates skipped:  {stats.duplicates_skipped}")
    print(f"  Zero-result ops:     {stats.zero_result_operations}")
    if stats.stubs_created:
        print(f"  Case stubs created:  {stats.stubs_created}")
    if stats.errors:
        print(f"  Errors:              {stats.errors}")
    print(f"  Elapsed:             {elapsed.total_seconds():.1f}s")

    if args.dry_run:
        print("\n  (dry-run mode -- no files written)")


if __name__ == "__main__":
    main()
