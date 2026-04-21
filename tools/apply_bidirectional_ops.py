"""
For every fully-verified operation in .verification/web_verified.md,
ensure each country in its participating_countries has the op listed
in its `operations_participated` frontmatter.

Idempotent — re-runs safely. Does not remove anything. Only appends
missing bidirectional back-links. Intended for the L19 "verified"
bucket: once the primary source explicitly names a country, the
country page should carry the back-link.

Run:
    python tools/apply_bidirectional_ops.py            # dry-run
    python tools/apply_bidirectional_ops.py --apply    # write changes
"""
from __future__ import annotations
import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


ROOT = Path(__file__).resolve().parent.parent
COUNTRIES = ROOT / "wiki" / "countries"
REPORT = ROOT / ".verification" / "web_verified.md"


def parse_report_verified_ops() -> list[tuple[str, list[str]]]:
    """Return list of (op_slug, verified_countries) for fully-verified ops."""
    if not REPORT.exists():
        return []
    text = REPORT.read_text(encoding="utf-8")
    out: list[tuple[str, list[str]]] = []
    for m in re.finditer(
        r"### ([\w\-]+).*?\*\*Verified via web \((\d+)\)\*\*: ([^\n]+).*?"
        r"\*\*Still missing \((\d+)\)\*\*: ([^\n]+)",
        text, re.DOTALL,
    ):
        slug = m.group(1).strip()
        n_missing = int(m.group(4))
        verified_raw = m.group(3).strip()
        if verified_raw == "—":
            continue
        verified = [c.strip() for c in verified_raw.split(",") if c.strip() and c.strip() != "—"]
        if n_missing == 0 and verified:
            out.append((slug, verified))
    return out


def patch_country(country_slug: str, op_slug: str, apply: bool) -> str:
    path = COUNTRIES / f"{country_slug}.md"
    if not path.exists():
        return "missing_country_page"
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return "no_frontmatter"
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return "bad_yaml"
    current = fm.get("operations_participated") or []
    if not isinstance(current, list):
        current = []
    current_slugs = {
        re.match(r"\[\[([^\|\]]+)", str(e).strip()).group(1).lower()
        if isinstance(e, str) and str(e).startswith("[[") else str(e).lower()
        for e in current
    }
    if op_slug.lower() in current_slugs:
        return "already_linked"
    if not apply:
        return "would_add"
    new_entry = f"'[[{op_slug}]]'"
    # find the last line of operations_participated list; if list is empty
    # (the key maps to []), we need to turn it into a block list.
    pattern_block = re.compile(
        r"^operations_participated:\s*\n((?:- [^\n]*\n)+)", re.MULTILINE
    )
    m_block = pattern_block.search(text)
    if m_block:
        inserted = m_block.group(0) + f"- {new_entry}\n"
        text = text[: m_block.start()] + inserted + text[m_block.end():]
    else:
        # empty list form: `operations_participated: []`
        text = re.sub(
            r"^operations_participated:\s*\[\s*\]\s*$",
            f"operations_participated:\n- {new_entry}",
            text, count=1, flags=re.MULTILINE,
        )
    # bump updated to today
    today = date.today().isoformat()
    text = re.sub(r"^updated:\s*\S.*$", f"updated: {today}", text, count=1,
                  flags=re.MULTILINE)
    path.write_text(text, encoding="utf-8")
    return "added"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="Write changes (default: dry-run)")
    args = ap.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[L19-apply] mode: {mode}", flush=True)

    ops = parse_report_verified_ops()
    print(f"[L19-apply] fully-verified ops from report: {len(ops)}", flush=True)

    totals = {"added": 0, "already_linked": 0, "would_add": 0,
              "missing_country_page": 0, "no_frontmatter": 0, "bad_yaml": 0}
    for op_slug, countries in ops:
        for c in countries:
            result = patch_country(c, op_slug, apply=args.apply)
            totals[result] = totals.get(result, 0) + 1
            if result in ("added", "would_add", "missing_country_page"):
                print(f"  {op_slug} -> {c}: {result}", flush=True)

    print("\n[L19-apply] summary:", flush=True)
    for k, v in totals.items():
        print(f"  {k}: {v}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
