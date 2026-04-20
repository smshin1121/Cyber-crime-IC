#!/usr/bin/env python3
"""
Step C-2: role-indicator-based visualization of the PoC v5 2-mode networks.

Reads:
  _workspace/sna/out/<snap>/edges_op_{country,agency,crimetype}.csv
  _workspace/sna/out/<snap>/metrics_centrality_{country,agency,crimetype}.csv
  _workspace/sna/out/<snap>/metrics_brokerage_{country,agency,crimetype}.csv
  _workspace/sna/out/<snap>/metrics_core_periphery.json

Writes:
  wiki/analysis/sna/agency-network.html   — pyvis interactive figure
  wiki/analysis/sna/country-network.html  — pyvis interactive figure
  cosmos/sna-roles.json                   — role classification per mode-2 node
                                            (consumed later by Cosmos UI; does
                                            NOT modify existing Cosmos views)
  _workspace/sna/out/<snap>/role_classification.csv
                                          — full classification manifest
                                            with inputs and rule version

Role classification rules (v1 — documented + reviewable):

  Agency:
    hub                 degree ≥ 0.30 AND coord ≥ 100 AND (gate+rep) ≥ 500
    liaison-broker      liais / max(1, total) > 0.65 AND coord / max(1, total) < 0.10 AND total ≥ 200
    internal-coordinator coord / max(1, total) > 0.30 AND coord ≥ 80
    regional-coordinator (gate + rep) / max(1, total) > 0.40 AND gate ≥ 80
    participant          (otherwise)

  Country:
    global-liaison       liais / max(1, total) > 0.90 AND degree > 0.30
    regional-coordinator (gate + rep) / max(1, total) > 0.20 AND degree > 0.15
    specialist-broker    degree < 0.20 AND betweenness / max(0.001, degree) > 0.50
    participant          (otherwise)

  Core/periphery flag is read from metrics_core_periphery.json per network.

Color scheme (pyvis + Cosmos — consistent):
  hub                  = '#FFC300'   # amber (balanced hub)
  liaison-broker       = '#C70039'   # red (cross-domain broker)
  internal-coordinator = '#1F77B4'   # blue
  regional-coordinator = '#2CA02C'   # green
  specialist-broker    = '#9467BD'   # purple (low-deg / high-btw)
  global-liaison       = '#FFD700'   # gold (bright — US-like)
  participant          = '#B0B0B0'   # gray

Operations (mode-1) are uniformly rendered as small circles in neutral tone.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import sys
from pathlib import Path

import networkx as nx
import pandas as pd
from pyvis.network import Network

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("viz")

REPO = Path(__file__).resolve().parents[1]
SNA_OUT = REPO / "_workspace" / "sna" / "out"
WIKI_ANALYSIS = REPO / "wiki" / "analysis"
FIG_DIR = WIKI_ANALYSIS / "sna"
COSMOS_DIR = REPO / "cosmos"

RULES_VERSION = "roles-v1"

ROLE_COLORS = {
    "hub": "#FFC300",
    "liaison-broker": "#C70039",
    "internal-coordinator": "#1F77B4",
    "regional-coordinator": "#2CA02C",
    "specialist-broker": "#9467BD",
    "global-liaison": "#FFD700",
    "participant": "#B0B0B0",
    "operation": "#2F4F4F",  # dark slate for ops (mode-1)
}


def classify_agency(row) -> str:
    deg = float(row["degree"])
    total = int(row["total"]) or 1
    coord = int(row["coordinator"])
    gate = int(row["gatekeeper"])
    rep = int(row["representative"])
    liais = int(row["liaison"])
    gate_rep = gate + rep
    if deg >= 0.30 and coord >= 100 and gate_rep >= 500:
        return "hub"
    if liais / total > 0.65 and coord / total < 0.10 and total >= 200:
        return "liaison-broker"
    if coord / total > 0.30 and coord >= 80:
        return "internal-coordinator"
    if gate_rep / total > 0.40 and gate >= 80:
        return "regional-coordinator"
    return "participant"


def classify_country(row) -> str:
    deg = float(row["degree"])
    btw = float(row["betweenness"])
    total = int(row["total"]) or 1
    gate = int(row["gatekeeper"])
    rep = int(row["representative"])
    liais = int(row["liaison"])
    if liais / total > 0.90 and deg > 0.30:
        return "global-liaison"
    if (gate + rep) / total > 0.20 and deg > 0.15:
        return "regional-coordinator"
    if deg < 0.20 and btw / max(0.001, deg) > 0.50:
        return "specialist-broker"
    return "participant"


def load_snapshot(snap_dir: Path) -> dict:
    def read_csv(name: str) -> pd.DataFrame:
        return pd.read_csv(snap_dir / name)
    out = {
        "edges": {
            "country": read_csv("edges_op_country.csv"),
            "agency": read_csv("edges_op_agency.csv"),
            "crime_type": read_csv("edges_op_crimetype.csv"),
        },
        "centrality": {
            "country": read_csv("metrics_centrality_country.csv"),
            "agency": read_csv("metrics_centrality_agency.csv"),
            "crime_type": read_csv("metrics_centrality_crimetype.csv"),
        },
        "brokerage": {
            "country": read_csv("metrics_brokerage_country.csv"),
            "agency": read_csv("metrics_brokerage_agency.csv"),
            "crime_type": read_csv("metrics_brokerage_crimetype.csv"),
        },
    }
    with (snap_dir / "metrics_core_periphery.json").open(encoding="utf-8") as fh:
        out["core_periphery"] = json.load(fh)
    return out


def merge_role_indicators(
    centrality: pd.DataFrame, brokerage: pd.DataFrame, core_members: set[str], kind: str
) -> pd.DataFrame:
    df = centrality.merge(brokerage, on="slug", how="outer", suffixes=("", "_brk"))
    # Fill numeric NaN with 0
    for col in ("coordinator", "gatekeeper", "representative", "consultant", "liaison", "total"):
        if col not in df.columns:
            df[col] = 0
        df[col] = df[col].fillna(0).astype(int)
    for col in ("degree", "betweenness", "closeness", "eigenvector"):
        if col not in df.columns:
            df[col] = 0.0
        df[col] = df[col].fillna(0.0)
    if "partition_value" not in df.columns:
        df["partition_value"] = "unknown"
    df["partition_value"] = df["partition_value"].fillna("unknown")
    df["core_periphery"] = df["slug"].apply(
        lambda s: "core" if s in core_members else "periphery"
    )
    if kind == "agency":
        df["role"] = df.apply(classify_agency, axis=1)
    elif kind == "country":
        df["role"] = df.apply(classify_country, axis=1)
    else:
        df["role"] = "participant"
    df["kind"] = kind
    return df


def build_network_html(
    edges: pd.DataFrame,
    role_df: pd.DataFrame,
    kind: str,
    title: str,
    out_path: Path,
) -> None:
    """Render a pyvis HTML visualization. Operations (mode-1) + mode-2 nodes."""
    role_by_slug = {r["slug"]: r for r in role_df.to_dict("records")}
    G = nx.Graph()

    # mode-2 nodes (with role-based styling)
    for slug, row in role_by_slug.items():
        role = row["role"]
        color = ROLE_COLORS.get(role, "#B0B0B0")
        deg = float(row.get("degree", 0.0))
        btw = float(row.get("betweenness", 0.0))
        total = int(row.get("total", 0))
        partition = row.get("partition_value", "unknown")
        core_flag = row.get("core_periphery", "periphery")
        # Size scale: degree-based (10 — 60 px)
        size = 10 + min(50, deg * 80)
        border_width = 3 if core_flag == "core" else 1
        tooltip = (
            f"<b>{slug}</b><br>"
            f"kind: {kind}<br>"
            f"role: {role}<br>"
            f"partition: {partition}<br>"
            f"core: {core_flag}<br>"
            f"degree: {deg:.3f}<br>"
            f"betweenness: {btw:.3f}<br>"
            f"brokerage total: {total}"
        )
        G.add_node(
            slug,
            label=slug,
            color=color,
            size=size,
            title=tooltip,
            borderWidth=border_width,
            group=role,
        )

    # mode-1 (operations) nodes
    left_col = edges.columns[0]
    right_col = edges.columns[1]
    op_slugs = sorted(edges[left_col].unique())
    for op in op_slugs:
        G.add_node(
            op,
            label="",
            color=ROLE_COLORS["operation"],
            size=6,
            title=f"<b>{op}</b><br>(operation node)",
            borderWidth=1,
            group="operation",
        )

    # edges
    for _, row in edges.iterrows():
        G.add_edge(row[left_col], row[right_col])

    net = Network(
        height="720px",
        width="100%",
        bgcolor="#ffffff",
        font_color="#1a1a1a",
        notebook=False,
        directed=False,
        cdn_resources="in_line",
    )
    net.from_nx(G)
    net.toggle_physics(True)
    net.set_options("""
    {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -80,
          "centralGravity": 0.01,
          "springLength": 130,
          "springConstant": 0.03,
          "damping": 0.9
        },
        "minVelocity": 0.75,
        "solver": "forceAtlas2Based",
        "stabilization": { "iterations": 180 }
      },
      "interaction": {
        "hover": true,
        "navigationButtons": true,
        "keyboard": true,
        "tooltipDelay": 120
      }
    }
    """)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Use generate_html() + explicit utf-8 write to avoid cp949 crash on Windows.
    html = net.generate_html(notebook=False)
    legend_html = _build_legend_html(kind, title)
    html = html.replace("</body>", legend_html + "\n</body>")
    out_path.write_text(html, encoding="utf-8")
    log.info("wrote %s (%d mode-2 nodes + %d op nodes)",
             out_path.relative_to(REPO), len(role_by_slug), len(op_slugs))


def _build_legend_html(kind: str, title: str) -> str:
    if kind == "agency":
        roles_shown = ["hub", "liaison-broker", "internal-coordinator",
                       "regional-coordinator", "participant", "operation"]
    elif kind == "country":
        roles_shown = ["global-liaison", "regional-coordinator", "specialist-broker",
                       "participant", "operation"]
    else:
        roles_shown = ["participant", "operation"]
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:8px;margin:3px 0">'
        f'<span style="display:inline-block;width:16px;height:16px;border-radius:50%;'
        f'background:{ROLE_COLORS[r]};border:1px solid #333"></span>'
        f'<span style="font-size:12px;color:#222">{r}</span></div>'
        for r in roles_shown
    )
    return (
        '<div style="position:fixed;top:12px;right:12px;background:rgba(255,255,255,0.96);'
        'padding:10px 12px;border:1px solid #bbb;border-radius:6px;font-family:Arial;'
        'box-shadow:0 1px 3px rgba(0,0,0,0.1);z-index:1000">'
        f'<div style="font-weight:bold;font-size:13px;margin-bottom:6px">{title}</div>'
        f'{rows}'
        '<div style="margin-top:8px;font-size:11px;color:#555">'
        'Core-block nodes have a thicker border. Hover a node for centrality + brokerage detail.'
        '</div>'
        '</div>'
    )


def export_cosmos_roles(
    role_dfs: dict[str, pd.DataFrame],
    edges_by_kind: dict[str, pd.DataFrame],
    out_path: Path,
    snapshot: str,
) -> None:
    """Write a consolidated sna-roles.json consumed by Cosmos SNA mode.
    Structure is per-kind (agency / country / crime_type) so the client can
    switch between 2-mode networks without re-fetching. Does not modify the
    existing Cosmos view — Cosmos reads this file only when SNA mode is
    selected."""
    def _node_record(r: dict) -> dict:
        return {
            "slug": r["slug"],
            "role": r["role"],
            "partition": r.get("partition_value", "unknown"),
            "core_periphery": r.get("core_periphery", "periphery"),
            "degree": float(r.get("degree", 0.0)),
            "betweenness": float(r.get("betweenness", 0.0)),
            "brokerage": {
                "coordinator": int(r.get("coordinator", 0)),
                "gatekeeper": int(r.get("gatekeeper", 0)),
                "representative": int(r.get("representative", 0)),
                "consultant": int(r.get("consultant", 0)),
                "liaison": int(r.get("liaison", 0)),
                "total": int(r.get("total", 0)),
            },
        }

    payload: dict = {
        "snapshot": snapshot,
        "rules_version": RULES_VERSION,
        "role_colors": ROLE_COLORS,
    }
    # Edge CSV columns: (op_slug, <kind>_slug)
    edge_col_right = {
        "agency": "agency_slug",
        "country": "country_slug",
        "crime_type": "crime_type_slug",
    }
    for kind, df in role_dfs.items():
        edges_df = edges_by_kind.get(kind)
        op_set: set[str] = set()
        edges_list: list[list[str]] = []
        if edges_df is not None and not edges_df.empty:
            right_col = edge_col_right[kind]
            for _, row in edges_df.iterrows():
                op = str(row["op_slug"])
                m2 = str(row[right_col])
                op_set.add(op)
                edges_list.append([op, m2])
        nodes = [_node_record(r) for r in df.to_dict("records")]
        payload[kind] = {
            "nodes": nodes,
            "operations": sorted(op_set),
            "edges": sorted(edges_list),
        }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=True)
    log.info(
        "wrote %s (agency %dn/%de, country %dn/%de, crime %dn/%de)",
        out_path.relative_to(REPO),
        len(payload["agency"]["nodes"]), len(payload["agency"]["edges"]),
        len(payload["country"]["nodes"]), len(payload["country"]["edges"]),
        len(payload["crime_type"]["nodes"]), len(payload["crime_type"]["edges"]),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--snapshot", help="Snapshot id under _workspace/sna/out/.")
    args = parser.parse_args()

    snap_dir = None
    if args.snapshot:
        snap_dir = SNA_OUT / args.snapshot
    else:
        candidates = sorted(SNA_OUT.glob("*-*/manifest.json"))
        if candidates:
            snap_dir = candidates[-1].parent
    if snap_dir is None or not snap_dir.exists():
        log.error("Snapshot directory not found. Use --snapshot.")
        return 2
    log.info("snapshot: %s", snap_dir.name)

    data = load_snapshot(snap_dir)
    cp = data["core_periphery"]
    agency_core = set(cp["agency"].get("mode2_core_members") or [])
    country_core = set(cp["country"].get("mode2_core_members") or [])
    crime_core = set(cp["crime_type"].get("mode2_core_members") or [])

    role_agency = merge_role_indicators(
        data["centrality"]["agency"], data["brokerage"]["agency"], agency_core, "agency"
    )
    role_country = merge_role_indicators(
        data["centrality"]["country"], data["brokerage"]["country"], country_core, "country"
    )
    role_crime = merge_role_indicators(
        data["centrality"]["crime_type"], data["brokerage"]["crime_type"], crime_core, "crime_type"
    )

    # Write classification manifest
    manifest_rows: list[dict] = []
    for df in (role_agency, role_country, role_crime):
        for rec in df.to_dict("records"):
            manifest_rows.append({
                "kind": rec["kind"],
                "slug": rec["slug"],
                "role": rec["role"],
                "core_periphery": rec["core_periphery"],
                "partition_value": rec.get("partition_value", "unknown"),
                "degree": rec.get("degree", 0.0),
                "betweenness": rec.get("betweenness", 0.0),
                "total_brokerage": rec.get("total", 0),
            })
    manifest_path = snap_dir / "role_classification.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "kind", "slug", "role", "core_periphery", "partition_value",
                "degree", "betweenness", "total_brokerage",
            ],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)
    log.info("wrote %s (%d rows)", manifest_path.relative_to(REPO), len(manifest_rows))

    # Build pyvis figures (agency + country; crime-type omitted — degenerate)
    build_network_html(
        data["edges"]["agency"],
        role_agency,
        kind="agency",
        title="Agency Network — PoC v5 (roles)",
        out_path=FIG_DIR / "agency-network.html",
    )
    build_network_html(
        data["edges"]["country"],
        role_country,
        kind="country",
        title="Country Network — PoC v5 (roles)",
        out_path=FIG_DIR / "country-network.html",
    )

    # Cosmos role data (with edges)
    export_cosmos_roles(
        {"agency": role_agency, "country": role_country, "crime_type": role_crime},
        {
            "agency": data["edges"]["agency"],
            "country": data["edges"]["country"],
            "crime_type": data["edges"]["crime_type"],
        },
        COSMOS_DIR / "sna-roles.json",
        snap_dir.name,
    )
    # Sync to docs/cosmos/ so the deployed build picks it up without a rebuild
    docs_cosmos = REPO / "docs" / "cosmos" / "sna-roles.json"
    if docs_cosmos.parent.exists():
        docs_cosmos.write_text(
            (COSMOS_DIR / "sna-roles.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        log.info("synced %s", docs_cosmos.relative_to(REPO))

    # Summary print
    for kind, df in (("agency", role_agency), ("country", role_country), ("crime_type", role_crime)):
        print(f"\n=== {kind} role distribution ===")
        counts = df["role"].value_counts()
        for role, n in counts.items():
            print(f"  {role:22s} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
