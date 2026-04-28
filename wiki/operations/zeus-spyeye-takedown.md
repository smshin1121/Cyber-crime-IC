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
  announced: 2015-06-25
  start: 2015-06-18
  end: 2015-06-19
  ongoing: false
crime_type: "[[banking-trojan-ic]]"
target_entity: "Zeus/SpyEye banking trojan syndicate"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[austria]]"
  - "[[belgium]]"
  - "[[finland]]"
  - "[[netherlands]]"
  - "[[norway]]"
  - "[[united-kingdom]]"
  - "[[estonia]]"
  - "[[latvia]]"
  - "[[germany]]"
  - "[[moldova]]"
  - "[[poland]]"
  - "[[ukraine]]"
  - "[[united-states]]"

participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
legal_basis:

mechanisms_used:
  - "[[joint-investigation-team]]"
  - "[[eurojust-coordination-meeting]]"

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
    - "Five suspects arrested in Ukraine"
    - "Eight house searches conducted across four Ukrainian cities"
    - "Computer equipment and devices seized for forensic analysis"
    - "Broader operation linked to 60 arrests, including 34 money-mule arrests"
edges:
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 3.85
source_tier: 2
missing_fields:
  - legal_basis
  - prosecution_outcomes
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
updated: 2026-04-28
operation_role: umbrella
parent_operation: ""
summary: "In June 2015, Europol announced the takedown of a cybercrime syndicate responsible for distributing the **Zeus** and **SpyEye** banking trojans. These malware families were among the most prolific financial cybercrime tools of the 2010s, responsible for stealing hundreds of millions of dollars from online banking users worldwide."
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
crime_types:
  - "[[banking-trojan-ic]]"
  - "[[malware-ic]]"
---
## Summary

In June 2015, Europol and Eurojust announced a Joint Investigation Team action against a cybercrime ring using **Zeus** and **SpyEye** banking trojans. The action days were 18-19 June 2015 in Ukraine, where authorities arrested five suspects, carried out eight house searches across four cities, and seized computer equipment for forensic analysis.

The operation targeted a full banking-trojan value chain: malware development, infection, credential theft, fraudulent online-banking transfers, and money-mule cash-out. The official Europol source also links the action to a broader operation that produced 60 arrests, including 34 arrests in a subsidiary money-mule network.

## Background

Zeus (also known as Zbot) first appeared around 2007 and became one of the most widespread banking trojans. SpyEye emerged as a competitor and later merged with Zeus code. Together, they formed the backbone of a vast cybercrime ecosystem that enabled financial fraud on a global scale. The malware was typically distributed through phishing emails and drive-by downloads, targeting online banking sessions to steal credentials and initiate fraudulent transfers.

## Participating Parties

| Role | Parties |
|---|---|
| Coordination | [[europol-ec3|Europol EC3]], [[eurojust|Eurojust]] |
| JIT members | [[austria|Austria]], [[belgium|Belgium]], [[finland|Finland]], [[netherlands|Netherlands]], [[norway|Norway]], [[united-kingdom|United Kingdom]] |
| Operational venue | [[ukraine|Ukraine]] |
| Additional cooperation | [[estonia|Estonia]], [[latvia|Latvia]], [[germany|Germany]], [[moldova|Moldova]], [[poland|Poland]], [[united-states|United States]] |

## Legal Framework

The public record identifies a Joint Investigation Team supported by Europol and Eurojust. The source set does not provide the underlying domestic charging documents or the complete legal-basis paperwork for each jurisdiction.

## Operational Timeline

| Date | Event |
|------|-------|
| 2015-06-18 to 2015-06-19 | Coordinated action days in Ukraine; arrests, searches, and forensic seizures. |
| 2015-06-25 | Europol announced the JIT takedown publicly. |
| 2015-06-27 to 2015-06-30 | Independent cybersecurity media coverage amplified the Europol announcement. |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 5 suspects arrested in Ukraine on the action days |
| Searches | 8 house searches in 4 Ukrainian cities |
| Seizures | Computer equipment and devices seized for forensic analysis |
| Broader enforcement context | 60 total arrests in the broader operation, including 34 money-mule arrests |
| Estimated damage | At least EUR 2 million for the investigated cluster in the Europol source digest |

## Cooperation Mechanisms Used

The core mechanism was a Joint Investigation Team with Eurojust judicial support. Ukraine was the main operational venue, while the United States and several European countries provided additional cooperation outside the JIT member list.

## Korean Involvement (한국의 참여)

No Korean involvement identified. Zeus and SpyEye primarily targeted Western banking institutions, though the malware had global reach.

## Contradictions & Open Questions

- The source set confirms the JIT and action-day results, but does not provide complete prosecution outcomes for all arrested suspects.
- The page overlaps heavily with [[zeus-spyeye-jit-takedown]]. That duplicate-canonical relationship should be reviewed separately before one page is absorbed into the other.
- Victim counts are not precise in the current corpus; the strongest quantified figure is the Europol damage estimate for the investigated cluster.

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

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a Joint Investigation Team arrest sweep against the Zeus/SpyEye banking-trojan syndicate, rather than a defendant-specific follow-on action. The record attributes coordination to Europol and Eurojust, with JIT members and additional cooperating jurisdictions recorded in the country list.

The cooperation model is documented through named agencies and partners: Europol EC3, Eurojust, FBI Cyber Division, the six JIT member states, Ukraine as operational venue, and additional cooperating European and U.S. authorities; enforcement posture: arrest sweep and forensic seizure.

Operational results captured for the canonical record: 5 action-day arrests; 8 searches across 4 Ukrainian cities; computer-equipment seizures; Zeus and SpyEye banking-trojan infrastructure disrupted; broader operation linked to 60 arrests including 34 money-mule arrests.

The canonical source set contains 6 reference(s): Europol Zeusspyeye Joint Investigation Team Takedown, 2015 06 30 News Sophos Com Zeus And Spyeye Crime Syndicate Taken Down By Europol, 2025 06 25 Helpnetsecurity Com The Downfall Of A Major Cybercrime Ring Exploiting Banking Trojans, 2015 06 25 Scworld Com Europol Takes Down High Profile Ukraine Based Cybergang, 2015 06 27 Thehackernews Com Europol Arrests Gang Behind Zeus And Spyeye Banking Malware, 2015 06 29 Techmonitor Ai Zeus Spyeye Malware Gang Members Arrested In Ukraine.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis, Prosecution Outcomes.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: Major Cybercrime Ring Dismantled by Joint Investigation Team | Europol | 2015-06-25 | https://www.europol.europa.eu/media-press/newsroom/news/major-cybercrime-ring-dismantled-joint-investigation-team |
| [2] | Zeus and SpyEye crime syndicate taken down by Europol | Sophos | 2015-06-30 | https://news.sophos.com/en-us/2015/06/30/zeus-and-spyeye-crime-syndicate-taken-down-by-europol/ |
| [3] | The downfall of a major cybercrime ring exploiting banking Trojans | Help Net Security | 2015-06-25 | https://www.helpnetsecurity.com/2015/06/25/the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans/ |
| [4] | Europol takes down high profile Ukraine-based cybergang | SC Media | 2015-06-25 | https://www.scworld.com/news/europol-takes-down-high-profile-ukraine-based-cybergang |
| [5] | Europol Arrests Gang Behind Zeus and SpyEye Banking Malware | The Hacker News | 2015-06-27 | https://thehackernews.com/2015/06/zeus-spyeye-banking-malware.html?m=1 |
| [6] | Zeus & SpyEye malware gang members arrested in Ukraine | Tech Monitor | 2015-06-29 | https://www.techmonitor.ai/hardware/zeus-spyeye-malware-gang-members-arrested-in-ukraine-4611234 |
