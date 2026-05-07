---
type: operation
title: "Operation Cookie Monster"
title_ko: "Operation Cookie Monster (Genesis Market takedown)"
aliases:
  - "Genesis Market takedown"
  - "Genesis Market disruption"
case_id: CYB-2023-054
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - arrest
  - search-and-seizure
  - victim-notification
outcome: success
timeframe:
  announced: 2023-04-05
  start: 2019
  end: 2023-04-04
  ongoing: false
crime_type: "[[identity-theft]]"
target_entity: "Genesis Market"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[estonia]]"
  - "[[finland]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[new-zealand]]"
  - "[[poland]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[switzerland]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust]]"
  - "[[netherlands-politie|Dutch National Police]]"
  - "[[uk-nca|UK National Crime Agency]]"
  - "[[australia-afp|Australian Federal Police]]"
  - "[[canada-rcmp|Royal Canadian Mounted Police]]"
  - "[[germany-bka|German Federal Criminal Police Office]]"
  - "[[spain-guardia-civil|Spanish Civil Guard]]"
  - "[[sweden-police|Swedish Police Authority]]"
  - "[[switzerland-fedpol|Swiss Federal Police]]"
  - "[[romania-police|Romanian Police]]"
legal_basis:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[electronic-evidence]]"
mechanisms_used:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[electronic-evidence]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 119
  indictments: 0
  servers_seized: 0
  domains_seized: 11
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Genesis Market infrastructure seized on 4 April 2023"
    - "119 arrests, 208 property searches, and 97 knock-and-talk measures reported by Europol"
    - "11 domain names seized under a U.S. District Court warrant in the Eastern District of Wisconsin"
    - "Genesis Market offered access credentials from more than 1.5 million compromised computers and more than 80 million account credentials"
    - "At takedown, Genesis Market listed more than 1.5 million bot listings totaling more than 2 million identities"
    - "Victim credentials were provided to Have I Been Pwned and Dutch Police victim-checking services"
edges:
  - source_actor: "FBI"
    target_actor: "Dutch National Police"
    cooperation_type: joint_investigation
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: "Participating national authorities"
    cooperation_type: operational_coordination
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "Eurojust"
    target_actor: "Participating judicial authorities"
    cooperation_type: judicial_coordination
    legal_basis: mutual_legal_assistance
    direction: undirected
  - source_actor: "US DOJ"
    target_actor: "Bulgaria and Latvia"
    cooperation_type: mutual_legal_assistance
    legal_basis: mutual_legal_assistance
    direction: outbound
credibility_index: 4.5
source_tier: 1
missing_fields:
  - administrator_identity_and_arrest_status
  - complete_country_level_arrest_breakdown
related_cases:
  - "[[monroeville-man-sentenced-to-24-months-for-purchasing-hundreds-of-stolen-log-in-credentials-off-the-darkweb]]"
  - "[[us-v-monroeville-man]]"
  - "[[us-v-andrew-shenkosky]]"
related_operations:
  - "[[operation-monroeville-man-sentenced-to-24-months-for-purchasing-hundreds-of-stolen-log-in-credentials-off-the-darkweb]]"
  - "[[operation-us-v-monroeville-man]]"
  - "[[operation-us-v-andrew-shenkosky]]"
challenges_encountered:
  - "Genesis Market operated as both a dark-web and clear-web marketplace, reducing friction for criminal users."
  - "The marketplace sold browser fingerprints and cookies that let buyers impersonate victims without triggering normal fraud controls."
  - "The user base and victim credentials were distributed globally, requiring parallel enforcement and victim-notification channels."
lessons_learned:
  - "Credential-market takedowns can generate both infrastructure disruption and user-focused enforcement at the same time."
  - "A command-post model at Europol can support parallel action days when searches and arrests occur across many jurisdictions."
  - "Victim-notification partnerships such as Have I Been Pwned and national police portals can convert seized credential data into remediation."
source_count: 4
sources:
  - "[[2023-04-05_justice-gov_criminal-marketplace-disrupted-genesis-market]]"
  - "[[2023-04-05_eurojust_operation-cookie-monster-genesis-market]]"
  - "[[2023-04-05_europol_operation-cookie-monster-genesis-market]]"
  - "[[2023-04-04_bleepingcomputer_fbi-seizes-stolen-credentials-market-genesis-in-operation-cookie-monster]]"
created: 2026-05-07
updated: 2026-05-07
operation_role: umbrella
parent_operation: ""
summary: "Operation Cookie Monster was the April 2023 FBI- and Dutch Police-led takedown of Genesis Market, a credential and browser-fingerprint marketplace used for account takeover, fraud, and ransomware-enabling access. Official DOJ, Eurojust, and Europol materials show a multi-country operation involving at least 17 countries, Europol, Eurojust, more than 100 arrests, more than 200 searches, and the seizure of 11 domains supporting Genesis Market infrastructure."
jurisdictions:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[estonia]]"
  - "[[finland]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[new-zealand]]"
  - "[[poland]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[switzerland]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust]]"
  - "[[netherlands-politie|Dutch National Police]]"
  - "[[uk-nca|UK National Crime Agency]]"
  - "[[australia-afp|Australian Federal Police]]"
  - "[[canada-rcmp|Royal Canadian Mounted Police]]"
  - "[[germany-bka|German Federal Criminal Police Office]]"
  - "[[spain-guardia-civil|Spanish Civil Guard]]"
  - "[[sweden-police|Swedish Police Authority]]"
  - "[[switzerland-fedpol|Swiss Federal Police]]"
  - "[[romania-police|Romanian Police]]"
crime_types:
  - "[[identity-theft]]"
  - "[[dark-web-ic]]"
  - "[[malware-ic]]"
  - "[[online-fraud-ic]]"
  - "[[ransomware-ic]]"
---
## Summary

Operation Cookie Monster was the April 2023 takedown of Genesis Market, a marketplace selling stolen credentials, cookies, and browser fingerprints from malware-infected or otherwise compromised devices. The operation is a distinct international-cooperation record because official sources identify the FBI and Dutch National Police as operational leads, Europol and Eurojust as coordination bodies, and law enforcement or judicial authorities across 17 countries.

The action combined infrastructure seizure with user-focused enforcement. DOJ reports that U.S. authorities seized 11 domains supporting Genesis Market pursuant to a warrant from the Eastern District of Wisconsin. Europol's public-information release reports 119 arrests, 208 property searches, and 97 knock-and-talk measures after a coordinated action day on 4 April 2023.

## Operational Scope

Genesis Market's significance came from the way it packaged stolen identities for immediate reuse. Buyers could purchase credentials, cookies, autofill data, and browser fingerprints, then use a custom browser profile to impersonate the victim and bypass fraud checks based on device or location.

The marketplace had operated since 2018. DOJ states that it offered access to data from more than 1.5 million compromised computers and more than 80 million account credentials. Europol's release adds that, at takedown, Genesis Market listed more than 1.5 million bot listings totaling more than 2 million identities.

## Cooperation Model

The operation used a three-layer cooperation model:

| Layer | Evidence in sources |
|---|---|
| Operational lead | FBI and Dutch National Police led the international sweep |
| Police coordination | Europol EC3 supported the investigation since 2019, organized operational meetings, facilitated information exchange, and ran an action-day command post in The Hague |
| Judicial coordination | Eurojust facilitated cross-border judicial cooperation, hosted a March 2023 coordination meeting, and supported parallel operations in 13 countries |

DOJ also records mutual legal assistance from Bulgaria and Latvia, showing that the operation was not merely informal information sharing but included formal cross-border evidence channels.

## Results

| Metric | Public figure |
|---|---:|
| Arrests | 119 |
| Property searches | 208 |
| Knock-and-talk measures | 97 |
| Domains seized | 11 |
| Participating countries | 17 |
| Compromised computers referenced by DOJ | 1.5M+ |
| Account credentials referenced by DOJ | 80M+ |
| Bot listings referenced by Europol | 1.5M+ |
| Identities referenced by Europol | 2M+ |

Victim remediation was part of the public action. DOJ provided credentials to Have I Been Pwned, and Dutch Police maintained a checkyourhack portal so potential victims could check whether their credentials appeared in Genesis Market data.

## Boundary Notes

This page is the canonical operation record for the Genesis Market takedown itself. Later U.S. prosecutions involving Genesis Market users, including the Odom and Shenkosky matters, should remain downstream case or follow-on operation records unless their sources independently document new multi-country action.

Operation Cookie Monster is also distinct from marketplace takedowns such as [[xdedic-marketplace-takedown|xDedic]], [[alphabay-takedown|Operation Bayonet]], and [[darkmarket-takedown|DarkMarket]]. Those operations also targeted criminal marketplaces, but their infrastructure, dates, countries, and evidentiary records differ.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2023-04-05_justice-gov_criminal-marketplace-disrupted-genesis-market|Criminal Marketplace Disrupted in International Cyber Operation]] | US DOJ | 2023-04-05 | https://www.justice.gov/archives/opa/pr/criminal-marketplace-disrupted-international-cyber-operation |
| [2] | [[2023-04-05_eurojust_operation-cookie-monster-genesis-market|Online market selling stolen account credentials to criminals worldwide taken down in multi-country effort dubbed Operation Cookie Monster]] | Eurojust | 2023-04-05 | https://www.eurojust.europa.eu/news/takedown-online-market-sold-stolen-account-credentials-Operation-Cookie-Monster |
| [3] | [[2023-04-05_europol_operation-cookie-monster-genesis-market|Takedown of notorious hacker marketplace selling your identity to criminals]] | Europol | 2023-04-05 | https://www.europol.europa.eu/media-press/newsroom/news/takedown-of-notorious-hacker-marketplace-selling-your-identity-to-criminals |
| [4] | [[2023-04-04_bleepingcomputer_fbi-seizes-stolen-credentials-market-genesis-in-operation-cookie-monster|FBI seizes stolen credentials market Genesis in Operation Cookie Monster]] | BleepingComputer | 2023-04-04 | https://www.bleepingcomputer.com/news/security/fbi-seizes-stolen-credentials-market-genesis-in-operation-cookie-monster/ |
