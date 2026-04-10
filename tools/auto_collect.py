"""
자동 수집 스크립트 — 사이버범죄 국제공조 관련 기사·보고서·문헌
Windows Task Scheduler 또는 cron으로 주기 실행.

주요 기능:
1. RSS/Atom 피드 수집 (Europol, INTERPOL, DOJ, NCSC, CISA, ENISA, KISA 등)
2. 학술 데이터베이스 검색 (OpenAlex API)
3. 강화된 IC-relevance 필터 (cyber AND international 양 조건)
4. 5-point match 사전 중복 검사 (기존 위키 작전 인덱스 대조)
5. 불확실한 항목은 _workspace/review_queue.md로 라우팅 (사용자 인터뷰 대상)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import quote
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "raw"
PENDING_DIR = PROJECT_ROOT / "_pending"
WIKI_DIR = PROJECT_ROOT / "wiki"
STATE_FILE = PROJECT_ROOT / "tools" / ".collect_state.json"
REVIEW_QUEUE = PROJECT_ROOT / "_workspace" / "review_queue.md"

# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------

# RSS/Atom feeds
FEEDS: list[dict[str, str]] = [
    # Tier A — 1차 출처: 공식 법집행기관
    {
        "name": "Europol News",
        "url": "https://www.europol.europa.eu/rss.xml",
        "domain": "europol.europa.eu",
        "publisher": "Europol",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "INTERPOL News",
        "url": "https://www.interpol.int/en/RSS/News",
        "domain": "interpol.int",
        "publisher": "INTERPOL",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "DOJ Cybercrime",
        "url": "https://www.justice.gov/news/rss?topic=cybercrime",
        "domain": "justice.gov",
        "publisher": "US DOJ",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "FBI National Press Releases",
        "url": "https://www.fbi.gov/feeds/national-press-releases/rss.xml",
        "domain": "fbi.gov",
        "publisher": "FBI",
        "type": "press-releases",
        "reliability": "A",
    },
    {
        "name": "Eurojust Press Releases",
        "url": "https://www.eurojust.europa.eu/news/press-releases/feed",
        "domain": "eurojust.europa.eu",
        "publisher": "Eurojust",
        "type": "press-releases",
        "reliability": "A",
    },
    # Tier A — 정부 사이버 보안 기관 (공조/정책 관점)
    {
        "name": "CISA Cybersecurity Advisories",
        "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
        "domain": "cisa.gov",
        "publisher": "CISA",
        "type": "government-reports",
        "reliability": "A",
    },
    {
        "name": "NCSC UK News",
        "url": "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",
        "domain": "ncsc.gov.uk",
        "publisher": "NCSC UK",
        "type": "government-reports",
        "reliability": "A",
    },
    {
        "name": "ENISA News",
        "url": "https://www.enisa.europa.eu/front-page/RSS",
        "domain": "enisa.europa.eu",
        "publisher": "ENISA",
        "type": "government-reports",
        "reliability": "A",
    },
    # Tier B — 보안 연구소·뉴스
    {
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/",
        "domain": "bleepingcomputer.com",
        "publisher": "BleepingComputer",
        "type": "news",
        "reliability": "C",
    },
    {
        "name": "The Record (Recorded Future)",
        "url": "https://therecord.media/feed/",
        "domain": "therecord.media",
        "publisher": "The Record",
        "type": "news",
        "reliability": "B",
    },
    {
        "name": "The Hacker News",
        "url": "https://feeds.feedburner.com/TheHackersNews",
        "domain": "thehackernews.com",
        "publisher": "The Hacker News",
        "type": "news",
        "reliability": "C",
    },
]

# OpenAlex API queries (academic literature)
# https://api.openalex.org/works?search=...&filter=publication_year:2024-2026
OPENALEX_QUERIES = [
    "cybercrime international cooperation",
    "Budapest Convention cybercrime ratification",
    "ransomware multinational law enforcement operation",
    "MLAT mutual legal assistance cybercrime",
    "transnational cybercrime joint investigation",
]

# ---------------------------------------------------------------------------
# IC Relevance Filter — 사이버 + 국제공조 양 조건 필터
# ---------------------------------------------------------------------------

CYBER_KEYWORDS = [
    "cyber", "cybercrime", "cyber-crime", "cyberattack", "cyber-attack",
    "ransomware", "malware", "phishing", "spear phishing", "smishing",
    "bec ", "business email compromise", "voice phishing", "vishing",
    "hack", "hacking", "hacker", "intrusion", "data breach",
    "stolen data", "credential theft", "darknet", "dark web", "darkweb",
    "ddos", "botnet", "infostealer", "ransom note", "crypto-jacking",
    "online fraud", "online scam", "investment scam",
    "cryptocurrency", "crypto theft", "bitcoin", "cryptomixer", "mixer",
    "online child sexual abuse", "csam", "child sexual abuse material",
    "online exploitation", "child exploitation",
    "digital evidence", "computer fraud", "computer misuse",
    "deepfake", "synthetic media",
    "encryption", "encrypted communications",
]

IC_KEYWORDS = [
    "international operation", "joint operation", "coordinated operation",
    "multinational operation", "multi-country", "cross-border",
    "law enforcement cooperation", "international cooperation",
    "interpol", "europol", "eurojust", "afripol", "aseanapol",
    "mlat", "mutual legal assistance", "extradition", "joint investigation",
    "joint investigation team", "jit", "international takedown",
    "global takedown", "global operation", "worldwide operation",
    "cross-border cooperation", "transnational",
    "budapest convention", "council of europe convention",
    "indictment of foreign", "extradited from", "extradited to",
    "24/7 network", "csam coalition",
]

# Hard-exclude: clearly non-cyber crime types
HARD_EXCLUDE_KEYWORDS = [
    "migrant smuggling", "migrant-smuggling", "human smuggling",
    "drug trafficking", "narcotics", "cocaine", "heroin", "cannabis",
    "weapons trafficking", "firearms trafficking", "gun trafficking",
    "money laundering",  # often non-cyber; exclude unless cyber kw also present
    "wildlife trafficking", "antiquities",
    "terrorism financing",  # unless cyber kw present
    "cigarette smuggling", "tobacco smuggling",
]

# Soft-exclude: usually noise but acceptable if combined with strong IC + cyber signal
SOFT_EXCLUDE_KEYWORDS = [
    "training", "workshop", "webinar", "conference announcement",
    "appointment", "job vacancy", "job posting",
]

# Policy advocacy markers — sources containing these without operational substance
# are policy/opinion pieces, not operations. The wiki indexes by operations,
# so policy-only items are rejected. Learned from rejection of Q0001 (Europol
# De Bolle CSAM statement, 2026-04-10).
POLICY_ADVOCACY_MARKERS = [
    "advocates", "advocacy", "urges", "calls for",
    "legal vacuum", "risk of removing", "would have far-reaching",
    "expresses concern", "position paper", "policy brief",
    "statement by", "statement of",
]

OPERATIONAL_MARKERS = [
    "arrest", "arrested", "indicted", "indictment",
    "seized", "seizure", "takedown", "dismantled",
    "extradition", "extradited", "raid", "raided",
    "convicted", "sentenced", "infrastructure seized",
    "domains seized", "servers seized", "victims rescued",
    "operation ", "joint investigation team",
]

# Data-privacy-heavy keywords — for academic sources that drift into data
# protection compliance rather than operational cybercrime cooperation.
# Learned from rejection of Q0002 (Khan systematic review, 2026-04-10).
DATA_PRIVACY_HEAVY = [
    "data privacy", "data protection", "gdpr",
    "personal data", "compliance framework",
    "standard contractual clauses", "binding corporate rules",
    "privacy law", "data subject rights",
]

INVESTIGATIVE_MARKERS = [
    "investigation", "prosecution", "joint operation",
    "mlat", "mutual legal assistance",
    "extradition", "criminal prosecution",
    "law enforcement cooperation", "police cooperation",
    "joint investigation team",
]


def is_ic_relevant(title: str, description: str) -> tuple[bool, str]:
    """Return (is_relevant, reason).

    Strict policy:
      1. MUST contain at least one CYBER keyword
      2. MUST contain at least one IC keyword OR be from Tier A cyber agency
      3. MUST NOT contain any HARD_EXCLUDE keyword without an overriding cyber+IC signal
    """
    text = f"{title} {description}".lower()

    # Hard exclude — drop unless very strong cyber signal AND strong IC signal
    if any(kw in text for kw in HARD_EXCLUDE_KEYWORDS):
        cyber_count = sum(1 for kw in CYBER_KEYWORDS if kw in text)
        ic_count = sum(1 for kw in IC_KEYWORDS if kw in text)
        if not (cyber_count >= 2 and ic_count >= 1):
            return False, "hard_excluded"

    cyber_hits = [kw for kw in CYBER_KEYWORDS if kw in text]
    ic_hits = [kw for kw in IC_KEYWORDS if kw in text]

    if not cyber_hits:
        return False, "no_cyber_keyword"
    if not ic_hits:
        return False, "no_ic_keyword"

    # Soft exclude — require both cyber and IC strongly present
    if any(kw in text for kw in SOFT_EXCLUDE_KEYWORDS):
        if len(cyber_hits) < 2 or len(ic_hits) < 2:
            return False, "soft_excluded"

    # Policy advocacy filter (learned from Q0001 rejection 2026-04-10):
    # If text contains policy-advocacy markers without any operational marker,
    # it is opinion/policy not an operation. Reject.
    has_policy = any(kw in text for kw in POLICY_ADVOCACY_MARKERS)
    has_operational = any(kw in text for kw in OPERATIONAL_MARKERS)
    if has_policy and not has_operational:
        return False, "policy_no_operations"

    # Data-privacy academic drift filter (learned from Q0002 rejection 2026-04-10):
    # If text is heavy on data privacy / compliance concepts but lacks
    # investigative markers, it is data-protection scholarship not cybercrime
    # IC. Reject.
    privacy_hits = sum(1 for kw in DATA_PRIVACY_HEAVY if kw in text)
    investigative_hits = sum(1 for kw in INVESTIGATIVE_MARKERS if kw in text)
    if privacy_hits >= 2 and investigative_hits == 0:
        return False, "data_privacy_drift"

    return True, f"cyber={len(cyber_hits)} ic={len(ic_hits)}"


# ---------------------------------------------------------------------------
# Pre-dedup against existing wiki operations index
# ---------------------------------------------------------------------------

def load_existing_operation_titles() -> set[str]:
    """Return a set of normalized title tokens from wiki/operations/*.md."""
    titles: set[str] = set()
    ops_dir = WIKI_DIR / "operations"
    if not ops_dir.exists():
        return titles
    for md in ops_dir.glob("*.md"):
        if md.name.startswith("_"):
            continue
        try:
            content = md.read_text(encoding="utf-8")
        except Exception:
            continue
        # Extract title from frontmatter
        m = re.search(r'^title:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        if m:
            titles.add(_normalize(m.group(1)))
        # Also use slug
        titles.add(_normalize(md.stem))
    return titles


def _normalize(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def likely_duplicate(title: str, existing_titles: set[str]) -> bool:
    """Cheap pre-dedup: check title token overlap (>=3 distinctive tokens)."""
    norm = _normalize(title)
    tokens = [t for t in norm.split() if len(t) > 3]
    if not tokens:
        return False
    distinctive = set(tokens) - {
        "operation", "police", "international", "cyber", "joint",
        "world", "global", "europe", "europol", "interpol", "doj",
        "with", "from", "their", "after", "into", "this", "that",
    }
    if len(distinctive) < 2:
        return False
    for existing in existing_titles:
        existing_tokens = set(existing.split())
        if len(distinctive & existing_tokens) >= 2:
            return True
    return False


# ---------------------------------------------------------------------------
# Feed parsing
# ---------------------------------------------------------------------------

def load_state() -> dict[str, Any]:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"seen_urls": [], "last_run": None}


def save_state(state: dict[str, Any]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def fetch_url(url: str, timeout: int = 15) -> str | None:
    try:
        req = Request(url, headers={
            "User-Agent": (
                "Mozilla/5.0 (Cyber-crime-IC wiki bot) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
            ),
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        })
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, TimeoutError) as e:
        print(f"  WARN: Failed to fetch {url}: {e}")
        return None


def parse_feed_items(xml_text: str) -> list[dict[str, str]]:
    items = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return items

    # RSS 2.0
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        desc = (item.findtext("description") or "").strip()
        # strip HTML tags from description for cleaner filtering
        desc = re.sub(r"<[^>]+>", " ", desc)
        pub_date = (item.findtext("pubDate") or "").strip()
        if title and link:
            items.append({
                "title": title,
                "link": link,
                "description": desc,
                "pub_date": pub_date,
            })

    # Atom
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall(".//atom:entry", ns):
        title = (entry.findtext("atom:title", namespaces=ns) or "").strip()
        link_el = entry.find("atom:link[@rel='alternate']", ns)
        if link_el is None:
            link_el = entry.find("atom:link", ns)
        link = link_el.get("href", "") if link_el is not None else ""
        desc = (entry.findtext("atom:summary", namespaces=ns) or "").strip()
        desc = re.sub(r"<[^>]+>", " ", desc)
        pub_date = (entry.findtext("atom:published", namespaces=ns) or "").strip()
        if title and link:
            items.append({
                "title": title,
                "link": link,
                "description": desc,
                "pub_date": pub_date,
            })

    return items


# ---------------------------------------------------------------------------
# OpenAlex academic search
# ---------------------------------------------------------------------------

def fetch_openalex(query: str, max_results: int = 5) -> list[dict[str, str]]:
    """Fetch academic works matching the query from OpenAlex API.

    OpenAlex is a free, comprehensive academic database (~250M works).
    No API key required. Polite pool: include mailto in User-Agent.
    """
    from datetime import date
    last_year = date.today().year - 1
    url = (
        f"https://api.openalex.org/works"
        f"?search={quote(query)}"
        f"&filter=publication_year:{last_year}-{date.today().year}"
        f"&per-page={max_results}"
        f"&sort=cited_by_count:desc"
    )
    text = fetch_url(url)
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    items = []
    for w in data.get("results", []):
        title = w.get("title", "")
        doi = w.get("doi", "")
        publish_date = w.get("publication_date", "")
        # Build a "description" from concepts and abstract
        concepts = ", ".join(c.get("display_name", "") for c in w.get("concepts", [])[:5])
        # OpenAlex returns abstract as inverted index — reconstruct
        abstract_idx = w.get("abstract_inverted_index") or {}
        if abstract_idx:
            max_pos = max((max(positions) for positions in abstract_idx.values()), default=0)
            words = [""] * (max_pos + 1)
            for word, positions in abstract_idx.items():
                for p in positions:
                    if 0 <= p < len(words):
                        words[p] = word
            abstract = " ".join(w for w in words if w)[:500]
        else:
            abstract = ""
        items.append({
            "title": title,
            "link": doi or w.get("id", ""),
            "description": f"{concepts}. {abstract}",
            "pub_date": publish_date,
        })
    return items


# ---------------------------------------------------------------------------
# Save helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text[:60].strip("-")


def save_pending(item: dict[str, str], feed: dict[str, str], reason: str) -> Path:
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(item["title"])
    filename = f"{today}_{feed['publisher'].lower().replace(' ', '-')}_{slug}.md"

    content = f"""---
title: "{item['title']}"
collection_source: "{feed['name']}"
collection_url: "{item['link']}"
collection_domain: "{feed['domain']}"
collection_date: "{today}"
publish_date: "{item.get('pub_date', today)}"
publisher: "{feed['publisher']}"
reliability: "{feed['reliability']}"
language: "en"
status: "pending"
auto_collected: true
filter_reason: "{reason}"
---

## {item['title']}

{item.get('description', '(본문을 가져오지 못했습니다. 파이프라인 실행 시 WebFetch로 보완 필요.)')}

---
*자동 수집됨. 파이프라인(`/ic-pipeline` 또는 `/ic-update`)을 실행하여 분류·평가·통합하세요.*
"""

    out_dir = PENDING_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    out_path.write_text(content, encoding="utf-8")

    raw_subdir = RAW_DIR / feed["type"]
    raw_subdir.mkdir(parents=True, exist_ok=True)
    (raw_subdir / filename).write_text(content, encoding="utf-8")

    return out_path


def append_review_queue(items: list[dict[str, Any]]) -> None:
    """Append uncertain items to the review queue for user interview."""
    if not items:
        return
    REVIEW_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    new_block = [f"\n## Batch — {timestamp}\n"]
    new_block.append("These items were collected but flagged as uncertain. Please review:\n")
    for i, it in enumerate(items, 1):
        new_block.append(f"### {i}. {it['title']}")
        new_block.append(f"- **Source**: {it['source']}")
        new_block.append(f"- **URL**: {it['url']}")
        new_block.append(f"- **Reason flagged**: {it['reason']}")
        new_block.append(f"- **Pre-dedup match**: {it.get('dup_hint', 'none')}")
        new_block.append(f"- **Decision needed**: {it.get('question', 'Is this cybercrime international cooperation?')}")
        new_block.append("- [ ] Approve  [ ] Reject  [ ] Need more info\n")

    existing = REVIEW_QUEUE.read_text(encoding="utf-8") if REVIEW_QUEUE.exists() else (
        "# Review Queue — Cybercrime IC Auto-Collection\n\n"
        "Uncertain items collected by `tools/auto_collect.py`. "
        "Resolve each item before running the integration pipeline.\n"
    )
    REVIEW_QUEUE.write_text(existing + "\n".join(new_block) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"=== IC Wiki Auto Collector === {datetime.now().isoformat()}")

    state = load_state()
    seen_urls = set(state.get("seen_urls", []))
    existing_op_titles = load_existing_operation_titles()
    print(f"  Loaded {len(existing_op_titles)} existing operation titles for pre-dedup")

    accepted: list[tuple[dict[str, str], dict[str, str], str]] = []
    review_items: list[dict[str, Any]] = []
    rejected_count = 0

    # --- RSS feeds ---
    for feed in FEEDS:
        print(f"\nFetching: {feed['name']}")
        xml_text = fetch_url(feed["url"])
        if not xml_text:
            continue

        items = parse_feed_items(xml_text)
        print(f"  Found {len(items)} items")

        for item in items:
            if item["link"] in seen_urls:
                continue
            relevant, reason = is_ic_relevant(item["title"], item.get("description", ""))
            if not relevant:
                rejected_count += 1
                seen_urls.add(item["link"])
                continue
            # Pre-dedup against existing operations
            if likely_duplicate(item["title"], existing_op_titles):
                # Send to review queue for user confirmation
                review_items.append({
                    "title": item["title"],
                    "source": feed["name"],
                    "url": item["link"],
                    "reason": reason,
                    "dup_hint": "Title overlap with existing operation",
                    "question": "Is this a new phase/development of an existing operation, or a duplicate?",
                })
                seen_urls.add(item["link"])
                continue
            accepted.append((item, feed, reason))
            seen_urls.add(item["link"])

    # --- OpenAlex academic search ---
    print("\n--- Academic search (OpenAlex) ---")
    for query in OPENALEX_QUERIES:
        print(f"  Query: {query}")
        academic = fetch_openalex(query, max_results=3)
        for item in academic:
            if item["link"] in seen_urls or not item["link"]:
                continue
            relevant, reason = is_ic_relevant(item["title"], item.get("description", ""))
            if not relevant:
                rejected_count += 1
                seen_urls.add(item["link"])
                continue
            feed = {
                "name": "OpenAlex",
                "url": "https://openalex.org",
                "domain": "openalex.org",
                "publisher": "OpenAlex Academic",
                "type": "academic-papers",
                "reliability": "B",
            }
            accepted.append((item, feed, reason))
            seen_urls.add(item["link"])

    # --- Save accepted items ---
    print(f"\n=== Results ===")
    print(f"  Rejected by filter: {rejected_count}")
    print(f"  Sent to review queue: {len(review_items)}")
    print(f"  Accepted as new pending: {len(accepted)}")

    if accepted:
        print(f"\nAccepted items:")
        for item, feed, reason in accepted:
            path = save_pending(item, feed, reason)
            print(f"  + [{feed['publisher']}] {item['title'][:70]}")
            print(f"      {path.name}")

    if review_items:
        append_review_queue(review_items)
        print(f"\n  Review queue updated: {REVIEW_QUEUE}")

    state["seen_urls"] = list(seen_urls)[-2000:]
    state["last_run"] = datetime.now().isoformat()
    save_state(state)

    if accepted:
        print(f"\n>>> Run '/ic-update' or '/ic-pipeline' in Claude Code to process pending items.")
    if review_items:
        print(f">>> Review queue at {REVIEW_QUEUE.relative_to(PROJECT_ROOT)} needs user attention.")


if __name__ == "__main__":
    main()
