---
title: Operation Low-Source Triage (2026-04-22)
type: analysis
created: 2026-04-22
updated: 2026-04-22
summary: "Repository-wide triage of operation pages below the 5-source minimum, grouped into merge, enrich, repair, and manual-review buckets."
source_count: 0
---
## Summary

This report classifies operation pages that remain below the `5`-source minimum into action buckets rather than treating every low-source page the same way.

## Bucket Counts

- merge_into_case: **0**
- merge_into_parent: **0**
- retain_and_enrich: **77**
- metadata_repair: **0**
- high_risk_review: **7**

## Bucket Meanings

- `merge_into_case`: operation page is likely a thin follow-on wrapper around an existing case page.
- `merge_into_parent`: operation page looks subordinate to a stronger parent operation and probably should not stand alone.
- `retain_and_enrich`: operation appears materially multinational or umbrella-like, but does not yet meet the source threshold.
- `metadata_repair`: `source_count` or `## References` is missing, inconsistent, or structurally broken.
- `high_risk_review`: page does not clearly qualify for retention or merger and should be reviewed manually before trust is implied.

## merge_into_case

Count: **0**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|

## merge_into_parent

Count: **0**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|

## retain_and_enrich

Count: **77**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|
| [[de-ch-crypto-mixer-takedown-2025]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[operation-jackal-iii]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[operation-source]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[rex-mundi-takedown]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[operation-bakovia]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[operation-checkmate-blacksuit]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[ramnit-botnet-takedown]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[operation-12-members-of-an-irish-high-risk-criminal-network-arrested]] | 1 | 1 | follow-on | 5 | multinational_but_thin |
| [[operation-goldfish-alpha-night-fury]] | 1 | 1 | umbrella | 7 | multinational_umbrella |
| [[operation-haechi-iv]] | 1 | 1 | umbrella | 8 | multinational_umbrella |
| [[operation-pleiades]] | 1 | 1 | umbrella | 10 | multinational_umbrella |
| [[operation-killer-bee]] | 1 | 1 | umbrella | 11 | multinational_umbrella |
| [[operation-endgame-phase1]] | 1 | 1 | umbrella | 13 | multinational_umbrella |
| [[2bagoldmule-qqaazz]] | 1 | 1 | umbrella | 16 | multinational_umbrella |
| [[operation-serengeti]] | 1 | 1 | umbrella | 19 | multinational_umbrella |
| [[operation-jackal]] | 1 | 1 | umbrella | 21 | multinational_umbrella |
| [[operation-haechi-vi]] | 1 | 1 | umbrella | 32 | multinational_umbrella |
| [[global-airport-action-day]] | 2 | 2 | umbrella | 2 | multinational_umbrella |
| [[operation-destabilise]] | 2 | 2 | umbrella | 2 | multinational_umbrella |
| [[operation-haechi-v]] | 2 | 2 | umbrella | 2 | multinational_umbrella |
| [[operation-nervone]] | 2 | 2 | umbrella | 2 | multinational_umbrella |
| [[operation-nightfury]] | 2 | 2 | umbrella | 2 | multinational_umbrella |
| [[operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america]] | 2 | 2 | follow-on | 2 | multinational_but_thin |
| [[zambia-golden-top-call-center]] | 2 | 2 | umbrella | 2 | multinational_umbrella |
| [[operation-germany-romania-trusted-seller-fraud-2025]] | 2 | 2 | umbrella | 3 | multinational_umbrella |
| [[zeus-spyeye-jit-takedown]] | 2 | 2 | umbrella | 3 | multinational_umbrella |
| [[operation-contender-2]] | 2 | 2 | umbrella | 4 | multinational_umbrella |
| [[operation-eur-100m-illegal-financial-service-laundering-2025]] | 2 | 2 | umbrella | 4 | multinational_umbrella |
| [[operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | 2 | 2 | follow-on | 4 | multinational_but_thin |
| [[proxy-service-takedown-2026-03]] | 2 | 2 | umbrella | 4 | multinational_umbrella |
| [[operation-eur-600m-crypto-scam-network-2025]] | 2 | 2 | umbrella | 5 | multinational_umbrella |
| [[operation-secreto]] | 2 | 2 | umbrella | 5 | multinational_umbrella |
| [[operation-synergia-ii]] | 2 | 2 | umbrella | 5 | multinational_umbrella |
| [[black-axe-bec-2021]] | 2 | 2 | umbrella | 6 | multinational_umbrella |
| [[cyber-fraud-international-2015]] | 2 | 2 | umbrella | 6 | multinational_umbrella |
| [[operation-eur-100m-crypto-investment-fraud-2025]] | 2 | 2 | umbrella | 6 | multinational_umbrella |
| [[operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto]] | 2 | 2 | follow-on | 6 | multinational_but_thin |
| [[operation-secure-interpol]] | 2 | 2 | umbrella | 6 | multinational_umbrella |
| [[operation-trojan-shield]] | 2 | 2 | umbrella | 6 | multinational_umbrella |
| [[operation-eur-3m-online-investment-fraud-2025]] | 2 | 2 | umbrella | 7 | multinational_umbrella |
| ... | ... | ... | ... | ... | 37 more |

## metadata_repair

Count: **0**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|

## high_risk_review

Count: **7**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|
| [[banking-trojan-fraud-sentencing-2017]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[operation-hyperion]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[operation-lyrebird]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[operation-delilah]] | 2 | 2 | umbrella | 0 | single_country_low_source |
| [[romania-phishing-takedown-2024]] | 2 | 2 | umbrella | 1 | single_country_low_source |
| [[zeus-spyeye-takedown]] | 2 | 2 | umbrella | 1 | single_country_low_source |
| [[operation-falcon]] | 4 | 4 | umbrella | 1 | single_country_low_source |

## Recommended First Batch

1. Merge obvious `operation-us-v-*` and single-country follow-on pages into case records.
2. Repair metadata mismatches before making trust judgments on pages that already claim higher source density.
3. Preserve genuinely multinational umbrella operations and enrich them toward the 5-source floor.
4. Review the remaining high-risk single-source pages one family at a time rather than one page at a time.
