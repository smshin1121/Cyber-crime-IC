---
type: analysis
title: "SNA Rebuild: 2014-2025 Five Cybercrime Categories"
analysis_type: dataset-rebuild
scope: "Operation-country, operation-agency, and operation-crime_type two-mode networks filtered to 2014-2025 and five target crime categories."
confidence: medium
created: 2026-05-05
updated: 2026-05-05
---

## Summary

This rebuild uses `_workspace/sna/current/manifest.json` as the current SNA manifest. It includes **83** operations from **2014-2025** whose operation frontmatter has at least one source URL, participating agencies, participating countries, and at least one of the six target crime categories.

The six-category crime filter is intentionally narrower than the older PoC SNA output. Crime-type edges are collapsed to `ransomware-ic`, `dark-web-ic`, `csam-ic`, `malware-ic`, `illegal-iptv-ic`, and `voice-phishing-ic`; other wiki crime categories are not exported into this subset.

## Output Manifest

| Artifact | Value |
|---|---:|
| Operations | 83 |
| Countries | 118 |
| Agencies | 102 |
| Crime types | 6 |
| Operation-country edges | 647 |
| Operation-agency edges | 416 |
| Operation-crime_type edges | 111 |

## Crime-Type Coverage

| Crime type | Included operations |
|---|---:|
| [[ransomware-ic]] | 29 |
| [[dark-web-ic]] | 15 |
| [[csam-ic]] | 6 |
| [[malware-ic]] | 44 |
| [[illegal-iptv-ic]] | 5 |
| [[voice-phishing-ic]] | 12 |

## Centrality Snapshots

### Countries

| Country | Degree |
|---|---:|
| [[united-states]] | 0.675 |
| [[germany]] | 0.470 |
| [[united-kingdom]] | 0.470 |
| [[netherlands]] | 0.398 |
| [[france]] | 0.301 |
| [[australia]] | 0.241 |
| [[canada]] | 0.217 |
| [[romania]] | 0.205 |
| [[spain]] | 0.205 |
| [[sweden]] | 0.181 |

### Agencies

| Agency | Degree |
|---|---:|
| [[europol-ec3]] | 0.566 |
| [[fbi-cyber-division]] | 0.398 |
| [[eurojust]] | 0.325 |
| [[netherlands-politie]] | 0.217 |
| [[germany-bka]] | 0.205 |
| [[uk-nca]] | 0.205 |
| [[us-doj]] | 0.193 |
| [[interpol]] | 0.169 |
| [[fbi]] | 0.157 |
| [[interpol-igci]] | 0.120 |

### Crime Types

| Crime type | Degree |
|---|---:|
| [[malware-ic]] | 0.530 |
| [[ransomware-ic]] | 0.349 |
| [[dark-web-ic]] | 0.181 |
| [[voice-phishing-ic]] | 0.145 |
| [[csam-ic]] | 0.072 |
| [[illegal-iptv-ic]] | 0.060 |

## Cohesion

| Network | Nodes | Edges | Density | Components | Largest component |
|---|---:|---:|---:|---:|---:|
| country | 201 | 647 | 0.0661 | 2 | 199 |
| agency | 185 | 416 | 0.0491 | 2 | 182 |
| crime_type | 89 | 111 | 0.2229 | 2 | 83 |

## Visualizations

- [Country network](sna/country-network.html)
- [Agency network](sna/agency-network.html)
- [Crime-type network](sna/crime-type-network.html)

## Validation Notes

- Out-of-range included operations: 0
- Included operations outside the target crime set: 0
- Included operations without source URLs: 0
- Included operations missing required agency/country/crime fields: 0

The source workbook cross-check reports are under `_workspace/imports/data_sample/` and are treated as review evidence, not as an automatic overwrite of wiki operation frontmatter.
