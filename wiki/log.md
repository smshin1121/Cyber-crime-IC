# Activity Log

## [2026-04-08] create | Wiki initialized
- Project structure created for International Cooperation on Cyber Crime domain
- CLAUDE.md schema and DESIGN.md written
- Empty index, log, overview, and category indexes created
- Ready for core content bootstrap and first source ingest

## [2026-04-08] create | Core content bootstrap (Phase 2)
- Pages created: budapest-convention.md, south-korea.md, mlat-process.md, 24-7-network.md, europol-ec3.md, interpol-igci.md, dual-criminality.md, territoriality-principle.md
- Total 8 pages covering: 1 legal framework, 1 country, 2 mechanisms, 2 organizations, 2 concepts
- Hub entities established: Budapest Convention, MLAT, South Korea
- Stub references created for: council-of-europe, second-additional-protocol, un-cybercrime-convention-2024, knpa-cyber-bureau, spo-international-cooperation, kisa, europol-jit, interpol-i247, direct-provider-request

## [2026-04-08] update | Domain correction
- Restructured from Cyber Threat Intelligence to International Cooperation
- Removed CTI categories (threat-actors, malware, vulnerabilities, techniques, etc.)
- Added IC categories (legal-frameworks, organizations, countries, operations, cases, mechanisms, procedures, crime-types, challenges)
- Rewrote CLAUDE.md and DESIGN.md for correct domain

## [2026-04-08] ingest | Operation Cronos Phase 1 (LockBit Disruption)
- Source: raw/press-releases/2024-02-20_europol_operation-cronos-lockbit.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-02-20-europol-operation-cronos-lockbit.md (source), operation-cronos-phase1.md (operation)
- Pages updated: europol-ec3.md
- Key metrics: 2 arrests, 34 servers seized, 10 countries, 12 agencies

## [2026-04-08] ingest | Operation Endgame Phase 1 (Botnet Takedown)
- Source: raw/press-releases/2024-05-30_europol_operation-endgame-botnet-takedown.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-05-30-europol-operation-endgame-botnet-takedown.md (source), operation-endgame-phase1.md (operation)
- Pages updated: europol-ec3.md
- Key metrics: 4 arrests, 100+ servers, 2,000+ domains, 13 countries, 15 agencies

## [2026-04-08] ingest | Operation Cronos Phase 3 (LockBit Arrests and Sanctions)
- Source: raw/press-releases/2024-10-01_europol_operation-cronos-lockbit-phase3.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-10-01-europol-operation-cronos-lockbit-phase3.md (source), operation-cronos-phase3.md (operation)
- Pages updated: europol-ec3.md
- Key metrics: 4 arrests, 9 servers seized, financial sanctions, 12 countries, 14 agencies

## [2026-04-08] ingest | Phobos/8Base Ransomware Crackdown
- Source: raw/press-releases/2025-02-11_europol_phobos-8base-ransomware-arrests.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-02-11-europol-phobos-8base-ransomware-arrests.md (source), phobos-8base-crackdown.md (operation)
- Pages updated: europol-ec3.md, south-korea.md
- Key metrics: 4 arrests, 27 servers, 400+ warned, 14 countries, 16 agencies, South Korea arrest/extradition

## [2026-04-08] ingest | Operation Endgame Phase 2 (Ransomware Kill Chain Disruption)
- Source: raw/press-releases/2025-05-23_europol_operation-endgame-phase2.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-05-23-europol-operation-endgame-phase2.md (source), operation-endgame-phase2.md (operation)
- Pages updated: europol-ec3.md
- Key metrics: 300 servers, 650 domains, EUR 3.5M seized, 20 warrants, 7 countries, 15 agencies

## [2026-04-08] ingest | Batch integration — entity stubs and crime type page
- Pages created: fbi-cyber-division.md (org stub), uk-nca.md (org stub), eurojust.md (org stub), ransomware-ic.md (crime type — full page)
- Pages updated: operations/_index.md, organizations/_index.md, sources/_index.md, crime-types/_index.md, countries/_index.md, index.md, overview.md
- Total: 14 pages created, 9 pages updated, 5 sources ingested
- Wiki page count: 8 -> 22

## [2026-04-08] ingest | Operation HAECHI V (INTERPOL Financial Crime)
- Source: raw/press-releases/2024-12-02_interpol_operation-haechi-v.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-12-02-interpol-operation-haechi-v.md (source), operation-haechi-v.md (operation)
- Pages updated: interpol-igci.md, south-korea.md
- Key metrics: 5,500+ arrests, USD 400M+ seized, 40 countries, Korean-Chinese voice phishing syndicate dismantled

## [2026-04-08] ingest | Operation Synergia II (INTERPOL Cyber Infrastructure)
- Source: raw/press-releases/2024-11-06_interpol_operation-synergia-ii.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-11-06-interpol-operation-synergia-ii.md (source), operation-synergia-ii.md (operation)
- Pages updated: interpol-igci.md, ransomware-ic.md
- Key metrics: 41 arrests, 22,800 IPs taken down, 59 servers seized, 95 countries

## [2026-04-08] ingest | Operation Serengeti (INTERPOL-AFRIPOL Africa)
- Source: raw/press-releases/2024-11-26_interpol_operation-serengeti.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-11-26-interpol-operation-serengeti.md (source), operation-serengeti.md (operation), afripol.md (org)
- Pages updated: interpol-igci.md, ransomware-ic.md
- Key metrics: 1,006 arrests, 134,089 malicious infrastructures dismantled, 19 African countries, USD 193M losses

## [2026-04-08] ingest | QakBot / Gallyamov Indictment (DOJ)
- Source: raw/press-releases/2025-05-22_doj_qakbot-gallyamov-indictment.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-05-22-doj-qakbot-gallyamov-indictment.md (source), qakbot-gallyamov-indictment.md (operation)
- Pages updated: fbi-cyber-division.md, europol-ec3.md, ransomware-ic.md
- Key metrics: 1 indicted (Gallyamov), USD 24M+ cryptocurrency seized, 7 countries + Europol

## [2026-04-08] ingest | Operation Checkmate — BlackSuit/Royal Ransomware Takedown (DOJ)
- Source: raw/press-releases/2025-08-11_doj_blacksuit-royal-ransomware-takedown.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-08-11-doj-blacksuit-royal-ransomware-takedown.md (source), operation-checkmate-blacksuit.md (operation)
- Pages updated: fbi-cyber-division.md, ransomware-ic.md
- Key metrics: 4 servers seized, 9 domains seized, USD 1.1M crypto, 8 countries, 5 US agencies

## [2026-04-08] ingest | i-Soon / APT27 Indictment (DOJ)
- Source: raw/press-releases/2025-03-05_doj_isoon-chinese-hackers-charges.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-03-05-doj-isoon-chinese-hackers-charges.md (source), isoon-apt27-indictment.md (operation)
- Pages updated: fbi-cyber-division.md, south-korea.md (as victim country)
- Key metrics: 12 Chinese nationals charged, Rewards for Justice up to USD 10M, Treasury sanctions

## [2026-04-08] ingest | Batch integration — new entity pages and index updates
- Pages created: online-fraud-ic.md (crime type), hacking-ic.md (crime type stub), afripol.md (org)
- Pages updated: operations/_index.md, organizations/_index.md, sources/_index.md, crime-types/_index.md, countries/_index.md, index.md, overview.md, log.md
- Total this batch: 15 pages created, 14 pages updated, 6 sources ingested
- Wiki page count: 22 -> 37

## [2026-04-08] ingest | Franco-Israeli CEO Fraud (Europol BEC)
- Source: _workspace/collected/2023-02-08_europol_franco-israeli-ceo-fraud-bust.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2023-02-08-europol-franco-israeli-ceo-fraud.md (source), franco-israeli-ceo-fraud.md (operation)
- Pages updated: europol-ec3.md
- Key metrics: 8 arrests, EUR 5.5M seized, 7 countries, EUR 38M single BEC theft

## [2026-04-08] ingest | Operation Jackal (INTERPOL vs Black Axe BEC)
- Source: _workspace/collected/2023-06-06_interpol_operation-jackal-black-axe-bec.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2023-06-06-interpol-operation-jackal.md (source), operation-jackal.md (operation)
- Pages updated: interpol-igci.md
- Key metrics: 103 arrests, EUR 2.15M seized, 21 countries, Black Axe target

## [2026-04-08] ingest | Operation Jackal III (INTERPOL vs Black Axe BEC Phase III)
- Source: _workspace/collected/2024-08-28_interpol_operation-jackal-iii-black-axe.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-08-28-interpol-operation-jackal-iii.md (source), operation-jackal-iii.md (operation)
- Pages updated: interpol-igci.md
- Key metrics: ~300 arrests, USD 3M seized, 21 countries, 720+ bank accounts blocked

## [2026-04-08] ingest | Operation Sentinel Africa (INTERPOL BEC/Ransomware)
- Source: _workspace/collected/2025-12-22_interpol_operation-sentinel-africa-bec.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-12-22-interpol-operation-sentinel-africa.md (source), operation-sentinel-africa.md (operation)
- Pages updated: interpol-igci.md
- Key metrics: 574 arrests, USD 3M recovered, 19 African countries, 6 ransomware variants decrypted

## [2026-04-08] ingest | Korea-China Voice Phishing Qingdao Joint Operation
- Source: _workspace/collected/2023-09-08_korea-china_voice-phishing-qingdao-joint-operation.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2023-09-08-korea-china-voice-phishing-qingdao.md (source), korea-china-voice-phishing-qingdao.md (operation)
- Pages updated: south-korea.md
- Key metrics: 16 arrests, KRW 2.7B losses, first Korea-China VP joint operation

## [2026-04-08] ingest | Operation HAECHI IV (INTERPOL Financial Crime)
- Source: _workspace/collected/2023-12-19_interpol_operation-haechi-iv.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2023-12-19-interpol-operation-haechi-iv.md (source), operation-haechi-iv.md (operation)
- Pages updated: interpol-igci.md, south-korea.md, online-fraud-ic.md
- Key metrics: 3,500 arrests, USD 300M seized, 34 countries, 82,112 bank accounts blocked

## [2026-04-08] ingest | Operation First Light 2024 (INTERPOL Online Scams)
- Source: _workspace/collected/2024-06-18_interpol_operation-first-light-2024.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2024-06-18-interpol-operation-first-light-2024.md (source), operation-first-light-2024.md (operation)
- Pages updated: interpol-igci.md, online-fraud-ic.md
- Key metrics: 3,950 arrests, USD 257M seized, 61 countries, 14,643 additional suspects

## [2026-04-08] ingest | Operation HAECHI VI (INTERPOL Financial Crime)
- Source: _workspace/collected/2025-09-25_interpol_operation-haechi-vi.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-09-25-interpol-operation-haechi-vi.md (source), operation-haechi-vi.md (operation)
- Pages updated: interpol-igci.md, south-korea.md, online-fraud-ic.md
- Key metrics: USD 439M recovered, 40 countries, 68,000+ bank accounts blocked, Korea-UAE I-GRIP recovery

## [2026-04-08] ingest | Korea-Cambodia Scam Centre Repatriation
- Source: _workspace/collected/2025-10-18_korea-cambodia_scam-centre-repatriation.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator
- Pages created: 2025-10-18-korea-cambodia-scam-repatriation.md (source), korea-cambodia-scam-repatriation.md (operation)
- Pages updated: south-korea.md
- Key metrics: 107+ repatriated from Cambodia, ~1,000 Koreans in Cambodian scam centres, USD 33M losses

## [2026-04-08] ingest | Batch integration — BEC/VP crime types, indexes, dashboard
- Pages created: bec-ic.md (crime type), voice-phishing-ic.md (crime type), seoul-metropolitan-police.md (org stub)
- Pages updated: operations/_index.md, organizations/_index.md, sources/_index.md, crime-types/_index.md, countries/_index.md, index.md, overview.md, log.md, ic-statistics-dashboard.md, online-fraud-ic.md, operation-haechi-v.md
- Total this batch: 21 pages created, 15 pages updated, 9 sources ingested
- Wiki page count: 37 -> 59
