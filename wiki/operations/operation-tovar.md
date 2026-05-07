---
type: operation
title: "Operation Tovar"
title_ko: "Operation Tovar"
aliases:
  - "Gameover Zeus disruption"
  - "GameOver Zeus disruption"
  - "CryptoLocker disruption"
case_id: CYB-2014-001
period: 1
operation_type: takedown
status: completed
enforcement_type:
  - infrastructure-disruption
  - indictment
  - sinkholing
  - victim-remediation
outcome: success
timeframe:
  announced: 2014-06-02
  start: 2014-05-30
  end: 2014-07-11
  ongoing: false
crime_type: "[[malware-ic]]"
target_entity: "Gameover Zeus botnet and CryptoLocker command-and-control infrastructure"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[netherlands]]"
  - "[[germany]]"
  - "[[france]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[luxembourg]]"
  - "[[new-zealand]]"
  - "[[canada]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[office-of-international-affairs|DOJ Office of International Affairs]]"
  - "DHS NCCIC / US-CERT"
  - "[[uk-nca|UK National Crime Agency]]"
  - "Australian Federal Police"
  - "[[netherlands-politie|Dutch National High Tech Crime Unit]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[germany-bka|Germany BKA]]"
  - "[[france-national-police|French Judicial Police]]"
  - "[[italy-polizia-postale|Italian Postal and Communications Police]]"
  - "[[japan-npa|Japan National Police Agency]]"
  - "Luxembourg Grand Ducal Police"
  - "New Zealand Police"
  - "[[canada-rcmp|Royal Canadian Mounted Police]]"
  - "[[ukraine-police|Ukraine Ministry of Internal Affairs cybercrime unit]]"
  - "[[shadowserver|Shadowserver Foundation]]"
  - "[[microsoft|Microsoft]]"
legal_basis:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[sinkholing]]"
  - "[[public-private-cooperation]]"
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[sinkholing]]"
  - "[[public-private-cooperation]]"
  - "[[mutual-legal-assistance]]"
results:
  arrests: 0
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Gameover Zeus infections were estimated at 500,000 to 1 million computers worldwide."
    - "The FBI estimated Gameover Zeus losses at more than USD 100 million."
    - "CryptoLocker infections were estimated at more than 234,000 computers as of April 2014."
    - "DOJ reported more than USD 27 million in CryptoLocker ransom payments during its first two months."
    - "Court-authorized sinkholing redirected infected computers away from criminal command infrastructure to substitute servers."
    - "By July 2014, DOJ reported all or nearly all active Gameover Zeus computers had been liberated from criminal control."
    - "Remediation reduced Gameover Zeus infections by 31 percent after disruption began."
    - "CryptoLocker was neutralized and unable to communicate with its control infrastructure."
edges:
  - source_actor: "FBI"
    target_actor: "UK National Crime Agency"
    cooperation_type: joint_investigation
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "FBI"
    target_actor: "Europol EC3"
    cooperation_type: info_sharing
    legal_basis: mutual_legal_assistance
    direction: undirected
  - source_actor: "FBI"
    target_actor: "Foreign law enforcement partners"
    cooperation_type: parallel_enforcement
    legal_basis: mutual_legal_assistance
    direction: undirected
  - source_actor: "FBI"
    target_actor: "Shadowserver Foundation"
    cooperation_type: technical_assistance
    legal_basis: public_private_cooperation
    direction: inbound
  - source_actor: "US-CERT"
    target_actor: "International CERTs"
    cooperation_type: victim_notification
    legal_basis: public_private_cooperation
    direction: outbound
credibility_index: 4.4
source_tier: 1
missing_fields:
  - exact_number_of_servers_seized
  - exact_number_of_domains_redirected_or_seized
  - final_custody_status_of_evgeniy_bogachev
related_cases: []
related_operations:
  - "[[operation-trident-breach]]"
  - "[[operation-ghost-click]]"
  - "[[operation-avalanche]]"
  - "[[emotet-takedown]]"
  - "[[operation-endgame-phase1]]"
challenges_encountered:
  - "Gameover Zeus used decentralized peer-to-peer command-and-control, making a conventional server takedown insufficient."
  - "CryptoLocker infrastructure had to be disrupted without harming already-infected victims."
  - "Victim remediation required rapid data sharing among law enforcement, CERTs, ISPs, and private security companies."
lessons_learned:
  - "Botnet disruption can combine criminal charges, civil injunctions, sinkholing, and public-private remediation."
  - "Court-authorized substitute servers can prevent recontact with criminal infrastructure while preserving victim privacy boundaries."
  - "International CERT distribution is a practical follow-through mechanism after a technical takedown."
source_count: 5
sources:
  - "[[2014-06-02_doj_operation-tovar-gameover-zeus]]"
  - "[[2014-06-02_fbi_gameover-zeus-botnet-disrupted]]"
  - "[[2014-07-11_doj_gameover-zeus-cryptolocker-update]]"
  - "[[2014-06-08_shadowserver_operation-tovar]]"
  - "[[2014-06-02_arstechnica_operation-tovar]]"
created: 2026-05-08
updated: 2026-05-08
operation_role: umbrella
parent_operation: ""
summary: "Operation Tovar was the 2014 multinational disruption of the Gameover Zeus botnet and CryptoLocker ransomware infrastructure. DOJ and FBI sources document the court-authorized sinkholing, criminal charges against Evgeniy Bogachev, more than USD 100 million in Gameover Zeus losses, CryptoLocker server seizures, and participation by law enforcement from more than 10 countries; Shadowserver and Ars Technica identify the public codename Operation Tovar."
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[netherlands]]"
  - "[[germany]]"
  - "[[france]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[luxembourg]]"
  - "[[new-zealand]]"
  - "[[canada]]"
  - "[[ukraine]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[office-of-international-affairs|DOJ Office of International Affairs]]"
  - "[[uk-nca|UK National Crime Agency]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[netherlands-politie|Dutch National High Tech Crime Unit]]"
  - "[[germany-bka|Germany BKA]]"
  - "[[france-national-police|French Judicial Police]]"
  - "[[italy-polizia-postale|Italian Postal and Communications Police]]"
  - "[[japan-npa|Japan National Police Agency]]"
  - "[[canada-rcmp|Royal Canadian Mounted Police]]"
  - "[[ukraine-police|Ukraine cybercrime police]]"
  - "[[shadowserver|Shadowserver Foundation]]"
  - "[[microsoft|Microsoft]]"
crime_types:
  - "[[malware-ic]]"
  - "[[banking-trojan-ic]]"
  - "[[ransomware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[online-fraud-ic]]"
---
## Summary

Operation Tovar was the 2014 multinational disruption of the Gameover Zeus botnet and CryptoLocker ransomware infrastructure. DOJ and FBI announcements describe a coordinated legal and technical action that used court-authorized substitute servers to redirect infected computers away from criminal control while foreign law-enforcement partners and private-sector specialists helped disrupt related command infrastructure and support victim remediation.

The operation qualifies as international cooperation because DOJ identified participating law-enforcement partners from Australia, the Netherlands, Europol EC3, Germany, France, Italy, Japan, Luxembourg, New Zealand, Canada, Ukraine, and the United Kingdom, alongside the United States. Shadowserver also identifies the public codename as Operation Tovar and describes it as a joint effort among FBI, UK NCA, Europol EC3, and multiple private partners.

## Operational Scope

Gameover Zeus was a peer-to-peer banking trojan used to steal banking credentials and redirect wire transfers. Its decentralized structure made the botnet harder to disrupt than earlier Zeus variants. CryptoLocker was ransomware that encrypted victims' files and demanded payment for decryption; DOJ treated the CryptoLocker server seizures as a related but distinct action tied to the same criminal ecosystem.

The disruption combined criminal charges against Evgeniy Bogachev, civil and criminal court orders, sinkholing, server seizures, CERT-based notification, and private-sector remediation support. DOJ later reported that the technical and legal measures had been successful and that CryptoLocker could no longer communicate with its control infrastructure.

## Results

| Metric | Public figure |
|---|---:|
| Gameover Zeus infections | 500,000-1,000,000 |
| Estimated Gameover Zeus losses | USD 100M+ |
| CryptoLocker infections | 234,000+ |
| Early CryptoLocker ransom payments | USD 27M+ |
| Gameover Zeus infection reduction after disruption | 31% |
| Named defendant charged | 1 |

## Boundary Notes

This page is the canonical operation record for the 2014 Gameover Zeus and CryptoLocker disruption known as Operation Tovar. It should remain separate from [[operation-trident-breach|Operation Trident Breach]], which concerned earlier Zeus/Jabber Zeus enforcement, and from later malware takedowns such as [[operation-avalanche|Operation Avalanche]], [[emotet-takedown|Emotet takedown]], and [[operation-endgame-phase1|Operation Endgame]].

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2014-06-02_doj_operation-tovar-gameover-zeus|U.S. Leads Multi-National Action Against Gameover Zeus Botnet and Cryptolocker Ransomware]] | U.S. Department of Justice | 2014-06-02 | https://www.justice.gov/opa/pr/us-leads-multi-national-action-against-gameover-zeus-botnet-and-cryptolocker-ransomware |
| [2] | [[2014-06-02_fbi_gameover-zeus-botnet-disrupted|GameOver Zeus Botnet Disrupted]] | FBI | 2014-06-02 | https://www.fbi.gov/news/stories/gameover-zeus-botnet-disrupted |
| [3] | [[2014-07-11_doj_gameover-zeus-cryptolocker-update|Department of Justice Provides Update on Gameover Zeus and Cryptolocker Disruption]] | U.S. Department of Justice | 2014-07-11 | https://www.justice.gov/archives/opa/pr/department-justice-provides-update-gameover-zeus-and-cryptolocker-disruption |
| [4] | [[2014-06-08_shadowserver_operation-tovar|Gameover Zeus & Cryptolocker]] | Shadowserver Foundation | 2014-06-08 | https://www.shadowserver.org/news/gameover-zeus-cryptolocker/ |
| [5] | [[2014-06-02_arstechnica_operation-tovar|Governments disrupt botnet Gameover ZeuS and ransomware Cryptolocker]] | Ars Technica | 2014-06-02 | https://arstechnica.com/tech-policy/2014/06/governments-disrupt-botnet-gameover-zeus-and-ransomware-cryptolocker/ |
