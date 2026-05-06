---
type: analysis
title: "Non-IC Public Wiki Exclusion Audit (2026-05-06)"
title_ko: "비국제공조 공개 위키 제외 감사"
analysis_type: scope-audit
scope: "Apply the public wiki rule that international cooperation requires at least two real country slugs."
confidence: medium
created: 2026-05-06
updated: 2026-05-07
---

## Summary

The public wiki now applies a stricter international-cooperation threshold: a record must have at least two real country slugs to be treated as international cooperation. Pseudo-geographic placeholders such as `international`, `global`, `worldwide`, and `european-union` do not count as countries.

The rule now applies to public discovery and direct public rendering. Existing markdown files remain in the repository so old backlinks and source traceability are not destroyed, but non-qualifying records are excluded from public category indexes, search index, statistics, Cosmos graph export, direct Flask routes, and generated static HTML.

## Public Inclusion Rule

| Page type | Public inclusion rule |
|---|---|
| Operations | `participating_countries` / `jurisdictions` must contain at least two real `wiki/countries` slugs. |
| Cases | Direct country count must be at least two, or the case must link to a qualifying operation. |
| Sources | Source must be referenced by a qualifying operation or qualifying case. |
| Other wiki categories | Retained, because they are reference entities, mechanisms, crime types, country profiles, organizations, or analysis pages rather than event records. |

## Current Public-Scope Counts

| Category | Total files | Public after rule | Excluded from public index |
|---|---:|---:|---:|
| Operations | 1,100 | 148 | 952 |
| Cases | 1,202 | 89 | 1,113 |
| Sources | 4,819 | 633 | 4,186 |

Operation scope detail:

| Operation scope | Public after rule | Excluded from public index |
|---|---:|---:|
| Canonical operations | 121 | 5 |
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
- `web/app.py`, `web/build_static.py`, `tools/sync_stats.py`, and `cosmos/extract.py` apply the same public visibility filter to category pages, direct wiki routes, generated HTML, search, statistics, and graph data.
- `tools/audit_public_ic_scope.py` verifies that category indexes, static HTML, search index, and Cosmos graph expose only qualifying public operations, cases, and sources.
- Wikilinks to non-qualifying trace pages render as plain text in public HTML, so the public site does not create broken internal links to excluded pages.
- Individual legacy pages are no longer generated as public static HTML unless they satisfy the two-country rule.

## Current Audit Result

As of the 2026-05-07 scope check, the public operation set contains **148** records and **0** records with fewer than two real country slugs. The same expected public sets are reflected in `wiki/*/_index.md`, `docs/wiki/*/*.html`, `docs/search-index.json`, and `cosmos/data.json` for operations, cases, and sources.

## Residual Work

- Review the five excluded canonical operations for missing second-country evidence. If a reliable source supports at least two participating countries, update structured metadata and rerun the build.
- Decide later whether to physically move non-qualifying trace pages out of `wiki/` after backlink and source-dependency risks are fully resolved.
