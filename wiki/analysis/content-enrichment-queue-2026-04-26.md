---
title: Content Enrichment Queue (2026-04-26)
type: analysis
created: 2026-04-26
updated: 2026-04-26
summary: "Prioritized queue for enriching source-rich, thin, placeholder, or duplicate-reference operation and case pages."
source_count: 0
---
## Summary

This queue converts the content-depth audit into an execution list. It is ordered to fix pages where existing sources already contain enough material before searching for new sources.

- Audited operation/case pages: **2287**
- Queue size: **0**

## Top Queue

| Rank | Page | Type | Score | Sources | Body words | Source words | Recommendation | Issues |
|---:|---|---|---:|---:|---:|---:|---|---|

## Execution Rules

1. Fix `duplicate_source_url_refs` before counting a page as source-rich.
2. For `enrich_from_existing_raw_sources`, use already collected raw/source text first.
3. For `replace_placeholder_or_absorb_wrapper`, decide whether the page is a real case/operation or a wrapper that should point to a canonical record.
4. For `manual_crime_type_review`, do not change taxonomy without source-backed review.
