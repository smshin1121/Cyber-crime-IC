---
type: analysis
title: "Non-IC Public Wiki Exclusion Audit (2026-05-06)"
title_ko: "비국제공조 공개 위키 제외 감사"
analysis_type: scope-audit
scope: "Apply the public wiki rule that international cooperation requires at least two real country slugs."
confidence: medium
created: 2026-05-06
updated: 2026-05-06
---

## Summary

The public wiki now applies a stricter international-cooperation threshold: a record must have at least two real country slugs to be treated as international cooperation. Pseudo-geographic placeholders such as `international`, `global`, `worldwide`, and `european-union` do not count as countries.

The first application of the rule changes public discovery surfaces, not the underlying trace archive. Existing markdown files remain in the repository so old backlinks and source traceability are not destroyed, but non-qualifying records are excluded from public category indexes, search index, statistics, and Cosmos graph export.

## Public Inclusion Rule

| Page type | Public inclusion rule |
|---|---|
| Operations | `participating_countries` / `jurisdictions` must contain at least two real `wiki/countries` slugs. |
| Cases | Direct country count must be at least two, or the case must link to a qualifying operation. |
| Sources | Source must be referenced by a qualifying operation or qualifying case. |
| Other wiki categories | Retained, because they are reference entities, mechanisms, crime types, country profiles, organizations, or analysis pages rather than event records. |

## First-Pass Counts

| Category | Total files | Public after rule | Excluded from public index |
|---|---:|---:|---:|
| Operations | 1,093 | 141 | 952 |
| Cases | 1,202 | 89 | 1,113 |
| Sources | 4,797 | 605 | 4,192 |

Operation scope detail:

| Operation scope | Public after rule | Excluded from public index |
|---|---:|---:|
| Canonical operations | 114 | 5 |
| Absorbed follow-on records | 27 | 947 |

## Canonical Operations Excluded

These five records were previously canonical but have only one real country slug in structured metadata:

| Operation | Country count | Recorded country | Reason |
|---|---:|---|---|
| [[bali-villa-cybercrime-raid-2024]] | 1 | Indonesia | Domestic immigration enforcement; foreign-victim context alone is not enough under the two-country rule. |
| [[operation-falcon]] | 1 | Nigeria | INTERPOL/private support appears, but structured country participation records only Nigeria. |
| [[operation-hyperion]] | 1 | United States | Public action was U.S.-anchored in current metadata. |
| [[operation-lyrebird]] | 1 | Morocco | Current metadata records only Morocco. |
| [[romania-phishing-takedown-2024]] | 1 | Romania | Current metadata records only Romania. |

## Implementation Notes

- `tools/ic_scope.py` centralizes the two-country rule.
- `tools/reconcile_indexes.py` excludes non-qualifying operations, cases, and sources from `_index.md` tables.
- `web/app.py`, `web/build_static.py`, `tools/sync_stats.py`, and `cosmos/extract.py` apply the same public visibility filter to category pages, search, statistics, and graph data.
- Individual legacy pages are still generated for link stability, but they are no longer part of public discovery counts unless they satisfy the two-country rule.

## Residual Work

- Review the five excluded canonical operations for missing second-country evidence. If a reliable source supports at least two participating countries, update structured metadata and rerun the build.
- Decide later whether to physically move non-qualifying trace pages out of `wiki/` after backlink and source-dependency risks are fully resolved.
