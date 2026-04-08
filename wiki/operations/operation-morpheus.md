---
type: operation
title: "Operation Morpheus (Cobalt Strike Takedown)"
title_ko: "모르페우스 작전 (코발트 스트라이크 소탕)"
aliases: ["Operation Morpheus", "Cobalt Strike takedown", "NCA Europol Cobalt Strike"]
case_id: "CYB-2024-050"
period: 3
operation_type: "infrastructure-seizure"
status: "completed"
enforcement_type:
  - "seizure"
  - "takedown"
outcome: "success"
timeframe:
  announced: "2024-06-28"
  start: "2024-06-28"
  end: "2024-06-28"
  ongoing: false
crime_type: "[[hacking-ic]]"
target_entity: "Unauthorized Cobalt Strike servers"
lead_agency: "[[uk-nca]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[poland]]"
  - "[[united-states]]"
participating_agencies:
  - "[[uk-nca]]"
  - "[[europol-ec3]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 593
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "593 Cobalt Strike servers associated with criminal activity taken down"
    - "27 countries involved overall"
    - "IP addresses flagged to internet service providers in 27 countries"
edges:
  - source_actor: "UK NCA"
    target_actor: "Europol"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
credibility_index: 2.55
source_tier: 3
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "complete_participating_countries"
  - "url"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Targeting dual-use tools (legitimate software abused for crime) requires coordination with the software vendor"
  - "IP flagging to ISPs in 27 countries demonstrates effective public-private cooperation"
source_count: 1
sources: []
created: 2026-04-08
updated: 2026-04-08
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

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Source 1 | thehackernews.com | - | [원본](https://thehackernews.com/2024/07/global-police-operation-shuts-down-600.html) |
| [2] | Source 2 | nationalcrimeagency.gov.uk | - | [원본](https://www.nationalcrimeagency.gov.uk/news/national-crime-agency-leads-international-operation-to-degrade-illegal-versions-of-cobalt-strike) |