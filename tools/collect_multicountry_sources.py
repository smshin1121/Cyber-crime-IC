from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

import frontmatter

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from stealth_fetch import SmartFetcher


ROOT = Path(__file__).resolve().parent.parent
SURVEY_JSON = ROOT / "wiki" / "analysis" / "multicountry-low-source-survey-2026-04-22.json"
RAW_DIR = ROOT / "raw" / "press-releases"
SOURCES_DIR = ROOT / "wiki" / "sources"
OPS_DIR = ROOT / "wiki" / "operations"
TODAY = "2026-04-23"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
SEARCH_ENGINES = ("bing", "ddg")


@dataclass
class SearchHit:
    url: str
    title: str
    snippet: str
    source_engine: str


@dataclass(frozen=True)
class OperationProfile:
    slug: str
    title: str
    aliases: list[str]
    phrases: list[str]
    token_sets: list[list[str]]


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def normalize_url(url: str) -> str:
    parts = urlsplit(url)
    return f"{parts.scheme}://{parts.netloc}{parts.path}"


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_phrase(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def significant_tokens(text: str) -> list[str]:
    stop = {"operation", "phase", "the", "and", "of", "on", "in", "for", "ii", "iii", "iv", "v", "vi"}
    return [tok for tok in normalize_phrase(text).split() if len(tok) >= 4 and tok not in stop]


def existing_urls() -> set[str]:
    urls: set[str] = set()
    for folder in (RAW_DIR, SOURCES_DIR):
        for path in folder.glob("*.md"):
            if path.name.startswith("_"):
                continue
            try:
                meta = frontmatter.load(path).metadata
            except Exception:
                continue
            for key in ("collection_url", "source_url"):
                url = str(meta.get(key) or "").strip()
                if url:
                    urls.add(normalize_url(url))
    return urls


def load_survey() -> list[dict[str, Any]]:
    data = json.loads(SURVEY_JSON.read_text(encoding="utf-8"))
    return list(data["operations"])


def load_operation_profile(op_slug: str) -> OperationProfile:
    path = OPS_DIR / f"{op_slug}.md"
    post = frontmatter.load(path)
    title = str(post.metadata.get("title") or op_slug)
    aliases = [str(v) for v in (post.metadata.get("aliases") or []) if str(v).strip()]
    phrases: list[str] = []
    for raw in [title, *aliases, op_slug.replace("-", " ")]:
        phrase = normalize_phrase(raw)
        if phrase and phrase not in phrases:
            phrases.append(phrase)
    token_sets: list[list[str]] = []
    for phrase in phrases:
        tokens = significant_tokens(phrase)
        if tokens and tokens not in token_sets:
            token_sets.append(tokens)
    return OperationProfile(
        slug=op_slug,
        title=title,
        aliases=aliases,
        phrases=phrases,
        token_sets=token_sets,
    )


def allowed_domains(op: dict[str, Any]) -> set[str]:
    domains: set[str] = set()
    for items in op.get("target_domains", {}).values():
        for domain in items:
            domains.add(str(domain).lower())
    for source in (
        "europol.europa.eu",
        "eurojust.europa.eu",
        "interpol.int",
        "coe.int",
        "arxiv.org",
        "usenix.org",
        "dl.acm.org",
    ):
        domains.add(source)
    return domains


def extract_publish_date(text: str, url: str) -> str:
    patterns = [
        re.search(r"(20\d{2})[-/](\d{2})[-/](\d{2})", text),
        re.search(r"/(20\d{2})/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/", url),
    ]
    for match in patterns:
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    year_match = re.search(r"(20\d{2})", text)
    if year_match:
        return f"{year_match.group(1)}-01-01"
    return TODAY


def request_text(url: str, *, timeout: int = 30) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def search_bing(query: str) -> list[SearchHit]:
    url = f"https://www.bing.com/search?format=rss&q={quote(query)}&setlang=en-US&cc=us"
    text = request_text(url)
    hits: list[SearchHit] = []
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return hits
    for item in root.findall(".//item"):
        link = clean_text(item.findtext("link") or "")
        title = clean_text(item.findtext("title") or "")
        snippet = clean_text(item.findtext("description") or "")
        if not link or not title:
            continue
        hits.append(SearchHit(url=link, title=title, snippet=snippet, source_engine="bing"))
        if len(hits) >= 8:
            break
    return hits


def search_ddg(query: str) -> list[SearchHit]:
    url = f"https://html.duckduckgo.com/html/?q={quote(query)}"
    text = request_text(url)
    hits: list[SearchHit] = []
    pattern = re.compile(
        r'<a[^>]+class="result__a"[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>.*?(?:<a[^>]+class="result__snippet".*?>(.*?)</a>|<div class="result__snippet">(.*?)</div>)?',
        re.S,
    )
    for match in pattern.finditer(text):
        snippet = match.group(3) or match.group(4) or ""
        hits.append(
            SearchHit(
                url=html.unescape(match.group(1)),
                title=clean_text(match.group(2)),
                snippet=clean_text(snippet),
                source_engine="ddg",
            )
        )
        if len(hits) >= 5:
            break
    return hits


def run_search(query: str) -> list[SearchHit]:
    for engine in SEARCH_ENGINES:
        try:
            if engine == "bing":
                hits = search_bing(query)
            else:
                hits = search_ddg(query)
        except Exception:
            continue
        if hits:
            return hits
    return []


def domain_allowed(url: str, allow: set[str]) -> bool:
    host = urlsplit(url).netloc.lower().removeprefix("www.")
    return any(host == domain or host.endswith("." + domain) for domain in allow)


def fetch_summary(url: str, fallback: str) -> str:
    fetcher = SmartFetcher(enable_camoufox=False)
    result = None
    try:
        result = fetcher.fetch(url, timeout=15)
    except Exception:
        result = None
    body = result.body if result else ""
    if not body:
        # Jina fallback for metadata extraction.
        try:
            jina_url = f"https://r.jina.ai/http://{urlsplit(url).netloc}{urlsplit(url).path}"
            body = request_text(jina_url, timeout=20)
        except Exception:
            body = ""
    if not body:
        return fallback

    title_match = re.search(r"<title>(.*?)</title>", body, re.I | re.S)
    desc_match = re.search(
        r'<meta[^>]+(?:name="description"|property="og:description")[^>]+content="([^"]+)"',
        body,
        re.I,
    )
    summary = clean_text(desc_match.group(1)) if desc_match else ""
    if not summary:
        text = clean_text(body)
        summary = text[:500]
    if title_match and fallback and fallback.lower() not in summary.lower():
        return f"{clean_text(title_match.group(1))}. {summary[:420]}".strip()
    return summary[:500] or fallback


def hit_relevant(op_profile: OperationProfile, hit: SearchHit, summary: str) -> bool:
    hay = normalize_phrase(" ".join([hit.title, hit.snippet, summary, hit.url]))
    for phrase in op_profile.phrases:
        if phrase and phrase in hay:
            return True
    for tokens in op_profile.token_sets:
        if len(tokens) >= 2 and sum(1 for token in tokens if token in hay) >= 2:
            return True
        if len(tokens) == 1 and tokens[0] in hay and len(tokens[0]) >= 7:
            return True
    return False


def publisher_from_url(url: str) -> str:
    host = urlsplit(url).netloc.lower().removeprefix("www.")
    mapping = {
        "europol.europa.eu": "Europol",
        "eurojust.europa.eu": "Eurojust",
        "interpol.int": "INTERPOL",
        "coe.int": "Council of Europe",
        "bka.de": "BKA",
        "bsi.bund.de": "BSI",
        "nationalcrimeagency.gov.uk": "UK National Crime Agency",
        "politie.nl": "Dutch Police",
        "om.nl": "Dutch Public Prosecution Service",
        "npa.go.jp": "Japan National Police Agency",
        "police.go.kr": "Korean National Police Agency",
        "spo.go.kr": "Supreme Prosecutors' Office of Korea",
        "rcmp-grc.gc.ca": "Royal Canadian Mounted Police",
    }
    for domain, publisher in mapping.items():
        if host == domain or host.endswith("." + domain):
            return publisher
    return host


def save_pair(op_slug: str, hit: SearchHit, summary: str) -> str | None:
    publish_date = extract_publish_date(f"{hit.title} {hit.snippet}", hit.url)
    host = urlsplit(hit.url).netloc.lower().removeprefix("www.").replace(".", "-")
    slug = f"{publish_date}_{host}_{slugify(hit.title)[:90]}".strip("-")
    raw_path = RAW_DIR / f"{slug}.md"
    source_path = SOURCES_DIR / f"{slug}.md"
    if raw_path.exists() or source_path.exists():
        return None

    publisher = publisher_from_url(hit.url)
    raw_post = frontmatter.Post(
        {
            "title": hit.title,
            "collection_source": publisher,
            "collection_url": hit.url,
            "collection_domain": urlsplit(hit.url).netloc.lower(),
            "collection_date": TODAY,
            "publish_date": publish_date,
            "language": "en",
            "status": "collected",
            "related_operation": op_slug,
        },
        f"## Summary\n\n{summary}\n",
    )
    raw_path.write_text(frontmatter.dumps(raw_post), encoding="utf-8")

    source_post = frontmatter.Post(
        {
            "type": "source",
            "title": hit.title,
            "raw_path": f"raw/press-releases/{slug}.md",
            "source_type": "web-reference",
            "publisher": publisher,
            "author": "",
            "publish_date": publish_date,
            "ingest_date": TODAY,
            "language": "en",
            "reliability": "high" if any(token in publisher.lower() for token in ("police", "agency", "europol", "interpol", "eurojust", "bka", "prosecution", "council")) else "medium",
            "credibility": "confirmed",
            "sensitivity": "public",
            "pages_updated": [op_slug],
            "key_findings": [summary or hit.snippet or hit.title],
            "collection_url": hit.url,
            "created": TODAY,
        },
        (
            "## Source Summary\n\n"
            f"{summary or hit.snippet or hit.title}\n\n"
            "## Relevance to IC\n\n"
            f"This source was collected from the multi-country low-source survey for [[{op_slug}]]."
        ),
    )
    source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")
    return slug


def parse_existing_sources(op_path: Path) -> list[str]:
    post = frontmatter.load(op_path)
    values = post.metadata.get("sources") or []
    if isinstance(values, str):
        values = [values]
    out: list[str] = []
    for value in values:
        text = str(value).strip()
        if text.startswith("[[") and text.endswith("]]"):
            text = text[2:-2].split("|", 1)[0].strip()
        if text:
            out.append(text)
    return out


def replace_references(content: str, source_slugs: list[str]) -> str:
    lines = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    for idx, slug in enumerate(source_slugs, start=1):
        source_path = SOURCES_DIR / f"{slug}.md"
        if not source_path.exists():
            continue
        meta = frontmatter.load(source_path).metadata
        title = str(meta.get("title") or slug).replace("|", " ")
        publisher = str(meta.get("publisher") or "Unknown").replace("|", " ")
        date = str(meta.get("publish_date") or "Unknown").replace("|", " ")
        url = str(meta.get("collection_url") or "").replace("|", "%7C")
        lines.append(f"| [{idx}] | {title} | {publisher} | {date} | {url} |")
    new_block = "\n".join(lines) + "\n"

    marker = "\n## References"
    idx = content.find(marker)
    if idx != -1:
        return content[:idx].rstrip() + "\n\n" + new_block
    if content.startswith("## References"):
        return new_block
    return content.rstrip() + "\n\n" + new_block


def update_operation(op_slug: str, new_source_slugs: list[str], dry_run: bool) -> None:
    op_path = OPS_DIR / f"{op_slug}.md"
    if not op_path.exists():
        return
    post = frontmatter.load(op_path)
    existing = parse_existing_sources(op_path)
    combined: list[str] = []
    for slug in existing + new_source_slugs:
        if slug and slug not in combined:
            combined.append(slug)

    if dry_run or not new_source_slugs:
        return
    post.metadata["sources"] = [f"[[{slug}]]" for slug in combined]
    post.metadata["source_count"] = len(combined)
    post.content = replace_references(post.content, combined)
    op_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def collect_for_operation(
    op: dict[str, Any],
    *,
    per_operation: int,
    dry_run: bool,
    seen_urls: set[str],
) -> dict[str, Any]:
    op_slug = str(op["slug"])
    op_profile = load_operation_profile(op_slug)
    allow = allowed_domains(op)
    added: list[str] = []
    checked_queries = 0
    used_urls: list[str] = []

    for query in op.get("queries", []):
        checked_queries += 1
        hits = run_search(query)
        for hit in hits:
            norm_url = normalize_url(hit.url)
            if norm_url in seen_urls or norm_url in used_urls:
                continue
            if not domain_allowed(hit.url, allow):
                continue
            summary = fetch_summary(hit.url, hit.snippet or hit.title)
            if not hit_relevant(op_profile, hit, summary):
                continue
            source_slug = save_pair(op_slug, hit, summary) if not dry_run else f"dryrun-{slugify(hit.title)[:30]}"
            if source_slug:
                added.append(source_slug)
                used_urls.append(norm_url)
                seen_urls.add(norm_url)
            if len(added) >= per_operation:
                break
        if len(added) >= per_operation:
            break
        time.sleep(0.3)

    update_operation(op_slug, added, dry_run=dry_run)
    return {
        "slug": op_slug,
        "added": added,
        "queries_checked": checked_queries,
        "source_count_before": op.get("source_count", 0),
        "source_count_after": op.get("source_count", 0) + len(added),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10, help="Number of operations to process from the queue.")
    parser.add_argument("--per-operation", type=int, default=2, help="Maximum new sources to add per operation.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--slugs", nargs="*", default=[], help="Specific operation slugs to process.")
    args = parser.parse_args()

    seen_urls = existing_urls()
    survey_ops = load_survey()
    if args.slugs:
        wanted = set(args.slugs)
        survey_ops = [op for op in survey_ops if op["slug"] in wanted]
    else:
        survey_ops = survey_ops[: args.limit]

    results: list[dict[str, Any]] = []
    for op in survey_ops:
        row = collect_for_operation(
            op,
            per_operation=args.per_operation,
            dry_run=args.dry_run,
            seen_urls=seen_urls,
        )
        results.append(row)
        print(f"{row['slug']}: +{len(row['added'])} ({row['source_count_before']} -> {row['source_count_after']})")

    created = sum(len(row["added"]) for row in results)
    print(f"OPERATIONS {len(results)}")
    print(f"CREATED {created}")


if __name__ == "__main__":
    main()
