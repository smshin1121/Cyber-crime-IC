"""
Build a prioritized URL queue for web-based participating_countries
verification.

Reads the latest .verification/participating_countries_audit.md, picks
the top-N ops with most unverified countries, extracts primary-source
URLs from each op's cited sources (`collection_url` fields in
wiki/sources/*.md), and writes `.verification/verify_queue.json`.

Run:
    python tools/collect_verify_queue.py --top 30
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / ".verification" / "participating_countries_audit.md"
OPS = ROOT / "wiki" / "operations"
SOURCES = ROOT / "wiki" / "sources"
QUEUE = ROOT / ".verification" / "verify_queue.json"


def load_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def parse_report_top(n: int) -> list[tuple[str, int, int, list[str]]]:
    """Return list of (op_slug, verified, unverified, unverified_countries)."""
    if not REPORT.exists():
        return []
    lines = REPORT.read_text(encoding="utf-8").splitlines()
    started = False
    out: list[tuple[str, int, int, list[str]]] = []
    for line in lines:
        if line.startswith("## Operations with unverified"):
            started = True
            continue
        if started and line.startswith("## "):
            break
        if not started or not line.startswith("| [["):
            continue
        m = re.match(
            r"\|\s*\[\[([^\]]+)\]\]\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*\d+\s*\|\s*([^|]*)\|",
            line,
        )
        if not m:
            continue
        slug = m.group(1).strip()
        verified = int(m.group(2))
        unverified = int(m.group(3))
        raw_list = m.group(5).strip()
        countries = [c.strip() for c in raw_list.split(",") if c.strip() and not c.strip().startswith("…")]
        out.append((slug, verified, unverified, countries))
    return out[:n]


def wikilink_to_slug(val: str) -> str:
    m = re.match(r"\[\[([^\|\]]+)", val.strip())
    return m.group(1).strip().lower() if m else val.strip().lower()


def source_url(ref: str) -> dict | None:
    ref_str = str(ref).strip()
    # Case 1 — inline markdown link: "[Title](https://...)"
    md_link = re.search(r"\[([^\]]+)\]\((https?://[^\s\)]+)\)", ref_str)
    if md_link:
        return {
            "source_slug": md_link.group(1)[:80],
            "url": md_link.group(2),
            "publisher": "",
            "reliability": "",
            "source_type": "",
            "publish_date": "",
        }
    # Case 2 — plain URL anywhere in the string
    raw_url = re.search(r"(https?://[^\s\)]+)", ref_str)
    if raw_url and not ref_str.startswith("[["):
        return {
            "source_slug": raw_url.group(1)[-60:],
            "url": raw_url.group(1),
            "publisher": "",
            "reliability": "",
            "source_type": "",
            "publish_date": "",
        }
    # Case 3 — wikilink to a wiki/sources/*.md page
    slug = wikilink_to_slug(ref_str)
    path = SOURCES / f"{slug}.md"
    if not path.exists():
        return None
    fm = load_frontmatter(path)
    url = (fm.get("collection_url") or fm.get("source_url")
           or fm.get("url") or "")
    if not url:
        return None
    return {
        "source_slug": slug,
        "url": url,
        "publisher": fm.get("publisher", ""),
        "reliability": fm.get("reliability", ""),
        "source_type": fm.get("source_type", ""),
        "publish_date": str(fm.get("publish_date", "")),
    }


def build_queue(top_n: int) -> list[dict]:
    queue: list[dict] = []
    for slug, verified, unverified, countries in parse_report_top(top_n):
        op_path = OPS / f"{slug}.md"
        if not op_path.exists():
            continue
        fm = load_frontmatter(op_path)
        srcs = fm.get("sources") or []
        urls: list[dict] = []
        for s in srcs:
            if not s:
                continue
            info = source_url(str(s))
            if info:
                urls.append(info)
        queue.append({
            "op_slug": slug,
            "op_title": fm.get("title", slug),
            "verified_local": verified,
            "unverified_local": unverified,
            "unverified_countries": countries,
            "participating_countries": [wikilink_to_slug(str(x)) for x in (fm.get("participating_countries") or [])],
            "source_urls": urls,
        })
    return queue


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=30)
    args = ap.parse_args()

    queue = build_queue(args.top)
    QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")

    with_url = sum(1 for q in queue if q["source_urls"])
    print(f"[queue] {len(queue)} ops; {with_url} have at least one source URL")
    print(f"[queue] written to {QUEUE}")
    if queue:
        print("[queue] top 5 targets:")
        for q in queue[:5]:
            print(f"  - {q['op_slug']}: unverified={q['unverified_local']}, urls={len(q['source_urls'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
