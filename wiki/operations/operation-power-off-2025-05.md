---
type: operation
title: "Operation PowerOFF (2025-05 Polish-led DDoS-for-hire takedown phase)"
title_ko: "Operation PowerOFF (2025-05 폴란드 주도 DDoS-for-hire 단속 단계)"
aliases:
  - "Operation PowerOFF May 2025"
  - "Polish DDoS-for-hire empire takedown 2025"
  - "Cfxapi Cfxsecurity neostress jetstress quickdown zapcut takedown 2025"
case_id: CYB-2025-214
period: 3
operation_role: follow-on
parent_operation: "[[operation-power-off]]"
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - infrastructure-seizure
  - domain-seizure
outcome: success
timeframe:
  announced: 2025-05-07
  start: 2022
  end: 2025-05
  ongoing: false
crime_type: "[[ddos-ic]]"
crime_types:
  - "[[ddos-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "Six interlinked DDoS-for-hire (stresser/booter) services — Cfxapi, Cfxsecurity, neostress, jetstress, quickdown, and zapcut — that operated 2022-2025 with slick no-technical-skills user interfaces enabling target-IP/attack-type/duration/fee-driven automated DDoS attacks against schools, government services, businesses, and gaming platforms"
lead_agency: "[[poland-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[poland]]"
  - "[[united-states]]"
  - "[[germany]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[poland-police]]"
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[germany-bka]]"
  - "[[dutch-police]]"
organizations:
  - "[[europol-ec3]]"
  - "[[poland-police]]"
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[germany-bka]]"
  - "[[dutch-police]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Polish search-and-arrest warrants executed by Central Cybercrime Bureau (Centralne Biuro Zwalczania Cyberprzestępczości / CBZC)"
  - "US domain-seizure warrants under USDOJ + FBI + HSI + DCIS authority"
  - "German support under BKA + Prosecutor General's Office Frankfurt am Main — Cyber Crime Centre (ZIT)"
  - "Dutch data-centre infrastructure seizure under National Police authority"
  - "Operation PowerOFF framework as multi-year umbrella for DDoS-for-hire takedown phases (parent: [[operation-power-off]])"
results:
  arrests: 4
  indictments: 0
  servers_seized: 0
  domains_seized: 9
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "4 admin arrests in Poland by Central Cybercrime Bureau (CBZC), running 6 stresser/booter services"
    - "9 booter-service domains seized in the United States during the coordinated week of action"
    - "Underlying disrupted services: Cfxapi, Cfxsecurity, neostress, jetstress, quickdown, zapcut (active 2022-2025)"
    - "Attack victims: schools, government services, businesses, and gaming platforms"
    - "Dutch warning campaign: fake booter sites deployed as deterrence"
    - "Dutch data-centre seizure data shared with Polish investigators (contributed to the 4-admin arrests)"
    - "German BKA + ZIT Frankfurt identified one suspect and shared intelligence on others"
edges:
  - source_actor: poland-police
    target_actor: dutch-police
    cooperation_type: data_sharing
    legal_basis: bilateral
    direction: directed
  - source_actor: poland-police
    target_actor: germany-bka
    cooperation_type: info_sharing
    legal_basis: bilateral
    direction: directed
  - source_actor: poland-police
    target_actor: fbi
    cooperation_type: info_sharing
    legal_basis: bilateral
    direction: undirected
  - source_actor: europol-ec3
    target_actor: poland-police
    cooperation_type: coordination
    legal_basis: europol-j-cat
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific names of the 4 Polish-arrested administrators"
  - "specific 9 US booter-service domain names seized"
  - "victim counts and cumulative DDoS-attack volumes attributable to the 6 services"
  - "specific data-centre locations of the Dutch infrastructure seizures"
related_cases:
  []
related_operations:
  - "[[operation-power-off]]"
  - "[[operation-power-off-2026-04]]"
  - "[[de-hesse-rlp-flight-rcs-dstat-cc-poweroff-takedown-2024]]"
challenges_encountered:
  []
lessons_learned:
  - "First wiki record of the Polish Central Cybercrime Bureau (Centralne Biuro Zwalczania Cyberprzestępczości / CBZC) as the lead Polish federal-cybercrime authority for an Operation PowerOFF phase."
  - "First wiki record of the Dutch fake-booter-site warning methodology as a discrete deception-based deterrence IC mechanism class — Dutch authorities running honeypot websites that warn users seeking out DDoS-for-hire services."
  - "Demonstrates a Polish-lead + US-domain-seizure + Dutch-data-sharing + German-suspect-ID 4-channel cooperation pattern under the Operation PowerOFF umbrella, distinct from the broader 21-country [[operation-power-off-2026-04|April 2026 PowerOFF phase]] which scaled to a sweeping warning + arrest + domain-seizure architecture."
  - "Establishes the centralised-rented-infrastructure DDoS-as-a-service pattern as a discrete cybercrime business model class, contrasted with traditional infected-device botnet DDoS in primary Europol documentation."
source_count: 1
sources:
  - "[[2025-05-07_europol_ddos-for-hire-empire-poland-4-administrators-us-9-domains]]"
summary: "On 2025-05-07 Europol announced the May 2025 phase of Operation PowerOFF: a 4-country (Germany, Netherlands, Poland, USA) coordinated takedown of a DDoS-for-hire empire running 6 stresser/booter services (Cfxapi, Cfxsecurity, neostress, jetstress, quickdown, zapcut) active 2022-2025. Polish Central Cybercrime Bureau (CBZC) arrested 4 administrators in Poland; US (USDOJ + FBI + HSI + DCIS) seized 9 booter-service domains during the coordinated week of action; Dutch authorities deployed fake booter sites as warnings and shared data from data-centre seizures with Polish investigators; German BKA + Prosecutor General's Office Frankfurt am Main — Cyber Crime Centre (ZIT) identified one suspect and shared intelligence on others. Europol EC3 provided analytical and operational support."
created: 2026-05-09
updated: 2026-05-16
---
## Summary

On **2025-05-07** Europol announced the **May 2025 phase of Operation PowerOFF** — a 4-country (**Germany, Netherlands, Poland, USA**) coordinated takedown of a DDoS-for-hire empire running **6 stresser/booter services** active 2022-2025: **Cfxapi, Cfxsecurity, neostress, jetstress, quickdown, and zapcut**. The **Polish Central Cybercrime Bureau (Centralne Biuro Zwalczania Cyberprzestępczości / CBZC)** arrested **4 administrators in Poland**; the **United States** (USDOJ + FBI + HSI + DCIS) seized **9 booter-service domains** during the coordinated week of action. **Dutch authorities** deployed fake booter sites as warnings and shared data from Dutch-data-centre seizures with Polish investigators. **German** authorities (BKA + ZIT Frankfurt) identified one suspect and shared intelligence on others. **Europol EC3** provided analytical and operational support throughout.

## Background

Stresser and booter services offer **on-demand cyberattacks**, often disguised as legitimate testing tools but widely used to cause deliberate disruption. They flood a target server or website with enormous volumes of fake traffic, making them inaccessible to real users (DDoS attacks). The released release describes the Cfxapi/Cfxsecurity/neostress/jetstress/quickdown/zapcut family as **industrialised DDoS-as-a-service** with slick UIs that required no technical skills (target IP + attack type + duration + fee → automated DDoS) and centralised rented infrastructure (rather than traditional infected-device botnets). Targets included **schools, government services, businesses, and gaming platforms**.

## Participating Parties

| Country | Lead Authority |
|---|---|
| Germany | [[germany-bka\|Federal Criminal Police Office (Bundeskriminalamt / BKA)]]; Prosecutor General's Office Frankfurt am Main — Cyber Crime Centre (ZIT) |
| Netherlands | [[dutch-police\|National Police of the Netherlands (Politie)]] |
| Poland | [[poland-police\|Central Cybercrime Bureau (Centralne Biuro Zwalczania Cyberprzestępczości / CBZC)]] |
| USA | [[us-doj\|US Department of Justice (USDOJ)]]; [[fbi\|Federal Bureau of Investigation (FBI)]]; Homeland Security Investigations (HSI); Defense Criminal Investigative Service (DCIS) |
| Coordination | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] (analytical and operational support throughout) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2022 — 2025 | Cfxapi/Cfxsecurity/neostress/jetstress/quickdown/zapcut DDoS-for-hire services active | Europol 2025-05-07 |
| (date not enumerated) | Dutch authorities seize data from booter websites in NL data centres; data shared with Polish investigators | Europol 2025-05-07 |
| (date not enumerated) | German BKA + ZIT Frankfurt identify one suspect; share intelligence on others with Poland | Europol 2025-05-07 |
| (date not enumerated) | Dutch authorities deploy fake booter sites as warnings to potential users | Europol 2025-05-07 |
| 2025-05 (action week) | Polish CBZC arrests 4 administrators; US seizes 9 booter-service domains | Europol 2025-05-07 |
| 2025-05-07 | Public announcement | Europol 2025-05-07 |

## Results and Impact

- **4 admin arrests** in Poland by CBZC.
- **9 booter-service domains seized** in the United States.
- **6 services dismantled**: Cfxapi, Cfxsecurity, neostress, jetstress, quickdown, zapcut.
- **2022-2025 service activity period**.
- **Dutch fake-booter-site warning campaign** deployed.
- **German BKA + ZIT Frankfurt suspect-identification** + intelligence-sharing.
- **Europol EC3** analytical and operational support throughout the investigation.

## Cooperation Mechanisms Used

The cited release describes four discrete IC mechanism classes for this phase:

1. **Polish CBZC as action-day lead** — first wiki record of CBZC as a Polish federal-cybercrime authority leading an Operation PowerOFF phase.
2. **Dutch fake-booter-site warning methodology** — first wiki record of this specific deception-based deterrence mechanism in the wiki corpus.
3. **Dutch data-centre seizure data shared with Polish investigators** — discrete IC mechanism class for cross-border data transfer from infrastructure seizure to suspect identification.
4. **Concurrent US-domain-seizure during the coordinated week of action** — parallel administrative-and-criminal action pattern.

The action is part of [[operation-power-off|Operation PowerOFF]], an ongoing multi-year international law enforcement effort targeting the infrastructure behind DDoS-for-hire activity. The May 2025 phase precedes the broader 21-country [[operation-power-off-2026-04|April 2026 PowerOFF phase]] in the wiki's PowerOFF chronology.

## Korean Involvement (한국의 참여)

South Korea is not named among the participating jurisdictions in the cited Europol release for this phase. The case is recorded in the wiki for the Polish-lead + US-domain-seizure + Dutch-data-sharing + German-suspect-ID 4-channel cooperation pattern. Korean exposure to the 6 dismantled services as either victim-target or user is not enumerated.

## Contradictions & Open Questions

- The cited release does not enumerate the specific names of the 4 Polish-arrested administrators.
- The 9 specific US booter-service domain names seized are not enumerated in the cited Europol release; cross-reference with USDOJ press releases would be needed.
- Victim counts and cumulative DDoS-attack volumes attributable to the 6 services are not enumerated.
- Specific data-centre locations of the Dutch infrastructure seizures are not enumerated.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-05-07_europol_ddos-for-hire-empire-poland-4-administrators-us-9-domains\|DDoS-for-hire empire brought down: Poland arrests 4 administrators, US seizes 9 domains]] | Europol | 2025-05-07 | https://www.europol.europa.eu/media-press/newsroom/news/ddos-for-hire-empire-brought-down-poland-arrests-4-administrators-us-seizes-9-domains |
