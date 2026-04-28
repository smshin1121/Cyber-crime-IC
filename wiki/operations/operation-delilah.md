---
operation_role: umbrella
parent_operation: ""
summary: "**Operation Delilah** was an INTERPOL-coordinated operation that resulted in the arrest of a leader of **SilverTerrier**, a prolific Nigerian Business Email Compromise (BEC) cybercrime group. The arrest was conducted in [[nigeria|Nigeria]] and represented a significant blow to one of the most tracked BEC groups."
aliases:

case_id: CYB-2022-050
challenges_encountered:

coordinating_body: "[[interpol]]"
created: 2026-04-08
credibility_index: 3.75
crime_type: "[[bec-ic]]"
edges:

enforcement_type:

lead_agency: "[[interpol]]"
legal_basis:

lessons_learned:

mechanisms_used:
  - "[[public-private-cooperation]]"
  - "[[capacity-building-ic]]"

missing_fields:

operation_type: arrest-sweep
outcome: success
participating_agencies:
  - "[[interpol]]"
  - "[[nigeria-police-force]]"
  - "[[group-ib]]"
  - "[[trend-micro]]"

participating_countries:
  - "[[nigeria]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[united-states]]"

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
    - "37-year-old suspected SilverTerrier leader arrested at Murtala Muhammed International Airport in Lagos"
    - "Private-sector referral from Group-IB, Palo Alto Networks Unit 42, and Trend Micro enriched by INTERPOL Cyber Fusion Centre"
    - "Third INTERPOL SilverTerrier-focused action after Falcon I and Falcon II"

  servers_seized: 0
  victims_notified: 0
crime_types:
  - "[[bec-ic]]"
  - "[[malware-ic]]"
source_count: 5
source_tier: 1
sources:
  - "[[group-ib-operation-delilah-silverterrier-bec]]"
  - "[[cyberscoop-operation-delilah-silverterrier-bec]]"
  - "[[2022-05-25_interpol-int_suspected-head-of-cybercrime-gang-arrested-in-nigeria]]"
  - "[[2022-05-25_bleepingcomputer-com_interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang]]"
  - "[[2022-05-25_unit42-paloaltonetworks-com_operation-delilah-business-email-compromise-actor]]"
status: completed
target_entity: "SilverTerrier BEC group leader"
timeframe:
  announced: 2022-05-25
  end: 2022-03
  ongoing: false
  start: 2021-05
title: "Operation Delilah (SilverTerrier BEC)"
title_ko: "들릴라 작전 (SilverTerrier BEC)"
type: operation
updated: 2026-04-28
---
## Summary

**Operation Delilah** was an INTERPOL-coordinated public-private operation against the SilverTerrier BEC ecosystem. The official INTERPOL release records that the cybercrime unit of the [[nigeria-police-force|Nigeria Police Force]] arrested a 37-year-old Nigerian suspect in Lagos after a year of international police collaboration.

The operation began with a private-sector intelligence referral from Group-IB, Palo Alto Networks Unit 42, and Trend Micro. INTERPOL's Cyber Fusion Centre enriched the intelligence, the Africa operations desk coordinated the case with Nigeria, and law-enforcement support was recorded from Australia, Canada, and the United States. That makes Delilah more than a simple one-person arrest: it is a named example of a public-private intelligence chain being converted into a physical arrest.

## Background

SilverTerrier is a Nigerian cybercrime cluster associated with business email compromise, mass phishing, credential theft, and malware-assisted fraud. The source set links Delilah to a wider INTERPOL sequence: Operation Falcon I in 2020, Operation Falcon II in 2021, and Delilah in 2022. Group-IB's source digest states that those three SilverTerrier-focused actions together produced at least 14 suspected-member arrests.

## Participating Parties

| Role | Parties |
|---|---|
| Coordination | [[interpol|INTERPOL]], including Cyber Fusion Centre and the Africa operations desk |
| Arrest execution | [[nigeria-police-force|Nigeria Police Force]] cybercrime unit |
| Private-sector intelligence | [[group-ib|Group-IB]], Palo Alto Networks Unit 42, [[trend-micro|Trend Micro]] |
| Named supporting jurisdictions | [[australia|Australia]], [[canada|Canada]], [[united-states|United States]] |
| Arrest location | Murtala Muhammed International Airport, Lagos, [[nigeria|Nigeria]] |

## Legal Framework

The public releases do not identify the domestic Nigerian charges or court file. What is documented is the operational mechanism: private-sector referral, INTERPOL analytic enrichment, AFJOC/Africa desk coordination, multiple case-coordination meetings, and Nigerian police arrest action.

## Operational Timeline

| Date | Event |
|------|-------|
| 2021-05 | INTERPOL's AFJOC/Africa desk capacity-building framework was active, and the Delilah referral process began. |
| 2021-2022 | INTERPOL and partners tracked the suspect's online and offline movements. |
| 2022-03 | Nigerian police arrested the suspect at Lagos airport. |
| 2022-05-25 | INTERPOL, Group-IB, CyberScoop, BleepingComputer, and Unit 42 published coordinated public coverage. |

## Results and Impact

- 1 senior SilverTerrier-linked suspect arrested in Nigeria.
- The suspect was linked in source coverage to mass phishing and BEC schemes targeting companies and individuals.
- Vendor reporting connects the suspect to hundreds of domains and dozens of malware command-and-control uses; these are attribution facts, not separate arrest counts.
- Delilah confirms that INTERPOL treated SilverTerrier as a recurring enforcement target across Falcon I, Falcon II, and Delilah.

## Cooperation Mechanisms Used

The strongest documented mechanism is public-private intelligence conversion: vendor telemetry and OSINT were referred to INTERPOL, enriched by INTERPOL analysts, coordinated through the Africa operations desk, and then actioned by Nigerian police. The operation also used case-coordination meetings with named support from Australia, Canada, and the United States.

## Korean Involvement (한국의 참여)

No Korean participation is identified in the current source set.

## Contradictions & Open Questions

- Nigerian charging, conviction, and sentencing records remain unavailable in the local corpus.
- The public sources identify supporting law-enforcement cooperation from several countries but do not publish a full country-by-country participant list for the four-continent coordination claim.
- Palo Alto Networks Unit 42 is a source and named contributor, but no separate organization page is currently present in the wiki taxonomy.

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

This page is retained as a canonical operation because it describes an INTERPOL-coordinated SilverTerrier BEC enforcement action, rather than a defendant-specific follow-on action. The record attributes lead responsibility and coordination to INTERPOL, with Nigeria as the arrest jurisdiction and Australia, Canada, and the United States recorded as named supporting jurisdictions.

The cooperation model is visible through private-sector referral, INTERPOL Cyber Fusion Centre enrichment, AFJOC/Africa desk coordination, and Nigerian police arrest execution.

Operational results captured for the canonical record: 1 arrest of a senior SilverTerrier-linked suspect; conversion of Group-IB, Unit 42, and Trend Micro intelligence into law-enforcement action.

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
