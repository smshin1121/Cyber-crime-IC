#!/usr/bin/env python3
"""
Repair two YAML frontmatter quoting bugs found in wiki/operations/*.md.

Pattern A — stray inner quote after colon:
    - "AlphaBay: "400,000 users, 40,000 vendors\""
becomes:
    - "AlphaBay: 400,000 users, 40,000 vendors"

Pattern B — markdown-link URL with broken colon-space injection:
    - "[Title](https: "//example.com/path)\""
becomes:
    - "[Title](https://example.com/path)"

Usage:
    python tools/repair_yaml_quotes.py --dry-run   # show diffs, no writes
    python tools/repair_yaml_quotes.py             # apply repairs
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("repair")

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO_ROOT / "wiki" / "operations"

# Pattern B: URL-in-markdown-link. Apply FIRST (more specific).
#   ^(lead)"(\[label\])\((scheme): "//(url))\""$
PATTERN_B_RE = re.compile(
    r'^(?P<lead>[ \t]*-[ \t]+)'
    r'"(?P<label>\[[^\]]+?\])'
    r'\((?P<scheme>https?):[ \t]+"//(?P<url>[^)"]+)\)\\""[ \t]*$',
    re.MULTILINE,
)
PATTERN_B_SUB = r'\g<lead>"\g<label>(\g<scheme>://\g<url>)"'

# Pattern A: inner-quote-after-colon. Apply AFTER Pattern B.
#   ^(lead)"(pre): "(post)\""$
# pre and post exclude raw double-quotes and newlines. Lazy on pre so the
# *first* colon-space-quote triggers the match (the broken boundary).
PATTERN_A_RE = re.compile(
    r'^(?P<lead>[ \t]*-[ \t]+)'
    r'"(?P<pre>[^"\n]+?):[ \t]+"(?P<post>[^"\n]+?)\\""[ \t]*$',
    re.MULTILINE,
)
PATTERN_A_SUB = r'\g<lead>"\g<pre>: \g<post>"'


def split_frontmatter(text: str) -> tuple[str, str, str] | None:
    """Return (leading, frontmatter_body, rest) or None if no FM."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    # parts[0] is empty (before first `---`), parts[1] is the fm body,
    # parts[2] is the rest (starting with `\n` after closing `---`).
    leading = "---"
    fm_body = parts[1]
    rest = "---" + parts[2]
    return leading, fm_body, rest


def repair_text(fm_body: str) -> tuple[str, int, int]:
    """Return (new_body, count_B_repairs, count_A_repairs)."""
    new_body, b_count = PATTERN_B_RE.subn(PATTERN_B_SUB, fm_body)
    new_body, a_count = PATTERN_A_RE.subn(PATTERN_A_SUB, new_body)
    return new_body, b_count, a_count


def verify_parse(fm_body: str) -> str | None:
    """Return None if YAML parse OK, else error message."""
    try:
        yaml.safe_load(fm_body)
        return None
    except yaml.YAMLError as exc:
        return str(exc).splitlines()[0] if str(exc) else "unknown YAML error"


def process_file(path: Path, dry_run: bool) -> dict[str, object]:
    original = path.read_text(encoding="utf-8")
    pre_error = None
    post_error = None
    split = split_frontmatter(original)
    if split is None:
        return {"path": path.name, "status": "no-frontmatter"}
    leading, fm_body, rest = split
    pre_error = verify_parse(fm_body)
    new_fm, b_count, a_count = repair_text(fm_body)
    if b_count == 0 and a_count == 0:
        return {
            "path": path.name,
            "status": "no-change",
            "pre_parse_ok": pre_error is None,
        }
    post_error = verify_parse(new_fm)
    new_text = leading + new_fm + rest
    action = "dry-run" if dry_run else "wrote"
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return {
        "path": path.name,
        "status": action,
        "pattern_B_repairs": b_count,
        "pattern_A_repairs": a_count,
        "pre_parse_ok": pre_error is None,
        "post_parse_ok": post_error is None,
        "pre_error_head": pre_error,
        "post_error_head": post_error,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be repaired without writing.",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=WIKI_OPS,
        help="Directory to scan (default: wiki/operations/).",
    )
    args = parser.parse_args()

    reports: list[dict[str, object]] = []
    for path in sorted(args.path.glob("*.md")):
        if path.name == "_index.md":
            continue
        reports.append(process_file(path, args.dry_run))

    changed = [r for r in reports if r.get("status") in ("wrote", "dry-run")]
    still_broken = [
        r for r in changed if r.get("post_parse_ok") is False
    ]
    recovered = [
        r
        for r in changed
        if r.get("pre_parse_ok") is False and r.get("post_parse_ok") is True
    ]
    still_ok = [
        r
        for r in changed
        if r.get("pre_parse_ok") and r.get("post_parse_ok")
    ]

    print(f"\n=== Summary ===")
    print(f"files scanned:         {len(reports)}")
    print(f"files changed:         {len(changed)} ({'dry' if args.dry_run else 'written'})")
    print(f"  repaired (was broken, now parses):  {len(recovered)}")
    print(f"  cosmetic (was OK, still OK):        {len(still_ok)}")
    print(f"  still-broken after repair:          {len(still_broken)}")

    for r in changed:
        tag = "OK" if r.get("post_parse_ok") else "FAIL"
        line = (
            f"  [{tag}] {r['path']} "
            f"(B={r.get('pattern_B_repairs')} A={r.get('pattern_A_repairs')})"
        )
        if not r.get("pre_parse_ok"):
            line += f"  was-broken: {r.get('pre_error_head')}"
        if r.get("post_parse_ok") is False:
            line += f"  still-broken: {r.get('post_error_head')}"
        print(line)

    return 0 if len(still_broken) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
