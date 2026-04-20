#!/usr/bin/env python3
"""
Migrate `crime_type` (single wikilink) → `crime_types` (list of wikilinks) on
wiki/operations/*.md.

Execution rules (user-approved, PoC v4):
1. Additive: inserts a new `crime_types:` block immediately after the existing
   `crime_type:` line.
2. Non-destructive: the existing `crime_type:` field is **preserved** as a
   read-only fallback during migration. Removal is deferred to a later cycle.
3. Idempotent: re-running skips files that already have `crime_types`.
4. Byte-faithful: the original `crime_type` value text is copied
   character-for-character (preserves quoting, wikilink brackets, spaces).

Usage:
    python tools/migrate_crime_type_to_list.py --dry-run
    python tools/migrate_crime_type_to_list.py
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("migrate")

REPO = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO / "wiki" / "operations"

# Line-based: `^crime_type: <value>$`. Stops at end-of-line, value group is
# everything after the colon (trimmed later).
CRIME_TYPE_LINE_RE = re.compile(r"^(?P<key>crime_type:\s*)(?P<value>.*)$", re.MULTILINE)


def migrate_text(text: str) -> tuple[str, str]:
    """Return (new_text, status).

    status ∈ {migrated, already_migrated, no_crime_type, empty_crime_type,
              line_not_found, parse_error, no_frontmatter}.
    """
    if not text.startswith("---"):
        return text, "no_frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, "no_frontmatter"
    fm = parts[1]
    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError:
        return text, "parse_error"
    if not isinstance(data, dict):
        return text, "parse_error"

    if "crime_types" in data:
        return text, "already_migrated"

    crime_type_val = data.get("crime_type")
    if crime_type_val is None or (
        isinstance(crime_type_val, str) and not crime_type_val.strip()
    ):
        return text, "empty_crime_type" if "crime_type" in data else "no_crime_type"

    match = CRIME_TYPE_LINE_RE.search(fm)
    if not match:
        return text, "line_not_found"

    value_text = match.group("value").rstrip()
    if not value_text:
        # Block-scalar or multi-line form — conservative: do not mutate.
        return text, "line_not_found"

    insert_block = f"\ncrime_types:\n  - {value_text}"
    end = match.end()
    new_fm = fm[:end] + insert_block + fm[end:]
    new_text = parts[0] + "---" + new_fm + "---" + parts[2]
    return new_text, "migrated"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--path", type=Path, default=WIKI_OPS)
    args = parser.parse_args()

    counts: dict[str, int] = {}
    migrated_paths: list[str] = []
    for path in sorted(args.path.glob("*.md")):
        if path.name == "_index.md":
            continue
        original = path.read_text(encoding="utf-8")
        new_text, status = migrate_text(original)
        counts[status] = counts.get(status, 0) + 1
        if status == "migrated":
            migrated_paths.append(path.name)
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")

    print(f"\n=== Migration summary ({'dry-run' if args.dry_run else 'applied'}) ===")
    for status in (
        "migrated",
        "already_migrated",
        "empty_crime_type",
        "no_crime_type",
        "line_not_found",
        "parse_error",
        "no_frontmatter",
    ):
        if status in counts:
            print(f"  {status:20s} {counts[status]}")
    print(f"  total_files         {sum(counts.values())}")

    if migrated_paths and args.dry_run:
        print(f"\nFirst 10 would-be-migrated:")
        for name in migrated_paths[:10]:
            print(f"  {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
