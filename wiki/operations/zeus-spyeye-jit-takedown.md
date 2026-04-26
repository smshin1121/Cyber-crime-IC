---
type: operation
title: "Zeus/SpyEye Joint Investigation Team Takedown"
title_ko: "공식 작전명 없음 (Zeus/SpyEye 합동수사팀 작전)"
aliases:
  - "Zeus SpyEye JIT"
case_id: CYB-2015-005
period: 1
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2015-06-19
  start: 2015-06-18
  end: 2015-06-19
  ongoing: false
crime_type: "[[malware-ic]]"
target_entity: "Zeus/SpyEye cybercrime ring"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[austria]]"
  - "[[belgium]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
legal_basis:

mechanisms_used:
  - "[[joint-investigation-team]]"
results:
  arrests: 5
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Computer equipment seized"
    - "Zeus and SpyEye banking trojan ring dismantled"
edges:
  - source_actor: Europol
    target_actor: Eurojust
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Austria
    target_actor: Ukraine
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 2.28
source_tier: 2
missing_fields:
  - legal_basis
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
summary: "In June 2015, Europol and Eurojust coordinated a Joint Investigation Team (JIT) operation involving Austria, Belgium, Ukraine, and at least 6 other European countries that dismantled a major cybercrime ring using Zeus and SpyEye banking trojans. The group had hacked online banking systems across Europe and laundered the stolen funds. Five suspects were arrested in Ukraine and computer equipment was seized."
jurisdictions:
  - "[[austria]]"
  - "[[belgium]]"
  - "[[ukraine]]"
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
crime_types:
  - "[[malware-ic]]"
---
## Summary

In June 2015, Europol and Eurojust coordinated a Joint Investigation Team (JIT) operation involving Austria, Belgium, Ukraine, and at least 6 other European countries that dismantled a major cybercrime ring using Zeus and SpyEye banking trojans. The group had hacked online banking systems across Europe and laundered the stolen funds. Five suspects were arrested in Ukraine and computer equipment was seized.

## Participating Parties

**Coordinating Bodies:**
- Europol
- Eurojust

**Participating Countries (6+):**
Austria, Belgium, Ukraine, and at least 3 additional European countries

## Results

- **5 arrests** in Ukraine
- Computer equipment seized
- Zeus and SpyEye banking trojan criminal ring dismantled
- Online banking hacking and money laundering network neutralized

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

## Operational Timeline

- 2015-06-18: activity or investigation start.
- 2015-06-19: public announcement.
- 2015-06-19: reported enforcement endpoint.
- 2015-06-25: public source coverage from Europol, Help Net Security, SC Media.
- 2015-06-27: public source coverage from The Hacker News.
- 2015-06-29: public source coverage from Tech Monitor.
- 2015-06-30: public source coverage from Sophos.

## Legal and Procedural Posture

- Recorded crime classification: malware.
- Recorded enforcement posture: Arrest and Seizure.
- The record is categorized as joint-investigation with status completed.

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
