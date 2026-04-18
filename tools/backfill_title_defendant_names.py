from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_DIR = ROOT / "raw" / "press-releases"
TODAY = "2026-04-18"

TITLE_NAME_PATTERNS = [
    re.compile(r"\b(?:Indictment|Indicted|Charges?|Charged|Arrested|Sentence[ds]?|Sentenced|Convicted|Guilty Plea of|Found Guilty)\s+(?:of\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b"),
    re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:Found Guilty|Sentenced|Charged|Arrested|Convicted|Pleads Guilty|Pleaded Guilty)\b"),
    re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+aka\b"),
    re.compile(r"\b(?:creator and owner|operator)\s+(?:of [^,]+,\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b", re.IGNORECASE),
]

SKIP_NAMES = {
    "United States", "Department Of Justice", "District Of Columbia", "Southern District",
    "Northern District", "Eastern District", "Western District", "Central District",
    "United States Attorney", "Justice Department", "Federal Court",
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


def extract_names_from_title(title: str) -> list[str]:
    names: list[str] = []
    cleaned = strip_tags(title).replace("U.S.", "US")
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


def enrich_source(path: Path) -> bool:
    post = frontmatter.load(path)
    meta = post.metadata
    if meta.get("defendant_names"):
        return False
    title = str(meta.get("title") or "").strip()
    names = extract_names_from_title(title)
    if not names:
        return False

    meta["defendant_names"] = names
    meta["updated"] = TODAY
    path.write_text(frontmatter.dumps(post), encoding="utf-8")

    raw_rel = str(meta.get("raw_path") or "").strip()
    if raw_rel:
        raw_path = ROOT / raw_rel
        if raw_path.exists():
            raw_post = frontmatter.load(raw_path)
            raw_post.metadata["defendant_names"] = names
            raw_post.metadata["updated"] = TODAY
            raw_path.write_text(frontmatter.dumps(raw_post), encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args()

    changed = 0
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        if enrich_source(path):
            changed += 1
        if changed >= args.limit:
            break
    print(f"Backfilled defendant_names on {changed} source pages.")


if __name__ == "__main__":
    main()
