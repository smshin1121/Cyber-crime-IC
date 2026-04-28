---
type: operation
title: "Imminent Monitor RAT Takedown"
title_ko: "이미넌트 모니터 RAT 소탕"
aliases:
  - "IM RAT takedown"
  - "Imminent Monitor operation 2019"
case_id: CYB-2019-050
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2019-11-29
  start: 2019-11-29
  end: 2019-12-02
  ongoing: false
crime_type: "[[hacking-ic]]"
target_entity: "Imminent Monitor RAT (Remote Access Trojan)"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[australia]]"
  - "[[colombia]]"
  - "[[czech-republic]]"
  - "[[netherlands]]"
  - "[[poland]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[australia-afp]]"
legal_basis:

mechanisms_used:

results:
  arrests: 13
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "430 devices seized"
    - "Imminent Monitor RAT infrastructure dismantled"
    - "14,500 buyers identified across 124 countries"
edges:
  - source_actor: Europol
    target_actor: "Australian Federal Police"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: Eurojust
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 1.88
source_tier: 3
missing_fields:
  - legal_basis
  - mechanisms_used
related_cases:

related_operations:

challenges_encountered:

lessons_learned:
  - "OpSec mistakes by RAT developers can lead to identification"
  - "Commodity malware with thousands of buyers requires broad international cooperation"
source_count: 5
sources:
  - "[[2019-11-29_thehackernews-com_europol-imminent-monitor-rat]]"
  - "[[2019-12-03_welivesecurity-com_notorious-rat-spy-tool-global-operation]]"
  - "[[2019-12-01_portswigger-net_imminent-monitor-spyware-operation-undone-by-opsec-mistakes]]"
  - "[[2019-12-01_aspi-org-au_national-security-wrap-186]]"
  - "[[2019-12-02_wired-gov-net_cybercrime-site-selling-hacking-tool-taken-down]]"
created: 2026-04-08
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "In November-December 2019, [[europol-ec3|Europol]] coordinated an international operation that dismantled the infrastructure of **Imminent Monitor**, a Remote Access Trojan (RAT) sold commercially as a legitimate tool but widely used for cybercrime. The operation involved law enforcement from 8 countries and resulted in **13 arrests** and the seizure of **430 devices**. Investigators identified **14,500 buyers** of the RAT across **124 countries**."
jurisdictions:
  - "[[australia]]"
  - "[[colombia]]"
  - "[[czech-republic]]"
  - "[[netherlands]]"
  - "[[poland]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[united-kingdom]]"
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[australia-afp]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[malware-ic]]"
---
## Summary

In November-December 2019, [[europol-ec3|Europol]] coordinated an international operation that dismantled the infrastructure of **Imminent Monitor**, a Remote Access Trojan (RAT) sold commercially as a legitimate tool but widely used for cybercrime. The operation involved law enforcement from 8 countries and resulted in **13 arrests** and the seizure of **430 devices**. Investigators identified **14,500 buyers** of the RAT across **124 countries**.

The operation was notable for targeting a commodity malware tool and its user base, rather than just a single criminal group, demonstrating law enforcement's expanding approach to cybercrime enforcement.

## Background

Imminent Monitor was a Remote Access Trojan marketed as a legitimate remote administration tool but widely used for malicious purposes including espionage, data theft, and surveillance. The tool was sold through a dedicated website and allowed buyers to remotely control victims' computers, access files, record keystrokes, and activate webcams. The developers' operational security failures contributed to their identification.

## Participating Parties

### Coordinating Bodies
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust]]

### Participating Countries (8)
- [[australia|Australia]]
- [[colombia|Colombia]]
- [[czech-republic|Czech Republic]]
- [[netherlands|Netherlands]]
- [[poland|Poland]]
- [[spain|Spain]]
- [[sweden|Sweden]]
- [[united-kingdom|United Kingdom]]

### Participating Agencies
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust]]
- [[australia-afp|Australian Federal Police]]

## Legal Framework

Specific legal instruments have not been detailed in available public sources. The coordination through Europol and Eurojust suggests use of EU cooperation mechanisms.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2019 | Investigation into Imminent Monitor RAT |
| 2019-11-29 | First announcements of operation |
| 2019-12-02 | Europol formal announcement |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 13 |
| Devices seized | 430 |
| Buyers identified | 14,500 |
| Countries with buyers | 124 |
| Countries participating | 8 |

## Cooperation Mechanisms Used

Details not fully documented in public sources. Europol and Eurojust coordination suggests formal EU cooperation channels.

## Korean Involvement (한국의 참여)

No Korean involvement identified. However, given the global user base (124 countries), Korean users may have been among the 14,500 identified buyers.

## Contradictions & Open Questions

- What were the specific OpSec mistakes that led to the developers' identification?
- How many of the 14,500 buyers were ultimately investigated?
- What was the legal basis for prosecuting buyers of a tool marketed as legitimate?
- Were there follow-up actions against the buyer base?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- The Hacker News, 2019-11-29: Europol Imminent Monitor RAT.
- WeLiveSecurity, 2019-12-03: Notorious RAT spy tool global operation.
- PortSwigger, 2019-12-01: Imminent Monitor spyware operation undone by opsec mistakes.
- ASPI, 2019-12-01: National Security Wrap 186.
- Wired-Gov, 2019-12-02: Cybercrime site selling hacking tool taken down.

## Evidence and Attribution Notes

- In November-December 2019, Europol coordinated an international operation that dismantled the infrastructure of **Imminent Monitor**, a Remote Access Trojan (RAT) sold commercially as a legitimate tool but widely used for cybercrime.
- The operation involved law enforcement from 8 countries and resulted in **13 arrests** and the seizure of **430 devices**.
- Investigators identified **14,500 buyers** of the RAT across **124 countries**.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against Imminent Monitor RAT (Remote Access Trojan), rather than a defendant-specific follow-on action. The record attributes lead responsibility to Europol Ec3 and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Australia, Colombia, Czech Republic, Netherlands, Poland, Spain, Sweden, United Kingdom.

The cooperation model is documented through named agencies and partners: Europol Ec3, Eurojust, Australia Afp; enforcement posture: Arrest, Seizure, Takedown.

Operational results captured for the canonical record: 13 arrests; 430 devices seized; Imminent Monitor RAT infrastructure dismantled; 14,500 buyers identified across 124 countries.

The canonical source set contains 5 reference(s): 2019 11 29 Thehackernews Com Europol Imminent Monitor Rat, 2019 12 03 Welivesecurity Com Notorious Rat Spy Tool Global Operation, 2019 12 01 Portswigger Net Imminent Monitor Spyware Operation Undone By Opsec Mistakes, 2019 12 01 Aspi Org Au National Security Wrap 186, 2019 12 02 Wired Gov Net Cybercrime Site Selling Hacking Tool Taken Down.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis and Mechanisms Used.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol Imminent Monitor RAT | The Hacker News | 2019-11-29 | https://thehackernews.com/2019/11/europol-imminent-monitor-rat.html |
| [2] | Notorious RAT spy tool global operation | WeLiveSecurity | 2019-12-03 | https://www.welivesecurity.com/2019/12/03/notorious-rat-spy-tool-global-operation/ |
| [3] | Imminent Monitor spyware operation undone by opsec mistakes | PortSwigger | 2019-12-01 | https://portswigger.net/daily-swig/imminent-monitor-spyware-operation-undone-by-opsec-mistakes |
| [4] | National Security Wrap 186 | ASPI | 2019-12-01 | https://www.aspi.org.au/strategist-posts/national-security-wrap-186/ |
| [5] | Cybercrime site selling hacking tool taken down | Wired-Gov | 2019-12-02 | https://www.wired-gov.net/wg/news.nsf/print/Cybercrime+site+selling+hacking+tool+taken+down+following+international+operation+02122019111500 |
