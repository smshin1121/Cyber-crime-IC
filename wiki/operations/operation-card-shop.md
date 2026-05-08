---
type: operation
title: "Operation Card Shop"
title_ko: "Operation Card Shop"
aliases:
  - "Carder Profit undercover forum"
  - "Card Shop carding takedown"
case_id: CYB-2012-002
period: 1
operation_type: arrest-sweep
status: completed
enforcement_type:
  - undercover-investigation
  - arrest
  - indictment
  - search-seizure
  - extradition-request
outcome: success
timeframe:
  announced: 2012-06-26
  start: 2010-06
  end: 2012-07
  ongoing: false
crime_type: "[[carding-fraud-ic]]"
target_entity: "Carder Profit undercover carding forum and related carding actors"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[bosnia-and-herzegovina]]"
  - "[[bulgaria]]"
  - "[[norway]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[macedonia]]"
  - "[[india]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "FBI New York Cyber Crime Task Force"
  - "United Kingdom law enforcement"
  - "Bosnia and Herzegovina law enforcement"
  - "[[bulgaria-police|Bulgarian law enforcement]]"
  - "[[norway-kripos|Norwegian law enforcement]]"
  - "[[germany-bka|German law enforcement]]"
  - "[[italy-polizia-postale|Italian law enforcement]]"
  - "[[japan-npa|Japanese law enforcement]]"
  - "Australian law enforcement"
  - "[[canada-rcmp|Canadian law enforcement]]"
  - "[[denmark-national-police|Danish law enforcement]]"
  - "Macedonian Ministry of Interior"
  - "Indian authorities"
legal_basis:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[public-private-cooperation]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 27
  indictments: 28
  servers_seized: 1
  domains_seized: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Initial 26 June 2012 action produced 24 arrests: 11 in the United States and 13 abroad."
    - "DOJ follow-up reported three additional arrests, bringing total arrests to 27."
    - "The initial coordinated action involved 13 countries, including the United States."
    - "Authorities executed more than 30 search warrants and conducted more than 30 subject interviews."
    - "The FBI notified card providers of more than 411,000 compromised credit and debit cards."
    - "The operation notified 47 companies, government entities, and educational institutions of network breaches."
    - "The undercover operation prevented estimated potential economic losses of more than USD 205 million."
    - "The FBI seized the UGNazi.com web server and the Carders.org domain in related U.S. action."
edges:
  - source_actor: "FBI"
    target_actor: "Foreign law enforcement partners"
    cooperation_type: parallel_enforcement
    legal_basis: mutual_legal_assistance
    direction: undirected
  - source_actor: "FBI"
    target_actor: "Card providers and victim institutions"
    cooperation_type: victim_notification
    legal_basis: public_private_cooperation
    direction: outbound
  - source_actor: "US DOJ"
    target_actor: "Indian authorities"
    cooperation_type: extradition
    legal_basis: extradition
    direction: inbound
  - source_actor: "US DOJ"
    target_actor: "Canadian authorities"
    cooperation_type: extradition
    legal_basis: extradition
    direction: inbound
credibility_index: 4.1
source_tier: 1
missing_fields:
  - complete_13_country_roster_from_official_chart
  - final_extradition_outcomes_for_all_foreign_arrests
  - complete_domain_and_server_inventory
related_cases: []
related_operations:
  - "[[operation-open-market]]"
  - "[[operation-firewall]]"
  - "[[operation-blackshades]]"
  - "[[operation-phish-phry]]"
challenges_encountered:
  - "The FBI-operated undercover forum needed to preserve evidence from private messages, postings, and IP logs while limiting entrapment concerns."
  - "Foreign arrests, interviews, and searches occurred across several countries with different procedural requirements."
  - "Victim mitigation required notifying card providers and breached entities before or alongside public enforcement."
lessons_learned:
  - "Undercover criminal forums can identify carders, malware sellers, drop-service providers, and fraud facilitators in one operation."
  - "Cybercrime carding cases benefit from simultaneous foreign action so suspects cannot warn each other or migrate platforms."
  - "Operational value includes harm prevention, not only arrests, when compromised payment cards and breach victims are notified."
source_count: 5
sources:
  - "[[2012-06-26_fbi_operation-card-shop]]"
  - "[[2012-06-26_doj_operation-card-shop]]"
  - "[[2012-07-13_doj_operation-card-shop-followup]]"
  - "[[2012-06-26_wired_operation-card-shop]]"
  - "[[2012-06-26_computerworld_operation-card-shop]]"
created: 2026-05-08
updated: 2026-05-08
operation_role: umbrella
parent_operation: ""
summary: "Operation Card Shop was a two-year FBI undercover carding investigation using the Carder Profit forum. Official sources describe the June 2012 coordinated action as involving 13 countries, 24 initial arrests, more than 30 search warrants, more than 30 interviews, notification of more than 411,000 compromised payment cards, and prevention of more than USD 205 million in potential losses; a July 2012 DOJ follow-up raised the arrest total to 27."
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[bosnia-and-herzegovina]]"
  - "[[bulgaria]]"
  - "[[norway]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[macedonia]]"
  - "[[india]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[bulgaria-police|Bulgarian law enforcement]]"
  - "[[norway-kripos|Norwegian law enforcement]]"
  - "[[germany-bka|German law enforcement]]"
  - "[[italy-polizia-postale|Italian law enforcement]]"
  - "[[japan-npa|Japanese law enforcement]]"
  - "[[canada-rcmp|Canadian law enforcement]]"
  - "[[denmark-national-police|Danish law enforcement]]"
crime_types:
  - "[[carding-fraud-ic]]"
  - "[[access-device-fraud]]"
  - "[[identity-theft]]"
  - "[[cybercrime-forum-ic]]"
  - "[[online-fraud-ic]]"
---
## Summary

Operation Card Shop was a two-year FBI undercover carding investigation built around an FBI-operated forum called Carder Profit. The forum allowed investigators to record posts, private messages, registration data, and IP addresses from users trading stolen payment-card data, counterfeit documents, hacked account information, malware, and drop services.

The operation qualifies as international cooperation because the initial June 2012 action involved 13 countries, including the United States, with 11 U.S. arrests and 13 foreign arrests across seven countries. Additional countries conducted interviews, searches, or other coordinated action, and a July 2012 DOJ follow-up reported additional arrests in India, Canada, and the United States.

## Operational Scope

The operation targeted the carding ecosystem rather than one single marketplace operator. The FBI created Carder Profit in June 2010 to identify cybercriminals, investigate their conduct, and prevent harm to victims. The undercover site was taken offline in May 2012, and the public action followed on 26 June 2012.

The case covered stolen credit and debit cards, identity data, counterfeit documents, hacking tools, malware, drop services, and related online fraud schemes. Official sources state that the FBI notified card providers of more than 411,000 compromised payment cards and notified 47 organizations of network breaches discovered during the operation.

## Results

| Metric | Public figure |
|---|---:|
| Initial arrests | 24 |
| Follow-up total arrests | 27 |
| Countries in initial coordinated action | 13 |
| Search warrants | 30+ |
| Subject interviews | 30+ |
| Compromised cards notified | 411,000+ |
| Potential losses prevented | USD 205M+ |

## Boundary Notes

This page is the canonical operation record for the 2010-2012 FBI undercover carding operation known as Operation Card Shop. It should remain separate from [[operation-firewall|Operation Firewall]], which targeted Shadowcrew/CarderPlanet/Darkprofits in 2004, [[operation-open-market|Operation Open Market]], which targeted Carder.su, and [[operation-blackshades|Operation Blackshades]], which later used investigative leads from this operation.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2012-06-26_fbi_operation-card-shop|Manhattan U.S. Attorney and FBI Assistant Director in Charge Announce 24 Arrests in Eight Countries as Part of International Cyber Crime Takedown]] | FBI | 2012-06-26 | https://archives.fbi.gov/archives/newyork/press-releases/2012/manhattan-u.s.-attorney-and-fbi-assistant-director-in-charge-announce-24-arrests-in-eight-countries-as-part-of-international-cyber-crime-takedown |
| [2] | [[2012-06-26_doj_operation-card-shop|Manhattan U.S. Attorney And FBI Assistant Director-In-Charge Announce 24 Arrests In Eight Countries As Part Of International Cyber Crime Takedown]] | U.S. Department of Justice | 2012-06-26 | https://www.justice.gov/archive/usao/nys/pressreleases/June12/cardshoparrests.html |
| [3] | [[2012-07-13_doj_operation-card-shop-followup|Manhattan U.S. Attorney And FBI Assistant Director-In-Charge Announce Three Additional Arrests In Operation Card Shop]] | U.S. Department of Justice | 2012-07-13 | https://www.justice.gov/archive/usao/nys/pressreleases/July12/cardshopfollowup.html |
| [4] | [[2012-06-26_wired_operation-card-shop|Feds Arrest 24 in Global Carding Ring Bust]] | Wired | 2012-06-26 | https://www.wired.com/2012/06/operation-card-shop/ |
| [5] | [[2012-06-26_computerworld_operation-card-shop|24 arrested in international online carding crackdown]] | Computerworld | 2012-06-26 | https://www.computerworld.com/article/1548676/24-arrested-in-international-online-carding-crackdown.html |
