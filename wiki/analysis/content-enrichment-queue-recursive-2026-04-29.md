---
title: Content Enrichment Queue (2026-04-26)
type: analysis
created: 2026-04-26
updated: 2026-04-26
summary: "Queue for enriching operation and case pages from existing source records."
source_count: 0
---
## Summary

This queue converts the content-depth audit into an execution list. It is ordered to fix pages where existing sources already contain enough material before searching for new sources.

- Selection mode: **priority audit findings**
- Audited operation/case pages: **2287**
- Queue size: **10**

## Top Queue

| Rank | Page | Type | Score | Sources | Body words | Source words | Recommendation | Issues |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | [[australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace]] | case | 34 | 5 | 447 | 9051 | enrich_from_existing_raw_sources | raw_available_underused:9051w_sources, high_source_to_body_gap |
| 2 | [[bremerton-washington-man-sentenced-to-3-years-in-prison-for-extensive-swatting-campaign-targeting-victims-in-u]] | case | 22 | 5 | 427 | 2136 | enrich_from_existing_raw_sources | raw_available_underused:2136w_sources |
| 3 | [[founder-and-majority-owner-of-bitzlato-a-cryptocurrency-exchange-charged-with-unlicensed-money-transmitting]] | case | 22 | 1 | 410 | 1889 | enrich_from_existing_raw_sources | raw_available_underused:1889w_sources |
| 4 | [[dark-web-vendor-of-illegal-narcotics-indicted-for-distributing-heroin-and-cocaine-in-exchange-for-bitcoin]] | case | 22 | 1 | 389 | 1525 | enrich_from_existing_raw_sources | raw_available_underused:1525w_sources |
| 5 | [[5-charged-in-2-8-million-dark-web-drug-trafficking-money-laundering-conspiracy]] | case | 22 | 1 | 431 | 1386 | enrich_from_existing_raw_sources | raw_available_underused:1386w_sources |
| 6 | [[former-hedge-fund-manager-convicted-of-wire-fraud-money-laundering-and-contempt-of-court]] | case | 22 | 1 | 215 | 1276 | enrich_from_existing_raw_sources | raw_available_underused:1276w_sources |
| 7 | [[bugat-botnet-administrator-arrested-and-malware-disabled]] | case | 22 | 1 | 440 | 1264 | enrich_from_existing_raw_sources | raw_available_underused:1264w_sources |
| 8 | [[four-members-of-notorious-cybercrime-group-fin9-charged-for-roles-in-attacking-u-s-companies]] | case | 22 | 1 | 428 | 1258 | enrich_from_existing_raw_sources | raw_available_underused:1258w_sources |
| 9 | [[citizen-of-croatia-and-serbia-charged-with-running-monopoly-drug-market-on-the-darknet]] | case | 22 | 1 | 418 | 1253 | enrich_from_existing_raw_sources | raw_available_underused:1253w_sources |
| 10 | [[4-arrested-in-latest-l-a-county-based-jcode-operation-for-allegedly-operating-a-drug-distribution-network-on-t]] | case | 22 | 1 | 446 | 1248 | enrich_from_existing_raw_sources | raw_available_underused:1248w_sources |

## Execution Rules

1. Fix `duplicate_source_url_refs` before counting a page as source-rich.
2. For `enrich_from_existing_raw_sources`, use already collected raw/source text first.
3. For `replace_placeholder_or_absorb_wrapper`, decide whether the page is a real case/operation or a wrapper that should point to a canonical record.
4. For `manual_crime_type_review`, do not change taxonomy without source-backed review.
