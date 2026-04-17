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
SKIP_DIRS = {"sources", ".obsidian"}


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def existing_urls() -> set[str]:
    urls: set[str] = set()
    for folder in [SOURCES_DIR, ROOT / "raw" / "press-releases", ROOT / "raw" / "case-documents"]:
        for path in folder.glob("*.md"):
            if path.name.startswith("_"):
                continue
            meta = frontmatter.load(path).metadata
            for key in ("collection_url", "source_url"):
                url = str(meta.get(key) or "").strip()
                if url:
                    urls.add(url)
    return urls


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


def discover_missing() -> list[tuple[Path, str, str]]:
    known = existing_urls()
    out: list[tuple[Path, str, str]] = []
    seen: set[str] = set()
    for folder in sorted(WIKI_DIR.iterdir()):
        if not folder.is_dir() or folder.name in SKIP_DIRS:
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name.startswith("_"):
                continue
            text = path.read_text(encoding="utf-8")
            for url in re.findall(r"https?://[^\s)\]>\"']+", text):
                clean = url.rstrip(".,")
                if clean in known or clean in seen:
                    continue
                seen.add(clean)
                out.append((path, clean, text))
    return out


def title_from_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.path and parsed.path != "/":
        last = parsed.path.rstrip("/").split("/")[-1]
    else:
        last = parsed.netloc
    return last.replace("-", " ").replace("_", " ").strip() or parsed.netloc


def create_pair(page_path: Path, url: str) -> bool:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    domain_slug = slugify(domain.replace("www.", "").replace(".", "-"))
    title = title_from_url(url)
    date = TODAY
    m = re.search(r"(20\d{2})[-/](\d{2})[-/](\d{2})", url)
    if m:
        date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    source_slug = f"{date}_{domain_slug}_{slugify(title)[:80]}".strip("-")
    raw_path = RAW_DIR / f"{source_slug}.md"
    source_path = SOURCES_DIR / f"{source_slug}.md"
    if raw_path.exists() or source_path.exists():
        return False

    post = frontmatter.load(page_path)
    summary = extract_summary(post.content) or f"External URL cited in [[{page_path.stem}]]."
    publisher = domain.replace("www.", "")

    raw_post = frontmatter.Post(
        {
            "title": title,
            "collection_source": publisher,
            "collection_url": url,
            "collection_domain": domain,
            "collection_date": TODAY,
            "publish_date": date,
            "language": "en",
            "status": "collected",
        },
        f"## Summary\n\n{summary}\n",
    )
    raw_path.write_text(frontmatter.dumps(raw_post), encoding="utf-8")

    source_post = frontmatter.Post(
        {
            "type": "source",
            "title": title,
            "raw_path": f"raw/press-releases/{source_slug}.md",
            "source_type": "web-reference",
            "publisher": publisher,
            "author": "",
            "publish_date": date,
            "ingest_date": TODAY,
            "language": "en",
            "reliability": "medium",
            "credibility": "unverified",
            "sensitivity": "public",
            "pages_updated": [page_path.stem],
            "key_findings": [summary],
            "collection_url": url,
            "created": TODAY,
        },
        (
            "## Source Summary\n\n"
            f"{summary}\n\n"
            "## Relevance to IC\n\n"
            f"This URL was cited in [[{page_path.stem}]] and has been normalized into the source corpus."
        ),
    )
    source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")
    return True


def main() -> None:
    created = 0
    for page_path, url, _ in discover_missing():
        if create_pair(page_path, url):
            created += 1
    print(f"Created {created} source/raw pairs from orphan URLs.")


if __name__ == "__main__":
    main()
