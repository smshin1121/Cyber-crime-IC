from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

import frontmatter

from harvest_linked_source_text import (
    ROOT,
    RAW_DIR,
    extract_readable_text,
    host_for,
    remove_generated_sections,
    sha256_text,
    word_count,
)


def extracted_section(content: str) -> str:
    match = re.search(r"\n*##\s+Extracted Text\s*\n(.*?)(?=\n##\s+Extraction Notes\s*\n|\Z)", content, flags=re.S)
    return match.group(1).strip() if match else ""


def trim_one(path: Path, run_date: str, dry_run: bool) -> tuple[bool, int, int]:
    post = frontmatter.load(path)
    meta = post.metadata
    extracted = extracted_section(post.content or "")
    if not extracted.startswith("Title: ") or "\nMarkdown Content:" not in extracted:
        return False, 0, 0

    url = str(meta.get("collection_url") or meta.get("final_url") or "").strip()
    if not url:
        return False, 0, 0

    old_words = word_count(extracted)
    title, text, parser = extract_readable_text(
        extracted,
        str(meta.get("content_type") or "text/plain"),
        url,
        str(meta.get("title") or path.stem),
    )
    new_words = word_count(text)
    if new_words < 120 or new_words >= old_words:
        return False, old_words, new_words

    if dry_run:
        return True, old_words, new_words

    meta["word_count"] = new_words
    meta["content_hash"] = sha256_text(text)
    meta["extraction_date"] = run_date
    meta["parser"] = parser
    meta.setdefault("collection_domain", host_for(url))
    post.metadata = meta

    base = remove_generated_sections(post.content or "")
    notes = [
        f"- parser: {parser}",
        f"- fetcher: {meta.get('fetcher') or meta.get('last_fetcher') or ''}",
        f"- normalized_at: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        f"- final_url: {meta.get('final_url') or url}",
        "- cleanup: jina navigation trim",
    ]
    post.content = (
        base.rstrip()
        + "\n\n## Extracted Text\n\n"
        + text.strip()
        + "\n\n## Extraction Notes\n\n"
        + "\n".join(notes)
        + "\n"
    )
    path.write_text(frontmatter.dumps(post), encoding="utf-8")

    source_page = str(meta.get("source_page") or "").strip()
    if source_page.startswith("wiki/sources/"):
        source_path = ROOT / source_page
        if source_path.exists():
            source_post = frontmatter.load(source_path)
            source_meta = source_post.metadata
            source_meta["word_count"] = new_words
            source_meta["content_hash"] = meta["content_hash"]
            source_meta["text_status"] = "parsed"
            source_meta["storage_mode"] = "fulltext"
            source_meta["extraction_date"] = run_date
            source_meta["last_fetcher"] = meta.get("fetcher") or meta.get("last_fetcher") or ""
            source_post.metadata = source_meta
            source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")

    return True, old_words, new_words


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    changed = 0
    samples: list[str] = []
    for path in sorted(RAW_DIR.rglob("*.md")):
        if path.name.startswith("_"):
            continue
        did_change, old_words, new_words = trim_one(path, args.date, args.dry_run)
        if not did_change:
            continue
        changed += 1
        if len(samples) < 20:
            samples.append(f"- {path.relative_to(ROOT).as_posix()}: {old_words} -> {new_words}")
        if args.limit and changed >= args.limit:
            break

    print("tools/trim_jina_extracted_text.py")
    print(f"  mode: {'dry-run' if args.dry_run else 'applied'}")
    print(f"  trimmed: {changed}")
    for sample in samples:
        print(sample)


if __name__ == "__main__":
    main()
