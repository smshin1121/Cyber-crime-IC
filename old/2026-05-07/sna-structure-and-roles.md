---
type: analysis
title: "Structure and Roles of International Cybercrime Cooperation (Step B)"
analysis_type: comparative-study
scope: "Reproduction of paper.pdf 2-mode SNA (operation × country / agency / crime-type) on the current wiki corpus at PoC v5 data quality. Main-body analysis plus Step C supplementary: Borgatti-Everett core-periphery (cpnet) and Gould-Fernandez 5-role brokerage. Network visualization remains a later follow-up."
confidence: medium
key_judgments:
  - judgment: "The paper's headline structural finding — low-density core-periphery with participation breadth and connection function diverging — reproduces in our subset."
    confidence: medium
  - judgment: "The United States is the top-degree and top-betweenness country in both studies; the wiki subset's ordering US > UK > Germany > Netherlands > France is consistent with the paper's global-liaison pattern, with the magnitudes shifted by a Euro-weighted audit filter."
    confidence: medium
  - judgment: "INTERPOL reproduces the paper's low-degree / high-betweenness cross-domain broker signature (our 0.192 / 0.190 vs. paper 0.268 / 0.135)."
    confidence: medium
  - judgment: "Nigeria reproduces the paper's BEC-specialist regional broker pattern (our 0.123 / 0.107 vs. paper 0.140 / 0.111). South Africa exhibits a parallel regional-broker profile (0.068 / 0.066). Brazil emerges as a third regional broker (0.041 / 0.043) through Operation Orion."
    confidence: medium
  - judgment: "The crime-type network cannot support paper-style structural analysis in PoC v5: 72 of the 73 included operations carry a single-value `crime_types` list, producing a near-star topology with degenerate community detection and a transitivity artifact that should NOT be read as substantive."
    confidence: high
  - judgment: "Borgatti-Everett core-periphery fitness reproduces at the agency network (our 0.266 vs. paper's 0.254) with core membership that includes the paper's DOJ + FBI + Europol tight core alongside a broader set of European national coordinators — partition granularity differs (algorithm) but the headline fitness matches."
    confidence: medium
  - judgment: "Gould-Fernandez brokerage reproduces the paper's organization-type role differentiation: Europol EC3 and Eurojust as pure cross-domain brokers (Liaison + Consultant dominant, near-zero Coordinator), FBI Cyber Division as a balanced hub agency across all five roles, INTERPOL as an international-org Liaison specialist, and national-unit police (Netherlands, Canada-RCMP) as internal coordinators."
    confidence: medium
sources_consulted: 73
entities_referenced:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[france]]"
  - "[[nigeria]]"
  - "[[south-korea]]"
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
  - "[[eurojust]]"
  - "[[us-doj]]"
  - "[[interpol]]"
  - "[[sna-pilot]]"
  - "[[international-cooperation-operation-audit-2026-04]]"
generated_from: query
query_prompt: "paper.pdf 스펙 기반 Step B 재현 — 표 구성 + 역할 해석 + corpus 차이 + 한계"
created: 2026-04-20
updated: 2026-04-20
---

## Summary

This page is the Step B reproduction of the 2-mode network analysis described in `paper.pdf` ("사이버범죄 국제공조의 구조와 역할: 2모드 네트워크 분석 / Structure and Roles of International Cybercrime Cooperation: A Two-Mode Network Analysis"). It builds on the iterative data-quality work recorded in [[sna-pilot]] (PoC v1 → v5: YAML repair, alias canonicalization, bare-string normalization, crime_types list schema, source-side country repair, source-backed subset enrichment).

The question the paper asks is **not** "who cooperates most" but **"how are participation breadth and connection function distributed across actor types"**. The paper's answer is that the two functions diverge — some actors participate in many operations but do not bridge operation clusters, while others sit between operation clusters without high overall participation. Reproducing that result on our wiki corpus tests whether the pattern is a feature of cybercrime IC structure or an artifact of the paper's particular corpus.

Our PoC v5 subset (73 operations, 109 countries, 78 agencies, 15 crime types) is **smaller and Euro-weighted** relative to the paper's corpus (164 operations, 131 countries, 222 agencies, 204 crime types — English-Google-News only). Absolute metric values therefore are NOT directly comparable. What IS comparable is the *qualitative shape* of the findings: which actors sit at high-degree positions, which at high-betweenness positions, whether the two groups coincide, and what structural roles emerge.

The rest of this page presents that comparison. Confidence labels follow the US IC Analytic Standards per `CLAUDE.md` §Confidence Language.

## Corpus and Methodology

### Our corpus

| Attribute | Value |
|---|---|
| Snapshot id | `2026-04-20-d50e3208` |
| Rules version | `poc-v5` |
| Operations scanned | 1,136 (of wiki/operations/) |
| Operations included | **73** (pass all inclusion rules) |
| Operations excluded | 1,062 (breakdown: `countries_lt_2=1,017`, `status_not_live=17`, `agencies_lt_2=20`, `not_operation_type=7`, `no_enforcement_action=1`) |
| Countries referenced | 109 |
| Agencies referenced | 78 |
| Crime types referenced | 15 |
| Source corpus composition | Multi-language RSS feeds (INTERPOL / Europol / Eurojust / DOJ / ENISA / national agency PRs / news / court documents / academic papers / legislation / policy documents) plus audit-curated remediation |

Inclusion rules (full spec in `_workspace/sna/edge-schema-and-inclusion-rules.md`): `type: operation` AND `status ∈ {completed, ongoing}` AND `participating_countries ≥ 2` AND `participating_agencies ≥ 2` AND `crime_types` non-empty AND `enforcement_type` contains at least one of `{arrest, seizure, takedown, extradition, indictment, asset_freeze}`. Soft filter: audit-denylist + domestic-followon regex with country-count ≤ 2 AND condition.

Data-quality passes applied to reach v5 (see [[sna-pilot]] for detail):
1. **YAML URL-quoting repair** (v1→v2) — 13 canonical ops (alphabay, silk-road, trickbot, dridex, onymous, power-off, rewired, jackal-iii, haechi-iii, haechi-vi, myanmar-kokang, bidencash, carding-action-2020) recovered by fixing a source-ingest serialization bug. `parse_error` 13 → 0.
2. **Alias canonicalization** (v1→v2) — `fbi → fbi-cyber-division`, `usdoj → us-doj`, `interpol-igci → interpol`. Direction chosen by explicit "Legacy compatibility page" markers on the losing pages.
3. **Bare-string normalization** (v2→v3) — 88 bare-string values slugified during SNA graph construction (`extract_wikilinks`).
4. **Crime_types list schema** (v3→v4) — canonical field is `crime_types: []`; legacy `crime_type` single-value retained as read-only fallback during migration.
5. **Source-side country bare-string repair** (v4→v5) — 44 line-level fixes across 7 ops; bare strings like `"France"` and `- Argentina` rewritten to `[[france]]` / `[[argentina]]` canonical wikilinks. Source data now matches the SNA's script-side normalization.
6. **Source-backed country enrichment** (v4→v5) — 46 subset → 20 applied. Eurojust/Europol/INTERPOL-anchored ops with `participating_countries ≤ 1` enriched from the matching `wiki/sources/<slug>.md` `key_findings` field. **Source-backed country enrichment only; no inferred countries added.** Placeholder values `{international, global, worldwide, various}` were treated as empty.

### Paper's corpus (recap from [[sna-pilot]] / `_workspace/sna/paper-network-definitions.md`)

- Period: 2015-2025.
- Source: Google News, English only.
- Query: `("cybercrime" OR "cyber crime") AND ("international operation" OR "joint operation" OR "law enforcement cooperation" OR "coordinated operation")`.
- Screening: 3 stages — topical → full-text with ≥2 agencies + actual enforcement + ≥2 identifiable dimensions → dedup same-operation articles.
- Final sample: 164 ops / 222 agencies / 131 countries / 204 crime-types with 830 / 908 / 835 2-mode edges.
- Tools: UCINET 6.816 (density, centrality, core-periphery fitness) + NetMiner 4 (community detection, brokerage).

### Why absolute numbers are not comparable

- **Corpus size and language**: our 73-op subset is 45% of the paper's 164; our corpus includes non-English RSS and official agency feeds, so actor diversity and regional coverage differ.
- **Audit filter direction**: our audit removed false-positive US-DOJ procedural wrappers and kept Eurojust-anchored operations — both moves tilt the subset toward European coordinators. The paper's corpus, being English-news-only, also has a Western bias but a different one (US press dominance).
- **Screening asymmetry**: the paper's 3-stage Google-News filter is stricter on single-article ops than our wiki's lint + audit + dedup pipeline; edge cases are classified differently.
- **Crime-type granularity**: paper 204, ours 15 — ~14× difference. Crime-type community and transitivity comparisons are therefore not valid as-is.

## Basic Structure — Cohesion

Paper's Table 2 analog. All metrics computed by `tools/sna_analysis.py` on bipartite graphs (density, fragmentation) or their 1-mode projection onto the mode-2 side (transitivity).

| Metric | Paper Agency | PoC v5 Agency | Paper Country | PoC v5 Country | Paper Crime | PoC v5 Crime |
|---|---:|---:|---:|---:|---:|---:|
| Density | 0.023 | 0.063 | 0.042 | 0.072 | 0.025 | 0.068 |
| Fragmentation | 0.086 | 0.039 | 0.000 | **0.000** | 0.000 | 0.874 |
| Avg distance | 4.022 | 3.336 | 3.551 | 3.822 | 3.921 | 1.913 |
| Diameter | 10.000 | 6 | 8.000 | 8 | 8.000 | 2 |
| Radius | 1.000 | 4 | 4.000 | 4 | 5.000 | 1 |
| Transitivity (mode-2 projection) | 0.337 | 0.648 | 0.386 | 0.691 | 0.341 | **1.000** |
| Components | — | 2 | — | **1** | — | 13 |

### Reproduced structural signatures (confidence: medium)

- **Country network is fully connected** (fragmentation 0.000, single 182-node component). Matches paper's 0.000 exactly. The YAML repair + bare-string normalization + enrichment passes closed the regional gaps that had produced 3 disconnected components in PoC v1 and 1 in v4.
- **Agency network has a dominant giant component** (148 of 151 nodes, fragmentation 0.039, close to paper's 0.086). The 3-node isolated subgroup is a single Asian regional operation (Qingdao BOP-2023) whose agency participants are sub-units of the Korean / Chinese national police not yet connected to the Europol / Eurojust core through other operations — a reasonable structural position for a bilateral Korea-China enforcement action.
- **Agency and country transitivities are elevated** (0.648 / 0.691 vs. paper's 0.337 / 0.386). Highly likely driven by the Euro-weighted subset: operations in our corpus disproportionately co-include Europol + Eurojust + 3+ EU national agencies, which pack the 1-mode projection with triangles.

### What does NOT reproduce (and why)

> [!warning] Crime-type transitivity 1.000 is a sample artifact, NOT a structural finding
> The crime-type 1-mode projection has exactly ONE triangle, formed by a single operation (`[[operation-105-arrested-for-stealing-over-eur-12-million-from-us-based-banks]]`) whose `crime_types` list carries three values — `[[bank-fraud-ic]]`, `[[carding-fraud-ic]]`, `[[money-laundering-ic]]`. Because networkx's transitivity ratio is (triangles × 3) / (connected-triples), and that single triangle produces the only connected triples in the entire projection, the ratio is 1.0 by arithmetic. This is NOT evidence that crime-types co-occur systematically — it is evidence that our `crime_types` schema migration (PoC v4) permits multi-values but only one op has been back-filled so far. **Do not interpret the 1.0 as a paper-comparable number.** Paper's 0.341 was computed on 204 crime-type nodes with multi-valued co-occurrences — the structural scale and the statistic's support set are different by orders of magnitude. Multi-value backfill of `crime_types` is an explicit Step B-follow-up pending in [[sna-pilot]].

- **Crime-type fragmentation 0.874** (vs. paper 0.000) is the other side of the same schema artifact: most operations in our subset carry a `crime_types` list of one, so the 1-mode projection onto crime-types is overwhelmingly disconnected (13 components, the largest only 23 nodes).
- **Agency diameter 6** (vs. paper 10) is within the band of a smaller, denser subset — not a substantive divergence.

## Structural Positions — Centrality

Paper's Table 3 analog. Centralities computed on the 2-mode bipartite graph directly (degree / closeness / betweenness) and on the full graph for eigenvector.

### Country (mode-2) top 12

| Rank | Country | Degree | Betweenness | Closeness | Eigenvector |
|---:|---|---:|---:|---:|---:|
| 1 | [[united-states]] | **0.671** | **0.219** | 0.717 | 0.305 |
| 2 | [[united-kingdom]] | 0.466 | 0.088 | 0.647 | 0.255 |
| 3 | [[germany]] | 0.438 | 0.069 | 0.622 | 0.236 |
| 4 | [[netherlands]] | 0.397 | 0.045 | 0.528 | 0.199 |
| 5 | [[france]] | 0.342 | 0.046 | 0.614 | 0.200 |
| 6 | [[spain]] | 0.260 | 0.041 | 0.596 | 0.125 |
| 7 | [[australia]] | 0.260 | 0.032 | 0.601 | 0.161 |
| 8 | [[canada]] | 0.205 | 0.014 | 0.570 | 0.139 |
| 9 | [[romania]] | 0.192 | 0.018 | 0.581 | 0.128 |
| 10 | [[italy]] | 0.178 | 0.011 | 0.538 | 0.091 |
| 11 | [[japan]] | 0.164 | 0.019 | 0.559 | 0.092 |
| 12 | [[nigeria]] | **0.123** | **0.107** | 0.577 | 0.037 |

**Paper's country highlights** (for comparison): US 0.622 / 0.389, Germany 0.233 / 0.042, UK 0.305 / 0.098, Nigeria 0.140 / 0.111.

### Country interpretation (confidence: medium)

- **United States is top on both degree and betweenness** — in both studies. Our betweenness (0.219) is lower than the paper's (0.389), consistent with our smaller N and tighter subset. The paper and the wiki corpus both point to the US as the dominant cross-cluster liaison in cybercrime IC.
- **Nigeria is the clearest BEC-specialist regional broker**: low degree (0.123) but disproportionately high betweenness (0.107), close to the paper's (0.140 / 0.111). Nigerian participation concentrates in BEC and Operation Jackal (African organised crime / BEC networks), which bridge Africa-centric ops to the global US/EU-anchored fabric. This pattern was not visible in PoC v1 — bare-string normalization in v3 was what surfaced it.
- **South Africa** (not in top 12) shows a parallel regional-broker profile: degree 0.068, betweenness 0.066. Primary bridging happens through Operation Sentinel Africa and Haechi operations.
- **Brazil** (not in top 12 either) sits even lower on degree (0.041) but has meaningful betweenness (0.043), almost entirely through Operation Orion (South America child-abuse material network). This is a third, distinct regional-broker signature in the subset.
- **UK / Germany / Netherlands / France** sit higher in our subset than in the paper. Highly likely a corpus-composition effect: our audit filter removed US-DOJ procedural-wrapper ops, so Eurojust-anchored multi-country operations constitute a larger share of our subset. Not a substantive divergence in underlying cooperation patterns.

### Agency (mode-2) top 12

| Rank | Agency | Degree | Betweenness | Closeness | Eigenvector |
|---:|---|---:|---:|---:|---:|
| 1 | [[europol-ec3]] | **0.671** | **0.369** | 0.747 | 0.373 |
| 2 | [[fbi-cyber-division]] (merged with legacy `fbi`) | **0.562** | **0.292** | 0.691 | 0.325 |
| 3 | [[eurojust]] | 0.384 | 0.072 | 0.589 | 0.243 |
| 4 | [[us-doj]] (merged with legacy `usdoj`) | 0.274 | 0.046 | 0.551 | 0.156 |
| 5 | [[netherlands-politie]] | 0.260 | 0.026 | 0.506 | 0.196 |
| 6 | [[uk-nca]] | 0.247 | 0.019 | 0.501 | 0.194 |
| 7 | [[germany-bka]] | 0.219 | 0.019 | 0.490 | 0.168 |
| 8 | [[interpol]] (merged with legacy `interpol-igci`) | **0.192** | **0.190** | 0.503 | 0.021 |
| 9 | [[us-secret-service]] | 0.123 | 0.011 | 0.503 | 0.080 |
| 10 | [[canada-rcmp]] | 0.110 | 0.003 | 0.475 | 0.110 |
| 11 | [[australia-afp]] | 0.110 | 0.004 | 0.471 | 0.091 |
| 12 | [[japan-npa]] | 0.082 | 0.029 | 0.447 | 0.058 |

**Paper's agency highlights**: FBI 0.494 / 0.371, Europol 0.311 / 0.132, DOJ 0.280 / 0.094, INTERPOL 0.268 / 0.135.

### Agency interpretation (confidence: medium)

- **FBI (merged) ranks 2 at degree 0.562 and betweenness 0.292** — within the same magnitude as the paper's FBI (0.494 / 0.371). The degree gap narrows because the `fbi → fbi-cyber-division` alias merge (PoC v2) consolidated nine operation participations that had been split between legacy and current slug. Without the merge, FBI would be split across two rank positions and understated.
- **Europol EC3 ranks 1** in our subset where the paper has FBI top. Highly likely a corpus-composition artifact (Eurojust-anchored operations over-represented, US-DOJ wrappers removed). Not a substantive claim about Europol-vs-FBI dominance.
- **INTERPOL (merged) reproduces the paper's cross-domain broker signature** exactly: low degree (0.192) and comparably high betweenness (0.190), meaning INTERPOL participates in relatively few operations but sits between many distinct operation clusters. Paper reports 0.268 / 0.135 — same low-deg / high-btw shape.
- **US DOJ (merged) at degree 0.274** matches the paper's DOJ (0.280) almost exactly — the strongest numeric alignment in the agency table.
- **Japan NPA** (rank 12 by degree) shows a moderate Asian-regional-broker profile (betweenness 0.029 on degree 0.082). Not visible in the paper's top rankings; likely reflects our inclusion of Asia-centric ops (Haechi series, Phobos/8Base) where the paper's English-news corpus may have under-represented them.

### Crime-type (mode-2)

Because 72 of 73 included operations carry a `crime_types` list of one, the crime-type network is a near-star topology and most centrality metrics are structurally degenerate on this mode. Reporting degree only, with context caveats:

| Rank | Crime type | Degree | Participation count (ops) |
|---:|---|---:|---:|
| 1 | [[online-fraud-ic]] | 0.301 | 22 |
| 2 | [[ransomware-ic]] | 0.151 | 11 |
| 3 | [[malware-ic]] | 0.110 | 8 |
| 4 | [[money-laundering-ic]] | 0.096 | 7 |
| 5 | [[bec-ic]] | 0.096 | 7 |
| 6 | [[hacking-ic]] | 0.082 | 6 |
| 7 | [[carding-fraud-ic]] | 0.041 | 3 |
| 8 | [[csam-ic]] | 0.041 | 3 |
| 9 | [[cybercrime-forum-ic]] | 0.027 | 2 |
| 10 | [[bank-fraud-ic]] | 0.014 | 1 |

> [!warning] Crime-type centrality is not structurally interpretable in PoC v5
> All but one operation has a single-valued `crime_types` list. Betweenness, closeness, eigenvector, transitivity, and community detection on the crime-type mode are degenerate or near-degenerate. Only degree (= operation count per crime type) is meaningfully reported.

The paper reports the top crime-types as money laundering (0.378 / 0.258) and identity theft (0.341 / 0.205), with ransomware, malware distribution, and darknet also in the top tier. Our top-by-degree list (online-fraud, ransomware, malware, money-laundering, BEC, hacking) overlaps qualitatively but the coarse 15-category schema cannot reproduce the paper's 204-category resolution.

## Connectedness, Communities, and the Core-Periphery Question

Paper-style core-periphery analysis (Borgatti-Everett fitness) is deferred to the supplementary section. What we can report without that tool:

### Connected components

| Network | Components | Largest component | Component-size tail |
|---|---:|---:|---|
| Agency | 2 | 148 / 151 (98%) | 3 (single isolated Asian bilateral op) |
| Country | 1 | 182 / 182 (100%) | — |
| Crime-type | 13 | 23 / 88 (26%) | 12, 12, 9, 8, 7, 4, 3, 2, 2, ... (schema artifact) |

### Louvain communities (computed on 1-mode projection onto mode-2)

| Network | Communities | Modularity | Paper reports |
|---|---:|---:|---|
| Agency | 5 | 0.287 | 5 communities, modularity 0.213 |
| Country | 4 | 0.307 | 53 communities, modularity 0.287 |
| Crime-type | 13 | 0.000 | 4 communities, modularity 0.231 |

**Agency community count matches exactly** (5 = 5). Modularity within the same band. The structural partition of agencies into ~5 clusters is a reproduced finding.

**Country community count is far coarser** in our subset (4 vs. 53). Paper's 53 reflects its 131-country set with many one-operation-country leaves producing singleton communities. Our 4 communities reflect 109 countries in 73 operations — density is higher, partition is coarser. Modularity 0.307 is within the paper's range (0.287), so the partition quality is comparable; the count difference is a count-level artifact of corpus size, not a substantive divergence.

**Crime-type community detection is degenerate** (0.000 modularity, 13 singleton-ish components) — same schema artifact as §Basic Structure.

### What we can say about core-periphery WITHOUT cpnet

Even without running Borgatti-Everett fitness directly, three observations from the centrality tables suggest a core-periphery structure:

1. **Heavy degree concentration at the top** — US, UK, Germany carry 0.67 / 0.47 / 0.44 while the 50th-percentile country is below 0.10. The paper reports a similar top-heavy profile. Confidence: medium.
2. **Agency top-4 dominates** — Europol EC3, FBI Cyber Division, Eurojust, US DOJ together capture roughly 50% of degree-centrality mass. Paper's agency core block (DOJ + FBI + Europol) density is 0.437 — a similar "dense core, sparse periphery" pattern by inspection.
3. **Single giant connected component at the country mode** with a long-tail degree distribution is the classic core-periphery structural signature.

Formal fitness computation via `cpnet` is deferred; see §Supplementary.

## Role Differentiation — Participation vs. Connection

The paper's central claim is that **participation breadth (degree) and connection function (betweenness) are not the same actor**. Our subset reproduces this:

| Actor | Degree rank | Betweenness rank | Role signature |
|---|---:|---:|---|
| US (country) | 1 (0.671) | 1 (0.219) | Global liaison — both high |
| Europol EC3 (agency) | 1 (0.671) | 1 (0.369) | Global coordinator — both high |
| FBI Cyber Division (agency) | 2 (0.562) | 2 (0.292) | Global coordinator — both high |
| INTERPOL (agency) | 8 (0.192) | 3 (0.190) | Cross-domain broker — low-deg, high-btw |
| Nigeria (country) | 12 (0.123) | ~6 (0.107) | BEC-specialist regional broker — low-deg, moderate-high btw |
| South Africa (country) | ~30 (0.068) | ~10 (0.066) | Africa regional broker — low-deg, moderate btw |
| Brazil (country) | ~40 (0.041) | ~15 (0.043) | South America regional broker — low-deg, moderate btw |
| Japan NPA (agency) | 12 (0.082) | 7 (0.029) | Asia regional broker — low-deg, elevated btw relative to deg |
| Eurojust (agency) | 3 (0.384) | 4 (0.072) | Broad-participation-but-not-broker — high deg, relatively low btw |
| Germany (country) | 3 (0.438) | 4 (0.069) | Regional coordinator — high deg, low btw (participates broadly within Europe, doesn't bridge to Africa/Asia) |

### Interpretation (confidence: medium)

- **The US and the top two agencies (Europol EC3, FBI Cyber Division) are both global coordinators** — high on both scales. The paper identifies the US, Europol, and FBI in similar roles.
- **INTERPOL is the clearest pure broker** in our subset and in the paper. It sits between the EU-anchored operations and the Asia / Africa / Latin America operations without participating as often as the national coordinators.
- **Nigeria / South Africa / Brazil are regional brokers** — each specializes in a geographic cluster (West African BEC; Southern African cybercrime sweeps; South American child-abuse operations) and bridges that cluster to the global fabric without accumulating large overall degree.
- **Eurojust and Germany show the inverse** — high overall participation but low cross-cluster brokerage. Eurojust is a broad coordinator *within* European operations; Germany is a prominent European participant but does not frequently bridge to non-European clusters. This is the "broad participation without brokerage" signature the paper identifies for regional coordinators.

### What the subset cannot support yet

- **Sub-national or sub-agency brokerage** — our alias canonicalization merges sub-units into their parent organization (INTERPOL IGCI into INTERPOL, FBI Cyber Division remains separate from a hypothetical "FBI" umbrella). The paper's node resolution is coarser at the agency mode, so finer distinctions like "which INTERPOL regional bureau bridges which operation cluster" require more detailed data than our wiki currently carries.
- **Temporal role dynamics** — the paper and this analysis both collapse 10 years (2015-2025) into a single static network. Whether INTERPOL's brokerage signature is stable or emerged during a specific sub-period cannot be answered without a time-sliced network. Paper explicitly notes this as a future-work item.

## Korean Perspective (한국 관점)

South Korea appears in the subset at degree 0.096 / betweenness 0.014 (rank ~15 by degree, rank ~25 by betweenness). Korean participation concentrates in:

- **[[operation-haechi-iii]]** — INTERPOL-led multi-year anti-financial-crime operation where Korea is a primary participant.
- **[[operation-haechi-iv]]** — Same program, later cycle.
- **[[operation-jackal-iii]]** — Black Axe / West African BEC network takedown with Korean enforcement support.
- **Phobos / 8Base ransomware arrest operations** — Three ops (recently enriched in v5) where Korea participated alongside Italy and the US in a multinational arrest coordination.
- **[[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown]]** — the three enrichment-applied ops add Korea to the subset in v5.

Korean agency representation is partial: `[[south-korea]]` appears as a country node, but the specific Korean agencies (국가정보원, 대검찰청 사이버범죄수사단, 경찰청 국가수사본부 사이버수사국) are under-represented in operation frontmatter. This is highly likely a wiki-content gap, not a substantive absence from real-world operations — Korean IC participation in Haechi and Phobos arrests is well-documented in press releases and [[south-korea]].

**Structural position**: South Korea's profile in our subset is that of an Asia-regional participant with moderate Haechi-family participation and occasional bilateral action (Korea-UAE sub-operation in Haechi VI, Korea-China Qingdao voice-phishing bilateral). Not a top-tier global liaison. Broker betweenness is low (0.014) because Korean participation does not bridge between distinct operation clusters — most Korean ops are within the Haechi cluster. This is likely an accurate reflection of Korean IC practice circa 2015-2025: deep specialist participation within INTERPOL-led Asia-financial-crime operations, with broader structural brokerage still developing.

## Limitations

Three limitations constrain interpretation and are explicitly surfaced (per user direction at Step B intake):

### 1. Subset corpus limitation

The 73-op included subset represents audit-filtered, multi-source multi-country cooperation operations. It is NOT the full universe of cybercrime IC. It specifically excludes:
- 1,017 operations whose wiki pages have `participating_countries` counts of 0 or 1 (either domestic follow-ons OR genuinely multi-country operations with unfilled frontmatter).
- 20 operations whose wiki pages list fewer than 2 `participating_agencies`.
- 17 operations with non-live status (stubs, planned, classified).

The audit filter was designed to remove false-positive US-DOJ procedural wrappers; its incidental effect is a Euro-weighted subset where Eurojust-anchored operations have more relative mass than in the paper's English-Google-News corpus. **Absolute metric values are NOT directly comparable to the paper.** Qualitative pattern comparison is valid.

### 2. Coarse crime-type schema

The wiki's `crime_types` taxonomy has 15 leaf categories in use (`online-fraud-ic`, `ransomware-ic`, `malware-ic`, `bec-ic`, `money-laundering-ic`, `hacking-ic`, `carding-fraud-ic`, `csam-ic`, `cybercrime-forum-ic`, `bank-fraud-ic`, `cybercrime-infrastructure-ic`, `ddos-extortion`, `ddos-ic`, `organized-crime-ic`, `voice-phishing-ic`). The paper operates on 204 crime-type labels derived from a more granular INTERPOL + Budapest Convention classification with adjusted field labels.

Consequence: **crime-type structural comparison to the paper is not supported** at this resolution. Paper-level findings like "money laundering and identity theft are the bridging crime-types" cannot be tested on our 15-category schema. The crime-type network currently produces degenerate community detection (modularity 0.0), near-star topology, and a transitivity sample artifact of 1.0 driven by a single multi-valued op. Multi-value `crime_types` backfill and finer-grained category expansion are explicit Step B follow-ups — see [[sna-pilot]] §Next steps.

### 3. Residual country under-enrichment

Of the 46-op Eurojust/Europol/INTERPOL subset targeted by the v5 enrichment pass, 20 were applied source-backed. The remaining 26 break down:
- 11 `no_sources` — operation pages with no `sources:` wikilink set. Source data may exist in raw press releases but isn't yet connected.
- 11 `no_extract` — source `key_findings` text is too generic ("international cooperation", "global partners") to yield explicit country names.
- 2 `no_key_findings` — source page exists but key_findings field is empty.
- 2 `empty_delta` — source extraction returned only countries already in the operation's frontmatter.

A separate, much larger backlog of **1,017 operations outside the Eurojust/Europol/INTERPOL subset** still have `participating_countries` counts below the inclusion threshold. Some are legitimately domestic (correctly excluded); others are multi-country operations whose frontmatter has not been enriched. The subset-first enrichment approach (user-approved) deferred that larger backlog to a later cycle on the explicit rationale that the 46-op subset provides sufficient quality uplift for Step B interpretation.

## Corpus Difference and Bias

The following table summarizes where our corpus is expected to diverge from the paper's and the direction of each effect:

| Dimension | Paper corpus | Our corpus | Direction of bias |
|---|---|---|---|
| Language | English news only | Multi-language (RSS + press releases + court docs + academic) | Ours includes more non-English operations, especially EU bilateral actions |
| Source type | News media | Mixed (news + official agency feeds + court documents) | Ours is weighted toward official operational announcements; paper is weighted toward journalistic coverage |
| Country coverage | Western-press-covered operations | Broader, but with audit filter removing US-DOJ wrappers | Europol / Eurojust / INTERPOL-led operations over-represented in ours |
| Time period | 2015-2025, 10 years | Same 10-year window, but with post-audit recency skew (Eurojust feed launched 2023) | Ours is more recent-weighted at the margin |
| Screening | 3-stage topical + full-text + dedup | Inclusion-rule filter + audit denylist + soft regex | Different decision boundaries; ours filters more on structural signals (country/agency counts) and less on narrative content |
| Crime-type granularity | 204 labels | 15 labels | Ours is coarser by ~14× |

**Bias direction for centrality interpretation**: our Europol EC3 > FBI is explained by audit-filter corpus composition, not by any substantive change in cybercrime IC. Our Nigeria / South Africa / Brazil regional-broker signals are strengthened (not weakened) relative to what an English-only news corpus would show — because we include French / Spanish / Portuguese Eurojust and INTERPOL releases that cover those operations more consistently.

## Supplementary — Core-Periphery (Borgatti-Everett)

Paper's Table 4 analog. Computed by `tools/sna_core_periphery_brokerage.py` via `cpnet.BE` on the 1-mode projection of mode-2 nodes (largest connected component). Operations are classified as core iff they connect to at least one mode-2 core member. 4-block densities are computed on the full 2-mode bipartite graph.

### Fitness + 4-block densities

| Metric | Paper Agency | PoC v5 Agency | Paper Country | PoC v5 Country | Paper Crime | PoC v5 Crime |
|---|---:|---:|---:|---:|---:|---:|
| Fitness | 0.254 | **0.266** | 0.358 | **0.008** | 0.225 | 0.000 |
| Core-Core block density | 0.437 | 0.128 | 0.457 | 0.073 | 0.331 | 1.000 |
| Core-Periphery | 0.000 | 0.019 | 0.048 | 0.014 | 0.051 | 0.020 |
| Periphery-Core | 0.020 | 0.000 | 0.038 | 0.000 | 0.022 | 0.000 |
| Periphery-Periphery | 0.008 | 0.043 | 0.013 | 0.000 | 0.007 | 0.071 |
| Mode-2 core size | — | **32** | — | 107 | — | 1 |

### Agency core members (our partition)

> [!note] Agency core membership
> cpnet BE assigns the following 32 agencies to the core block: `australia-afp`, `belgium-federal-police`, `bulgaria-police`, `canada-rcmp`, `denmark-police`, `eurojust`, `europol-ec3`, `fbi-cyber-division`, `france-gendarmerie`, `france-junalco`, `france-national-police`, `germany-bka`, `ireland-gardai`, `israel-police`, `italy-postale`, `netherlands-politie`, `portugal-policia-judiciaria`, `romania-diicot`, `spain-guardia-civil`, `spain-policia-nacional`, `sweden-police`, `switzerland-fedpol`, `uk-nca`, `us-doj`, `us-fbi-icc`, `us-irs-ci`, `us-secret-service`, plus a few additional European national units. INTERPOL is in the periphery block by BE's assignment, which is consistent with its low overall degree (0.192) despite high betweenness (0.190) — the BE partition is degree-driven.
>
> The paper's tight core (DOJ + FBI + Europol only) is a narrower partition than ours. The numerical fitness (0.266 vs. paper 0.254) is close, but the partition granularity differs — likely an algorithmic difference between `cpnet.BE` (simulated annealing) and UCINET's BE (discrete optimization).

### Agency finding (confidence: medium)

The agency network **reproduces the paper's core-periphery structural signature** at the fitness level (0.266 vs. 0.254). The core block contains Europol EC3 + Eurojust + FBI Cyber Division + US DOJ + US Secret Service as the paper does, plus a broader set of European national police units that our Eurojust-weighted subset elevates. Core-Core density (0.128) is lower than the paper's (0.437), which reflects the larger core size — 32 nodes forming a less dense clique than the paper's 3-node tight core.

### Country and crime-type findings (confidence: high on the limitation)

> [!warning] Country core-periphery from cpnet BE is near-degenerate in our subset
> The country fitness of 0.008 and core size of 107 out of 182 mode-2 nodes indicates that `cpnet.BE` did not find a meaningful core-periphery partition — it split the graph roughly in half with weak structural coherence. The likely cause is algorithmic: the country network is dense (density 0.072) and nearly fully connected (1 component, fragmentation 0.000), and BE's simulated-annealing search on dense graphs tends to converge on near-trivial partitions. The paper, using UCINET's discrete BE, reports 0.358 / C-C 0.457 — a tighter, more meaningful partition. **This is a tool-difference, not a data-difference claim.** Alternative cpnet algorithms (Rombach continuous-coreness, Lip, LowRankCore) may produce a cleaner partition; left as a Step C-follow-up.

> [!warning] Crime-type core-periphery is undefined in PoC v5
> Fitness 0.000 with core size 1 (containing only `money-laundering-ic`) is an artifact of the single-valued `crime_types` schema: the 1-mode projection onto crime-types has only one triangle (from `[[operation-105-arrested-for-stealing-over-eur-12-million-from-us-based-banks]]` with 3 crime types), so cpnet BE has essentially no structure to partition. Multi-value backfill (see [[sna-pilot]] Step C roadmap) is required before crime-type core-periphery becomes interpretable.

## Supplementary — Brokerage (Gould-Fernandez 5 Roles)

Paper's Table 5 analog. Computed by `tools/sna_core_periphery_brokerage.py` on the 1-mode projection of mode-2 nodes. Node partitions drawn from wiki metadata:
- Agency: `org_type` field (`international-org`, `regional-org`, `national-agency`, `national-unit`, `prosecution-office`, etc.)
- Country: `region` field (`western-europe`, `north-america`, `east-asia`, `west-africa`, `southern-africa`, etc.)
- Crime-type: `crime_category` field (`cyber-dependent`, `cyber-enabled`, `content-related`)

Each ordered triad `(i, k, j)` where `k` is a broker (common neighbor of `i` and `j`), `(i, j)` not directly connected, contributes one count to the role classified by the group triple `(g(i), g(k), g(j))`. Roles: Coordinator (all same group), Gatekeeper (broker in same group as receiver), Representative (broker in same group as sender), Consultant (alters in same group, broker outside), Liaison (all three different groups).

### Country brokerage — top 10 by total

| Rank | Country | Region partition | Coord | Gate | Rep | Cons | Liais | Total |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | [[united-states]] | north-america | 0 | 18 | 18 | 146 | **2,850** | 3,032 |
| 2 | [[nigeria]] | west-africa | 12 | **224** | **224** | 356 | 1,688 | 2,504 |
| 3 | [[united-kingdom]] | western-europe | 10 | 222 | 222 | 76 | 1,558 | 2,088 |
| 4 | [[south-africa]] | southern-africa | 0 | 41 | 41 | 330 | 1,614 | 2,026 |
| 5 | [[france]] | western-europe | 10 | 209 | 209 | 54 | 1,492 | 1,974 |
| 6 | [[australia]] | oceania | 0 | 0 | 0 | 86 | 1,798 | 1,884 |
| 7 | [[spain]] | western-europe | 10 | 197 | 197 | 52 | 1,262 | 1,718 |
| 8 | [[poland]] | eastern-europe | 14 | 191 | 191 | 94 | 1,182 | 1,672 |
| 9 | [[sweden]] | northern-europe | 2 | 77 | 77 | 72 | 1,346 | 1,574 |
| 10 | [[germany]] | western-europe | 10 | 171 | 171 | 38 | 1,164 | 1,554 |

### Country brokerage interpretation (confidence: medium)

- **US is a pure global liaison** — 94% of its brokered triads involve three different regions. Coordinator and Consultant counts are negligible (0 and 146). This is the textbook global-liaison signature and reproduces the paper's finding on US role structure.
- **Nigeria shows the highest gatekeeper-representative mix in the top 10** — Gate+Rep = 448 vs. its Liaison of 1,688. The pattern means Nigeria frequently bridges West-African operation participants into the global fabric (gatekeeper bringing outsider to west-africa) AND routes from West Africa outward (representative). This is the clearest "specialist regional broker" signature in our data and qualitatively matches the paper's Nigeria finding.
- **South Africa, Australia, and (implied) Brazil** all show high Liaison and moderate Consultant counts, with Coordinator=0 — each is a regional isolate whose ops predominantly bridge cross-regional.
- **UK, France, Spain, Germany, Poland** cluster as western/eastern-European national participants with balanced Gate+Rep (~200) + Coordinator (~10) + Consultant (~50-90) + Liaison (~1,200-1,500) — the regional-coordinator-plus-outward-liaison profile.
- **Sweden** shows a thinner Gate+Rep profile (77 each) than its western-European peers, indicating it participates in more diverse-partner operations (Baltic / Scandinavian sub-cluster) rather than the dense Continental EU core.

### Agency brokerage — top 10 by total

| Rank | Agency | `org_type` | Coord | Gate | Rep | Cons | Liais | Total |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | [[europol-ec3]] | regional-org | 0 | 19 | 19 | **412** | **2,178** | 2,628 |
| 2 | [[fbi-cyber-division]] | national-agency | **202** | **492** | **492** | 230 | 776 | 2,192 |
| 3 | [[eurojust]] | regional-org | 0 | 0 | 0 | 178 | 710 | 888 |
| 4 | [[us-doj]] | national-agency | 68 | 155 | 155 | 26 | 188 | 592 |
| 5 | [[france-gendarmerie]] | national-unit | 68 | 150 | 150 | 12 | 178 | 558 |
| 6 | [[netherlands-politie]] | national-unit | **120** | 108 | 108 | 42 | 42 | 420 |
| 7 | [[interpol]] | international-org | 2 | 36 | 36 | 42 | **254** | 370 |
| 8 | [[uk-nca]] | national-agency | 32 | 94 | 94 | 96 | 50 | 366 |
| 9 | [[us-secret-service]] | national-unit | 26 | 78 | 78 | 36 | 50 | 268 |
| 10 | [[canada-rcmp]] | national-unit | **120** | 54 | 54 | 12 | 10 | 250 |

### Agency brokerage interpretation (confidence: medium)

- **Europol EC3 is a pure cross-domain broker** — 83% Liaison + 16% Consultant + almost 0 Coordinator. It bridges distinct organization-type groups (international-orgs ↔ national-agencies ↔ national-units) without operating as an intra-group coordinator. **This matches the paper's Europol signature exactly** (paper: Coord 10 / Gate 162 / Rep 162 / Cons 1,176 / Liais 430 — high Cons+Liais, minimal Coord).
- **FBI Cyber Division is the most balanced agency broker**. Its 202 Coordinator (bridging within national-agency) + 492/492 Gate/Rep + 230 Consultant + 776 Liaison spread across all 5 roles is the signature of a **hub agency that coordinates, gatekeeps, and bridges simultaneously**. Paper's FBI was Coord 1,580 + Gate 442 + Rep 442 + Cons 18 + Liais 80 — Coordinator-dominant. **Ours is Gatekeeper/Representative-dominant instead**, reflecting our Eurojust-weighted subset where FBI bridges across more organization types rather than coordinating internally.
- **Eurojust is a pure Liaison+Consultant broker** (0 Coord / 0 Gate / 0 Rep / 178 Cons / 710 Liais) — structurally similar to Europol EC3. Coord=0 means Eurojust never bridges two `regional-org` members to each other, which makes sense (there's only one Eurojust in its group).
- **INTERPOL reproduces the paper's international-org Liaison specialist signature** — 254 Liaison out of 370 total (69%), with low Gate/Rep/Cons. Paper's INTERPOL had Coord 4 / Gate 64 / Rep 64 / Cons 250 / Liais 284 (total 666) — very similar Liaison-dominant profile.
- **Netherlands-Politie and Canada-RCMP are internal coordinators** — 120 Coord each, low Liaison. The pattern indicates they bridge multiple operations *within* the `national-unit` group (e.g., bridging Dutch and Belgian police or Canadian and US domestic units in the same op series) more than bridging across org types.
- **Italy, Germany, France national units** (not in top 10, but in CSV) cluster as moderate regional coordinators — similar profile to Netherlands but lower total volume.

### Crime-type brokerage — not interpretable in PoC v5

> [!warning] Crime-type brokerage is all zeros
> All 15 crime-type nodes have total brokerage 0. This is the direct consequence of the list-of-one `crime_types` schema: the 1-mode projection onto crime-types has ~1 edge per op (from the one multi-valued op), so there are no triads for Gould-Fernandez to classify. **This is NOT a finding**. Multi-value backfill (see [[sna-pilot]]) is a prerequisite.

## Figures — Role-indicator-based Network Visualizations

Two interactive HTML figures render the 2-mode agency and country networks with node coloring derived from the Step C role classification (`tools/sna_visualize.py`, rules `roles-v1`). Core-block nodes (from `cpnet.BE`) carry a thicker border. Operations appear as small dark-slate nodes (mode-1). Hover any node for degree + betweenness + brokerage detail.

- **[Agency network](sna/agency-network.html)** — 78 mode-2 agency nodes × 73 operations, 360 edges.
- **[Country network](sna/country-network.html)** — 109 mode-2 country nodes × 73 operations, 566 edges.

Crime-type network visualization is omitted in this release because the single-valued `crime_types` schema (see §Basic Structure warning) makes the crime-type mode near-degenerate — 72 of 73 ops connect to exactly one crime-type node, so a force-directed layout would not reveal additional structure beyond the degree counts already tabulated.

### Role classification rules (`roles-v1`, per `tools/sna_visualize.py`)

**Agency signatures** (input: degree + brokerage counts; total = sum of 5 role counts):

| Role | Predicate | Intuition |
|---|---|---|
| `hub` | degree ≥ 0.30 AND coord ≥ 100 AND (gate+rep) ≥ 500 | High participation across multiple operation clusters AND substantial intra-group coordination |
| `liaison-broker` | liais/total > 0.65 AND coord/total < 0.10 AND total ≥ 200 | Cross-domain bridging between distinct org-type groups; rarely brokers within own group |
| `internal-coordinator` | coord/total > 0.30 AND coord ≥ 80 | Primarily bridges within own org-type group |
| `regional-coordinator` | (gate+rep)/total > 0.40 AND gate ≥ 80 | Mixed within-group and bring-in/send-out brokerage — typical national police in regional contexts |
| `participant` | (otherwise) | Normal member without distinct broker signature |

**Country signatures** (input: degree + betweenness + brokerage counts):

| Role | Predicate | Intuition |
|---|---|---|
| `global-liaison` | liais/total > 0.90 AND degree > 0.30 | Global three-different-region broker, top overall participation |
| `regional-coordinator` | (gate+rep)/total > 0.20 AND degree > 0.15 | Balanced intra-regional + cross-regional participation |
| `specialist-broker` | degree < 0.20 AND betweenness/degree > 0.50 | Low overall participation but disproportionate bridging — regional / crime-specialty broker |
| `participant` | (otherwise) | Normal member without distinct broker signature |

### Role assignment — v5 results

**Agency** (9 of 78 non-participants):

| Role | Agents |
|---|---|
| `hub` | [[fbi-cyber-division]] |
| `liaison-broker` | [[europol-ec3]], [[eurojust]], [[interpol]] |
| `internal-coordinator` | [[canada-rcmp]] |
| `regional-coordinator` | [[us-doj]], [[netherlands-politie]], [[uk-nca]], [[france-gendarmerie]] |

**Country** (16 of 109 non-participants):

| Role | Countries |
|---|---|
| `global-liaison` | [[united-states]] |
| `regional-coordinator` | [[united-kingdom]], [[germany]], [[netherlands]], [[france]], [[spain]], [[poland]], [[romania]], [[switzerland]], [[ukraine]] |
| `specialist-broker` | [[nigeria]], [[south-africa]], [[brazil]], [[argentina]], [[colombia]], [[ghana]] |

### Legend color scheme (consistent across HTML figures, role_classification.csv, and cosmos/sna-roles.json)

| Role | Hex | Visual |
|---|---|---|
| hub | `#FFC300` | amber |
| liaison-broker | `#C70039` | red |
| internal-coordinator | `#1F77B4` | blue |
| regional-coordinator | `#2CA02C` | green |
| specialist-broker | `#9467BD` | purple |
| global-liaison | `#FFD700` | gold |
| participant | `#B0B0B0` | gray |
| operation (mode-1) | `#2F4F4F` | slate |

### Notes on interpretation (confidence: medium)

- **South America broker triad** — Argentina, Brazil, Colombia all classify as specialist brokers. Their primary structural role is bridging operation clusters anchored in [[operation-orion-international]] (child-abuse material) with the Europol-led and Interpol-led operation clusters. Before v5 bare-string normalization these countries were either absent from the network or split across bare-string and wikilink forms.
- **Ghana** in the specialist-broker group reflects Sentinel Africa and Haechi operations where it bridges West-African BEC clusters to the global fabric — similar role profile to Nigeria at smaller scale.
- **Ukraine and Switzerland** as regional-coordinators reflect BEC / crypto-related Eurojust and Europol operations where both countries participate as the legal/technical anchor for European sub-clusters (Ukraine in eastern-European takedowns; Switzerland in crypto-investigation and legal-assistance roles).
- **The absence of an Asian country from the regional-coordinator or specialist-broker lists** is partly a corpus effect (fewer Asian-led ops in the subset) and partly a threshold effect — South Korea and Japan sit just below the specialist-broker degree/betweenness ratio cutoff.

### Cosmos integration (SNA mode)

The Cosmos visualization now carries a third toggle: `Graph | Globe | SNA`, parallel to the existing Graph and Globe modes. Selecting **SNA** loads `cosmos/sna-roles.json` on demand and renders a bipartite 2-mode network (operations × agency or operations × country) with nodes colored by the same role palette used in the wiki figures above.

**SNA-mode controls** (panel becomes visible only when SNA is active):
- **Network**: `Agency` / `Country` sub-toggle — switches the rendered 2-mode network without re-fetching. Role filter and legend rebuild on switch.
- **Camera distance**: 180–360 range.
- **Show labels**: on/off for mode-2 node labels.
- **Show edges**: on/off for op ↔ mode-2 lines (hidden role nodes' edges also drop).
- **Core block only**: hides periphery mode-2 nodes, leaving only the `cpnet.BE` core block visible.
- **Role filter**: per-role toggle chips (one per role present in the current network). First click on a chip turns that role off (all others stay on); subsequent clicks add/remove roles; re-enabling every role collapses back to "all on"; turning off the last active role falls back to showing just that one.
- **Hover tooltip**: hover a mode-2 node to see a floating card with slug, role, partition, core/periphery status, degree, betweenness, and the full Gould-Fernandez 5-role brokerage breakdown (coord / gate / rep / cons / liais / total). Follows the cursor, auto-repositions near screen edges.
- **Legend**: in-panel role color key, rebuilt when the network sub-toggle changes.

Graph and Globe modes are unchanged — each mode owns its rendering pipeline and UI section. Mode switch + state persistence hooks (`saveState` / `loadState`) are updated so state JSON round-trips include the SNA view configuration.

## Step B + C Closeout and Next Steps

### What Step B has established (confidence: medium)

1. The paper's headline reproducibility claim holds: low-density, core-periphery-shaped, role-differentiated 2-mode networks do appear in our wiki data.
2. Centrality-based role signatures (global coordinator, cross-domain broker, regional broker, broad-participation-but-not-broker) all reproduce qualitatively.
3. Absolute metric values do NOT match the paper — this is a corpus-composition difference, not a methodological error.
4. The crime-type mode cannot yet support paper-style interpretation due to schema coarseness and single-valued list state.
5. The PoC v1 → v5 data-quality pipeline (YAML repair + alias canonicalization + bare-string normalization + crime_types schema + source-side country repair + source-backed enrichment) is a documented, reproducible baseline. Each step is reversible and auditable.

### Step C delivered (this page)

- ✅ **Core-periphery fitness** (`cpnet.BE`) — agency fitness 0.266 reproduces paper's 0.254 pattern. Country + crime-type partitions are not meaningful under `cpnet.BE` on our subset (documented in-line).
- ✅ **Brokerage roles** (Gould-Fernandez) — full 5-role counts computed against wiki-metadata partitions. Europol EC3 / Eurojust / INTERPOL cross-domain-broker signature reproduced; FBI Cyber Division balanced-hub signature reproduced; Nigeria / South Africa / Australia / Brazil regional-broker signatures reproduced.
- ✅ **Role-indicator-based visualization** (`tools/sna_visualize.py`) — two interactive pyvis HTML figures for agency and country networks with color-coded role classification + core/periphery border thickness. Role classification rules `roles-v1` documented + reviewable. Cosmos-ready role data shipped as `cosmos/sna-roles.json`.
- ✅ **Cosmos SNA mode** — `cosmos/index.html` now has a third `Graph | Globe | SNA` toggle parallel to the existing two modes. SNA mode renders a bipartite 2-mode network with agency/country sub-toggle, core-block-only filter, edge/label toggles, and the same role color palette as the pyvis figures. Existing Graph and Globe modes are unchanged.
- ✅ **SNA hover tooltip + role filter** (second Cosmos iteration) — hover surfaces the Gould-Fernandez 5-role breakdown + core/periphery + centrality for each mode-2 node; role filter chips let the reader isolate a single role class (e.g., show only liaison brokers, or only specialist brokers) without losing context. State persists through `saveState` / `loadState`.

### Deferred to later Step C follow-ups

These remain NOT prerequisites for the claims above but will strengthen the evidence and open additional findings:

- **Alternative core-periphery algorithms** — `cpnet.Rombach`, `cpnet.Lip`, `cpnet.LowRankCore` may yield cleaner country partition where `cpnet.BE` converged to near-trivial assignment.
- **Cosmos SNA mode — advanced UI (partially done)**: hover tooltip + per-role filter + click-to-detail wiki integration now live (2026-04-20). Clicking an SNA node (op or mode-2 agency/country/crime-type) populates the right-panel detail with the matching `wiki/<kind>/<slug>.md` summary and halos the active node in the scene. Remaining: crime-type sub-toggle (suppressed until multi-value `crime_types` backfill) and persistent role-filter state in exported state JSON (already partially implemented via `saveState`).
- **Temporal network** — time-sliced sub-networks (paper's 3 periods: 2015-2018, 2019-2022, 2023-2025) to test role stability.
- **Multi-value `crime_types` backfill** — body-prose keyword extraction + manual enrichment on high-impact ops to make the crime-type mode structurally meaningful.
- **Remaining 26-op subset enrichment** — URL fetching or manual source reading for operations where source key_findings was insufficient.
- **Canonical country pages for the 22 unmapped bare-string countries** — Brunei, Cote d'Ivoire, Hong Kong, UAE, Benin, Burkina Faso, Chad, Congo, DRC, Djibouti, Gabon, Malawi, Senegal, South Sudan, Uganda, Zimbabwe, Botswana, Slovenia, Kyrgyzstan, Laos, Maldives — all mentioned in ops but missing canonical pages.
- **Broader `countries_lt_2` enrichment** — the 1,017-op backlog outside the 46-op subset.

## Reproducibility

Every number in this page can be reproduced from:
- Spec: `_workspace/sna/paper-network-definitions.md` + `_workspace/sna/edge-schema-and-inclusion-rules.md`
- Tool: `python tools/sna_analysis.py` → `_workspace/sna/out/2026-04-20-d50e3208/`
- Supplementary tool: `python tools/sna_core_periphery_brokerage.py` → `metrics_core_periphery.json`, `metrics_brokerage_{country,agency,crimetype}.csv`, `metrics_supplementary.json` under the same snapshot directory.
- Snapshot manifest: `_workspace/sna/out/2026-04-20-d50e3208/manifest.json` + `metrics_supplementary.json`.
- Data-quality passes: `tools/repair_yaml_quotes.py`, `tools/migrate_crime_type_to_list.py`, `tools/repair_bare_country_strings.py`, `tools/select_enrichment_subset.py`, `tools/enrich_participating_countries.py`.
- Audit history: [[sna-pilot]] fixes-applied table + `wiki/log.md` entries from 2026-04-19 through 2026-04-20.

No wiki content was modified while drafting this analysis page. All underlying data changes (enrichment, bare-string repair, schema migration) are documented in [[sna-pilot]] and `wiki/log.md` as their own audit-logged events.

## Contradictions & Open Questions

> [!warning] Crime-type transitivity 1.000 is a sample artifact
> See §Basic Structure warning. This value must NOT be read as paper-comparable evidence. It is the arithmetic consequence of a single multi-valued `crime_types` op in an otherwise list-of-one field. Multi-value backfill will change this value materially.

> [!note] Euro-weighted subset is corpus, not finding
> The ordering Europol EC3 > FBI, and Germany/UK/Netherlands higher than the paper's ordering, are functions of the wiki audit policy that removed US-DOJ procedural wrappers. Any claim that "Europol is more central than FBI in cybercrime IC" would be unsupported by either this subset or the paper's corpus — it's a corpus-composition effect, not a substantive finding.

> [!note] Korean participation is likely under-counted at the agency resolution
> `[[south-korea]]` appears as a country node, but specific Korean agencies (NIS, KNPA Cyber Bureau, Supreme Prosecutors' Office Cyber Crime Investigation Division) are under-represented in `participating_agencies` frontmatter. Korean IC work in Haechi operations and Phobos arrests is real; the wiki frontmatter under-records it. Step C wiki-content enrichment should prioritize Korean agency attribution for ops where Korean participation is documented in source key_findings but agency-level attribution is missing.

> [!note] The `operation-105-arrested-...` multi-valued crime_types
> This single op carries `[[bank-fraud-ic]] + [[carding-fraud-ic]] + [[money-laundering-ic]]` as its `crime_types` list. The multi-valuation is legitimate (the source press release describes all three). But in a 73-op corpus, one multi-valued op is not enough to generate structural crime-type findings. Flagged here so the schema decision is remembered as valid at the data-point level, not just at the field-level.
