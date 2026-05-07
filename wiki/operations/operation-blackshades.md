---
type: operation
title: "Operation Blackshades"
title_ko: "Operation Blackshades"
aliases:
  - "Blackshades malware takedown"
  - "Blackshades RAT takedown"
  - "International Blackshades Malware Takedown"
case_id: CYB-2014-002
period: 1
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - indictment
  - search-seizure
  - domain-seizure
  - extradition
outcome: success
timeframe:
  announced: 2014-05-19
  start: 2013-11
  end: 2015-06
  ongoing: false
crime_type: "[[malware-ic]]"
target_entity: "Blackshades Remote Access Tool creators, sellers, and users"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[belgium]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[united-kingdom]]"
  - "[[finland]]"
  - "[[austria]]"
  - "[[estonia]]"
  - "[[denmark]]"
  - "[[italy]]"
  - "[[croatia]]"
  - "[[canada]]"
  - "[[chile]]"
  - "[[switzerland]]"
  - "[[moldova]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[eurojust]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[netherlands-politie|Dutch cybercrime authorities]]"
  - "[[belgium-federal-police|Belgian Federal Police]]"
  - "[[france-national-police|French cybercrime authorities]]"
  - "[[germany-bka|German cybercrime authorities]]"
  - "[[uk-nca|UK cybercrime authorities]]"
  - "[[denmark-national-police|Danish National Police]]"
  - "[[italy-polizia-postale|Italian Postal and Communications Police]]"
  - "[[canada-rcmp|Royal Canadian Mounted Police]]"
  - "[[switzerland-fedpol|Swiss Federal Office of Police]]"
legal_basis:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[eurojust-coordination-meeting]]"
results:
  arrests: 97
  indictments: 5
  servers_seized: 0
  domains_seized: 1901
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "The coordinated action involved 16 participating countries in Eurojust reporting and 18 other countries in FBI reporting."
    - "More than 90 arrests were reported by FBI and DOJ; Eurojust's evaluation reported 97 arrests."
    - "Eurojust reported 359 house searches worldwide."
    - "Authorities seized more than 1,100 data-storage devices, plus cash, firearms, and drugs."
    - "FBI reporting states that more than 1,900 domains used by Blackshades users were seized."
    - "Blackshades was sold to thousands of users in more than 100 countries and infected more than 500,000 computers worldwide."
    - "Alex Yucel, a Swedish national, was arrested in Moldova and later extradited to the United States."
edges:
  - source_actor: "FBI"
    target_actor: "Eurojust"
    cooperation_type: joint_investigation
    legal_basis: mutual_legal_assistance
    direction: undirected
  - source_actor: "Eurojust"
    target_actor: "Europol EC3"
    cooperation_type: coordination
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "FBI"
    target_actor: "Moldovan authorities"
    cooperation_type: extradition
    legal_basis: extradition
    direction: inbound
  - source_actor: "Eurojust"
    target_actor: "Participating national authorities"
    cooperation_type: parallel_enforcement
    legal_basis: mutual_legal_assistance
    direction: undirected
credibility_index: 4.3
source_tier: 1
missing_fields:
  - complete_country_by_country_arrest_breakdown
  - full_domain_inventory
  - full_final_outcomes_for_all_users
related_cases: []
related_operations:
  - "[[operation-tovar]]"
  - "[[operation-ghost-click]]"
  - "[[imminent-monitor-rat-takedown]]"
challenges_encountered:
  - "Participating investigations were at different stages and needed a common action date."
  - "Authorities had to distinguish criminal malware use from remote-access-tool ambiguity in some jurisdictions."
  - "The action required real-time cross-border coordination across searches, arrests, domain seizure, and evidence collection."
lessons_learned:
  - "Eurojust coordination centres can provide real-time judicial support during simultaneous cybercrime action days."
  - "Large malware-user sweeps require both upstream developer charges and downstream user enforcement."
  - "FBI-origin data can be operationalized across European investigations when judicial admissibility is handled early."
source_count: 5
sources:
  - "[[2014-05-19_fbi_blackshades-malware-takedown]]"
  - "[[2014-05-19_doj_blackshades-malware-charges]]"
  - "[[2015-01-01_eurojust_operation-blackshades-evaluation]]"
  - "[[2014-05-19_computerworld_blackshades-97-arrests]]"
  - "[[2015-06-23_fbi_blackshades-yucel-sentencing]]"
created: 2026-05-08
updated: 2026-05-08
operation_role: umbrella
parent_operation: ""
summary: "Operation Blackshades was a 2014 FBI-, Eurojust-, and Europol-supported international operation targeting creators, sellers, and users of the Blackshades Remote Access Tool. Official and contemporary sources report a 16-country Eurojust-coordinated action, more than 90 arrests, 359 house searches, more than 1,100 devices seized, more than 1,900 domains seized by FBI field offices, and a malware ecosystem that infected more than 500,000 computers worldwide."
jurisdictions:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[belgium]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[united-kingdom]]"
  - "[[finland]]"
  - "[[austria]]"
  - "[[estonia]]"
  - "[[denmark]]"
  - "[[italy]]"
  - "[[croatia]]"
  - "[[canada]]"
  - "[[chile]]"
  - "[[switzerland]]"
  - "[[moldova]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[eurojust]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[netherlands-politie|Dutch cybercrime authorities]]"
  - "[[belgium-federal-police|Belgian Federal Police]]"
  - "[[france-national-police|French cybercrime authorities]]"
  - "[[germany-bka|German cybercrime authorities]]"
  - "[[uk-nca|UK cybercrime authorities]]"
  - "[[denmark-national-police|Danish National Police]]"
  - "[[italy-polizia-postale|Italian Postal and Communications Police]]"
  - "[[canada-rcmp|Royal Canadian Mounted Police]]"
  - "[[switzerland-fedpol|Swiss Federal Office of Police]]"
crime_types:
  - "[[malware-ic]]"
  - "[[hacking-ic]]"
  - "[[ransomware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[online-fraud-ic]]"
---
## Summary

Operation Blackshades was a 2014 international cybercrime action targeting creators, sellers, and users of the Blackshades Remote Access Tool. Blackshades let users remotely control victims' computers, activate webcams, steal files and credentials, record keystrokes, and deploy ransomware-like extortion.

The operation qualifies as international cooperation because Eurojust describes a 16-state worldwide investigation coordinated through a Eurojust coordination centre and supported by Europol EC3, while FBI and DOJ reporting describe an unprecedented operation involving 18 other countries and more than 90 arrests.

## Operational Scope

The U.S. prosecutorial core focused on Blackshades owner Alex Yucel, co-developer Michael Hogue, administrators, marketers, and users. The international action also targeted purchasers and users identified in participating countries. Eurojust's evaluation states that the Netherlands opened a case in November 2013, Eurojust held coordination meetings, and a common two-day action was executed in May 2014.

Public sources report that Blackshades was sold to thousands of people in more than 100 countries and infected more than 500,000 computers worldwide. The operation also connected back to prior FBI work in Operation Cardshop, which helped identify Blackshades actors.

## Results

| Metric | Public figure |
|---|---:|
| Arrests | 90+ / 97 |
| House searches | 359 |
| Data-storage devices seized | 1,100+ |
| FBI-seized Blackshades user domains | 1,900+ |
| Infected computers | 500,000+ |
| Countries where Blackshades was sold | 100+ |

## Boundary Notes

This page is the canonical operation record for the 2014 Blackshades RAT takedown. It should remain separate from [[operation-tovar|Operation Tovar]], which targeted Gameover Zeus and CryptoLocker in June 2014, and from [[imminent-monitor-rat-takedown|Operation Imminent Monitor]], which targeted a later commercial RAT ecosystem.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2014-05-19_fbi_blackshades-malware-takedown|International Blackshades Malware Takedown]] | FBI | 2014-05-19 | https://www.fbi.gov/news/stories/international-blackshades-malware-takedown-1 |
| [2] | [[2014-05-19_doj_blackshades-malware-charges|Manhattan U.S. Attorney And FBI Assistant Director-In-Charge Announce Charges In Connection With Blackshades Malicious Software]] | U.S. Department of Justice | 2014-05-19 | https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-and-fbi-assistant-director-charge-announce-charges-connection |
| [3] | [[2015-01-01_eurojust_operation-blackshades-evaluation|Operation BlackShades: An Evaluation]] | Eurojust | 2015 | https://www.eurojust.europa.eu/publication/operation-blackshades-evaluation |
| [4] | [[2014-05-19_computerworld_blackshades-97-arrests|BlackShades users targeted in 16-nation sweep; 97 arrested]] | Computerworld | 2014-05-19 | https://www.computerworld.com/article/1509689/blackshades-users-targeted-in-16-nation-sweep-97-arrested.html |
| [5] | [[2015-06-23_fbi_blackshades-yucel-sentencing|Swedish Co-Creator of Blackshades Malware Sentenced to 57 Months in Prison]] | FBI | 2015-06-23 | https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/swedish-co-creator-of-blackshades-malware-that-enabled-users-around-the-world-to-secretly-and-remotely-control-victims-computers-sentenced-to-57-months-in-prison |
