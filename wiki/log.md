# Activity Log

## [2026-04-14] source-enrichment pilot | 5 operations with empty sources enriched
- Pilot scope: 5 of 19 operations that had empty `sources: []` frontmatter
- Targets: alphabay-takedown, emotet-takedown, operation-morpheus, operation-trojan-shield (Tier 1), zambia-golden-top-call-center (Tier 2 fallback)
- Sources created (14): 5 for alphabay (Europol/DOJ/DEA/FBI/UNODC), 4 for emotet (Europol/DOJ/Eurojust/DOJ-MDNC), 1 for morpheus (NCA), 2 for trojan-shield (FBI/Europol), 2 for zambia (The Record/Bitdefender)
- Operation pages updated: 5 (frontmatter sources + source_count + updated date)
- Data corrections: zambia-golden-top raid date 2025→2024 (L16 cascade caught); emotet dead politie.nl URL pruned; morpheus Hacker News Tier-3 row replaced with NCA Tier-1
- Methodology doc: `_workspace/source-enrichment-method.md` — scaling estimate for remaining 14 ops: ~50 min wall-clock with 4 parallel agents
- Lint: CRITICAL 0 / HIGH 0 / MEDIUM 0 / LOW 16 (unchanged from baseline)
- check_links.py: broken 0 (unchanged)

## [2026-04-14] ingest | 4 Eurojust press releases (Eurojust RSS 복구 후 첫 수집분)
- Sources: raw/press-releases/2026-04-14_eurojust_cryptocurrency-mixing-service-used-to-launder-money-taken-do.md, raw/press-releases/2026-04-14_eurojust_european-judicial-cybercrime-network-strengthens-resolve-to.md, raw/press-releases/2026-04-14_eurojust_judicial-cooperation-key-to-arresting-leaders-of-online-frau.md, raw/press-releases/2026-04-14_eurojust_servers-used-for-cybercrime-around-the-world-taken-down.md
- Pages created (10):
  - sources/2025-12-01-eurojust-de-ch-crypto-mixer-takedown.md
  - sources/2025-12-05-eurojust-ejcn-19th-plenary.md
  - sources/2026-03-11-eurojust-de-fr-online-fraud-group.md
  - sources/2026-03-12-eurojust-proxy-service-takedown.md
  - operations/de-ch-crypto-mixer-takedown-2025.md (DE+CH crypto mixer takedown, EUR 25M+ seized, 3 servers, published 2025-12-01)
  - operations/proxy-service-takedown-2026-03.md (FR/AT/NL/US +4 unnamed, 102 victim countries, IP proxy + payment platform, published 2026-03-12)
  - mechanisms/european-judicial-cybercrime-network.md (EJCN — Eurojust-administered prosecutorial liaison network; 19th plenary 2025-12-04/05, 62 experts from 26 countries)
  - cases/de-fr-online-fraud-group-2026.md (DE-FR bilateral online fraud prosecution, ~EUR 1M victim losses, published 2026-03-11)
  - countries/austria.md (stub created — first wiki page for Austria)
  - crime-types/money-laundering-ic.md (new crime type page for cryptocurrency-enabled money laundering IC)
- Pages updated (10): organizations/eurojust.md (+4 ops/case/mechanism, +4 sources), organizations/europol-ec3.md (+2 ops, +2 sources), countries/germany.md (+1 op, +1 case, +2 sources), countries/switzerland.md (+1 op, +1 source), countries/france.md (+1 op, +1 case, +2 sources), countries/netherlands.md (+1 op, +1 source), countries/united-states.md (+1 op, +1 source), crime-types/online-fraud-ic.md (+1 case, +1 source), crime-types/hacking-ic.md (+1 op, +1 source), wiki/index.md (master catalog, +1 case section, mechanisms/crime-types bumped)
- Indexes updated: operations/_index.md (+2), cases/_index.md (+1, first entry ever), mechanisms/_index.md (+1), sources/_index.md (+4), countries/_index.md (+austria), crime-types/_index.md (+money-laundering-ic, updated 2 rows)
- Key findings:
  - **DE-CH crypto mixer takedown (2025-12-01)**: First fully-documented Germany-Switzerland bilateral cryptocurrency mixing service takedown in the wiki — EUR 25M+ seized, 3 servers down. Switzerland's role *likely* limited to asset freezing per source; service name not disclosed.
  - **Proxy service takedown (2026-03-12)**: FR/AT/NL/US named, 4 unnamed; 102 victim countries; *highly likely* a residential proxy botnet given the malware-victim framing in the source.
  - **EJCN existence catalogued**: First Eurojust judicial cybercrime *network* (as distinct from operational casework) documented in wiki — Council Conclusions (2016) basis, 19th plenary in Dec 2025, 26 countries.
  - **First case page**: cases/_index.md was empty until this ingest; de-fr-online-fraud-group-2026 is the first case entry.

## [2026-04-10] enrich | Operation LadyBird (Emotet) + Operation Bayonet (AlphaBay) stub pages fully written
- Pages enriched: emotet-takedown.md (stub -> full operation page, ~272 lines)
- Pages enriched: alphabay-takedown.md (stub -> full operation page, ~329 lines)
- Sources verified: Europol (2021-01-27), DOJ (2021-01-27), Dutch National Police (2021-01-27), Eurojust (2021-01-27), Europol (2017-07-20), DOJ (2017-07-20), DEA (2017-07-20), FBI
- Cross-references updated: europol-ec3.md, netherlands-politie.md, fbi-cyber-division.md, eurojust.md (added operations_participated); netherlands.md, germany.md, united-states.md, united-kingdom.md, france.md, canada.md, ukraine.md, thailand.md (added operations_participated); japan.md (corrected false Emotet participation claim); operations/_index.md (2 entries added)
- Key findings:
  - Emotet (Operation LadyBird, 2021-01-27): 8 countries, ~700 C2 servers, 2000+ domains seized; Dutch police deployed uninstall module via Emotet's own update mechanism (activated 2021-04-25); 2 arrests in Ukraine; botnet resurfaced Nov 2021 via TrickBot -- partial outcome
  - AlphaBay (Operation Bayonet, 2017-07-20): Unprecedented double-sting; Dutch police covertly operated Hansa for ~1 month; AlphaBay shut down July 4; 400K users and 40K vendors disrupted; Cazes arrested in Thailand July 5, died in custody July 12; $30M+ assets seized/frozen

## [2026-04-10] enrich | Operation Dark HunTOR + Silk Road Takedown stub pages fully written
- Pages enriched: operation-dark-huntor.md (stub → full operation page, ~250 lines)
- Pages enriched: silk-road-takedown.md (stub → full operation page, ~300 lines)
- Sources verified: Europol (2021-10-26), DOJ/DEA (2021-10-26), NCA (2021-10-27), FBI NY (2015-02-04), DOJ SDNY (multiple), ICE (2015-05-29), Wikipedia
- Cross-references updated: europol-ec3.md (added operation-dark-huntor), darkmarket-takedown.md (added related_operations link), operations/_index.md (3 entries added)
- Key findings:
  - Dark HunTOR: 150 arrests across 9 countries; cascade from DarkMarket seizure via J-CAT/EMPACT
  - Silk Road: FBI-led 2013 takedown; Iceland server cooperation; ~173,991 BTC seized; Ulbricht pardoned 2025-01-21

## [2026-04-10] fix | 21건 URL-operation mismatch 정리 + 스케줄러 3회/일 개선
- Scheduler: 1x daily (07:00) → 3x daily (07:00, 12:00, 19:00) — register_scheduler.py 리팩토링
- 20건 source pages_updated 재할당 완료 (모든 [!warning] mismatch → [!info] resolved)
- 7 신규 작전 페이지 생성: bali-villa-cybercrime-raid-2024, operation-heart-blocker, operation-kraken-ghost-platform, lumma-stealer-takedown, nemesis-market-takedown, operation-chakra-iii, myanmar-kokang-scam-compound-crackdown
- botnet-takedown-europol-2023 → ramnit-botnet-takedown 리네임 (실제 2015 Ramnit 작전)
- operation-avalanche participating_countries 13 → 30 (Europol 공식 출처 확인)
- 2건 추가 mismatch 발견: the-cyber-express-marketplace-a-dekhtyarchuk-indictment → operation-endgame, hackread-global-airport-action-day → carding-action-2020
- BBC 미검증 URL 2건 인터뷰 큐 등록 (Q0003)
- lint: CRITICAL 0, HIGH 0 / check_links: broken 0 / ZZPROT: 0

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

## [2026-04-08] ingest | Operation Stream / Kidflix CSAM Takedown (Pipeline Test — CSAM batch)
- Source: raw/press-releases/2025-04-04_europol_operation-stream-kidflix-takedown.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator (FULL UPDATED PIPELINE)
- Pages created: 2025-04-04-europol-operation-stream-kidflix.md (source), operation-stream-kidflix.md (operation)
- Pages updated: europol-ec3.md (pending), csam-ic.md
- Key metrics: 79 arrests, 35+ countries, 1.8M platform users, 39 children protected
- Case ID: CYB-2025-001 | Period: 3 | CI: 2.55 | Verdict: INCLUDE

## [2026-04-08] ingest | Operation Cyber Guardian — Asia CSAM (Pipeline Test — CSAM batch)
- Source: raw/press-releases/2025-04-07_korea-npa_operation-cyber-guardian-asia-csam.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator (FULL UPDATED PIPELINE)
- Pages created: 2025-04-07-korea-npa-operation-cyber-guardian.md (source), operation-cyber-guardian.md (operation)
- Pages updated: south-korea.md (pending), csam-ic.md
- Key metrics: 544 arrests, 6 Asian countries, Korea: 435 arrests (49% teenagers)
- Case ID: CYB-2025-002 | Period: 3 | CI: 2.95 | Verdict: INCLUDE
- Multi-language source (Korean): translated: true

## [2026-04-08] ingest | Operation Orion International — South America CSAM (Pipeline Test — CSAM batch)
- Source: raw/press-releases/2024-10-15_interpol_operation-orion-international-south-america-csam.md
- Pipeline: collector -> classifier -> evaluator -> verifier -> integrator (FULL UPDATED PIPELINE)
- Pages created: 2024-10-15-interpol-operation-orion-international.md (source), operation-orion-international.md (operation)
- Pages updated: interpol-igci.md (pending), csam-ic.md
- Key metrics: 144 arrests, 12 countries, 20 children rescued, 7 Red Notice arrests
- Case ID: CYB-2024-001 | Period: 3 | CI: 2.28 | Verdict: INCLUDE

## [2026-04-08] ingest | Batch integration — CSAM crime type, indexes (Pipeline Test)
- Pages created: csam-ic.md (crime type — full page, NEW crime type)
- Pages updated: operations/_index.md, sources/_index.md, crime-types/_index.md, index.md, log.md
- Workspace files created: exclusion_log.md, capture_recapture.md
- Total this batch: 7 pages created, 5 pages updated, 3 sources ingested
- Wiki page count: 59 -> 66
- Pipeline test: ALL new methodology features exercised (case_id, period, actors, edges, enforcement_type, outcome, CI formula, decision tree, missing_fields, capture-recapture)

## [2026-04-08] ingest | Excel Batch Import — 130 rows audited, 4 new operations integrated

### Audit Summary (Full Decision Tree on 130 rows)
- **130 rows** from Excel spreadsheet processed through IC evaluator decision tree
- **18 rows** had complete structured data (rows 1-18 + partial 19-21)
- **44 rows** had URL only, no structured data (rows 22-62)
- **68 rows** completely empty (rows 63-130)

### Audit Results
| Verdict | Count |
|---------|-------|
| INCLUDE_NEW | 5 operations (4 integrated, 1 flagged for review) |
| INCLUDE_UPDATE | 3 (operation-endgame-phase2, operation-haechi-v) |
| DUPLICATE | 19 rows (mapping to existing wiki operations) |
| EXCLUDE | 8 (non-enforcement/policy/single-country/invalid) |
| UNVERIFIABLE (URL-only) | 27 (collection leads documented) |
| UNVERIFIABLE (empty) | 68 (blank rows discarded) |

### Pages Created (4 new operations)
- operation-red-card.md — CYB-2024-011 | CI: 2.95 | 306 arrests, 7 African countries
- operation-contender-2.md — CYB-2024-010 | CI: 2.28 | 8 arrests, West Africa BEC
- operation-talent.md — CYB-2025-011 | CI: 2.28 | Cracked/Nulled forums, 8 countries
- operation-secure-interpol.md — CYB-2025-012 | CI: 2.28 | 32 arrests, 26 Asia-Pacific countries

### Pages Updated
- operation-endgame-phase2.md — Added DanaBot detail (16 indicted, 300K computers, $50M) + 5 detentions follow-up
- operation-haechi-v.md — Added dig.watch supplementary source
- operations/_index.md — 4 new entries added

### Workspace Files Created
- _workspace/excel_audit.md — Full 130-row audit table with decision tree results
- _workspace/excel_unverifiable.md — 95 rows (27 URL-only + 68 empty) as collection leads

### Flagged for Review (CI < 2.0)
- Operation Chakra-V (row 3) — CI: 1.48 (single Tier 4 source, needs additional sources)
- Africa Cyber Surge Operation (row 9) — CI: 1.88 (single Tier 3 source, borderline)

### Key Decisions
1. 68 empty rows (63-130) discarded as blank spreadsheet placeholders
2. 27 URL-only rows preserved as collection leads with priority ranking
3. Operation names "Operation SECURE" (CoE, row 6) vs "Operation Secure" (INTERPOL, row 18) disambiguated — only INTERPOL enforcement version integrated
4. Multiple Operation Endgame entries (rows 2,5,11,14,21) consolidated into single wiki page update
5. Operation Red Card merged from 2 Excel rows (8+13) with INTERPOL source as primary

## [2026-04-08] update | Wiki-wide consistency cleanup
- Fixed index.md total page count (132->129) and source count (28->23)
- Replaced verbose operation/source listings in index.md with compact references to _index pages
- Rebuilt statistics dashboard (ic-statistics-dashboard.md) for all 82 operations:
  - Section 1: Added aggregate stats (82 ops, period breakdown, coordinating body distribution, top 10 by CI)
  - Section 2: Clarified scope as "20 most-sourced operations" with note about remaining 62
  - Section 3: Added CSAM as 6th crime type
  - Section 4: Updated source diversity (23 sources: Europol 6, INTERPOL 10, DOJ 3, Korea NPA 1, News 3)
  - Section 5: Added Operation Cyber Guardian and HAECHI-II to Korea section
  - Section 6: Updated all row counts (operations 20->82, crime types 5->6, sources 20->23, total 129)
- Updated overview.md to reflect full 82-operation dataset:
  - Executive summary now covers 5 coordination models with accurate counts
  - Key operations table replaced with top 10 by significance (arrest volume)
  - Cooperation statistics table updated with all derived metrics
- Verified all 6 category _index.md files: all correct (organizations 7, countries 1, crime-types 6, mechanisms 2, concepts 2, sources 23)

## [2026-04-08] create | Legal frameworks, mechanisms, and procedures batch (7 pages)
- Pages created:
  - wiki/legal-frameworks/un-cybercrime-convention-2024.md — UN Convention against Cybercrime (GA adopted 2024-12-24, not yet in force)
  - wiki/legal-frameworks/second-additional-protocol.md — CETS No. 224, Budapest modernization protocol (adopted 2022-05-12, not yet in force)
  - wiki/legal-frameworks/cloud-act.md — US CLOUD Act framework for cross-border data access (in force since 2018-03-23)
  - wiki/mechanisms/europol-jit.md — Europol Joint Investigation Team mechanism (formal, weeks-months setup)
  - wiki/mechanisms/interpol-i-grip.md — INTERPOL I-GRIP rapid payment interception (semi-formal, hours-days)
  - wiki/procedures/emergency-data-preservation.md — Budapest Convention Art. 29 preservation procedure (24-72 hours)
  - wiki/procedures/extradition-request.md — Extradition request procedure (6-24 months)
- Pages updated: legal-frameworks/_index.md (+3 rows), mechanisms/_index.md (+2 rows), procedures/_index.md (+2 rows), index.md (counts updated: legal frameworks 1->4, mechanisms 2->4, procedures 0->2, total 142->149)
- Key findings:
  - Three-layer legal framework architecture now documented: Budapest (in-force), Second Additional Protocol (not yet in force), UN Convention (not yet in force), CLOUD Act (in-force bilateral)
  - Korea has no CLOUD Act executive agreement; evaluating Second Additional Protocol signature
  - Phobos/8Base Korea-to-US extradition (2025, ~6 months) is the primary Korean cybercrime extradition precedent

## [2026-04-08] create | Challenges and concepts batch (5 pages)
- Pages created:
  - wiki/challenges/data-sovereignty.md — Data sovereignty and localization requirements (legal, critical)
  - wiki/challenges/jurisdictional-conflicts.md — Jurisdictional conflicts in cybercrime (legal, critical)
  - wiki/concepts/ne-bis-in-idem.md — Ne bis in idem / double jeopardy (human-rights-safeguard, criminal-law)
  - wiki/concepts/specialty-principle.md — Specialty principle / rule of specialty (legal-principle, international-law)
  - wiki/concepts/nationality-principle.md — Nationality principle / active personality (jurisdictional-doctrine, international-law)
- Pages updated: challenges/_index.md (+2 rows), concepts/_index.md (+3 rows), index.md (Challenges 0->2, Concepts 2->5, total 149->154)
- Key findings:
  - Data sovereignty challenge: Korea has no CLOUD Act executive agreement; PIPA amendments create growing friction with cross-border LEA data access
  - Jurisdictional conflicts: Budapest Convention Art. 22(5) consultation is non-binding; no global binding mechanism exists
  - Ne bis in idem: Korean 형법 Art. 7 allows mitigation but not bar for foreign judgments — weaker than EU transnational protection
  - Specialty principle: Phobos admin Korea-to-US extradition is the primary Korean cybercrime example; US-Korea Treaty Art. 15 applies
  - Nationality principle: Korean 형법 Art. 3 is among the broadest globally (all offenses, no dual criminality requirement); directly relevant to Cambodia scam centre repatriations

## [2026-04-10] create+factcheck | C-PROC, Direct Provider Request, UNODC + treaty updates
- Pages created:
  - wiki/organizations/c-proc.md (Cybercrime Programme Office of the Council of Europe, Bucharest, est. 2014-04-07)
  - wiki/mechanisms/direct-provider-request.md (voluntary + CLOUD Act + CETS 224 Art. 7/8 direct cooperation)
  - wiki/organizations/unodc.md (UN Office on Drugs and Crime, Vienna, est. 1997)
- Pages updated:
  - wiki/legal-frameworks/budapest-convention.md — states_parties 76->81; signatories 3->2 (Ireland, South Africa); added References table; updated 2026-04-10
  - wiki/legal-frameworks/un-cybercrime-convention-2024.md — signatories 0->74; states_parties 0->2 (Qatar Feb 2026, Vietnam); Hanoi 2025-10-25/26 signing ceremony documented; References table added
  - wiki/overview.md — Recent Treaty Developments expanded with Hanoi signing, Qatar ratification, Hungary CETS 224 ratification
- Key findings:
  - Budapest Convention: 81 parties as of Aug 2025 (per Wikipedia citing CoE), not 76 as previously recorded
  - CETS 224 Second Additional Protocol: 3 ratifications only (Japan, Serbia, Hungary 2026-02-05); still not in force
  - UN Cybercrime Convention: opened for signature in Hanoi 2025-10-25/26 (72 states + EU); 74 signatories by March 2026; Qatar first to ratify in Feb 2026 with reservations; Vietnam second
  - C-PROC operational since 2014-04-07 in Bucharest under MoU with Romania; 2000+ activities for 130+ countries over 10 years

## [2026-04-10] create | 3 new operation pages from URL-mismatch audit
- Pages created:
  - wiki/operations/bali-villa-cybercrime-raid-2024.md — Indonesia deported 103 foreigners from Bali villa raid (June 2024); no criminal prosecution due to jurisdictional gap
  - wiki/operations/operation-heart-blocker.md — US-Dutch seizure of 39 HeartSender domains (Jan 2025) + 21 Pakistan arrests (May 2025)
  - wiki/operations/operation-kraken-ghost-platform.md — AFP/Europol Ghost encrypted platform takedown, 51 arrests across 9 countries (Sep 2024)
- Pages updated:
  - wiki/operations/_index.md — 3 new entries added
- Key findings:
  - Bali raid: illustrates jurisdictional gap — host country could not prosecute because victims were abroad; deportation only
  - Heart Blocker: rare Pakistan-based cybercrime disruption; loss estimates range $3M (DOJ) to $50M+ (Pakistan NCCIA)
  - Operation Kraken: AFP infiltrated Ghost via software update modification; 2.5-year investigation; continues EncroChat/AN0M/Sky ECC lineage of criminal encrypted platform takedowns

## [2026-04-10] create | 2 new operation pages from URL-mismatch audit (batch 2)
- Pages created:
  - wiki/operations/operation-chakra-iii.md — CBI India Operation Chakra-III (Jul-Sep 2024): 43 arrests across 6+ Indian cities dismantling tech-support scam call centers targeting US victims; CBI + FBI + INTERPOL + HSI collaboration; 951 devices + 57 gold bars seized
  - wiki/operations/myanmar-kokang-scam-compound-crackdown.md — China-Myanmar cyber scam compound crackdown (Sep 2023 - Jan 2024): 41,000+ suspects repatriated to China; MNDAA Operation 1027 military offensive physically overran Kokang scam compounds; Ming family leadership arrested; largest cybercrime enforcement by volume in history
- Pages updated:
  - wiki/operations/_index.md — 2 new entries added
- Key findings:
  - Chakra-III: Part of multi-phase CBI series (I-V); arrest count discrepancy (43 total vs 26 in second wave) likely sequential; Microsoft role unclear for Phase III specifically
  - Myanmar-Kokang: Unprecedented case of military conflict intersecting with cybercrime enforcement; non-state armed group (MNDAA) served as de facto enforcement partner; scam operations displaced to other regions rather than eliminated
  - Both operations represent non-Western IC models: India bilateral with US/INTERPOL; China bilateral pressure + tacit military support

## [2026-04-13] fix | operation-orion-international 참여국 역링크 복구 (11 stub + 1 backlink)
- Pages created (11 South American country stubs):
  - wiki/countries/argentina.md, bolivia.md, brazil.md, chile.md, ecuador.md, guyana.md, paraguay.md, peru.md, suriname.md, uruguay.md, venezuela.md
- Pages updated:
  - wiki/countries/colombia.md — operations_participated에 [[operation-orion-international]] 역참조 추가
- Key findings:
  - Operation Orion International은 2024년 5-9월 12개 남미국 합동 CSAM 단속(144명 체포, 아동 20명 구출)으로 participating_countries frontmatter에 12개국 wikilink가 전부 박혀 있었으나, 이 중 11개 국가 페이지 자체가 존재하지 않아 broken wikilink 상태였음 (Colombia만 페이지 존재하되 역참조 누락)
  - CLAUDE.md Rule 7 (non-existent page wikilink 금지 + stub 필수) + Rule 3 (bidirectional invariant) + LESSONS.md L17 (participating_countries 공식 출처 교차 검증) 위반 사례
  - 검증: check_links.py broken 0, lint.py CRITICAL/HIGH/MEDIUM 0
