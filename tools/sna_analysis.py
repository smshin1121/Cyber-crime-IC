#!/usr/bin/env python3
"""
SNA snapshot + basic metrics for cybercrime IC operations.

PoC reproduction of paper.pdf methodology — 2-mode networks of
operation × {country, agency, crime-type}. Outputs edge lists,
node metadata, cohesion metrics, and centrality tables.

Spec:
- _workspace/sna/paper-network-definitions.md
- _workspace/sna/edge-schema-and-inclusion-rules.md

Usage:
    python tools/sna_analysis.py                      # default snapshot today
    python tools/sna_analysis.py --snapshot-date 2026-04-20
    python tools/sna_analysis.py --out-dir custom/dir
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import networkx as nx
import pandas as pd
import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("sna")

REPO_ROOT = Path(__file__).resolve().parents[1]
WIKI_OPS = REPO_ROOT / "wiki" / "operations"
WIKI_ORGS = REPO_ROOT / "wiki" / "organizations"
WIKI_COUNTRIES = REPO_ROOT / "wiki" / "countries"
WIKI_CRIMES = REPO_ROOT / "wiki" / "crime-types"
WORKSPACE_SNA = REPO_ROOT / "_workspace" / "sna"
AUDIT_DENYLIST = WORKSPACE_SNA / "audit-denylist.txt"
SPEC_PAPER = WORKSPACE_SNA / "paper-network-definitions.md"
SPEC_RULES = WORKSPACE_SNA / "edge-schema-and-inclusion-rules.md"
ALIAS_MAP_FILE = WORKSPACE_SNA / "node-alias-map.yaml"

RULES_VERSION = "poc-v4"

LIVE_STATUSES = {"completed", "ongoing"}
ENFORCEMENT_KEYWORDS = {
    "arrest",
    "seizure",
    "takedown",
    "extradition",
    "indictment",
    "asset_freeze",
}

# Soft domestic-followon patterns. Applied only when participating_countries ≤ 2.
DOMESTIC_FOLLOWON_PATTERNS = [
    re.compile(r"^operation-us-v-"),
    re.compile(r"-(man|woman)-(sentenced|pleads-guilty|pleaded-guilty|indicted-for)"),
    re.compile(r"-(sentenced|pleads-guilty|pleaded-guilty)-for-"),
]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
NORMALIZE_BARE_RE = re.compile(r"[^a-z0-9]+")


def normalize_bare_string(s: str) -> str:
    """Slugify a bare (non-wikilink) string: lowercase, non-alphanumeric → hyphen,
    collapse, trim. Returns '' if nothing alphanumeric remains."""
    return NORMALIZE_BARE_RE.sub("-", s.strip().lower()).strip("-")


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------

@dataclass
class OpRecord:
    slug: str
    title: str | None
    status: str | None
    period: int | None
    outcome: str | None
    lead_agency: str | None
    coordinating_body: str | None
    timeframe_announced: str | None
    source_count: int | None
    enforcement_type: list[str]
    countries: list[str]
    agencies: list[str]
    crime_types: list[str]        # canonical (list-valued, PoC v4)
    crime_type_fallback_used: bool = False  # diagnostic: True if read from legacy single field


@dataclass
class ExclusionReport:
    not_operation_type: list[str] = field(default_factory=list)
    parse_error: list[str] = field(default_factory=list)
    countries_lt_2: list[str] = field(default_factory=list)
    agencies_lt_2: list[str] = field(default_factory=list)
    crime_type_missing: list[str] = field(default_factory=list)
    status_not_live: list[str] = field(default_factory=list)
    no_enforcement_action: list[str] = field(default_factory=list)
    audit_denylist: list[str] = field(default_factory=list)
    domestic_followon_pattern: list[str] = field(default_factory=list)

    def as_counts(self) -> dict[str, int]:
        return {k: len(v) for k, v in self.__dict__.items()}

    def rows_for_csv(self) -> list[tuple[str, str]]:
        rows: list[tuple[str, str]] = []
        for reason, slugs in self.__dict__.items():
            for slug in slugs:
                rows.append((slug, reason))
        rows.sort()
        return rows


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

# Module-level counters populated by extract_wikilinks. Reset per run in main().
_BARE_NORM_STATS: dict[str, int] = {"normalized": 0, "empty_dropped": 0}


def extract_wikilinks(value: Any) -> list[str]:
    """Collect canonical slug(s) from a YAML value.

    - Wikilinks `[[slug]]` pass through verbatim.
    - Bare (non-wikilink) strings are slugified via normalize_bare_string
      and counted in _BARE_NORM_STATS. Empty-after-normalization strings
      are dropped and counted.
    """
    if value is None:
        return []
    items: list[str] = []
    if isinstance(value, list):
        pool = value
    else:
        pool = [value]
    for item in pool:
        if item is None:
            continue
        s = str(item).strip()
        if not s:
            continue
        matches = WIKILINK_RE.findall(s)
        if matches:
            items.extend(m.strip() for m in matches)
        else:
            normalized = normalize_bare_string(s)
            if normalized:
                _BARE_NORM_STATS["normalized"] += 1
                items.append(normalized)
            else:
                _BARE_NORM_STATS["empty_dropped"] += 1
    seen: set[str] = set()
    out: list[str] = []
    for s in items:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        log.warning("read error: %s (%s)", path.name, exc)
        return None
    if not text.startswith("---"):
        return None
    # split off the first frontmatter block
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    fm_text = parts[1]
    try:
        data = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        log.warning("YAML parse error: %s (%s)", path.name, exc)
        return None
    return data if isinstance(data, dict) else None


def build_record(path: Path, fm: dict[str, Any]) -> OpRecord:
    slug = path.stem
    enforcement = fm.get("enforcement_type") or []
    if isinstance(enforcement, str):
        enforcement = [enforcement]
    countries = extract_wikilinks(fm.get("participating_countries"))
    agencies = extract_wikilinks(fm.get("participating_agencies"))
    # Add lead/coordinating to agency set (per spec §1 field mapping)
    for field_name in ("lead_agency", "coordinating_body"):
        for slug_id in extract_wikilinks(fm.get(field_name)):
            if slug_id not in agencies:
                agencies.append(slug_id)
    # Canonical: crime_types list. Fallback: legacy crime_type single value
    # (read-only during PoC v4 migration).
    crime_types = extract_wikilinks(fm.get("crime_types"))
    fallback_used = False
    if not crime_types:
        legacy = extract_wikilinks(fm.get("crime_type"))
        if legacy:
            crime_types = legacy
            fallback_used = True
    timeframe = fm.get("timeframe") or {}
    timeframe_announced = None
    if isinstance(timeframe, dict):
        timeframe_announced = timeframe.get("announced")
    return OpRecord(
        slug=slug,
        title=str(fm.get("title") or "") or None,
        status=(str(fm.get("status")).strip().lower() if fm.get("status") else None),
        period=fm.get("period") if isinstance(fm.get("period"), int) else None,
        outcome=str(fm.get("outcome")) if fm.get("outcome") else None,
        lead_agency=(extract_wikilinks(fm.get("lead_agency")) or [None])[0],
        coordinating_body=(extract_wikilinks(fm.get("coordinating_body")) or [None])[0],
        timeframe_announced=str(timeframe_announced) if timeframe_announced else None,
        source_count=int(fm.get("source_count")) if isinstance(fm.get("source_count"), int) else None,
        enforcement_type=[str(x).strip().lower() for x in enforcement if x],
        countries=countries,
        agencies=agencies,
        crime_types=crime_types,
        crime_type_fallback_used=fallback_used,
    )


def load_denylist() -> set[str]:
    if not AUDIT_DENYLIST.exists():
        return set()
    deny: set[str] = set()
    for line in AUDIT_DENYLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        deny.add(line)
    return deny


def load_alias_map() -> dict[str, dict[str, str]]:
    """Return {kind: {raw_slug: canonical_slug}}. Empty if file missing."""
    if not ALIAS_MAP_FILE.exists():
        return {"agency": {}, "country": {}, "crime_type": {}}
    data = yaml.safe_load(ALIAS_MAP_FILE.read_text(encoding="utf-8")) or {}
    return {
        "agency": dict(data.get("agency") or {}),
        "country": dict(data.get("country") or {}),
        "crime_type": dict(data.get("crime_type") or {}),
    }


def apply_alias(slug: str, table: dict[str, str]) -> str:
    """Return canonical slug if mapped, else the input."""
    return table.get(slug, slug)


def canonicalize_record(
    rec: OpRecord, alias_map: dict[str, dict[str, str]]
) -> OpRecord:
    """Return a new OpRecord with aliased slugs replaced. Preserves order and dedups."""
    a_tbl = alias_map.get("agency", {})
    c_tbl = alias_map.get("country", {})
    t_tbl = alias_map.get("crime_type", {})

    def dedup(items: list[str], table: dict[str, str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for s in items:
            canonical = apply_alias(s, table)
            if canonical not in seen:
                seen.add(canonical)
                out.append(canonical)
        return out

    new_agencies = dedup(rec.agencies, a_tbl)
    new_countries = dedup(rec.countries, c_tbl)
    new_crime_types = dedup(rec.crime_types, t_tbl)
    new_lead = apply_alias(rec.lead_agency, a_tbl) if rec.lead_agency else rec.lead_agency
    new_coord = (
        apply_alias(rec.coordinating_body, a_tbl) if rec.coordinating_body else rec.coordinating_body
    )
    return OpRecord(
        slug=rec.slug,
        title=rec.title,
        status=rec.status,
        period=rec.period,
        outcome=rec.outcome,
        lead_agency=new_lead,
        coordinating_body=new_coord,
        timeframe_announced=rec.timeframe_announced,
        source_count=rec.source_count,
        enforcement_type=rec.enforcement_type,
        countries=new_countries,
        agencies=new_agencies,
        crime_types=new_crime_types,
        crime_type_fallback_used=rec.crime_type_fallback_used,
    )


def count_alias_hits(
    records: list[OpRecord], alias_map: dict[str, dict[str, str]]
) -> dict[str, dict[str, int]]:
    """Count how many records each alias mapping merges."""
    hits: dict[str, dict[str, int]] = {"agency": {}, "country": {}, "crime_type": {}}
    for rec in records:
        for s in rec.agencies:
            if s in alias_map["agency"]:
                hits["agency"][s] = hits["agency"].get(s, 0) + 1
        for s in rec.countries:
            if s in alias_map["country"]:
                hits["country"][s] = hits["country"].get(s, 0) + 1
        for s in rec.crime_types:
            if s in alias_map["crime_type"]:
                hits["crime_type"][s] = hits["crime_type"].get(s, 0) + 1
    return hits


# ---------------------------------------------------------------------------
# Inclusion filter
# ---------------------------------------------------------------------------

def apply_inclusion(
    records: list[OpRecord],
    denylist: set[str],
) -> tuple[list[OpRecord], ExclusionReport]:
    kept: list[OpRecord] = []
    report = ExclusionReport()
    for rec in records:
        # Rule 9: audit denylist (hard — before any soft rule)
        if rec.slug in denylist:
            report.audit_denylist.append(rec.slug)
            continue
        # Rule 1-2 are upstream (file was loaded)
        # Rule 6: status
        if rec.status not in LIVE_STATUSES:
            report.status_not_live.append(rec.slug)
            continue
        # Rule 3
        if len(rec.countries) < 2:
            report.countries_lt_2.append(rec.slug)
            continue
        # Rule 4
        if len(rec.agencies) < 2:
            report.agencies_lt_2.append(rec.slug)
            continue
        # Rule 5
        if not rec.crime_types:
            report.crime_type_missing.append(rec.slug)
            continue
        # Rule 7: enforcement_type non-empty AND contains keyword
        if not any(
            any(kw in ev for kw in ENFORCEMENT_KEYWORDS) for ev in rec.enforcement_type
        ):
            report.no_enforcement_action.append(rec.slug)
            continue
        # Rule 8 (soft): domestic-followon regex AND countries ≤ 2
        if len(rec.countries) <= 2 and any(
            p.search(rec.slug) for p in DOMESTIC_FOLLOWON_PATTERNS
        ):
            report.domestic_followon_pattern.append(rec.slug)
            continue
        kept.append(rec)
    return kept, report


# ---------------------------------------------------------------------------
# Graph + metrics
# ---------------------------------------------------------------------------

def build_bipartite(
    records: list[OpRecord],
    mode2_attr: str,
    mode2_prefix: str,
) -> tuple[nx.Graph, list[str], list[str]]:
    """Return (G, op_nodes, mode2_nodes). Node ids prefixed to avoid collisions."""
    G = nx.Graph()
    op_nodes: list[str] = []
    m2_nodes_set: set[str] = set()
    for rec in records:
        op_id = f"op::{rec.slug}"
        G.add_node(op_id, bipartite=0, kind="op", slug=rec.slug)
        op_nodes.append(op_id)
        values = getattr(rec, mode2_attr)
        if isinstance(values, str):
            values = [values] if values else []
        elif values is None:
            values = []
        for raw in values:
            if not raw:
                continue
            m2_id = f"{mode2_prefix}::{raw}"
            if m2_id not in m2_nodes_set:
                G.add_node(m2_id, bipartite=1, kind=mode2_prefix, slug=raw)
                m2_nodes_set.add(m2_id)
            G.add_edge(op_id, m2_id)
    op_nodes.sort()
    m2_nodes = sorted(m2_nodes_set)
    return G, op_nodes, m2_nodes


def cohesion_metrics(G: nx.Graph, top_nodes: list[str]) -> dict[str, Any]:
    n = G.number_of_nodes()
    m = G.number_of_edges()
    density = nx.bipartite.density(G, set(top_nodes)) if top_nodes else 0.0
    components = list(nx.connected_components(G))
    component_sizes = sorted((len(c) for c in components), reverse=True)
    # Fragmentation: 1 - Σ n_c * (n_c - 1) / (N * (N - 1))
    if n > 1:
        fragmentation = 1.0 - sum(
            s * (s - 1) for s in component_sizes
        ) / (n * (n - 1))
    else:
        fragmentation = 0.0
    largest = max(components, key=len) if components else set()
    sub = G.subgraph(largest).copy() if largest else G
    try:
        avg_distance = nx.average_shortest_path_length(sub) if sub.number_of_nodes() > 1 else 0.0
    except nx.NetworkXError:
        avg_distance = float("nan")
    try:
        diameter = nx.diameter(sub) if sub.number_of_nodes() > 1 else 0
        radius = nx.radius(sub) if sub.number_of_nodes() > 1 else 0
    except nx.NetworkXError:
        diameter = 0
        radius = 0
    # Transitivity on 1-mode projection of mode-2 side (the non-operation side)
    mode2_nodes = [v for v in G.nodes() if v not in set(top_nodes)]
    if mode2_nodes:
        try:
            proj = nx.bipartite.projected_graph(G, mode2_nodes)
            transitivity = nx.transitivity(proj)
        except Exception as exc:
            log.warning("projection transitivity failed: %s", exc)
            transitivity = float("nan")
    else:
        transitivity = 0.0
    return {
        "nodes": n,
        "edges": m,
        "density": density,
        "components": len(components),
        "component_sizes": component_sizes[:10],
        "largest_component_size": component_sizes[0] if component_sizes else 0,
        "fragmentation": fragmentation,
        "avg_distance_largest_cc": avg_distance,
        "diameter_largest_cc": diameter,
        "radius_largest_cc": radius,
        "transitivity_mode2_projection": transitivity,
    }


def centrality_table(G: nx.Graph, nodes: list[str], prefix: str) -> pd.DataFrame:
    """Centrality for mode-2 nodes (non-operation side).

    Degree/closeness/betweenness via bipartite normalization.
    Eigenvector via generic algorithm (falls back to NaN if non-convergent).
    """
    if not nodes:
        return pd.DataFrame(columns=["slug", "degree", "betweenness", "closeness", "eigenvector"])
    # Bipartite centralities take the *opposite* set as the reference.
    opposite_nodes = [v for v in G.nodes() if v not in set(nodes)]
    deg = nx.bipartite.degree_centrality(G, opposite_nodes)
    clo = nx.bipartite.closeness_centrality(G, opposite_nodes)
    # Betweenness has no bipartite-specific normalization in networkx 3.x;
    # use generic betweenness which already handles bipartite correctly.
    btw = nx.betweenness_centrality(G, normalized=True)
    try:
        eig = nx.eigenvector_centrality(G, max_iter=1000, tol=1e-6)
    except nx.PowerIterationFailedConvergence as exc:
        log.warning("eigenvector non-convergent: %s", exc)
        eig = {v: float("nan") for v in G.nodes()}
    rows = []
    for v in nodes:
        if not v.startswith(f"{prefix}::"):
            continue
        rows.append(
            {
                "slug": v.split("::", 1)[1],
                "degree": deg.get(v, float("nan")),
                "betweenness": btw.get(v, float("nan")),
                "closeness": clo.get(v, float("nan")),
                "eigenvector": eig.get(v, float("nan")),
            }
        )
    df = pd.DataFrame(rows).sort_values("degree", ascending=False, ignore_index=True)
    return df


def community_on_projection(
    G: nx.Graph,
    project_onto: list[str],
    prefix: str,
) -> dict[str, Any]:
    if not project_onto:
        return {"communities": 0, "modularity": float("nan"), "communities_detail": []}
    proj = nx.bipartite.projected_graph(G, project_onto)
    if proj.number_of_edges() == 0:
        return {"communities": 0, "modularity": 0.0, "communities_detail": []}
    try:
        communities = nx.community.louvain_communities(proj, seed=42)
    except Exception as exc:
        log.warning("louvain failed: %s", exc)
        return {"communities": 0, "modularity": float("nan"), "communities_detail": []}
    mod = nx.community.modularity(proj, communities)
    detail = []
    for i, comm in enumerate(sorted(communities, key=len, reverse=True)):
        slugs = sorted(v.split("::", 1)[1] for v in comm)
        detail.append({"id": i, "size": len(slugs), "members": slugs[:30]})
    return {
        "communities": len(communities),
        "modularity": mod,
        "communities_detail": detail,
    }


# ---------------------------------------------------------------------------
# Git + environment helpers
# ---------------------------------------------------------------------------

def git_ref() -> dict[str, Any]:
    def run(*cmd: str) -> str:
        try:
            out = subprocess.check_output(
                ["git", *cmd], cwd=REPO_ROOT, stderr=subprocess.DEVNULL
            )
            return out.decode("utf-8").strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ""
    head = run("rev-parse", "--short", "HEAD")
    branch = run("rev-parse", "--abbrev-ref", "HEAD")
    dirty_out = run("status", "--porcelain")
    return {"head": head, "branch": branch, "dirty": bool(dirty_out)}


def tool_versions() -> dict[str, str]:
    return {
        "python": sys.version.split()[0],
        "networkx": nx.__version__,
        "pandas": pd.__version__,
        "pyyaml": yaml.__version__,
    }


# ---------------------------------------------------------------------------
# Aux metadata lookup for node CSVs
# ---------------------------------------------------------------------------

def node_attrs_from_wiki(
    kind: str,
    slug: str,
) -> dict[str, str]:
    """Best-effort attribute lookup from wiki/<kind>/<slug>.md. Empty dict if not found."""
    base_map = {
        "country": WIKI_COUNTRIES,
        "agency": WIKI_ORGS,
        "crime_type": WIKI_CRIMES,
    }
    base = base_map.get(kind)
    if base is None:
        return {}
    path = base / f"{slug}.md"
    if not path.exists():
        return {}
    fm = parse_frontmatter(path)
    if not fm:
        return {}
    if kind == "country":
        return {
            "iso_code": str(fm.get("iso_code") or ""),
            "region": str(fm.get("region") or ""),
            "ic_capacity_rating": str((fm.get("ic_capacity") or {}).get("rating") or ""),
        }
    if kind == "agency":
        return {
            "org_type": str(fm.get("org_type") or ""),
            "country": (extract_wikilinks(fm.get("country")) or [""])[0],
            "parent_org": (extract_wikilinks(fm.get("parent_org")) or [""])[0],
        }
    if kind == "crime_type":
        return {"crime_category": str(fm.get("crime_category") or "")}
    return {}


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def write_csv(path: Path, header: list[str], rows: list[list[Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, default=str, sort_keys=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--snapshot-date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        help="Snapshot date tag (default: UTC today).",
    )
    parser.add_argument(
        "--out-base",
        default=str(WORKSPACE_SNA / "out"),
        help="Output base directory.",
    )
    args = parser.parse_args()

    git_info = git_ref()
    snapshot_id = f"{args.snapshot_date}-{git_info['head'] or 'nogit'}"
    out_dir = Path(args.out_base) / snapshot_id
    out_dir.mkdir(parents=True, exist_ok=True)
    log.info("snapshot_id=%s out_dir=%s", snapshot_id, out_dir)

    # --- 1. Scan + parse operation frontmatter ---
    log.info("scanning wiki/operations/ ...")
    # Reset bare-string normalization stats for this run.
    _BARE_NORM_STATS["normalized"] = 0
    _BARE_NORM_STATS["empty_dropped"] = 0
    all_paths = sorted(WIKI_OPS.glob("*.md"))
    exclusion = ExclusionReport()
    records: list[OpRecord] = []
    for path in all_paths:
        if path.name == "_index.md":
            continue
        fm = parse_frontmatter(path)
        if fm is None:
            exclusion.parse_error.append(path.stem)
            continue
        if str(fm.get("type") or "").strip() != "operation":
            exclusion.not_operation_type.append(path.stem)
            continue
        records.append(build_record(path, fm))
    log.info("parsed %d operation records (of %d *.md files)", len(records), len(all_paths))

    # --- 2. Inclusion filter ---
    denylist = load_denylist()
    kept, excl2 = apply_inclusion(records, denylist)
    # merge parse/type exclusions (upstream) with inclusion-rule exclusions
    for attr in excl2.__dict__:
        getattr(exclusion, attr).extend(getattr(excl2, attr))
    log.info(
        "inclusion: kept=%d excluded=%d (denylist=%d)",
        len(kept),
        sum(len(v) for v in exclusion.__dict__.values()),
        len(exclusion.audit_denylist),
    )

    # --- 2b. Alias canonicalization (before graph build) ---
    alias_map = load_alias_map()
    alias_hits = count_alias_hits(kept, alias_map)
    fallback_used_count = sum(1 for r in kept if r.crime_type_fallback_used)
    log.info(
        "crime_type legacy-fallback reads: %d/%d included ops still use single `crime_type`",
        fallback_used_count,
        len(kept),
    )
    kept = [canonicalize_record(rec, alias_map) for rec in kept]
    total_alias_hits = sum(
        sum(m.values()) for m in alias_hits.values()
    )
    log.info(
        "alias canonicalization: %d mappings applied across %d record-slots",
        sum(len(v) for v in alias_map.values()),
        total_alias_hits,
    )

    # --- 3. Build 2-mode graphs ---
    G_country, ops_c, countries_c = build_bipartite(kept, "countries", "country")
    G_agency, ops_a, agencies_a = build_bipartite(kept, "agencies", "agency")
    # crime_types is canonical list-valued (PoC v4). Legacy single `crime_type`
    # is read as fallback in build_record when the list is empty — transparent here.
    G_crime, ops_t, crimes_t = build_bipartite(kept, "crime_types", "crimetype")

    # --- 4. Edge lists ---
    def edge_rows(G: nx.Graph, op_prefix: str, other_prefix: str) -> list[list[str]]:
        rows: list[list[str]] = []
        for u, v in G.edges():
            if u.startswith(f"{op_prefix}::") and v.startswith(f"{other_prefix}::"):
                rows.append([u.split("::", 1)[1], v.split("::", 1)[1]])
            elif v.startswith(f"{op_prefix}::") and u.startswith(f"{other_prefix}::"):
                rows.append([v.split("::", 1)[1], u.split("::", 1)[1]])
        rows.sort()
        return rows
    write_csv(out_dir / "edges_op_country.csv", ["op_slug", "country_slug"],
              edge_rows(G_country, "op", "country"))
    write_csv(out_dir / "edges_op_agency.csv", ["op_slug", "agency_slug"],
              edge_rows(G_agency, "op", "agency"))
    write_csv(out_dir / "edges_op_crimetype.csv", ["op_slug", "crime_type_slug"],
              edge_rows(G_crime, "op", "crimetype"))

    # --- 5. Node metadata CSVs ---
    op_rows: list[list[Any]] = []
    for rec in sorted(kept, key=lambda r: r.slug):
        op_rows.append([
            rec.slug, rec.title or "", rec.period or "", rec.outcome or "",
            rec.lead_agency or "", rec.coordinating_body or "",
            rec.timeframe_announced or "", rec.source_count or "",
            rec.status or "",
        ])
    write_csv(
        out_dir / "nodes_operations.csv",
        ["slug", "title", "period", "outcome", "lead_agency", "coordinating_body",
         "timeframe_announced", "source_count", "status"],
        op_rows,
    )

    def node_rows(nodes: list[str], prefix: str, kind: str, extra_cols: list[str]) -> list[list[Any]]:
        rows: list[list[Any]] = []
        for n in nodes:
            slug = n.split("::", 1)[1]
            attrs = node_attrs_from_wiki(kind, slug)
            rows.append([slug] + [attrs.get(c, "") for c in extra_cols])
        rows.sort()
        return rows
    write_csv(
        out_dir / "nodes_countries.csv",
        ["slug", "iso_code", "region", "ic_capacity_rating"],
        node_rows(countries_c, "country", "country", ["iso_code", "region", "ic_capacity_rating"]),
    )
    write_csv(
        out_dir / "nodes_agencies.csv",
        ["slug", "org_type", "country", "parent_org"],
        node_rows(agencies_a, "agency", "agency", ["org_type", "country", "parent_org"]),
    )
    write_csv(
        out_dir / "nodes_crimetypes.csv",
        ["slug", "crime_category"],
        node_rows(crimes_t, "crimetype", "crime_type", ["crime_category"]),
    )

    # --- 6. Cohesion metrics ---
    cohesion = {
        "country": cohesion_metrics(G_country, ops_c),
        "agency": cohesion_metrics(G_agency, ops_a),
        "crime_type": cohesion_metrics(G_crime, ops_t),
    }
    write_json(out_dir / "metrics_cohesion.json", cohesion)

    # --- 7. Centrality (mode-2 side) ---
    df_c = centrality_table(G_country, countries_c, "country")
    df_a = centrality_table(G_agency, agencies_a, "agency")
    df_t = centrality_table(G_crime, crimes_t, "crimetype")
    df_c.to_csv(out_dir / "metrics_centrality_country.csv", index=False)
    df_a.to_csv(out_dir / "metrics_centrality_agency.csv", index=False)
    df_t.to_csv(out_dir / "metrics_centrality_crimetype.csv", index=False)

    # --- 8. Components + community ---
    def comp_sizes(G: nx.Graph) -> list[int]:
        return sorted((len(c) for c in nx.connected_components(G)), reverse=True)
    components_payload = {
        "country": {"count": nx.number_connected_components(G_country),
                    "sizes": comp_sizes(G_country)[:10]},
        "agency": {"count": nx.number_connected_components(G_agency),
                   "sizes": comp_sizes(G_agency)[:10]},
        "crime_type": {"count": nx.number_connected_components(G_crime),
                       "sizes": comp_sizes(G_crime)[:10]},
    }
    write_json(out_dir / "metrics_components.json", components_payload)

    community_payload = {
        "country": community_on_projection(G_country, countries_c, "country"),
        "agency": community_on_projection(G_agency, agencies_a, "agency"),
        "crime_type": community_on_projection(G_crime, crimes_t, "crimetype"),
    }
    write_json(out_dir / "metrics_community.json", community_payload)

    # --- 9. Included / excluded lists ---
    included_path = out_dir / "included_operations.txt"
    included_path.write_text(
        "\n".join(sorted(r.slug for r in kept)) + "\n", encoding="utf-8"
    )
    write_csv(
        out_dir / "excluded_operations.csv",
        ["slug", "reason"],
        [list(r) for r in exclusion.rows_for_csv()],
    )

    # --- 10. Manifest ---
    manifest = {
        "snapshot_date": args.snapshot_date,
        "snapshot_id": snapshot_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git_ref": git_info,
        "rules_version": RULES_VERSION,
        "wiki_totals": {
            "operations_files_scanned": len(all_paths),
            "countries_referenced": len(countries_c),
            "agencies_referenced": len(agencies_a),
            "crime_types_referenced": len(crimes_t),
        },
        "inclusion": {
            "included_operations_count": len(kept),
            "excluded_operations_count": sum(len(v) for v in exclusion.__dict__.values()),
            "exclusion_reason_breakdown": exclusion.as_counts(),
        },
        "edges": {
            "op_country": G_country.number_of_edges(),
            "op_agency": G_agency.number_of_edges(),
            "op_crimetype": G_crime.number_of_edges(),
        },
        "nodes": {
            "operations_kept": len(kept),
            "countries": len(countries_c),
            "agencies": len(agencies_a),
            "crime_types": len(crimes_t),
        },
        "tool_versions": tool_versions(),
        "spec_files": {
            "paper": str(SPEC_PAPER.relative_to(REPO_ROOT)),
            "rules": str(SPEC_RULES.relative_to(REPO_ROOT)),
            "denylist": str(AUDIT_DENYLIST.relative_to(REPO_ROOT)),
            "alias_map": str(ALIAS_MAP_FILE.relative_to(REPO_ROOT)),
        },
        "alias_canonicalization": {
            "mappings": alias_map,
            "hits": alias_hits,
            "total_slot_merges": total_alias_hits,
        },
        "bare_string_normalization": {
            "normalized": _BARE_NORM_STATS["normalized"],
            "empty_dropped": _BARE_NORM_STATS["empty_dropped"],
            "scan_report": "_workspace/sna/bare-strings-scan.csv",
        },
        "crime_type_schema_migration": {
            "canonical_field": "crime_types (list)",
            "legacy_field": "crime_type (single) — read as fallback during PoC v4",
            "included_ops_using_fallback": fallback_used_count,
            "note": "canonical `crime_types` list is authoritative; legacy single field is still read if list is empty/absent.",
        },
    }
    write_json(out_dir / "manifest.json", manifest)

    # --- 11. Summary to stderr for the user ---
    log.info("DONE snapshot=%s", snapshot_id)
    log.info("  included_operations_count: %d", manifest["inclusion"]["included_operations_count"])
    log.info("  excluded_operations_count: %d", manifest["inclusion"]["excluded_operations_count"])
    log.info("  exclusion breakdown: %s", manifest["inclusion"]["exclusion_reason_breakdown"])
    log.info("  nodes: countries=%d agencies=%d crime_types=%d",
             len(countries_c), len(agencies_a), len(crimes_t))
    log.info("  edges: op-country=%d op-agency=%d op-crimetype=%d",
             G_country.number_of_edges(), G_agency.number_of_edges(), G_crime.number_of_edges())
    log.info("  out_dir: %s", out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
