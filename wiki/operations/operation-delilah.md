---
operation_role: umbrella
parent_operation: ""
summary: "**Operation Delilah** was an INTERPOL-coordinated operation that resulted in the arrest of a leader of **SilverTerrier**, a prolific Nigerian Business Email Compromise (BEC) cybercrime group. The arrest was conducted in [[nigeria|Nigeria]] and represented a significant blow to one of the most tracked BEC groups."
aliases:

case_id: CYB-2022-050
challenges_encountered:

coordinating_body: "[[interpol]]"
created: 2026-04-08
credibility_index: 2.25
crime_type: "[[bec-ic]]"
edges:

enforcement_type:

lead_agency: "[[interpol]]"
legal_basis:

lessons_learned:

mechanisms_used:

missing_fields:

operation_type: arrest-sweep
outcome: success
participating_agencies:

participating_countries:

period: 2
related_cases:

related_operations:

results:
  arrests: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:

  servers_seized: 0
  victims_notified: 0
source_count: 5
source_tier: 3
sources:
  - "[[group-ib-operation-delilah-silverterrier-bec]]"
  - "[[cyberscoop-operation-delilah-silverterrier-bec]]"
  - "[[2022-05-25_interpol-int_suspected-head-of-cybercrime-gang-arrested-in-nigeria]]"
  - "[[2022-05-25_bleepingcomputer-com_interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang]]"
  - "[[2022-05-25_unit42-paloaltonetworks-com_operation-delilah-business-email-compromise-actor]]"
status: completed
target_entity: "SilverTerrier BEC group leader"
timeframe:
  announced: 2022-01-01
  end: 2022-12-31
  ongoing: false
  start: 2022-01-01
title: "Operation Delilah (SilverTerrier BEC)"
title_ko: "들릴라 작전 (SilverTerrier BEC)"
type: operation
updated: 2026-04-26
---
> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

**Operation Delilah** was an INTERPOL-coordinated operation that resulted in the arrest of a leader of **SilverTerrier**, a prolific Nigerian Business Email Compromise (BEC) cybercrime group. The arrest was conducted in [[nigeria|Nigeria]] and represented a significant blow to one of the most tracked BEC groups.

SilverTerrier is a threat actor tracked by Palo Alto Networks' Unit 42, associated with hundreds of BEC campaigns targeting organizations worldwide.

## Background

SilverTerrier is a Nigerian cybercrime group known for conducting large-scale BEC attacks. The group has been tracked by cybersecurity researchers since the mid-2010s and is associated with multiple malware families used for credential theft and email compromise. The arrest of the group's leader was *likely* a result of long-term intelligence sharing between INTERPOL and private sector threat intelligence providers.

## Participating Parties

### Coordinating Body
- [[interpol|INTERPOL]]

### Participating Countries
- [[nigeria|Nigeria]]

## Legal Framework

Specific legal instruments not detailed in available sources. INTERPOL's operations in Nigeria for BEC enforcement have typically been conducted under bilateral cooperation arrangements.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2022 | SilverTerrier BEC leader arrested in Nigeria |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 1 (group leader) |

## Cooperation Mechanisms Used

INTERPOL coordination with Nigerian law enforcement (EFCC).

## Korean Involvement (한국의 참여)

No Korean involvement identified. SilverTerrier has primarily targeted Western companies, but BEC campaigns increasingly target Asia-Pacific organizations.

## Contradictions & Open Questions

- What was the total financial loss attributed to SilverTerrier?
- How many countries were victimized by the group?
- Was the arrested leader convicted?
- Which private sector companies provided intelligence for the operation?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Group-IB, 2022-05-25: Group-IB: Operation Delilah — Interpol Nabs Suspected Leader of Transnational Phishing Ring.
- CyberScoop, 2022-05-25: CyberScoop: Operation Delilah (SilverTerrier BEC).
- INTERPOL, 2022-05-25: Suspected head of cybercrime gang arrested in Nigeria.
- BleepingComputer, 2022-05-25: Interpol arrests alleged leader of the SilverTerrier BEC gang.
- Palo Alto Networks Unit 42, 2022-05-25: Operation Delilah Helps Identify Business Email Compromise Actor.

## Evidence and Attribution Notes

- Group-IB announced on or around 2022-05-25 that Operation Delilah — led by Interpol with intelligence support from Group-IB, Palo Alto Networks Unit 42, and Trend Micro — resulted in the arrest of a 37-year-old Nigerian man at Murtala Muhammed International Airport in Lagos in March 2022
- The suspect is alleged to be a senior leader of the SilverTerrier cybercrime syndicate, which has operated BEC and mass-phishing campaigns since at least 2015
- Delilah is the *third* Interpol operation focused on SilverTerrier, following Operation Falcon I (November 2020) and Operation Falcon II (2021); the three operations together have led to the arrest of at least 14 suspected SilverTerrier members
- Intelligence chain: Group-IB, Unit 42, and Trend Micro provided the initial threat-intelligence referral → Interpol Cyber Fusion Centre analysts enriched it → Nigerian police conducted the physical arrest at the airport (tracking months of suspect movements)
- Operation Delilah's law-enforcement coordination spanned police agencies across four continents (including Europe, Asia, Africa, Australia)
- Significance for IC studies: Delilah illustrates a rare operationalisation of a *public–private intelligence chain* where three commercial cybersecurity vendors drove an Interpol-coordinated arrest — a pattern used later in Africa Cyber Surge II (2023)
- INTERPOL's Operation Delilah resulted in the March 2022 arrest of a 37-year-old Nigerian man identified as a senior figure in the SilverTerrier BEC fraud network, detained upon attempting to re-enter Nigeria after fleeing arrest in 2021
- Researchers (Palo Alto Networks Unit 42, Group-IB, Trend Micro) traced more than 240 domains registered to the suspect's aliases, with 50+ used for malware command-and-control; the group is assessed to have targeted ~50,000 victims since 2014

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Group-IB: Operation Delilah — Interpol Nabs Suspected Leader of Transnational Phishing Ring | Group-IB | 2022-05-25 | https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/ |
| [2] | CyberScoop: Operation Delilah (SilverTerrier BEC) | CyberScoop | 2022-05-25 | https://cyberscoop.com/silverterrier-interpol-nigeria-bec/ |
| [3] | Suspected head of cybercrime gang arrested in Nigeria | INTERPOL | 2022-05-25 | https://www.interpol.int/en/News-and-Events/News/2022/Suspected-head-of-cybercrime-gang-arrested-in-Nigeria |
| [4] | Interpol arrests alleged leader of the SilverTerrier BEC gang | BleepingComputer | 2022-05-25 | https://www.bleepingcomputer.com/news/security/interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang/ |
| [5] | Operation Delilah Helps Identify Business Email Compromise Actor | Palo Alto Networks Unit 42 | 2022-05-25 | https://unit42.paloaltonetworks.com/operation-delilah-business-email-compromise-actor/ |
