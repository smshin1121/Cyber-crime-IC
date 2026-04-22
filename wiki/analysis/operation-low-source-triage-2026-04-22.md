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
- retain_and_enrich: **81**
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

Count: **81**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|
| [[bec-nigeria-2016]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[de-ch-crypto-mixer-takedown-2025]] | 1 | 0 | umbrella | 2 | source_count_mismatch:1!=0, missing_visible_references, multinational_umbrella |
| [[global-airport-action-day]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[isoon-apt27-indictment]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[korea-cambodia-scam-repatriation]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[korea-china-voice-phishing-qingdao]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[marketplace-a-dekhtyarchuk-indictment]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[operation-de-fr-online-fraud-group-2026]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[operation-destabilise]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[operation-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | 1 | 1 | follow-on | 2 | multinational_but_thin |
| [[operation-haechi-v]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[operation-nervone]] | 1 | 1 | umbrella | 2 | multinational_umbrella |
| [[operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america]] | 1 | 1 | follow-on | 2 | multinational_but_thin |
| [[operation-first-light-2024]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[operation-germany-romania-trusted-seller-fraud-2025]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[operation-jackal-iii]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown]] | 1 | 1 | follow-on | 3 | multinational_but_thin |
| [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-3]] | 1 | 1 | follow-on | 3 | multinational_but_thin |
| [[operation-source]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[rex-mundi-takedown]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[xdedic-marketplace-takedown]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[zeus-spyeye-jit-takedown]] | 1 | 1 | umbrella | 3 | multinational_umbrella |
| [[operation-bakovia]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[operation-checkmate-blacksuit]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[operation-eur-100m-illegal-financial-service-laundering-2025]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | 1 | 1 | follow-on | 4 | multinational_but_thin |
| [[proxy-service-takedown-2026-03]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[ramnit-botnet-takedown]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[rydox-marketplace-takedown]] | 1 | 1 | umbrella | 4 | multinational_umbrella |
| [[fake-shopping-sites-takedown-2024]] | 1 | 1 | umbrella | 5 | multinational_umbrella |
| [[operation-12-members-of-an-irish-high-risk-criminal-network-arrested]] | 1 | 1 | follow-on | 5 | multinational_but_thin |
| [[operation-eur-600m-crypto-scam-network-2025]] | 1 | 1 | umbrella | 5 | multinational_umbrella |
| [[operation-secreto]] | 1 | 1 | umbrella | 5 | multinational_umbrella |
| [[operation-synergia-ii]] | 1 | 1 | umbrella | 5 | multinational_umbrella |
| [[operation-wirewire]] | 1 | 1 | umbrella | 5 | multinational_umbrella |
| [[black-axe-bec-2021]] | 1 | 1 | umbrella | 6 | multinational_umbrella |
| [[cyber-fraud-international-2015]] | 1 | 1 | umbrella | 6 | multinational_umbrella |
| [[darkode-takedown]] | 1 | 1 | umbrella | 6 | multinational_umbrella |
| [[franco-israeli-ceo-fraud]] | 1 | 1 | umbrella | 6 | multinational_umbrella |
| [[operation-eur-100m-crypto-investment-fraud-2025]] | 1 | 1 | umbrella | 6 | multinational_umbrella |
| ... | ... | ... | ... | ... | 41 more |

## metadata_repair

Count: **0**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|

## high_risk_review

Count: **7**

| Operation | Sources | Refs | Role | Countries | Notes |
|---|---:|---:|---|---:|---|
| [[operation-lyrebird]] | 1 | 1 | umbrella | 0 | single_country_low_source |
| [[banking-trojan-fraud-sentencing-2017]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[operation-hyperion]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[romania-phishing-takedown-2024]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[zeus-spyeye-takedown]] | 1 | 1 | umbrella | 1 | single_country_low_source |
| [[operation-delilah]] | 2 | 2 | umbrella | 0 | single_country_low_source |
| [[operation-falcon]] | 4 | 4 | umbrella | 1 | single_country_low_source |

## Recommended First Batch

1. Merge obvious `operation-us-v-*` and single-country follow-on pages into case records.
2. Repair metadata mismatches before making trust judgments on pages that already claim higher source density.
3. Preserve genuinely multinational umbrella operations and enrich them toward the 5-source floor.
4. Review the remaining high-risk single-source pages one family at a time rather than one page at a time.
