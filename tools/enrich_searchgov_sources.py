from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import frontmatter

from doj_fetch import DOJClient


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_DIR = ROOT / "raw" / "press-releases"
TODAY = "2026-04-18"


NAME_PATTERNS = [
    re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s*,\s*\d{1,3}\s*,"),
    re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+was\s+(?:sentenced|charged|arrested|convicted)\b"),
    re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:pleaded|pleads)\s+guilty\b"),
]

TITLE_NAME_PATTERNS = [
    re.compile(r"\b(?:Indictment|Indicted|Charges?|Charged|Arrested|Sentence[ds]?|Sentenced|Convicted|Guilty Plea of)\s+(?:of\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b"),
    re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:Found Guilty|Sentenced|Charged|Arrested|Convicted|Pleads Guilty|Pleaded Guilty)\b"),
    re.compile(r"\bcreator and owner(?: of [^,]+)?,\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b", re.IGNORECASE),
]

SKIP_NAMES = {
    "United States", "Department Of Justice", "District Of Columbia", "Southern District",
    "Northern District", "Eastern District", "Western District", "Central District",
    "Office Of Public", "United States Attorney", "Justice Department", "Federal Court",
}
GENERIC_NAME_TOKENS = {
    "man", "woman", "national", "defendant", "defendants", "offender", "offenders",
    "trafficker", "developer", "administrator", "administrators", "citizen", "citizens",
    "teenager", "teenagers", "member", "members", "exchange", "marketplace", "drug",
    "dark", "web", "darknet", "market", "county", "district", "charges", "charged",
    "sentenced", "guilty", "pleads", "pleaded", "convicted", "hacking", "seizure",
    "ransomware", "affiliates", "across", "continents", "travel", "child", "offense",
    "official", "operator", "operators", "trafficking", "conspiracy",
}


def strip_tags(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_title(html_text: str) -> str:
    for pattern in [
        r'<h1[^>]*>\s*<span[^>]*>(.*?)</span>\s*</h1>',
        r"<title>\s*(.*?)\s*</title>",
    ]:
        match = re.search(pattern, html_text, re.DOTALL | re.IGNORECASE)
        if match:
            return strip_tags(match.group(1))
    return ""


def extract_paragraphs(html_text: str) -> list[str]:
    article_match = re.search(r'<div class="node-body">(.*?)<div class="node-bundle"', html_text, re.DOTALL)
    scope = article_match.group(1) if article_match else html_text
    paragraphs: list[str] = []
    for match in re.finditer(r"<p>(.*?)</p>", scope, re.DOTALL | re.IGNORECASE):
        text = strip_tags(match.group(1))
        lowered = text.lower()
        if not text:
            continue
        if any(skip in lowered for skip in [
            "official websites use .gov",
            "an official website of the united states government",
            "share this page",
        ]):
            continue
        if text:
            paragraphs.append(text)
        if len(paragraphs) >= 8:
            break
    return paragraphs


def extract_names(paragraphs: list[str]) -> list[str]:
    blob = " ".join(paragraphs[:4])
    names: list[str] = []
    for pattern in NAME_PATTERNS:
        for match in pattern.finditer(blob):
            name = match.group(1).strip()
            if name in SKIP_NAMES or len(name.split()) < 2:
                continue
            words = re.findall(r"[A-Za-z]+", name.lower())
            if any(word in GENERIC_NAME_TOKENS for word in words):
                continue
            if name not in names:
                names.append(name)
    return names[:5]


def extract_names_from_title(title: str) -> list[str]:
    names: list[str] = []
    cleaned = title.replace("U.S.", "US")
    for pattern in TITLE_NAME_PATTERNS:
        for match in pattern.finditer(cleaned):
            name = strip_tags(match.group(1)).strip(" ,.-")
            if name in SKIP_NAMES or len(name.split()) < 2:
                continue
            words = re.findall(r"[A-Za-z]+", name.lower())
            if any(word in GENERIC_NAME_TOKENS for word in words):
                continue
            if name not in names:
                names.append(name)
    return names[:5]


def enrich_source(path: Path, client: DOJClient) -> bool:
    post = frontmatter.load(path)
    meta = post.metadata
    if meta.get("defendant_names"):
        return False
    url = str(meta.get("collection_url") or "").strip()
    if not url or "justice.gov" not in url:
        return False

    html_text = client.fetch(url)
    if not html_text:
        return False

    title = extract_title(html_text)
    paragraphs = extract_paragraphs(html_text)
    names = extract_names(paragraphs)
    if not names and title:
        names = extract_names_from_title(title)
    summary = paragraphs[0] if paragraphs else ""

    changed = False
    if title and title != str(meta.get("title") or "").strip():
        meta["title"] = title
        changed = True
    if summary:
        findings = [summary]
        if findings != list(meta.get("key_findings") or []):
            meta["key_findings"] = findings
            changed = True
    if names:
        meta["defendant_names"] = names
        changed = True
    meta["updated"] = TODAY

    if not changed:
        return False

    path.write_text(frontmatter.dumps(post), encoding="utf-8")

    raw_rel = str(meta.get("raw_path") or "").strip()
    if raw_rel:
        raw_path = ROOT / raw_rel
        if raw_path.exists():
            raw_post = frontmatter.load(raw_path)
            raw_meta = raw_post.metadata
            if title:
                raw_meta["title"] = title
            if names:
                raw_meta["defendant_names"] = names
            raw_meta["updated"] = TODAY
            raw_path.write_text(frontmatter.dumps(raw_post), encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--recent-only", action="store_true")
    args = parser.parse_args()

    client = DOJClient()
    paths = sorted(SOURCES_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    changed = 0
    for path in paths:
        if path.name.startswith("_"):
            continue
        if args.recent_only and "2026-04-18_justice-gov_" not in path.name:
            continue
        if enrich_source(path, client):
            changed += 1
        if changed >= args.limit:
            break
    print(f"Enriched {changed} SearchGov-derived source pages.")


if __name__ == "__main__":
    main()
