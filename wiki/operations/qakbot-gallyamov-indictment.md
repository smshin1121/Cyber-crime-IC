---
type: operation
title: "QakBot / Gallyamov Indictment"
aliases:

case_id: CYB-2025-005
operation_type: joint-investigation
operation_role: umbrella
parent_operation: ""
status: ongoing
period: 3
enforcement_type:

outcome: ongoing
credibility_index: 3.25
source_tier: 2
edges:

missing_fields:
  - legal_basis
  - mechanisms_used
timeframe:
  announced: 2025-05-22
  start: 2008
  end: ""
  ongoing: true
crime_type: "[[ransomware-ic]]"
target_entity: "Rustam Rafailevich Gallyamov and Qakbot malware network"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[canada]]"
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[netherlands-om]]"
  - "[[netherlands-politie]]"
legal_basis:

mechanisms_used:

results:
  arrests: 0
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "USD 24,000,000+"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:

related_cases:
  - "[[us-v-gallyamov-qakbot]]"
related_operations:
  - "[[operation-endgame-phase2]]"
challenges_encountered:

lessons_learned:

source_count: 5
sources:
  - "[[2025-05-22_justice-gov_qakbot-gallyamov-indictment]]"
  - "[[2023-08-29_om-nl_qakbot-onschadelijk-gemaakt]]"
  - "[[2025-05-22_cdca_qakbot-gallyamov-indictment]]"
  - "[[2025-05-23_helpnetsecurity-com_danabot-botnet-disrupted-qakbot-leader-indicted]]"
  - "[[2023-08-30_eurojust-europa-eu_qakbot-malware-network-dismantled]]"
created: 2026-04-08
updated: 2026-04-27
summary: "The US Department of Justice unsealed an indictment on 22 May 2025 charging Rustam Rafailevich Gallyamov with leading the Qakbot malware conspiracy. The operation also sits on top of a multinational disruption chain in which Dutch prosecutors and police publicly described the 2023 seizure of 22 Qakbot servers in the Netherlands."
organizations:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[netherlands-om]]"
  - "[[netherlands-politie]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
jurisdictions:
  - "[[canada]]"
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
---
## Summary

The US Department of Justice unsealed an indictment on 22 May 2025 charging **Rustam Rafailevich Gallyamov**, 48, of Moscow, Russia, with leading the Qakbot malware conspiracy since 2008. Gallyamov allegedly used Qakbot to build a botnet providing access to co-conspirators who deployed ransomware variants including **ProLock, DopplePaymer, Egregor, REvil, Conti, Name Locker, Black Basta, and Cactus**.

This action was a multinational effort involving the US, France, Germany, the Netherlands, Denmark, the United Kingdom, and Canada, with [[europol-ec3|Europol]] providing support.

## Audit Note

This page intentionally fuses the 2025 indictment with the 2023 Dutch disruption layer. The multinational substance is real, but the two phases should not be read as a single procedural event.

## Background

Qakbot, also known as QBot or Pinkslipbot, is one of the longest-running malware families, active since 2008. Originally a banking trojan, it evolved into a major initial-access-as-a-service platform for ransomware operators. In August 2023, a multinational action disrupted the botnet and seized infrastructure across several countries.

The Dutch prosecution-side record is particularly useful for this operation family. In August 2023, the [[netherlands-om|Openbaar Ministerie]] and Dutch police jointly announced the Qakbot botnet disruption and said that **22 servers** tied to the malware had been seized in Dutch datacenters. That gives this repo a direct way to connect Dutch prosecutorial involvement to the wider Qakbot enforcement chain, rather than leaving the Netherlands as a nameless supporting state.

## Participating Parties

- **Lead:** US Department of Justice / [[fbi-cyber-division|FBI Cyber Division]]
- **Coordination support:** [[europol-ec3|Europol EC3]]
- **Dutch prosecutor-side partner for the earlier disruption layer:** [[netherlands-om|Openbaar Ministerie - Landelijk Parket]]
- **Dutch police-side partner for the earlier disruption layer:** [[netherlands-politie|Dutch National Police]]
- **International partners:** France, Germany, Netherlands, Denmark, United Kingdom, Canada

## Results and Impact

- **Indictment** of Gallyamov for conspiracy, wire fraud, and related charges
- **USD 24 million+** in cryptocurrency targeted through civil forfeiture

## Contradictions & Open Questions

- Will Gallyamov ever be apprehended given his location in Russia?
- How effective was the August 2023 botnet takedown if criminal activity continued?
- What is the total financial impact of Qakbot-facilitated ransomware attacks?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- US DOJ, 2025-05-22: Page not found.
- Openbaar Ministerie, 2023-08-29: Grootste wereldwijde botnet Qakbot onschadelijk gemaakt.
- US DOJ (OPA), 2025-05-22: Leader of Qakbot Malware Conspiracy Indicted for Involvement in Global Ransomware Scheme.
- Help Net Security, 2025-05-23: DanaBot botnet disrupted, QakBot leader indicted.
- Eurojust, 2023-08-30: Malware network that infected more than 700,000 victims and caused hundreds of millions of dollars in damage worldwide dismantled in multinational..

## Operational Timeline

- 2008: activity or investigation start.
- 2025-05-22: public announcement.
- 2023-08-29: public source coverage from Openbaar Ministerie.
- 2023-08-30: public source coverage from Eurojust.
- 2025-05-22: public source coverage from US DOJ, US DOJ (OPA).
- 2025-05-23: public source coverage from Help Net Security.

## Legal and Procedural Posture

- Recorded crime classification: ransomware and malware.
- The record is categorized as joint-investigation with status ongoing.
- Related legal or operational records: Us V Gallyamov Qakbot.

## Evidence and Attribution Notes

- The OM and Dutch police jointly announced the international Qakbot disruption.
- The Dutch side reported seizure of 22 servers in different datacenters in the Netherlands.
- The source shows formal prosecution involvement in a major multinational botnet operation.
- This joint OM-police release documents Dutch prosecutorial participation in the Qakbot disruption.
- On 22 May 2025, the Department of Justice unsealed an indictment charging Rustam Rafailevich Gallyamov, 48, of Moscow, Russia, with leading the QakBot malware conspiracy since 2008.
- The indictment was unsealed in conjunction with Operation Endgame, the international law enforcement campaign targeting ransomware-enabling infrastructure.
- Charges Gallyamov was charged with conspiracy, wire fraud, and related offenses.
- He allegedly developed and deployed QakBot to build a botnet that provided access to co-conspirators who deployed ransomware variants including ProLock, DopplePaymer, Egregor, REvil, Conti, Name Locker, Black Basta, and Cactus.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- Eurojust, 2023-08-30: Malware network that infected more than 700.000 victims and caused hundreds of millions of dollars in damage worldwide dismantled in multinational law enforcement operation | Eurojust | European Union Agency for Criminal Justice Cooperation Eurojust European Union Agency for Criminal Justice Cooperation Search Main navigation Home About.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a joint-investigation against Rustam Rafailevich Gallyamov and Qakbot malware network, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Fbi Cyber Division and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Canada, Denmark, France, Germany, Netherlands, United Kingdom, United States.

The cooperation model is documented through named agencies and partners: Fbi Cyber Division, Europol Ec3, Netherlands Om, Netherlands Politie.

Operational results captured for the canonical record: 1 indictments; cryptocurrency/asset result recorded as USD 24,000,000+.

The canonical source set contains 5 reference(s): 2025 05 22 Justice Gov Qakbot Gallyamov Indictment, 2023 08 29 Om Nl Qakbot Onschadelijk Gemaakt, 2025 05 22 Cdca Qakbot Gallyamov Indictment, 2025 05 23 Helpnetsecurity Com Danabot Botnet Disrupted Qakbot Leader Indicted, 2023 08 30 Eurojust Europa Eu Qakbot Malware Network Dismantled.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis and Mechanisms Used.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Page not found | US DOJ | 2025-05-22 | https://www.justice.gov/archives/opa/pr/leader-qakbot-malware-conspiracy-indictment-involvement-global-ransomware-scheme |
| [2] | Grootste wereldwijde botnet Qakbot onschadelijk gemaakt | Openbaar Ministerie | 2023-08-29 | https://www.om.nl/actueel/nieuws/2023/08/29/grootste-wereldwijde-botnet-qakbot-onschadelijk-gemaakt |
| [3] | Leader of Qakbot Malware Conspiracy Indicted for Involvement in Global Ransomware Scheme | US DOJ (OPA) | 2025-05-22 | https://www.justice.gov/opa/pr/leader-qakbot-malware-conspiracy-indicted-involvement-global-ransomware-scheme |
| [4] | DanaBot botnet disrupted, QakBot leader indicted | Help Net Security | 2025-05-23 | https://www.helpnetsecurity.com/2025/05/23/operation-endgame-danabot-botnet-disrupted-qakbot-leader-indicted/ |
| [5] | Malware network that infected more than 700,000 victims and caused hundreds of millions of dollars in damage worldwide dismantled in multinational law enforcement operation | Eurojust | 2023-08-30 | https://www.eurojust.europa.eu/news/malware-network-infected-more-700000-victims-and-caused-hundreds-millions-dollars-damage |
