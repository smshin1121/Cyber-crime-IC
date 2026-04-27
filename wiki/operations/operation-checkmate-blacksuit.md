---
type: operation
title: "Operation Checkmate (BlackSuit/Royal Ransomware Takedown)"
aliases:
  - "Operation Checkmate"
  - "BlackSuit Takedown"
  - "Royal Ransomware Takedown"
operation_type: takedown
status: completed
case_id: CYB-2025-007
period: 3
enforcement_type:
  - seizure
  - takedown
  - asset_freeze
outcome: success
credibility_index: 2.28
source_tier: 2
edges:
  - source_actor: FBI
    target_actor: "UK Law Enforcement"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: FBI
    target_actor: "German Law Enforcement"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: HSI
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
missing_fields:
  - legal_basis
  - mechanisms_used
  - specific_international_agencies
timeframe:
  announced: 2025-08-11
  start: 2022
  end: 2025-07-24
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "BlackSuit (formerly Royal) ransomware group"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[germany]]"
  - "[[france]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
legal_basis:

mechanisms_used:

results:
  arrests: 0
  indictments: 0
  servers_seized: 4
  domains_seized: 9
  cryptocurrency_seized: "USD 1,091,453"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "450+ US victims identified since 2022"
    - "Bitcoin ransom payment of 49.3120227 BTC (USD 1,445,454.86 at transaction time) seized from one case"
related_cases:

related_operations:

challenges_encountered:

lessons_learned:
  - "Multi-agency domestic coordination (5 US agencies) combined with international partnerships enables comprehensive ransomware disruption"
  - "Domain seizures targeting leak sites and negotiation portals directly disrupt ransomware business model"
source_count: 5
sources:
  - "[[2025-08-11-doj-blacksuit-royal-ransomware-takedown]]"
  - "[[2025-07-24_bleepingcomputer-com_law-enforcement-seizes-blacksuit-ransomware-leak-sites]]"
  - "[[2025-07-25_scworld-com_operation-checkmate-shuts-down-blacksuits-extortion-sites]]"
  - "[[2025-07-25_bitdefender-com_after-500-million-in-ransom-demands-law-enforcement-seizes-blacksuit-site]]"
  - "[[2025-07-28_techradar-com_top-ransomware-group-blacksuit-has-dark-web-extortion-sites-seized-and-shut-down]]"
created: 2026-04-08
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "Operation Checkmate was a coordinated international operation to disrupt the **BlackSuit (formerly Royal) ransomware group**, announced by the US Department of Justice on 11 August 2025. The operation culminated in the takedown of **4 servers and 9 domains** on 24 July 2025. The seized domains were used by BlackSuit to leak stolen data and communicate with victims for ransom negotiations. **USD 1,091,453** in virtual currency was seized."
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[germany]]"
  - "[[france]]"
organizations:
  - "[[fbi-cyber-division]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[dark-web-ic]]"
---
## Summary

Operation Checkmate was a coordinated international operation to disrupt the **BlackSuit (formerly Royal) ransomware group**, announced by the US Department of Justice on 11 August 2025. The operation culminated in the takedown of **4 servers and 9 domains** on 24 July 2025. The seized domains were used by BlackSuit to leak stolen data and communicate with victims for ransom negotiations. **USD 1,091,453** in virtual currency was seized.

The operation involved five US agencies — Homeland Security Investigations (HSI), US Secret Service, IRS Criminal Investigation (IRS-CI), the [[fbi-cyber-division|FBI]], and DOJ — and international law enforcement from the United Kingdom, Germany, Ireland, France, Canada, Ukraine, and Lithuania.

## Background

BlackSuit ransomware evolved from the Royal ransomware group. Since 2022, BlackSuit had compromised **more than 450 victims** in the United States. The group operated a double-extortion model: encrypting victim data and threatening to publish stolen data on their leak site unless ransom was paid.

## Participating Parties

- **US agencies:** DOJ, DHS Homeland Security Investigations (HSI), US Secret Service, IRS Criminal Investigation, [[fbi-cyber-division|FBI]]
- **International partners:** United Kingdom, Germany, Ireland, France, Canada, Ukraine, Lithuania
- **Total countries:** 8

## Results and Impact

| Metric | Value |
|--------|-------|
| Servers seized | 4 |
| Domains seized | 9 |
| Cryptocurrency seized | USD 1,091,453 |
| US victims (since 2022) | 450+ |
| Countries participating | 8 |
| US agencies involved | 5 |

## Korean Involvement (한국의 참여)

No Korean involvement noted in this operation.

## Contradictions & Open Questions

- Were any BlackSuit operators identified or indicted?
- What is the total ransom collected by BlackSuit/Royal across all victims?
- Will the group reconstitute under a new name, as Royal did when becoming BlackSuit?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- US Department of Justice, 2025-08-11: Justice Department Announces Coordinated Disruption Actions Against BlackSuit (Royal) Ransomware Operations.
- BleepingComputer, 2025-07-24: BlackSuit ransomware extortion sites seized in Operation Checkmate.
- SC Media, 2025-07-25: Operation Checkmate shuts down BlackSuit's extortion sites.
- Bitdefender, 2025-07-25: After $500 Million in Ransom Demands, Law Enforcement Seizes BlackSuit Site.
- TechRadar, 2025-07-28: Top ransomware group BlackSuit has dark web extortion sites seized and shut down.

## Operational Timeline

- 2022: activity or investigation start.
- 2025-08-11: public announcement.
- 2025-07-24: reported enforcement endpoint.
- 2025-07-24: public source coverage from BleepingComputer.
- 2025-07-25: public source coverage from Bitdefender, SC Media.
- 2025-07-28: public source coverage from TechRadar.
- 2025-08-11: public source coverage from US Department of Justice.

## Legal and Procedural Posture

- Recorded crime classification: ransomware and dark web.
- Recorded enforcement posture: Seizure, Takedown, Asset Freeze.
- The record is categorized as takedown with status completed.

## Evidence and Attribution Notes

- DOJ press release announcing coordinated international disruption actions against the BlackSuit (Royal) ransomware group under Operation Checkmate.
- The operation involved 5 US agencies and international partners from 7 countries, seizing 4 servers and 9 domains used for data leaking and ransom negotiations.
- The US Department of Justice announced coordinated international disruption actions against the BlackSuit (Royal) ransomware group on 11 August 2025.
- The operation, codenamed Operation Checkmate, included the takedown of four servers and nine domains on 24 July 2025.
- The seized domains were used by BlackSuit to leak stolen data and communicate with victims to negotiate ransom payments.
- BleepingComputer reported that BlackSuit's extortion and leak sites were seized under Operation Checkmate.
- The article said DOJ confirmed a court-authorized seizure of the domains.
- It preserves the first public reporting around the July 24 infrastructure action.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US Department of Justice, 2025-08-11: The takedown was conducted by the Department of Homeland Security’s Homeland Security Investigations (HSI), the U.S.
- US Department of Justice, 2025-08-11: Secret Service, IRS Criminal Investigation (IRS-CI), the FBI, and international law enforcement from the United Kingdom, Germany, Ireland, France, Canada, Ukraine, and Lithuania.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against BlackSuit (formerly Royal) ransomware group, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Fbi Cyber Division and coordination to Fbi Cyber Division, with participating or affected jurisdictions recorded as United States, United Kingdom, Germany, France.

The cooperation model is documented through named agencies and partners: Fbi Cyber Division; enforcement posture: Seizure, Takedown, Asset Freeze.

Operational results captured for the canonical record: 4 servers seized; 9 domains seized; cryptocurrency/asset result recorded as USD 1,091,453; 450+ US victims identified since 2022; Bitcoin ransom payment of 49.3120227 BTC (USD 1,445,454.86 at transaction time) seized from one case.

The canonical source set contains 5 reference(s): 2025 08 11 Doj Blacksuit Royal Ransomware Takedown, 2025 07 24 Bleepingcomputer Com Law Enforcement Seizes Blacksuit Ransomware Leak Sites, 2025 07 25 Scworld Com Operation Checkmate Shuts Down Blacksuits Extortion Sites, 2025 07 25 Bitdefender Com After 500 Million In Ransom Demands Law Enforcement Seizes Blacksuit Site, 2025 07 28 Techradar Com Top Ransomware Group Blacksuit Has Dark Web Extortion Sites Seized And Shut Down.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis, Mechanisms Used, Specific International Agencies.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Justice Department Announces Coordinated Disruption Actions Against BlackSuit (Royal) Ransomware Operations | US Department of Justice | 2025-08-11 | https://www.justice.gov/opa/pr/justice-department-announces-coordinated-disruption-actions-against-blacksuit-royal |
| [2] | BlackSuit ransomware extortion sites seized in Operation Checkmate | BleepingComputer | 2025-07-24 | https://www.bleepingcomputer.com/news/security/law-enforcement-seizes-blacksuit-ransomware-leak-sites/ |
| [3] | Operation Checkmate shuts down BlackSuit's extortion sites | SC Media | 2025-07-25 | https://www.scworld.com/brief/operation-checkmate-shuts-down-blacksuits-extortion-sites |
| [4] | After $500 Million in Ransom Demands, Law Enforcement Seizes BlackSuit Site | Bitdefender | 2025-07-25 | https://www.bitdefender.com/en-us/blog/businessinsights/blacksuit-ransomware-seized-takedown |
| [5] | Top ransomware group BlackSuit has dark web extortion sites seized and shut down | TechRadar | 2025-07-28 | https://www.techradar.com/pro/security/top-ransomware-group-blacksuit-has-dark-web-extortion-sites-seized-and-shut-down |
