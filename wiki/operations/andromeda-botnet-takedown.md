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
source_count: 5
sources:
  - "[[2017-12-04_europol-europa-eu_andromeda-botnet-dismantled-in-international-cyber-operation]]"
  - "[[2017-12-04_microsoft-com_microsoft-assists-law-enforcement-help-disrupt-andromeda-botnet]]"
  - "[[2026-04-18_microsoft-com_gamarue-threat-profile]]"
  - "[[2017-12-04_bleepingcomputer-com_andromeda-botnet-gets-crushed]]"
  - "[[portswigger-911-s5-botnet-dismantling]]"
summary: "The Andromeda/Gamarue takedown combined Europol and FBI coordination, German and Belarusian enforcement action, and Microsoft-backed sinkhole support to disrupt a long-running malware ecosystem in late 2017."
created: 2026-04-08
updated: 2026-04-27
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

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2017-12-04: Andromeda Botnet Dismantled in International Cyber Operation.
- Microsoft, 2017-12-04: Microsoft assists law enforcement to help disrupt the Andromeda botnet.
- Microsoft, 2026-04-18: Gamarue threat profile.
- BleepingComputer, 2017-12-04: Andromeda Botnet Gets Crushed.
- PortSwigger (The Daily Swig), 2017-12-05: PortSwigger Daily Swig: Andromeda Botnet Dismantled by International Taskforce.

## Operational Timeline

- 2017-11-29: activity or investigation start.
- 2017-12-04: public announcement.
- 2017-12-04: reported enforcement endpoint.
- 2017-12-04: public source coverage from BleepingComputer, Europol, Microsoft.
- 2017-12-05: public source coverage from PortSwigger (The Daily Swig).
- 2026-04-18: public source coverage from Microsoft.

## Evidence and Attribution Notes

- In late November to early December 2017, an international law enforcement operation dismantled the Andromeda botnet infrastructure.
- The FBI, German Central Criminal Investigation Office in Luneburg, Europol's European Cybercrime Centre (EC3), the Joint Cybercrime Action Task Force (J-CAT), and Eurojust coordinated with 17 countries and private sector partners including Microsoft to neutralize the botnet.
- The operation disrupted servers and domains used for malware distribution through the Andromeda malware family.
- Microsoft states that its Digital Crimes Unit and security teams supported law enforcement and partners in disrupting Gamarue/Andromeda after a coordinated eradication campaign.
- The post helps explain the private-sector sinkhole and technical-assistance role behind the 2017 multinational operation.
- Microsoft's post adds the private-sector disruption perspective to the Andromeda takedown.
- It is useful for attributing the sinkhole and coordinated malware-eradication support that complemented the public-sector enforcement action.
- The Andromeda/Gamarue takedown combined Europol and FBI coordination, German and Belarusian enforcement action, and Microsoft-backed sinkhole support to disrupt a long-running malware ecosystem in late 2017.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against Andromeda Botnet, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Fbi and coordination to Europol Ec3, with participating or affected jurisdictions recorded as United States, Germany, Austria, Belgium, Finland, France, Italy, Netherlands, Poland, Spain, United Kingdom, Australia, Belarus, Canada, Montenegro, Singapore, Taiwan.

The cooperation model is documented through named agencies and partners: Fbi, Europol Ec3, J Cat, Eurojust, German Bka, Microsoft; mechanisms: Sinkholing and informal cooperation; enforcement posture: Arrest, Seizure, Takedown.

Operational results captured for the canonical record: 1 arrests; 1500 domains seized; Approximately 2 million victim IP addresses observed during a 48-hour sinkhole window; Andromeda/Gamarue infrastructure disrupted after a long-running eradication campaign.

The canonical source set contains 5 reference(s): 2017 12 04 Europol Europa Eu Andromeda Botnet Dismantled In International Cyber Operation, 2017 12 04 Microsoft Com Microsoft Assists Law Enforcement Help Disrupt Andromeda Botnet, 2026 04 18 Microsoft Com Gamarue Threat Profile, 2017 12 04 Bleepingcomputer Com Andromeda Botnet Gets Crushed, Portswigger 911 S5 Botnet Dismantling.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Andromeda Botnet Dismantled in International Cyber Operation | Europol | 2017-12-04 | https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation |
| [2] | Microsoft assists law enforcement to help disrupt the Andromeda botnet | Microsoft | 2017-12-04 | https://www.microsoft.com/en-us/msrc/blog/2018/01/microsoft-teams-up-with-law-enforcement-and-other-partners-to-disrupt-gamarue-andromeda |
| [3] | Gamarue threat profile | Microsoft | 2026-04-18 | https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/ |
| [4] | Andromeda Botnet Gets Crushed | BleepingComputer | 2017-12-04 | https://www.bleepingcomputer.com/news/security/andromeda-botnet-gets-crushed-in-eu-us-law-enforcement-operation/ |
| [5] | PortSwigger Daily Swig: Andromeda Botnet Dismantled by International Taskforce | PortSwigger (The Daily Swig) | 2017-12-05 | https://portswigger.net/daily-swig/andromeda-botnet-dismantled-by-international-taskforce |
