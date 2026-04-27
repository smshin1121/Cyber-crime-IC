---
type: operation
title: "Operation Endgame — Phase 1 (Botnet Takedown)"
aliases:
  - "Operation Endgame Phase 1"
  - "Endgame botnet takedown May 2024"
operation_type: takedown
status: completed
case_id: CYB-2024-003
period: 3
enforcement_type:
  - arrest
  - seizure
  - takedown
  - asset_freeze
outcome: success
credibility_index: 2.28
source_tier: 2
edges:
  - source_actor: Europol
    target_actor: "German BKA"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: Eurojust
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
missing_fields:
  - legal_basis
  - mechanisms_used
timeframe:
  announced: 2024-05-30
  start: 2024-05-27
  end: 2024-05-29
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "Dropper malware ecosystem (IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot)"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[armenia]]"
  - "[[bulgaria]]"
  - "[[lithuania]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[switzerland]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[denmark-police]]"
  - "[[france-national-police]]"
  - "[[germany-bka]]"
  - "[[netherlands-politie]]"
  - "[[uk-nca]]"
  - "[[fbi-cyber-division]]"
  - "[[armenia-police]]"
  - "[[bulgaria-police]]"
  - "[[lithuania-police]]"
  - "[[portugal-police]]"
  - "[[romania-police]]"
  - "[[switzerland-fedpol]]"
  - "[[ukraine-police]]"
legal_basis:

mechanisms_used:

results:
  arrests: 4
  indictments: 0
  servers_seized: 100
  domains_seized: 2000
  cryptocurrency_seized: "EUR 69 million (accumulated by key suspect)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "16 location searches conducted"
    - "Command post with 20+ officers at Europol HQ"
related_cases:

related_operations:
  - "[[operation-endgame-phase2]]"
challenges_encountered:

lessons_learned:
  - "Targeting upstream infrastructure (dropper malware) disrupts the entire ransomware supply chain"
  - "On-site command post at Europol HQ with 20+ officers from 4 countries enabled real-time coordination"
  - "Scale of 100+ servers and 2,000+ domains required coordinated simultaneous action across 10 countries"
source_count: 5
sources:
  - "[[2024-05-30-europol-operation-endgame-botnet-takedown]]"
  - "[[2024-05-29_fbi-gov_operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-o]]"
  - "[[2024-05-30_bmi-bund-de_worldwide-investigation-against-cyber-crime-crowned-by-success]]"
  - "[[2024-05-30_krebsonsecurity-com_operation-endgame-hits-malware-delivery-platforms]]"
  - "[[2026-04-17_europol-europa-eu_operation-endgame-official-page]]"
created: 2026-04-08
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "**Operation Endgame Phase 1** was the **largest-ever international operation against botnets**, conducted between 27 and 29 May 2024. The operation targeted dropper malware families — IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, and Trickbot — that serve as initial-access vectors for ransomware groups. Coordinated from [[europol-ec3|Europol]]'s headquarters with a command post of 20+ officers, the action resulted in 4 arrests, 100+ servers taken down across 10 countries, and 2,000+ domains seized."
jurisdictions:
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[armenia]]"
  - "[[bulgaria]]"
  - "[[lithuania]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[switzerland]]"
  - "[[ukraine]]"
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[denmark-police]]"
  - "[[france-national-police]]"
  - "[[germany-bka]]"
  - "[[netherlands-politie]]"
  - "[[uk-nca]]"
  - "[[fbi-cyber-division]]"
  - "[[armenia-police]]"
  - "[[bulgaria-police]]"
  - "[[lithuania-police]]"
  - "[[portugal-police]]"
  - "[[romania-police]]"
  - "[[switzerland-fedpol]]"
  - "[[ukraine-police]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
---
## Summary

**Operation Endgame Phase 1** was the **largest-ever international operation against botnets**, conducted between 27 and 29 May 2024. The operation targeted dropper malware families — IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, and Trickbot — that serve as initial-access vectors for ransomware groups. Coordinated from [[europol-ec3|Europol]]'s headquarters with a command post of 20+ officers, the action resulted in 4 arrests, 100+ servers taken down across 10 countries, and 2,000+ domains seized.

The operation *almost certainly* represented a strategic shift in international ransomware enforcement: rather than targeting ransomware operators directly, it struck at the infrastructure that enables ransomware deployment in the first place.

## Background

Dropper malware (also known as "loaders" or "initial access brokers") forms the first stage of the ransomware attack chain. These malware families infect systems and then sell or provide access to ransomware operators. The targeted families — IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, and Trickbot — were linked to at least **15 ransomware groups**, including BlackBasta, REvil, and Conti.

By disrupting the dropper ecosystem, law enforcement aimed to break the ransomware kill chain at its earliest point, a strategy that would become even more pronounced in [[operation-endgame-phase2|Phase 2]].

## Participating Parties

### Coordinating Body
- [[europol-ec3|Europol]] — hosted command post at HQ with 20+ officers

### Judicial Coordination
- [[eurojust|Eurojust]]

### Participating Countries (6 primary + 7 supporting)
**Primary:** Denmark, France, Germany, Netherlands, United Kingdom, United States
**Supporting:** Armenia, Bulgaria, Lithuania, Portugal, Romania, Switzerland, Ukraine

### Participating Agencies (15)
[[europol-ec3]], [[eurojust]], [[denmark-police|Danish Police]], [[france-national-police|French National Police]], [[germany-bka|German BKA]], [[netherlands-politie|Dutch National Police]], [[uk-nca|UK NCA]], [[fbi-cyber-division|FBI]], [[armenia-police|Armenian Police]], [[bulgaria-police|Bulgarian Police]], [[lithuania-police|Lithuanian Police]], [[portugal-police|Portuguese Police]], [[romania-police|Romanian Police]], [[switzerland-fedpol|Swiss Fedpol]], [[ukraine-police|Ukrainian Police]]

## Legal Framework

The operation involved law enforcement and judicial authorities from 13 countries. Arrests were conducted in Armenia (1) and Ukraine (3).

> [!warning] Legal status check needed
> Specific legal bases and treaty provisions for the cross-border enforcement actions need to be identified from additional sources.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2024 | Multi-country investigation phase |
| 2024-05-27 | Action days begin |
| 2024-05-27 to 2024-05-29 | Servers taken down, domains seized, arrests executed |
| 2024-05-30 | Public announcement by Europol |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 4 (1 Armenia, 3 Ukraine) |
| Location searches | 16 |
| Servers taken down | 100+ (across 10 countries) |
| Domains seized | 2,000+ |
| Cryptocurrency (key suspect) | EUR 69 million accumulated |
| Malware families targeted | 6 |
| Linked ransomware groups | 15+ |

## Cooperation Mechanisms Used

- **Europol command post:** On-site coordination center at Europol HQ with 20+ officers from Denmark, France, Germany, and the US
- **Eurojust coordination meetings:** Judicial coordination for multi-jurisdictional arrest warrants and seizure orders

## Lessons Learned

1. **Attack the supply chain:** Targeting dropper malware infrastructure disrupts multiple ransomware operations simultaneously, providing a force-multiplier effect compared to targeting individual ransomware groups.
2. **Real-time coordination center:** The 20+ officer command post at Europol HQ enabled rapid decision-making and synchronized action across time zones.
3. **Scale requires coordination:** Taking down 100+ servers and 2,000+ domains simultaneously across 10 countries requires a level of coordination that *almost certainly* could not be achieved without dedicated institutional support from Europol and Eurojust.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.


- [[operation-endgame-phase2|Operation Endgame Phase 2]] (May 2025): 300 servers taken down, 650 domains neutralized, EUR 3.5M cryptocurrency seized, 20 international arrest warrants issued

## Korean Involvement (한국의 참여)

No direct Korean involvement in Operation Endgame Phase 1 was identified.

## Contradictions & Open Questions

- What specific ransomware groups lost access as a direct result of the dropper takedown?
- What was the measurable impact on ransomware deployment rates following the operation?
- How quickly did the targeted malware families reconstitute after the takedown?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2024-05-30: Largest ever operation against botnets hits dropper malware ecosystem - Operation Endgame.
- FBI, 2024-05-29: Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals.
- German BMI, 2024-05-30: Worldwide investigation against cyber crime crowned by success.
- KrebsOnSecurity, 2024-05-30: 'Operation Endgame' Hits Malware Delivery Platforms.
- Europol, 2026-04-17: Operation Endgame — official page.

## Evidence and Attribution Notes

- Operation Endgame Phase 1 was the largest-ever international action against botnets, conducted 27-29 May 2024
- Targeted dropper malware families: IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot
- 4 arrests (1 Armenia, 3 Ukraine), 100+ servers taken down across 10 countries, 2,000+ domains seized
- Key suspect accumulated at least EUR 69 million in cryptocurrency from renting criminal infrastructure
- Malware droppers linked to at least 15 ransomware groups including BlackBasta, REvil, Conti
- Between 27 and 29 May 2024, **Operation Endgame** — the largest-ever international action against botnets — targeted dropper malware families including IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, and Trickbot.
- Coordinated from Europol's headquarters with a command post of 20+ officers from Denmark, France, Germany, and the US, the operation resulted in 4 arrests, over 100 servers taken down across 10 countries, and over 2,000 domains seized.
- These malware droppers serve as initial-access vectors linked to at least 15 ransomware groups, including BlackBasta, REvil, and Conti.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2024-05-29: Law enforcement in Ukraine, Portugal, Romania, Lithuania, Bulgaria, and Switzerland supported police actions to arrest or interview suspects, conduct searches, and seize or take down servers.
- FBI, 2024-05-29: Beginning on May 28, 2024, the first coordinated international operation of its kind involved a dozen countries that conducted searches, questioned or arrested subjects, and took down or disrupted more than 100 servers to defeat multiple malware variants.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against Dropper malware ecosystem (IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot), rather than a defendant-specific follow-on action. The record attributes lead responsibility to Europol Ec3 and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Denmark, France, Germany, Netherlands, United Kingdom, United States, Armenia, Bulgaria, Lithuania, Portugal, Romania, Switzerland, Ukraine.

The cooperation model is documented through named agencies and partners: Europol Ec3, Eurojust, Denmark Police, France National Police, Germany Bka, Netherlands Politie, Uk Nca, Fbi Cyber Division, Armenia Police, Bulgaria Police; enforcement posture: Arrest, Seizure, Takedown, Asset Freeze.

Operational results captured for the canonical record: 4 arrests; 100 servers seized; 2000 domains seized; cryptocurrency/asset result recorded as EUR 69 million (accumulated by key suspect); 16 location searches conducted; Command post with 20+ officers at Europol HQ.

The canonical source set contains 5 reference(s): 2024 05 30 Europol Operation Endgame Botnet Takedown, 2024 05 29 Fbi Gov Operation Endgame Coordinated Worldwide Law Enforcement Action Against Network O, 2024 05 30 Bmi Bund De Worldwide Investigation Against Cyber Crime Crowned By Success, 2024 05 30 Krebsonsecurity Com Operation Endgame Hits Malware Delivery Platforms, 2026 04 17 Europol Europa Eu Operation Endgame Official Page.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis and Mechanisms Used.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Largest ever operation against botnets hits dropper malware ecosystem - Operation Endgame | Europol | 2024-05-30 | https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem |
| [2] | Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals | FBI | 2024-05-29 | https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals |
| [3] | Worldwide investigation against cyber crime crowned by success | German BMI | 2024-05-30 | https://www.bmi.bund.de/SharedDocs/kurzmeldungen/EN/2024/05/endgame.html |
| [4] | 'Operation Endgame' Hits Malware Delivery Platforms | KrebsOnSecurity | 2024-05-30 | https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/ |
| [5] | Operation Endgame — official page | Europol | 2026-04-17 | https://www.europol.europa.eu/operations-services-and-innovation/operations/operation-endgame |
