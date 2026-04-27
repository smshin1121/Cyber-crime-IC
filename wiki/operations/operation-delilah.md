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
crime_types:
  - "[[malware-ic]]"
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
updated: 2026-04-27
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

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- INTERPOL, 2022-05-25: Suspected head of cybercrime gang arrested in Nigeria The suspect’s arrest follows a year of international police collaboration, acting on information initially shared by private partners.
- INTERPOL, 2022-05-25: SINGAPORE: The cybercrime unit of the Nigeria Police Force arrested a 37-year-old Nigerian man in an international operation spanning four continents, coordinated and facilitated by the recently created Africa operations desk within INTERPOL’s cybercrime directorate .

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a arrest-sweep against SilverTerrier BEC group leader, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Interpol and coordination to Interpol, with participating or affected jurisdictions recorded as no participating-country list.

The cooperation model is visible primarily through the lead/coordinating agencies and country list; detailed legal mechanism fields remain sparse.

Operational results captured for the canonical record: 1 arrests.

The canonical source set contains 5 reference(s): Group Ib Operation Delilah Silverterrier Bec, Cyberscoop Operation Delilah Silverterrier Bec, 2022 05 25 Interpol Int Suspected Head Of Cybercrime Gang Arrested In Nigeria, 2022 05 25 Bleepingcomputer Com Interpol Arrests Alleged Leader Of The Silverterrier Bec Gang, 2022 05 25 Unit42 Paloaltonetworks Com Operation Delilah Business Email Compromise Actor.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Group-IB: Operation Delilah — Interpol Nabs Suspected Leader of Transnational Phishing Ring | Group-IB | 2022-05-25 | https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/ |
| [2] | CyberScoop: Operation Delilah (SilverTerrier BEC) | CyberScoop | 2022-05-25 | https://cyberscoop.com/silverterrier-interpol-nigeria-bec/ |
| [3] | Suspected head of cybercrime gang arrested in Nigeria | INTERPOL | 2022-05-25 | https://www.interpol.int/en/News-and-Events/News/2022/Suspected-head-of-cybercrime-gang-arrested-in-Nigeria |
| [4] | Interpol arrests alleged leader of the SilverTerrier BEC gang | BleepingComputer | 2022-05-25 | https://www.bleepingcomputer.com/news/security/interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang/ |
| [5] | Operation Delilah Helps Identify Business Email Compromise Actor | Palo Alto Networks Unit 42 | 2022-05-25 | https://unit42.paloaltonetworks.com/operation-delilah-business-email-compromise-actor/ |
