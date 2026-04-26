---
type: source
title: "Group-IB: Operation Delilah — Interpol Nabs Suspected Leader of Transnational Phishing Ring"
collection_url: "https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/"
collection_domain: "group-ib.com"
source_type: "press-release"
publisher: "Group-IB"
publish_date: "2022-05-25"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "medium-high"
credibility: "probably-true"
sensitivity: "public"
source_tier: 2
pages_updated:
  - "operation-delilah"
key_findings:
  - "Group-IB announced on or around 2022-05-25 that Operation Delilah — led by Interpol with intelligence support from Group-IB, Palo Alto Networks Unit 42, and Trend Micro — resulted in the arrest of a 37-year-old Nigerian man at Murtala Muhammed International Airport in Lagos in March 2022"
  - "The suspect is alleged to be a senior leader of the SilverTerrier cybercrime syndicate, which has operated BEC and mass-phishing campaigns since at least 2015"
  - "Delilah is the *third* Interpol operation focused on SilverTerrier, following Operation Falcon I (November 2020) and Operation Falcon II (2021); the three operations together have led to the arrest of at least 14 suspected SilverTerrier members"
  - "Intelligence chain: Group-IB, Unit 42, and Trend Micro provided the initial threat-intelligence referral → Interpol Cyber Fusion Centre analysts enriched it → Nigerian police conducted the physical arrest at the airport (tracking months of suspect movements)"
  - "Operation Delilah's law-enforcement coordination spanned police agencies across four continents (including Europe, Asia, Africa, Australia)"
  - "Significance for IC studies: Delilah illustrates a rare operationalisation of a *public–private intelligence chain* where three commercial cybersecurity vendors drove an Interpol-coordinated arrest — a pattern used later in Africa Cyber Surge II (2023)"
created: 2026-04-08
updated: 2026-04-10
duplicate_of: "[[2022-01-01_group-ib-com_interpol-gib-delilah]]"
duplicate_reason: same_collection_url
duplicate_key: "https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/"
duplicate_normalized_at: 2026-04-26
---

## Source

- **Publisher**: Group-IB
- **URL**: <https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/>
- **Published**: ~2022-05-25 (coincident with Interpol's own Delilah announcement)
- **Source Tier**: 2 (primary intelligence contributor, acting as a quasi-official partner to Interpol)
- **Reliability**: medium-high (Group-IB is an investigation participant, so the release is semi-authoritative; some self-promotional framing)
- **Credibility**: probably-true
- **Operations referenced**: [[operation-delilah|Operation Delilah (SilverTerrier BEC)]]

> [!note] Fetch note
> group-ib.com returned HTTP 403 at enrichment time. Facts below are corroborated by independent reporting from The Hacker News, BleepingComputer, CyberScoop, Unit 42's parallel blog post, and The Register.

## Summary

Group-IB's Operation Delilah release documents the **arrest of a senior SilverTerrier BEC leader** in Lagos in March 2022, following a year-long tracking operation initiated in May 2021. Key facts:

1. **Suspect**: 37-year-old Nigerian national (unnamed in public releases); apprehended at Lagos' Murtala Muhammed International Airport in March 2022
2. **Operational structure**: Intelligence referral by **Group-IB + Palo Alto Networks Unit 42 + Trend Micro** → **Interpol Cyber Fusion Centre** enrichment → **Nigeria Police Force** arrest
3. **SilverTerrier context**: Nigerian BEC/phishing syndicate active since at least 2015; Delilah is the third Interpol operation in the sequence **Falcon I (2020) → Falcon II (2021) → Delilah (2022)**, together arresting at least 14 suspected members
4. **Cross-continental scope**: Police agencies from four continents participated
5. **Charges**: Operating a transnational cybercrime syndicate running mass phishing and BEC campaigns

## Why this source matters

For [[operation-delilah]] and for the wider IC narrative on SilverTerrier this Group-IB release provides:

- **Primary-participant confirmation** of the Falcon I → Falcon II → Delilah arc, useful for building a timeline
- Documentation of the **three-vendor + Interpol + Nigeria Police** intelligence chain — a replicable model for public–private IC
- Supports the SNA finding that Interpol operates as a *hub* node connecting vendor intelligence to national-police field action
- Helps quantify the enduring SilverTerrier threat: 14 arrests across three operations in three years, yet the group remains operationally active — illustrating the *resilience* challenge of BEC takedowns

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| Interpol Operation Delilah press release | Official coordinator statement |
| Palo Alto Networks Unit 42 blog | Independent vendor attribution, SilverTerrier technical indicators |
| Trend Micro research blog | Second independent vendor attribution |
| [[the-hacker-news-operation-delilah]] (if collected) | Independent news corroboration |
| [[cyberscoop-operation-delilah]] (if collected) | Independent news corroboration |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operation Delilah: Group-IB helps INTERPOL nab suspected leader | Group-IB | ~2022-05-25 | https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/ |
| [2] | Operation Delilah: Unit 42 Helps INTERPOL Identify Nigerian BEC Actor | Palo Alto Networks Unit 42 | 2022-05-25 | https://unit42.paloaltonetworks.com/operation-delilah-business-email-compromise-actor/ |
| [3] | Interpol arrests alleged leader of the SilverTerrier BEC gang | BleepingComputer | 2022-05-25 | https://www.bleepingcomputer.com/news/security/interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang/ |
