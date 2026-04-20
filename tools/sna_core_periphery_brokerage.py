#!/usr/bin/env python3
"""
Step C supplementary metrics — core-periphery (Borgatti-Everett via cpnet)
and Gould-Fernandez 5-role brokerage on the PoC v5 2-mode networks.

Inputs:
  _workspace/sna/out/<snapshot>/edges_op_{country,agency,crimetype}.csv
  wiki/{organizations,countries,crime-types}/*.md  (for node partitions)

Outputs:
  _workspace/sna/out/<snapshot>/metrics_core_periphery.json
  _workspace/sna/out/<snapshot>/metrics_brokerage_{agency,country,crimetype}.csv
  _workspace/sna/out/<snapshot>/metrics_supplementary.json  (manifest)

Rules:
  - Core-periphery: run cpnet.BE on the 1-mode projection of mode-2 nodes.
    Op (mode-1) core/periphery derived heuristically: op is core if ≥1 of
    its neighbors is in the mode-2 core, else periphery. Report fitness
    (cpnet score) + 4-block density on the 2-mode graph.
  - Brokerage: Gould-Fernandez 5-role counts on the 1-mode projection of
    mode-2 nodes, using wiki-page metadata for node partitions:
      * agency.org_type
      * country.region
      * crime-type.crime_category
    Nodes without metadata are grouped as `unknown`.
  - Projection self-loops removed before all analyses.
  - Findings expected to be directional (ordering of nodes), not strict
    numeric reproduction of the paper (corpus differs).
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import cpnet
import networkx as nx
import pandas as pd
import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("supp")

REPO = Path(__file__).resolve().parents[1]
WIKI_ORGS = REPO / "wiki" / "organizations"
WIKI_COUNTRIES = REPO / "wiki" / "countries"
WIKI_CRIMES = REPO / "wiki" / "crime-types"
WORKSPACE_OUT = REPO / "_workspace" / "sna" / "out"

ROLES = ("coordinator", "gatekeeper", "representative", "consultant", "liaison")


# ---------------------------------------------------------------------------
# Partition loaders
# ---------------------------------------------------------------------------

def _read_fm(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return {}
        parts = text.split("---", 2)
        if len(parts) < 3:
            return {}
        data = yaml.safe_load(parts[1])
        return data if isinstance(data, dict) else {}
    except (yaml.YAMLError, OSError):
        return {}


def agency_partitions() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in WIKI_ORGS.glob("*.md"):
        if p.stem == "_index":
            continue
        fm = _read_fm(p)
        val = str(fm.get("org_type") or "").strip() or "unknown"
        out[p.stem] = val
    return out


def country_partitions() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in WIKI_COUNTRIES.glob("*.md"):
        if p.stem == "_index":
            continue
        fm = _read_fm(p)
        val = str(fm.get("region") or "").strip() or "unknown"
        out[p.stem] = val
    return out


def crimetype_partitions() -> dict[str, str]:
    out: dict[str, str] = {}
    for p in WIKI_CRIMES.glob("*.md"):
        if p.stem == "_index":
            continue
        fm = _read_fm(p)
        val = str(fm.get("crime_category") or "").strip() or "unknown"
        out[p.stem] = val
    return out


# ---------------------------------------------------------------------------
# Graph construction from edge CSV
# ---------------------------------------------------------------------------

def load_bipartite(
    edge_csv: Path, left_col: str, right_col: str
) -> tuple[nx.Graph, list[str], list[str]]:
    """Return bipartite G, ops_nodes_list, mode2_nodes_list."""
    G = nx.Graph()
    ops = set()
    mode2 = set()
    with edge_csv.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            o = f"op::{row[left_col]}"
            m = f"m2::{row[right_col]}"
            G.add_node(o, bipartite=0)
            G.add_node(m, bipartite=1)
            G.add_edge(o, m)
            ops.add(o)
            mode2.add(m)
    return G, sorted(ops), sorted(mode2)


def project_mode2(G: nx.Graph, mode2_nodes: list[str]) -> nx.Graph:
    """1-mode projection onto mode-2 side. Removes self-loops."""
    P = nx.bipartite.projected_graph(G, mode2_nodes)
    P.remove_edges_from(nx.selfloop_edges(P))
    return P


# ---------------------------------------------------------------------------
# Core-periphery (Borgatti-Everett via cpnet)
# ---------------------------------------------------------------------------

def core_periphery(
    G_bi: nx.Graph, mode2_nodes: list[str], ops_nodes: list[str]
) -> dict:
    """Return fitness + coreness partition + 4-block density matrix."""
    P = project_mode2(G_bi, mode2_nodes)
    if P.number_of_edges() == 0:
        return {
            "note": "mode-2 projection has zero edges; core-periphery undefined",
            "fitness": None,
            "mode2_core_count": 0,
            "mode2_periphery_count": len(mode2_nodes),
            "blocks": None,
        }
    # cpnet.BE operates on a connected component ideally; subset to largest CC.
    cc = max(nx.connected_components(P), key=len)
    P_cc = P.subgraph(cc).copy()
    alg = cpnet.BE()
    alg.detect(P_cc)
    coreness = alg.get_coreness()   # {node: 0 or 1}
    pair_id = alg.get_pair_id()
    try:
        scores = alg.score(P_cc, pair_id, coreness)
        fitness = float(scores[0]) if scores else None
    except Exception as exc:
        log.warning("fitness score failed: %s", exc)
        fitness = None

    # cpnet convention: coreness==1 for core, 0 for periphery.
    mode2_core = {n for n in P_cc.nodes() if coreness.get(n, 0) == 1}
    mode2_peri = {n for n in mode2_nodes if n not in mode2_core}

    # Ops core heuristic: op is core if at least 1 neighbor is in mode2_core.
    ops_core: set[str] = set()
    for op in ops_nodes:
        neigh = set(G_bi.neighbors(op))
        if neigh & mode2_core:
            ops_core.add(op)
    ops_peri = set(ops_nodes) - ops_core

    # 4-block density (2-mode) — edges(A, B) / (|A| * |B|)
    def block_density(a: set[str], b: set[str]) -> float:
        if not a or not b:
            return 0.0
        cnt = 0
        for u in a:
            for v in G_bi.neighbors(u):
                if v in b:
                    cnt += 1
        return cnt / (len(a) * len(b))

    blocks = {
        "core_core": block_density(ops_core, mode2_core),
        "core_periphery": block_density(ops_core, mode2_peri),
        "periphery_core": block_density(ops_peri, mode2_core),
        "periphery_periphery": block_density(ops_peri, mode2_peri),
    }
    return {
        "fitness": fitness,
        "mode2_core_count": len(mode2_core),
        "mode2_periphery_count": len(mode2_peri),
        "ops_core_count": len(ops_core),
        "ops_periphery_count": len(ops_peri),
        "mode2_core_members": sorted(n.split("::", 1)[1] for n in mode2_core),
        "blocks": blocks,
    }


# ---------------------------------------------------------------------------
# Gould-Fernandez 5-role brokerage (on 1-mode projection of mode-2)
# ---------------------------------------------------------------------------

def brokerage_counts(
    P: nx.Graph, partition: dict[str, str]
) -> dict[str, dict[str, int]]:
    """Compute G-F brokerage per node. Each ordered triad (i, k, j) where
    i != k != j, (i, j) not directly connected, and k is a common neighbor
    of i and j, contributes one count to the role implied by the group
    triple (g(i), g(k), g(j))."""
    counts: dict[str, dict[str, int]] = {
        n: {r: 0 for r in ROLES} for n in P.nodes()
    }
    nodes = list(P.nodes())
    for k in nodes:
        g_k = partition.get(k, "unknown")
        neigh = list(P.neighbors(k))
        n_neigh = len(neigh)
        if n_neigh < 2:
            continue
        for ii in range(n_neigh):
            i = neigh[ii]
            g_i = partition.get(i, "unknown")
            for jj in range(n_neigh):
                if ii == jj:
                    continue
                j = neigh[jj]
                if P.has_edge(i, j):
                    continue
                g_j = partition.get(j, "unknown")
                same_ij = g_i == g_j
                same_ik = g_i == g_k
                same_kj = g_k == g_j
                if same_ik and same_kj:           # all same
                    counts[k]["coordinator"] += 1
                elif same_ik and not same_kj:     # i=k, j out
                    counts[k]["representative"] += 1
                elif not same_ik and same_kj:     # k=j, i out
                    counts[k]["gatekeeper"] += 1
                elif same_ij and not same_ik:     # i=j, k out
                    counts[k]["consultant"] += 1
                else:                             # all different
                    counts[k]["liaison"] += 1
    return counts


def brokerage_table(
    P: nx.Graph, partition: dict[str, str]
) -> pd.DataFrame:
    counts = brokerage_counts(P, partition)
    rows = []
    for node, roles in counts.items():
        slug = node.split("::", 1)[1]
        total = sum(roles.values())
        rows.append({
            "slug": slug,
            "partition_value": partition.get(node, "unknown"),
            **roles,
            "total": total,
        })
    df = pd.DataFrame(rows).sort_values("total", ascending=False, ignore_index=True)
    return df


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--snapshot", help="Snapshot ID under _workspace/sna/out/.")
    args = parser.parse_args()

    snap_dir = None
    if args.snapshot:
        snap_dir = WORKSPACE_OUT / args.snapshot
    else:
        candidates = sorted(WORKSPACE_OUT.glob("*-*/manifest.json"))
        if candidates:
            snap_dir = candidates[-1].parent
    if snap_dir is None or not snap_dir.exists():
        log.error("Snapshot dir not found. Pass --snapshot <id>.")
        return 2
    log.info("snapshot: %s", snap_dir.name)

    # Load bipartite graphs from edge CSVs
    G_country, ops_c, m2_c = load_bipartite(
        snap_dir / "edges_op_country.csv", "op_slug", "country_slug"
    )
    # Convert country node prefix
    nx.relabel_nodes(
        G_country,
        {n: f"m2::{n.split('::', 1)[1]}" for n in G_country.nodes() if n.startswith("m2::")},
        copy=False,
    )
    G_agency, ops_a, m2_a = load_bipartite(
        snap_dir / "edges_op_agency.csv", "op_slug", "agency_slug"
    )
    G_crime, ops_t, m2_t = load_bipartite(
        snap_dir / "edges_op_crimetype.csv", "op_slug", "crime_type_slug"
    )

    log.info("graphs: country %de, agency %de, crime %de",
             G_country.number_of_edges(),
             G_agency.number_of_edges(),
             G_crime.number_of_edges())

    # Core-periphery
    log.info("running core-periphery (cpnet BE on projections)")
    cp_country = core_periphery(G_country, m2_c, ops_c)
    cp_agency = core_periphery(G_agency, m2_a, ops_a)
    cp_crime = core_periphery(G_crime, m2_t, ops_t)

    cp_payload = {
        "country": cp_country,
        "agency": cp_agency,
        "crime_type": cp_crime,
        "method": {
            "algorithm": "Borgatti-Everett (cpnet.BE)",
            "applied_to": "1-mode projection onto mode-2 side (largest connected component)",
            "ops_core_rule": "op is core iff ≥1 of its neighbors is in the mode-2 core",
            "block_densities": "computed on the full 2-mode bipartite graph",
        },
    }
    cp_path = snap_dir / "metrics_core_periphery.json"
    with cp_path.open("w", encoding="utf-8") as fh:
        json.dump(cp_payload, fh, ensure_ascii=False, indent=2, sort_keys=True)

    # Brokerage
    log.info("loading partitions and running Gould-Fernandez brokerage")
    agency_part = {f"m2::{k}": v for k, v in agency_partitions().items()}
    country_part = {f"m2::{k}": v for k, v in country_partitions().items()}
    crime_part = {f"m2::{k}": v for k, v in crimetype_partitions().items()}

    P_country = project_mode2(G_country, m2_c)
    P_agency = project_mode2(G_agency, m2_a)
    P_crime = project_mode2(G_crime, m2_t)

    df_country = brokerage_table(P_country, country_part)
    df_agency = brokerage_table(P_agency, agency_part)
    df_crime = brokerage_table(P_crime, crime_part)

    df_country.to_csv(snap_dir / "metrics_brokerage_country.csv", index=False)
    df_agency.to_csv(snap_dir / "metrics_brokerage_agency.csv", index=False)
    df_crime.to_csv(snap_dir / "metrics_brokerage_crimetype.csv", index=False)

    # Partition distribution (how many nodes per group)
    def part_dist(nodes, partmap):
        counts = defaultdict(int)
        for n in nodes:
            counts[partmap.get(n, "unknown")] += 1
        return dict(counts)

    supp_payload = {
        "snapshot": snap_dir.name,
        "rules_version": "step-c-v1",
        "core_periphery_method": cp_payload["method"],
        "brokerage_method": {
            "algorithm": "Gould-Fernandez 5 roles",
            "applied_to": "1-mode projection onto mode-2 side",
            "node_partitions": {
                "agency": "org_type",
                "country": "region",
                "crime_type": "crime_category",
            },
            "missing_metadata_handling": "grouped as 'unknown'",
        },
        "partition_distributions": {
            "agency": part_dist(m2_a, agency_part),
            "country": part_dist(m2_c, country_part),
            "crime_type": part_dist(m2_t, crime_part),
        },
    }
    with (snap_dir / "metrics_supplementary.json").open("w", encoding="utf-8") as fh:
        json.dump(supp_payload, fh, ensure_ascii=False, indent=2, sort_keys=True)

    # Console summary
    print(f"\n=== Core-periphery ===")
    for label, cp in (("country", cp_country), ("agency", cp_agency), ("crime_type", cp_crime)):
        fit = cp.get("fitness")
        cc = cp["blocks"]["core_core"] if cp.get("blocks") else None
        cp_ = cp["blocks"]["core_periphery"] if cp.get("blocks") else None
        pc = cp["blocks"]["periphery_core"] if cp.get("blocks") else None
        pp = cp["blocks"]["periphery_periphery"] if cp.get("blocks") else None
        fit_s = f"{fit:.3f}" if fit is not None else "n/a"
        print(f"  {label:11s}  fitness={fit_s}  core_mode2={cp['mode2_core_count']:3d}  "
              f"C-C={cc:.3f}  C-P={cp_:.3f}  P-C={pc:.3f}  P-P={pp:.3f}"
              if cc is not None else
              f"  {label:11s}  fitness={fit_s}  (blocks undefined — projection empty)")
        if cp.get("mode2_core_members"):
            preview = cp["mode2_core_members"][:8]
            print(f"    mode2 core preview: {preview}")

    print(f"\n=== Brokerage top 10 by total ===")
    for label, df in (("country", df_country), ("agency", df_agency), ("crime_type", df_crime)):
        print(f"  {label}:")
        for _, row in df.head(10).iterrows():
            print(f"    {row['slug']:45s} [{row['partition_value']:15s}]  "
                  f"coord={row['coordinator']:4d}  gate={row['gatekeeper']:4d}  "
                  f"rep={row['representative']:4d}  cons={row['consultant']:4d}  "
                  f"liais={row['liaison']:4d}  total={row['total']:5d}")

    print(f"\nWritten: {cp_path.relative_to(REPO)}")
    print(f"Written: metrics_brokerage_{{country,agency,crimetype}}.csv under {snap_dir.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
