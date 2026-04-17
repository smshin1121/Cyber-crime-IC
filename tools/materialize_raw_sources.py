from __future__ import annotations

import argparse
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
RAW_CASE_DIR = ROOT / "raw" / "case-documents"
RAW_PRESS_DIR = ROOT / "raw" / "press-releases"
SOURCES_DIR = ROOT / "wiki" / "sources"
TODAY = "2026-04-17"


def existing_raw_paths() -> set[str]:
    paths: set[str] = set()
    for path in SOURCES_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        raw_path = str(post.metadata.get("raw_path") or "").strip()
        if raw_path:
            paths.add(raw_path)
    return paths


def body_summary(content: str) -> str:
    lines: list[str] = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line or line == "---" or line.startswith("## "):
            continue
        if line.startswith("*Court document collected"):
            continue
        lines.append(line)
    return " ".join(lines[:3]).strip()


def create_source_from_raw(raw_path: Path, rel_raw: str, refresh: bool = False) -> bool:
    source_path = SOURCES_DIR / raw_path.name
    if source_path.exists() and not refresh:
        return False

    post = frontmatter.load(raw_path)
    meta = post.metadata
    title = str(meta.get("title") or raw_path.stem.replace("-", " ").title())
    publisher = str(meta.get("publisher") or meta.get("collection_source") or meta.get("court") or "Unknown")
    publish_date = str(meta.get("publish_date") or meta.get("date_filed") or meta.get("collection_date") or TODAY)
    url = str(meta.get("collection_url") or meta.get("source_url") or "")
    summary = body_summary(post.content)
    reliability = "high" if any(token in publisher.lower() for token in ["doj", "fbi", "europol", "interpol", "eurojust", "court"]) else "medium"

    pages_updated: list[str] = []
    related_operation = str(meta.get("related_operation") or "").strip()
    if related_operation:
        pages_updated.append(related_operation)

    source_post = frontmatter.Post(
        {
            "type": "source",
            "title": title,
            "raw_path": rel_raw,
            "source_type": "court-document" if "case-documents" in rel_raw else "press-release",
            "publisher": publisher,
            "author": "",
            "publish_date": publish_date,
            "ingest_date": TODAY,
            "language": str(meta.get("language") or "en"),
            "reliability": reliability,
            "credibility": "confirmed",
            "sensitivity": str(meta.get("sensitivity") or "public"),
            "pages_updated": pages_updated,
            "key_findings": [summary or f"Materialized from {raw_path.name}"],
            "collection_url": url,
            "created": TODAY,
        },
        (
            "## Source Summary\n\n"
            f"{summary or f'Structured source page materialized from `{rel_raw}`.'}\n\n"
            "## Relevance to IC\n\n"
            f"This source was generated from `{rel_raw}` to make the raw corpus addressable from the source index."
        ),
    )
    source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    known = existing_raw_paths()
    created = 0

    for folder, rel_prefix in [(RAW_CASE_DIR, "raw/case-documents"), (RAW_PRESS_DIR, "raw/press-releases")]:
        for raw_path in sorted(folder.glob("*.md")):
            rel_raw = f"{rel_prefix}/{raw_path.name}"
            if rel_raw in known and not args.refresh:
                continue
            if create_source_from_raw(raw_path, rel_raw, refresh=args.refresh):
                created += 1

    print(f"Created {created} source pages from raw materials.")


if __name__ == "__main__":
    main()
