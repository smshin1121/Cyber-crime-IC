from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
RAW_DIR = ROOT / "raw" / "press-releases"
TODAY = "2026-04-17"
SKIP_DIRS = {"sources", "cases", ".obsidian", "timelines"}


REF_ROW_RE = re.compile(r"^\|\s*(?:\[\d+\]|\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def sanitize_url_cell(text: str) -> str:
    match = re.search(r"\((https?://[^)]+)\)", text)
    if match:
        return match.group(1).strip()
    match = re.search(r"https?://\S+", text)
    if match:
        return match.group(0).rstrip(")|].,")
    return ""


def get_domain_slug(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return slugify(host.split(":", 1)[0].replace(".", "-"))


def normalize_date(text: str) -> str:
    value = text.strip()
    m = re.search(r"(20\d{2})[-/.](\d{2})[-/.](\d{2})", value)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"(20\d{2})[-/.](\d{2})", value)
    if m:
        return f"{m.group(1)}-{m.group(2)}-01"
    m = re.search(r"(20\d{2})", value)
    if m:
        return f"{m.group(1)}-01-01"
    return TODAY


def extract_summary(content: str) -> str:
    match = re.search(r"^## Summary\s*$", content, re.MULTILINE)
    if not match:
        return ""
    tail = content[match.end():].lstrip()
    lines: list[str] = []
    for line in tail.splitlines():
        stripped = line.strip()
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith("#"):
            break
        lines.append(stripped)
    return " ".join(lines).strip()


def reliability_for(publisher: str, url: str) -> str:
    text = f"{publisher} {url}".lower()
    if any(token in text for token in ["justice.gov", "fbi.gov", "europol", "interpol", "eurojust", "nca", "gov", "unodc"]):
        return "high"
    return "medium"


def discover_pages() -> list[Path]:
    pages: list[Path] = []
    for folder in sorted(WIKI_DIR.iterdir()):
        if not folder.is_dir() or folder.name in SKIP_DIRS:
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name.startswith("_"):
                continue
            pages.append(path)
    return pages


def create_pair(page_path: Path, title: str, publisher: str, date_text: str, url: str, summary: str) -> bool:
    publish_date = normalize_date(date_text)
    source_slug = f"{publish_date}_{get_domain_slug(url)}_{slugify(title)[:80]}".strip("-")
    raw_path = RAW_DIR / f"{source_slug}.md"
    source_path = SOURCES_DIR / f"{source_slug}.md"
    if raw_path.exists() or source_path.exists():
        return False

    page_slug = page_path.stem
    page_kind = page_path.parent.name.rstrip("s")
    domain = urlparse(url).netloc.lower()

    raw_text = (
        f"---\n"
        f"title: \"{title.replace(chr(34), chr(92) + chr(34))}\"\n"
        f"collection_source: \"{publisher.replace(chr(34), chr(92) + chr(34))}\"\n"
        f"collection_url: \"{url}\"\n"
        f"collection_domain: \"{domain}\"\n"
        f"collection_date: \"{TODAY}\"\n"
        f"publish_date: \"{publish_date}\"\n"
        f"language: \"en\"\n"
        f"status: \"collected\"\n"
        f"---\n\n"
        f"## Summary\n\n"
        f"{summary or f'Source referenced by {page_slug}.'}\n"
    )
    raw_path.write_text(raw_text, encoding="utf-8")

    source_meta = {
        "type": "source",
        "title": title,
        "raw_path": f"raw/press-releases/{source_slug}.md",
        "source_type": "press-release",
        "publisher": publisher,
        "author": "",
        "publish_date": publish_date,
        "ingest_date": TODAY,
        "language": "en",
        "reliability": reliability_for(publisher, url),
        "credibility": "confirmed",
        "sensitivity": "public",
        "pages_updated": [page_slug],
        "key_findings": [summary or f"Source cited in {page_slug} ({page_kind})."],
        "collection_url": url,
        "created": TODAY,
    }
    source_body = (
        "## Source Summary\n\n"
        f"{summary or f'This source is cited by [[{page_slug}]] and was normalized from a wiki reference table.'}\n\n"
        "## Relevance to IC\n\n"
        f"The source supports [[{page_slug}]] in the `{page_path.parent.name}` corpus."
    )
    post = frontmatter.Post(source_meta, source_body)
    source_path.write_text(frontmatter.dumps(post), encoding="utf-8")
    return True


def process_page(page_path: Path) -> int:
    text = page_path.read_text(encoding="utf-8")
    if "## References" not in text or "http" not in text:
        return 0

    post = frontmatter.load(page_path)
    summary = extract_summary(post.content)
    in_refs = False
    created = 0

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line == "## References":
            in_refs = True
            continue
        if in_refs and line.startswith("## "):
            break
        if not in_refs or "|---" in line or not line.startswith("|"):
            continue
        match = REF_ROW_RE.match(line)
        if not match:
            continue
        title, publisher, date_text, url_cell = [m.strip() for m in match.groups()]
        url = sanitize_url_cell(url_cell)
        if not url:
            continue
        if create_pair(page_path, title, publisher, date_text, url, summary):
            created += 1
    return created


def main() -> None:
    total = 0
    for page in discover_pages():
        total += process_page(page)
    print(f"Created {total} new source/raw pairs from wiki references.")


if __name__ == "__main__":
    main()
