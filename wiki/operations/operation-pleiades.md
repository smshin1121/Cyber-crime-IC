---
type: operation
title: "Operation Pleiades"
title_ko: "Operation Pleiades (DD4BC 단속)"
aliases:
  - "DD4BC Takedown"
case_id: CYB-2015-006
period: 1
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2016-01-12
  start: 2015-12-15
  end: 2015-12-16
  ongoing: false
crime_type: "[[ddos-ic]]"
target_entity: "DD4BC (DDoS for Bitcoin) group"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-kingdom]]"
  - "[[austria]]"
  - "[[germany]]"
  - "[[bosnia-and-herzegovina]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[france]]"
  - "[[japan]]"
  - "[[romania]]"
  - "[[switzerland]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[j-cat]]"
  - "[[london-metropolitan-police]]"
  - "[[fbi]]"
  - "[[us-secret-service]]"
  - "[[interpol]]"
legal_basis:

mechanisms_used:

results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "One additional suspect detained"
    - "Property searches conducted in Bosnia and Herzegovina"
    - "DD4BC extortion network disrupted"
edges:
  - source_actor: "Europol EC3"
    target_actor: "London Metropolitan Police"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "UK Metropolitan Police Cyber Crime Unit"
    target_actor: "Bosnia and Herzegovina Federal Police"
    cooperation_type: intelligence_sharing
    legal_basis: unknown
    direction: undirected
credibility_index: 2.28
source_tier: 2
missing_fields:
  - legal_basis
  - mechanisms_used
related_cases:

related_operations:

challenges_encountered:

lessons_learned:
  - "DDoS extortion cases required broad reporting and information-sharing because many victims were reluctant to notify police."
  - "Operation Pleiades is an early example of coordinated crypto-extortion enforcement before ransomware became dominant."
source_count: 5
sources:
  - "[[europol-operation-pleiades]]"
  - "[[2016-01-12_pcworld_europol-tracks-dd4bc-cyber-extortion-gang-to-bosnia]]"
  - "[[2016-01-13_welivesecurity_global-operation-against-dd4bc-results-in-arrests]]"
  - "[[2016-01-12_coindesk_suspected-members-of-bitcoin-extortion-group-dd4bc-captured]]"
  - "[[2016-01-13_infosecurity-magazine_police-around-the-world-join-forces-to-target-ddos-gang]]"
created: 2026-04-08
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "Operation Pleiades was the December 2015 international action against DD4BC, the DDoS-for-Bitcoin extortion group. The operation combined Austrian, Bosnian, British, German, U.S., and wider international support, producing one arrest, one detention, and evidence seizures in Bosnia and Herzegovina."
jurisdictions:
  - "[[united-kingdom]]"
  - "[[austria]]"
  - "[[germany]]"
  - "[[bosnia-and-herzegovina]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[france]]"
  - "[[japan]]"
  - "[[romania]]"
  - "[[switzerland]]"
organizations:
  - "[[europol-ec3]]"
  - "[[j-cat]]"
  - "[[london-metropolitan-police]]"
  - "[[fbi]]"
  - "[[us-secret-service]]"
  - "[[interpol]]"
crime_types:
  - "[[ddos-ic]]"
---
## Summary

Operation Pleiades was the international enforcement action against DD4BC, a group known for threatening and launching distributed denial-of-service attacks unless victims paid in Bitcoin. The operation matters as an early multinational response to crypto-denominated cyber extortion, before later ransomware takedowns became more common.

## Participating Parties

**Lead and coordination**
- [[europol-ec3|Europol EC3]]
- [[j-cat|Joint Cybercrime Action Taskforce]]

**Operational countries**
- [[austria|Austria]]
- [[bosnia-and-herzegovina|Bosnia and Herzegovina]]
- [[germany|Germany]]
- [[united-kingdom|United Kingdom]]

**Supporting countries and agencies**
- [[france|France]]
- [[japan|Japan]]
- [[romania|Romania]]
- [[switzerland|Switzerland]]
- [[united-states|United States]] ([[fbi|FBI]], [[us-secret-service|US Secret Service]])
- [[australia|Australia]]
- [[interpol|INTERPOL]]

## Results

- **1 main target arrested**
- **1 additional suspect detained**
- **Property searches and evidence seizures** in Bosnia and Herzegovina
- **DD4BC extortion network disrupted**

## Threat Context

DD4BC started by targeting online gambling operators and later expanded into financial services and entertainment. Its model combined low-level proof-of-capability DDoS attacks with Bitcoin ransom demands and reputational threats if victims did not comply.

## Operational Timeline

| Date | Event |
|------|-------|
| 2014 | DD4BC extortion campaigns begin to draw international attention |
| 2015-12-15 to 2015-12-16 | Coordinated action days carried out |
| 2016-01-12 | Europol publicly announces Operation Pleiades |

## Cooperation Mechanisms Used

Public reporting credits:

- Austrian initiation of the operation
- UK Metropolitan Police Cyber Crime Unit identification of key suspects in Bosnia and Herzegovina
- Europol coordination through EC3 and J-CAT
- wider intelligence and support from France, Japan, Romania, Switzerland, Australia, the FBI, the U.S. Secret Service, and INTERPOL

## Korean Involvement

No Korean participation was identified in the available public record.

## Follow-Up Actions

> [!warning] No public court documents found
> Open-source review through 2026-04-23 did not surface accessible court records tied to the arrested DD4BC suspects.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2016-01-12: Europol: International Action Against DD4BC Cybercriminal Group (Operation Pleiades).
- PCWorld, 2016-01-12: Europol tracks DD4BC cyber-extortion gang to Bosnia.
- WeLiveSecurity, 2016-01-13: Global operation against DD4BC results in arrests.
- CoinDesk, 2016-01-12: Suspected Members of Bitcoin Extortion Group DD4BC Captured.
- Infosecurity Magazine, 2016-01-13: Police Around the World Join Forces to Target DDoS Gang.

## Legal and Procedural Posture

- Recorded crime classification: Ddos Ic.
- Recorded enforcement posture: Arrest and Seizure.
- The record is categorized as arrest-sweep with status completed.

## Evidence and Attribution Notes

- Europol announced Operation Pleiades on 12 January 2016, describing a coordinated 15-16 December 2015 action against the DD4BC (DDoS for Bitcoin) cybercriminal group responsible for Bitcoin extortion campaigns since mid-2014
- Lead agencies were the Austrian Cybercrime Competence Center (C4) and Bosnia and Herzegovina's Federal Police, supported by the German Bundeskriminalamt and the UK Metropolitan Police, with additional support from Australia, France, Japan, Romania, Switzerland, and the USA (FBI, US Secret Service)
- Operational outputs: one main target arrested and one additional suspect detained, with extensive property searches and substantial evidence seizures during the December 2015 action day
- DD4BC's modus operandi targeted online gambling operators initially, then expanded to financial services and the entertainment industry; victims received DDoS threats accompanied by Bitcoin ransom demands, with follow-on reputational threats for non-compliance
- Europol noted that companies paying ransom 'risk appearing vulnerable and being targeted again for a higher amount' — institutional guidance against ransom payment
- Operation Pleiades is an early (2015-2016) case study of INTERPOL-Europol joint coordination on crypto-extortion and is often cited as precedent for later DDoS-for-ransom enforcement actions
- PCWorld said Operation Pleiades produced one arrest and one detention in Bosnia and emphasized the UK Metropolitan Police Cyber Crime Unit's role in identifying the DD4BC suspects.
- PCWorld provides an accessible media account of the operational action in Bosnia and the supporting international coalition behind Operation Pleiades.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: International Action Against DD4BC Cybercriminal Group (Operation Pleiades) | Europol | 2016-01-12 | https://www.europol.europa.eu/media-press/newsroom/news/international-action-against-dd4bc-cybercriminal-group |
| [2] | Europol tracks DD4BC cyber-extortion gang to Bosnia | PCWorld | 2016-01-12 | https://www.pcworld.com/article/419135/europol-tracks-dd4bc-cyber-extortion-gang-to-bosnia.html |
| [3] | Global operation against DD4BC results in arrests | WeLiveSecurity | 2016-01-13 | https://www.welivesecurity.com/2016/01/13/global-operation-dd4bc-results-arrests/ |
| [4] | Suspected Members of Bitcoin Extortion Group DD4BC Captured | CoinDesk | 2016-01-12 | https://www.coindesk.com/markets/2016/01/12/suspected-members-of-bitcoin-extortion-group-dd4bc-captured |
| [5] | Police Around the World Join Forces to Target DDoS Gang | Infosecurity Magazine | 2016-01-13 | https://www.infosecurity-magazine.com/news/police-around-world-join-forces/ |
