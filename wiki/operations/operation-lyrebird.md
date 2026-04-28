---
operation_role: umbrella
parent_operation: ""
summary: "**Operation Lyrebird** was an INTERPOL-coordinated operation that resulted in the arrest of a suspect in **Morocco** linked to **phishing** and **carding** activities. The operation was conducted with intelligence support from cybersecurity firm **Group-IB**. The arrest demonstrated INTERPOL's growing capability to coordinate cybercrime operations in the African region."
aliases:

case_id: CYB-2021-050
challenges_encountered:

coordinating_body: "[[interpol]]"
created: 2026-04-08
credibility_index: 3.55
crime_type: "[[online-fraud-ic]]"
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
  - "[[morocco-dgsn]]"
  - "[[group-ib]]"

participating_countries:
  - "[[morocco]]"

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
    - "Moroccan suspect tracked as Dr HeX arrested by Moroccan police"
    - "Group-IB linked the suspect to attacks on 134 websites over 2009-2018"
    - "Private-sector attribution pivoted from phishing-kit evidence and OSINT to INTERPOL-coordinated arrest"

  servers_seized: 0
  victims_notified: 0
crime_types:
  - "[[online-fraud-ic]]"
  - "[[malware-ic]]"
source_count: 5
source_tier: 2
sources:
  - "[[group-ib-operation-lyrebird]]"
  - "[[2021-07-06_interpol-int_suspected-key-actor-arrested-in-morocco-operation-lyrebird]]"
  - "[[2021-07_portswigger-net_operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin]]"
  - "[[2021-09-28_technadu-com_operation-lyrebird-dr-hex-arrest]]"
  - "[[2021-07-06_darkreading-com_operation-lyrebird-morocco-arrest]]"
status: completed
target_entity: "Moroccan phishing/carding suspect"
timeframe:
  announced: 2021-07-05
  end: 2021-05
  ongoing: false
  start: 2019
title: "Operation Lyrebird"
title_ko: "라이어버드 작전"
type: operation
updated: 2026-04-28
---
## Summary

**Operation Lyrebird** was an INTERPOL-coordinated public-private action that led to the arrest in [[morocco|Morocco]] of a suspect tracked by Group-IB as **Dr HeX**. The operation targeted phishing, carding, defacement, fraud, and malware-development activity attributed to the suspect over a long period.

The operational value of Lyrebird is the attribution chain. Group-IB reported that its analysts started the investigation in 2019, extracted a phishing kit, pivoted from an email address to public OSINT accounts, and connected the online persona to a Moroccan suspect. INTERPOL then coordinated with Moroccan police, who carried out the arrest in May 2021.

## Background

Group-IB's source digest links Dr HeX to attacks on 134 websites between 2009 and 2018, including French telecommunications companies, major French banks, and multinational corporations. The suspect's French-language capability is cited as relevant to the targeting pattern. The INTERPOL source gives the official law-enforcement confirmation for the Morocco arrest, while the media sources corroborate the Dr HeX attribution and carding/phishing framing.

## Participating Parties

| Role | Parties |
|---|---|
| Coordination | [[interpol|INTERPOL]] |
| Arrest execution | Moroccan police / [[morocco-dgsn|DGSN]]-linked national policing structure |
| Private-sector intelligence | [[group-ib|Group-IB]] |
| Enforcement jurisdiction | [[morocco|Morocco]] |

## Legal Framework

The public source set does not publish Moroccan charging papers or a court docket. The documented mechanism is operational coordination: private-sector threat intelligence, INTERPOL coordination, and Moroccan police arrest execution.

## Operational Timeline

| Date | Event |
|------|-------|
| 2019 | Group-IB investigation into the Dr HeX persona began. |
| 2021-05 | Moroccan police arrested the suspect. |
| 2021-07-05 | Group-IB announced Operation Lyrebird. |
| 2021-07-06 | INTERPOL and independent media coverage confirmed the operation publicly. |

## Results and Impact

- 1 Moroccan suspect arrested.
- The suspect was attributed by Group-IB to phishing, carding, malware development, defacement, and fraud.
- Group-IB linked the suspect to attacks on 134 websites over 2009-2018.
- Lyrebird demonstrates an INTERPOL model in which private OSINT/technical attribution becomes a police action in an African jurisdiction.

## Cooperation Mechanisms Used

Private-sector threat intelligence was converted into an INTERPOL-coordinated police action. In the wiki taxonomy this is best represented as public-private cooperation with an African cyber-capacity-building context, rather than a JIT or MLAT-centered case.

## Korean Involvement (한국의 참여)

No Korean involvement identified.

## Contradictions & Open Questions

- Moroccan court outcome and sentencing information are not present in the current corpus.
- The source set supports 134 websites as an attribution count, not a confirmed victim count.
- DGSN is used as the closest existing Moroccan national-police taxonomy page; the public sources describe "Moroccan police" without naming a specific unit.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Group-IB, 2021-07-05: Group-IB: Operation Lyrebird — Identifying 'Dr HeX' in Morocco.
- INTERPOL, 2021-07-06: Suspected cybercrime actor arrested in Morocco after INTERPOL operation.
- The Daily Swig / PortSwigger, 2021-07-01: Operation Lyrebird: Cybercops nab Moroccan phish-and-carding kingpin.
- TechNadu, 2021-09-28: Operation Lyrebird leads to arrest of Dr HeX-linked suspect.
- Dark Reading, 2021-07-06: INTERPOL operation leads to Morocco arrest in phishing and carding case.

## Evidence and Attribution Notes

- Operation Lyrebird, announced on 5 July 2021 by Group-IB and INTERPOL, resulted in the May 2021 arrest of a Moroccan national identified by Group-IB's Threat Intelligence team as 'Dr HeX' by Moroccan police
- Dr HeX was alleged to be active from at least 2009 and was linked by Group-IB to attacks on 134 websites over 2009-2018, including phishing kits, defacement, malware development, fraud, and carding
- Key victims included French telecommunications companies, major French banks, and multinational corporations — the suspect's French-language skills enabled targeting of French-speaking victim bases
- Attribution methodology: Group-IB analysts extracted a phishing kit, found an email address inside it, pivoted to the suspect's YouTube channel (signed up under the same name 'Dr HeX'), and cross-referenced OSINT indicators to deanonymize
- Cooperation model: Private-sector threat intelligence (Group-IB) → INTERPOL (coordination) → Moroccan national police (arrest execution).
- This illustrates INTERPOL's growing 'force multiplier' role for private-sector intelligence in the African region
- Two-year investigation timeline — Group-IB's investigation began in 2019 before INTERPOL coordination was formalized
- INTERPOL announced the Moroccan arrest linked to Operation Lyrebird.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes an INTERPOL-coordinated arrest sweep against a Moroccan phishing/carding suspect, rather than a defendant-specific follow-on action. The record attributes lead responsibility and coordination to INTERPOL, with Morocco recorded as the enforcement jurisdiction.

The cooperation model is visible through Group-IB attribution, INTERPOL coordination, and Moroccan police arrest execution.

Operational results captured for the canonical record: 1 arrest; attribution of the Dr HeX persona to phishing, carding, defacement, malware development, and attacks on 134 websites.

The canonical source set contains 5 reference(s): Group Ib Operation Lyrebird, 2021 07 06 Interpol Int Suspected Key Actor Arrested In Morocco Operation Lyrebird, 2021 07 Portswigger Net Operation Lyrebird Cybercops Nab Moroccan Phish And Carding Kingpin, 2021 09 28 Technadu Com Operation Lyrebird Dr Hex Arrest, 2021 07 06 Darkreading Com Operation Lyrebird Morocco Arrest.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Group-IB: Operation Lyrebird — Identifying 'Dr HeX' in Morocco | Group-IB | 2021-07-05 | https://www.group-ib.com/media-center/press-releases/gib-interpol-lyrebird/ |
| [2] | Suspected cybercrime actor arrested in Morocco after INTERPOL operation | INTERPOL | 2021-07-06 | https://www.interpol.int/News-and-Events/News/2021/Suspected-cybercrime-actor-arrested-in-Morocco |
| [3] | Operation Lyrebird: Cybercops nab Moroccan phish-and-carding kingpin | The Daily Swig / PortSwigger | 2021-07-01 | https://portswigger.net/daily-swig/operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin |
| [4] | Operation Lyrebird leads to arrest of Dr HeX-linked suspect | TechNadu | 2021-09-28 | https://www.technadu.com/operation-lyrebird-dr-hex-arrest/315867/ |
| [5] | INTERPOL operation leads to Morocco arrest in phishing and carding case | Dark Reading | 2021-07-06 | https://www.darkreading.com/cyberattacks-data-breaches/interpol-operation-lyrebird-morocco-arrest |
