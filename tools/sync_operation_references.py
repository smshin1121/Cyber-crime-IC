#!/usr/bin/env python3
"""Synchronize operation References tables from frontmatter source links.

This intentionally uses a small frontmatter scanner instead of a YAML parser so it
can still repair operation pages while unrelated source pages have YAML quoting
problems.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"
WIKILINK_RE = re.compile(r"\[\[([^|\]]+)(?:\|[^\]]*)?\]\]")


def clean(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.replace('\\"', '"').replace("\\'", "'").strip()


def escape_cell(value: str) -> str:
    value = " ".join((value or "?").split())
    return value.replace("|", "\\|")


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if not line or line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = clean(value)
    return data


def extract_source_slugs(text: str) -> list[str]:
    lines = text.splitlines()
    slugs: list[str] = []
    in_sources = False
    for line in lines:
        if line == "sources:":
            in_sources = True
            continue
        if in_sources:
            if line and not line.startswith((" ", "\t", "-")):
                break
            match = WIKILINK_RE.search(line)
            if match:
                slugs.append(match.group(1).strip())
    return slugs


def source_row(index: int, slug: str) -> str:
    path = SOURCE_DIR / f"{slug}.md"
    if not path.exists():
        return f"| [{index}] | {escape_cell(slug)} | ? | ? | ? |"

    meta = read_frontmatter(path)
    title = meta.get("title", slug)
    publisher = meta.get("publisher", "?")
    date = meta.get("publish_date") or meta.get("date") or meta.get("created") or "?"
    url = meta.get("collection_url") or meta.get("url") or meta.get("attribution_url") or "?"
    return (
        f"| [{index}] | {escape_cell(title)} | {escape_cell(publisher)} | "
        f"{escape_cell(date)} | {escape_cell(url)} |"
    )


def render_references(slugs: list[str]) -> str:
    rows = [
        "## References",
        "",
        "| # | Title | Publisher | Date | URL |",
        "|---|---|---|---|---|",
    ]
    rows.extend(source_row(index, slug) for index, slug in enumerate(slugs, start=1))
    return "\n".join(rows).rstrip() + "\n"


def replace_references(text: str, refs: str) -> str:
    marker = "\n## References"
    pos = text.find(marker)
    prefix_newline = True
    if pos == -1:
        if text.startswith("## References"):
            pos = 0
            prefix_newline = False
        else:
            return text.rstrip() + "\n\n" + refs

    start = pos + (1 if prefix_newline else 0)
    next_heading = re.search(r"\n## (?!References\b)", text[start + 1 :])
    if next_heading:
        end = start + 1 + next_heading.start()
        return text[:start] + refs.rstrip() + "\n" + text[end:]
    return text[:start] + refs


def sync_file(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    slugs = extract_source_slugs(text)
    if not slugs:
        return False
    updated = replace_references(text, render_references(slugs))
    if updated == text:
        return False
    if not dry_run:
        path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Operation markdown files to update")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    changed = []
    for item in args.paths:
        path = (ROOT / item).resolve()
        if not path.exists():
            raise SystemExit(f"missing file: {item}")
        if sync_file(path, args.dry_run):
            changed.append(str(path.relative_to(ROOT)))

    for path in changed:
        print(path)
    print(f"{'would update' if args.dry_run else 'updated'}: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
