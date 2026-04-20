#!/usr/bin/env python3
"""
One-shot scan: find every non-wikilink "bare string" value in
participating_agencies / participating_countries / crime_type /
lead_agency / coordinating_body across wiki/operations/*.md.

Output: CSV to stdout. Columns: kind, raw_value, normalized_slug,
has_canonical_page, occurrence_count, example_op.

Used to decide normalization strategy (script-side vs source-side).
Does NOT modify any files.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO / "wiki" / "operations"
WIKI_ORGS = REPO / "wiki" / "organizations"
WIKI_COUNTRIES = REPO / "wiki" / "countries"
WIKI_CRIMES = REPO / "wiki" / "crime-types"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
NORMALIZE_RE = re.compile(r"[^a-z0-9]+")


def normalize(raw: str) -> str:
    s = raw.strip().lower()
    s = NORMALIZE_RE.sub("-", s)
    return s.strip("-")


def classify_value(v) -> tuple[str, str] | None:
    """Return (kind, slug_or_bare) from a YAML value. kind is 'wikilink' or 'bare'.
    For lists, caller iterates. For None/empty, return None."""
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    m = WIKILINK_RE.fullmatch(s)
    if m:
        return ("wikilink", m.group(1).strip())
    m2 = WIKILINK_RE.search(s)
    if m2:
        return ("wikilink", m2.group(1).strip())
    return ("bare", s)


def iter_values(v):
    if v is None:
        return
    if isinstance(v, list):
        yield from v
    else:
        yield v


def main() -> int:
    canonical_pages = {
        "agency": {p.stem for p in WIKI_ORGS.glob("*.md")},
        "country": {p.stem for p in WIKI_COUNTRIES.glob("*.md")},
        "crime_type": {p.stem for p in WIKI_CRIMES.glob("*.md")},
    }
    bare_counts: dict[tuple[str, str], int] = Counter()
    bare_examples: dict[tuple[str, str], str] = {}

    fields = {
        "agency": ["participating_agencies", "lead_agency", "coordinating_body"],
        "country": ["participating_countries"],
        "crime_type": ["crime_type"],
    }

    parse_fail = 0
    scanned = 0
    for path in sorted(WIKI_OPS.glob("*.md")):
        if path.name == "_index.md":
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            parse_fail += 1
            continue
        if not isinstance(fm, dict):
            continue
        scanned += 1
        for kind, field_list in fields.items():
            for fname in field_list:
                for v in iter_values(fm.get(fname)):
                    cls = classify_value(v)
                    if cls is None or cls[0] != "bare":
                        continue
                    key = (kind, cls[1])
                    bare_counts[key] += 1
                    bare_examples.setdefault(key, path.stem)

    writer = csv.writer(sys.stdout)
    writer.writerow(
        ["kind", "raw_value", "normalized_slug", "has_canonical_page",
         "occurrence_count", "example_op"]
    )
    rows = []
    for (kind, raw), count in bare_counts.items():
        norm = normalize(raw)
        has_page = norm in canonical_pages[kind] if norm else False
        rows.append([kind, raw, norm, "yes" if has_page else "no", count, bare_examples[(kind, raw)]])
    rows.sort(key=lambda r: (r[0], -r[4], r[1]))
    for row in rows:
        writer.writerow(row)

    print(f"\n# Scanned: {scanned} ops, parse_fail: {parse_fail}", file=sys.stderr)
    print(f"# Unique bare entries: {len(rows)}", file=sys.stderr)
    for kind in ("agency", "country", "crime_type"):
        kc = sum(1 for r in rows if r[0] == kind)
        total = sum(r[4] for r in rows if r[0] == kind)
        canonical_hit = sum(1 for r in rows if r[0] == kind and r[3] == "yes")
        print(
            f"#   {kind}: {kc} unique / {total} occurrences "
            f"({canonical_hit} normalize to an existing canonical page)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
