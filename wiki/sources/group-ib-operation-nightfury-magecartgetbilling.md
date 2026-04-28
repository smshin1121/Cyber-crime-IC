---
type: source
title: "Group-IB: Night Fury — INTERPOL-coordinated arrest of Magecart/GetBilling operators"
collection_url: https://www.group-ib.com/media-center/press-releases/night-fury/
collection_domain: group-ib.com
source_type: news
publisher: Group-IB
publish_date: 2020-01-24
ingest_date: 2026-04-08
enriched_date: 2026-04-10
language: en
reliability: medium
credibility: possibly-true
sensitivity: public
source_tier: 3
pages_updated:
  - operation-nightfury
key_findings:
  - "On 24 January 2020, INTERPOL's ASEAN Cybercrime Operations Desk announced the results of Operation Night Fury, which resulted in the arrest of 3 Indonesian nationals involved in a Magecart-style JavaScript web skimming operation known as 'GetBilling'"
  - "Private-sector origin: The operation was driven by intelligence provided by Singapore-based cybersecurity firm Group-IB, which had been tracking GetBilling since 2018 and had identified infrastructure linking the group to hundreds of compromised e-commerce sites worldwide"
  - "Technical profile: GetBilling deployed obfuscated JavaScript skimmers that were injected into e-commerce payment checkout pages to exfiltrate customer payment card data, shipping details and personal information — the hallmark Magecart pattern"
  - "Scope of compromise: Group-IB's report describes that GetBilling had compromised 'hundreds' of online stores across multiple countries, though no specific country list was published beyond confirmation that victims spanned Asia-Pacific, Europe and North America"
  - "Operation Night Fury was also folded into INTERPOL's broader ASEAN 'Operation Goldfish Alpha/Night Fury' reporting, presenting the arrests as part of a regional cyberthreat response rather than a standalone named action"
  - "Historical significance: This was one of the first publicly announced arrests of Magecart operators anywhere in the world — the broader Magecart umbrella (estimated 20+ distinct groups) had been tracked by security researchers since 2015 without successful takedowns until this Indonesia action"
created: 2026-04-08
updated: 2026-04-10
duplicate_of: "[[2020-01-27_group-ib_night-fury]]"
duplicate_reason: same_collection_url
duplicate_key: https://www.group-ib.com/media-center/press-releases/night-fury/
duplicate_normalized_at: 2026-04-26
raw_path: raw/news/group-ib-operation-nightfury-magecartgetbilling.md
text_status: summarized
storage_mode: summary-only
content_hash: sha256:8c3e92ee6c561d32143b289666b377ad47ebc7e440eae1418da0dff5a366e5f0
word_count: 394
extraction_date: 2026-04-27
copyright_policy: summary-only
---
## Source

- **Publisher**: Group-IB (Singapore-based cybersecurity firm, Russian-origin, private sector)
- **URL**: <https://www.group-ib.com/media-center/press-releases/night-fury/>
- **Published**: 2020-01-24
- **Source Tier**: 3 (industry vendor press release / threat intelligence)
- **Reliability**: medium (vendor with commercial interest in attribution; high technical credibility but marketing incentive must be noted)
- **Credibility**: possibly-true (primary technical claims corroborated by INTERPOL; vendor-framed narrative)
- **Operations referenced**: [[operation-nightfury|Operation NightFury (Magecart/GetBilling)]]

## Summary

Group-IB's press release describes its role in **Operation Night Fury**, an INTERPOL-coordinated action that resulted in the **24 January 2020** arrest of 3 Indonesian nationals operating the 'GetBilling' Magecart-style web skimming group. Key points:

1. **Arrest**: 3 Indonesian nationals, coordinated by INTERPOL with Indonesian Police and Singapore Police Force cooperation
2. **Private-sector role**: Group-IB provided long-term threat intelligence that identified the infrastructure and operators — an important example of formal private-sector integration into INTERPOL takedowns
3. **Technical method**: Obfuscated JavaScript skimmers injected into e-commerce payment pages (Magecart-style)
4. **Tracking duration**: Group-IB claims to have tracked GetBilling since at least 2018, a ~2-year intelligence-gathering effort before arrest
5. **First Magecart arrests**: This operation is widely cited as one of the first known Magecart-operator arrests globally

## Why this source matters

For the IC analysis on [[operation-nightfury]] this Group-IB release is important despite its Tier 3 rating because:

- **It is the primary published source for technical attribution of GetBilling to the three Indonesian nationals** — INTERPOL's own statement is sparse on technical detail
- **It documents a novel private-sector-to-law-enforcement intelligence pipeline** involving Group-IB → INTERPOL → Indonesian Police → Singapore Police Force
- **It sets a precedent for Magecart takedowns** that would influence later actions
- **Vendor framing caveat**: Group-IB has a commercial interest in publicizing its role in takedowns; all numeric claims should be cross-checked against INTERPOL's independent statement

> [!note] Reliability qualifier
> Group-IB is a for-profit cybersecurity vendor with a marketing incentive to be associated with high-profile takedowns. While its technical reporting has historically been accurate, independent corroboration from INTERPOL is required before treating specific figures as *confirmed*.

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| INTERPOL ASEAN press release 2020-02-17 | 3 Indonesian arrests, regional operation framing |
| CyberScoop 2020-01-24 | Group-IB intelligence role, INTERPOL coordination |
| PortSwigger Daily Swig 2020-01-25 | Magecart-style skimming attribution |

Source diversity is *low-medium* — multiple Tier 3 sources but all ultimately trace to Group-IB's threat intelligence. INTERPOL is the only fully independent Tier 2 corroboration.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Night Fury | Group-IB | 2020-01-24 | https://www.group-ib.com/media-center/press-releases/night-fury/ |
| [2] | INTERPOL report highlights key cyberthreats in Southeast Asia | INTERPOL | 2020-02-17 | https://www.interpol.int/News-and-Events/News/2020/INTERPOL-report-highlights-key-cyberthreats-in-Southeast-Asia |
| [3] | Magecart arrest Indonesia INTERPOL GetBilling | CyberScoop | 2020-01-24 | https://cyberscoop.com/magecart-arrest-indonesia-interpol-getbilling/ |
| [4] | Police arrest three Magecart cybercrime suspects in Indonesia | PortSwigger Daily Swig | 2020-01-25 | https://portswigger.net/daily-swig/police-arrest-three-magecart-cybercrime-suspects-in-indonesia |
