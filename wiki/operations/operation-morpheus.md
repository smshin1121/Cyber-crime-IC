---
aliases:

case_id: CYB-2024-050
challenges_encountered:

coordinating_body: "[[europol-ec3]]"
created: 2026-04-08
credibility_index: 2.55
crime_type: "[[hacking-ic]]"
edges:

enforcement_type:

lead_agency: "[[uk-nca]]"
legal_basis:

lessons_learned:

mechanisms_used:

missing_fields:

operation_type: infrastructure-seizure
outcome: success
participating_agencies:

participating_countries:

period: 3
related_cases:

related_operations:

results:
  arrests: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:

  servers_seized: 593
  victims_notified: 0
source_count: 1
source_tier: 2
sources:
  - "[[2024-06-28-uk-nca-operation-morpheus-cobalt-strike]]"
status: completed
target_entity: "Unauthorized Cobalt Strike servers"
timeframe:
  announced: 2024-06-28
  end: 2024-06-28
  ongoing: false
  start: 2024-06-28
title: "Operation Morpheus (Cobalt Strike Takedown)"
title_ko: "모르페우스 작전 (코발트 스트라이크 소탕)"
type: operation
updated: 2026-04-09
operation_role: umbrella
parent_operation: ""
summary: "**Operation Morpheus** was an NCA-led, Europol-coordinated international operation targeting unauthorized (pirated/cracked) instances of **Cobalt Strike**, a legitimate penetration testing tool that has been extensively abused by cybercriminals for ransomware attacks, espionage, and other malicious purposes. The operation resulted in the takedown of **593 Cobalt Strike servers** across **27 countries**."
organizations:
  - "[[uk-nca]]"
  - "[[europol-ec3]]"
crime_types:
  - "[[hacking-ic]]"
---
> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

**Operation Morpheus** was an NCA-led, Europol-coordinated international operation targeting unauthorized (pirated/cracked) instances of **Cobalt Strike**, a legitimate penetration testing tool that has been extensively abused by cybercriminals for ransomware attacks, espionage, and other malicious purposes. The operation resulted in the takedown of **593 Cobalt Strike servers** across **27 countries**.

The operation was significant as it targeted the criminal abuse of a dual-use tool rather than a specific criminal group, demonstrating an infrastructure-focused approach to disrupting the cybercrime ecosystem.

## Background

Cobalt Strike is a commercial penetration testing tool developed by HelpSystems (now Fortra). While designed for legitimate security testing, cracked and pirated versions of Cobalt Strike have become one of the most popular tools among cybercriminals for post-exploitation activities, command-and-control communications, and ransomware deployment. The widespread abuse of Cobalt Strike has been a significant concern for the cybersecurity community.

## Participating Parties

### Lead Agency
- [[uk-nca|UK National Crime Agency]]

### Coordinating Body
- [[europol-ec3|Europol EC3]]

### Participating Countries (7 lead + 20 supporting = 27 total)
Lead participants:
- [[united-kingdom|United Kingdom]]
- [[australia|Australia]]
- [[canada|Canada]]
- [[germany|Germany]]
- [[netherlands|Netherlands]]
- [[poland|Poland]]
- [[united-states|United States]]

An additional 20 countries were involved through ISP notifications.

## Legal Framework

Specific legal instruments not detailed in available Tier 3 sources.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2024 | Investigation into criminal Cobalt Strike infrastructure |
| 2024-06-28 | 593 servers taken down across 27 countries |

## Results and Impact

| Metric | Count |
|--------|-------|
| Servers taken down | 593 |
| Countries involved | 27 |
| Lead participating countries | 7 |

The takedown of 593 Cobalt Strike servers *likely* disrupted the operations of numerous cybercrime groups, given the tool's widespread use in the criminal ecosystem.

## Cooperation Mechanisms Used

Not detailed in Tier 3 source. The IP flagging to ISPs suggests a combination of formal legal processes and voluntary cooperation with internet service providers.

## Korean Involvement (한국의 참여)

No Korean involvement identified. However, Cobalt Strike abuse is a global issue and Korean organizations have been targets of attacks using the tool.

## Contradictions & Open Questions

- How many criminal groups were impacted by the server takedowns?
- What was the legal basis for taking down servers in 27 different jurisdictions?
- How many of the servers were subsequently replaced by criminals?
- What role did Fortra (Cobalt Strike developer) play in the operation?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References
| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike | UK NCA | 2024-07-03 | [link](https://www.nationalcrimeagency.gov.uk/news/national-crime-agency-leads-international-operation-to-degrade-illegal-versions-of-cobalt-strike) |

> [!note] Source enrichment 2026-04-14
> A prior Tier-3 row (The Hacker News aggregator, 2024-07) was removed in favor of the Tier-1 NCA primary source. The NCA page corroborates all quantitative claims on this page.