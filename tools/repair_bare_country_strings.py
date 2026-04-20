#!/usr/bin/env python3
"""
Repair bare-string country entries in wiki/operations/*.md frontmatter.

Target: `participating_countries:` list entries that are bare strings
like `- "France"` or `- "Nigeria"`. If the string, when slugified
(lowercase + non-alphanumeric → hyphen), matches an existing
`wiki/countries/<slug>.md` page, rewrite the line to the canonical
wikilink form `- "[[france]]"`.

Rules:
- Only rewrite inside the `participating_countries:` block.
- Skip entries that are already wikilinks (contain `[[`).
- Skip entries whose normalized form does NOT match a canonical page.
- Idempotent: re-running does not double-wrap.
- Additive-only: no other fields are touched.
- Body prose is not touched.

Usage:
    python tools/repair_bare_country_strings.py --dry-run
    python tools/repair_bare_country_strings.py
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("repair")

REPO = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO / "wiki" / "operations"
WIKI_COUNTRIES = REPO / "wiki" / "countries"

BLOCK_START_RE = re.compile(r"^participating_countries:\s*$")
NEXT_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*:\s*(?:\S.*)?$")
# Quoted list item: `  - "value"` — value can contain anything except `"`
LIST_ITEM_QUOTED_RE = re.compile(r'^(?P<lead>\s+- )"(?P<val>[^"]*)"(?P<tail>\s*)$')
# Unquoted list item: `  - value` — value starts with alphanumeric, no quotes/brackets
LIST_ITEM_BARE_RE = re.compile(r'^(?P<lead>\s+- )(?P<val>[A-Za-z][^\n"\[]*?)(?P<tail>\s*)$')
NORMALIZE_RE = re.compile(r"[^a-z0-9]+")
FRONTMATTER_END_RE = re.compile(r"^---\s*$")


def normalize(raw: str) -> str:
    return NORMALIZE_RE.sub("-", raw.strip().lower()).strip("-")


def canonical_country_slugs() -> set[str]:
    return {p.stem for p in WIKI_COUNTRIES.glob("*.md") if p.stem != "_index"}


def repair_text(text: str, canonical: set[str]) -> tuple[str, int, list[str]]:
    """Return (new_text, change_count, changed_from_to)."""
    lines = text.splitlines(keepends=True)
    in_fm = False
    fm_boundaries_seen = 0
    in_block = False
    changes = 0
    diff: list[str] = []
    new_lines: list[str] = []

    for line in lines:
        stripped = line.rstrip("\r\n")

        # Track frontmatter fences. Only process the first FM block.
        if FRONTMATTER_END_RE.match(stripped):
            fm_boundaries_seen += 1
            in_fm = fm_boundaries_seen == 1
            in_block = False
            new_lines.append(line)
            continue

        if not in_fm:
            new_lines.append(line)
            continue

        # Block boundary detection
        if BLOCK_START_RE.match(stripped):
            in_block = True
            new_lines.append(line)
            continue

        if in_block:
            # End of block when a new top-level key appears (non-indented line).
            if stripped and not stripped.startswith(("  ", "\t", "- ", " -")) and NEXT_KEY_RE.match(stripped):
                in_block = False
                new_lines.append(line)
                continue
            m = LIST_ITEM_QUOTED_RE.match(stripped) or LIST_ITEM_BARE_RE.match(stripped)
            if m:
                value = m.group("val")
                if "[[" in value or not value.strip():
                    new_lines.append(line)
                    continue
                slug = normalize(value)
                if slug in canonical:
                    new_inner = f'[[{slug}]]'
                    # Preserve original line ending
                    end = line[len(stripped):]
                    new_line = f'{m.group("lead")}"{new_inner}"{m.group("tail")}{end}'
                    new_lines.append(new_line)
                    changes += 1
                    diff.append(f'{value!r} → [[{slug}]]')
                    continue
            new_lines.append(line)
            continue

        new_lines.append(line)

    return "".join(new_lines), changes, diff


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--path", type=Path, default=WIKI_OPS)
    args = parser.parse_args()

    canonical = canonical_country_slugs()
    log.info("canonical country slugs known: %d", len(canonical))

    total_files_changed = 0
    total_lines_changed = 0
    per_file: list[tuple[str, int, list[str]]] = []

    for path in sorted(args.path.glob("*.md")):
        if path.name == "_index.md":
            continue
        original = path.read_text(encoding="utf-8")
        new_text, count, diff = repair_text(original, canonical)
        if count == 0:
            continue
        per_file.append((path.name, count, diff))
        total_files_changed += 1
        total_lines_changed += count
        if not args.dry_run:
            path.write_text(new_text, encoding="utf-8")

    mode = "dry-run" if args.dry_run else "applied"
    print(f"\n=== Bare country string repair ({mode}) ===")
    print(f"files changed: {total_files_changed}")
    print(f"lines changed: {total_lines_changed}")
    for fname, count, diff in per_file:
        print(f"  [{count:2d}] {fname}")
        for entry in diff:
            print(f"        {entry}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
