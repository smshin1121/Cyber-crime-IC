---
type: operation
title: "Operation Open Market"
title_ko: "Operation Open Market"
aliases:
  - "Carder.su investigation"
  - "Carder.su takedown"
  - "Celtic undercover operation"
case_id: CYB-2012-001
period: 1
operation_type: joint-investigation
status: completed
enforcement_type:
  - undercover-investigation
  - arrest
  - indictment
  - extradition
outcome: success
timeframe:
  announced: 2012-03-16
  start: 2007-03
  end: 2015-12
  ongoing: false
crime_type: "[[carding-fraud-ic]]"
target_entity: "Carder.su identity-theft and carding organization"
lead_agency: "[[us-secret-service|US Secret Service]]"
coordinating_body: "[[us-secret-service|US Secret Service]]"
participating_countries:
  - "[[united-states]]"
  - "[[albania]]"
  - "[[austria]]"
  - "[[greece]]"
participating_agencies:
  - "[[us-secret-service|US Secret Service]]"
  - "ICE Homeland Security Investigations"
  - "Southwestern Identity Theft and Fraud Task Force"
  - "[[us-doj]]"
  - "[[office-of-international-affairs|DOJ Office of International Affairs]]"
  - "U.S. State Department Diplomatic Security Service"
  - "U.S. Marshals Service"
  - "HSI attaché office Vienna"
  - "HSI attaché office Athens"
  - "Austrian Department of Justice"
  - "Austrian Ministry of Interior"
  - "Albanian National Police"
  - "Interpol Tirana"
legal_basis:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[extradition]]"
  - "[[mutual-legal-assistance]]"
  - "[[public-private-cooperation]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[extradition]]"
  - "[[mutual-legal-assistance]]"
  - "[[public-private-cooperation]]"
  - "[[informal-cooperation]]"
results:
  arrests: 19
  indictments: 56
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Initial March 2012 enforcement produced 19 arrests in nine U.S. states."
    - "Four separate indictments ultimately charged 55 to 56 defendants, depending on the public reporting date."
    - "DOJ reported 33 convictions by December 2015."
    - "Carder.su had an estimated 5,500 members in July 2011."
    - "The forums were generally hosted within the former Soviet Union and senior members were described as residing there."
    - "Jordan Georgievski, a Macedonian national, was detained by Albanian authorities and extradited to the United States in January 2015."
    - "Some convicted defendants were ordered to pay USD 50.8 million in restitution."
edges:
  - source_actor: "US Secret Service"
    target_actor: "ICE Homeland Security Investigations"
    cooperation_type: joint_investigation
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "DOJ Office of International Affairs"
    target_actor: "Albanian National Police"
    cooperation_type: extradition
    legal_basis: extradition
    direction: inbound
  - source_actor: "HSI attaché offices"
    target_actor: "Austrian authorities"
    cooperation_type: investigative_support
    legal_basis: mutual_legal_assistance
    direction: undirected
  - source_actor: "Interpol Tirana"
    target_actor: "US authorities"
    cooperation_type: fugitive_location
    legal_basis: extradition
    direction: inbound
credibility_index: 4.1
source_tier: 1
missing_fields:
  - complete_defendant_country_list
  - full_foreign_law_enforcement_roster_for_initial_indictments
  - final_outcomes_for_remaining_fugitives
related_cases: []
related_operations:
  - "[[operation-firewall]]"
  - "[[operation-phish-phry]]"
  - "[[operation-trident-breach]]"
  - "[[infraud-organization-takedown]]"
  - "[[carding-action-2020]]"
challenges_encountered:
  - "Carder.su used screening procedures to prevent law-enforcement infiltration and rival access."
  - "Senior Carder.su members and forum infrastructure were described as outside the United States."
  - "The operation generated large multi-defendant RICO proceedings and years of follow-on extradition and sentencing activity."
lessons_learned:
  - "Long-running undercover identities can expose trust structures inside carding forums."
  - "International fugitive recovery remains essential when cybercrime defendants operate from or transit through multiple jurisdictions."
  - "RICO-style charging can be used to frame online carding forums as organized cybercrime enterprises."
source_count: 4
sources:
  - "[[2012-03-16_secret-service_operation-open-market]]"
  - "[[2015-01-11_ice_georgievski-open-market-extradition]]"
  - "[[2015-12-09_doj_operation-open-market-sentencing]]"
  - "[[2013-07-22_wired_operation-open-market]]"
created: 2026-05-08
updated: 2026-05-08
operation_role: umbrella
parent_operation: ""
summary: "Operation Open Market was a long-running HSI and US Secret Service undercover investigation into the Carder.su carding organization. Public sources describe the case as a transnational organized cybercrime investigation that produced 19 initial arrests, four indictments charging 55 to 56 defendants, later convictions and sentencings, and a 2015 extradition from Albania coordinated through HSI attaché offices, DOJ OIA, Austrian and Albanian authorities, and Interpol Tirana."
jurisdictions:
  - "[[united-states]]"
  - "[[albania]]"
  - "[[austria]]"
  - "[[greece]]"
organizations:
  - "[[us-secret-service|US Secret Service]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs|DOJ Office of International Affairs]]"
crime_types:
  - "[[carding-fraud-ic]]"
  - "[[identity-theft]]"
  - "[[access-device-fraud]]"
  - "[[cybercrime-forum-ic]]"
  - "[[online-fraud-ic]]"
---
## Summary

Operation Open Market was a long-running undercover investigation into Carder.su, an online carding organization whose members traded compromised payment-card data, counterfeit identification documents, money-laundering services, and other cybercrime services. The operation began in 2007 and the first public indictment and arrest wave was announced in March 2012.

The operation qualifies as international cooperation because Carder.su was a transnational organization, later public reporting described defendants across multiple countries, and ICE's 2015 extradition release documents coordination with Albanian, Austrian, Greek-based HSI attaché, DOJ, State Department, and Interpol channels to bring a Macedonian defendant from Albania to the United States.

## Operational Scope

Secret Service reporting describes Operation Open Market as an investigation into a transnational organized-crime group operating across cyber platforms. Members bought and sold stolen personal and financial information through online forums and used those forums to trade counterfeit identification documents, stolen credit-card data, money-laundering services, and related fraud tools.

DOJ later described Carder.su as a forum-based organization with an estimated 5,500 members in July 2011. The organization used member-vetting procedures and role separation among moderators, reviewers, vendors, and buyers to reduce infiltration risk.

## Results

| Metric | Public figure |
|---|---:|
| Initial arrests announced in March 2012 | 19 |
| Persons charged across four indictments | 55-56 |
| Convictions reported by December 2015 | 33 |
| Estimated Carder.su members in July 2011 | 5,500 |
| Restitution ordered in several sentencings | USD 50.8M |

## Boundary Notes

This page is the canonical operation record for Operation Open Market and the Carder.su undercover/RICO investigation. It should remain separate from [[operation-firewall|Operation Firewall]], which targeted Shadowcrew, CarderPlanet, and Darkprofits in 2003-2004, and from [[infraud-organization-takedown|Infraud Organization Takedown]], which involved a later and distinct cybercrime marketplace.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2012-03-16_secret-service_operation-open-market|U.S. Secret Service's Operation Open Market Nets 19 Arrests]] | U.S. Secret Service | 2012-03-16 | https://www.secretservice.gov/press/releases/2012/03/us-secret-services-operation-open-market-nets-19-arrests |
| [2] | [[2015-01-11_ice_georgievski-open-market-extradition|Defendant in massive credit card and identity theft scheme extradited from Albania]] | ICE | 2015-01-11 | https://www.ice.gov/news/releases/defendant-massive-credit-card-and-identity-theft-scheme-extradited-albania |
| [3] | [[2015-12-09_doj_operation-open-market-sentencing|Defendant in Operation Open Market Sentenced]] | U.S. Department of Justice | 2015-12-09 | https://www.justice.gov/usao-nv/pr/defendant-operation-open-market-sentenced |
| [4] | [[2013-07-22_wired_operation-open-market|The Secret Service Agent Who Collared Cybercrooks by Selling Them Fake IDs]] | Wired | 2013-07-22 | https://www.wired.com/2013/07/open-market/ |
