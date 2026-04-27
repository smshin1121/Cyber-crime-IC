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
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[poland]]"
  - "[[united-states]]"
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
source_count: 5
source_tier: 2
sources:
  - "[[2024-06-28-uk-nca-operation-morpheus-cobalt-strike]]"
  - "[[the-hacker-news-operation-morpheus-cobalt-strike-takedown]]"
  - "[[uk-nca-operation-morpheus-cobalt-strike-takedown]]"
  - "[[2024-07-03_bleepingcomputer-com_europol-takes-down-593-cobalt-strike-servers-used-by-cybercriminals]]"
  - "[[2024-07-03_techradar-com_hundreds-of-cobalt-strike-linked-servers-taken-down-in-major-police-operation]]"
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
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "**Operation Morpheus** was an NCA-led, Europol-coordinated international operation targeting unauthorized (pirated/cracked) instances of **Cobalt Strike**, a legitimate penetration testing tool that has been extensively abused by cybercriminals for ransomware attacks, espionage, and other malicious purposes. The operation resulted in the takedown of **593 Cobalt Strike servers** across **27 countries**."
organizations:
  - "[[uk-nca]]"
  - "[[europol-ec3]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
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

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- UK National Crime Agency, 2024-07-03: National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike.
- The Hacker News, 2024-07-03: The Hacker News: Global Police Operation Shuts Down 600 Cybercrime Servers (Operation Morpheus).
- UK NCA, Unknown: UK NCA: Operation Morpheus (Cobalt Strike Takedown).
- BleepingComputer, 2024-07-03: Europol takes down 593 Cobalt Strike servers used by cybercriminals.
- TechRadar, 2024-07-03: Hundreds of Cobalt Strike-linked servers taken down in major police operation.

## Evidence and Attribution Notes

- 690 malicious Cobalt Strike instances targeted across 129 ISPs in 27 countries; 593 removed.
- Multi-agency operation: Europol, FBI, AFP, RCMP, German BKA, Dutch Politie, Polish CBZC.
- Action week beginning 24 June 2024 (published 3 July 2024).
- **Operation Morpheus** was an NCA-led, Europol-coordinated international operation targeting unauthorized (pirated/cracked) instances of **Cobalt Strike**, a legitimate penetration testing tool that has been extensively abused by cybercriminals for ransomware attacks, espionage, and other malicious purposes.
- The operation resulted in the takedown of **593 Cobalt Strike servers** across **27 countries**.
- Europol announced Operation Morpheus on 3 July 2024: the takedown of 593 unlicensed/cracked Cobalt Strike red-team tool servers used by cybercriminals out of 690 IP addresses initially flagged to online service providers in 27 countries during an intensive week of action from 24-28 June 2024
- Lead agency: UK National Crime Agency (NCA); participating law enforcement: Australia, Canada, Germany, Netherlands, Poland, and the United States — coordinated through Europol headquarters
- Private-sector partners played unusually prominent roles: BAE Systems Digital Intelligence, Trellix, Shadowserver, Spamhaus, and Abuse.ch contributed to identification and reporting of malicious Cobalt Strike instances; the Malware Information Sharing Platform (MISP) was used for real-time threat intelligence sharing

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- UK National Crime Agency, 2024-07-03: National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show submenu for Who we are Our mission Our people Our leadership.
- UK NCA, 2024-07-03: National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show submenu for Who we are Our mission Our people Our leadership.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against Unauthorized Cobalt Strike servers, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Uk Nca and coordination to Europol Ec3, with participating or affected jurisdictions recorded as United Kingdom, Australia, Canada, Germany, Netherlands, Poland, United States.

The cooperation model is visible primarily through the lead/coordinating agencies and country list; detailed legal mechanism fields remain sparse.

Operational results captured for the canonical record: 593 servers seized.

The canonical source set contains 5 reference(s): 2024 06 28 Uk Nca Operation Morpheus Cobalt Strike, The Hacker News Operation Morpheus Cobalt Strike Takedown, Uk Nca Operation Morpheus Cobalt Strike Takedown, 2024 07 03 Bleepingcomputer Com Europol Takes Down 593 Cobalt Strike Servers Used By Cybercriminals, 2024 07 03 Techradar Com Hundreds Of Cobalt Strike Linked Servers Taken Down In Major Police Operation.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike | UK National Crime Agency | 2024-07-03 |  |
| [2] | The Hacker News: Global Police Operation Shuts Down 600 Cybercrime Servers (Operation Morpheus) | The Hacker News | 2024-07-03 | https://thehackernews.com/2024/07/global-police-operation-shuts-down-600.html |
| [3] | UK NCA: Operation Morpheus (Cobalt Strike Takedown) | UK NCA | Unknown | https://www.nationalcrimeagency.gov.uk/news/national-crime-agency-leads-international-operation-to-degrade-illegal-versions-of-cobalt-strike |
| [4] | Europol takes down 593 Cobalt Strike servers used by cybercriminals | BleepingComputer | 2024-07-03 | https://www.bleepingcomputer.com/news/security/europol-takes-down-593-cobalt-strike-servers-used-by-cybercriminals/ |
| [5] | Hundreds of Cobalt Strike-linked servers taken down in major police operation | TechRadar | 2024-07-03 | https://www.techradar.com/pro/security/hundreds-of-cobalt-strike-linked-servers-taken-down-in-major-police-operation |
