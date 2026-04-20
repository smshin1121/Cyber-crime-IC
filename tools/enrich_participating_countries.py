#!/usr/bin/env python3
"""
Source-backed enrichment of `participating_countries` for the A subset.

Flow:
  1. Load subset from `_workspace/sna/enrichment-subset-<date>.csv`.
  2. For each op: resolve `sources:` wikilinks → wiki/sources/<slug>.md
     → read `key_findings:` text. Extract country mentions using a strict
     noun-form alias table (no adjective-only forms, no inference).
  3. Produce proposals CSV: `_workspace/sna/enrichment-proposals-<date>.csv`
     columns:
       slug, current_countries, proposed_add, proposed_keep, evidence_source,
       evidence_snippet, confidence, status
     where:
       status ∈ {no_sources, no_key_findings, no_extract, empty_delta, ready}
  4. With --apply, rewrite the `participating_countries:` block on each op
     whose status is `ready` — additive only (union with existing
     non-placeholder countries). Placeholder `"international"` (and similar)
     is removed during the rewrite.

Lock rules (user):
  - source-backed only, no inference, no estimation
  - snapshot_date + subset_rule + enriched_ops_count recorded in manifest
  - placeholder-only values ("international") treated as empty
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("enrich")

REPO = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO / "wiki" / "operations"
WIKI_SRC = REPO / "wiki" / "sources"
WIKI_CTRY = REPO / "wiki" / "countries"
WORKSPACE = REPO / "_workspace" / "sna"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")

PLACEHOLDERS = {"international", "global", "worldwide", "various"}


def canonical_country_slugs() -> set[str]:
    return {p.stem for p in WIKI_CTRY.glob("*.md") if p.stem != "_index"}


def build_country_alias_table() -> dict[str, str]:
    """Return {lowercase_noun_form: canonical_slug}. Conservative — noun forms only.
    Adjective-only matches (e.g., "French", "German") are deliberately excluded
    to prevent false positives from narrative text like "French authorities."
    """
    slugs = canonical_country_slugs()
    aliases: dict[str, str] = {}
    for slug in slugs:
        aliases[slug.replace("-", " ")] = slug
        # Title-cased form
        aliases[slug.replace("-", " ").title().lower()] = slug

    # Curated noun-form extras (common abbreviations, "the X", alt names).
    curated = {
        "us": "united-states",
        "u.s.": "united-states",
        "u.s.a.": "united-states",
        "usa": "united-states",
        "united states of america": "united-states",
        "america": "united-states",
        "the united states": "united-states",
        "uk": "united-kingdom",
        "u.k.": "united-kingdom",
        "britain": "united-kingdom",
        "great britain": "united-kingdom",
        "the united kingdom": "united-kingdom",
        "korea": "south-korea",
        "south korea": "south-korea",
        "republic of korea": "south-korea",
        "the republic of korea": "south-korea",
        "netherlands": "netherlands",
        "the netherlands": "netherlands",
        "holland": "netherlands",
        "czech republic": "czechia",
        "czechia": "czechia",
        "uae": "united-arab-emirates",
    }
    for k, v in curated.items():
        if v in slugs:
            aliases[k] = v
    # Strip aliases shorter than 2 chars to avoid tiny-match false positives.
    return {k: v for k, v in aliases.items() if len(k) >= 2}


def normalize_bare(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.strip().lower()).strip("-")


def current_country_ids(fm_countries) -> list[str]:
    """Return list of current country node ids with placeholders treated as empty."""
    out: list[str] = []
    if fm_countries is None:
        return out
    pool = fm_countries if isinstance(fm_countries, list) else [fm_countries]
    for item in pool:
        if item is None:
            continue
        s = str(item).strip()
        if not s:
            continue
        wls = WIKILINK_RE.findall(s)
        if wls:
            for w in wls:
                w = w.strip()
                if w and w.lower() not in PLACEHOLDERS and w not in out:
                    out.append(w)
        else:
            slug = normalize_bare(s)
            if slug and slug not in PLACEHOLDERS and slug not in out:
                out.append(slug)
    return out


def extract_source_wikilinks(sources_field) -> list[str]:
    out: list[str] = []
    if sources_field is None:
        return out
    pool = sources_field if isinstance(sources_field, list) else [sources_field]
    for item in pool:
        if item is None:
            continue
        s = str(item)
        for m in WIKILINK_RE.finditer(s):
            slug = m.group(1).strip()
            if slug and slug not in out:
                out.append(slug)
    return out


def read_source_key_findings(source_slug: str) -> tuple[str, str] | None:
    """Return (concatenated_findings_text, source_path_relative) or None if
    source page absent / unreadable."""
    path = WIKI_SRC / f"{source_slug}.md"
    if not path.exists():
        return None
    try:
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1]) or {}
    except (yaml.YAMLError, IndexError):
        return None
    kf = fm.get("key_findings")
    if not kf:
        return None
    if isinstance(kf, list):
        text = " ".join(str(x) for x in kf if x)
    else:
        text = str(kf)
    return text, str(path.relative_to(REPO)).replace("\\", "/")


def extract_countries_from_text(text: str, aliases: dict[str, str]) -> set[str]:
    """Return canonical slugs whose noun-form alias appears in text, whole-word."""
    out: set[str] = set()
    lower = text.lower()
    for alias, canon in aliases.items():
        # Whole-word match (alias may contain spaces/dots).
        pattern = r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])"
        if re.search(pattern, lower):
            out.add(canon)
    return out


# ---------------------------------------------------------------------------
# Line-based YAML rewrite of participating_countries block
# ---------------------------------------------------------------------------

FM_END_RE = re.compile(r"^---\s*$")
BLOCK_START_RE = re.compile(r"^participating_countries:\s*$")
NEXT_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*:\s*(?:\S.*)?$")


def rewrite_participating_countries(
    text: str, new_slugs_sorted: list[str]
) -> tuple[str, bool]:
    """Replace the `participating_countries:` block with a list of wikilinks.
    Preserves block position. Empty `new_slugs_sorted` writes an empty key.
    Returns (new_text, changed).
    """
    lines = text.splitlines(keepends=True)
    in_fm = False
    fm_count = 0
    block_start: int | None = None
    block_end: int | None = None  # exclusive
    for i, line in enumerate(lines):
        stripped = line.rstrip("\r\n")
        if FM_END_RE.match(stripped):
            fm_count += 1
            in_fm = fm_count == 1
            if fm_count == 2 and block_start is not None and block_end is None:
                block_end = i
            continue
        if not in_fm:
            continue
        if block_start is None:
            if BLOCK_START_RE.match(stripped):
                block_start = i
                continue
        else:
            # Inside block
            if (
                stripped
                and not stripped.startswith(("  ", "\t", "- ", " -"))
                and NEXT_KEY_RE.match(stripped)
            ):
                block_end = i
                break

    if block_start is None:
        # No participating_countries key — insert after a known anchor (e.g., timeframe end)?
        # Conservative: do not synthesize the block. Skip with no change.
        return text, False

    if block_end is None:
        # Block extends to end of frontmatter (not found a next key before FM end)
        block_end = len(lines)

    # Build replacement lines
    if new_slugs_sorted:
        new_block = ["participating_countries:\n"] + [
            f'  - "[[{s}]]"\n' for s in new_slugs_sorted
        ]
    else:
        # Preserve empty-list convention (key present, empty list).
        new_block = ["participating_countries: []\n"]

    new_lines = lines[:block_start] + new_block + lines[block_end:]
    new_text = "".join(new_lines)
    return new_text, (new_text != text)


# ---------------------------------------------------------------------------
# Proposal generation
# ---------------------------------------------------------------------------

def build_proposals(
    subset_rows: list[dict], aliases: dict[str, str]
) -> list[dict]:
    proposals: list[dict] = []
    canonical = canonical_country_slugs()
    for r in subset_rows:
        slug = r["slug"]
        op_path = WIKI_OPS / f"{slug}.md"
        text = op_path.read_text(encoding="utf-8")
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
        current = current_country_ids(fm.get("participating_countries"))
        source_wlinks = extract_source_wikilinks(fm.get("sources"))
        status = "ready"
        evidence_source = ""
        evidence_snippet = ""
        extracted: set[str] = set()
        if not source_wlinks:
            status = "no_sources"
        else:
            kf_hits = 0
            for sw in source_wlinks:
                got = read_source_key_findings(sw)
                if got is None:
                    continue
                findings_text, src_path = got
                kf_hits += 1
                hits = extract_countries_from_text(findings_text, aliases)
                if hits:
                    if not evidence_source:
                        evidence_source = src_path
                        evidence_snippet = findings_text[:280]
                    extracted |= hits
            if kf_hits == 0:
                status = "no_key_findings"
            elif not extracted:
                status = "no_extract"
        if status == "ready":
            # Keep only canonical slugs. Drop placeholders.
            filtered = {s for s in extracted if s in canonical and s not in PLACEHOLDERS}
            add = sorted(filtered - set(current))
            keep = sorted(set(current) & canonical)
            if not add and not keep:
                status = "empty_delta"
            final = sorted(set(add) | set(keep))
        else:
            add = []
            keep = sorted(set(current) & canonical)
            final = keep
        proposals.append({
            "slug": slug,
            "status": status,
            "current_countries": "|".join(current),
            "proposed_add": "|".join(add),
            "proposed_keep": "|".join(keep),
            "proposed_final": "|".join(final),
            "evidence_source": evidence_source,
            "evidence_snippet": evidence_snippet,
        })
    return proposals


def git_sha() -> str:
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
    parser.add_argument(
        "--subset-csv",
        type=Path,
        default=None,
        help="Override subset CSV path. Default: matches snapshot-date.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply proposed changes to operation pages. Without this, only "
             "proposals CSV + manifest are written.",
    )
    args = parser.parse_args()

    subset_csv = args.subset_csv or WORKSPACE / f"enrichment-subset-{args.snapshot_date}.csv"
    if not subset_csv.exists():
        # Try most recent
        candidates = sorted(WORKSPACE.glob("enrichment-subset-*.csv"))
        if not candidates:
            log.error("No enrichment-subset CSV found in %s", WORKSPACE)
            return 2
        subset_csv = candidates[-1]
        log.info("Falling back to %s", subset_csv.name)

    subset_rows = list(csv.DictReader(subset_csv.open(encoding="utf-8")))
    log.info("subset loaded: %d ops from %s", len(subset_rows), subset_csv.name)

    aliases = build_country_alias_table()
    log.info("country alias table: %d entries", len(aliases))

    proposals = build_proposals(subset_rows, aliases)

    proposals_csv = WORKSPACE / f"enrichment-proposals-{args.snapshot_date}.csv"
    with proposals_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "slug", "status", "current_countries",
                "proposed_add", "proposed_keep", "proposed_final",
                "evidence_source", "evidence_snippet",
            ],
        )
        writer.writeheader()
        writer.writerows(proposals)

    status_counts: dict[str, int] = {}
    for p in proposals:
        status_counts[p["status"]] = status_counts.get(p["status"], 0) + 1

    applied_count = 0
    applied_detail: list[dict] = []
    if args.apply:
        for p in proposals:
            if p["status"] != "ready":
                continue
            if not p["proposed_add"]:
                # No additions needed beyond existing — skip to avoid churn
                continue
            op_path = WIKI_OPS / f"{p['slug']}.md"
            original = op_path.read_text(encoding="utf-8")
            new_slugs = [s for s in p["proposed_final"].split("|") if s]
            new_text, changed = rewrite_participating_countries(original, new_slugs)
            if not changed:
                continue
            op_path.write_text(new_text, encoding="utf-8")
            applied_count += 1
            applied_detail.append({
                "slug": p["slug"],
                "added": p["proposed_add"],
                "final": p["proposed_final"],
            })

    manifest = {
        "snapshot_date": args.snapshot_date,
        "git_sha": git_sha(),
        "subset_csv": str(subset_csv.relative_to(REPO)),
        "subset_size": len(subset_rows),
        "proposals_csv": str(proposals_csv.relative_to(REPO)),
        "status_counts": status_counts,
        "subset_rule": {
            "description": "ops with Eurojust/Europol/INTERPOL-anchored source AND participating_countries count <= 1",
            "file": "_workspace/sna/enrichment-subset-<date>.json",
        },
        "enrichment_rules": {
            "source_backed_only": True,
            "inference_or_estimation_allowed": False,
            "placeholder_values_treated_as_empty": sorted(PLACEHOLDERS),
            "noun_form_alias_matching_only": True,
        },
        "applied": args.apply,
        "enriched_ops_count": applied_count,
        "applied_detail": applied_detail,
    }
    manifest_path = WORKSPACE / f"enrichment-proposals-{args.snapshot_date}.json"
    with manifest_path.open("w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"\n=== Enrichment ({'APPLIED' if args.apply else 'dry-run'}) ===")
    print(f"subset size:          {len(subset_rows)}")
    print(f"proposals CSV:        {proposals_csv.relative_to(REPO)}")
    print(f"manifest:             {manifest_path.relative_to(REPO)}")
    for status in ("ready", "no_sources", "no_key_findings", "no_extract", "empty_delta"):
        if status in status_counts:
            print(f"  status={status:18s} {status_counts[status]}")
    if args.apply:
        print(f"\noperations rewritten: {applied_count}")
        for d in applied_detail:
            print(f"  + {d['slug']}  (added: {d['added']})")
    else:
        print(f"\n(no files modified - pass --apply to rewrite op frontmatter)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
