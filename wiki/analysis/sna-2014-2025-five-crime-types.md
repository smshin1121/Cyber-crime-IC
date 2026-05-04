---
type: analysis
title: "SNA Rebuild: 2014-2025 Five Cybercrime Categories"
analysis_type: dataset-rebuild
scope: "Operation-country, operation-agency, and operation-crime_type two-mode networks filtered to 2014-2025 and five target crime categories."
confidence: medium
created: 2026-05-04
updated: 2026-05-04
---

## Summary

This rebuild uses `_workspace/sna/current/manifest.json` as the current SNA manifest. It includes **68** operations from **2014-2025** whose operation frontmatter has at least one source URL, participating agencies, participating countries, and at least one of the five target crime categories.

The five-category crime filter is intentionally narrower than the older PoC SNA output. Crime-type edges are collapsed to `ransomware-ic`, `dark-web-ic`, `csam-ic`, `malware-ic`, and `illegal-iptv-ic`; other wiki crime categories are not exported into this subset.

## Output Manifest

| Artifact | Value |
|---|---:|
| Operations | 68 |
| Countries | 108 |
| Agencies | 94 |
| Crime types | 5 |
| Operation-country edges | 531 |
| Operation-agency edges | 372 |
| Operation-crime_type edges | 95 |

## Crime-Type Coverage

| Crime type | Included operations |
|---|---:|
| [[ransomware-ic]] | 29 |
| [[dark-web-ic]] | 15 |
| [[csam-ic]] | 6 |
| [[malware-ic]] | 44 |
| [[illegal-iptv-ic]] | 1 |

## Centrality Snapshots

### Countries

| Country | Degree |
|---|---:|
| [[united-states]] | 0.750 |
| [[germany]] | 0.515 |
| [[united-kingdom]] | 0.515 |
| [[netherlands]] | 0.441 |
| [[france]] | 0.324 |
| [[australia]] | 0.250 |
| [[canada]] | 0.250 |
| [[romania]] | 0.206 |
| [[switzerland]] | 0.206 |
| [[spain]] | 0.176 |

### Agencies

| Agency | Degree |
|---|---:|
| [[europol-ec3]] | 0.632 |
| [[fbi-cyber-division]] | 0.471 |
| [[eurojust]] | 0.338 |
| [[germany-bka]] | 0.250 |
| [[netherlands-politie]] | 0.250 |
| [[uk-nca]] | 0.250 |
| [[us-doj]] | 0.221 |
| [[fbi]] | 0.191 |
| [[interpol]] | 0.162 |
| [[us-secret-service]] | 0.118 |

### Crime Types

| Crime type | Degree |
|---|---:|
| [[malware-ic]] | 0.647 |
| [[ransomware-ic]] | 0.426 |
| [[dark-web-ic]] | 0.221 |
| [[csam-ic]] | 0.088 |
| [[illegal-iptv-ic]] | 0.015 |

## Cohesion

| Network | Nodes | Edges | Density | Components | Largest component |
|---|---:|---:|---:|---:|---:|
| country | 176 | 531 | 0.0723 | 2 | 174 |
| agency | 162 | 372 | 0.0582 | 1 | 162 |
| crime_type | 73 | 95 | 0.2794 | 2 | 71 |

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
