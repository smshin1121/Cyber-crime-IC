from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
CASES_DIR = ROOT / "wiki" / "cases"
SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_DIR = ROOT / "raw" / "press-releases"
TARGETS_FILE = Path(__file__).resolve().parent / "_low_source65.txt"
TODAY = "2026-04-22"

REF_ROW_RE = re.compile(
    r"^\|\s*(?:\[\d+\]|\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$"
)


def wikilink_slug(value: str) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


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


def domain_slug(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return slugify(host.replace(".", "-"))


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


def create_pair(
    case_slug: str,
    op_slug: str,
    title: str,
    publisher: str,
    date_text: str,
    url: str,
    summary: str,
) -> bool:
    publish_date = normalize_date(date_text)
    source_slug = f"{publish_date}_{domain_slug(url)}_{slugify(title)[:80]}".strip("-")
    raw_path = RAW_DIR / f"{source_slug}.md"
    source_path = SOURCES_DIR / f"{source_slug}.md"
    if raw_path.exists() or source_path.exists():
        return False

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
        f"{summary or title}\n"
    )
    raw_path.write_text(raw_text, encoding="utf-8")

    source_post = frontmatter.Post(
        {
            "type": "source",
            "title": title,
            "raw_path": f"raw/press-releases/{source_slug}.md",
            "source_type": "press-release",
            "publisher": publisher,
            "author": "",
            "publish_date": publish_date,
            "ingest_date": TODAY,
            "language": "en",
            "reliability": "high" if ".gov" in domain or "europol" in domain or "interpol" in domain else "medium",
            "credibility": "confirmed",
            "sensitivity": "public",
            "pages_updated": [case_slug, op_slug],
            "key_findings": [summary or title],
            "collection_url": url,
            "created": TODAY,
        },
        (
            "## Source Summary\n\n"
            f"{summary or title}\n\n"
            "## Relevance to IC\n\n"
            f"This source was normalized from [[{case_slug}]] and linked to [[{op_slug}]]."
        ),
    )
    source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")
    return True


def main() -> None:
    targets = {
        line.strip()
        for line in TARGETS_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    created = 0

    for op_slug in sorted(targets):
        op_path = OPS_DIR / f"{op_slug}.md"
        if not op_path.exists():
            continue
        op_post = frontmatter.load(op_path)
        related_cases = op_post.metadata.get("related_cases") or []
        if isinstance(related_cases, str):
            related_cases = [related_cases]
        for value in related_cases:
            case_slug = wikilink_slug(value)
            if not case_slug:
                continue
            case_path = CASES_DIR / f"{case_slug}.md"
            if not case_path.exists():
                continue
            text = case_path.read_text(encoding="utf-8")
            if "## References" not in text or "http" not in text:
                continue
            case_post = frontmatter.load(case_path)
            summary = extract_summary(case_post.content)
            in_refs = False
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
                if create_pair(case_slug, op_slug, title, publisher, date_text, url, summary):
                    created += 1
                    print(f"{op_slug}: + {title}")

    print(f"CREATED {created}")


if __name__ == "__main__":
    main()
