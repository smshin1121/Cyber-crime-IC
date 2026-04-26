---
type: operation
title: "Andromeda Botnet Dismantling"
title_ko: "Andromeda 봇넷 해체"
aliases:
  - "Andromeda Botnet Takedown"
case_id: CYB-2017-001
period: 1
operation_type: takedown
operation_role: umbrella
parent_operation: ""
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2017-12-04
  start: 2017-11-29
  end: 2017-12-04
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
target_entity: "Andromeda Botnet"
lead_agency: "[[fbi]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[germany]]"
  - "[[austria]]"
  - "[[belgium]]"
  - "[[finland]]"
  - "[[france]]"
  - "[[italy]]"
  - "[[netherlands]]"
  - "[[poland]]"
  - "[[spain]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[belarus]]"
  - "[[canada]]"
  - "[[montenegro]]"
  - "[[singapore]]"
  - "[[taiwan]]"
participating_agencies:
  - "[[fbi]]"
  - "[[europol-ec3]]"
  - "[[j-cat]]"
  - "[[eurojust]]"
  - "[[german-bka]]"
  - "[[microsoft]]"
legal_basis:
  []
mechanisms_used:
  - "[[sinkholing]]"
  - "[[informal-cooperation]]"
related_cases:
  []
related_operations:
  []
results:
  arrests: 1
  servers_seized: 0
  domains_seized: 1500
  indictments: 0
  decryption_keys_recovered: 0
  victims_notified: 0
  cryptocurrency_seized: ""
  other:
    - "Approximately 2 million victim IP addresses observed during a 48-hour sinkhole window"
    - "Andromeda/Gamarue infrastructure disrupted after a long-running eradication campaign"
edges:
  - source_actor: FBI
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Germany
    target_actor: Belarus
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 3.75
source_tier: 2
source_count: 4
sources:
  - "[[2017-12-04_europol-europa-eu_andromeda-botnet-dismantled-in-international-cyber-operation]]"
  - "[[2017-12-04_microsoft-com_microsoft-assists-law-enforcement-help-disrupt-andromeda-botnet]]"
  - "[[2026-04-18_microsoft-com_gamarue-threat-profile]]"
  - "[[bleeping-computer-andromeda-botnet-takedown]]"
summary: "The Andromeda/Gamarue takedown combined Europol and FBI coordination, German and Belarusian enforcement action, and Microsoft-backed sinkhole support to disrupt a long-running malware ecosystem in late 2017."
created: 2026-04-08
updated: "2026-04-26"
---
## Summary

The Andromeda/Gamarue takedown combined Europol and FBI coordination, German and Belarusian enforcement action, and Microsoft-backed sinkhole support to disrupt a long-running malware ecosystem in late 2017.

## Why The Operation Matters

Andromeda is better understood as ecosystem disruption than as a single arrest case. Public sources emphasize the technical scale:

- Andromeda had remained active for years as a crimeware service used to monetize installs and deliver follow-on payloads

## Participating Parties

**Core agencies:**
- [[fbi]]
- [[europol-ec3|Europol EC3]]
- German investigators in Lueneburg
- [[eurojust]]
- [[microsoft]]

**States publicly identified:**
United States, Germany, Austria, Belgium, Finland, France, Italy, Netherlands, Poland, Spain, United Kingdom, Australia, Belarus, Canada, Montenegro, Singapore and Taiwan.

## Results

- 1 publicly announced arrest in Belarus
- 1,500 malicious domains sinkholed

## Cooperation And Legal Analysis

This operation is a good example of why cyber takedowns need both technical and legal framing. Europol's press material gives the enforcement outline, but Microsoft's material fills in the private-sector disruption role. That matters because Andromeda was not just a website or a marketplace. It was a persistent malware-install ecosystem, so technical remediation and sinkhole coordination were essential to any lasting operational effect.

The page also avoids overstating the criminal-procedure side. Public sources clearly support the takedown and one arrest, but they do not expose a rich public docket trail. For that reason, this repo should treat Andromeda primarily as a multinational disruption operation, not as a heavily documented prosecution.

## Follow-Up Actions

> [!warning] No public court documents found
> Public material strongly supports the takedown narrative, but the repo does not currently contain a robust set of public filings matching the operation.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Andromeda Botnet Dismantled in International Cyber Operation | Europol | 2017-12-04 | https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation |
| [2] | Microsoft assists law enforcement to help disrupt the Andromeda botnet | Microsoft | 2017-12-04 | https://www.microsoft.com/en-us/msrc/blog/2018/01/microsoft-teams-up-with-law-enforcement-and-other-partners-to-disrupt-gamarue-andromeda |
| [3] | Gamarue threat profile | Microsoft | 2026-04-18 | https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/ |
| [4] | bleeping-computer-andromeda-botnet-takedown |  |  | [[bleeping-computer-andromeda-botnet-takedown]] |
