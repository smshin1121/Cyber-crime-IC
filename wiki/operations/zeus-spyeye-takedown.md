---
type: operation
title: "Zeus/SpyEye Crime Syndicate Takedown"
title_ko: "Zeus/SpyEye 범죄 조직 소탕"
aliases:
  - "Zeus SpyEye takedown 2015"
case_id: CYB-2015-050
period: 1
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - indictment
outcome: success
timeframe:
  announced: 2015-06-30
  start: 2015-06-30
  end: 2015-06-30
  ongoing: false
crime_type: "[[banking-trojan-ic]]"
target_entity: "Zeus/SpyEye banking trojan syndicate"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:

participating_agencies:
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
legal_basis:

mechanisms_used:

results:
  arrests: 5
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Zeus and SpyEye banking trojan infrastructure disrupted"
edges:
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 1.88
source_tier: 3
missing_fields:
  - legal_basis
  - mechanisms_used
  - exact_participating_countries
  - exact_arrest_count
related_cases:

related_operations:

challenges_encountered:

lessons_learned:

source_count: 6
sources:
  - "[[europol-zeusspyeye-joint-investigation-team-takedown]]"
  - "[[2015-06-30_news-sophos-com_zeus-and-spyeye-crime-syndicate-taken-down-by-europol]]"
  - "[[2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans]]"
  - "[[2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang]]"
  - "[[2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware]]"
  - "[[2015-06-29_techmonitor-ai_zeus-spyeye-malware-gang-members-arrested-in-ukraine]]"
created: 2026-04-08
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "In June 2015, Europol announced the takedown of a cybercrime syndicate responsible for distributing the **Zeus** and **SpyEye** banking trojans. These malware families were among the most prolific financial cybercrime tools of the 2010s, responsible for stealing hundreds of millions of dollars from online banking users worldwide."
organizations:
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
crime_types:
  - "[[banking-trojan-ic]]"
  - "[[malware-ic]]"
---
> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

In June 2015, Europol announced the takedown of a cybercrime syndicate responsible for distributing the **Zeus** and **SpyEye** banking trojans. These malware families were among the most prolific financial cybercrime tools of the 2010s, responsible for stealing hundreds of millions of dollars from online banking users worldwide.

The operation involved international law enforcement cooperation to dismantle the criminal network operating these banking trojans. The Zeus and SpyEye malware families had been used to harvest banking credentials from infected computers on a massive scale.

## Background

Zeus (also known as Zbot) first appeared around 2007 and became one of the most widespread banking trojans. SpyEye emerged as a competitor and later merged with Zeus code. Together, they formed the backbone of a vast cybercrime ecosystem that enabled financial fraud on a global scale. The malware was typically distributed through phishing emails and drive-by downloads, targeting online banking sessions to steal credentials and initiate fraudulent transfers.

## Participating Parties

### Coordinating Body
- [[europol-ec3|Europol EC3]]

### Participating Agencies
- [[europol-ec3|Europol EC3]]
- [[fbi-cyber-division|FBI Cyber Division]]

> [!warning] Legal status check needed
> The full list of participating countries and agencies needs verification from official Tier 1-2 sources.

## Legal Framework

Specific legal bases for the international cooperation have not been identified from available Tier 3 sources.

## Operational Timeline

| Date | Event |
|------|-------|
| 2015-06-30 | Europol announces takedown of Zeus/SpyEye crime syndicate |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Syndicate disrupted | Zeus/SpyEye banking trojan network |
| International cooperation | Multi-country joint operation |

> [!warning] Legal status check needed
> Precise arrest counts and seizure details need verification from official sources.

## Cooperation Mechanisms Used

Details of specific cooperation mechanisms are not available from the Tier 3 source.

## Korean Involvement (한국의 참여)

No Korean involvement identified. Zeus and SpyEye primarily targeted Western banking institutions, though the malware had global reach.

## Contradictions & Open Questions

- What was the exact number of arrests and in which countries?
- Which specific legal instruments enabled the cross-border cooperation?
- What was the timeline of the investigation preceding the takedown announcement?
- How many victims were affected by the Zeus/SpyEye syndicate?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2015-06-25: Europol: Major Cybercrime Ring Dismantled by Joint Investigation Team.
- Sophos, 2015-06-30: Zeus and SpyEye crime syndicate taken down by Europol.
- Help Net Security, 2015-06-25: The downfall of a major cybercrime ring exploiting banking Trojans.
- SC Media, 2015-06-25: Europol takes down high profile Ukraine-based cybergang.
- The Hacker News, 2015-06-27: Europol Arrests Gang Behind Zeus and SpyEye Banking Malware.
- Tech Monitor, 2015-06-29: Zeus & SpyEye malware gang members arrested in Ukraine.

## Evidence and Attribution Notes

- Europol announced on 25 June 2015 the results of a Joint Investigation Team (JIT) action against a Zeus/SpyEye banking-Trojan network, with the coordinated action executed 18-19 June 2015 in Ukraine
- On the action days: 5 suspects arrested in Ukraine, 8 house searches conducted across 4 Ukrainian cities, and computer equipment and devices seized for forensic analysis
- The JIT comprised 6 core member states: Austria, Belgium, Finland, Netherlands, Norway, and United Kingdom — an unusually small and tight configuration for a cybercrime JIT — with Europol and Eurojust coordination support
- Additional cooperation (non-JIT) came from Estonia, Latvia, Germany, Moldova, Poland, Ukraine, and the United States; Ukraine was the primary operational venue despite not being a JIT party
- Estimated damages: at least EUR 2 million from the investigated cluster; the group engaged in malware development, infection, credential harvesting, and money-mule laundering across the full cybercrime value chain
- 60 total arrests across the broader operation including 34 from a linked money-mule subsidiary network — connecting banking-Trojan developers to the downstream cash-out layer
- This operation is cited as one of Europol's early (pre-EC3-maturity) successful uses of the Joint Investigation Team mechanism for cybercrime, establishing procedural precedent for later JITs
- In June 2015, Europol announced the takedown of a cybercrime syndicate responsible for distributing the **Zeus** and **SpyEye** banking trojans.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: Major Cybercrime Ring Dismantled by Joint Investigation Team | Europol | 2015-06-25 | https://www.europol.europa.eu/media-press/newsroom/news/major-cybercrime-ring-dismantled-joint-investigation-team |
| [2] | Zeus and SpyEye crime syndicate taken down by Europol | Sophos | 2015-06-30 | https://news.sophos.com/en-us/2015/06/30/zeus-and-spyeye-crime-syndicate-taken-down-by-europol/ |
| [3] | The downfall of a major cybercrime ring exploiting banking Trojans | Help Net Security | 2015-06-25 | https://www.helpnetsecurity.com/2015/06/25/the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans/ |
| [4] | Europol takes down high profile Ukraine-based cybergang | SC Media | 2015-06-25 | https://www.scworld.com/news/europol-takes-down-high-profile-ukraine-based-cybergang |
| [5] | Europol Arrests Gang Behind Zeus and SpyEye Banking Malware | The Hacker News | 2015-06-27 | https://thehackernews.com/2015/06/zeus-spyeye-banking-malware.html?m=1 |
| [6] | Zeus & SpyEye malware gang members arrested in Ukraine | Tech Monitor | 2015-06-29 | https://www.techmonitor.ai/hardware/zeus-spyeye-malware-gang-members-arrested-in-ukraine-4611234 |
