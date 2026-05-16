---
type: operation
title: "Operation Endgame — Phase 3 (Infostealer + RAT + Botnet Disruption)"
title_ko: "오퍼레이션 엔드게임 — 페이즈 3 (정보탈취·RAT·봇넷 차단)"
aliases:
  - "Operation Endgame 2025-11"
  - "Endgame Phase 3"
  - "Endgame Rhadamanthys/VenomRAT/Elysium phase"
case_id: CYB-2025-201
period: 3
operation_role: phase
parent_operation: "[[operation-endgame]]"
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - search-seizure
  - arrest
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2025-11-13
  start: 2025-11
  end: 2025-11-13
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
  - "[[ransomware-ic]]"
  - "[[hacking-ic]]"
target_entity: "Rhadamanthys infostealer (malware-as-a-service since 2022), VenomRAT (RAT delivered via phishing), and the Elysium botnet"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[germany]]"
  - "[[france]]"
  - "[[netherlands]]"
  - "[[denmark]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[greece]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[france-gendarmerie]]"
  - "[[netherlands-politie]]"
  - "[[denmark-police]]"
  - "[[uk-nca]]"
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-dcis]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
organizations:
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[france-gendarmerie]]"
  - "[[netherlands-politie]]"
  - "[[denmark-police]]"
  - "[[uk-nca]]"
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-dcis]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[eurojust-coordination-meeting]]"
legal_basis:
  []
results:
  arrests: 1
  indictments: 0
  servers_seized: 1025
  domains_seized: 20
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1,025 servers worldwide shut down"
    - "20 domains seized"
    - "11 searches conducted across participating jurisdictions"
    - "Login data from over 100,000 cryptocurrency wallets recovered (stolen but not yet exploited per Eurojust)"
    - "Three named malware families disrupted: Rhadamanthys (infostealer), VenomRAT (RAT), and Elysium (botnet)"
    - "Main RAT-line suspect arrested in Greece"
edges:
  - source_actor: europol-ec3
    target_actor: eurojust
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: germany-bka
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: uk-nca
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: australia-afp
    target_actor: fbi
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments (the cited Eurojust release does not enumerate downstream charging counts)"
  - "victims_notified (release attributes 600,000+ infected victims to the cited malware families across multiple sources)"
related_cases:
  []
related_operations:
  - "[[operation-endgame]]"
  - "[[operation-endgame-phase1]]"
  - "[[operation-endgame-phase2]]"
  - "[[hellenic-police-endgame-venomrat-mastermind-attica-arrest-2025]]"
challenges_encountered:
  []
lessons_learned:
  - "Endgame Phase 3 shifts the umbrella's targeting from dropper/loader infrastructure (Phase 1) and ransomware-affiliate kill chain (Phase 2) to the initial-access stack — infostealer-as-a-service, RAT, and a downstream botnet. The same coordinating bodies (Europol + Eurojust) and a substantially overlapping core-partner roster (DE, FR, NL, DK, UK, US) maintain continuity across phases."
  - "Greece enters the Endgame partner roster for the first time in this phase via the RAT-suspect arrest, demonstrating extension of the umbrella's geographic enforcement reach beyond the prior six-country core."
source_count: 1
sources:
  - "[[2025-11-13_eurojust_operation-endgame-phase3-malware-operation]]"
summary: "Phase 3 of the Europol- and Eurojust-coordinated Operation Endgame, announced on 2025-11-13. The operation dismantled 1,025 servers worldwide, seized 20 domains, conducted 11 searches across participating jurisdictions, recovered login data from over 100,000 cryptocurrency wallets, and arrested a main RAT-line suspect in Greece. Three malware families were disrupted: Rhadamanthys (infostealer-as-a-service since 2022), VenomRAT (RAT delivered via phishing), and Elysium (associated botnet). Tier-1 participating-authorities roster (verbatim from Eurojust): Germany (BKA + Frankfurt PPO), France (Paris PPO J3 + JUNALCO + BL2C + OFAC), Netherlands (NPP + Politie), Denmark (Prosecution + Police), UK (NCA), US (DOJ + FBI + DCIS), Australia (AFP), Canada (RCMP + Sûreté du Québec); Greece named for the arrest action."
created: 2026-05-08
updated: 2026-05-16
---
## Summary

The 13 November 2025 phase of [[operation-endgame|Operation Endgame]] dismantled the criminal infrastructure behind three named malware families — the Rhadamanthys infostealer (a malware-as-a-service offering surfacing in 2022), the VenomRAT Remote Access Trojan (delivered via phishing), and the Elysium associated botnet. The Eurojust release reports 1,025 servers worldwide shut down, 20 domains seized, 11 searches conducted across participating jurisdictions, and login data recovered from over 100,000 cryptocurrency wallets that had been stolen but not yet exploited. One main RAT-line suspect was arrested in Greece.

The action was coordinated "from the outset" through [[europol-ec3|Europol]] and [[eurojust|Eurojust]]. The cited tier-1 release names eight participating authorities verbatim, plus Greece for the RAT-line arrest. The release does not designate the operation as a formal [[europol-jit|Joint Investigation Team]] or use the JIT acronym.

## Background

Operation Endgame is a multi-phase Europol- and Eurojust-coordinated international cooperation against the criminal infrastructure that underwrites large-scale cybercrime, beginning with the May 2024 dropper/loader takedown ([[operation-endgame-phase1|Phase 1]]) and continuing with the May 2025 ransomware-affiliate kill-chain disruption ([[operation-endgame-phase2|Phase 2]]). Phase 3 represents a shift in targeting from dropper/loader infrastructure (Phase 1) and ransomware-affiliate kill chain (Phase 2) to the initial-access stack — infostealer-as-a-service, RAT, and downstream botnet — while preserving continuity in the coordinating bodies (Europol + Eurojust) and the core-partner roster (DE, FR, NL, DK, UK, US).

## Participating Parties

| Role | Parties |
|---|---|
| Coordinating bodies | [[europol-ec3\|Europol]] and [[eurojust\|Eurojust]] |
| Germany | [[germany-bka\|German Federal Criminal Police Office (BKA)]]; [[germany-frankfurt-prosecutor\|Public Prosecutor General's Office Frankfurt am Main – Cybercrime Office]] |
| France | PPO Paris Cybercrime unit J3; Investigative judges JUNALCO; BL2C (Cyber unit of Paris Police Prefecture); [[france-gendarmerie\|OFAC (Central Office against cybercrime)]] |
| Netherlands | Netherlands Public Prosecution Service (National Office); [[netherlands-politie\|Netherlands Police]] |
| Denmark | Danish Prosecution Service; [[denmark-police\|Danish Police]] |
| United Kingdom | [[uk-nca\|National Crime Agency (NCA)]] |
| United States | [[us-doj\|Department of Justice]]; [[fbi\|FBI]]; [[us-dcis\|Defense Criminal Investigative Service]] |
| Australia | [[australia-afp\|Australian Federal Police (AFP)]] |
| Canada | [[canada-rcmp\|Royal Canadian Mounted Police (RCMP)]]; Sûreté du Québec |
| Greece | (arrest jurisdiction; Hellenic Police agency not named in release) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2024-05-30 | Operation Endgame Phase 1 announced (dropper/loader takedown) | (See [[operation-endgame-phase1]]) |
| 2025-05-23 | Operation Endgame Phase 2 announced (ransomware kill-chain disruption) | (See [[operation-endgame-phase2]]) |
| 2025-11-13 | Operation Endgame Phase 3 announced (infostealer + RAT + botnet disruption) | Eurojust 2025-11-13 |

## Results and Impact

- 1,025 servers worldwide shut down.
- 20 domains seized.
- 11 searches conducted across participating jurisdictions.
- Login data recovered from over 100,000 cryptocurrency wallets (stolen but not yet exploited per Eurojust).
- Three named malware families disrupted: Rhadamanthys (infostealer-as-a-service since 2022), VenomRAT (RAT), and Elysium (botnet).
- One main RAT-line suspect arrested in Greece.

## Cooperation Mechanisms Used

The cited tier-1 release describes coordination "from the outset through Eurojust and Europol" with parallel domestic enforcement actions in the eight named jurisdictions. The release does not designate the operation as a Joint Investigation Team (JIT) or invoke a specific MLAT instrument; the legal-basis classification therefore follows [[search-seizure|domestic search-and-seizure]] and [[domain-seizure|domain seizure]] instruments executed in each participating jurisdiction during the action window.

## Korean Involvement (한국의 참여)

South Korea is not named in the Eurojust release among the participating authorities or among the arrest jurisdictions for this phase of Operation Endgame. The case is recorded in the wiki for the umbrella enrichment and the verbatim eight-country participating-authorities roster; Korean malware / RAT IC posture is not directly informed by this source.

## Contradictions & Open Questions

- Tier-2 same-day reporting (CyberNews, eSecurity Planet) widens the participating-countries roster of the November 2025 phase to include Belgium and Lithuania alongside the eight Eurojust-named jurisdictions and Greece. Those two countries are not named in the cited tier-1 Eurojust release and are therefore not added to the wiki record's `participating_countries`. The Europol-side release for the same announcement may name them explicitly; this is flagged for follow-up.
- The exact date of the Greek arrest is not given in the cited Eurojust release body; corroborating tier-2 reporting cites 2025-11-03.
- Per-country search counts and per-country cryptocurrency-wallet recovery breakdowns are not enumerated in the cited release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-11-13_eurojust_operation-endgame-phase3-malware-operation\|Authorities continue to protect citizens from cybercriminals during major malware operation]] | Eurojust | 2025-11-13 | https://www.eurojust.europa.eu/news/authorities-continue-protect-citizens-cybercriminals-during-major-malware-operation |
