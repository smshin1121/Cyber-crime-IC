#!/usr/bin/env python3
"""
Scan wiki/operations/*.md and produce the enrichment subset for SNA Step B.

Subset rule (user-approved, PoC v4 → Step B preparation):
  (a) operation has at least one Eurojust / Europol / INTERPOL-anchored source
      (source-page wikilink slug OR source URL OR lead/coordinating agency)
  (b) AND participating_countries count ≤ 1 after wikilink normalization

Output:
  _workspace/sna/enrichment-subset-<date>.csv
  _workspace/sna/enrichment-subset-<date>.json  (manifest)

Columns:
  slug, title, status, current_countries_count, current_countries,
  matched_via, source_urls_joined, lead_agency, coordinating_body

Rules the user locked:
  - source_backed_only (no estimation / inference during enrichment)
  - snapshot_date, subset_rule, matched_ops_count recorded in manifest
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("subset")

REPO = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO / "wiki" / "operations"
WORKSPACE = REPO / "_workspace" / "sna"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")

# Anchored-source matchers (all case-insensitive)
ANCHOR_SLUG_PATTERNS = ("eurojust", "europol", "interpol")
ANCHOR_URL_PATTERNS = (
    "eurojust.europa.eu",
    "europol.europa.eu",
    "interpol.int",
)
ANCHOR_AGENCY_SLUGS = {
    "eurojust",
    "europol-ec3",
    "europol",
    "interpol",
    "interpol-igci",
}


def extract_wikilink_slugs(val):
    if val is None:
        return []
    out = []
    pool = val if isinstance(val, list) else [val]
    for item in pool:
        if item is None:
            continue
        s = str(item)
        for m in WIKILINK_RE.finditer(s):
            out.append(m.group(1).strip())
    return out


def find_urls(sources):
    if sources is None:
        return []
    out = []
    pool = sources if isinstance(sources, list) else [sources]
    for item in pool:
        if item is None:
            continue
        s = str(item)
        # Extract http(s)://... up to whitespace or closing paren/bracket/quote
        for m in re.finditer(r'https?://[^\s\)\]"]+', s):
            out.append(m.group(0))
    return out


def classify_source_anchor(
    sources_raw, lead_slug: str | None, coord_slug: str | None
) -> list[str]:
    matched_via: list[str] = []
    # (a1) wikilink slug contains one of the anchor patterns
    wl_slugs = extract_wikilink_slugs(sources_raw)
    for slug in wl_slugs:
        slug_lower = slug.lower()
        for pat in ANCHOR_SLUG_PATTERNS:
            if pat in slug_lower:
                matched_via.append(f"source-wikilink:{slug}")
                break
    # (a2) URL pattern
    urls = find_urls(sources_raw)
    for u in urls:
        ul = u.lower()
        for pat in ANCHOR_URL_PATTERNS:
            if pat in ul:
                matched_via.append(f"source-url:{u}")
                break
    # (a3) lead / coord agency
    for slug, label in ((lead_slug, "lead_agency"), (coord_slug, "coordinating_body")):
        if slug and slug.lower() in ANCHOR_AGENCY_SLUGS:
            matched_via.append(f"{label}:{slug}")
    return matched_via


def git_short_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO, stderr=subprocess.DEVNULL
        )
        return out.decode("utf-8").strip()
    except Exception:
        return "nogit"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--snapshot-date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    )
    args = parser.parse_args()

    rows = []
    scanned = 0
    parse_fail = 0
    not_operation_type = 0
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
        if str(fm.get("type") or "").strip() != "operation":
            not_operation_type += 1
            continue
        scanned += 1

        # Count countries (after wikilink normalization; bare strings also count)
        countries_val = fm.get("participating_countries") or []
        country_ids: list[str] = []
        if isinstance(countries_val, list):
            for item in countries_val:
                if item is None:
                    continue
                s = str(item)
                wls = WIKILINK_RE.findall(s)
                if wls:
                    for w in wls:
                        w = w.strip()
                        if w and w not in country_ids:
                            country_ids.append(w)
                else:
                    s = s.strip()
                    if s and s not in country_ids:
                        country_ids.append(s)
        country_count = len(country_ids)
        if country_count > 1:
            continue

        lead_slugs = extract_wikilink_slugs(fm.get("lead_agency"))
        coord_slugs = extract_wikilink_slugs(fm.get("coordinating_body"))
        lead_slug = lead_slugs[0] if lead_slugs else None
        coord_slug = coord_slugs[0] if coord_slugs else None

        matched = classify_source_anchor(fm.get("sources"), lead_slug, coord_slug)
        if not matched:
            continue

        urls = find_urls(fm.get("sources"))
        rows.append({
            "slug": path.stem,
            "title": str(fm.get("title") or "").strip(),
            "status": str(fm.get("status") or "").strip(),
            "current_countries_count": country_count,
            "current_countries": "|".join(country_ids),
            "matched_via": "; ".join(matched),
            "source_urls_joined": "|".join(urls[:5]),
            "lead_agency": lead_slug or "",
            "coordinating_body": coord_slug or "",
        })

    rows.sort(key=lambda r: r["slug"])
    out_csv = WORKSPACE / f"enrichment-subset-{args.snapshot_date}.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "slug", "title", "status", "current_countries_count",
                "current_countries", "matched_via", "source_urls_joined",
                "lead_agency", "coordinating_body",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    manifest = {
        "snapshot_date": args.snapshot_date,
        "git_short_sha": git_short_sha(),
        "subset_rule": {
            "criteria_a_source_anchor": {
                "wikilink_slug_patterns": list(ANCHOR_SLUG_PATTERNS),
                "url_patterns": list(ANCHOR_URL_PATTERNS),
                "agency_slugs": sorted(ANCHOR_AGENCY_SLUGS),
            },
            "criteria_b_countries": "participating_countries_count <= 1 after wikilink normalization",
            "conjunction": "AND",
        },
        "enrichment_rules": {
            "source_backed_only": True,
            "inference_or_estimation": False,
            "must_record": [
                "snapshot_date",
                "subset_rule",
                "enriched_ops_count",
            ],
        },
        "scanned": scanned,
        "parse_fail": parse_fail,
        "not_operation_type": not_operation_type,
        "matched_ops_count": len(rows),
        "subset_csv": str(out_csv.relative_to(REPO)),
    }
    out_json = WORKSPACE / f"enrichment-subset-{args.snapshot_date}.json"
    with out_json.open("w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"\n=== Enrichment subset selection ===")
    print(f"scanned ops:          {scanned}")
    print(f"parse_fail:           {parse_fail}")
    print(f"matched subset size:  {len(rows)}")
    print(f"output CSV:           {out_csv.relative_to(REPO)}")
    print(f"output manifest:      {out_json.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
