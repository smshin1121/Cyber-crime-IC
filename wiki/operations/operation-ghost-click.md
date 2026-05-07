---
type: operation
title: "Operation Ghost Click"
title_ko: "Operation Ghost Click (DNSChanger)"
aliases:
  - "DNSChanger takedown"
  - "Rove Digital takedown"
case_id: CYB-2011-001
period: 1
operation_type: botnet-disruption
status: completed
enforcement_type:
  - arrest
  - indictment
  - infrastructure-disruption
  - extradition
outcome: success
timeframe:
  announced: 2011-11-09
  start: 2009
  end: 2014
  ongoing: false
crime_type: "[[malware-ic]]"
target_entity: "DNSChanger / Rove Digital advertising-fraud infrastructure"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[fbi-cyber-division|FBI]]"
participating_countries:
  - "[[united-states]]"
  - "[[estonia]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "FBI New York"
  - "NASA Office of Inspector General"
  - "Estonian Police and Border Guard Board"
  - "[[netherlands-politie|Dutch National Police]]"
legal_basis:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[search-seizure]]"
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 6
  indictments: 7
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "DNSChanger infected more than 4 million computers worldwide"
    - "More than 500,000 infected computers were in the United States"
    - "Fraudulent advertising revenue was estimated at more than USD 14 million"
    - "Six Estonian nationals were arrested in Estonia; one Russian defendant remained at large in initial public reporting"
    - "FBI later reported that three Estonian nationals were extradited to the United States in November 2013"
    - "Temporary clean DNS service was deployed to avoid disconnecting infected users during remediation"
edges:
  - source_actor: "FBI"
    target_actor: "Estonian Police and Border Guard Board"
    cooperation_type: joint_investigation
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "FBI"
    target_actor: "Dutch National Police"
    cooperation_type: investigative_support
    legal_basis: electronic_evidence
    direction: undirected
  - source_actor: "US DOJ"
    target_actor: "Estonian authorities"
    cooperation_type: extradition
    legal_basis: extradition
    direction: inbound
credibility_index: 4.3
source_tier: 1
missing_fields:
  - complete_server_inventory
  - final_outcomes_for_all_defendants
related_cases: []
related_operations:
  - "[[operation-trident-breach]]"
  - "[[operation-phish-phry]]"
  - "[[operation-endgame-phase1]]"
challenges_encountered:
  - "Immediate shutdown of rogue DNS infrastructure risked disconnecting still-infected victims from the Internet."
  - "The criminal infrastructure and defendants crossed U.S., Estonian, and Dutch cooperation channels."
  - "Victim remediation required public-private coordination beyond arrests and indictment."
lessons_learned:
  - "Botnet disruptions may need temporary clean infrastructure when takedown would otherwise harm victims."
  - "Large malware operations can combine law enforcement, private-sector telemetry, and technical remediation in one action."
  - "Extradition and follow-on proceedings can remain active years after the initial disruption announcement."
source_count: 4
sources:
  - "[[2011-11-09_fbi_operation-ghost-click]]"
  - "[[2014-07-15_fbi_taking-down-botnets-ghost-click]]"
  - "[[2011-11-10_arstechnica_dnschanger-ghost-click]]"
  - "[[2011-11-10_guardian_ghost-click-botnet]]"
created: 2026-05-08
updated: 2026-05-08
operation_role: umbrella
parent_operation: ""
summary: "Operation Ghost Click was a two-year FBI investigation that dismantled the DNSChanger/Rove Digital advertising-fraud botnet in November 2011. FBI reporting states that the operation disrupted an international cyber ring that infected more than 4 million computers worldwide, generated more than USD 14 million in fraudulent advertising revenue, and involved arrests of six Estonian nationals with support from the Estonian Police and Border Guard Board and Dutch National Police."
jurisdictions:
  - "[[united-states]]"
  - "[[estonia]]"
  - "[[netherlands]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj]]"
  - "[[netherlands-politie|Dutch National Police]]"
crime_types:
  - "[[malware-ic]]"
  - "[[online-fraud-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
---
## Summary

Operation Ghost Click was a two-year FBI investigation that disrupted the DNSChanger/Rove Digital botnet and advertising-fraud infrastructure in November 2011. FBI reporting states that DNSChanger infected millions of computers worldwide, redirected victims through rogue DNS servers, and allowed the operators to manipulate web traffic and online advertising revenue.

The operation qualifies as international cooperation because the FBI credited the Estonian Police and Border Guard Board and the Dutch National Police, and public reporting describes the arrest of six Estonian defendants in Estonia. FBI later testified that three Estonian nationals were extradited to the United States in November 2013.

## Operational Scope

DNSChanger modified infected computers' DNS settings so that victims used rogue name servers controlled by the criminal group. That let the operators redirect users from legitimate destinations, replace online advertisements, and monetize hijacked traffic. Public reporting consistently places the botnet at more than 4 million infections worldwide and more than 500,000 in the United States.

The FBI response included a victim-safety component. Because abruptly turning off the rogue DNS infrastructure could have cut infected users off from the Internet, the FBI obtained court authority for temporary clean DNS servers while users and service providers remediated affected machines.

## Results

| Metric | Public figure |
|---|---:|
| Defendants indicted | 7 |
| Initial arrests in Estonia | 6 |
| Worldwide infected computers | 4M+ |
| U.S. infected computers | 500K+ |
| Fraudulent advertising revenue | USD 14M+ |

## Boundary Notes

This page is the canonical operation record for DNSChanger/Rove Digital. It should not be merged with later botnet takedowns such as [[operation-endgame-phase1|Operation Endgame]], which targeted a different malware ecosystem and legal coordination model.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2011-11-09_fbi_operation-ghost-click|Operation Ghost Click: International Cyber Ring That Infected Millions of Computers Dismantled]] | FBI | 2011-11-09 | https://www.fbi.gov/news/stories/international-cyber-ring-that-infected-millions-of-computers-dismantled |
| [2] | [[2014-07-15_fbi_taking-down-botnets-ghost-click|Taking Down Botnets]] | FBI | 2014-07-15 | https://www.fbi.gov/news/speeches-and-testimony/taking-down-botnets |
| [3] | [[2011-11-10_arstechnica_dnschanger-ghost-click|How the most massive botnet scam ever made millions for Estonian hackers]] | Ars Technica | 2011-11-10 | https://arstechnica.com/tech-policy/2011/11/how-the-most-massive-botnet-scam-ever-made-millions-for-estonian-hackers/ |
| [4] | [[2011-11-10_guardian_ghost-click-botnet|FBI shuts down 'Ghost Click' botnet of 4m PCs as seven face charges]] | The Guardian | 2011-11-10 | https://www.theguardian.com/technology/2011/nov/10/ghost-click-botnet-infected-computers-millions |
