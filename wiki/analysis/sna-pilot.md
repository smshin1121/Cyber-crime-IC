---
type: analysis
title: "SNA Pilot — Two-Mode Network Reproduction (PoC)"
analysis_type: effectiveness-assessment
scope: "PoC v5 reproduction of paper.pdf 2-mode network methodology on the current wiki corpus, after YAML-quoting repair + alias canonicalization + bare-string normalization + crime_types list schema migration + source-side country bare-string repair + source-backed `participating_countries` enrichment on the 46-op Eurojust/Europol/INTERPOL subset (20 applied). Multi-value crime_types backfill and broader countries_lt_2 enrichment pending before Step B."
confidence: medium
key_judgments:
  - judgment: "The wiki corpus supports paper-style 2-mode SNA. After YAML repair (+11 ops) and alias canonicalization (3 agency mappings), the current snapshot (N=72 operations) reproduces the paper's headline structural patterns: US top country degree + betweenness, FBI top agency degree after alias merge, INTERPOL low-deg / high-btw broker signature, country network fully connected."
    confidence: high
  - judgment: "Europol EC3 ranks above FBI in our subset (agency degree 0.667 vs 0.569) where the paper has FBI > Europol (0.494 vs 0.311). Likely a corpus-composition artifact of the audit filter removing US-DOJ procedural wrappers, not a substantive divergence in the underlying cooperation network."
    confidence: medium
  - judgment: "Crime-type network is not directly comparable to the paper: our schema is single-valued `crime_type` per operation, which produces a star topology (transitivity 0, community detection degenerate). Must be resolved in Step B before numeric comparison."
    confidence: high
sources_consulted: 72
entities_referenced: []
generated_from: query
query_prompt: "현재 wiki에 페이지를 추가하여 SNA 분석 결과를 반영하고 싶다. 수집된 데이터를 기반으로 paper.pdf에서 분석한것과 유사하게 SNA 분석을 할 수있는가?"
created: 2026-04-20
updated: 2026-04-20
---

## Summary

This is the **PoC snapshot** of the 2-mode network methodology from `paper.pdf` ("Structure and Roles of International Cybercrime Cooperation: A Two-Mode Network Analysis") applied to the current wiki corpus. It is **not** a re-implementation of the paper — the corpora, screening rules, node-set scales, and tool stacks differ. It is a *first baseline* against which Step-B (post-cleanup full reproduction) will be compared.

All snapshot artifacts are in `_workspace/sna/out/2026-04-19-d50e3208/` — edge lists, node metadata, metrics JSON, included/excluded operation lists, and the manifest.

## Snapshot metadata

| Field | Value |
|---|---|
| `snapshot_date` | **2026-04-19** (UTC) |
| `snapshot_id` | `2026-04-19-d50e3208` |
| `git_ref.head` | `d50e3208` (branch `master`, working tree dirty) |
| `rules_version` | `poc-v5` (v4 + source-side country bare-string repair + source-backed `participating_countries` enrichment on the Eurojust/Europol/INTERPOL subset) |
| `operations_files_scanned` | 1,136 |
| `included_operations_count` | **73** |
| `excluded_operations_count` | **1,062** |
| `enrichment_subset_size` | **46** (ops with Eurojust/Europol/INTERPOL-anchored source AND `participating_countries` count ≤ 1) |
| `enrichment_applied` | **20** (of 46 subset — 46 subset → 20 applied; source-backed country enrichment only; no inferred countries added) |
| `alias_slot_merges` | **21** (3 agency mappings: `fbi`, `usdoj`, `interpol-igci`) |
| `bare_string_normalizations` | **88** (bare strings slugified; 33 country entries merged into existing canonical pages) |
| `tool_versions` | Python 3.14.3, networkx 3.6.1, pandas 3.0.2, pyyaml 6.0.2 |

### Exclusion reason breakdown

| Reason | Count | Meaning |
|---|---:|---|
| `countries_lt_2` | 1,025 | Operation page has fewer than 2 distinct `participating_countries` entries after wikilink normalization |
| `status_not_live` | 17 | `status` ∉ {`completed`, `ongoing`} — stubs, planned, classified |
| `agencies_lt_2` | 13 | Fewer than 2 distinct `participating_agencies` (after lead/coordinating merge) |
| `not_operation_type` | 7 | File parses but `type: operation` header is missing or different |
| `no_enforcement_action` | 1 | `enforcement_type` list is empty or has no enforcement keyword |
| `parse_error` | 0 | YAML URL-quoting bug fixed by `tools/repair_yaml_quotes.py` (13 canonical ops recovered incl. alphabay, silk-road, trickbot, dridex, onymous, power-off, rewired, jackal-iii, haechi-iii, haechi-vi, myanmar-kokang, bidencash, carding-action-2020) |
| `crime_type_missing` | 0 | — |
| `audit_denylist` | 0 | None of the 14 audit-denylist slugs were still in the wiki at snapshot time (already removed) |
| `domestic_followon_pattern` | 0 | Soft regex pattern + `countries ≤ 2` AND condition caught no additional cases beyond the hard filter |

### Snapshot node + edge counts

| Network | Operations (mode-1) | Mode-2 nodes | Edges |
|---|---:|---:|---:|
| Operation × Country | 73 | 109 | 571 |
| Operation × Agency | 73 | 78 | 360 |
| Operation × Crime-type | 73 | 15 | 75 |

Paper for comparison: 164 operations × 131 countries / 222 agencies / 204 crime-types with 908 / 830 / 835 edges. Country count dropped from v2's 133 to 109 after bare-string normalization merged 24 duplicates (e.g., `"France"` bare-string → `france` canonical slug). Agency count unchanged (11 bare-strings normalized but none matched existing canonical slugs; the new slugs are sub-units like `spain-policia-nacional`, `israel-police`). PoC v5 added +5 country edges and +1 operation after source-backed enrichment of the 46-op Eurojust/Europol/INTERPOL subset (20 applied).

## Inclusion rules (from `_workspace/sna/edge-schema-and-inclusion-rules.md`)

Hard filters (mechanical): `type: operation` AND `status ∈ {completed, ongoing}` AND `≥ 2 distinct participating_countries` AND `≥ 2 distinct participating_agencies` (lead + coordinating merged in) AND `crime_type` non-empty AND `enforcement_type` contains at least one of `{arrest, seizure, takedown, extradition, indictment, asset_freeze}`.

Soft filter: domestic-followon filename pattern excluded only when `participating_countries ≤ 2` (regex list in `tools/sna_analysis.py`).

Manual denylist: `_workspace/sna/audit-denylist.txt` (14 slugs from `[[international-cooperation-operation-audit-2026-04]]`) — at snapshot time all 14 were already physically removed from the wiki.

## Cohesion metrics (PoC vs. paper)

| Metric | Paper Agency | PoC Agency | Paper Country | PoC Country | Paper Crime | PoC Crime |
|---|---:|---:|---:|---:|---:|---:|
| Density | 0.023 | 0.064 | 0.042 | 0.059 | 0.025 | 0.071 |
| Fragmentation | 0.086 | 0.039 | 0.000 | **0.000** | 0.000 | **0.879** |
| Avg distance | 4.022 | 3.336 | 3.551 | 3.822 | 3.921 | 1.913 |
| Diameter | 10.000 | 6 | 8.000 | 8 | 8.000 | 2 |
| Radius | 1.000 | 4 | 4.000 | 4 | 5.000 | 1 |
| Transitivity (mode-2 projection) | 0.337 | 0.648 | 0.386 | 0.673 | 0.341 | 0.000 |
| Components | — | 2 | — | **1** | — | 14 |

**Observations** (confidence medium unless stated):

- **Country network is now fully connected** (fragmentation 0.000, single 205-node component) — matches the paper exactly. The YAML repair reinstated canonical ops (silk-road, trickbot, dridex, onymous, etc.) that bridged the previously-disjoint regional clusters.
- **Higher density across all three** (~2-3x paper's) is almost certainly a sample-size effect: our 72 operations pack the same mode-2 nodes into a bipartite graph with a smaller denominator than the paper's 164.
- **Agency transitivity 0.648** (vs. paper 0.337) remains elevated. Likely driven by our Euro-biased subset: many operations co-include Europol + Eurojust + multiple EU national agencies, forming triangle-heavy projections. Same mechanism applies to country transitivity.
- **Crime-type fragmentation 0.879** is an almost-certainly-a-schema-artifact finding, not substantive. Our schema ties each operation to a single `crime_type` — this produces a star graph per crime type with no triangles (transitivity 0). Paper's operations carry multiple crime-types each; their crime-type network is therefore non-degenerate. **Still not comparable as currently built** — Step B must resolve.

## Centrality — top rankings

### Agency (mode-2)

| Rank | Agency | Degree | Betweenness | Closeness | Eigenvector |
|---:|---|---:|---:|---:|---:|
| 1 | Europol EC3 | **0.667** | **0.363** | 0.746 | 0.370 |
| 2 | FBI Cyber Division (`fbi`+`fbi-cyber-division` merged) | **0.569** | **0.296** | 0.694 | 0.326 |
| 3 | Eurojust | 0.389 | 0.073 | 0.591 | 0.243 |
| 4 | US DOJ (`us-doj`+`usdoj` merged) | 0.278 | 0.046 | 0.552 | 0.157 |
| 5 | Netherlands Politie | 0.264 | 0.027 | 0.507 | 0.197 |
| 6 | UK NCA | 0.250 | 0.019 | 0.502 | 0.195 |
| 7 | Germany BKA | 0.222 | 0.019 | 0.491 | 0.168 |
| 8 | INTERPOL (`interpol`+`interpol-igci` merged) | 0.194 | **0.192** | 0.504 | 0.022 |
| 9 | Australia AFP | 0.111 | 0.004 | 0.472 | 0.091 |
| 10 | US Secret Service | 0.111 | 0.009 | 0.502 | 0.077 |

Paper comparison: FBI leads (Deg 0.494, Btw 0.371), then Europol (0.311, 0.132), DOJ (0.280, 0.094), INTERPOL (0.268, 0.135).

**Interpretation** (confidence medium):

- **FBI now ranks #2 (degree 0.569, betweenness 0.296)** after the alias canonicalization pass merged `fbi` and `fbi-cyber-division`. This is within the same order of magnitude as the paper's FBI (0.494 / 0.371) and confirms that the PoC v1 FBI-split was a methodology artifact, not a data artifact.
- **Europol EC3 still leads both degree and betweenness** in our subset (0.667 / 0.363 vs. paper's 0.311 / 0.132). This is **likely a corpus-composition effect**, not a substantive divergence. The audit pass removed many US-DOJ procedural-wrapper operations; what remains is Eurojust-anchored in a large share of cases (`operation-de-fr-online-fraud-group-2026`, `operation-eur-600m-crypto-scam-network-2025`, and several other Eurojust-sourced operations per `[[international-cooperation-operation-audit-2026-04]]`).
- **INTERPOL low-degree / high-betweenness pattern reproduces the paper.** In our subset (deg 0.194, btw 0.192) INTERPOL's betweenness is comparable to its degree — the cross-domain broker signature the paper identifies for international organizations. Paper reports INTERPOL deg 0.268 / btw 0.135.
- **DOJ rank 4 matches paper's rank 3** (0.280). Close numeric alignment.

### Country (mode-2)

| Rank | Country | Degree | Betweenness | Closeness | Eigenvector |
|---:|---|---:|---:|---:|---:|
| 1 | United States | **0.667** | **0.215** | 0.716 | 0.303 |
| 2 | United Kingdom | 0.472 | 0.089 | 0.649 | 0.256 |
| 3 | Germany | 0.444 | 0.070 | 0.623 | 0.237 |
| 4 | Netherlands | 0.403 | 0.046 | 0.529 | 0.200 |
| 5 | France | 0.347 | 0.047 | 0.615 | 0.200 |
| 6 | Australia | 0.264 | 0.032 | 0.603 | 0.161 |
| 7 | Spain | 0.250 | 0.038 | 0.595 | 0.122 |
| 8 | Canada | 0.208 | 0.014 | 0.571 | 0.139 |
| 9 | Romania | 0.194 | 0.019 | 0.583 | 0.128 |
| 10 | Sweden / Italy (tie) | 0.181 | 0.016 / 0.012 | 0.581 / 0.539 | 0.128 / 0.092 |

**Notable lower-rank findings**:

| Rank (by deg) | Country | Degree | Betweenness | Note |
|---:|---|---:|---:|---|
| ~20 | Nigeria | 0.125 | **0.108** | BEC-specialist broker — **now visible after bare-string normalization** (was absent in v2 due to `"Nigeria"` bare-string entries on Operation Jackal). Paper: deg 0.140 / btw 0.111 — close match. |
| ~29 | South Africa | 0.069 | 0.066 | Similar low-deg / high-btw broker for Africa-centric ops (Sentinel Africa, Haechi). |

Paper comparison: US 0.622 / 0.389, Germany 0.233 / 0.042, UK 0.305 / 0.098, Nigeria 0.140 / 0.111.

**Interpretation** (confidence medium):

- **US leads on both degree (0.667) and betweenness (0.215) in both studies** — the "global liaison" pattern reproduces. Our betweenness (0.215) is lower than the paper's (0.389), consistent with smaller N.
- **Nigeria broker signature now reproduces the paper** (our 0.125 / 0.108 vs paper 0.140 / 0.111). Bare-string normalization of `"Nigeria"` entries in Operation Jackal and related BEC operations surfaced this latent pattern.
- **South Africa** shows a similar low-deg / high-btw broker profile — a regional analog of Nigeria's role, now visible in the Haechi and Sentinel Africa subsets.
- UK / Germany / Netherlands / France remain higher than the paper (Euro-weighted audit filter).

### Crime-type (mode-2)

With the single-valued `crime_type` schema, the crime-type-mode bipartite graph is a star — any operation connects to exactly one crime type. Degree rankings therefore only reflect how many operations reference a given crime type; betweenness, closeness, eigenvector, transitivity, and community detection are all structurally degenerate. **Top-by-degree only, reported for completeness:**

`online-fraud-ic` (18 ops), `ransomware-ic` (12), `malware-ic` (10), `bec-ic` (7), `money-laundering-ic` (7), `hacking-ic` (7), `csam-ic` (4), `cybercrime-forum-ic` (3). These counts are consistent with the paper's broad crime ordering (fraud + ransomware + malware at the top) but do not reflect brokerage structure.

**This entire mode should be rebuilt in Step B** with either (a) list-valued `crime_types: []` schema + frontmatter migration, or (b) multi-edges derived from body prose / `related_operations`.

## Components and communities

| Network | Components | Largest CC | Louvain communities | Modularity |
|---|---:|---:|---:|---:|
| Agency | 2 | 147 (98%) | 6 | 0.290 |
| Country | **1** | **205 (100%)** | 7 | 0.341 |
| Crime-type | 14 | 23 (27%) | 0 (degenerate) | 0.000 |

Paper reports: agency 5 communities / modularity 0.213, country 53 / 0.287, crime-type 4 / 0.231.

**Observations** (confidence medium):

- **Country network now matches the paper's full-connectivity claim** (fragmentation 0.000, 1 component of 205 nodes, vs paper's 0.000 fragmentation). The YAML repair reinstated canonical ops that bridged previously-disjoint regional clusters.
- Agency community count close to paper (6 vs 5). Modularity 0.290 vs paper 0.213 — still slightly higher, consistent with our cleaner Euro-biased subset.
- Country 7 communities vs paper 53. Paper's high community count likely reflects its 131-country set with many singleton-operation countries. Our 205-country set has 72 operations, so on average 3 ops per community — coarser but qualitatively similar regional structure. Modularity 0.341 is now close to paper's 0.287.
- Crime-type community detection still degenerates to 0 communities / 0 modularity — this is the schema artifact (single-valued `crime_type` → star topology → empty projection). **Not fixable without a schema decision in Step B.**

## Known limitations of this PoC (post-v2)

1. **Corpus: ~1/16 of available operation pages.** Of 1,136 operation files scanned, only 72 pass all inclusion rules. The overwhelming majority (1,025) fail the `participating_countries ≥ 2` hard filter — this is both a valid filter (domestic-only follow-ons correctly rejected) AND a surfacing of a genuine wiki enrichment gap (many ops have empty `participating_countries` fields despite being multi-country).
2. **Crime-type network is structurally not comparable** to the paper. See §Centrality / §Components-Communities above. Step B must migrate `crime_type` to a list-valued field OR derive multi-edges from body prose.
3. **Subset is Euro-biased** by construction of the audit filter. This is intentional (removes false-positive US-procedural-wrappers) but directly affects the relative centrality ordering — in particular Europol EC3 sits where the paper's FBI sat. Absolute metric comparison to the paper is **not valid**.
4. **Aliases beyond the 3 known pairs are not merged.** Current alias map (`_workspace/sna/node-alias-map.yaml`) handles only `fbi → fbi-cyber-division`, `usdoj → us-doj`, `interpol-igci → interpol`. Other duplicate slug pairs (e.g., bare-string agencies like `"DEA"`, `"IRS-CI"` appearing in operation frontmatter alongside proper wikilink slugs like `dea`) are not yet resolved.
5. **No core-periphery, no brokerage (Gould-Fernandez), no visualizations** — deferred to Step B per `_workspace/sna/edge-schema-and-inclusion-rules.md §4`.
6. **Tool differences.** Paper uses UCINET 6.816 and NetMiner 4; we use networkx 3.6.1. Algorithmic defaults on ties and disconnected components differ. Values are reproducible within our tool stack but not byte-identical to the paper's.

### Fixes applied across PoC v1 → v2 → v3 → v4

| Fix | Version | Impact |
|---|---|---|
| YAML URL-quoting repair (`tools/repair_yaml_quotes.py`) on 13 canonical ops | v1→v2 | +11 ops to included set (61 → 72); `parse_error` 13 → 0; country network went from 3 components → **1 connected component matching paper** |
| Alias canonicalization (`_workspace/sna/node-alias-map.yaml`, 3 agency mappings) | v1→v2 | 21 record-slots merged; FBI consolidated to rank 2 at degree 0.569 (was split 0.393 + 0.148); DOJ consolidated to rank 4; INTERPOL now shows the paper's low-deg / high-btw broker signature |
| Bare-string normalization (extract_wikilinks slugifies non-wikilink values) | v2→v3 | 88 bare strings slugified; country node count 133 → **109** (33 merged into existing canonical slugs like `france`, `nigeria`, `spain`, etc.); **Nigeria broker signature now visible** (deg 0.125 / btw 0.108 — close match to paper's 0.140 / 0.111) |
| **`crime_types` list schema migration** (`tools/migrate_crime_type_to_list.py`, `CLAUDE.md` updated, SNA reads canonical list + legacy single fallback) | v3→v4 | Canonical field is now `crime_types: []` list. 4 remaining ops back-filled from legacy single field; 1,124 ops already had the list form. All 72 included ops read from canonical list (0 fallback reads). **Crime-type network is still list-of-one structurally** — multi-crime backfill is Step B work — but the schema is now in place for non-degenerate analysis. |
| Source-side bare-string repair (`tools/repair_bare_country_strings.py`) — 44 country entries across 7 ops converted from bare strings (`"France"`, `Argentina`) to canonical wikilinks (`"[[france]]"`) | v4→v5 | SNA edge counts unchanged (script-side already normalized) but wiki source now canonical — build, lint, reconcile, and future ingest all benefit. Remaining 22 country bare-strings have no canonical page yet (Brunei, Cote d'Ivoire, Hong Kong (China), etc. — country-page creation is a separate backlog). |
| Source-backed `participating_countries` enrichment (`tools/enrich_participating_countries.py`) on the 46-op subset (Eurojust/Europol/INTERPOL anchor AND count ≤ 1) | v4→v5 | **46 subset → 20 applied**. **Source-backed country enrichment only; no inferred countries added.** Adjective-only matches and placeholder values (`"international"`) excluded by design. +1 op passed the `participating_countries ≥ 2` gate; +5 country edges. Manifest in `_workspace/sna/enrichment-proposals-2026-04-20.json` records `snapshot_date`, `subset_rule`, `enriched_ops_count`, `applied_detail`. Remaining 26 of the subset (11 no-sources, 11 no-extract, 2 no-key-findings, 2 empty-delta) are Step B tasks — require URL fetching or manual source reading. |

## What this PoC confirms and what it does not

- **Confirmed (high confidence):** the wiki schema supports paper-style 2-mode SNA. The mechanical pipeline (parse → filter → build 2-mode graph → compute metrics → export) works end-to-end and produces reproducible, manifest-backed snapshots.
- **Confirmed (medium confidence):** broad structural patterns of the paper reappear — core-periphery concentration hinted at by skewed degree distributions, US leads country degree + betweenness, agencies-with-breadth vs. agencies-with-brokerage split visible (INTERPOL low-deg high-btw pattern).
- **Not yet confirmed:** any absolute metric value or ranking order. The corpus is too small, Euro-biased, schema-restricted (crime-type), and alias-split to make numeric claims.
- **Clearly surfaced for fix:** a concrete data-cleanup backlog (YAML parse, alias canonicalization, crime-type multi-valued, `participating_countries` enrichment on ops that are genuinely international but have empty field) that Step B should resolve before full-paper reproduction.

## Next steps

- [x] ~~Fix YAML parse errors on the 13 canonical ops~~ — done in `tools/repair_yaml_quotes.py`; +11 ops recovered.
- [x] ~~Alias canonicalization pass (`fbi`, `usdoj`, `interpol-igci`)~~ — done in `tools/sna_analysis.py` + `_workspace/sna/node-alias-map.yaml`.
- [x] ~~Bare-string normalization~~ — done in `tools/sna_analysis.py`; 88 bare-strings slugified; Nigeria broker signature recovered.
- [x] ~~Crime-type schema decision~~ — `crime_types: []` list is the canonical field (PoC v4). `crime_type` single-value remains as read-only legacy fallback. Migration in `tools/migrate_crime_type_to_list.py`; `CLAUDE.md` operation schema updated; `sna_analysis.py` reads list first, falls back to single.
- [x] ~~Source-side bare-string repair for 33 country entries~~ — done in `tools/repair_bare_country_strings.py` (44 line fixes across 7 ops; `operation-jackal` alone had 19 bare-string countries rewritten to wikilinks).
- [x] ~~Source-backed `participating_countries` enrichment on Eurojust/Europol/INTERPOL subset~~ — 20 of 46 subset ops applied via `tools/enrich_participating_countries.py`. Source-backed country enrichment only; no inferred countries added. `_workspace/sna/enrichment-proposals-2026-04-20.json` carries the manifest.
- [ ] **Backfill multi-value `crime_types`** (Step B) — derive additional crime-type edges per op from body prose + `related_operations` union. Currently all but one of the 73 included ops are list-of-one, so the crime-type network is still effectively star-topology. Two-pronged backfill: (a) body-prose keyword extraction (automated, noisy, needs review), (b) manual enrichment on the high-impact ops first (e.g., AlphaBay has both `online-fraud-ic` and realistically `money-laundering-ic` + `csam-ic`).
- [ ] **Enrich remaining 26 subset ops** — 11 no-sources, 11 no-extract, 2 no-key-findings, 2 empty-delta. Requires URL fetching of the raw press release OR manual reading of existing raw files.
- [ ] **Country page creation for the 22 remaining bare-string countries** — Brunei, Cote d'Ivoire, Hong Kong, Kyrgyzstan, Laos, Maldives, UAE, Slovenia, Benin, Burkina Faso, Chad, Congo, DRC, Djibouti, Gabon, Malawi, Senegal, South Sudan, Uganda, Zimbabwe, Botswana, Zimbabwe. These are mentioned in ops (mostly Haechi / Sentinel-Africa) but have no canonical country page — creating them would give operation-country wikilinks a target to resolve to.
- [ ] **Enrich `participating_countries` on operations outside the 46-op subset** (larger 1,017-op backlog) — only after Step B body is drafted, so the content priorities are clear.
- [ ] **Step B** (`wiki/analysis/sna-structure-and-roles.md`): fuller numeric comparison to the paper + core-periphery (`cpnet`) + Gould-Fernandez brokerage + visualizations.

## Reproducibility

Re-run this snapshot (read-only over the wiki — produces files only under `_workspace/sna/out/`):

```bash
python tools/sna_analysis.py
```

Artifacts under `_workspace/sna/out/2026-04-19-d50e3208/`:
- `manifest.json` — snapshot metadata + exclusion breakdown
- `included_operations.txt` — 61 operation slugs
- `excluded_operations.csv` — 1,074 slugs with reason
- `edges_op_country.csv`, `edges_op_agency.csv`, `edges_op_crimetype.csv`
- `nodes_operations.csv`, `nodes_countries.csv`, `nodes_agencies.csv`, `nodes_crimetypes.csv`
- `metrics_cohesion.json`, `metrics_centrality_*.csv`, `metrics_components.json`, `metrics_community.json`

Spec documents:
- `_workspace/sna/paper-network-definitions.md` — paper methodology extraction
- `_workspace/sna/edge-schema-and-inclusion-rules.md` — PoC schema + filter rules

## Contradictions & Open Questions

> [!note] Crime-type schema
> The single-valued `crime_type` (single wikilink) schema is functional for wiki navigation but structurally insufficient for paper-style crime-type SNA. Consider migrating to `crime_types: []` list or building a derived multi-edge network in Step B.

> [!note] Audit filter directionality
> The audit filter was designed to remove false-positive US-DOJ procedural wrappers from the wiki catalog, not to normalize for SNA corpus composition. The Euro-centric skew that results is a feature of the wiki catalog policy, not a bug in the filter — but it does mean the PoC subset is **not** a sample representative of global cybercrime IC. Step B will need an explicit note on corpus composition when comparing to the paper's English-Google-News corpus.

> [!warning] Legal status check needed
> None — this page contains no legal-status claims.
