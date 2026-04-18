from __future__ import annotations

import argparse
import html
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from urllib.error import HTTPError
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw" / "press-releases"
SOURCES_DIR = ROOT / "wiki" / "sources"
TODAY = "2026-04-18"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


TOPICS = [
    "darknet",
    "\"dark web\"",
    "ransomware",
    "malware",
    "botnet",
    "phishing",
    "carding",
    "\"business email compromise\"",
    "cryptocurrency fraud",
    "\"online fraud\"",
    "cybercrime",
    "hacker",
    "hacker charged",
    "hacker sentenced",
    "\"computer fraud\"",
    "\"wire fraud\"",
    "\"identity theft\"",
    "\"access device fraud\"",
    "\"money laundering\" cyber",
    "\"crypto laundering\"",
    "\"marketplace\" cybercrime",
    "\"drug trafficking\" darknet",
    "\"fraud ring\" cyber",
    "\"botnet operator\"",
    "\"malware author\"",
    "\"malware developer\"",
    "\"ransomware affiliate\"",
    "\"darknet vendor\"",
    "\"dark web dealer\"",
    "\"cyber fraud\"",
    "\"cyber enabled fraud\"",
    "\"internet fraud\"",
    "\"bank fraud\" malware",
    "\"credential theft\"",
    "\"SIM swap\"",
    "\"sextortion\" cyber",
    "\"bulletproof hosting\"",
    "\"DDoS\" cybercrime",
    "\"carding forum\"",
    "\"romance scam\" cyber",
    "\"pig butchering\"",
    "\"cryptojacking\"",
    "\"initial access\" broker",
    "\"malvertising\"",
]

ACTIONS = [
    "sentenced",
    "charged",
    "indicted",
    "\"pleaded guilty\"",
    "convicted",
    "arrested",
    "extradited",
    "\"found guilty\"",
    "\"sentenced to\"",
    "\"admits\"",
    "\"forfeiture\"",
    "\"seized\"",
    "\"dismantled\"",
    "\"taken down\"",
]


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def existing_urls() -> set[str]:
    urls: set[str] = set()
    for folder in (RAW_DIR, SOURCES_DIR):
        for path in folder.glob("*.md"):
            if path.name.startswith("_"):
                continue
            post = frontmatter.load(path)
            meta = post.metadata
            url = str(meta.get("collection_url") or meta.get("source_url") or "").strip()
            if url:
                urls.add(url)
    return urls


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except HTTPError:
        return ""


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(text)).strip()


def search_searchgov(query: str, page: int) -> tuple[int, list[tuple[str, str, str, str]]]:
    url = (
        "https://search.justice.gov/search?affiliate=justice&query="
        + urllib.parse.quote(query)
        + f"&page={page}"
    )
    html_text = fetch(url)
    if not html_text:
        return 0, []
    rows: list[tuple[str, str, str]] = []
    try:
        props = re.search(r'data-react-props=\"(\{.*?\})\"', html_text)
        if not props:
            return 0, []
        data = json.loads(html.unescape(props.group(1)))
    except Exception:
        return 0, []

    total_pages = int(data.get("resultsData", {}).get("totalPages") or 0)
    items = data.get("resultsData", {}).get("results") or []
    output: list[tuple[str, str, str, str]] = []
    for item in items:
        link = str(item.get("url") or "").strip()
        if "justice.gov" not in urllib.parse.urlparse(link).netloc.lower():
            continue
        title = strip_tags(str(item.get("title") or "").strip())
        snippet = strip_tags(str(item.get("description") or "").strip())
        published = strip_tags(str(item.get("publishedDate") or "").strip())
        output.append((link, title, snippet, published))
    return total_pages, output


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))


def infer_publish_date(url: str) -> str:
    m = re.search(r"/(20\d{2})/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/", url)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return TODAY


def normalize_publish_date(text: str, url: str) -> str:
    m = re.search(r"(20\d{2})", text)
    if m:
        year = m.group(1)
        months = {
            "january": "01", "february": "02", "march": "03", "april": "04",
            "may": "05", "june": "06", "july": "07", "august": "08",
            "september": "09", "october": "10", "november": "11", "december": "12",
        }
        lowered = text.lower()
        month = next((v for k, v in months.items() if k in lowered), "01")
        day_match = re.search(r"(\d{1,2})(?:st|nd|rd|th)?", lowered)
        day = f"{int(day_match.group(1)):02d}" if day_match else "01"
        return f"{year}-{month}-{day}"
    return infer_publish_date(url)


def raw_slug(url: str, title: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower().replace("www.", "").replace(".", "-")
    date = infer_publish_date(url)
    path_slug = slugify(parsed.path.split("/")[-1] or title)[:90]
    return f"{date}_{host}_{path_slug}".strip("-")


def save_pair(url: str, title: str, snippet: str, published: str) -> bool:
    slug = raw_slug(url, title)
    raw_path = RAW_DIR / f"{slug}.md"
    source_path = SOURCES_DIR / f"{slug}.md"
    if raw_path.exists() or source_path.exists():
        return False

    domain = urllib.parse.urlsplit(url).netloc.lower().replace("www.", "")
    publisher = "US DOJ"
    if "usao-" in url:
        publisher = "US DOJ USAO"
    elif "/opa/" in url:
        publisher = "US DOJ (Office of Public Affairs)"

    publish_date = normalize_publish_date(published, url)
    raw_text = (
        f"---\n"
        f"title: \"{title.replace(chr(34), chr(92) + chr(34))}\"\n"
        f"collection_source: \"{publisher}\"\n"
        f"collection_url: \"{url}\"\n"
        f"collection_domain: \"{domain}\"\n"
        f"collection_date: \"{TODAY}\"\n"
        f"publish_date: \"{publish_date}\"\n"
        f"language: \"en\"\n"
        f"status: \"collected\"\n"
        f"---\n\n"
        f"## Summary\n\n"
        f"{snippet or title}\n"
    )
    raw_path.write_text(raw_text, encoding="utf-8")

    source_post = frontmatter.Post(
        {
            "type": "source",
            "title": title,
            "raw_path": f"raw/press-releases/{slug}.md",
            "source_type": "press-release",
            "publisher": publisher,
            "author": "",
            "publish_date": publish_date,
            "ingest_date": TODAY,
            "language": "en",
            "reliability": "high",
            "credibility": "confirmed",
            "sensitivity": "public",
            "pages_updated": [],
            "key_findings": [snippet or title],
            "collection_url": url,
            "created": TODAY,
        },
        (
            "## Source Summary\n\n"
            f"{snippet or title}\n\n"
            "## Relevance to IC\n\n"
            "This source was discovered from DOJ SearchGov results limited to official DOJ domains."
        ),
    )
    source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")
    return True


def query_list(limit: int) -> list[str]:
    queries: list[str] = []
    for topic in TOPICS:
        queries.append(f"{topic}")
        queries.append(f"{topic} doj")
        for action in ACTIONS:
            queries.append(f"{topic} {action}")
            queries.append(f"{topic} {action} cybercrime")
            queries.append(f"{topic} {action} indictment")
    return queries[:limit]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", type=int, default=24)
    parser.add_argument("--sleep", type=float, default=1.0)
    args = parser.parse_args()

    known = existing_urls()
    created = 0
    seen_urls: set[str] = set()

    for query in query_list(args.queries):
        total_pages, _ = search_searchgov(query, 1)
        max_pages = min(total_pages or 1, 10)
        for page in range(1, max_pages + 1):
            _, rows = search_searchgov(query, page)
            for url, title, snippet, published in rows:
                norm = normalize_url(url)
                if norm in known or norm in seen_urls:
                    continue
                if save_pair(norm, title, snippet, published):
                    created += 1
                    seen_urls.add(norm)
        time.sleep(args.sleep)

    print(f"Created {created} DOJ raw/source pairs from SearchGov discovery.")


if __name__ == "__main__":
    main()
