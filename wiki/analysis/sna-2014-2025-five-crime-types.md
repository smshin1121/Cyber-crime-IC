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

This rebuild uses `_workspace/sna/current/manifest.json` as the current SNA manifest. It includes **72** operations from **2014-2025** whose operation frontmatter has at least one source URL, participating agencies, participating countries, and at least one of the five target crime categories.

The five-category crime filter is intentionally narrower than the older PoC SNA output. Crime-type edges are collapsed to `ransomware-ic`, `dark-web-ic`, `csam-ic`, `malware-ic`, and `illegal-iptv-ic`; other wiki crime categories are not exported into this subset.

## Output Manifest

| Artifact | Value |
|---|---:|
| Operations | 72 |
| Countries | 110 |
| Agencies | 97 |
| Crime types | 5 |
| Operation-country edges | 560 |
| Operation-agency edges | 386 |
| Operation-crime_type edges | 99 |

## Crime-Type Coverage

| Crime type | Included operations |
|---|---:|
| [[ransomware-ic]] | 29 |
| [[dark-web-ic]] | 15 |
| [[csam-ic]] | 6 |
| [[malware-ic]] | 44 |
| [[illegal-iptv-ic]] | 5 |

## Centrality Snapshots

### Countries

| Country | Degree |
|---|---:|
| [[united-states]] | 0.722 |
| [[germany]] | 0.514 |
| [[united-kingdom]] | 0.500 |
| [[netherlands]] | 0.444 |
| [[france]] | 0.333 |
| [[australia]] | 0.236 |
| [[canada]] | 0.236 |
| [[romania]] | 0.208 |
| [[spain]] | 0.194 |
| [[switzerland]] | 0.194 |

### Agencies

| Agency | Degree |
|---|---:|
| [[europol-ec3]] | 0.625 |
| [[fbi-cyber-division]] | 0.444 |
| [[eurojust]] | 0.361 |
| [[germany-bka]] | 0.236 |
| [[netherlands-politie]] | 0.236 |
| [[uk-nca]] | 0.236 |
| [[us-doj]] | 0.222 |
| [[fbi]] | 0.181 |
| [[interpol]] | 0.153 |
| [[us-secret-service]] | 0.111 |

### Crime Types

| Crime type | Degree |
|---|---:|
| [[malware-ic]] | 0.611 |
| [[ransomware-ic]] | 0.403 |
| [[dark-web-ic]] | 0.208 |
| [[csam-ic]] | 0.083 |
| [[illegal-iptv-ic]] | 0.069 |

## Cohesion

| Network | Nodes | Edges | Density | Components | Largest component |
|---|---:|---:|---:|---:|---:|
| country | 182 | 560 | 0.0707 | 2 | 180 |
| agency | 169 | 386 | 0.0553 | 1 | 169 |
| crime_type | 77 | 99 | 0.2750 | 2 | 71 |

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
