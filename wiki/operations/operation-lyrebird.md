---
operation_role: umbrella
parent_operation: ""
summary: "**Operation Lyrebird** was an INTERPOL-coordinated operation that resulted in the arrest of a suspect in **Morocco** linked to **phishing** and **carding** activities. The operation was conducted with intelligence support from cybersecurity firm **Group-IB**. The arrest demonstrated INTERPOL's growing capability to coordinate cybercrime operations in the African region."
aliases:

case_id: CYB-2021-050
challenges_encountered:

coordinating_body: "[[interpol]]"
created: 2026-04-08
credibility_index: 2.55
crime_type: "[[online-fraud-ic]]"
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
  - "[[group-ib-operation-lyrebird]]"
  - "[[2021-07-06_interpol-int_suspected-key-actor-arrested-in-morocco-operation-lyrebird]]"
  - "[[2021-07_portswigger-net_operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin]]"
  - "[[2021-09-28_technadu-com_operation-lyrebird-dr-hex-arrest]]"
  - "[[2021-07-06_darkreading-com_operation-lyrebird-morocco-arrest]]"
status: completed
target_entity: "Moroccan phishing/carding suspect"
timeframe:
  announced: 2021-07-05
  end: 2021-07-05
  ongoing: false
  start: 2021-07-05
title: "Operation Lyrebird"
title_ko: "라이어버드 작전"
type: operation
updated: 2026-04-26
---
> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

**Operation Lyrebird** was an INTERPOL-coordinated operation that resulted in the arrest of a suspect in **Morocco** linked to **phishing** and **carding** activities. The operation was conducted with intelligence support from cybersecurity firm **Group-IB**. The arrest demonstrated INTERPOL's growing capability to coordinate cybercrime operations in the African region.

## Background

Phishing and carding remain among the most common forms of cybercrime, with perpetrators operating from diverse geographic locations. Morocco has been identified as an origin point for some phishing and online fraud schemes targeting French-speaking and global victims. The collaboration between INTERPOL and Group-IB enabled the identification and location of the suspect.

## Participating Parties

### Coordinating Body
- [[interpol|INTERPOL]]

### Participating Countries
- [[morocco|Morocco]]

### Private Sector Support
- Group-IB (threat intelligence)

## Legal Framework

Specific legal instruments not detailed in available sources.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2021 | Operation Lyrebird conducted |
| 2021 | Arrest in Morocco |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 1 |

## Cooperation Mechanisms Used

INTERPOL coordination with Moroccan law enforcement, supported by Group-IB private sector intelligence.

## Korean Involvement (한국의 참여)

No Korean involvement identified.

## Contradictions & Open Questions

- What was the full scope of the suspect's criminal activities?
- How many victims were affected?
- Was the suspect convicted and sentenced?
- What specific evidence did Group-IB provide?

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

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Group-IB: Operation Lyrebird — Identifying 'Dr HeX' in Morocco | Group-IB | 2021-07-05 | https://www.group-ib.com/media-center/press-releases/gib-interpol-lyrebird/ |
| [2] | Suspected cybercrime actor arrested in Morocco after INTERPOL operation | INTERPOL | 2021-07-06 | https://www.interpol.int/News-and-Events/News/2021/Suspected-cybercrime-actor-arrested-in-Morocco |
| [3] | Operation Lyrebird: Cybercops nab Moroccan phish-and-carding kingpin | The Daily Swig / PortSwigger | 2021-07-01 | https://portswigger.net/daily-swig/operation-lyrebird-cybercops-nab-moroccan-phish-and-carding-kingpin |
| [4] | Operation Lyrebird leads to arrest of Dr HeX-linked suspect | TechNadu | 2021-09-28 | https://www.technadu.com/operation-lyrebird-dr-hex-arrest/315867/ |
| [5] | INTERPOL operation leads to Morocco arrest in phishing and carding case | Dark Reading | 2021-07-06 | https://www.darkreading.com/cyberattacks-data-breaches/interpol-operation-lyrebird-morocco-arrest |
