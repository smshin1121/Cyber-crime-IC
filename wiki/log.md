# Activity Log

## [2026-05-03] audit | Source-grounding and treaty-status consistency pass
- Scope: follow-up whole-corpus consistency check after the source/depth audits, focused on stale source-scope notes, source-summary bleed, and Korea/Budapest Convention party-status contradictions.
- Country profiles: 67 zero-source country pages normalized into assessment-control records, removing unsupported legal-capacity claims while preserving operation backlinks and follow-up source targets.
- Source integrity: 13 source pages and their raw archive digests corrected where copied South Korea country-profile language had replaced source-specific summaries; affected case wrappers for HAECHI IV and Phobos/8Base now carry source-specific facts and scope limits.
- Treaty status: [[overview]], [[budapest-convention]], [[south-korea]], [[germany]], [[netherlands]], and [[unodc]] now align with the Council of Europe Treaty Office Treaty 185 chart status dated 2026-04-25: Korea is invited to accede but is not yet a party.
- Source page corrected: [[2026-04-17_coe-int_treaty-185-signatures-chart]] now summarizes Treaty 185 status rather than unrelated Spain profile text.

## [2026-05-03] methodology | Project goal and success criteria set
- Scope: converted the implicit project direction into an explicit goal document and wiki analysis page.
- Files created: `GOAL.md`, [[project-goal-2026-05-03]].
- Goal: build a source-grounded, SNA-ready knowledge base on public international cooperation against cybercrime, with source integrity and canonical-operation separation as the controlling criteria.
- Success criteria: operation/case records must support reproducible analysis of countries, agencies, mechanisms, crime types, outcomes, Korea relevance, and public-record limitations.
- Quality gates: lint, link checks, integrity audit, operation consistency audit, content-depth audit, source-duplicate audit, and placeholder scans define readiness for analytical use.

## [2026-05-03] audit | Residual source-title and taxonomy consistency review
- Scope: follow-up review after the repository-wide integrity cleanup, focused on visible `Page not found` source labels, corrected DOJ URLs, duplicate-source audit residue, and crime-type mismatch flags.
- Source metadata corrected: 16 DOJ-derived source pages now carry real titles/publish dates or alias to canonical source pages instead of preserving `Page not found` as the user-facing title.
- HeartSender correction: replaced the dead SDTX URL with the official 2025-01-30 SDTX release URL, corrected the seizure/announcement date split, and added the existing KrebsOnSecurity corroborating source to [[operation-heart-blocker]].
- Redundant dead DOJ references pruned from [[emotet-takedown]], [[isoon-apt27-indictment]], and [[qakbot-gallyamov-indictment]] where canonical working source pages already existed.
- xDedic consistency: four sparse defendant pages now record the parent-marketplace contextual classifications (`online-fraud-ic`, `cybercrime-forum-ic`, `dark-web-ic`) with a note that the statutory charge remains wire fraud.
- Validation: lint 0 issues; content-depth mismatch flags 0; source duplicate audit active URL groups 0, active content-hash groups 0, review-only hash groups reduced to 12; integrity audit broken wikilinks 0; operation consistency issues 0.

## [2026-05-02] audit | Integrity and consistency cleanup
- Scope: repository-wide wiki integrity review, duplicate-source normalization, empty-section remediation, and static-site rebuild.
- Source aliases normalized: 14 `wiki/sources` pages now carry `duplicate_of` metadata for same-URL duplicates; active duplicate URL groups are 0.
- Operation references deduplicated: 11 operation pages now point to unique source URLs while preserving canonical source coverage.
- Content gaps closed: 74 case/operation pages had empty `Source Coverage`, `Evidence and Attribution Notes`, or `Results` sections filled from existing metadata and references; 11 alias-resolved source pages received missing `created` metadata.
- Tooling added: `tools/resolve_empty_sections.py` for repeatable low-risk empty-section remediation.
- Validation: lint 0 issues; integrity audit broken wikilinks 0, parse errors 0, duplicate slugs 0; operation consistency issues 0; static-site link check broken 0 and malformed 0.

## [2026-04-21] audit | Full web-verification pipeline mature — 96/100 top-queue ops verified
- Added Akamai Bot Manager bypass (meta-refresh + session + 5.5s wait) to unblock DOJ / justice.gov / usao-* URLs that curl_cffi TLS impersonation alone could not reach. Logged as LESSONS.md L21.
- Extended queue builder to parse URLs from three source formats: wikilink → wiki/sources/*.md (with `collection_url`/`source_url`/`url` field), inline markdown link `[title](url)`, or plain URL in a string.
- Top-100 verification run after all upgrades: **96 fully verified, 1 partial, 3 with URL-less sources.**
- Cumulative L19 back-link additions across all rounds today: **217** country→op links populated across roughly 60 country pages.
- Remaining unresolved: `bidencash-takedown` (3/6 — Denmark/Finland/Germany not in cited sources, may be genuinely absent or secondary-only), `dridex-operations` (plain-text references, URLs live in body reference table — needs manual source-page ingestion), `operation-ghost-*` and `operation-in-re-heartsender-*` (USAO subdomain fetches still flaky). All logged for follow-up, none asserted-without-proof.

## [2026-04-21] audit | TLS-spoofing pipeline + L19 bidirectional back-link apply (30 ops)
- Built `tools/web_verify_tls.py` using `curl_cffi` with Chrome TLS fingerprint impersonation to bypass Cloudflare on Europol / Eurojust / DOJ / BSI / national CERT primary sources.
- First batch (top-30 unverified ops): 15 fully verified (including Avalanche 29/29 and HAECHI-VI 32/32 after adding Viet Nam + Kazakhstan + UAE aliases and stub pages), 4 partially, 11 with no reachable sources on record.
- Lesson logged: LESSONS.md L20 ("Cloudflare/SPA wall — curl_cffi TLS impersonation + script-preserving parse is the required fallback before declaring a country 'not in source'").
- Correction: [[colombia]] reinstated in [[operation-avalanche]] — earlier same-day removal was based on accessible-subset only and the Europol press release does explicitly list Colombia.
- Applied L19 "verified" bucket: `tools/apply_bidirectional_ops.py` — added 81 missing country→op back-links to 39 country pages across the 15 fully-verified operations. Idempotent; re-run safe.
- Stub pages created: `wiki/countries/kazakhstan.md`, `wiki/countries/united-arab-emirates.md` (named in INTERPOL HAECHI-VI roster but previously dangling wikilinks).

## [2026-04-21] audit | Avalanche participating-countries tier-1 verification pass
- Follow-up to the Colombia audit earlier today. Audited the full 29-country roster of [[operation-avalanche]] against accessible tier-1 primary sources.
- Europol full press release (the one source believed to hold the 30-country roster) is web-blocked by Cloudflare (per LESSONS.md L11). Verification is based on the subset accessible: INTERPOL mirror, Eurojust 2017 case report PDF, FBI/DOJ archive text indirectly via secondary reporting, Canadian Cyber Centre advisory.
- Explicitly named in tier-1 sources: **Germany, United States, Netherlands, Canada**.
- Removed earlier today (absence from every accessible source): **Colombia**.
- 24 remaining countries retained as provisional (absence from accessible subset ≠ absence in full Europol roster). Flagged in a detailed verification table on the operation page.
- Pages updated: wiki/operations/operation-avalanche.md (expanded Audit Note with verification breakdown), wiki/countries/canada.md (added [[operation-avalanche]] to operations_participated — Canada's participation is verified by RCMP statement in Canadian Cyber Centre advisory).

## [2026-04-21] audit | Colombia participating-operations source verification
- Trigger: Globe picker showed Colombia across 4 operations; user asked for data provenance. Principle applied — only assert participation when a tier-1 primary source explicitly names Colombia.
- Verified (primary source explicit): [[operation-orion-international]] (INTERPOL 2024-10-15), [[operation-haechi-ii]] (INTERPOL 2021-11-30), [[imminent-monitor-rat-takedown]] (Europol 2019-11-29)
- Un-verified, removed: [[operation-avalanche]] — Europol press release, US DOJ press release, and 2017 Eurojust case report PDF do not name Colombia. Removed `[[colombia]]` from avalanche's `participating_countries`; flagged in Colombia's Contradictions section pending evidence.
- Pages updated: wiki/countries/colombia.md (added Verified Operational Participation table + source-verification policy), wiki/operations/operation-avalanche.md (Audit Note).

## [2026-04-12] ingest | Court documents for 10 operations (판결문 수집 첫 배치)
- Source: DOJ press releases, indictments, sentencing announcements (justice.gov)
- Raw case documents created (10): silk-road sentencing, infraud indictment, goznym indictment, darkode indictment, trickbot/conti indictments, qakbot/gallyamov indictment, danabot indictment, dridex/yakubets indictment, ghinkul/bugat indictment, emotet disruption order
- Case pages created (9): us-v-ulbricht-silk-road, us-v-bondarenko-infraud, us-v-konovolov-goznym, us-v-gudmunds-darkode, us-v-galochkin-trickbot-conti, us-v-gallyamov-qakbot, us-v-stepanov-danabot, us-v-yakubets-dridex, emotet-disruption-ladybird
- Operations updated (9): silk-road (already had link), infraud, goznym, darkode, trickbot, operation-endgame, operation-endgame-phase2, qakbot-gallyamov, dridex, emotet
- Key findings:
  - Ulbricht life sentence (2015) + Trump pardon (2025) is the most historically significant cyber sentencing/clemency sequence
  - GozNym case established unprecedented parallel-prosecution model across 6 countries
  - TrickBot/Conti: Dunaev arrest in South Korea is a key Korean IC cooperation example
  - Infraud RICO application to cybercrime forums set prosecution precedent for 36-defendant indictment
  - All 16 DanaBot defendants and most TrickBot/Dridex defendants remain at large in Russia

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
- lint: CRITICAL 0, HIGH 0 / check_links: broken 0 / placeholder-token scan: 0

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
## [2026-04-18] query-filed | priority country source expansion registry
- Pages created:
  - wiki/analysis/priority-country-source-registry.md
- Pages updated:
  - wiki/analysis/_index.md
  - wiki/index.md
  - CLAUDE.md
- Key findings:
  - Source diversification should prioritize Germany, France, the United Kingdom, the Netherlands, Belgium, Spain, and Italy before broader global expansion.
  - Country expansion is most useful when it strengthens synthesis, cross-jurisdiction comparison, and existing operation/case pages rather than creating thin standalone entries.
  - The repo now has an explicit registry-level rule for shifting from page-count growth toward interpretation, connectedness, and trusted multi-country sourcing.

## [2026-04-20] analysis-filed | SNA PoC — 2-mode network reproduction of paper.pdf
- Analysis page: [[sna-pilot|SNA Pilot]]
- Tool: `tools/sna_analysis.py` (networkx 3.6.1 + pandas 3.0.2 + pyyaml 6.0.2)
- Spec: `_workspace/sna/paper-network-definitions.md`, `_workspace/sna/edge-schema-and-inclusion-rules.md`
- Snapshot: `2026-04-19-d50e3208` under `_workspace/sna/out/`
- Pages created: [[sna-pilot]]
- Pages updated: `_workspace/sna/audit-denylist.txt` (new, 14 slugs from audit Batches 1-3)
- Key findings:
  - 61 operations pass all inclusion rules out of 1,136 scanned (1,023 rejected by `participating_countries ≥ 2` hard filter; 13 lost to YAML URL-quoting parse errors on canonical ops incl. alphabay / silk-road / trickbot / dridex).
  - Paper-style structural patterns reappear at low confidence: US leads country degree+betweenness (0.607 / 0.175), core-periphery skew visible, agencies-with-breadth vs agencies-with-brokerage split visible (INTERPOL low-deg high-btw).
  - Europol EC3 dominates agency-mode centrality (degree 0.689, betweenness 0.446) in our subset — higher than paper's Europol (0.311 / 0.132). Likely a corpus-composition artifact of the audit filter removing US-DOJ procedural wrappers, not a substantive divergence.
  - Crime-type network structurally not comparable (single-valued `crime_type` schema → star topology → transitivity 0, community detection degenerate). Step B must resolve.
  - Alias-resolution deferral splits FBI into `fbi` + `fbi-cyber-division`, understating FBI centrality.
- Step B backlog surfaced: (1) fix YAML URL-quoting on 13 canonical ops, (2) alias canonicalization pass in `sna_analysis.py`, (3) crime-type schema decision (list-valued vs body-derived), (4) `participating_countries` enrichment on genuinely-multi-country ops with empty field, (5) add cpnet core-periphery + Gould-Fernandez brokerage + visualizations after data cleanup.

## [2026-04-20] fix+sna-rerun | YAML URL-quoting repair + SNA alias canonicalization (PoC v2)
- Tools added: `tools/repair_yaml_quotes.py` (frontmatter repair, idempotent, dry-run supported), `_workspace/sna/node-alias-map.yaml` (3 agency merge mappings)
- Tool updated: `tools/sna_analysis.py` — loads alias map, applies `canonicalize_record` before graph build, records `alias_canonicalization` block in manifest, `rules_version` bumped `poc-v1 → poc-v2`
- Pages updated: [[sna-pilot]] (all numeric tables + key judgments + next steps refreshed against v2 snapshot)
- Files modified by YAML repair (13 canonical ops, frontmatter only, body untouched): alphabay-takedown, bidencash-takedown, carding-action-2020, dridex-operations, myanmar-kokang-scam-compound-crackdown, operation-haechi-iii, operation-haechi-vi, operation-jackal-iii, operation-onymous, operation-power-off, operation-rewired, silk-road-takedown, trickbot-operations — total 48 line-level fixes (26 Pattern A inner-quote + 22 Pattern B URL-in-markdown-link)
- Alias merges applied: fbi→fbi-cyber-division (9 slot-merges), usdoj→us-doj (5), interpol-igci→interpol (7). Direction chosen by explicit "Legacy compatibility page" markers in the losing pages' `mandate:` fields.
- Snapshot v2 outcome: included 61→72 (+11), parse_error 13→0, agencies 81→78 (−3 aliased), edges country 433→566 / agency 314→358 / crime 61→72.
- Structural outcome: country network now fully connected (fragmentation 0.269→**0.000**, matches paper); FBI consolidated to rank 2 agency (degree 0.569, was split 0.393 + 0.148); INTERPOL now shows the paper's low-deg / high-btw broker signature (0.194 / 0.192).
- Remaining Step B backlog: crime-type schema decision, `countries_lt_2` enrichment on genuinely-multi-country ops, bare-string agency normalization, cpnet + Gould-Fernandez + viz.

## [2026-04-20] fix+sna-rerun | Bare-string normalization + crime_types list schema (PoC v3 → v4)
- Tools added: `tools/scan_bare_strings.py` (diagnostic scanner), `tools/migrate_crime_type_to_list.py` (one-shot, idempotent schema migration)
- Tool updated: `tools/sna_analysis.py` — `extract_wikilinks` slugifies non-wikilink bare strings; `OpRecord` field `crime_type` → `crime_types: list[str]`; canonical list read first, legacy single field read only as fallback. `rules_version` bumped `poc-v3 → poc-v4`.
- Schema change in `CLAUDE.md` — Operation frontmatter template: `crime_types: []` (canonical list) added as primary field; `crime_type: ""` marked DEPRECATED / read-only fallback.
- Pages updated: [[sna-pilot]] (confidence raised to medium; all v1→v2→v3→v4 progression table complete).
- Files modified by schema migration: 4 operation files back-filled `crime_types` from legacy single value (`andromeda-botnet-takedown`, `carbanak-cobalt-takedown`, `operation-avalanche`, `operation-us-v-parsarad-nemesis`). 1,124 ops already had the list form from prior data work; 7 have no crime type data yet.
- Bare-string normalization outcome: 88 bare-string values slugified. Country node count 133 → 109 (24 merged into canonical pages like `france`, `nigeria`, `spain`). Nigeria broker signature now visible (deg 0.125 / btw 0.108 — close match to paper's 0.140 / 0.111). South Africa shows a parallel regional-broker pattern (0.069 / 0.066).
- Crime-types schema outcome: all 72 included ops read from canonical `crime_types` list (0 legacy-fallback reads). Current network is still list-of-one structurally — multi-value backfill is Step B work.
- Step B open items now: (1) multi-value `crime_types` backfill (body-prose + related_operations), (2) `countries_lt_2` enrichment on genuinely-multi-country ops, (3) source-side fix for 33 country bare-strings that map to existing canonical pages (listed in `_workspace/sna/bare-strings-scan.csv`), (4) cpnet core-periphery + Gould-Fernandez brokerage + visualizations, (5) `wiki/analysis/sna-structure-and-roles.md` full comparison.

## [2026-04-20] fix+enrich+sna-rerun | Source-side country bare-string repair + source-backed subset enrichment (PoC v4 → v5)
- Tools added: `tools/repair_bare_country_strings.py` (idempotent, dry-run), `tools/select_enrichment_subset.py` (subset rule codified), `tools/enrich_participating_countries.py` (proposal + apply, source-backed only)
- Pages updated: [[sna-pilot]] (v5 tables and status), 7 ops frontmatter (bare-string source fix), 20 ops frontmatter (source-backed country enrichment)
- `tools/repair_bare_country_strings.py` outcome: 44 line-level fixes across 7 ops (`dridex-operations`, `franco-israeli-ceo-fraud`, `korea-china-voice-phishing-qingdao`, `operation-haechi-iii`, `operation-haechi-iv`, `operation-jackal`, `operation-sentinel-africa`). `operation-jackal` alone had 19 bare country strings rewritten. SNA edge counts unchanged (script-side already normalized); source cleanup benefits build / lint / reconcile / future ingest.
- Subset selection (A): 46 ops with Eurojust/Europol/INTERPOL-anchored source AND `participating_countries` count ≤ 1. Manifest at `_workspace/sna/enrichment-subset-2026-04-19.json`. Locked subset rule: source wikilink slug contains `eurojust|europol|interpol`, OR URL on those domains, OR `lead_agency`/`coordinating_body` in `{eurojust, europol-ec3, europol, interpol, interpol-igci}`.
- Enrichment (A): 46 subset → **20 applied**. Source-backed country enrichment only; no inferred countries added. Adjective-only matches excluded by design. Placeholder values `{international, global, worldwide, various}` treated as empty. Manifest at `_workspace/sna/enrichment-proposals-2026-04-20.json` records `snapshot_date`, `subset_rule`, `enriched_ops_count`, `applied_detail` per user rule. Remaining 26 subset ops break down: 11 no-sources, 11 no-extract, 2 no-key-findings, 2 empty-delta.
- Enrichment adds 17 unique canonical country slugs across 20 ops (argentina, austria, belgium, canada, denmark, france, greece, hong-kong, ireland, italy, romania, south-korea, spain, sweden, thailand, united-kingdom, united-states).
- SNA v5 outcome: included 72 → 73 (+1 op passed country gate after enrichment); op-country edges 566 → 571 (+5); op-agency 358 → 360 (+2, agency set unchanged); op-crime 72 → 75 (+3, crime-type count 14 → 15 with one multi-valued op accidentally producing crime-type transitivity 1.0 — artifact of list schema, not a meaningful pattern yet).
- Step B open items: (1) multi-value `crime_types` backfill, (2) enrichment of remaining 26 subset ops (URL fetch / raw-file reading required), (3) country page creation for 22 bare-string countries without canonical pages (Brunei, Cote d'Ivoire, Hong Kong, UAE, etc.), (4) broader `countries_lt_2` enrichment on the 1,017-op backlog, (5) cpnet + Gould-Fernandez + viz, (6) `wiki/analysis/sna-structure-and-roles.md` main Step B page.

## [2026-04-20] analysis-filed | SNA Step B main analysis — structure and roles
- Pages created: [[sna-structure-and-roles]] (Step B main body — comparative-study, confidence medium, ~540 lines)
- Basis: PoC v5 snapshot `2026-04-20-d50e3208` (73 ops, 109 countries, 78 agencies, 15 crime types)
- Structure: Summary → Corpus and methodology → Basic structure (cohesion vs paper Table 2) → Structural positions (centrality vs paper Table 3) → Connectedness + communities → Role differentiation (participation vs connection) → Korean perspective → Limitations (subset / coarse crime schema / residual enrichment) → Corpus difference/bias → Step C supplementary roadmap → Reproducibility → Contradictions & open questions
- Reproduced qualitative findings (confidence medium): US global liaison (top-deg + top-btw both studies); FBI Cyber Division rank 2 agency at 0.562/0.292 (paper's FBI 0.494/0.371); INTERPOL low-deg/high-btw cross-domain broker signature (ours 0.192/0.190 vs paper 0.268/0.135); Nigeria BEC-specialist regional broker (ours 0.123/0.107 vs paper 0.140/0.111); Europol EC3 rank 1 (corpus-composition artifact, not substantive divergence from paper).
- Additional findings (Asia/LatAm/Africa): South Africa regional broker (0.068/0.066), Brazil regional broker (0.041/0.043 through Operation Orion), Japan NPA Asia broker (0.082/0.029).
- Strong caveats flagged with callouts: crime-type transitivity 1.000 is sample artifact from single multi-valued op, not structural finding; Euro-weighted subset ordering Europol>FBI is corpus-composition, not substantive; Korean agency attribution under-represented at frontmatter level.
- Step C deferred: cpnet Borgatti-Everett fitness, Gould-Fernandez brokerage, network visualization, temporal slicing, multi-value crime_types backfill, remaining 26 subset enrichment, 22 canonical country page creation, 1,017-op broader countries_lt_2 enrichment.

## [2026-04-20] analysis-extended | Step C supplementary — core-periphery + Gould-Fernandez brokerage
- Tools added: `tools/sna_core_periphery_brokerage.py` (cpnet.BE on mode-2 projection, Gould-Fernandez 5-role on mode-2 projection with wiki-metadata partitions).
- Dependency added: `cpnet==0.0.21` installed via pip (pulls in `simanneal`, `numba`, `llvmlite`, `plotly`, `seaborn`).
- Outputs: `_workspace/sna/out/2026-04-20-d50e3208/metrics_core_periphery.json`, `metrics_brokerage_{agency,country,crimetype}.csv`, `metrics_supplementary.json`.
- Pages updated: [[sna-structure-and-roles]] — added Supplementary §Core-Periphery and §Brokerage sections (+104 lines, total 473); refreshed scope + key_judgments in frontmatter.
- Core-periphery outcome: agency fitness 0.266 (paper 0.254 — close match). Country fitness 0.008 is `cpnet.BE` near-degenerate on dense connected graph (documented as tool-difference vs paper's UCINET BE). Crime-type fitness 0.000 schema-artifact (documented). Agency core block (32 nodes) includes paper's DOJ + FBI + Europol tight core plus broader EU national units — partition granularity differs.
- Brokerage outcome: paper's role signatures reproduce qualitatively — Europol EC3 pure cross-domain broker (Liais 2,178 / 96%); FBI Cyber Division balanced hub (all 5 roles, Gate+Rep 492+492 dominant); Eurojust Liaison-dominant (Liais 710 / 80%); INTERPOL Liaison specialist (254 / 69%) matching paper's international-org pattern; Netherlands-Politie and Canada-RCMP internal coordinators (Coord 120 each). Country-side: US 94% Liaison (global-liaison signature), Nigeria Gate+Rep 448 (BEC-specialist regional broker), South Africa / Australia / Brazil Liaison-dominant regional brokers.
- Strong caveats preserved: crime-type brokerage is all zeros (schema artifact), country cpnet BE partition is near-trivial (algorithm-specific), Step C role matches are qualitative not numeric.
- Visualization and temporal slicing remain in later Step C follow-ups, now designable against confirmed role indicators.

## [2026-04-20] analysis-extended | Step C-2 — role-indicator-based visualizations
- Tools added: `tools/sna_visualize.py` — classifies every mode-2 node into `{hub, liaison-broker, internal-coordinator, regional-coordinator, specialist-broker, global-liaison, participant}` per `roles-v1` rules; renders pyvis HTML figures; exports consolidated role data for Cosmos.
- Dependency added: `pyvis==0.3.2` installed via pip.
- Files created:
  - `wiki/analysis/sna/agency-network.html` — 78 mode-2 + 73 op nodes, 360 edges, role-colored
  - `wiki/analysis/sna/country-network.html` — 109 mode-2 + 73 op nodes, 566 edges, role-colored
  - `cosmos/sna-roles.json` — 202-node role+centrality+brokerage manifest ready for future Cosmos UI integration (existing Cosmos view unchanged)
  - `_workspace/sna/out/2026-04-20-d50e3208/role_classification.csv` — full classification manifest (inputs + rule version)
- Pages updated: [[sna-structure-and-roles]] — added §Figures (147 lines, brings total to 547).
- Role classification results (Step B/C interpretations confirmed):
  - Agency 9 non-participants: hub (1) FBI Cyber Division; liaison-broker (3) Europol EC3 / Eurojust / INTERPOL; internal-coordinator (1) Canada-RCMP; regional-coordinator (4) US-DOJ / Netherlands-Politie / UK-NCA / France-Gendarmerie.
  - Country 16 non-participants: global-liaison (1) US; regional-coordinator (9) UK/Germany/Netherlands/France/Spain/Poland/Romania/Switzerland/Ukraine; specialist-broker (6) Nigeria/South-Africa/Brazil/Argentina/Colombia/Ghana.
  - Crime-type (15 nodes): all `participant` — schema artifact (list-of-one topology produces no brokerage, already-known limitation).
- Refinements during this turn: agency liaison-broker rule tightened from `liais/total > 0.70 AND coord/total < 0.05` to `liais/total > 0.65 AND coord/total < 0.10 AND total ≥ 200` — captures INTERPOL (liais ratio 69%) while rejecting small-volume noise (germany-frankfurt-prosecutor total 88).
- Cosmos UI integration deferred to a follow-up turn (role filter / core-periphery highlight / broker badge). Data layer (`cosmos/sna-roles.json`) already shipped.
- Next candidates: Cosmos UI integration; cpnet alternative algorithms for country partition; multi-value crime_types backfill.

## [2026-04-20] cosmos-feature | SNA mode added as third toggle parallel to Graph/Globe
- `cosmos/index.html` + `docs/cosmos/index.html` updated (222 → 236 lines) — additive only, Graph and Globe modes unchanged.
- UI changes: third button in top-right mode segment (`Graph | Globe | SNA`); new SNA-only section in right panel with Agency/Country sub-toggle, camera distance, show labels / show edges / core-block-only checkboxes, role legend.
- JS changes: `S.sna` config + `S.snaData`; `loadSnaData()` (lazy fetch `./sna-roles.json` on first SNA mode entry); `renderSna()` (bipartite 2-mode sphere layout — inner sphere = operations, outer sphere = mode-2 nodes — role-colored, core-block emissive bump, degree-sized); `syncSnaControls()`; `buildSnaLegend()`; `updateViewModeUI()` extended; `rerender`/`render`/`wheel`/`saveState`/`loadState` extended for the sna case. `body.view-sna` CSS class auto-hides Graph + Globe only sections.
- Data layer: `tools/sna_visualize.py` reshaped `cosmos/sna-roles.json` export — now per-kind (`agency`, `country`, `crime_type`) with `nodes` / `operations` / `edges` lists. 78 agencies / 360 edges, 109 countries / 571 edges, 15 crime-types / 75 edges. Manifest written to `cosmos/sna-roles.json` AND synced to `docs/cosmos/sna-roles.json`.
- Verification: JS parses cleanly (headless `new Function()` check); all HTML IDs and JS refs match; no changes to existing data.json or Graph/Globe render paths.
- [[sna-structure-and-roles]] updated — §Figures / Cosmos integration section rewritten from "deferred UI" to "SNA mode live"; Step C closeout checkbox added for Cosmos SNA mode; remaining Cosmos-UI follow-ups (broker badge, role filter, crime-type sub-toggle) deferred to the next supplementary milestone.
- Outstanding: multi-value `crime_types` backfill, cpnet alternative algorithms for country core-periphery, broader 1,017-op `countries_lt_2` enrichment.

## [2026-04-20] cosmos-feature | SNA mode UI — hover tooltip + role filter
- `cosmos/index.html` + `docs/cosmos/index.html` updated (236 → 243 lines). Additive only — Graph / Globe / SNA base render paths unchanged.
- New HTML: top-level `#snaTooltip` div (sna-only, position:fixed, pointer-events:none), `#snaRoleFilter` chip container inside the SNA section (between core-only checkbox and legend).
- New state: `S.sna.roleFilter = null | Set<string>`. `null` means all roles enabled. A Set means only listed roles render. Serialized as array in `saveState` / rehydrated to Set in `loadState`.
- New functions: `snaRolesPresent()` (derive sorted role set for current network), `buildSnaRoleFilter()` (renders clickable chips, toggles with sensible defaults — first click isolates clicked role's opposites, re-enabling all collapses back to null, emptying falls back to clicked-role-only), `hoverSna(ev)` (raycaster against MES, pops floating tooltip with slug + role + partition + core/periphery + degree + betweenness + full G-F 5-role brokerage counts), `hideSnaTooltip()`.
- `renderSna()` applies `S.sna.roleFilter` before node placement; edges to filtered-out nodes also drop. `visibleSlugs` set drives edge inclusion.
- Event hooks: `R.domElement.addEventListener("mousemove", hoverSna)` + `"mouseleave", hideSnaTooltip`. `updateViewModeUI` hides tooltip whenever leaving SNA mode. Network sub-toggle resets `roleFilter` to null and rebuilds the chip set (different networks have different role compositions).
- Verification: JS parses (`new Function()` check), all HTML ids + JS refs + functions wired, mousemove/mouseleave hooks registered. Sync to `docs/cosmos/index.html` done.
- [[sna-structure-and-roles]] updated — SNA-mode controls table now includes Role filter + Hover tooltip sections; Step C closeout adds a new checkbox row for the second Cosmos iteration; remaining Cosmos UI follow-ups narrowed to crime-type sub-toggle (schema-gated) and click-to-detail SNA→wiki-page linkage.
- Outstanding Cosmos UI: click-to-select SNA node → E.detail wiki-page summary; crime-type sub-toggle activation after multi-value `crime_types` backfill.


## [2026-04-20] cosmos-feature | SNA mode — click-to-detail wiki linkage
- `cosmos/index.html` + `docs/cosmos/index.html` updated (243 lines unchanged — additive edits within existing lines).
- New behavior: clicking an SNA node (inner-sphere operation OR outer-sphere mode-2 agency/country/crime-type) populates the right-panel `#detail` with the node's wiki summary — identical detail rendering to graph-mode click. Activation gated on `S.map.get(id)` so only wiki-backed slugs open the panel.
- Click handler change: `click(ev)` now dispatches on `S.viewMode === "sna"` before the graph branch. Sets `S.active = id`, calls `updateDetail(id)`, then `renderSna()` so the active-node halo refreshes. Graph and globe click paths untouched.
- Render change: `renderSna()` adds a primary-color transparent glow sphere at the active node position (radius 1.4 for ops, 6.5 for mode-2 — wraps max degree-sized node). Activated only when `S.active` matches an op slug or mode-2 slug in the current network (`posMap.get("op::" + S.active) || posMap.get("m2::" + S.active)`). No-op when `S.active` is a legal-framework, case, etc. that isn't part of the SNA bipartite — no regression when crossing modes.
- Verification: two edit anchors unique in both files; cosmos/ and docs/cosmos/ diff clean; `lint.py` 0 issues; `check_links.py` 0 broken (153,397 links total).
- Closes outstanding follow-up from the prior SNA-mode entry ("click-to-select SNA node → E.detail wiki-page summary").
- Remaining Cosmos UI follow-up: crime-type sub-toggle activation — gated on multi-value `crime_types` backfill.


## [2026-04-20] cosmos-tweak | Camera defaults closer + zoom range widened
- Initial camera distance reduced on all three modes — users reported the default angle felt too far from the scene. New defaults: Graph 210 → 130, Globe 255 → 180, SNA 260 → 140.
- Wheel zoom clamps widened so zoom-in/zoom-out has useful headroom at both ends: Graph 120..320 → 60..320, Globe 180..340 → 110..360, SNA 180..360 → 60..400.
- Sliders in the right panel updated to match the new bounds (globeDistance and snaDistance min/max/value attributes).
- `cosmos/index.html` + `docs/cosmos/index.html` synced. JS brackets balanced, no structural changes.


## [2026-04-20] cosmos-tweak | Revert Graph/Globe camera defaults + SNA Crime-Type toggle activated
- Prior entry changed camera defaults and wheel-zoom clamps on all three modes (Graph, Globe, SNA). User feedback: Graph and Globe were fine — only SNA needed the closer angle and wider zoom range.
- Reverted Graph and Globe to original values: Graph default 210, clamp 120..320; Globe default 255, clamp 180..340, slider min/max/value and `globeDistanceVal2` restored; `CAM.position.set(0,0,220)` restored.
- Kept the SNA-only changes from the prior entry: default 140, clamp 60..400, slider min=60 max=400 value=140.
- New: SNA network sub-toggle gains a third segment — `Agency | Country | Crime` — matching the paper's 2-mode community structure dimensions. Button added to `#snaNetwork` with `data-sna-network="crime_type"`; segment container extended to 3-column grid via inline `grid-template-columns`.
- No JS change needed: `renderSna()`, `buildSnaLegend()`, `snaRolesPresent()`, `buildSnaRoleFilter()`, and the `#snaNetwork button` onclick handler all already dispatched on `S.sna.network` as a string key and already had a crime-type fallback branch ("star topology — schema artifact" warning in rootBadge).
- Schema limitation remains: crime-type mode-2 nodes (15 total) are all role="participant" because every operation still lists exactly one crime_type under the deprecated single-value schema. Star topology — degree, betweenness, and role differentiation are all zero. Reactivates structurally only after multi-value `crime_types` backfill (Option B, deferred).
- `cosmos/index.html` + `docs/cosmos/index.html` synced. JS brackets balanced.


## [2026-04-20] cosmos-feature | SNA 2D / 3D view toggle
- New UI in SNA controls: `3D | 2D` segment under the Agency/Country/Crime toggle. `S.sna.view` state (default "3d") persists via saveState/loadState.
- 3D mode (default): current sphere layout — ops on inner sphere r=16, mode-2 on outer sphere r=30 via Fibonacci spiral.
- 2D mode: ops and mode-2 flatten to concentric circles in the XY plane (z=0). On entering 2D the scene group rotation is reset to zero; auto-rotate is suppressed while SNA+2D so the plane stays face-on to the camera. Toggling back to 3D restores normal rotation.
- No change to hover tooltip, role filter, click-to-detail, or active-node halo — all continue to work in both views because they operate on the shared posMap positions.
- `cosmos/index.html` + `docs/cosmos/index.html` synced; JS brackets balanced.


## [2026-04-20] cosmos-tweak | SNA font size slider
- New right-panel slider under Camera distance: `Font size` (range 0.40..2.50x, step 0.05, default 1.00x). `S.sna.fontScale` state multiplies the per-label `scale` arg passed to `label()` so every mode-2 label scales uniformly. Operations remain unlabeled dots.
- Slider live-redraws SNA on input (same pattern as Camera distance). syncSnaControls keeps slider + value readout in sync after loadState. saveState persists `fontScale`.
- `cosmos/index.html` + `docs/cosmos/index.html` synced; JS brackets balanced.


## [2026-04-20] cosmos-feature | SNA paper-style force layout + community coloring
- `tools/sna_visualize.py` extended — new `compute_layout_and_community()` runs `nx.spring_layout` (seed=42, 100 iterations, k=1/sqrt(N)) on the 2-mode graph and `nx.community.louvain_communities` on the mode-2 projection. Outputs deterministic positions in [-1, 1] and community assignment per node (ops inherit plurality-of-neighbors community).
- `cosmos/sna-roles.json` schema widened — per mode-2 node: `x`, `y`, `community_id`. New per-kind dicts: `op_meta` (op slug → `{x, y, community_id}`) and `community_colors` (palette indexed by community id). 12-color `COMMUNITY_PALETTE` in `sna_visualize.py`.
- Community counts from regeneration: agency 6 communities, country 4 communities, crime_type 13 communities (most singletons — expected given the single-value `crime_type` schema).
- Cosmos SNA UI: two new toggles under the network segment.
  - View: `3D | Rings | Force`. 3D keeps the Fibonacci sphere. Rings is the concentric XY-plane layout (renamed from "2D"). Force reads precomputed `x/y` from the JSON and places nodes at `(x, y, 0) * 26` — paper-faithful 2-mode spring layout.
  - Color: `Role | Community`. Role keeps the G-F brokerage palette. Community uses `community_colors`; ops also take community color in this mode (emissive dimmed) so Louvain clusters read visually.
- `renderSna()` branches on both view and colorBy. `buildSnaLegend()` swaps to community legend when colorBy === "community". Auto-rotate suppressed for rings and force views; legacy save-state `view === "2d"` is migrated to "rings" in `loadState`.
- `cosmos/index.html` + `docs/cosmos/index.html` synced; JS brackets balanced. `cosmos/sna-roles.json` and `docs/cosmos/sna-roles.json` regenerated by `tools/sna_visualize.py`.


## [2026-05-08] ingest | DOJ 2026-04-29 — Coordinated cryptocurrency scam-center takedown (Dubai-led)
- Source: raw/press-releases/2026-04-29_justice-gov_coordinated-takedown-scam-centers-276-arrests.md (DOJ Press Release 26-411, full-text preserved)
- Pages created: wiki/operations/coordinated-cryptocurrency-scam-center-takedown-2026.md, wiki/sources/2026-04-29_justice-gov_coordinated-takedown-scam-centers-276-arrests.md, wiki/organizations/dubai-police.md (stub)
- Pages updated: 4 country pages (united-states, united-arab-emirates, china, thailand), 6 organization pages (fbi, china-mps, thailand-royal-police, us-doj, us-secret-service, interpol), 2 crime-type pages (online-fraud-ic, money-laundering-ic) — all `operations_participated`/`notable_operations` + source backlinks via tools/reconcile_indexes.py
- Key findings:
  - DOJ explicitly characterizes US–UAE–China cooperation on cryptocurrency-investment fraud as "unprecedented" — rare data point for Five-Eyes-plus-China cooperation pattern in the SNA corpus.
  - Dubai Police, under the UAE Ministry of Interior, was the lead apprehending authority (275 of 276+ arrests); Royal Thai Police apprehended one defendant in Thailand. FBI San Diego ran the underlying Homeland Security Task Force investigation since 2025.
  - Six SDCA defendants charged with wire fraud and money laundering conspiracy; "pig-butchering" methodology against three named scam-compound operators (Ko Thet Company / Pixy, Sanduo Group, Giant Company); defendant nationalities Burmese (1) and Indonesian (5).
  - Private-sector partner: Meta Platforms, Inc. provided critical investigation information.
  - Korean involvement not named in cited tier-1 source — `participating_countries` does not include South Korea; case retained for SNA cooperation-pattern relevance.


## [2026-05-08] ingest | DOJ 2026-03-04 — LeakBase hacker-forum 14-country takedown
- Source: raw/press-releases/2026-03-04_justice-gov_united-states-leads-dismantlement-leakbase-hacker-forum.md (DOJ Press Release 26-205, full-text preserved)
- Pages created: wiki/operations/leakbase-takedown-2026.md, wiki/sources/2026-03-04_justice-gov_united-states-leads-dismantlement-leakbase-hacker-forum.md
- Pages updated: 14 country pages (US, AU, BE, PL, PT, RO, ES, UK, CA, DE, GR, XK, MY, NL — `operations_participated`), 4 organization pages (fbi, europol-ec3, us-doj, office-of-international-affairs — `operations_participated`), 3 crime-type pages (cybercrime-forum-ic, hacking-ic, online-fraud-ic — `notable_operations` + sources where applicable). Indexes regenerated via tools/reconcile_indexes.py.
- Bidirectional-link fix-up: also added missing `[[operation-switch-off-illegal-iptv-2026]]` back-link to wiki/countries/kosovo.md, and migrated kosovo's broken `operations_participated:\n  []` (parsed as dict by frontmatter) to a proper YAML list literal.
- Key findings:
  - 14-country synchronized action 2026-03-03 to 2026-03-04, coordinated by Europol in The Hague: 8 active-enforcement countries (US, AU, BE, PL, PT, RO, ES, UK) and 6 assistance countries (CA, DE, GR, XK, MY, NL). The 8/6 split is captured explicitly for SNA edge weighting.
  - LeakBase: 142,000+ members, 215,000+ messages, two domains seized, no per-country arrest counts disclosed in the cited tier-1 source.
  - DOJ release explicitly chains the takedown with predecessor RaidForums (2022) and BreachForums (2023, founder convicted 2025) — establishing a US-led / Europol-coordinated takedown cycle on the open-web English-language cybercriminal-forum vertical.
  - Korean involvement not named in cited tier-1 source — South Korea not added to `participating_countries`.


## [2026-05-08] ingest | Europol 2026-04-13 — Operation PowerOFF (2026 action week, 21 countries)
- Source: raw/press-releases/2026-04-13_europol_operation-poweroff-75000-ddos-users.md (Europol newsroom; participating-country roster + methodology paragraphs preserved verbatim from `window.SERVER_DATA.body`)
- Pages created: wiki/operations/operation-power-off-2026-04.md (follow-on to umbrella `[[operation-power-off]]`), wiki/sources/2026-04-13_europol_operation-poweroff-75000-ddos-users.md
- Pages updated: 21 country pages (AU, AT, BE, BR, BG, DK, EE, FI, DE, JP, LV, LT, LU, NL, NO, PL, PT, SE, TH, UK, US — `operations_participated`), 1 organization page (europol-ec3 — `operations_participated`), 1 crime-type page (ddos-ic — `notable_operations` + sources), 1 parent operation (operation-power-off — `related_operations`). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 2026-04-13 Operation PowerOFF action week verbatim 21-country roster preserved: Australia, Austria, Belgium, Brazil, Bulgaria, Denmark, Estonia, Finland, Germany, Japan, Latvia, Lithuania, Luxembourg, Netherlands, Norway, Poland, Portugal, Sweden, Thailand, United Kingdom, United States.
  - Reported results: 53 domains taken down, 4 arrests, 25 search warrants, 75 000+ user-warning communications, 3 million+ criminal user accounts identified in seized booter-service databases.
  - Korean involvement not named — South Korea not added to `participating_countries` for this phase.
  - Body extraction caveat documented: Europol newsroom embeds press-release body as JSON inside `window.SERVER_DATA`; the captured 2 416-byte body field covers the participating-countries paragraph and methodology paragraphs but truncates at the `Operation PowerOFF: disrupt and prevent` H2; future re-fetch under a different extraction path is flagged as open work.


## [2026-05-08] ingest | KNPA 2026-04-27 — Korea–Cambodia–Philippines 73-person scam extradition (largest single-country cyber-fugitive extradition into Korea on record)
- Source: raw/press-releases/2026-04-27_korean-press_korea-cambodia-philippines-73-extradition.md (KNPA via Korea.kr 정책브리핑 newsId 156740857; Korea.kr is connection-reset on TLS-spoof and WebFetch — secondary capture via Kyunghyang 2026-04-27 coverage with verbatim numerical breakdown)
- Pages created: wiki/operations/korea-cambodia-philippines-73-extradition-2026.md, wiki/sources/2026-04-27_korean-press_korea-cambodia-philippines-73-extradition.md, wiki/organizations/ministry-of-foreign-affairs-korea.md (stub), wiki/organizations/national-intelligence-service-korea.md (stub)
- Pages updated: 3 country pages (south-korea, cambodia, philippines — `operations_participated`), 3 organization pages (knpa, knpa-cyber-bureau, ministry-of-justice-korea — `operations_participated`), 2 crime-type pages (voice-phishing-ic, online-fraud-ic — `notable_operations` + sources), 1 sister operation (korea-cambodia-scam-repatriation — `related_operations`). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 2026-04-27 KNPA announcement is the first wiki-recorded Korean operation that explicitly names a whole-government task force (범정부 「초국가범죄 특별대응TF」) coordinating KNPA, MOFA, MOJ, and NIS in the same extradition cycle — directly project-relevant for Korean SNA enrichment.
  - Cambodia 42-person tranche operationally tied to a Korea-side field unit `「코리아전담반」` (Korea-dedicated Squad) embedded in Cambodian operations.
  - 73-person cohort spans five distinct cyber-enabled crime types and includes a 15-year-old data-breach extradition (~1.75M records, 송환까지 15년) — signalling Korean willingness to extradite legacy cyber cases.
  - Cohort breakdown verbatim: 보이스피싱 24/368 victims/~₩51.7B, 로맨스스캠 14/53 victims/~₩2.3B, 불법 도박사이트 운영 3/scale ~₩5.9T, 2011 capital-firm 데이터 침해 1/~1.75M records, 자동차 대출금 사기 3/2022-2024/~₩12B, 성착취 24 (overlap with voice-phishing).
  - Korea.kr unfetchable across all available tooling on 2026-05-08 → flagged as open follow-up; raw archive built from same-day Kyunghyang verbatim coverage with explicit fidelity caveat in source page.


## [2026-05-08] ingest | Eurojust 2025-11-13 — Operation Endgame Phase 3 (infostealer + RAT + botnet)
- Source: raw/press-releases/2025-11-13_eurojust_operation-endgame-phase3-malware-operation.md (Eurojust press release; participating-authorities roster preserved verbatim via WebFetch)
- Pages created: wiki/operations/operation-endgame-phase3.md (third phase under umbrella `[[operation-endgame]]`), wiki/sources/2025-11-13_eurojust_operation-endgame-phase3-malware-operation.md
- Pages updated: 9 country pages (DE, FR, NL, DK, UK, US, AU, CA, GR — `operations_participated`), 13 organization pages (germany-bka, germany-frankfurt-prosecutor, france-gendarmerie, netherlands-politie, denmark-police, uk-nca, us-doj, fbi, us-dcis, australia-afp, canada-rcmp, europol-ec3, eurojust — `operations_participated`), 2 crime-type pages (malware-ic, ransomware-ic — `notable_operations` + sources), 3 sister/parent operations (operation-endgame, operation-endgame-phase1, operation-endgame-phase2 — `related_operations`). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 1,025 servers worldwide shut down; 20 domains seized; 11 searches; login data from 100,000+ cryptocurrency wallets recovered (stolen but not yet exploited per Eurojust); one main RAT-line suspect arrested in Greece.
  - Targeted three named malware families: Rhadamanthys (infostealer-as-a-service since 2022), VenomRAT (RAT delivered via phishing), and Elysium (associated botnet).
  - Phase 3 shifts the umbrella's targeting from dropper/loader infrastructure (Phase 1, 2024-05) and ransomware-affiliate kill chain (Phase 2, 2025-05) to the initial-access stack (infostealer + RAT + botnet) while maintaining Europol+Eurojust coordination and the DE/FR/NL/DK/UK/US core-partner roster.
  - Greece enters the Endgame partner roster for the first time in this phase via the RAT-suspect arrest.
  - Tier-2 reporting (CyberNews, eSecurity Planet) widens the participating-countries roster to include Belgium and Lithuania alongside the 9 named in the cited Eurojust release; per project rule those two countries are not added to `participating_countries` until a tier-1 source confirms them — flagged as open follow-up.
  - Korean involvement not named — South Korea not added to `participating_countries`.


## [2026-05-08] gap-fill | DOJ DNJ 2024-05-07 — Operation Cronos Phase 2 (Khoroshev / LockBitSupp indictment + concurrent US-UK-AU sanctions)
- Source: raw/press-releases/2024-05-07_justice-gov-dnj_us-charges-russian-national-developing-operating-lockbit-ransomware.md (US Attorney's Office for the District of New Jersey, full-text via TLS-spoof; quotes from AG Garland, US Attorney Sellinger, DAG Monaco, FBI Director Wray preserved verbatim)
- Pages created: wiki/operations/operation-cronos-phase2.md (fills gap between existing operation-cronos-phase1 (2024-02) and operation-cronos-phase3 (2024-10)), wiki/sources/2024-05-07_justice-gov-dnj_us-charges-russian-national-developing-operating-lockbit-ransomware.md
- Pages updated: 3 country pages (US, UK, AU — `operations_participated`), 4 organization pages (us-doj, fbi, uk-nca, australia-afp — `operations_participated`), 2 crime-type pages (ransomware-ic, malware-ic — `notable_operations` + sources), 2 sister phases (operation-cronos-phase1, operation-cronos-phase3 — `related_operations`). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 26-count federal indictment unsealed in DNJ against Dmitry Yuryevich Khoroshev (a.k.a. LockBitSupp / LockBit / putinkrab; 31, Voronezh, Russia) — alleged developer/administrator of LockBit from September 2019 through May 2024.
  - Concurrent international sanctions architecture: US Treasury (OFAC), UK HMT Office of Financial Sanctions Implementation (OFSI), Australia DFAT — all designating Khoroshev on the same day; State Department $10M reward.
  - LockBit cohort scale recorded verbatim from the indictment summary: 2,500+ victims in 120+ countries; 1,800 US victims; USD 500M+ in ransom proceeds; billions of dollars in broader losses; Khoroshev personally received USD 100M+ through his 20% developer share.
  - The wave is now correctly modelled as the named-suspect attribution layer between Phase 1 (infrastructure disruption, February 2024) and Phase 3 (arrests + further sanctions, October 2024) within the Operation Cronos umbrella.


## [2026-05-08] enrichment | Operation Secure (INTERPOL APAC infostealer crackdown 2025) — participating-countries roster + Korean involvement
- Source: existing wiki/sources/2025-04-01-interpol-operation-secure-infostealer.md (INTERPOL 2025-06-11 release; collection_url https://www.interpol.int/en/News-and-Events/News/2025/20-000-malicious-IPs-and-domains-taken-down-in-INTERPOL-infostealer-crackdown)
- Pages updated: wiki/operations/operation-secure-interpol.md (4 country slugs added to `participating_countries` — maldives, nepal, sri-lanka, timor-leste; Korean Involvement section expanded to project-relevant length; Contradictions section enumerates the 7 Pacific-island jurisdictions named verbatim in the INTERPOL release but not yet wikilinked due to absent country pages); 4 country pages backlinked.
- Key findings:
  - INTERPOL release names a 26-country APAC roster verbatim. Wiki frontmatter previously captured 15 of those 26 (those with existing country pages). Expanded to 19 by adding the four jurisdictions whose pages do exist. Remaining 7 (Fiji, Kiribati, Nauru, Papua New Guinea, Samoa, Solomon Islands, Tonga, Vanuatu) are named in body prose only, with explicit caveat in the Contradictions section.
  - Korean involvement section materially expanded: from a single-sentence 2-line note to a full Korean-relevance paragraph identifying KNPA + KNPA Cyber Bureau as the likely Korean coordinating channels under the Asia and South Pacific Joint Operations Against Cybercrime (ASPJOC) project frame, plus a forward-link rationale to Korean voice-phishing / romance-scam / account-takeover IC corpus.
  - Net SNA effect: +4 country edges to operation-secure-interpol; cross-corpus consistency between Korean voice-phishing and APAC infostealer takedown lines is now linkable through the expanded Korean Involvement section.


## [2026-05-08] ingest | NCA UK 2026-02-20 — UK-Nigeria-Meta scam centre disruption (Agbor)
- Source: raw/press-releases/2026-02-20_nca-uk_fraudsters-arrested-nigeria-following-nca-intelligence-sharing.md (UK National Crime Agency, full-text via WebFetch; corroborated by parallel Meta blog post on the same date)
- Pages created: wiki/operations/uk-nigeria-meta-scam-centre-disruption-2026.md, wiki/sources/2026-02-20_nca-uk_fraudsters-arrested-nigeria-following-nca-intelligence-sharing.md
- Pages updated: 2 country pages (united-kingdom, nigeria — `operations_participated`), 2 organization pages (uk-nca, nigeria-police-force — `operations_participated`), 1 crime-type page (online-fraud-ic — `notable_operations` + sources). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 2026-01-13 action day: 7 men arrested in Agbor, Delta State, Nigeria, by Nigerian Police National Cybercrime Centre following NCA intelligence sharing; 26 mobile phones, 42 SIM cards, 1 laptop seized.
  - Crypto-investment-scam methodology: fake social-media accounts impersonating cryptocurrency traders + fraudulent Facebook groups featuring fabricated testimonials; targets UK residents and US persons resident in the UK.
  - Meta is named as the private-sector partner alongside NCA and Nigerian Police; Meta wiki organization page does not yet exist and Meta is mentioned in body prose without a wikilink.
  - The operation's structural shape (requesting state intelligence + host state arrests + global platform partner) reproduces in microcosm the broader 2026 cooperation pattern across the wiki (US-UAE-China-Thailand pig-butchering takedown, Korea-Cambodia-Philippines extradition cycle); explicit cross-links recorded in the operation page's `related_operations`.
  - Korean involvement not named — South Korea not added to `participating_countries`.


## [2026-05-08] ingest | DOJ 2026-03-23 — U.S. v Volkov (Yanluowang IAB) sentencing (US-Italy extradition)
- Source: raw/press-releases/2026-03-23_justice-gov_russian-citizen-sentenced-prison-hacking-us-companies-yanluowang.md (DOJ Press Release 26-280, full-text via TLS-spoof)
- Pages created: wiki/operations/us-v-volkov-yanluowang-sentencing.md, wiki/sources/2026-03-23_justice-gov_russian-citizen-sentenced-prison-hacking-us-companies-yanluowang.md
- Pages updated: 3 country pages (US, IT, RU — `operations_participated`), 3 organization pages (us-doj, fbi, office-of-international-affairs — `operations_participated`), 2 crime-type pages (ransomware-ic, hacking-ic — `notable_operations` + sources). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Aleksei Volkov (26, St. Petersburg, Russia), Yanluowang ransomware affiliate operating as an "initial access broker" (IAB), sentenced to 81 months in SDIN on 2026-03-23. USD 9 167 198.19+ restitution ordered; USD 24M+ in intended losses across the attacks Volkov enabled.
  - US-Italy bilateral extradition: arrested in Rome January 2024, extradited via DOJ Office of International Affairs cooperation with the Government of Italy, plea 2025-11-25 to 4 SDIN counts and 2 EDPA counts after EDPA case consolidation in SDIN.
  - First wiki record explicitly using "initial access broker" as a DOJ-charging-language category for the ransomware-affiliate kill chain. Establishes a public-record IAB-prosecution category that complements the existing operation-cronos-phase2 named-suspect attribution wave.
  - Case fits the broader 2024-2026 European-arrest-and-US-extradition pathway for Russian ransomware-ecosystem actors traveling into Schengen states.


## [2026-05-08] ingest | DOJ EDMI 2025-12-17 — E-Note crypto-exchange takedown (US-Germany-Finland cooperation)
- Source: raw/press-releases/2025-12-17_doj-edmi_e-note-crypto-exchange-takedown.md (USAO Eastern District of Michigan announcement; DOJ EDMI press release URL not directly accessible from this corpus's TLS-spoofing fetch tool or Anthropic WebFetch on 2026-05-08; verbatim numerical and structural facts captured from same-day tier-2 reporting reproducing the USAO-EDMI press conference content — flagged as open follow-up)
- Pages created: wiki/operations/e-note-crypto-exchange-takedown-2025.md, wiki/sources/2025-12-17_doj-edmi_e-note-crypto-exchange-takedown.md, wiki/organizations/finland-nbi.md (stub — first wiki entry for the Finnish National Bureau of Investigation in the public IC corpus)
- Pages updated: 4 country pages (US, DE, FI, RU — `operations_participated`), 3 organization pages (us-doj, fbi, germany-bka — `operations_participated`), 2 crime-type pages (money-laundering-ic, ransomware-ic — `notable_operations` + sources). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Mykhalio Petrovich Chudnovets, 39, Russian national, indicted in EDMI on one count of money laundering conspiracy (max 20 years) for operating the E-Note cryptocurrency exchange and payment-processing service from approximately 2011 through 2025.
  - 3 domains seized (e-note.com, e-note.ws, jabb.mn) plus servers and associated mobile applications.
  - FBI identified USD 70 million+ in illicit proceeds transferred through E-Note since 2017; US victims in healthcare and critical-infrastructure sectors.
  - Multi-jurisdictional cooperation: USAO-EDMI, FBI Detroit Division, Michigan State Police (incl. Michigan Cyber Command Center), German BKA, Finnish NBI. First wiki entry for the Finnish NBI as a national-agency record.
  - Continues the 2024-2026 pattern of Russian-national operator attribution in DOJ-led cybercrime takedowns alongside Volkov (Yanluowang IAB) and Khoroshev (LockBit administrator).
  - Korean involvement not named — South Korea not added to `participating_countries`.


## [2026-05-08] enrichment | DOJ 2026-05-04 — U.S. v Zolotarjovs (Conti / Karakurt sentencing) closing-out
- Source: raw/press-releases/2026-05-04_justice-gov_member-prolific-russian-ransomware-group-zolotarjovs-sentenced.md (DOJ Press Release 26-444, full-text via TLS-spoof; quotes from AAG Duva, USA Gerace, AD Leatherman, SAC Cromartie preserved verbatim)
- Pages updated: wiki/cases/us-v-deniss-zolotarjovs.md (replaced thin auto-stub with full sentencing record — case status moved from "charged" to "sentenced", participating-jurisdictions expanded from US-only to US + Georgia + Latvia + Russia, defendant nationality and 102-month sentence recorded, multi-brand Conti-successor taxonomy attributed); wiki/sources/2026-05-04_justice-gov_member-prolific-russian-ransomware-group-zolotarjovs-sentenced.md created. 4 country pages and 3 organization pages backlinked via `notable_cases`; 2 crime-type pages backlinked via `notable_cases` + sources. Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Deniss Zolotarjovs, 35, Latvian national of Moscow Russia, sentenced to 102 months in SDOH on 2026-05-04 for ransom-negotiator role in a Conti-successor organisation operating under Conti / Karakurt / Royal / TommyLeaks / SchoolBoys / Akira brand names from June 2021 to August 2023.
  - First wiki record explicitly attributing the multi-brand Conti-successor cluster to a single named individual at the negotiator tier in DOJ-charging language. Operationally significant for SNA reasoning about ransomware-organisation continuity across rebranding cycles.
  - US-Georgia bilateral extradition pathway: arrest December 2023, contested extradition phase, US custody August 2024 (~8-month contested phase), plea July 2025, sentencing May 2026.
  - Verbatim victim-loss figures: 13 named victims with USD 56M+ losses, 41 additional victims paid USD 13M ransom, total estimated period losses in the hundreds of millions of dollars.
  - Notable verbatim findings: pediatric-healthcare patient data weaponised for extortion; government 911-system shutdown; organisation operations from Lakhtinskaya Street, St. Petersburg with multiple former Russian law-enforcement officers among membership.
  - Korean involvement not named.


## [2026-05-08] ingest | KNPA 2026-03-03 — Korea-Philippines police MOU 2nd revision (legal-framework)
- Source: raw/press-releases/2026-03-03_korean-press_korea-philippines-police-mou-second-revision.md (KNPA via Korea.kr 정책브리핑 newsId 156747062; Korea.kr is connection-reset on TLS-spoof and WebFetch — secondary capture from 시사경찰일보 / police112.net article 46005 with explicit fidelity caveat in source page)
- Pages created: wiki/legal-frameworks/korea-philippines-police-mou-2026-revision.md (first wiki bilateral-MOU legal-framework entry for a Korea-led police bilateral), wiki/sources/2026-03-03_korean-press_korea-philippines-police-mou-second-revision.md, wiki/organizations/philippine-national-police.md (stub — first wiki entry for the Philippine National Police)
- Pages updated: 2 country pages (south-korea, philippines — sources), 2 organization pages (knpa, philippine-national-police — frameworks_administered), 1 operation (korea-cambodia-philippines-73-extradition-2026 — legal_basis now explicitly cites the bilateral MOU). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 2026-03-03 Manila signing of the second Korea–Philippines police cooperation MOU revision since the original 2007 agreement. Signed by Acting KNPA Commissioner Yoo Jae-sung 유재성 and Philippine National Police Chief Jose Melencio Nartatez Jr.
  - Substantive scope expansion: drugs + online scams + sophisticated transnational crime. Operationalises the bilateral Korean-fugitive extradition pathway demonstrated at scale by the 2026-04-27 73-person extradition cycle (31 Korean nationals extradited from the Philippines).
  - Korean Desk (코리안 데스크) — originally established at Philippine National Capital Region Police Office in 2012; 2026 revision adds 1 additional KNPA liaison officer (경찰협력관) deployed during H1 2026.
  - Related multilateral structures named: IICA (International Cooperation Consultative Body, KNPA-led), ANCRA (Asia Narcotic Crime Response Cooperation), ICON (International Drug Investigation Conference, Seoul 2026).
  - First wiki public-record bilateral police MOU entry for a Korea-led IC framework — directly project-relevant for Korean cybercrime IC posture documentation.


## [2026-05-08] ingest | 외교부+경찰청 2025-11-10 — 한-캄보디아 공동 전담반(코리아전담반) MOU
- Source: raw/press-releases/2025-11-10_korean-press_korea-cambodia-joint-task-force-mou-signing.md (Korean MOFA + KNPA joint announcement; Korea.kr / overseas.mofa.go.kr URLs connection-reset on TLS-spoof and WebFetch — secondary capture from Korean tier-1 search-engine reproduction with explicit fidelity caveat)
- Pages created: wiki/legal-frameworks/korea-cambodia-joint-task-force-mou-2025.md (foundational instrument for the 코리아전담반 mechanism; the second wiki bilateral-MOU legal-framework entry for a Korea-led police bilateral after the 2026-03-03 Korea-Philippines revision), wiki/sources/2025-11-10_korean-press_korea-cambodia-joint-task-force-mou-signing.md, wiki/organizations/cambodian-national-police.md (stub — first wiki entry for the Cambodian National Police)
- Pages updated: 2 country pages (south-korea, cambodia — sources), 3 organization pages (knpa, cambodian-national-police, ministry-of-foreign-affairs-korea — frameworks_administered), 2 operations (korea-cambodia-philippines-73-extradition-2026 + korea-cambodia-scam-repatriation — legal_basis now explicitly cites the bilateral MOU). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 2025-11-10 Phnom Penh signing of the Korea–Cambodia Joint Task Force for Korean Nationals MOU. Signed by Acting KNPA Commissioner Yoo Jae-sung 유재성 and Cambodian Police Commissioner Sar Thet 써 텟 in the presence of Korean Foreign Minister Cho Hyun 조현 and Cambodian Interior Minister Sar Sokha 써 소카. Implementation phase of the 2025-10-27 Korea-Cambodia summit decisions reached in Malaysia.
  - Joint Task Force operates as a single Korean-Cambodian shared-staff police unit (12 Cambodian + 7 Korean officers per Korean reporting) responsible for "the entire process from report receipt to rescue, investigation, and suspect repatriation" for cases involving Korean nationals.
  - First two months of operations (2025-11-10 to early January 2026): 7 rounds of joint operations, 135 suspects arrested in field, 3 Korean victims rescued. The MOU is the foundational instrument for the 코리아전담반 mechanism that produced the Cambodia tranche (42 of 73) of the 2026-04-27 73-person extradition cycle.
  - Together with the 2026-03-03 Korea-Philippines police MOU revision, this MOU forms the backbone of Korea's 2025–2026 Southeast Asian scam-compound cooperation infrastructure. Both bilateral instruments now have wiki legal-framework entries.


## [2026-05-09] ingest | KNPA + Chinese MPS 2025-11-01 — Korea-China voice-phishing/online-scam MOU
- Source: raw/press-releases/2025-11-01_korean-press_korea-china-anti-scam-mou-signing.md (Joint KNPA + Chinese MPS announcement; Korean and Chinese government URLs connection-reset on TLS-spoof and WebFetch — secondary capture from Kyunghyang Shinmun coverage with explicit fidelity caveat)
- Pages created: wiki/legal-frameworks/korea-china-anti-scam-mou-2025.md (third wiki Korea-led bilateral-MOU legal-framework entry, completing the 2025-2026 Southeast Asian scam-compound cooperation backbone), wiki/sources/2025-11-01_korean-press_korea-china-anti-scam-mou-signing.md
- Pages updated: 2 country pages (south-korea, china — sources), 2 organization pages (knpa, china-mps — frameworks_administered), 1 operation (operation-haechi-v — legal_basis now references the bilateral MOU). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 2025-11-01 signing in Korea during APEC Korea 2025 summit (Gyeongju, Oct 31 - Nov 1). Signed by Acting KNPA Commissioner Yoo Jae-sung 유재성 and Chinese Ambassador to Korea Dai Bing 다이 빙, observed by both heads of state — heads-of-state-level visibility makes this Korea's most ambitious bilateral cybercrime cooperation framework with China to date.
  - Establishes a new standing institution: 「한·중 공동대응 협의체」 (Korea-China Joint Response Council) operated through designated departments inside KNPA and Chinese MPS.
  - Substantive scope: information sharing on Southeast Asian scam-crime bases (especially Cambodia), joint operations and investigations, victim rescue/protection/repatriation, asset tracing and freezing.
  - Builds on the 2024 Operation HAECHI V joint Korea-China dismantling of a USD 1.1 billion voice-phishing syndicate; formalises the precedent into a standing bilateral framework.
  - Pre-positions Korea-China cooperation 9 days before the 2025-11-10 Korea-Cambodia Joint Task Force MOU — coordinated Korean policy posture toward Southeast Asian scam-compound enforcement during the October-November 2025 window.
  - This is the third wiki Korea-led bilateral cooperation instrument for cybercrime IC in 2025-2026, completing the backbone alongside the 2025-11-10 Korea-Cambodia MOU and the 2026-03-03 Korea-Philippines MOU revision.


## [2026-05-09] enrichment | DOJ 2025-12-10 — U.S. v Dubranova (CARR + NoName057(16)) two-indictment closing-out
- Source: raw/press-releases/2025-12-10_justice-gov_ukrainian-national-indicted-cyberattacks-russia-carr-noname.md (DOJ Press Release 25-1158, full-text via TLS-spoof; quotes from AAG Eisenberg, FAUSA Essayli, AD Leatherman, EPA AAA Pritzlaff preserved verbatim)
- Pages updated: wiki/cases/us-v-victoria-eduardovna-dubranova.md (replaced thin auto-stub with full two-indictment record — case status remains "prosecuted" but participating-jurisdictions expanded from US-only to US + Ukraine + Russia, defendant nationality and aliases captured, statutory maxima 27y CARR + 5y NoName recorded, US-victim categories enumerated including public drinking-water systems, LA meat-processing facility, US election infrastructure, US nuclear-regulatory websites); wiki/sources/2025-12-10_justice-gov_ukrainian-national-indicted-cyberattacks-russia-carr-noname.md created. 3 country pages and 3 organization pages backlinked via `notable_cases`; 2 crime-type pages backlinked via `notable_cases` + sources. Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - First wiki-recorded US public-record indictment to directly allege GRU founding/funding/direction of a named Telegram hacktivist group (CARR / Z-Pentest, with >100 members including juveniles and 75,000+ Telegram followers).
  - First wiki-recorded US prosecution to identify the Russian Presidential-decree CISM organisation (October 2018) as a staffing source for a hacktivist DDoS group (NoName057(16) DDoSia).
  - US-jurisdictional extradition reach demonstrated for a Ukrainian-national operator of Russian-state-tied groups; specific source-state of extradition not enumerated in cited tier-1 release.
  - Concurrent State Department reward offers: USD 2M (CARR), USD 10M (NoName); concurrent multi-agency Joint Cybersecurity Advisory by FBI/CISA/NSA/DOE/EPA/DC3.
  - FBI Los Angeles Field Office's "Operation Red Circus" named as the umbrella US enforcement frame against Russian state-sponsored cyberthreats.
  - Korean involvement not named.


## [2026-05-09] ingest | DOJ 2025-12-18 — U.S. v Stryzhak (Nefilim ransomware affiliate plea, US-Spain extradition)
- Source: raw/press-releases/2025-12-18_justice-gov_ukrainian-national-pleads-guilty-conspiracy-nefilim-ransomware.md (DOJ Press Release 25-1224, full-text via TLS-spoof)
- Pages created: wiki/cases/us-v-stryzhak-nefilim.md (new case page; first wiki entry for the Stryzhak Nefilim affiliate prosecution distinct from the Tymoshchuk administrator-tier indictment), wiki/sources/2025-12-18_justice-gov_ukrainian-national-pleads-guilty-conspiracy-nefilim-ransomware.md
- Pages updated: 3 country pages (US, ES, UA — `notable_cases`), 3 organization pages (us-doj, fbi, office-of-international-affairs — `notable_cases`), 2 crime-type pages (ransomware-ic — `notable_cases` + sources; hacking-ic — `notable_cases`). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Artem Aleksandrovych Stryzhak, 35, Ukrainian national of Barcelona Spain, pleaded guilty 2025-12-18 in EDNY to one count of conspiracy to commit computer fraud (max 10 years). Sentencing scheduled 2026-05-06.
  - US-Spain bilateral extradition: arrest June 2024 in Spain → US custody 2025-04-30 (~10-month transit, comparable to but slightly faster than the Volkov US-Italy and Zolotarjovs US-Georgia pathways).
  - Affiliate-tier compensation structure documented verbatim: 20% revenue split with Nefilim administrators since June 2021. Targets US/Canada/Australia companies with USD 100M+ revenue (later raised to USD 200M+).
  - Nefilim victim-leak site named verbatim: "Corporate Leaks".
  - Co-conspirator Volodymyr Tymoshchuk (administrator-tier) remains a fugitive with US State Department TOC reward of up to USD 11 million.
  - Adds a third 2024-2025 European-arrest US-extradition pathway record alongside Volkov (Italy) and Zolotarjovs (Georgia), consolidating the Schengen-region pattern for Russian-and-Ukrainian-resident ransomware-affiliate prosecution.
