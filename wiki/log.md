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
