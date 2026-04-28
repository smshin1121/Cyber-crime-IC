---
aliases:

case_id: CYB-2020-001
challenges_encountered:

coordinating_body: "[[interpol]]"
created: 2026-04-08
credibility_index: 3.62
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

participating_countries:
  - "[[nigeria]]"

period: 2
related_cases:

related_operations:

results:
  arrests: 3
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:
    - "Three suspected TMT/SilverTerrier members arrested in Lagos"
    - "26 malware families, spyware tools, and remote-access trojans attributed in source coverage"
    - "Group-IB attributed potential compromise of more than 500,000 organizations across 150+ countries to the broader cluster"

  servers_seized: 0
  victims_notified: 0
source_count: 5
source_tier: 2
sources:
  - "[[interpol-operation-falcon]]"
  - "[[cyberscoop-operation-falcon]]"
  - "[[2020-11-25_group-ib_operation-falcon-group-ib-helps-interpol-identify-nigerian-bec-ring-members]]"
  - "[[2020-11-27_pmnewsnigeria_operation-falcon-three-nigerians-busted-for-cybercrime]]"
  - "[[2020-11-27_guardian-ng_operation-falcon-nigerian-police-join-interpol-group-ib-to-arrest-three-suspected-tmt-fraudsters]]"
status: completed
target_entity: "Nigerian BEC group (TMT)"
timeframe:
  announced: 2020-11
  end: 2020-11
  ongoing: false
  start: 2019
title: "Operation Falcon"
title_ko: "Operation Falcon (나이지리아 BEC 조직 단속)"
type: operation
updated: 2026-04-28
operation_role: umbrella
parent_operation: ""
summary: "INTERPOL, Group-IB, and the Nigeria Police Force conducted Operation Falcon, a joint investigation that resulted in the arrest of 3 Nigerian nationals in November 2020. The suspects were part of a prolific cybercrime group that used 26 different types of malware including AgentTesla, Loki, Azorult, Spartan, Nanocore, and Remcos to conduct phishing attacks and Business Email Compromise (BEC) schemes targeting government organizations and private companies in over 150 countries."
organizations:
  - "[[interpol]]"
crime_types:
  - "[[bec-ic]]"
  - "[[malware-ic]]"
---
## Summary

Operation Falcon was the first named INTERPOL/Group-IB/Nigeria Police Force action against the Nigerian TMT/SilverTerrier BEC ecosystem. The operation followed a year-long investigation and resulted in the arrest of three suspects in Lagos in November 2020.

The source set gives the operation more substance than the arrest count alone. It links the suspects to phishing and BEC campaigns, 26 malware families or remote-access tools, and a broader victimization footprint across more than 150 countries. Group-IB's attribution is broader than the three arrested defendants, so the wiki separates the confirmed enforcement result from the wider threat-intelligence estimate.

## Participating Parties

| Role | Parties |
|---|---|
| Coordination | [[interpol|INTERPOL]] |
| Arrest execution | [[nigeria-police-force|Nigeria Police Force]] |
| Private-sector intelligence | [[group-ib|Group-IB]] |
| Enforcement jurisdiction | [[nigeria|Nigeria]] |
| Victim footprint | Organizations and individuals in 150+ countries were reported as targeted or potentially compromised, but those are not all participant jurisdictions. |

## Results

- **3 arrests** in Lagos, Nigeria.
- **26 malware/tool families** identified in source coverage, including AgentTesla, Loki, Azorult, Spartan, Nanocore, and Remcos.
- **50,000 victims** were attributed by INTERPOL/CyberScoop coverage to the three suspects.
- **500,000+ potentially compromised organizations** across **150+ countries** were attributed by Group-IB to the broader TMT cluster.
- Operation Falcon is analytically linked to Falcon II and Operation Delilah, but those later actions remain separate operation records.

## Cooperation Model

Falcon is a compact public-private enforcement model: Group-IB developed the technical intelligence, INTERPOL coordinated the international police channel, and Nigerian police executed arrests domestically. The victim geography is global, but the currently documented enforcement venue is Nigeria.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- INTERPOL, Unknown: INTERPOL: Operation Falcon.
- CyberScoop, 2020-11-25: CyberScoop: Accused Email Scammers Busted in Nigeria (Operation Falcon).
- Group-IB, 2020-11-25: Operation Falcon: Group-IB helps INTERPOL identify Nigerian BEC ring members.
- PM News Nigeria, 2020-11-27: Interpol: 3 Nigerians busted for cybercrime, operate in 150 countries.
- The Guardian Nigeria, 2020-11-27: Nigerian police join INTERPOL, Group-IB to arrest three suspected TMT fraudsters.

## Operational Timeline

- 2019: activity or investigation start.
- 2020-11: public announcement.
- 2020-11: reported enforcement endpoint.
- 2020-11-25: public source coverage from CyberScoop, Group-IB.
- 2020-11-27: public source coverage from PM News Nigeria, The Guardian Nigeria.
- Unknown: public source coverage from INTERPOL.

## Legal and Procedural Posture

- Recorded crime classification: BEC and malware.
- The record is categorized as arrest-sweep with status completed.

## Evidence and Attribution Notes

- CyberScoop reported on 2020-11-25 that Interpol, Group-IB, and the Nigeria Police Force concluded a year-long operation (Operation Falcon) targeting the Nigerian BEC/phishing gang known as TMT
- Three suspects arrested in Lagos, identified only by initials (O.C., I.O., O.I.); Interpol cited their alleged involvement in defrauding approximately 50,000 victims
- Group-IB assessment: TMT had compromised 'potentially more than 500,000' victims since 2017, spanning over 150 countries — a much larger victim pool than the three suspects were directly tied to
- TMT's tooling included commodity info-stealers and RATs: AgentTesla, Loki, AzoRult, and NetWire; they also exploited COVID-19 themes as bait (fraudulent aid offers)
- Macro-level context cited in the article: FBI IC3 recorded approximately USD 1.7 billion in BEC losses for 2019 alone, framing why Interpol prioritised Nigerian BEC groups
- This is the Falcon I (November 2020) operation, distinct from Falcon II (2021) and the subsequent Operation Delilah (2022), all targeting the overlapping SilverTerrier/TMT Nigerian BEC ecosystem
- Group-IB said Operation Falcon led to the arrest of three TMT gang members in Lagos.
- The release attributed more than 500,000 compromised organizations across 150 countries to the broader TMT cluster.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- INTERPOL, 2020-11-01: Three arrested as INTERPOL, Group-IB and the Nigeria Police Force disrupt prolific cybercrime group The year-long investigation was code-named ‘Operation Falcon’ Three suspects have been arrested in Lagos following a joint INTERPOL, Group-IB and Nigeria Police Force cybercrime investigation.
- INTERPOL, 2020-11-01: They then used these campaigns to disseminate 26 malware programmes, spyware and remote access tools, including AgentTesla, Loki, Azorult, Spartan and the nanocore and Remcos Remote Access Trojans.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes an INTERPOL-coordinated arrest sweep against the Nigerian TMT/SilverTerrier BEC cluster, rather than a defendant-specific follow-on action. The record attributes lead responsibility and coordination to INTERPOL, with Nigeria recorded as the enforcement jurisdiction.

The cooperation model is visible through INTERPOL coordination, Group-IB intelligence support, and Nigeria Police Force arrest execution.

Operational results captured for the canonical record: 3 arrests; 26 malware/tool families identified; threat-intelligence reporting of 50,000 direct victims and 500,000+ potentially compromised organizations across 150+ countries.

The canonical source set contains 5 reference(s): Interpol Operation Falcon, Cyberscoop Operation Falcon, 2020 11 25 Group Ib Operation Falcon Group Ib Helps Interpol Identify Nigerian Bec Ring Members, 2020 11 27 Pmnewsnigeria Operation Falcon Three Nigerians Busted For Cybercrime, 2020 11 27 Guardian Ng Operation Falcon Nigerian Police Join Interpol Group Ib To Arrest Three Suspected Tmt Fraudsters.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | INTERPOL: Operation Falcon | INTERPOL | Unknown | https://www.interpol.int/News-and-Events/News/2020/Three-arrested-as-INTERPOL-Group-IB-and-the-Nigeria-Police-Force-disrupt-prolific-cybercrime-group |
| [2] | CyberScoop: Accused Email Scammers Busted in Nigeria (Operation Falcon) | CyberScoop | 2020-11-25 | https://cyberscoop.com/nigeria-email-scam-arrests-bec-group-ib/ |
| [3] | Operation Falcon: Group-IB helps INTERPOL identify Nigerian BEC ring members | Group-IB | 2020-11-25 | https://www.group-ib.com/media-center/press-releases/gib-interpol-bec/ |
| [4] | Interpol: 3 Nigerians busted for cybercrime, operate in 150 countries | PM News Nigeria | 2020-11-27 | https://pmnewsnigeria.com/2020/11/27/interpol-3-nigerians-busted-for-cyber-crime-operate-in-150-countries/ |
| [5] | Nigerian police join INTERPOL, Group-IB to arrest three suspected TMT fraudsters | The Guardian Nigeria | 2020-11-27 | https://guardian.ng/news/nigerian-police-join-interpol-group-ib-to-arrest-three-suspected-tmt-fraudsters/ |
