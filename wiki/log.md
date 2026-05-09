# Activity Log

## [2026-05-10] ingest [iter 119, single-agent, under-sourced tier-1 publisher] | PF Belgium-Brazil passive extradition arrest (PF/SR-SP, 2026-03-09, Belgian national wanted for IT-forgery + fraud)
- Sources: 1 raw + 1 source page (pt) + 1 operation page (3 new pages)
- Pages created: `raw/press-releases/2026-03-09_pf-gov-br_pf-prende-foragido-belga-fraude-falsificacao-tecnologia-informacao-sao-paulo.md`, `wiki/sources/2026-03-09_pf-gov-br_pf-prende-foragido-belga-fraude-falsificacao-tecnologia-informacao-sao-paulo.md`, `wiki/operations/pf-belgium-extradition-arrest-sao-paulo-2026.md`.
- Pages NOT updated (per task instruction: do NOT touch backlinks): country (brazil, belgium), organization (brazil-ministry-of-justice-public-security), mechanism (extradition), legal-framework (budapest-convention), crime-type (online-fraud-ic), concept (dual-criminality).
- Key findings:
  - **Third wiki ingest from gov.br/pf** (after Operação Magna Fraus 2025-10-30 and Operação Dark Bet 2025-12-16) — the publisher remains under-sourced and benefits from a Belgium-as-requesting / Brazil-as-requested extradition record.
  - **2026-03-09 PF/SR-SP arrest in São Paulo** of a Belgian national residing in Brazil on a STF *mandado de prisão para extradição* in response to a Belgian extradition request. Belgian charges enumerated by PF: document forgery, criminal threat, fraud, **falsificação de tecnologia da informação** (computer-related forgery — Budapest Convention Art. 7 territory), breach of trust, and unspecified additional offences.
  - **First wiki record of the Brazilian-Portuguese rendering** *falsificação de tecnologia da informação* for what under Belgian law is *falsification informatique / informaticavalsheid* (Code pénal / Strafwetboek Art. 210bis) and under Budapest Convention is Art. 7. Translation pattern noted for future PF extradition releases.
  - **Per L19**: only Brazil and Belgium asserted as participating_countries (both named in the primary source). Per L23: lead_agency and coordinating_body left as empty strings; Belgian counterpart authority and specific PF unit beyond SR/SP not named in the release. Per L17: no headcount/country-count fields to verify.
- Process notes: gov.br/pf landing-page WebFetch produced minimal content; pivoted to direct article URL via WebFetch + curl_cffi chrome124 (200 OK, 110KB) for verbatim Portuguese capture. Rejected candidates this iter: PowerOFF 2026-04-16 (already heavily sourced — 2 PF, 1 Europol, 2 DOJ, multiple secondary), Operação Citrus 2026-02-26 (no IC element), Operação Cryptoscam 2025-05 (already in wiki as `spf-fpb-operation-cryptoscam-2025`), Operação Synergia III (Brazil+71 countries, but PF is secondary; INTERPOL is primary and already covered for Synergia series), Goiás Portuguese-Belgian fugitive 2026-04 (financial-fraud only, weaker cyber nexus than the IT-forgery-charged São Paulo case).

## [2026-05-10] ingest [iter 117, single-agent, new-publisher tier-1] | Operación Aliados por la Infancia VI (MPF CABA, 2026-04-29, AR-led 13-jurisdiction CSAM operation)
- Sources: 1 raw + 1 source page (es) + 1 operation page (3 new pages)
- Pages created: `raw/press-releases/2026-04-29_mpf-caba_aliados-por-la-infancia-vi-megaoperativo-internacional.md`, `wiki/sources/2026-04-29_mpf-caba_aliados-por-la-infancia-vi-megaoperativo-internacional.md`, `wiki/operations/aliados-por-la-infancia-vi-mpf-caba-2026.md`.
- Pages NOT updated (per task instruction: do NOT touch backlinks): country (argentina, brazil, panama, dominican-republic, guatemala, uruguay, paraguay, costa-rica, spain, peru, honduras, france), organization (us-dhs, ncmec), crime-type (csam-ic), mechanism (informal-cooperation).
- Key findings:
  - **First wiki ingest from mpfciudad.gob.ar (Ministerio Público Fiscal de la Ciudad Autónoma de Buenos Aires)**, the prosecutor's office of the City of Buenos Aires that coordinates the recurring "Aliados por la Infancia" multilateral CSAM operation series. Iteration **VI** (April 28-29 2026) is the largest published instance: **270 raids across 13 jurisdictions, 84 detentions** (26 in Argentina, 44 Brazil, 7 Panama, 3 Uruguay, 3 Peru, 1 Puerto Rico).
  - **Tripartite IC channel** explicitly named in the primary source: U.S. Embassy in Buenos Aires + U.S. Department of Homeland Security + MPF CABA via Cuerpo de Investigaciones Judiciales (CIJ). Detection driven by **ICACCOPS (Internet Crimes Against Children Child Online Protection System)** via Argentine agreement with the National Criminal Justice Training Center (Fox Valley Technical College, Wisconsin) plus **CPS (Child Protection System)** by Child Rescue Coalition. Inbound tip stream: NCMEC CyberTipline.
  - Argentine federal/city enforcement line of effort named (Policía de la Ciudad, Policía Federal Argentina, Gendarmería Nacional, Prefectura Naval Argentina) — none currently wiki entities; left in prose only per L23.
  - Per L19, included only the 12 jurisdictions enumerated in the verified raid breakdown; Mexico/Colombia/El Salvador (mentioned only in secondary press summaries) excluded; Puerto Rico left in prose only since no Puerto Rico country wiki page exists. Headline-vs-detail country count discrepancy ("otros 15 países" vs. enumerated 12) flagged in Contradictions section.
- Process notes: WebFetch on PDI Chile (HTTP 403) and gov.br PF and gob.mx FGR landing pages all blocked; pivoted to MPF CABA via curl_cffi chrome124 (200 OK, 439KB, BeautifulSoup get_text). Pre-checked candidates: AFP Australia (already ingested 2026-05-08), RCMP (already ingested), KNPA (already ingested), NPA Japan (already ingested), Brazil PF (Operação Cryptoscam already exists as `spf-fpb-operation-cryptoscam-2025`), PDI Chile Orión III (couldn't get tier-1 primary URL — Cloudflare 403 — deferred). Per L23, lead_agency / coordinating_body left as empty strings (Argentine prosecutor entity not yet a wiki entity page).

## [2026-05-10] ingest [iter 114, partner-state primary source] | Italy → US extradition of PRC HAFNIUM hacker (Polizia di Stato, 2026-04-27, IT+US)
- Sources: 1 raw + 1 source page (it) + 1 operation page (3 new pages)
- Pages created: `raw/press-releases/2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti.md`, `wiki/sources/2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti.md`, `wiki/operations/italy-china-us-hafnium-hacker-extradition-2026.md`.
- Pages NOT updated (per task instruction: do NOT touch backlinks): country (italy, united-states), organization (polizia-di-stato, italy-polizia-postale, fbi, fbi-cyber-division, us-doj, office-of-international-affairs), crime-type (hacking-ic, malware-ic), mechanism (extradition).
- Key findings:
  - **Italy-side primary-source for the Italy → US extradition of the HAFNIUM PRC contract hacker** (referred to as "X. Z." in the Italian release per Italian presumption-of-innocence convention; identified as **Xu Zewei** in the parallel US DOJ release of the same date 2026-04-27). The case-prosecution angle was already documented in [[us-v-xu-zewei-hafnium-extradited-italy]]; this new operation page captures the **Italian-partner-state operational angle** that the US release summarises only as "Italian National Police — Cyber Division".
  - **Six Italian agencies/authorities named** in the Italian release: (1) Polizia di Stato, (2) Servizio Polizia Postale e per la Sicurezza Cibernetica (Polizia Postale), (3) Polaria di Malpensa (border police, Malpensa airport — co-executed July 2025 arrest), (4) Servizio per la Cooperazione Internazionale di Polizia (Italian INTERPOL-NCB-equivalent — coordinated extradition handover), (5) Corte d'Appello di Milano (extradition decision), (6) Ministro della giustizia (final extradition authorisation). The full Italian extradition authorisation chain (Corte d'Appello + Ministro) is the standard Italian-law procedural pathway under Codice di procedura penale Libro XI for treaty-based extraditions.
  - Italian-law charges-frame: associazione per delinquere + accesso abusivo a sistemi informatici + frode informatica + furto d'identità — closely mirrors US 9-count indictment categories (wire-fraud conspiracy, unauthorized access to protected computers, identity theft) → dual-criminality cross-reference established.
  - Italian release explicitly characterises the FBI–Italian-investigators relationship as "una lunga collaborazione operativa" (a long operational collaboration) — *highly likely* to refer to FBI targeting intelligence flowing to Italian investigators in advance of the July 2025 Malpensa airport interception (suspect was on a holiday transit, not a scheduled appearance), implying real-time intelligence sharing.
  - First wiki record of an Italy → US extradition of a PRC state-sponsored cyber actor sourced from the **Italian primary-source side** — complements the US-prosecution-side documentation in the existing case page.
- Process notes: curl_cffi chrome120 → 200 OK on commissariatodips.it (no Cloudflare/Akamai challenge). BeautifulSoup main-tag extraction worked first try. Pre-checked candidates: BMI Austria (recent items not cyber-IC), fedpol.admin.ch (404 / 426 on multiple URL patterns), policija.lrv.lt (403 on chrome120 + chrome124), poliziadistato.it/articolo/ (404 on listing page; only static reference articles surfaced from home page). Polaria di Malpensa, Servizio per la Cooperazione Internazionale di Polizia, Corte d'Appello di Milano, Ministro della giustizia, and the US-Italy 1983 extradition treaty have no wiki entity pages → recorded in body prose only, not as wikilinks (per L23 + task instruction). Provisional / sparse-source callout in operation page.

## [2026-05-09] ingest [single agent, regional focus] | DOJ-Bulgaria Zamunda+ArenaBG+Zelka piracy takedown (2026-01-30, BG+US+RO+GR)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 4 country (BG, US, RO, GR), 4 organization (us-doj, usdoj, bulgaria-police, bulgaria-ministry-of-interior, europol-ec3), 3 crime-type (illegal-iptv-ic, organized-crime-ic, money-laundering-ic).
- Key findings:
  - **DOJ-Bulgaria piracy takedown (DOJ OPA PR 26-82, 2026-01-30)**: Three of the largest piracy sites in the European Union — **zamunda.net + arenabg.com + zelka.org** (3 US-registered domains, S.D. Miss. seizure warrants). Bulgarian agencies: National Investigative Service + Ministry of Interior General Directorate Combating Organized Crime (GDCOC/GDBOP) + State Agency for National Security + Prosecutor's Office. US agencies: USAO S.D. Miss. + HSI New Orleans + IPR Center + OPDAT + CCIPS. **In-region attachés**: HSI Athens (GR) + CBP Sofia (BG) + ICHIP Bucharest (RO). Multilateral: **Europol "critical role"**. BTA same-day corroboration: 4 detained, 30 addresses searched, supervised by Sofia City + Sofia District Prosecutor's Offices, coordinated by Acting Prosecutor General Borislav Sarafov. **DOJ ICHIP April 2026 summary**: 3 individuals charged with online piracy + money laundering under **a new Bulgarian piracy-platform-operator statute drafted with OPDAT and CCIPS assistance ("the first law of its kind in Europe")** — important capacity-building IC artifact. **First wiki record of OPDAT/CCIPS-assisted Bulgarian piracy-platform-operator statute drafting** (treaty-level cybercrime-law capacity-building cooperation pattern).
- Process notes: DOJ Akamai + curl_cffi chrome124 (per L21). DIICOT (priority 2) blocked by JS challenge — pivoted. Hong Kong CSTCB Operation SECURE skip-list. usdoj missing-backlink HIGH lint backfilled.

## [2026-05-09] ingest [single agent, regional focus] | Operación KAERB iServer PhaaS takedown (2024-09-24, ES+AR+CO+CL+EC+PE 6-country LatAm-Iberian)
- Sources: 1 raw + 1 source page (es) + 1 operation page (3 new pages)
- Pages updated: 6 country (ES, AR, CO, CL, EC, PE), 4 organization (spain-national-police, spain-guardia-civil, europol-ec3, group-ib), 2 crime-type (online-fraud-ic, cybercrime-infrastructure-ic), 2 cross-link (Tycoon 2FA + LabHost sister PhaaS ops).
- Key findings:
  - **Operación KAERB iServer PhaaS takedown (Argentina Ministerio de Seguridad 2024-09-24)**: KAERB = "Break" reversed. Targeted **iServer** Spanish-language phishing-as-a-service platform active for ≥5 years with 2,000+ subscriber accounts ("desbloqueadores"). Action day 2024-09-10. **6-country LatAm-Iberian IC chain** (rare structural pattern in wiki): Spain + Argentina + Colombia + Chile + Ecuador + Peru. **17 arrests** + 28 home searches + **921 electronic devices seized**. Victims: **483,000 globally** (Chile 77K, Colombia 70K, Ecuador 42K, Peru 41.5K, Spain 30K, Argentina 29K, ~193.5K other). Argentina footprint: 5 arrests, 12 raids (CABA 5, Santa Fe 3, Córdoba 3, Jujuy 1). Apex suspect (iServer administrator) residing in Santa Fe Province, Argentina. Coordination: **EUROPOL + AMERIPOL + PAcCTO 2.0 + Group-IB** public-private partnership. Press-conference principals: Sec. Alejandra Monteoliva (AR), Counsellor Francisco Arenas Morales (ES), Comisario Gustavo Cabada (PFA Ciberpatrullaje), Cmdt. Gen. Claudio Miguel Brilloni (Gendarmería Nacional). **First wiki record of AMERIPOL + PAcCTO Iberian-LatAm coordination + Spanish-language PhaaS takedown** (sister to LabHost + Tycoon 2FA English/EU PhaaS takedowns; cross-linked).
- Process notes: Spanish-language tier-1 source. fiscales.gob.ar DNS unresolvable; pivoted to argentina.gob.ar Ministry of Security as equivalent tier-1. Per L19 secondary-press suspect name (Iván David Cudde) NOT asserted. spain-guardia-civil missing-backlink HIGH lint backfilled.

## [2026-05-09] ingest [single agent, regional focus] | AIT-Taiwan elder romance fraud first MLAA proffer takedown (2025-05-14, US+TW)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 2 country (TW, US), 2 crime-type (online-fraud-ic, money-laundering-ic).
- Key findings:
  - **AIT-Taiwan elder romance fraud takedown (AIT PR-2510, 2025-05-14)**: Taiwan-US joint takedown of Taiwanese-led elder fraud organisation. Hundreds of elderly US victims; >USD 100M laundered; investigation opened May 2023. Cooperating units: Taiwan NPA-CIB + MOJ + TTDPO + Administrative Enforcement Agency + Taichung City Police; HSI Taipei + HSI Los Angeles + HSI Nashville; AIT. **Landmark IC milestone**: **first in-country MLAA proffer interview by a Taiwanese prosecutor in the US since the 2002 Mutual Legal Assistance Agreement (MLAA)** — prosecutor Chang Fu-chun questioned witness Sun in Nashville, April 2025; HSI delegation visited TTDPO March 2025. **Defendants** (TTDPO indictment subset, 3 victims/USD 5.32M): Liao 廖 (36, ringleader, arrested 2025-01-24 Taoyuan, 10-yr recommended), Huang 黃 (39, collections, 5-yr), Hsiao 肖, Sun 孫 (US-based). Charges: Organized Crime Prevention Act + Money Laundering Control Act + Passport Act + Criminal Code. Assets: BTC/USDT + Lexus + Swiss watch + diamond ring + mother's accounts. **First wiki record of Taiwan-US MLAA proffer-interview cooperation pathway**, distinct from formal extradition (Taiwan has no formal extradition treaty with US).
- Process notes: AIT tier-1 primary + Taipei Times + Focus Taiwan as cross-confirmation. Taiwan agencies (CIB, MOJ, TTDPO, AEA, Taichung Police) and HSI have no wiki org pages — referenced in prose only. Provisional callout.

## [2026-05-09] ingest [single agent, regional focus] | FRONTIER+ Cross-border Anti-Scam Collaboration Platform 1st joint operation (2025-06-03, 7 jurisdictions)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 7 country (HK, MO, MY, MV, SG, KR, TH), 5 organization (hong-kong-police, singapore-police, knpa, malaysia-police+royal-malaysia-police, thailand-royal-police), 2 crime-type (online-fraud-ic, voice-phishing-ic), 1 cross-link (existing cross-border-online-cse-operation-spf-2026 sister op).
- Key findings:
  - **FRONTIER+ Cross-border Anti-Scam Collaboration Platform 1st joint op (info.gov.hk 2025-06-03)**: First joint operation of regional anti-scam platform. **Operation period 2025-04-28 – 2025-05-28 (1 month)**. **7 participating jurisdictions** in this op: HK SAR + Macao SAR + Malaysia + Maldives + Singapore + South Korea + Thailand. **2,700+ personnel deployed**; **1,858 arrests** (ages 14–81): HK 337, Macao 9, Malaysia 708, Maldives 0, Singapore 106, South Korea 116, Thailand 582. **9,268 scam cases**; **aggregate loss USD 225M**; **32,607 bank accounts frozen**; ~USD 20M intercepted. Platform launched October 2024; HK release lists 10 members vs SPF CAD 2024 lists 11 (adds Brunei) — preserved as Contradiction. Singapore-side 106 arrests + S$7.7M cross-source confirmed against Singapore CAD 2024 report. **First wiki record of FRONTIER+ regional platform** + standing-platform IC mechanism distinct from one-off operation models.
- Process notes: HKSAR info.gov.hk tier-1 primary + Annex PDF (per-jurisdiction breakdown table). Macao SAR and Maldives Police Service have no wiki org pages (prose-only). Macao country page exists as `macau.md`.

## [2026-05-09] ingest [single agent, regional focus] | Indonesia INP + US FBI global phishing MFA-bypass syndicate (2026-04-23, ID+US)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 2 country (ID, US), 2 organization (indonesia-police, fbi), 3 crime-type (online-fraud-ic, cybercrime-infrastructure-ic, money-laundering-ic).
- Key findings:
  - **Indonesia INP-FBI MFA-bypass phishing syndicate (Polri 2026-04-23)**: 2 suspects arrested 2026-04-22 in Jakarta — **GWL** (developer since 2018) + **FYT** (crypto-laundering); identified as a couple. Indonesian National Police (Polri) Bareskrim ↔ FBI bilateral cooperation. Senior official: Insp. Gen. Nunung Syaifuddin (Deputy Chief of Bareskrim). **Scale**: 17,000 accounts compromised, **34,000 victims globally**, **USD 20M loss**, 9 Indonesian corporates + US victims. Charge: ITE Law (max 15 years). **First wiki record of Indonesia INP/Polri-FBI bilateral on MFA-bypass phishing-as-development-platform** — distinct from W3LL (different actor) and Bali villa raid (immigration vs BEC).
- Process notes: Indonesian-language outlet's English newsroom used as tier-1 primary. `inp.polri.go.id` accessible via curl_cffi chrome124. ITE Law (Indonesian Information & Electronic Transactions Law) referenced; no wiki legal-framework page so prose-only.

## [2026-05-09] ingest [single agent, regional focus] | Swiss OAG + fedpol real-time phishing joint investigation — UK conviction 7yr (2025-07-29, CH+UK)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 2 country (CH, UK), 4 organization (switzerland-fedpol, europol-ec3, eurojust, uk-nca), 3 crime-type (bank-fraud-ic, online-fraud-ic, money-laundering-ic).
- Key findings:
  - **Swiss OAG/fedpol real-time phishing UK conviction (2025-07-29)**: Joint investigation announced by Swiss Office of the Attorney General (Bundesanwaltschaft) + fedpol. **Modus operandi**: real-time phishing kit, fake e-banking pages promoted via Google Ads, SMS-based 2FA bypass, money-mule + crypto-exchange laundering. **Cross-border IC chain**: ~30 cantonal Swiss complainants → ~CHF 2.4M loss → Article 147 SCC proceedings opened 2022-07 → suspect arrested in England 2023-10-26 → OAG transferred prosecution to UK → **UK court sentenced suspect to 7 years on 2025-07-23**. Europol + Eurojust supporting roles per fedpol Report 2024 (provenance flagged for tightening). **First wiki record of OAG-to-UK forum-non-conveniens prosecution transfer pattern** for cyber-enabled bank fraud — useful for `mechanisms/transfer-of-proceedings.md` analysis.
- Process notes: Swiss OAG admin.ch direct URL returned 403 — agent used `bag.admin.ch/en/newnsb/...` mirror + Keystone-SDA/SWI swissinfo.ch + fedpol.report 2024 narrative as 3 concordant tier-1/2 sources. source_count corrected to 3. Defendant name not released by OAG; UK court/case number pending.

## [2026-05-09] ingest [single agent, regional focus] | Korean SPO Seoul Eastern District 합수부 — Clark Philippines voice phishing call-centre arrest+extradition (2026-04-30, KR+PH+INTERPOL)
- Sources: 1 raw + 1 source page (ko, with embedded PDF) + 1 operation page (3 new pages)
- Pages updated: 2 country (KR, PH), 5 organization (supreme-prosecutors-office-korea, ministry-of-justice-korea, philippine-national-police, interpol, spo-international-cooperation), 3 crime-type (voice-phishing-ic, online-fraud-ic, organized-crime-ic), 1 mechanism (extradition), 1 cross-link (existing korea-cambodia-philippines-73-extradition-2026 sister case).
- Key findings:
  - **SPO Seoul Eastern Clark Philippines voice phishing (서울동부지방검찰청 합수부 2026-04-30)**: 4 defendants (incl. A=37yo male call-centre manager) indicted in custody on 2026-04-28 for **통신사기피해환급에관한특별법위반 + 사기 (KCC §347)**. Clark, PH call-centre operating 2025-06–07; indicted-offence fraud volume ~₩130M. **MO**: two-stage 'review-task' (리뷰달기) lure scam — 1st stage hotel-review mission with small payouts → 2nd stage 'purchase-authentication team mission' with debt-coercion script. **3-jurisdiction IC chain**: SPO Organised Crime Division-deployed prosecutorial investigator (대검찰청 조직범죄과 파견 검찰수사관) → Philippine Bureau of Immigration FSU (수배자 추적대) → INTERPOL Red Notice + Korean passport invalidation → MOJ International Criminal Affairs Division (법무부 국제형사과) + Korean Embassy Manila police attaché-Consul (총경) → forced repatriation. Operational timeline: 2025-07-24 informant → 2025-07-26 raid + Bicutan immigration detention → 2025-08–09 Red Notice + passport invalidation → 2026-02–04 four-party repatriation negotiation → 2026-03–04 indictment in custody → 2026-04-30 announcement. Evidence: 5 PCs + phones + tablets seized + transferred. **Korean structural attestation**: 합수부 = four-agency fusion (검찰/경찰/관세청/국세청), launched 2022-07-29 as 합동수사단, embedded as permanent 부 on 2026-01-06; cumulative outputs to 2026-03-31: 1,206 booked, 481 in custody. **First wiki record of operational immigration-detention + Red Notice + passport invalidation cooperation pathway** (no formal Korea-Philippines extradition treaty article cited — flagged as Open Question).
- Process notes: Korean-language tier-1 source preserved per CLAUDE.md rule 11. Original SPO press release HTML + signed PDF both fetched via curl_cffi chrome120. Backfill: spo-international-cooperation org backlink + source `created` date fixed.

## [2026-05-09] ingest [single agent, regional focus] | Operation FEVER — Polish CBZC EU Presidency CSAM crackdown (2025-04-09, 12+ countries)
- Sources: 1 raw + 1 source page (pl) + 1 operation page (3 new pages)
- Pages updated: 14 country (PL, DK, EE, DE, EL, HU, IE, LV, RO, ES, SE, BG, UK, US), 5 organization (poland-police, europol-ec3, uk-nca, fbi, germany-bka, ncmec), 1 crime-type (csam-ic), 1 cross-link (operation-stream-kidflix sub-component).
- Key findings:
  - **Operation FEVER (CBZC+KGP umbrella, 2025-04-09)**: Largest European-led CSAM crackdown of Poland's H1 2025 EU Council Presidency. **International total**: 166 detentions; **Poland subset**: 98 (ages 22-78); CSAM-distribution arrests 111. Polish enforcement footprint: 159 searches, ~600 officers, 1,700+ devices, 520,000+ CSAM files, 48 pre-trial detentions, 3 unauthorised firearms. **12 EU + 2 non-EU participants**: Poland (lead), DK, EE, DE, EL, HU, IE, LV, RO, ES, SE, BG + UK NCA + US FBI/HSI/NCMEC. Coordination: Europol J-CAT. Sub-operations: **Kidflix** (CBZC + German police; server seized 2025-03-11 in DE/NL; 12 Polish targets — sister to existing [[operation-stream-kidflix]] page) + CBZC-FBI dark web forum track. Earlier referenced CBZC ops 2022-2024: ANASTAZJA, BARBOSSA, CARLOS, DAKOTA, ENOLA GAY (cumulative 280+ charged, 2M+ files). **First wiki record of CBZC EU-Presidency-framed umbrella operation**.
- Process notes: Polish-language tier-1 source preserved per CLAUDE.md rule 11. Backfill: germany-bka + ncmec missing-backlink HIGH lints fixed. CBZC org page does not exist (`poland-police.md` used as canonical lead-agency page). HSI no wiki page; referenced in prose. Operation FEVER is umbrella for Kidflix already in wiki; cross-linked.

## [2026-05-09] ingest [single agent, regional focus] | NL Politie + US FBI Veriftools fake-ID marketplace follow-up arrests (2026-04-09, NL+US)
- Sources: 1 raw + 1 source page (nl) + 1 operation page (3 new pages)
- Pages updated: 2 country (NL, US), 3 organization (netherlands-politie, netherlands-om, fbi), 3 crime-type (identity-theft, online-fraud-ic, cybercrime-infrastructure-ic), 2 mechanism (informal-cooperation, domain-seizure).
- Key findings:
  - **Veriftools fake-ID marketplace follow-up (Politie 2026-04-09)**: Follow-up to **2025-08-27 joint Politie-FBI server seizure** of Veriftools fake-ID marketplace. 7-8 Apr 2026 first arrest wave: 8 arrests (ages 20-34) + 9 summonses (incl. 2 minors). Server data turned out to be a "goldmine" (Dutch: "goudmijn"): 636,847 customer accounts; 915,655 fake-ID images; 5,169 fake NL documents; 236,002 fake US documents (USD 1,468,836.98 turnover); EUR 3M+ revenue last year. Rotterdam Team Cybercrime + AVIM + Netherlands OM led; FBI bilateral cooperation channel. **First wiki record of Veriftools** + first wiki record of post-seizure-data-mining-driven Dutch arrest wave. Body source-mining pattern (server seizure → forensic analysis → individual customer/operator arrests months later) is a documented IC pattern useful for `cybercrime-infrastructure-ic` analysis.
- Process notes: Single-agent regional-focus dispatch. Dutch-language tier-1 source preserved per CLAUDE.md rule 11. US-side DOJ/FBI primary press release not in this ingest pass — secondary outlets (helpnetsecurity, hackernews, register, securityaffairs) report USD 6.4M figure but per L19 not asserted. `informal-cooperation` mechanism asserted (no MLAT cited in primary).

## [2026-05-09] ingest [single agent, regional focus] | AFP-FGR Mexico Yucatán+Nayarit CSAM bilateral investigation (2026-05-08, MX+AU)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 2 country (MX, AU), 1 organization (australia-afp), 2 crime-type (csam-ic, dark-web-ic), 1 mechanism (informal-cooperation), 4 cross-link (Mad Hatter Italy + live-distant CSAM Italy + Eclipse CSAM Americas + Cyber Guardian).
- Key findings:
  - **AFP-FGR Mexico CSAM bilateral (AFP/QPS joint release with FGR/SSPC, 2026-05-08)**: Two-case bilateral CSAM investigation. **Yucatán case**: 38yo male arrested 2026-04-07 Kanasín, charged trata de personas agravada (aggravated human trafficking); decade-long grooming via football training; ordered to stand trial. **Nayarit case**: 31yo male arrested March 2026 Tuxpan; alleged distribution via instant messaging + dark web; 1 child rescued; phones/computers/hard drives/USB devices/clothing/bedding seized. Cooperation channel: **QPS Task Force Argos (Brisbane) → AFP Liaison Officers in Mexico City → FGR-FEMDO + SSPC**. Long-standing informal bilateral; no MLAT cited. **First wiki record of MX↔AU CSAM bilateral cooperation pattern** + first wiki appearance of Mexican federal entities (FGR / FEMDO / SSPC / Secretaría de Marina) — none have wiki org pages yet (referenced in prose only).
- Process notes: Single-agent regional-focus dispatch (JP/HK/MX/SG/IT/ES priority). Agent skipped Japan NPA (Cyber Guardian already in), Hong Kong CSTCB (Operation SECURE already in), Spain (Op Talent already in; Anonymous Fénix DANA pure-domestic), Indonesia Polri LCS Cambodia (weaker IC depth — Red Notice channel only). FGR direct URL HTTP 500 — used AFP joint release as primary tier-1 anchor (both jurisdictions co-signed). 6 Spanish-language secondary outlets supplemented (El Imparcial, Por Esto, Infobae, Informador, La Voz de Michoacán, SDP Noticias).

## [2026-05-09] ingest [single agent, regional focus] | Singapore Police Force 7-country cross-border online CSE operation (2026-04-28, SG+HK+JP+KR+MY+TH+BN)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 7 country (SG, HK, JP, KR, MY, TH, BN), 6 organization (singapore-police, hong-kong-police, japan-npa, knpa, knpa-cyber-bureau, malaysia-police, royal-malaysia-police, thailand-royal-police, thai-royal-police), 1 crime-type (csam-ic), 1 cross-link (operation-cyber-guardian related operation).
- Key findings:
  - **SPF cross-border online CSE op (Singapore Police Force 2026-04-28)**: 7-jurisdiction multilateral operation (SG+HK+JP+KR+MY+TH+BN). Operation period 23 Mar 2026 – 17 Apr 2026. Aggregate: **326 arrests + 119 under investigation = 445 subjects** (430 men + 15 women, ages 12-72); **382 locations raided**; seizures 116 computers + 340 phones + 25 tablets + 140 storage devices + 16 routers. Singapore subset: 11 men aged 22-44 arrested + 16 under investigation; lead unit Specialised Crime Branch CID; Deputy Commissioner Zhang Weihan quoted. Crime focus: CSAM production/distribution/possession, sexual communication with minors, commercial sexual exploitation, intimate-image abuse, obscene material distribution. **Distinct from existing 2025 6-country [[operation-cyber-guardian]] (Asia-led CSAM crackdown) — Brunei is the new 7th participant**, marking expansion of the Asia-Pacific CSE-IC corridor.
- Process notes: Single-agent regional-focus dispatch (AFP/JP/SG/IT/Eurojust priority). AFP 2024-2026 candidates all in wiki — pivoted to Singapore SPF. Royal Brunei Police Force has no wiki org page; referenced in prose only. Backfilled wiki org-page duplicates (knpa-cyber-bureau, royal-malaysia-police, thai-royal-police variants both backlinked alongside canonical knpa, malaysia-police, thailand-royal-police).

## [2026-05-09] ingest [single agent, regional focus] | Italy Polizia Postale + HSI + Europol live-distant child abuse operation (2026-02-02, IT+US)
- Sources: 1 raw + 1 source page (it) + 1 operation page (3 new pages)
- Pages updated: 2 country (IT, US), 2 organization (italy-polizia-postale, europol-ec3), 1 crime-type (csam-ic), 1 cross-link (Mad Hatter related operation).
- Key findings:
  - **Italy Polizia Postale + HSI + Europol live-distant CSAM (Polizia di Stato 2026-02-02, modified 2026-02-03)**: Lead C.N.C.P.O. (Centro Nazionale per il Contrasto alla Pedopornografia Online) within Polizia Postale e per la sicurezza cibernetica; coordinated by Procura di Milano. **International partners explicitly named**: U.S. Homeland Security Investigations (HSI) and Europol — described as "determinante" (decisive). 2 arrests (Trento + Reggio Calabria) + 4 reported at liberty (Roma + Latina + Brescia + Milano, ages 47–57). Modus operandi: "buyers" → "traffickers/vendors" via Asian adult-content platforms → private rooms → real-time webcam abuse → "tips" via mainstream money-business services. **Sister operation to existing Mad Hatter** (Apr 2026) — both feature Italy Polizia Postale CNCPO + US LE bilateral cooperation against transnational online CSAM; cross-linked.
- Process notes: Italian-language tier-1 source preserved per CLAUDE.md rule 11. Secondary press calls this "Operazione Light Bridge" but official Polizia di Stato release does NOT use that name — treated as unverified secondary alias per L19. WebFetch blocked on poliziadistato.it (HTTP 403); recovered via curl_cffi chrome124 per L20. HSI not in wiki as standalone organization page — referenced in prose only, no wikilink.

## [2026-05-09] ingest [single agent, regional focus] | Eurojust Romania-Moldova phishing/laundering JIT action day (2025-06-12, RO+MD)
- Sources: 1 raw + 1 source page (en) + 1 operation page (3 new pages)
- Pages updated: 4 country (RO, MD, UA, IT), 2 organization (eurojust, romania-diicot), 2 mechanism (joint-investigation-team, european-investigation-order), 2 crime-type (online-fraud-ic, money-laundering-ic).
- Key findings:
  - **Eurojust Romania-Moldova phishing/laundering JIT (2025-06-12)**: Action day on JIT set up March 2025 (Eurojust-financed); investigation initiated by Moldova PCCOCS in November 2022. Lead: Romania DIICOT (Galați Regional Structure) + Moldova PCCOCS. **44 search locations** across both countries. OCG active since at least 2013, suspect nationalities Romanian + Moldovan + Ukrainian + Italian; **30 victims identified across the EU; aggregate EUR 20M loss**. Call centres located in Moldova. EIOs paired with JIT; **Moldova one of twelve Liaison Prosecutor countries at Eurojust** — significant for non-EU LE cooperation pattern. Laundering chain: false-Romanian-ID bank accounts → financial platforms → cryptocurrency wallets. **First wiki record of Romania-Moldova JIT pairing** — important RO-MD bilateral cooperation pattern not previously captured (existing Moldova-anchored cases: GoZNyM, xDedic, Carbanak, DarkMarket are all multi-country US-led).
- Process notes: Single-agent regional-focus dispatch (JP/AFP/IT/ES/Eurojust priority). Eurojust English-language tier-1 source. Agent skipped Japan-NPA-India CBI tech-support scam candidate (already in wiki as operation-chakra-v + india-cbi-noida-tech-support-scam-takedown-2025) and AFP Pompilid (Five Eyes already-saturated CSAM channel) in favor of structurally underrepresented Moldova-anchored JIT.

## [2026-05-09] ingest [single agent, regional focus] | RCMP Canada-FBI Twitter/NFT theft Redman case (CA→PT→US extradition, sentencing 2025-09-10)
- Sources: 1 raw (RCMP CNW mirror + DOJ EDVA cross-reference) + 1 source page (en) + 1 case page (3 new pages)
- Pages updated: 3 country (CA, US, PT), 4 organization (canada-rcmp, us-doj, fbi, office-of-international-affairs), 3 crime-type (hacking-ic, online-fraud-ic, identity-theft), 1 mechanism (extradition).
- Key findings:
  - **US v. Redman (Twitter Partner Support Portal abuse / NFT theft, EDVA No. 1:25-cr-129)**: Cameron Albert Redman, 22, Mississauga, Ontario (Canadian national). Court: U.S. District Court for the Eastern District of Virginia, Judge Leonie M. Brinkema. Sentencing: 2025-07-29, 12 months' imprisonment + restitution. Conduct (May 2022): unauthorized access to Twitter Partner Support Portal; resold via online forum; co-conspirators stole NFTs/crypto from 200+ victims; ~USD 794,000 profit (DOJ figure for conspirator profit; RCMP "several million dollars" for broader victim loss preserved as separate metric). **3-jurisdiction IC chain**: Canada (RCMP Central Region CIT investigation + FBI info-sharing) → Portugal (arrest of Redman) → United States (extradition March 2025 via DOJ Office of International Affairs, prosecution by EDVA / FBI Washington Field Office). Canadian investigation formally closed once US prosecution succeeded. **First wiki record of CA→PT→US 3-jurisdiction extradition pattern with platform-abuse origin**.
- Process notes: Single-agent regional-focus dispatch (JP/AFP/RCMP/IT/ES priority). RCMP rcmp.ca returned HTTP 500 — body recovered from official Newswire/CNW Group syndication mirror. DOJ Akamai bm-verify bypass per L21 (6s sleep + meta-refresh follow). **Pre-existing wiki defect flagged but not fixed**: existing `wiki/cases/canadian-cybercriminal-sentenced-to-a-year-in-prison-for-nft-theft-scheme.md` lists defendant as "Conor Brian Fitzpatrick" (BreachForums founder, different defendant) — name appears only in DOJ EDVA sidebar. Flagged for future cleanup audit.

## [2026-05-09] ingest [single agent, regional focus] | Germany BKA — "Crimenetwork" relaunched darknet marketplace takedown + Mallorca arrest (2026-05-08, DE+ES+MD)
- Sources: 1 raw + 1 source page (de) + 1 operation page (3 new pages)
- Pages updated: 4 organization (germany-bka, zit-frankfurt, spain-national-police, eurojust), 3 country (DE, ES, MD), 5 mechanism (european-arrest-warrant, eurojust-coordination-meeting, domain-seizure, cryptocurrency-seizure, marketplace-admin-liability), 5 crime-type (dark-web-ic, cybercrime-forum-ic, drug-trafficking, online-fraud-ic, counterfeit-goods).
- Key findings:
  - **Crimenetwork relaunch takedown (BKA 2026-05-08, action day 2026-05-06)**: Targeted relaunched German-language darknet marketplace (Crimenetwork) — 22,000+ users, 100+ vendors, EUR 3.6M+ turnover. **3-country IC chain**: Germany BKA + ZIT Frankfurt + GenStA Karlsruhe + PP Offenburg + PP Reutlingen + Spain Policía Nacional special unit (Mallorca arrest) + Moldova Centrul pentru Combaterea Crimelor Cibernetice. Eurojust coordination. **1 arrest** of 35-year-old German national on Mallorca on European Arrest Warrant (EAW). Platform takedown; **EUR 194,000 in assets provisionally seized**; extensive user/transaction data captured; seizure banner + bustedagaincrime.network notification site. Charges: § 127 StGB (Betreiben krimineller Handelsplattformen im Internet — operating criminal trading platforms online — landmark recent provision), §§ 29a/30a BtMG (Betäubungsmittelgesetz — narcotics law), parallel commercial-fraud (gewerbsmäßiger Betrug) Karlsruhe proceeding. **First wiki record of post-Sept-2024 § 127 StGB application** (German criminal-platform-operator-liability statute, parallel to Italian Mad Hatter / US RICO infrastructure approach). Re-launch dimension: prior takedown was December 2024 of original Crimenetwork; this is the relaunched successor.
- Process notes: Single-agent regional-focus dispatch (JP/BKA/AFP/SG/IT/ES priority). German-language tier-1 source preserved per CLAUDE.md rule 11. Moldova counterpart agency (Centrul pentru Combaterea Crimelor Cibernetice) referenced in prose only — no wiki page exists, stub creation deferred. `germany-bka.md` (canonical, 195 lines) used over legacy `german-bka.md` (68 lines) — duplication noted for future canonicalization audit.

## [2026-05-09] ingest [single agent, regional focus] | Brazil Polícia Federal Operação Dark Bet — BET-sector Brazil→Nigeria trafficking + forced cybercrime labour (2025-12-16, BR+NG)
- Sources: 1 raw + 1 source page (pt) + 1 operation page (3 new pages); operation page references 2 PR mirrors (PF + MJSP).
- Pages updated: 2 country (BR, NG), 1 organization (brazil-ministry-of-justice-public-security), 2 crime-type (organized-crime-ic, online-fraud-ic), 1 mechanism (informal-cooperation).
- Key findings:
  - **Operação Dark Bet (Polícia Federal Brazil 2025-12-16)**: PF dismantled Brazilian organised criminal group running 2 BET-sector online sports-betting platforms used as **recruitment fronts to traffic Brazilian nationals to Nigeria for forced cybercrime labour** under armed surveillance. **Reverse-discovery cooperation pattern**: trigger event = arrest of 109 persons in Nigeria including 5 Brazilians on cybercrime charges → PF home-country trafficking origin investigation. Charges (per PF release, no Penal Code articles cited): tráfico internacional de pessoas para fins de exploração laboral + redução à condição análoga à de escravo (Art. 149 typical) + organização criminosa + crimes cibernéticos. Results: 11 search-and-seizure warrants across 5 Brazilian states (CE/MA/PR/SC/SP), 4 temporary arrests in Brazil, asset blocks > R$ 446M, 2 BET platforms taken offline. **First wiki record of Brazil↔Nigeria reverse-discovery IC pattern + forced-labour-cybercrime + BET-sector-as-recruitment-front modality** — distinct IC pattern from Cryptoscam (SG-domestic complaint → BR action) and Magna Fraus (BR-domestic-led PIX bank fraud). Marina Bernardes (MJSP-Coordenação-Geral de Cooperação Internacional) public statement (MJSP mirror).
- Process notes: Single-agent regional-focus dispatch (JP/BKA/AFP/SG/Italian priority — agent pivoted to PF Brazil after RCMP candidates blocked by HTTP 500). Brazilian Portuguese tier-1 source preserved per CLAUDE.md rule 11. `informal-cooperation` mechanism asserted (PF release names no Nigerian counterpart agency — flagged via `[!warning] Legal status check needed` per L17/L19). EFCC participation NOT asserted despite contextual indication (Dec 2024 Lagos cybercrime crackdown). source_count corrected to 2 (PF + MJSP mirror).

## [2026-05-09] ingest [single agent, regional focus] | Italy Polizia Postale Operazione Mad Hatter — CSAM + FBI cooperation (2026-04-28, IT+US)
- Sources: 1 raw + 1 source page (it) + 1 operation page (3 new pages)
- Pages updated: 2 country (IT, US), 2 organization (italy-polizia-postale, fbi), 1 crime-type (csam-ic), 1 mechanism (informal-cooperation).
- Key findings:
  - **Operazione Mad Hatter (Polizia di Stato Questura di Milano 2026-04-28)**: Long-duration online undercover infiltration operation (started 2024) by C.N.C.P.O. (Centro Nazionale per il Contrasto alla Pedopornografia Online), within Polizia Postale e per la sicurezza cibernetica, coordinated by Procura della Repubblica di Roma. ~50 specialised C.O.S.C./S.O.S.C. operators across Bari, Cagliari, Firenze, Milano, Roma, Torino, Venezia. **Foreign cooperation**: US FBI provided information enabling identification of subjects of interest. 3 in-flagrante arrests (men aged 70/63/28 in provinces of Belluno, Mantova, Como); 6 reported at liberty in 6 other Italian provinces; 9 simultaneous search warrants in 9 Italian cities; thousands of CSAM files seized; **AI-generated CSAM identified** — increasingly important enforcement signal. **First wiki record of Italy Polizia Postale + FBI bilateral cooperation against transnational CSAM**.
- Process notes: Italian-language tier-1 source preserved per CLAUDE.md rule 11. `informal-cooperation` mechanism asserted (no specific MLAT or Budapest Convention citation in primary source — flagged via `[!warning] Legal status check needed` callout per L17). Provisional single-source page (`source_count=1`) below preferred 5-source threshold; `[!info] Provisional` callout placed.

## [2026-05-09] ingest [single agent, regional focus] | KNPA Breaking Chains (브레이킹 체인스) 2nd international operation meeting (2026-02-05, KR+US+CN+JP+KH+TH+VN)
- Sources: 1 raw + 1 source page (ko, full-text-via-secondary 뉴데일리/이데일리) + 1 operation page (3 new pages)
- Pages updated: 7 country (KR, KH, TH, VN, CN, JP, US), 6 organization (knpa, knpa-cyber-bureau, interpol, aseanapol, afripol, unodc), 3 crime-type (online-fraud-ic, voice-phishing-ic, organized-crime-ic), 4 mechanism (informal-cooperation, extradition, interpol-i24-7, interpol-asean-desk), 3 legal-framework (Korea-Cambodia JTF MOU 2025, Korea-China anti-scam MOU 2025, Korea-Philippines Police MOU 2026), 5 cross-links to existing related operations.
- Key findings:
  - **KNPA Breaking Chains 제2차 국제공조 회의 (Korea.kr 2026-02-05)**: 2nd international operation meeting hosted by KNPA in Seoul against transnational scam crime (보이스피싱 + romance fraud + scam compounds + human trafficking) operating from KH, TH, VN, CN. 22-country roster (only 6 verbatim-named in primary source: KR, US, CN, JP, KH, TH, VN); 5 international organisations (INTERPOL, ASEANAPOL, AFRIPOL, IOM, UNODC). Phase-1 outcomes (cumulative through 2026-02-05): 26 cases / 75 leads exchanged at 1st meeting (2025-11); KH 15 arrests (₩2.589B / 27 victims, 2025-12-04), TH 13 arrests (~₩100M); VN/CN-track: 31 arrests + 15 KR repatriations + 1 KH-TH trafficker leader arrest. 2nd meeting agenda: 13 countries / 45 cases / 80 leads. **First wiki record of explicit policy-level recognition of balloon-effect (풍선효과)** — strengthening cooperation in one corridor pushes scam orgs to weaker-enforcement jurisdictions; provides primary-source support for `wiki/challenges/` frame. Korean officials named: 박성주 (KNPA National Investigation Headquarters Commissioner), 이재영 (KNPA International Cooperation Officer).
- Process notes: Single-agent regional-focus dispatch (KR/JP/VN/IT priority). Korea.kr Synap iframe variant of L11 — body retrieved via tier-1-secondary-republication (뉴데일리 verbatim 전재 + 이데일리 Phase-1 verbatim outcomes). Korean source language preserved per CLAUDE.md multi-language rule (operation page Korean Perspective section substantive). Stale category-style "challenges" wikilinks (pointing at the directory, not a page) were converted to plain text during cleanup.

## [2026-05-09] ingest [single agent, regional focus] | Brazil Polícia Federal Operação Magna Fraus Phase 2 PIX bank fraud (2025-10-30, BR+ES+AR+PT)
- Sources: 1 raw + 1 source page (pt) + 1 operation page (3 new pages)
- Pages updated: 4 country (BR, ES, AR, PT), 3 organization (interpol, spain-national-police, brazil-ministry-of-justice-public-security), 3 crime-type (bank-fraud-ic, money-laundering-ic, online-fraud-ic), 2 mechanism (interpol-i24-7, informal-cooperation), 1 cross-link (spf-fpb-operation-cryptoscam-2025) + Reference rows.
- Key findings:
  - **Operação Magna Fraus Phase 2 (Polícia Federal Brazil 2025-10-30)**: 4-jurisdiction Iberian-LatAm action — Brazil PF + Cyber GAECO MP-SP + Spain Brigada Central de Fraudes Informáticos + Argentina (INTERPOL NCB action-day partner) + Portugal (NCB cooperation, no arrests). INTERPOL Command and Coordination Centre coordinated. Target: organized criminal group draining accounts that BR banks/payment institutions use to manage customer **PIX (instant-payment) transfers**. Loss: **R$ 813M (~USD 145M)**. 26 arrest warrants → 21 arrests executed (13 BR + 6 ES + 2 AR), 42 search-and-seizure warrants, asset-blocking up to R$ 640M, 15 vehicles, 25 properties, R$ 1M+ crypto, luxury goods. Charges per Lei 12.850/2013 (organização criminosa) + art. 154-A Lei 12.737/2012 (invasão de dispositivo informático) + art. 155 §4-B (furto mediante fraude eletrônica) + Lei 9.613/1998 (lavagem de dinheiro). **First wiki record of Brazil-led INTERPOL-mediated 4-NCB action targeting Brazilian PIX-rail bank-fraud ecosystem** — important pattern for LatAm-Iberian cooperation analysis. Original-language Portuguese source preserved per CLAUDE.md multi-language rule.
- Process notes: Single-agent regional-focus dispatch (ROK/JP/BR/SG priority). Brazil gov.br endpoint accessible via `tools/stealth_fetch.py` urllib tier. L8 cp949 fix applied. Page tagged `[!info] Provisional / Single-Source` (source_count=1 below preferred 5-source threshold; novel IC pattern + tier-1 government primary justifies provisional publication). Portugal verification gap flagged (NCB listed as cooperation partner but no arrests reported).

## [2026-05-09] ingest [single agent] | Europol Spain EUR 460M crypto investment fraud ring takedown (2025-06-30, ES+EE+FR+US)
- Sources: 1 raw + 1 source page + 1 operation page (3 new pages)
- Pages updated: 4 country (ES, EE, FR, US), 4 organization (europol-ec3, spain-guardia-civil, france-gendarmerie-nationale, us-dhs), 2 crime-type (online-fraud-ic, money-laundering-ic) + Reference rows.
- Key findings:
  - **Crypto investment fraud Spain EUR 460M (Europol 2025-06-30)**: 4-jurisdiction action (Spain Guardia Civil + Estonia Police and Border Guard Board + France New Caledonia National Gendarmerie + USA HSI) coordinated by Europol EC3. Action day 2025-06-25. 5 arrests (3 in Canary Islands, 2 in Madrid), 5 searches, EUR 460M laundered, 5,000+ victims worldwide. Hong Kong corporate-and-banking layer named as alleged laundering pivot but NOT participating action-day jurisdiction (per L19, kept out of `participating_countries`).
- Process notes: Single-agent broader-discovery dispatch. Europol React SPA → curl_cffi chrome124 + SERVER_DATA inline-JSON parse (per L20). Cache-aware Windows cp949 fix per L8.
- Wiki coverage milestone: agent reported very dense coverage of 2024-2026 tier-1 IC actions; ~12 prior candidates (Operation PowerOFF / Tycoon 2FA / Operation Talent / Operation Atlantic / Cracked-Nulled / LeakBase / SocksEscort / SIMCARTEL / Albanian call centres / Versus Project / Rydox / Cryptomixer / NCA-Nigeria Meta / India CBI Noida / Operation Sentinel / Red Card / HAECHI VI / Synergia III / Vachon-Desjardins / Endgame / Volkov / Medjedovic / Ukraine ransomware) all already in wiki — saturation signal for future iterations.

## [2026-05-09] ingest [single agent] | Europol Tycoon 2FA phishing-as-a-service platform takedown (2026-03-04)
- Sources: 1 raw + 1 source page + 1 operation page (3 new pages)
- Pages updated: 6 country (LV, LT, PT, PL, ES, UK), 11 organization (europol-ec3, latvia-state-police, lithuania-police, portugal-policia-judiciaria, poland-police, spain-national-police, spain-guardia-civil, uk-nca, microsoft, trend-micro, shadowserver), 3 crime-type (cybercrime-infrastructure-ic, online-fraud-ic, hacking-ic) + 5 cross-links to related operations (LabHost, Lumma Stealer, W3LL, LeakBase, XSS.is forum) + body Reference rows.
- Key findings:
  - **Tycoon 2FA PhaaS Takedown (Europol 2026-03-04)**: 6-country EU action coordinated by Europol EC3 against Tycoon 2FA — adversary-in-the-middle (AitM) phishing-as-a-service platform active since at least August 2023. 330 domains taken down; ~30 months of operation disrupted; tens of millions of phishing emails per month at peak; ~100,000 organisations globally affected; ~62% of mid-2025 Microsoft-blocked phishing share. **First wiki record of Europol Cyber Intelligence Extension Programme (CIEP)** as IC mechanism class — public-private intelligence-sharing platform. Private partners credited: Cloudflare, Coinbase, Intel471, Microsoft (technical lead), Proofpoint, Shadowserver, SpyCloud, Trend Micro (initial intelligence). No arrests / named individual defendants in primary release — infrastructure-disruption focus.
- Process notes: Single-agent broader-discovery dispatch. Europol newsroom is React SPA — agent recovered body via curl_cffi chrome124 + inline `window.SERVER_DATA={...}` JSON parse (per L20). Cross-linked to existing related PhaaS / forum / infostealer takedowns.

## [2026-05-09] ingest [single agent] | Treasury OFAC Doppelganger companion sanctions JY-2559 (2024-09-04)
- Sources: 1 raw + 1 source page + 1 operation page (3 new pages)
- Pages updated: 2 country (US, RU), 3 organization (us-treasury, us-doj, fbi), 2 crime-type (cybercrime-infrastructure-ic, money-laundering-ic) + body Reference rows + cross-link to existing DOJ Doppelganger operation.
- Key findings:
  - **Treasury OFAC Doppelganger companion (JY-2559, 2024-09-04)**: Same-day companion to existing [[us-doj-doppelganger-russian-influence-op-domain-seizures-2024]] DOJ action. Designated 2 entities (ANO Dialog + ANO Dialog Regions) and 10 individuals: 6 RT executives (Margarita Simonyan, Elizaveta Brodskaia, Anton Anisimov, Andrey Kiyashko, Konstantin Kalashnikov, Elena Afanasyeva — last two also indicted by SDNY in DOJ companion), 3 RaHDit operatives (Garashchenko, Yermoshkina, Nezhentsev), 1 ANO Dialog leader (Vladimir Tabak). Authority: EO 14024 (IEEPA Russia harmful foreign activities). EU previously+separately sanctioned ANO Dialog for War on Fakes — referenced as prior action, not coordinated package. URL slug correction: prompt JY-2625 wrong; correct release JY-2559 (per L1).
- Process notes: Single-agent ingest. Treasury URL needed L11 Cloudflare bypass via curl_cffi chrome120 (WebFetch timed out twice). Page tagged `[!warning] IC scope flag` (US unilateral, no FVEY co-designation; EU prior independent action only).

## [2026-05-09] ingest [parallel batch x2] | Treasury OFAC Integrity Technology Group / Flax Typhoon sanctions (2025-01-03) + Treasury OFAC Yin Kecheng / Salt Typhoon sanctions (2025-01-17)
- Sources: 2 raw + 2 source pages + 2 operation pages (6 new pages)
- Pages updated: 2 country (US, CN), 2 organization (us-treasury, fbi), 2 crime-type (hacking-ic, cybercrime-infrastructure-ic) + body Reference rows + 1 cross-link to existing DOJ Raptor Train operation.
- Key findings:
  - **Treasury OFAC Integrity Technology Group (JY-2769, 2025-01-03)**: First Treasury OFAC designation of a publicly-traded PRC contractor entity for state-sponsored cyber activity (Flax Typhoon). Beijing-based, public brand "KRLab". Acting Under Secretary for TFI Bradley T. Smith quoted. Legal basis: EO 13694 amended by EO 13757. **Companion to existing [[us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024]] operation** (DOJ disruption ~3.5 months earlier; cross-linked). IC-scope flagged (US unilateral; no allies named in primary source).
  - **Treasury OFAC Yin Kecheng (JY-2792, 2025-01-17)**: Designation of Yin Kecheng (Shanghai-based, MSS-affiliated cyber actor for over a decade) + Sichuan Juxinhe Network Technology Co., LTD (Sichuan-based) for Salt Typhoon malicious cyber activity (US telecom/ISP intrusion). Legal basis: EO 13694 amended by new EO on Strengthening and Promoting Innovation in Nation's Cybersecurity (signed January 2025). Press release describes victims only generically as "multiple major U.S. telecommunication and internet service provider companies" — Verizon/AT&T/T-Mobile/Lumen widely reported in tier-2 coverage but NOT asserted in operation page per L19. URL slug correction: prompt JY-2782 was off-by-one; correct release JY-2792.
- Process notes: Iter 64 used parallel multi-agent harness (2 of 2 successful). Both Treasury URLs needed L11 Cloudflare bypass via curl_cffi chrome120 (Agent A's primary URL timed out via WebFetch — reconstructed from globalsecurity.org + Alston & Bird + Industrial Cyber + Cybersecurity Dive secondary mirrors with documented `[!note] Fetch caveat`). Both pages tagged `[!warning] IC scope flag` per Doppelganger pattern (US unilateral, no FVEY allies named in primary source).

## [2026-05-09] ingest [parallel batch x2] | DOJ DPRK IT worker disruption Knoot Nashville (2024-08-08) + Politie Bohemia/Cannabia darknet marketplace takedown (2024-10-08)
- Sources: 2 raw + 2 source pages + 2 operation pages (6 new pages)
- Pages updated: 6 country (US, KP, CN, RU, KR, NL, IE, UK), 6 organization (us-doj, fbi, fbi-cyber-division, netherlands-politie, netherlands-om, ireland-garda, uk-nca), 5 crime-type (online-fraud-ic, identity-theft, money-laundering-ic, dark-web-ic, drug-trafficking, cybercrime-infrastructure-ic) + body Reference rows + 2 cross-links to existing related operations.
- Key findings:
  - **DOJ DPRK IT worker disruption (2024-08-08, USAO-MDTN)**: Press release named ONLY Matthew Isaac Knoot (38, US national, Nashville laptop farm operator) — Chapman/Didenko referenced via May 2024 hyperlinks as separate prior actions. Charges: conspiracy to damage protected computers + conspiracy to launder + conspiracy wire fraud + intentional damage + aggravated identity theft + conspiracy unlawful employment of aliens. Knoot cell paid >USD 250K to overseas DPRK IT workers (Jul 2022 – Aug 2023); >USD 500K victim remediation costs. **DPRK RevGen: Domestic Enabler Initiative** (launched March 2024 by NSD + FBI Cyber + FBI Counterintelligence) is the documented cooperation framework. ROK October 2023 joint guidance referenced. Related to existing [[us-v-knoot-prince-dprk-laptop-farms-2026]] sentencing case (cross-linked).
  - **Bohemia / Cannabia darknet market takedown (Politie 2024-10-08)**: 11-country international action; 2 administrators arrested (20-year-old British national at Schiphol Airport 2024-06-27; 23-year-old Irish national in Ireland August 2024); 3+ servers (database + crypto + web) seized; >EUR 8M crypto seized. Marketplace metrics: ~82,000 daily ads, ~67,000 monthly txns, EUR 12M peak monthly turnover (Sep 2023), ~EUR 5M admin profits, ≥14,000 NL-origin txns / ~EUR 1.7M. Tier-1 IC chain: NL Politie THTC + OM + Ireland Garda Síochána + UK NCA + US LE (DOJ-level not specified in primary source). Operation date `2024-06-27` (Schiphol arrest) corrected to **2024-10-08** (publication date) per L1.
- Process notes: Iter 63 parallel multi-agent harness (2 of 2 successful). Both agents reported all-3-candidate-URL 404s for primary sources, both used WebSearch + L21 doj_fetch / L11 secondary corroboration to recover content. Agent A flagged slug-content alignment warning (slug bundles Knoot+Chapman+Didenko but body covers only Knoot; Chapman+Didenko backlog flagged). Agent A's stale source wikilink suffix (`-2024`) corrected to canonical `2024-08-08_justice-gov_dprk-it-worker-fraud-disruption-knoot-chapman-didenko`.

## [2026-05-09] ingest [parallel batch x2] | DOJ Raptor Train / Flax Typhoon PRC IoT botnet disruption (2024-09-18) + DOJ 5 Scattered Spider members charged (2024-11-20)
- Sources: 2 raw + 2 source pages + 1 operation page + 1 case page (6 new pages)
- Pages updated: 7 country (US, FR, AU, CA, NZ, UK, CN, ES — 5 Scattered Spider adds Spain), 3 organization (us-doj, fbi, fbi-cyber-division), 4 crime-type (hacking-ic, cybercrime-infrastructure-ic, malware-ic, online-fraud-ic, identity-theft) + Reference rows + 2 cross-case backlinks (Jubair sister cases).
- Key findings:
  - **Raptor Train / Flax Typhoon (DOJ 2024-09-18, Press Release 24-1173)**: Court-authorized operation in W.D. Pa. disrupted PRC state-sponsored botnet of 200,000+ consumer SOHO devices (routers, IP cameras, DVRs, NAS) operated by Beijing-based Integrity Technology Group (KRLab brand). Five Eyes IC chain documented: US (FBI San Diego, FBI Cyber Division, USAO-WDPA, NSD/CCIPS/OIA, NSA, USCYBERCOM CNMF) + France ("French authorities") + AU + CA + NZ + UK ("partner agencies" — country-named, agency-unnamed). In-operation DDoS counter-attack from adversary against FBI infrastructure was unsuccessful. **First wiki record of court-authorized PRC contractor-botnet takeover** with Five Eyes joint advisory.
  - **US v. 5 Scattered Spider members (DOJ 2024-11-20, Press Release 24-289, C.D. Cal.)**: 5 defendants charged via indictment + 1 by complaint — Tyler Robert Buchanan (UK national, charged by complaint, secondary-source-only Spain arrest in Palma de Mallorca June 2024), Ahmed Hossam Eldin Elbadawy (TX), Noah Michael Urban (FL), Evans Onyeaka Osiebo (TX), Joel Martin Evans (NC, arrested 2024-11-19). FBI Los Angeles + Charlotte / Denver / Houston / Portland field offices + USAO-EDNC + Police Scotland named (Scottish cooperation explicit, Spain arrest secondary-source-only). Charges: wire fraud + conspiracy + aggravated identity theft. **Sister to existing Scattered Spider matters** [[us-v-jubair-scattered-spider-2025]] + [[uk-jubair-flowers-tfl-cyber-attack-2025]] (cross-linked).
- Process notes: Iter 62 used parallel multi-agent harness (2 of 2 successful, both DOJ Akamai bypassed via L21). Both agents flagged URL slug discrepancies — Flax Typhoon URL needed apostrophe drop (`peoples-republic-china-state`); Scattered Spider real URL was `usao-cdca/pr/5-defendants-charged-federally-running-scheme-targeted-victim-companies-phishing-text` (not the prompted candidates). Per L1 verified body publish dates against URL/secondary-source claims. Agent A's `[[usdoj]]` in operation page replaced with `[[us-doj]]` for canonical backlink.

## [2026-05-09] ingest [parallel batch x2] | DOJ Doppelganger Russian Influence Op domain seizures (2024-09-04) + DOJ 14 DPRK IT worker conspiracy indictment (2024-12-12)
- Sources: 2 raw + 2 source pages + 1 operation page + 1 case page (6 new pages)
- Pages updated: 4 country (US, RU, KP, CN), 3 organization (us-doj, fbi, us-treasury), 6 crime-type (cybercrime-infrastructure-ic, money-laundering-ic, online-fraud-ic, identity-theft, extortion-ic, malware-ic) + body Reference rows.
- Key findings:
  - **Doppelganger / RT / Tenet Media (DOJ 2024-09-04, SDNY + EDPA)**: 32 domains seized; SDNY indictment of 2 RT employees (Konstantin Kalashnikov + Elena Afanasyeva, both fugitive in Russia) under FARA conspiracy + money-laundering conspiracy; Treasury OFAC same-day designations (10 individuals + 2 entities); Russian apparatus identified as Social Design Agency + Structura + ANO Dialog allegedly directed by Sergei Kiriyenko (First Deputy Chief of Staff). **IC-scope flag**: no foreign LE cooperation partner credited — kept as comparison case for "no-cooperation cyber enforcement" pattern with explicit warning callout. Useful for IC effectiveness analysis comparing parallel-sanction vs. joint-investigation models.
  - **US v. 14 DPRK IT workers (DOJ 2024-12-12, E.D. Mo., Eastern Division — St. Louis)**: 14 DPRK nationals indicted (Jong Song Hwa, Ri Kyong Sik, Kim Ryu Song, Rim Un Chol, Kim Mu Rim, Cho Chung Pom, Hyon Chol Song, Son Un Chol, Sok Kwang Hyok, Choe Jong Yong, Ko Chung Sok, Kim Ye Won, Jong Kyong Chol, Jang Chol Myong) for ~$88M+ generated 2017-2023. Geographies: DPRK (defendants) + China (Yanbian Silverstar, Yanji, Jilin) + Russia (Volasys Silver Star, Vladivostok). Charges: IEEPA conspiracy + wire fraud + money laundering + identity theft + 8/14 aggravated identity theft. State Dept Rewards for Justice $5M reward; $2.26M + $764K seizures; 17+12=29 internet domains seized (Oct 2023 + May 2024 prior actions referenced).
- Process notes: Iter 61 used parallel multi-agent harness (2 of 2 successful). DOJ Akamai 403 caught L21 retry pattern in both agents. Wayback Machine blocked in this environment for both — both agents fell back to globalsecurity.org mirror + secondary tier-1/2 sources (CyberScoop, The Hacker News, Lawfare, NPR, etc.) for cross-corroboration per L11.

## [2026-05-09] ingest [parallel batch x2 + 1 abort] | Eurojust Operation Magnus RedLine/META Stealer (2024-10-29) + DOJ Rim Jong Hyok / Andariel ransomware indictment (2024-07-25); Karakurt/Zolotarjovs aborted (already canonicalized)
- Sources: 2 raw + 2 source pages + 1 operation page + 1 case page (6 new pages)
- Pages updated: 7 country (NL, US, BE, PT, UK, AU + ROK + UK + KP cooperation), 13 organization (eurojust, netherlands-politie, netherlands-om, fbi, us-doj, us-ncis, us-dcis, belgium-federal-police, portugal-policia-judiciaria, uk-nca, australia-afp, us-treasury, knpa, national-intelligence-service-korea), 5 crime-type (malware-ic, cybercrime-infrastructure-ic, identity-theft, ransomware-ic, hacking-ic, money-laundering-ic) + body Reference rows.
- Key findings:
  - **Operation Magnus (2024-10-29)**: Multi-country (NL+US+BE+PT+UK+AU) takedown of RedLine + META infostealer-as-a-service infrastructure. Lead: Netherlands Politie + Eurojust coordination. 2 arrests (Belgium), 1 indictment (Maxim Rudometov), 3 servers seized, 2 domains seized, 1,200+ infected servers identified, victim-check resource published at operation-magnus.com. **First wiki record of Eurojust-coordinated infostealer-MaaS takedown** with public victim-notification artifact.
  - **US v. Rim Jong Hyok / Andariel (2024-07-25)**: Landmark US indictment (D. Kan., 2:24-cr-20061-HLT-ADM) of explicitly state-sponsored RGB / Andariel cyber operator for ransomware against US healthcare critical infrastructure (~6 hospitals/clinics) + linked espionage exfiltration against US defense/aerospace + South Korean defense industrial base + Taiwanese defense + NASA OIG. Co-signed Joint Cybersecurity Advisory **AA24-207A** with ROK NIS, ROK NPA, UK NCSC. **First wiki-recorded landmark public-record artifact of US-Korea-UK ransomware/espionage cooperation against DPRK state-sponsored actor**. $10M Rewards for Justice reward; $114K crypto seized + $500K prior FBI seizure; 4.3 BTC traced through Sino-Korean Friendship Bridge laundering pathway (Dandong → Sinuiju).
  - **Karakurt / Zolotarjovs ABORTED**: Existing canonical case page `wiki/cases/us-v-deniss-zolotarjovs.md` covers full extradition (Country of Georgia → US, NOT Latvia as prompted) + plea + 2026-05-04 sentencing. Per CLAUDE.md rule 19 (canonicalize entities), no new page created. Agent flagged minor data-integrity observation: existing case page lists `[[hacking-ic]]` but actual charges are money laundering + wire fraud + Hobbs Act extortion conspiracy — defer to follow-up audit pass.
- Process notes: Iter 60 used parallel multi-agent harness (2 of 3 successful, 1 graceful abort). DOJ Akamai bot-protection caught L21 retry pattern (Agent B). Eurojust URL slug found via WebSearch fallback (L11) — slug is `malware-targeting-millions-people-taken-down-international-coalition`, not the prompted candidate. Mid-cycle integrity push performed at end of iter 60 per user instruction.

## [2026-05-09] ingest [parallel batch x3] | BKA Operation Final Exchange (2024-09-19) + DOJ Blender/Sinbad mixer indictment (2025-01-10) + DOJ-OPA Jubair US-side parallel (2025-09-18)
- Sources: 3 raw + 3 source pages + 1 operation page + 2 case pages (9 new pages)
- Pages updated: 5 country (DE, RU, US, NL, FI, UK), 5 organization (germany-bka, fbi, us-doj, office-of-international-affairs, uk-nca), 5 crime-type (money-laundering-ic, ransomware-ic, cybercrime-infrastructure-ic, hacking-ic, extortion-ic) + body Reference rows; cross-links to existing operations [[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]], [[treasury-garantex-grinex-russian-network-sanctions-2025]], [[de-ch-crypto-mixer-takedown-2025]], [[uk-jubair-flowers-tfl-cyber-attack-2025]], [[us-v-kai-west-intelbroker-2025]].
- Key findings:
  - **BKA Operation Final Exchange (2024-09-19)**: First wiki record of single-jurisdiction takedown of 47 Russian-language no-KYC cryptocurrency exchanges (Xchange.cash, Bankcomat, CoinBlinker, Cryptostrike, Baksman, Prostocash + 41 others). Charged under §§ 127, 261 StGB. Establishes the **no-KYC instant-swap exchange ecosystem-as-category-target** disruption model.
  - **DOJ Blender/Sinbad mixer indictment (2025-01-10)**: 3 Russian nationals (Ostapenko + Oleynik + Tarasov) charged in N.D. Ga. for operating Blender.io (2018-2022) and successor Sinbad.io (2022-2023) mixers. Tri-national arrest cooperation: Netherlands FIOD + Finland NBI + FBI (2024-12-01). Lazarus Group / DPRK heist proceeds nexus (Axie Infinity USD 620M + Horizon Bridge USD 100M).
  - **DOJ-OPA Jubair US-side parallel (2025-09-18, PR# 25-967)**: Thalha Jubair (UK national, Scattered Spider) charged in D.N.J. complaint with ~120 network intrusions affecting 47 US victims; >USD 115M ransom; victims include US Courts (federal judiciary) and a US critical infrastructure company. **First wiki-recorded parallel UK + US prosecution model for a single Scattered Spider defendant** (companion to existing UK NCA TfL case page).
- Process notes: Iter 59 used parallel multi-agent harness (3 of 3 successful). Lint caught 2 stale wikilinks ([[zit-frankfurt]], [[germany-frankfurt-prosecutor]]) in Final Exchange operation page; cleaned via direct frontmatter edit.

## [2026-05-09] ingest [parallel batch x3] | Treasury jy1933 Sinbad mixer DPRK (2023-11-29) + Treasury sb0205 Korea Sobaeksu DPRK IT (2025-07-24) + Treasury sb0416 Amnokgang DPRK IT facilitators (2026-03-12)
- Sources: 3 raw + 3 source pages + 3 operation pages (9 new pages)
- Pages updated: 5 country (US, NK, VN, LA, ES), 4 organization (us-treasury, us-doj, us-dhs, fbi), 3 crime-type (money-laundering-ic, online-fraud-ic, ransomware-ic) + 6 cross-links to existing DPRK Treasury operations.
- Key findings:
  - **Treasury jy1933 (2023-11-29)**: First wiki record of mixer-as-laundering-vehicle for state-sponsored cyber theft pattern. Sinbad.io processed Lazarus Group heist proceeds: Axie Infinity (~USD 620M, March 2022), Horizon Bridge (~USD 100M, June 2022), Atomic Wallet (USD 100M, June 2023) — 3-heist crypto-laundering chain through one mixer.
  - **Treasury sb0205 (2025-07-24)**: Korea Sobaeksu Trading Company + 3 DPRK individuals (Kim Se Un, Jo Kyong Hun, Myong Chol Min) sanctioned for DPRK IT-worker schemes funding nuclear/missile programs. Cross-agency coordination with DOJ + DHS + State + FBI + HSI cited in release.
  - **Treasury sb0416 (2026-03-12)**: 6 individuals (incl. 3 Vietnamese nationals) + 2 entities (Amnokgang DPRK + Quangvietdnbg Vietnam) sanctioned for DPRK IT-worker fraud generating USD 800M revenue in 2024. **Amnokgang→Quangvietdnbg Vietnam-based front company structure** as a discrete IC pattern; ~21 cryptocurrency addresses across multiple blockchains in SDN List.
- Together with previously-ingested SB-0230, SB-0302, SB-0319, JY-2326, JY-1486, JY-2623, the wiki now has **9 DPRK / Russian / cybercrime-infrastructure Treasury sanctions actions** documented.
- Process notes: Iter 58 used parallel multi-agent harness (3 of 3 successful). Mid-cycle push checkpoint follows this commit.

## [2026-05-09] ingest [parallel batch x3] | Treasury jy1486 Matveev sanctions (2023-05-16) + Treasury jy2623 Evil Corp tri-lateral (2024-10-01) + NCA TfL Jubair/Flowers case (2025-09-18)
- Sources: 3 raw + 3 source pages + 2 operation pages + 1 case page (9 new pages)
- Pages updated: 4 country (US, UK, AU, RU), 5 organization (us-treasury, us-doj, fbi, uk-nca, city-of-london-police), 3 crime-type (ransomware-ic, hacking-ic + asset-freezing mechanism); 7 cross-links to existing operations.
- Key findings:
  - **Treasury jy1486 (2023-05-16)**: Mikhail Matveev OFAC sanctions + parallel DOJ-NJ + DOJ-DC indictments + USD 10M State Rewards. Multi-ecosystem attribution (LockBit + Babuk + Hive). Tri-track parallel-action pattern (administrative + criminal + reward) as the operative IC lesson when Russian extradition is unavailable.
  - **Treasury jy2623 (2024-10-01)**: Evil Corp tri-lateral US/UK/AU sanctions — 7 OFAC + 15 UK FCDO + 3 AU DFAT designees + 2 entities. Concurrent DOJ-EDTX BitPaymer indictment vs Aleksandr Ryzhenkov. **First wiki-recorded tri-lateral cyber-sanctions action**, predicate template for the **9-month BPH chain** (Feb/Jul/Nov 2025).
  - **NCA TfL Jubair/Flowers case (2025-09-18)**: 2 UK defendants charged under Computer Misuse Act for 31 Aug 2024 TfL attack; Flowers additionally faces charges related to US healthcare attacks on SSM Health and Sutter Health. Demonstrates the **UK-as-prosecution-venue + US-target-victim pattern** — UK can prosecute cross-border attacks on US victims standalone without US extradition.
- Process notes: Iteration 57 used parallel multi-agent harness (3 of 3 successful). Agent C had to bypass NCA URL 404 via Wayback Machine snapshot (2025-09-26) to recover content; documented in raw frontmatter.

## [2026-05-09] ingest [parallel batch x3] | Treasury sb0018 Zservers (2025-02-11) + Treasury sb0185 Aeza Group (2025-07-01) + DOJ Romeo Chita Romanian cyber fraud ring (2018-10-09)
- Sources: 3 raw + 3 source pages + 2 operation pages + 1 case page (9 new pages total)
- Pages updated: 11 country pages (US, UK, AU, RU, RO, CA, HR, LV, HU, BA, CN, JO, MY), 4 organization pages (us-treasury, fbi, us-doj, uk-nca, office-of-international-affairs), 5 crime-type pages (ransomware-ic, cybercrime-infrastructure-ic, malware-ic, online-fraud-ic, money-laundering-ic, organized-crime-ic) + body Reference rows; cross-links to existing operations [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025]], [[operation-cronos-phase1]], [[operation-cronos-phase3]].
- Key findings:
  - **Treasury sb0018 (2025-02-11)**: First wiki record of the **9-month US-AU-UK BPH sanctions chain** (Feb 2025 Zservers → July 2025 Aeza Group → November 2025 Media Land + Hypercore). Joint OFAC/DFAT/FCDO action on Zservers Russia BPH for LockBit ransomware support. Designations: Zservers + Mishin + Bolshakov (Russia) + UK XHOST front company + 4 employees (Sidorov/Bolshakov/Odintsov/Ananev).
  - **Treasury sb0185 (2025-07-01)**: US Treasury + UK NCA bilateral sanctions vs Aeza Group (St. Petersburg BPH) + 4 leaders (Penzev/Bozoyan/Gast/Knyazev) + 3 subsidiaries. Hosted Meduza/Lumma infostealers, BianLian ransomware, RedLine, BlackSprut darknet marketplace. Establishes the **Aeza→Hypercore rebranding-after-designation pattern** that emerged after July 2025 (per the Nov 2025 Media Land sanctions release).
  - **DOJ Romeo Chita (2018-10-09, PR# 18-1311)**: 9-defendant Romanian cyber fraud ring extradition; 18-year operational longevity (2007-2025); 10-country footprint (US/RO/CA/HR/LV/HU/BA/CN/JO/MY); USD 4M+ stolen via multi-impersonation phishing (BBB/IRS/US Tax Court/National Payroll Records Center) + keylogger malware. RICO + wire fraud conspiracy + money laundering + counterfeit services trafficking. Daniel Mihai Radu + Manuel Tudor previously extradited from Romania. *Note: agent initially used 2025-02-05 archive-update date in slug; renamed to 2018-10-09 (actual press release date) for accuracy.*
- Process notes: Iteration 56 used parallel multi-agent harness (3 of 3 successful). Agent C correctly flagged the Romeo Chita date discrepancy in its return; main thread renamed slugs and updated cross-references before backlinker apply. lint also caught and fixed a `[[usdoj]]` vs `[[us-doj]]` wikilink mismatch in the Zservers operation page.

## [2026-05-09] ingest [parallel batch x3] | Treasury sb0230 (DPRK Andreyev/Chinyong 2025-08-27) + DOJ Three IRGC hack-and-leak case (2024-09-27) + DOJ IntelBroker Kai West case (2025-06-25)
- Sources: 3 raw + 3 source pages + 1 operation page + 2 case pages (9 new pages total)
- Pages updated: 9 country pages (US, RU, NK, CN, LA, IR, UK, FR, ES, NL), 4 organization pages (us-treasury, fbi, fbi-cyber-division, us-doj, office-of-international-affairs), 4 crime-type pages (money-laundering-ic, online-fraud-ic, hacking-ic, identity-theft, extortion-ic) + body Reference rows; cross-links to existing operations [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]], [[treasury-sanctions-dprk-bankers-laundering-cybercrime-2025]], [[us-doj-iranian-mois-handala-domain-seizure-2026]], [[leakbase-takedown-2026]].
- Key findings:
  - **Treasury sb0230 (2025-08-27)**: First wiki record of the Russia-based DPRK consular official + Russian-national facilitator + Chinese front company + DPRK trading co quadrilateral pattern. 4 designations under E.O. 13687: Vitaliy Sergeyevich Andreyev (Russian national, USD 600K+ crypto-to-USD conversions since Dec 2024), Kim Ung Sun (Russia-based DPRK economic/trade consular official), Shenyang Geumpungri Network Technology Co. Ltd. (Chinese front company in Shenyang), Korea Sinjin Trading Corp. (DPRK trading company). Network supports Chinyong Information Technology Cooperation Company (DPRK Defence Ministry).
  - **DOJ Three IRGC hack-and-leak case (2024-09-27)**: Masoud Jalili (36) + Seyyed Ali Aghamiri (34) + Yaser Balaghi (37) — Iranian nationals, IRGC employees — indicted for spearphishing campaign since ~Jan 2020 against US officials, media, NGOs, and presidential campaign personnel; 'hack-and-leak' against Campaign 1 in June 2024 for the 2024 election. State Dept Rewards for Justice USD 10M reward outstanding. Establishes the **state-sponsored election-interference cyber-actor indictment** baseline alongside the [[us-doj-iranian-mois-handala-domain-seizure-2026|MOIS Handala 2026 domain seizure]].
  - **DOJ-USAO-SDNY IntelBroker Kai West case (2025-06-25, PR# 25-149)**: 25-year-old British national, arrested in France ~Feb 2025, US extradition pending. Forum-1 (BreachForums) owner Aug 2024–Jan 2025; Dec 2022–Jan 2025; 40+ organizations breached; 41 sale offers + 117 free distributions; sought USD 2.4M+; caused USD 25M+ damages. Cooperation thanked: French + Spanish + British + Dutch authorities + DOJ-OIA + FBI-NY. Case before Judge Katherine Polk Failla (S.D.N.Y.). 4 counts: conspiracy to commit computer intrusions; conspiracy to commit wire fraud; accessing protected computers; wire fraud. Establishes the **BreachForums-cybercrime-marketplace-leadership prosecution** complementing the [[leakbase-takedown-2026|LeakBase March 2026 takedown]].
- Process notes: Iteration 55 used parallel multi-agent harness (3 agents → 3 successful ingests). Pre-validated IC scope and publish dates before dispatch. Akamai bot-protection on archives.justice.gov + DOJ USAO-SDNY required curl_cffi Session + 6s sleep + retry pattern (per LESSONS L21).

## [2026-05-09] ingest [parallel batch] | Treasury sb0319 (US/AU/UK Media Land sanctions 2025-11-19) + DOJ Jin/Pak/Alonso/Prince/Ashtor 5-defendant DPRK IT case (2025-01-23) + Treasury sb0225 (Garantex/Grinex re-designation 2025-08-14)
- Sources: 3 raw releases + 3 source pages + 2 operation pages + 1 case page (8 new pages total)
- Pages created: [[2025-11-19_treasury_us-au-uk-sanctions-russian-cybercrime-infrastructure-media-land]], [[2025-01-23_justice-gov_two-north-korean-nationals-three-facilitators-indicted-dprk-it-worker]], [[2025-08-14_treasury_garantex-grinex-russian-network-cyber-criminals-sanctions-evasion]] (sources); [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025]], [[treasury-garantex-grinex-russian-network-sanctions-2025]] (operations); [[us-v-jin-pak-alonso-prince-ashtor-dprk-it-workers-2025]] (case).
- Pages updated: 8 country pages (US, AU, UK, RU, NK, MX, NL, CN), 5 organization pages (us-treasury, fbi, us-doj, office-of-international-affairs, us-secret-service), 6 crime-type pages (ransomware-ic, ddos-ic, cybercrime-infrastructure-ic, hacking-ic, online-fraud-ic, money-laundering-ic, identity-theft) + body Reference rows; [[asset-freezing]] mechanism (operations_using); cross-links to existing operations [[us-uk-prince-group-tco-huione-group-sanctions-2025]], [[cryptex-pm2btc-sanctions]], [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]].
- Key findings:
  - **Treasury sb0319 (2025-11-19)**: First wiki record of US-AU-UK tri-national OFAC/DFAT/FCDO joint sanctions against Russia-based bulletproof hosting (Media Land + 3 leadership + 3 sister companies + Hypercore as Aeza Group rebrand). Establishes the **bulletproof-hosting-as-ransomware-enabler** sanctions track and the Aeza Group → Hypercore rebranding-after-designation pattern (July 2025 Aeza designation → Hypercore rebrand → November 2025 Hypercore designation).
  - **DOJ DPRK 5-def case (2025-01-23, PR# 25-105)**: Jin Sung-Il + Pak Jin-Song (DPRK) + Pedro Ernesto Alonso De Los Reyes (Mexico) + Erick Ntekereze Prince + Emanuel Ashtor (US) indicted in S.D. Florida for multi-year DPRK IT worker scheme; April 2018–August 2024; 64 US victim companies; USD 866,255+ revenue laundered through Chinese bank account; IEEPA charge against Jin and Pak. Alonso arrested in Netherlands 2025-01-10. Establishes the **DPRK-IT-worker-RevGen indictment baseline** that successive 2025-2026 prosecutions (Knoot/Prince sentencings, Treasury sb0302) build on.
  - **Treasury sb0225 (2025-08-14)**: Re-designation of Garantex Europe + designation of successor Grinex + 3 Garantex executives + 6 associated companies in Russia and Kyrgyz Republic. Closes the technical-evasion loophole opened when Garantex officers transferred customer deposits to Grinex after the March 2025 DOJ-led Garantex disruption. Documented ransomware nexus: Conti, Black Basta, LockBit, NetWalker, Phoenix Cryptolocker.
- Process notes: Iteration 54 used the parallel multi-agent harness (3 agents → 3 successful ingests). All 3 candidates pre-validated for IC scope (≥2 countries) and publish-date integrity before dispatch.

## [2026-05-09] ingest | NCA 2025-09-24 — UK arrest of 40s male West Sussex over Collins Aerospace MUSE ransomware affecting Heathrow / Brussels / Berlin Brandenburg airports
- Source: `raw/press-releases/2025-09-24_nca-uk_uk-arrest-following-aerospace-cyber-incident.md` (NCA primary; tier-1)
- Pages created: [[2025-09-24_nca-uk_uk-arrest-following-aerospace-cyber-incident]] (source summary), [[uk-collins-aerospace-airport-ransomware-arrest-2025]] (case page)
- Pages updated: [[united-kingdom]], [[belgium]], [[germany]] (notable_cases), [[uk-nca]] (notable_cases), [[ransomware-ic]] (notable_cases + sources + body Reference row).
- Key findings: NCA arrest 23 September 2025 (evening) of a man in his 40s in West Sussex on suspicion of Computer Misuse Act offences; later released on conditional bail. Triggering incident: 19 September 2025 RTX Corporation product cyber-security incident involving ransomware on Collins Aerospace's MUSE passenger-processing software, disrupting London Heathrow, Brussels Airport, and Berlin Brandenburg from late 19 Sep through 20 Sep 2025. NCA Deputy Director Paul Foster (NCA National Cyber Crime Unit) named in release. Establishes (a) UK-led investigation of pan-European-airport-disruption cyber-physical incident with multi-country victim impact, (b) ransomware-affecting-aviation-supply-chain pattern. Note: NCA release uses 'cyber incident' not 'ransomware'; ransomware framing comes from broader contemporaneous reporting and is flagged in the case page.

## [2026-05-09] ingest | Treasury 2025-11-04 — OFAC SB-0302 designating 8 individuals + 2 entities (Jang Kuk Chol, Ho Jong Son, KMCTC + U Yong Su, Ryujong Credit Bank, 5 China/Russia-based DPRK financial reps) for laundering DPRK cybercrime + IT worker proceeds
- Source: `raw/press-releases/2025-11-04_treasury_dprk-bankers-laundering-cybercrime-it-worker-funds.md` (Treasury press release SB-0302; tier-1 primary)
- Pages created: [[2025-11-04_treasury_dprk-bankers-laundering-cybercrime-it-worker-funds]] (source summary), [[treasury-sanctions-dprk-bankers-laundering-cybercrime-2025]] (operation page)
- Pages updated: [[united-states]], [[north-korea]], [[china]], [[russia]] (operations_participated), [[us-treasury]] (operations_participated), [[money-laundering-ic]], [[online-fraud-ic]] (notable_operations + sources + body Reference rows), [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]] (related_operations cross-link).
- Key findings: 10 OFAC designations under E.O. 13694 (as amended by E.O. 13757, 14144, 14306), E.O. 13810, E.O. 13551, and E.O. 13722. Two North Korean bankers (Jang Kuk Chol, Ho Jong Son) managed USD 5.3M in cryptocurrency for First Credit Bank, with funds linked to a DPRK ransomware actor targeting US victims; KMCTC operates IT worker delegations from Shenyang and Dandong (China) using Chinese nationals as banking proxies; Ryujong Credit Bank facilitated China-North Korea sanctions-evasion remittances. 5 China- or Russia-based DPRK financial representatives designated (Ho Yong Chol, Han Hong Gil, Jong Sung Hyok, Choe Chun Pom, Ri Jin Hyok). DPRK cyber theft cumulative figure: USD 3 billion+ over 3 years (primarily cryptocurrency). First Credit Bank SDN entry updated to surface cryptocurrency addresses for VASP compliance screening. Establishes (a) **DPRK banker-tier sanctions** as a discrete enforcement layer (vs. lower-tier IT worker / facilitator designations), (b) **China + Russia as the operational nodes** for DPRK financial-representative deployment, and (c) **VASP-compliance-screening-via-SDN-update** as a deliberate sanctions design choice.

## [2026-05-09] ingest | DOJ-OPA 2026-03-19 — Court-authorized seizure of 4 Iranian MOIS / Handala Hack faketivist domains (FBI Baltimore + DOJ NSCS + USAO-MD)
- Source: `raw/press-releases/2026-03-19_justice-gov_iranian-mois-cyber-psychological-operations-handala.md` (DOJ-OPA Press Release 26-251; tier-1 primary)
- Pages created: [[2026-03-19_justice-gov_iranian-mois-cyber-psychological-operations-handala]] (source summary), [[us-doj-iranian-mois-handala-domain-seizure-2026]] (operation page)
- Pages updated: [[united-states]], [[iran]], [[israel]] (operations_participated), [[fbi]], [[us-doj]] (operations_participated), [[hacking-ic]], [[extortion-ic]] (notable_operations + sources + body Reference rows).
- Key findings: Court-authorized seizure of 4 MOIS-controlled domains (Justicehomeland.org, Handala-Hack.to, Karmabelow80.org, Handala-Redwanted.to) used as Handala Hack 'faketivist' persona for cyber-enabled psychological operations. Documented activity: 11 March 2026 destructive malware attack on US-based multinational medical technologies firm; 9 March 2026 leak of ~190 IDF/Israeli government PII; 6 March 2026 claimed 851 GB Sanzer Hasidic community data theft; 1 March 2026 death-threat email via Handala_Team@outlook.com offering USD 250K bounty for beheading 2 Iranian-dissident/journalist targets, with explicit invocation of **Jalisco New Generation Cartel (CJNG)** 'partners' in America and Canada. Earlier 2022 Justicehomeland.org claims of MOIS thefts from Albanian government (retaliation for MEK support). Establishes (a) **state-sponsored cyber-enabled transnational repression** as discrete IC-relevant pattern, (b) **cyber-physical-violence convergence via criminal-cartel proxy** as first-of-its-kind documented attack model, (c) **court-authorized domain seizure** as the recurring DOJ disruption tool against state-sponsored cyber operations in absence of extradition opportunity, (d) **faketivist persona pattern** as MOIS operational tradecraft, (e) Albania-2022 → Israel/US-2026 trajectory of MOIS faketivist domain reuse, (f) outstanding USD 10M Rewards for Justice incentive for MOIS personnel attribution.

## [2026-05-09] ingest | SPF 2025-02-27 — SPF + RTP arrest of ALTDOS/DESORDEN/GHOSTR/0mid16B 4-alias data-breach-extortion threat actor in Thailand
- Source: `raw/press-releases/2025-02-27_spf-singapore_global-hacker-arrested-thailand-altdos-desorden-ghostr-0mid16b.md` (SPF press release; tier-1 primary)
- Pages created: [[2025-02-27_spf-singapore_global-hacker-arrested-thailand-altdos-desorden-ghostr-0mid16b]] (source summary), [[sg-th-altdos-desorden-ghostr-takedown-2025]] (operation page)
- Pages updated: [[singapore]], [[thailand]] (operations_participated), [[singapore-police]], [[thailand-royal-police]] (operations_participated), [[hacking-ic]], [[extortion-ic]] (notable_operations + sources + body Reference rows), [[spf-fpb-operation-cryptoscam-2025]], [[afp-rtp-bangkok-scam-centre-operation-firestorm-2025]] (related_operations cross-links).
- Key findings: ~5-year SPF Cybercrime Command + RTP Central Investigation Bureau bilateral track culminating in 26 February 2025 arrest of a 39-year-old male in Thailand suspected of operating sequentially under aliases ALTDOS, DESORDEN, GHOSTR, and 0mid16B. Internationally responsible for at least 75 cases (90+ per corresponding Group-IB release; 13TB+ stolen personal data). Triggered by 11 Singapore victim reports in 2020. Charges (Thailand): Thai Criminal Code + Computer-Related Crime Act. Assets seized: > 10 million THB. Establishes (a) **SPF-RTP bilateral cybercrime track** as a sustained 5-year channel, (b) **4-alias / 5-year correlation tradecraft** as the analytical foundation, (c) **extortion-without-encryption pattern** (exfil + reputation-pressure escalation via media + DP regulators) as a structurally distinct attack-pattern category from ransomware, (d) **public-private partnership** (SPF/RTP/CSA + Group-IB DCRCs) as the documented operational model for multi-alias cybercriminal arrests.

## [2026-05-09] ingest | Treasury 2026-04-23 — OFAC sanctions Cambodian Senator Kok An + 28-target scam-center network + Scam Center Strike Force coordinated actions
- Source: `raw/press-releases/2026-04-23_treasury_sanctions-cambodian-senator-kok-an-scam-center-network.md` (Treasury press release SB-0469; tier-1 primary)
- Pages created: [[2026-04-23_treasury_sanctions-cambodian-senator-kok-an-scam-center-network]] (source summary), [[treasury-sanctions-kok-an-scam-center-network-2026]] (operation page)
- Pages updated: [[united-states]], [[cambodia]] (operations_participated), [[us-treasury]], [[us-doj]], [[fbi]], [[us-secret-service]] (operations_participated), [[online-fraud-ic]], [[money-laundering-ic]], [[organized-crime-ic]] (notable_operations + sources + body Reference rows), [[us-uk-prince-group-tco-huione-group-sanctions-2025]] (related_operations cross-link).
- Key findings: 29 OFAC designations (Kok An + Crown Resorts + Anco Brothers + 26 individuals/entities) under E.O. 13694 as amended, in furtherance of E.O. 14390 (6 March 2026) 'Combating Cybercrime, Fraud, and Predatory Schemes Against American Citizens'. Coordinated with the **Scam Center Strike Force** (USAO-DC + DOJ Criminal Division + FBI + USSS; focus Burma/Cambodia/Laos), which the same day announced charges against 2 Burma-Cambodia scam-compound operators, seizure of a social media messaging app used to recruit human-trafficking victims, and seizure of **503 fraudulent web domains** for cryptocurrency investment fraud. State Department announced USD 10M reward for Tai Chang (Burma) info + USD 4M reward for fugitive Daren Li. Establishes (a) the **Scam Center Strike Force** as a formal US multi-agency framework, (b) **E.O. 14390** as new presidential authority, (c) **Cambodian political-protection layer** as structural enforcement obstacle (Kok An is a sitting senator), (d) **casino-as-laundering-vehicle pattern** explicitly cited, and (e) **sustained ~18-month OFAC SE-Asia sanctions chain** (Apr 2026 + Nov 2025 + Oct 2025 + Sep 2025 + Sep 2024).

## [2026-05-09] ingest | AFP 2026-03-07 — Operation Candy: Swedish-led 5-country phone-forensics-derived synthetic-drug + money-laundering takedown (Sweden + Spain + Thailand + Australia + Germany + Europol + Eurojust)
- Source: `raw/press-releases/2026-03-07_afp_operation-candy-15-arrests-australia-spain-sweden-thailand.md` (AFP media release; tier-1 primary)
- Pages created: [[2026-03-07_afp_operation-candy-15-arrests-australia-spain-sweden-thailand]] (source summary), [[operation-candy-encrypted-comms-drugs-2026]] (operation page)
- Pages updated: [[sweden]], [[spain]], [[thailand]], [[australia]], [[germany]] (operations_participated), [[europol-ec3]], [[eurojust]], [[australia-afp]] (operations_participated), [[money-laundering-ic]], [[organized-crime-ic]], [[dark-web-ic]], [[drug-trafficking]] (notable_operations + sources + body Reference rows).
- Key findings: ~2.5-year transnational organised-crime takedown started Nov 2023 with seizure of 2 mobile phones from a Swedish trafficker, expanded via Europol forensic analysis to expose synthetic-drug + money-laundering networks across Sweden, Thailand, Spain, Germany, and Australia, culminating in the **4 March 2026** action day with ~20 simultaneous house searches in SE/ES/TH and 13 overseas arrests (15 total including 2 prior Australia from a Feb 2025 German Customs 1.2t drug interception). EUR 4M criminal-asset seizure with tracing-pending posture. Establishes (a) **phone-forensics-first investigative model** (small device seizure → multi-country prosecution chain via sustained Europol support), (b) Sweden-led Eurojust 5-country judicial coordination as essential to *prosecution* (per Eurojust framing), (c) rare **Sweden + Australia + Thailand cooperation track**, and (d) canonical **substituted-cargo controlled delivery** as the international drug-trafficking attribution chain.

## [2026-05-09] ingest | UK NCA 2026-04-09 — Operation Atlantic: NCA-led UK-US-Canada cryptocurrency 'approval phishing' takedown ($12M frozen, 20,000 victims, $45M fraud identified)
- Source: `raw/press-releases/2026-04-09_nca-uk_operation-atlantic-cryptocurrency-fraudsters.md` (NCA Newsroom press release; tier-1 primary)
- Pages created: [[2026-04-09_nca-uk_operation-atlantic-cryptocurrency-fraudsters]] (source summary), [[operation-atlantic-approval-phishing-2026]] (operation page)
- Pages updated: [[united-kingdom]], [[united-states]], [[canada]] (operations_participated), [[uk-nca]], [[us-secret-service]], [[city-of-london-police]] (operations_participated), [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows).
- Key findings: NCA-led weeklong UK-US-Canada international action against cryptocurrency 'approval phishing' fraud. Co-hosted by NCA + US Secret Service + Ontario Provincial Police + Ontario Securities Commission; UK participation also from City of London Police + Financial Conduct Authority. Outcomes: 20,000+ victims identified, USD 12M+ frozen, USD 45M+ in cryptocurrency fraud identified globally; 120+ web domains disrupted (per corresponding US Secret Service release); one UK victim documented loss > GBP 52,000. Establishes (a) the NCA-led UK-US-Canada tri-jurisdiction North-Atlantic cooperation pattern, (b) **'approval phishing' as a discrete cryptocurrency-fraud technique class** (granting attackers ongoing wallet access vs. one-time credential capture), (c) NCA London HQ physical co-location format paralleling Europol J-CAT / data-sprint formats, and (d) **asset-recovery-first metric set** (frozen funds + victims as primary outcomes; zero documented arrests in cited release).

## [2026-05-09] ingest | FBI Atlanta 2026-04-10 — W3LL phishing kit / W3LLSTORE takedown (FBI Atlanta + Indonesian National Police; first US-Indonesia phishing-developer action)
- Source: `raw/press-releases/2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll.md` (FBI Atlanta press release; tier-1 primary)
- Pages created: [[2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll]] (source summary), [[w3ll-phishing-kit-takedown-2026]] (operation page)
- Pages updated: [[united-states]], [[indonesia]] (operations_participated), [[fbi]], [[indonesia-police]] (operations_participated), [[online-fraud-ic]], [[cybercrime-infrastructure-ic]] (notable_operations + sources + body Reference rows), [[labhost-phishing-as-a-service-takedown-2024]], [[leakbase-takedown-2026]] (related_operations cross-links).
- Key findings: First-of-its-kind US-Indonesia coordinated action against a phishing kit developer (per FBI Atlanta). Detention of alleged W3LL developer 'G.L.' by Indonesian National Police; FBI Atlanta + USAO-NDGA seized US-side infrastructure and key W3LL/W3LLSTORE domains. W3LL phishing kit (~USD 500/access) uniquely captured **session data alongside credentials**, enabling MFA bypass — making it a 'full-service cybercrime platform'. W3LLSTORE marketplace facilitated 25,000+ compromised account sales (2019-2023); post-2023 the kit migrated to encrypted messaging platforms (rebranded), targeting 17,000+ victims worldwide and USD 20M+ in attempted fraud (2023-2024 phase alone). Establishes (a) US-Indonesia bilateral track in PhaaS disruption, (b) MFA-bypassing session-data capture as a senior-tier PhaaS attribute, and (c) the marketplace-shutdown→encrypted-messaging migration pattern as a documented PhaaS persistence mode.

## [2026-05-09] ingest | DOJ-OPA 2026-04-30 — Versus Project dark web marketplace cofounder Patrick Schmitz extradited from Colombia (D.N.J., 8-count indictment; CCE)
- Source: `raw/press-releases/2026-04-30_justice-gov_versus-project-creator-extradited-colombia.md` (DOJ-OPA Press Release 26-428; tier-1 primary)
- Pages created: [[2026-04-30_justice-gov_versus-project-creator-extradited-colombia]] (source summary), [[us-v-schmitz-versus-project]] (case page)
- Pages updated: [[united-states]], [[colombia]], [[germany]] (notable_cases), [[fbi]], [[us-doj]], [[office-of-international-affairs]] (notable_cases), [[dark-web-ic]] (notable_cases + sources + body Reference rows), [[drug-trafficking]] (notable_cases + sources + body Reference rows), [[online-fraud-ic]], [[money-laundering-ic]] (notable_cases).
- Key findings: 22-month US-Colombia extradition timeline (June 2024 provisional arrest → 29 April 2026 extradition) for Patrick Schmitz (37, German national, Taganga, Colombia), cofounder/day-to-day operator of The Versus Project (380,000+ users, 32,000+ listings, 300,000+ orders, Bitcoin/Monero-only payment rail, Nov 2019–May 2022). 8-count D.N.J. indictment with **continuing criminal enterprise** (20-yr mandatory minimum, max life) as the lead count — atypical CCE framing for a dark web *marketplace* cofounder. Investigative stack: HSI Newark (lead), FBI Kansas City, IRS-CI Newark, DOJ-OIA, US Marshals, Policía Nacional de Colombia. **JCODE** attribution.

## [2026-05-09] ingest | Europol 2026-03-21 — Operation Alice: 23-country takedown of 373,000+ dark web onion domains (BLKA + ZKI + BKA + Europol; CSAM-fraud + CaaS-fraud)
- Source: `raw/press-releases/2026-03-21_europol_global-cybercrime-crackdown-373000-dark-web-sites-operation-alice.md` (Europol Newsroom press release; tier-1 primary)
- Pages created: [[2026-03-21_europol_global-cybercrime-crackdown-373000-dark-web-sites-operation-alice]] (source summary), [[operation-alice-csam-fraud-2026]] (operation page)
- Pages updated: 23 country pages (operations_participated), [[germany-bka]], [[europol-ec3]], [[australia-afp]], [[canada-rcmp]], [[switzerland-fedpol]], [[polizia-di-stato]], [[portugal-policia-judiciaria]], [[spain-guardia-civil]], [[uk-nca]] (operations_participated), [[csam-ic]], [[online-fraud-ic]], [[cybercrime-infrastructure-ic]] (notable_operations + sources + body Reference rows).
- Key findings: German-led, 23-country, Europol-coordinated takedown of a single-perpetrator dark web platform empire — 373,000+ Tor onion domains seized, 105 servers seized in Germany (out of 287 at peak), 1 perpetrator (35-year-old PRC-based male, international arrest warrant issued), 440 customers worldwide identified (100+ ongoing). Network advertised CSAM 'packages' (90,000+ domains, EUR 17–215, ~10,000 paying customers, EUR 345,000+ profit Feb 2020–Jul 2025) and CaaS offerings (~283,000 domains) without delivering — the **fraud-CSAM hybrid pattern**. Establishes (a) the largest documented dark-web onion-domain takedown in the wiki corpus by site count, (b) the **paying-customer-as-suspect** prosecutorial model (attempted purchase = predicate), and (c) the largest CSAM-related Europol-coordinated cooperation in the corpus to date by participating-country count (23).

## [2026-05-09] ingest | Europol 2026-01-12 — 34 arrests in Spain against 'Black Axe' criminal organisation (Spanish National Police + Bavarian BLKA + Europol)
- Source: `raw/press-releases/2026-01-12_europol_34-arrests-spain-black-axe-criminal-organisation.md` (Europol Newsroom press release; tier-1 primary)
- Pages created: [[2026-01-12_europol_34-arrests-spain-black-axe-criminal-organisation]] (source summary), [[black-axe-spain-takedown-2026]] (operation page)
- Pages updated: [[spain]], [[germany]] (operations_participated), [[spain-national-police]], [[germany-bka]], [[europol-ec3]] (operations_participated), [[online-fraud-ic]], [[money-laundering-ic]], [[organized-crime-ic]] (notable_operations + sources + body Reference rows), [[black-axe-switzerland-takedown-2026]], [[black-axe-bec-2021]] (related_operations cross-links).
- Key findings: Spanish National Police + Bavarian BLKA + Europol coordinated arrest sweep against the core Spain-side cell of the Nigeria-origin 'Black Axe' / Neo-Black Movement of Africa transnational organised crime group: 34 arrests (28 Seville + 3 Madrid + 2 Málaga + 1 Barcelona), EUR 5.93M+ documented fraud damages, EUR 119,352 frozen, EUR 66,403 cash seized. 2 BLKA officers deployed on-site; Madrid-held Europol data sprint + on-the-spot support. Establishes the **Bavaria–Andalusia bilateral track** preceding the [[black-axe-switzerland-takedown-2026|Switzerland April 2026 action]] by ~3 months.

## [2026-05-09] ingest | DOJ-OPA 2025-10-14 — Chairman of Prince Group indicted for Cambodian forced-labor scam compounds + USD 15B BTC forfeiture (EDNY, parallel track to OFAC/UK sanctions)
- Source: `raw/press-releases/2025-10-14_justice-gov_chairman-prince-group-indicted-cambodian-forced-labor-scam-compounds.md` (DOJ-OPA Press Release 25-1,031; tier-1 primary)
- Pages created: [[2025-10-14_justice-gov_chairman-prince-group-indicted-cambodian-forced-labor-scam-compounds]] (source summary), [[us-v-chen-zhi-prince-group-edny-2025]] (case page)
- Pages updated: [[united-states]], [[united-kingdom]], [[cambodia]], [[fbi]], [[us-doj]], [[office-of-international-affairs]], [[uk-nca]], [[online-fraud-ic]], [[money-laundering-ic]], [[organized-crime-ic]] (sources + body Reference rows where applicable), [[us-uk-prince-group-tco-huione-group-sanctions-2025]] (related_cases cross-link).
- Key findings: EDNY indictment of Chen Zhi (Cambodia, 37, founder/chairman Prince Holding Group, at large) for wire-fraud and money-laundering conspiracy directing 10+ Cambodian forced-labor scam compounds running cryptocurrency-investment ('pig butchering') fraud; concurrent civil forfeiture complaint against ~127,271 BTC (USD 15B+) — the largest forfeiture in DOJ history. Documents 'spraying' + 'funneling' crypto-laundering techniques and phone-farm scam-compound infrastructure. Establishes the case-on-operation pattern paired with [[us-uk-prince-group-tco-huione-group-sanctions-2025|US-UK October 2025 sanctions]] (concurrent administrative + criminal action).

## [2026-05-09] enrichment | Europol 2025-11-26 — Operation Olympia / Cryptomixer takedown (DE-CH, complement to existing 2025-12-01 Eurojust release)
- Source: `raw/press-releases/2025-11-26_europol_cryptomixer-operation-olympia-takedown.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2025-11-26_europol_cryptomixer-operation-olympia-takedown]] (source summary)
- Pages enriched: [[de-ch-crypto-mixer-takedown-2025]] — title updated to capture Operation Olympia + Cryptomixer; aliases expanded; timeframe updated (announced 2025-12-01 → 2025-11-26; start "" → 2025-11-24; end 2025-12-01 → 2025-11-28); target_entity updated to specify Cryptomixer (cryptomixer.io) hybrid mixer with EUR 1.3B+ lifetime laundering volume since 2016; participating_agencies adds [[germany-bka]]; results enriched with cryptomixer.io domain seizure, 12 TB data, lifetime EUR 1.3B+ laundering, splash banner; missing_fields tightened; source_count 5 → 6; Europol release added as 6th source.
- Pages updated: [[money-laundering-ic]] (sources + body Reference row).
- Key findings: Operation Olympia (24-28 November 2025) targeted Cryptomixer (cryptomixer.io) — a hybrid clear-web + dark-web cryptocurrency mixing service active since 2016 that laundered EUR 1.3 billion+ in Bitcoin for ransomware groups, dark web markets, drug traffickers, weapons traffickers, and payment-card fraudsters. Lead authorities: BKA + Frankfurt am Main ZIT (DE); Zurich City + Cantonal Police + Zurich PPO (CH). Europol J-CAT coordination + on-spot forensic support. Action-day seizures: 3 servers in Switzerland; cryptomixer.io domain; 12+ TB data; EUR 25M+ Bitcoin. Predecessor mixer takedown chronology: Chipmixer (March 2023) → Cryptomixer (November 2025). Adds Operation Olympia name + Cryptomixer service identification (both absent from the prior Eurojust 2025-12-01 release) + Europol J-CAT mechanism class to the operation page.

## [2026-05-09] ingest | Europol 2024-12-03 — MATRIX encrypted messaging service takedown (NL-FR JIT + Europol OTF, NL/FR/DE/IT/LT/ES 6-country)
- Source: `raw/press-releases/2024-12-03_europol_matrix-encrypted-messaging-service-takedown.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2024-12-03_europol_matrix-encrypted-messaging-service-takedown]] (source summary), [[matrix-encrypted-messaging-takedown-2024]] (operation, case_id `CYB-2024-203`)
- Pages updated: 6 country pages (NL/FR/DE/IT/LT/ES) operations_participated; 7 org pages (dutch-police/france-national-police/germany-bka/lithuania-police/spain-national-police/europol-ec3/eurojust) operations_participated; [[cybercrime-infrastructure-ic]] + [[organized-crime-ic]] (notable_operations + sources + body Reference rows); [[europol-jit]] + [[european-arrest-warrant]] (operations_using); related_operations cross-link to [[operation-kraken-ghost-platform]]; index/master indexes reconciled.
- Key findings: 2024-12-03 action day in 4 countries: 3 arrests (1 FR + 2 ES under EAW from NL); 13 house searches (1 FR + 6 ES + 6 LT); main MATRIX servers in France and Germany taken down (40+ total servers across several countries). Predecessor service to Sky ECC/EncroChat/Exclu/Ghost. NL-FR JIT at Eurojust + Europol Operational Task Force (June 2024 onwards, 5 countries: NL/FR/LT/IT/ES). German technical expertise (Frankfurt am Main ZIT + BKA) + Italian Antimafia Directorate support. 3-month live interception phase: 2.3M+ messages in 33 languages intercepted and deciphered. Splash-page user warning deployed post-takedown. First wiki record of: Europol Operational Task Force (OTF) as discrete IC coordination mechanism class distinct from JIT/J-CAT; encrypted-comms-platform takedown chronology (Sky ECC → EncroChat → Exclu → Ghost → MATRIX) in primary IC documentation.

## [2026-05-09] ingest | DOJ 2026-04-27 — US v. Xu Zewei (HAFNIUM / COVID-19 research, PRC MSS contract hacker extradited from Italy)
- Source: `raw/press-releases/2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy.md` (DOJ-OPA Press Release 26-404; tier-1 primary)
- Pages created: [[2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy]] (source summary), [[us-v-xu-zewei-hafnium-extradited-italy]] (case)
- Pages updated: [[united-states]], [[italy]], [[china]] (notable_cases); [[fbi]], [[us-doj]], [[office-of-international-affairs]] (notable_cases); [[hacking-ic]], [[malware-ic]] (notable_cases + sources + body Reference rows); [[extradition]] (cases_using); index/master indexes reconciled.
- Key findings: Xu Zewei (PRC, 34) extradited from Italy weekend of 2026-04-25/26 to first US court appearance Houston (S.D. Texas) 2026-04-27 on 9-count indictment; co-defendant Zhang Yu (PRC, 44) at large. Activity: Feb 2020 — June 2021 under direction of PRC MSS Shanghai State Security Bureau (SSSB) officers via Shanghai Powerock Network Co. Ltd. enabling-company contractor structure. Phase 1 (early 2020): COVID-19 research intrusions targeting US universities + virologists/immunologists. Phase 2 (late 2020 — early 2021): HAFNIUM Microsoft Exchange Server vulnerability exploitation campaign (12,700+ US organisations compromised); specific Xu/Zhang victims include another S.D. Texas university and a worldwide-offices law firm with offices in Washington, D.C.; mailbox-search terms 'Chinese sources', 'MSS', 'HongKong'. Italy arrest at Milan Malpensa airport July 2025; ~9-month extradition window. DOJ OIA + Italian National Police Cyber Division (Polizia Postale) coordinated extradition. First wiki record of an Italy-as-extradition-source for a Chinese state-sponsored cyber actor. Adds Xu+Zhang+Powerock to wiki's PRC enabling-company prosecution corpus alongside iSoon. First wiki record of HAFNIUM-attributed intrusion-volume figures (12,700+ US orgs) in primary IC documentation.

## [2026-05-09] ingest | Europol 2025-07-23 — xss.is Russian-speaking cybercrime forum takedown (Kyiv arrest, French-led + Ukrainian SBU partnership)
- Source: `raw/press-releases/2025-07-23_europol_xss-is-cybercrime-forum-administrator-arrested-ukraine.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2025-07-23_europol_xss-is-cybercrime-forum-administrator-arrested-ukraine]] (source summary), [[xss-is-cybercrime-forum-takedown-2025]] (operation, case_id `CYB-2025-215`)
- Pages updated: [[france]], [[ukraine]] (operations_participated); [[france-national-police]], [[ukraine-sbu]], [[europol-ec3]] (operations_participated); [[cybercrime-forum-ic]], [[malware-ic]] (notable_operations + sources + body Reference rows); related_operations cross-links to [[leakbase-takedown-2026]], [[labhost-phishing-as-a-service-takedown-2024]], [[archetyp-market-takedown-operation-deep-sentinel-2025]]; index/master indexes reconciled.
- Key findings: 2025-07-22 Kyiv arrest of suspected administrator of xss.is (formerly DaMaGeLaB) — 12-year Russian-speaking cybercrime forum (50,000+ users) selling stolen data, hacking tools, malware, compromised system access, and ransomware-related services. Suspect ran thesecure.biz private cybercriminal messaging platform; served as trusted-third-party arbiter for criminal disputes; earned EUR 7M+ in advertising and facilitation fees over ~20 years of cybercrime activity. Lead: French Police Brigade de lutte contre la cybercriminalité (BL2C, Préfecture de Police de Paris) + Paris Prosecutor (Parquet de Paris JUNALCO); investigation initiated July 2021. Ukrainian SBU Cybercrime Department + General Prosecutor's Office of Ukraine partner. Europol EC3 contributions: virtual command post (September 2024); on-site Kyiv mobile office during action week. First wiki record of: (a) French BL2C as lead France-side cybercrime authority for transnational forum takedown; (b) Europol virtual command post mechanism as discrete IC support class; (c) trusted-third-party-arbiter cybercrime-forum-business-model class in primary IC documentation.

## [2026-05-09] ingest | Europol 2025-05-07 — Operation PowerOFF May 2025 phase (Polish-led DDoS-for-hire empire takedown, PL/US/DE/NL)
- Source: `raw/press-releases/2025-05-07_europol_ddos-for-hire-empire-poland-4-administrators-us-9-domains.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2025-05-07_europol_ddos-for-hire-empire-poland-4-administrators-us-9-domains]] (source summary), [[operation-power-off-2025-05]] (operation, case_id `CYB-2025-214`, parent_operation [[operation-power-off]])
- Pages updated: [[poland]], [[united-states]], [[germany]], [[netherlands]] (operations_participated); [[europol-ec3]], [[poland-police]], [[fbi]], [[us-doj]], [[germany-bka]], [[dutch-police]] (operations_participated); [[ddos-ic]] (notable_operations + sources + body Reference row); related_operations cross-links to [[operation-power-off]] and [[operation-power-off-2026-04]]; index/master indexes reconciled.
- Key findings: Polish CBZC arrested 4 administrators of 6 stresser/booter services (Cfxapi, Cfxsecurity, neostress, jetstress, quickdown, zapcut, active 2022-2025); US (USDOJ + FBI + HSI + DCIS) seized 9 booter-service domains during the coordinated week; Dutch authorities deployed fake booter sites as warnings + shared data from Dutch data-centre infrastructure seizures with Poland; German BKA + ZIT Frankfurt identified one suspect and shared intelligence on others; Europol EC3 analytical and operational support throughout. First wiki record of: (a) Polish Central Cybercrime Bureau (CBZC) as lead Polish federal-cybercrime authority for an Operation PowerOFF phase; (b) Dutch fake-booter-site warning methodology as a discrete deception-based deterrence IC mechanism class.

## [2026-05-09] ingest | Treasury 2025-10-14 — US-UK largest-ever sanctions action vs SE Asia cybercriminal networks (Prince Group TCO + Huione Group)
- Source: `raw/press-releases/2025-10-14_treasury_us-uk-largest-action-cybercriminal-networks-southeast-asia.md` (US Treasury press release SB0278; tier-1 primary)
- Pages created: [[2025-10-14_treasury_us-uk-largest-action-cybercriminal-networks-southeast-asia]] (source summary), [[us-uk-prince-group-tco-huione-group-sanctions-2025]] (operation, case_id `CYB-2025-213`)
- Pages updated: [[united-states]], [[united-kingdom]], [[cambodia]] (operations_participated); [[fbi]], [[us-doj]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]], [[extortion-ic]] (notable_operations + sources + body Reference rows); related_operations cross-links to [[korea-cambodia-philippines-73-extradition-2026]], [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]], [[afp-rtp-bangkok-scam-centre-operation-firestorm-2025]]; index/master indexes reconciled.
- Key findings: 2025-10-14 OFAC + FinCEN + UK FCDO + UK OFSI four-channel coordinated action — 146 OFAC sanctions targets within Prince Group TCO (Cambodia-based, Chen Zhi-led); 117 affiliated businesses + 1 official designated; concurrent UK FCDO/OFSI sanctions on Prince Group entities; FinCEN Section 311 final rule severing Huione Group from US financial system; EDNY criminal indictment unsealed against Chen Zhi. Underlying scope: $16.6B+ cumulative US online-investment-scam losses, $10B+ in 2024 alone (66% YoY) attributable to SE Asia. Huione Group laundered $4B+ Aug 2021-Jan 2025 ($37M+ DPRK cyber heists, $36M+ VC investment scams, $300M+ other cyber scams). 10+ Cambodian scam compounds; 100+ shell-company web (MU/TW/SG/LA/PW/KH); January 2025 OFAC-OFSI MOU as foundational instrument. First wiki record of: (a) OFAC + FinCEN + FCDO + OFSI four-channel sanctions architecture; (b) FinCEN Section 311 used against SE Asia scam-laundering target; (c) cross-laundering nexus where single SE Asia conglomerate (Huione) processes both DPRK cyber-heist and SE Asia pig-butchering proceeds.

## [2026-05-09] ingest | AFP 2025-06-17 — AFP-RTP Bangkok investment scam centre takedown (Operation Firestorm, AU-TH bilateral)
- Source: `raw/press-releases/2025-06-17_afp_bangkok-investment-scam-centre-takedown-operation-firestorm.md` (AFP press release; tier-1 primary)
- Pages created: [[2025-06-17_afp_bangkok-investment-scam-centre-takedown-operation-firestorm]] (source summary), [[afp-rtp-bangkok-scam-centre-operation-firestorm-2025]] (operation, case_id `CYB-2025-212`)
- Pages updated: [[australia]], [[thailand]] (operations_participated); [[australia-afp]], [[thailand-royal-police]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); related_operations cross-links to [[india-cbi-noida-tech-support-scam-takedown-2025]], [[korea-cambodia-philippines-73-extradition-2026]], [[uk-nigeria-meta-scam-centre-disruption-2026]]; index/master indexes reconciled.
- Key findings: 2025-06-16 RTP execution of search warrants at six-bedroom Bangkok-suburb residential property operating as investment scam boiler room; 13 men arrested (5 Australian, 6 UK, 1 Canadian, 1 South African) under Section 210 Thai Criminal Code; AUD 1,900,000+ in suspected stolen funds amassed in two months (April-June 2025); fake high-yield fixed-income bond pitches with fraudulent international-financial-firm representations + misappropriated authentic financial services licence + online face-to-face video meetings + cryptocurrency-laundering downstream. First Thailand takedown under AFP JPC3 Operation Firestorm (launched August 2024) — three prior takedowns in Manila. First wiki record of: (a) Operation Firestorm framework; (b) AFP Joint Policing Cybercrime Coordination Centre (JPC3); (c) AFP International Network as discrete IC channel class; (d) Australia-Thailand bilateral cybercrime cooperation pattern.

## [2026-05-09] enrichment | Europol 2025-11-26 — Phase 2 of EUR 700M+ crypto-fraud network takedown (affiliate-marketing infrastructure, BG/IL/MT added)
- Source: `raw/press-releases/2025-11-26_europol_international-takedown-cryptocurrency-fraud-network-eur-700-million.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2025-11-26_europol_international-takedown-cryptocurrency-fraud-network-eur-700-million]] (source summary)
- Pages enriched: [[eurojust-600m-crypto-money-laundering-takedown-2025]] (renamed to capture both phases; added Phase 2 to Operational Timeline + Results + Cooperation Mechanisms; added bulgaria/israel/malta to participating_countries; added [[europol-ec3]] to participating_agencies; updated source_count 1→2; updated network laundering total from EUR 600M to EUR 700M+; added the Europol release as second tier-1 source).
- Pages updated: [[bulgaria]], [[israel]], [[malta]] (operations_participated); [[europol-ec3]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (sources + body Reference rows); index/master indexes reconciled.
- Key findings: Phase 2 (2025-11-25 to 2025-11-26) targeted affiliate-marketing infrastructure with searches in Belgium, Bulgaria, Germany, Israel; targets included companies offering deepfake celebrity / media-outlet / politician impersonation ad services to drive crypto-investment-fraud victim recruitment. First wiki record of (a) Israeli National Cybercrime Unit (Intelligence Division) operational involvement in a Europol-coordinated cryptocurrency-fraud takedown; (b) deepfake-celebrity-impersonation affiliate-marketing methodology in primary IC documentation; (c) two-phase EU + non-EU partner takedown of crypto-fraud + affiliate-marketing infrastructure. Updates the case to reflect 8-country participation (BE/BG/CY/FR/DE/IL/MT/ES) and >EUR 700M+ network laundering total (vs EUR 600M Phase-1-only Eurojust figure).

## [2026-05-09] ingest | Europol ECTC — Project Compass against The Com network (28-country, January 2025 — ongoing)
- Source: `raw/policy-documents/2026-02_europol_project-compass-the-com-network.md` (Europol Operations / Project Compass page; tier-1 primary)
- Pages created: [[2026-02_europol_project-compass-the-com-network]] (source summary), [[project-compass-the-com-network-2025]] (operation, case_id `CYB-2025-211`)
- Pages updated: 30 country pages (AU/AT/BE/CA/HR/CZ/DK/FI/FR/DE/EL/HU/IS/IE/IT/LU/MT/NL/NZ/NO/PL/PT/RO/SK/SI/ES/SE/CH/UK/US) operations_participated; 4 org pages (europol-ec3/fbi/uk-nca/canada-rcmp) operations_participated; [[csam-ic]], [[extortion-ic]] (notable_operations + sources); related_operations cross-links to [[operation-stream-kidflix]], [[labhost-phishing-as-a-service-takedown-2024]]; index/master indexes reconciled.
- Key findings: Europol European Counter Terrorism Centre (ECTC)–coordinated 28-country project active since January 2025 targeting The Com (nihilistic extremist transnational virtual network). Subgroups: Cyber Com (network intrusions / ransomware), Offline Com (terrorism), (S)extortion Com (CSAM extortion of minors); subgroup 764 active since 2021 (recruitment/grooming/violence). Results snapshot: 30 perpetrators arrested (contributed to AP Dolphin); 4 victims safeguarded; 62 identified or partial victims; 179 identified or partial perpetrators; 9 awareness-raising activities. First wiki record of: (a) Europol ECTC as coordination authority for a long-running cybercrime+extremism cooperation project; (b) 28-country roster combining Five Eyes + 22 EU MS + 3 EFTA partners; (c) "data sprints" as a discrete IC mechanism class; (d) The Com / 764 as a wiki entity bridging cybercrime, CSAM, and counter-terrorism corpora.

## [2026-05-09] ingest | Eurojust 2022-11-10 — Massive cryptocurrency investment fraud takedown (Sweden-led 8-country JIT, 10-country action 2022-11-08→2022-11-09)
- Source: `raw/press-releases/2022-11-10_eurojust_massive-investment-fraud-hundreds-thousands-victims.md` (Eurojust press release; tier-1 primary)
- Pages created: [[2022-11-10_eurojust_massive-investment-fraud-hundreds-thousands-victims]] (source summary), [[eurojust-massive-investment-fraud-hundreds-thousands-victims-2022]] (operation, case_id `CYB-2022-201`)
- Pages updated: 10 country pages (SE/AL/FI/GE/DE/LV/ES/UA/BG/MK) operations_participated; 5 org pages (eurojust/europol-ec3/germany-bka/spain-national-police/sweden-police) operations_participated; [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); [[europol-jit]], [[european-investigation-order]], [[eurojust-coordination-meeting]], [[mlat-process]] (operations_using); related_operations cross-links to [[eurojust-100m-crypto-investment-fraud-takedown-2025]], [[eurojust-600m-crypto-money-laundering-takedown-2025]], [[albania-austria-call-centre-investment-fraud-2026]]; index/master indexes reconciled.
- Key findings: Sweden-led 8-country JIT (SE/AL/FI/GE/DE/LV/ES/UA) executed 8-9 November 2022 action across 5 territories (AL/BG/GE/MK/UA); 5 arrests (4 AL, 1 GE); 15 call-centre searches (6 AL, 5 GE, 3 UA, 1 MK); 27 other locations + 5 vehicles searched; ~50 hearings; 500+ electronic devices + EUR 340K+ cash + crypto wallets + properties + bank accounts seized. Underlying disrupted OCG: hundreds of thousands of victims worldwide; cryptocurrency-investment fraud since at least 2016; ~EUR 50M/quarter damage rate; dozens of call centres + hundreds of online platforms. JIT-state officials deployed to action-state territories (~33 ES officials in AL action; ~60 DE officials in GE action). 13 Eurojust coordination meetings + 7 Europol operational meetings. First wiki record of an 8-country EU JIT-anchored cryptocurrency-investment-fraud takedown and the largest enumerated JIT membership in the corpus for a single OCG. First wiki record of the Bavarian Central Office for the Prosecution of Cybercrime (ZCB Bamberg).

## [2026-05-09] ingest | Europol 2025-06-16 — Archetyp Market takedown / Operation Deep Sentinel (DE-NL-RO-ES-SE-US, 2025-06-11→2025-06-13)
- Source: `raw/press-releases/2025-06-16_europol_europe-wide-takedown-archetyp-dark-web-drug-market.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2025-06-16_europol_europe-wide-takedown-archetyp-dark-web-drug-market]] (source summary), [[archetyp-market-takedown-operation-deep-sentinel-2025]] (operation, case_id `CYB-2025-210`)
- Pages updated: 6 country pages (DE/NL/RO/ES/SE/US) operations_participated; 8 org pages (germany-bka/dutch-police/romanian-police/spain-national-police/sweden-police/us-doj/europol-ec3/eurojust) operations_participated; [[dark-web-ic]], [[drug-trafficking]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); [[european-investigation-order]], [[eurojust-coordination-meeting]], [[mlat-process]] (operations_using); related_operations cross-link to [[operation-raptor]]; index/master indexes reconciled.
- Key findings: 11-13 June 2025 action days across 5 EU jurisdictions + US partners; ~300 officers deployed; Archetyp Market platform (NL-hosted) taken offline; 30-year-old German-national admin arrested in Barcelona, Spain; 1 moderator + 6 highest vendors targeted in DE/SE; EUR 7.8M assets seized. Underlying disrupted marketplace: 5+ years of operation, 600,000+ users, EUR 250M+ transactions, 17,000+ listings (incl. fentanyl + synthetic opioids). German lead: Generalstaatsanwaltschaft Frankfurt am Main ZIT + BKA. Eurojust EIO + MLA coordination during action days. First wiki record of Operation Deep Sentinel as a discrete operation name; most fully-articulated DE-Spain-NL-SE-RO-US 6-jurisdiction darknet-marketplace takedown architecture in the corpus.

## [2026-05-09] ingest | DOJ 2025-06-30 — DPRK RevGen Initiative coordinated nationwide enforcement wave (DPRK IT worker schemes)
- Source: `raw/press-releases/2025-06-30_justice-gov_coordinated-nationwide-actions-dprk-it-workers.md` (DOJ-OPA Press Release 25-680; tier-1 primary)
- Pages created: [[2025-06-30_justice-gov_coordinated-nationwide-actions-dprk-it-workers]] (source summary), [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]] (operation, case_id `CYB-2025-209`)
- Pages updated: 7 country pages (US/DPRK/CN/UAE/TW/RS/MY) operations_participated; [[fbi]], [[us-doj]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); [[us-v-knoot-prince-dprk-laptop-farms-2026]] (related_operation cross-link); index/master indexes reconciled.
- Key findings: DOJ-coordinated 2025-06-30 nationwide enforcement wave under DPRK RevGen: Domestic Enabler Initiative — 2 indictments (D. Mass. Zhenxing Wang et al.; N.D. Ga. Kim Kwang Jin et al.), 1 information+plea (D. Mass. Kejia Wang), 1 arrest (Zhenxing Wang), 29 laptop-farm searches across 16 states (June 10-17 wave: 21 premises, 14 states, 137 laptops; October 2024 prior: 8 locations, 3 states, 70+ laptops), 29 financial accounts seized, 21 fraudulent websites seized, ~200 computers seized total. Defendants: 2 US, 8 Chinese, 4 DPRK (at large), 2 Taiwanese nationals. D. Mass. scheme: USD 5M+ revenue, 80+ stolen identities, 100+ Fortune 500 victim companies, ITAR theft from CA AI defense contractor (2024-01-19→2024-04-02). N.D. Ga. scheme: USD 900K+ virtual currency theft via smart-contract source-code modification, laundered via Tornado Cash + fraudulent Malaysian IDs. First wiki record of DPRK RevGen Initiative as discrete IC enforcement framework class.

## [2026-05-09] ingest | USAO-OR 2025-07-16 — US v. Vardanyan / Ryuk ransomware (Armenian national extradited from Ukraine)
- Source: `raw/press-releases/2025-07-16_doj-or_armenian-national-extradited-ryuk-ransomware-extortion-conspiracy.md` (USAO-OR press release; tier-1 primary)
- Pages created: [[2025-07-16_doj-or_armenian-national-extradited-ryuk-ransomware-extortion-conspiracy]] (source summary), [[us-v-vardanyan-avetisyan-ryuk-ransomware]] (case)
- Pages updated: [[united-states]], [[ukraine]], [[france]], [[armenia]] (notable_cases); [[fbi]], [[us-doj]], [[office-of-international-affairs]] (notable_cases); [[ransomware-ic]] (notable_cases + sources + body Reference row); [[extradition]] (cases_using); index/master indexes reconciled.
- Key findings: Karen Serobovich Vardanyan (Armenia, 33) arrested in Kyiv April 2025 at FBI request, extradited from Ukraine to US 2025-06-18; Levon Avetisyan (Armenia, 45) in custody France pending US extradition request; Lyulyava and Prykhodchenko (Ukraine, 53 each) at large. Charges: conspiracy + computer fraud + extortion. Activity period March 2019 – September 2020; ~1,610 BTC (USD 15M+ at time) received in ransom payments. First wiki record explicitly capturing a Ryuk ransomware US prosecution thread; first wiki record of Ukraine-as-extradition-source pattern in Conti-family ransomware prosecution corpus (alongside Spain/Stryzhak, Georgia/Zolotarjovs, France-pending/Avetisyan).

## [2026-05-09] ingest | SPF 2025-06-17 — Operation Cryptoscam (Singapore-Brazil-INTERPOL crypto-tracing cooperation, May 2025 FPB action)
- Source: `raw/press-releases/2025-06-17_spf-singapore_singapore-police-force-partners-interpol-and-federal-police-of-brazil.md` (Singapore Police Force press release; tier-1 primary)
- Pages created: [[2025-06-17_spf-singapore_singapore-police-force-partners-interpol-and-federal-police-of-brazil]] (source summary), [[spf-fpb-operation-cryptoscam-2025]] (operation, case_id `CYB-2025-207`)
- Pages updated: [[singapore]], [[brazil]] (operations_participated); [[singapore-police]], [[interpol-igci]], [[brazil-ministry-of-justice-public-security]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); [[interpol-i24-7]] (operations_using); index/master indexes reconciled.
- Key findings: SPF-originated investigation traced a USD 1.4M January-2024 cryptocurrency-wallet compromise (Singapore victim) to Brazil; FPB alerted via INTERPOL channels; May 2025 FPB executed two simultaneous operations (Operation Cryptoscam being the SPF-originated track) producing 26 search-and-seizure warrants and 11 arrest warrants. Brazil-side authorities: Repression Electronic Bank Fraud Coordination + FPB Regional Office Itajaí, Santa Catarina. First wiki record of Singapore-Brazil bilateral cybercrime cooperation pattern; ASEAN-LATAM cybercrime cooperation channel via INTERPOL.

## [2026-05-09] ingest | Europol 2024-04-18 — LabHost phishing-as-a-service takedown (UK Met-led, 19-country joint action 2024-04-14 to 2024-04-17)
- Source: `raw/press-releases/2024-04-18_europol_international-investigation-disrupts-phishing-service-platform-labhost.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2024-04-18_europol_international-investigation-disrupts-phishing-service-platform-labhost]] (source summary), [[labhost-phishing-as-a-service-takedown-2024]] (operation, case_id `CYB-2024-202`)
- Pages updated: 19 country pages (UK, US, AU, AT, BE, CA, CZ, EE, FI, IE, LT, MT, NL, NZ, PL, PT, RO, ES, SE) operations_participated; 7 org pages (europol-ec3, uk-metropolitan-police, fbi, us-secret-service, australia-afp, canada-rcmp, ireland-garda) operations_participated; [[online-fraud-ic]] + [[malware-ic]] (notable_operations + sources + body Reference rows); [[domain-seizure]], [[informal-cooperation]] (operations_using); related_operations cross-links to [[operation-cronos-phase1]], [[operation-endgame]], [[latvia-sim-box-cybercrime-as-a-service-takedown-2025]], [[2bagoldmule-qqaazz]]; index/master indexes reconciled.
- Key findings: 14-17 April 2024 action days produced 70 searches globally; 37 arrests; 4 UK arrests including LabHost's original developer. LabHost = $249/month phishing-as-a-service with 170+ fake-website templates and the LabRat 2FA-capture campaign-management tool. ~10,000 LabHost users worldwide; ≥40,000 LabHost-linked phishing domains. UK Met-led with Europol EC3 + J-CAT support; September 2023 Europol involvement; operational sprint at HQ; action-phase Europol specialist deployed to Dutch National Police. First wiki record of the J-CAT (Joint Cybercrime Action Taskforce) as a discrete IC mechanism class; most fully-articulated 19-country action-day enumeration in the wiki for a phishing-as-a-service takedown (5 Eyes + EU + EFTA scope).

## [2026-05-09] ingest | NCA UK 2025-07-11 — India CBI Noida tech-support scam takedown (CBI-NCA-FBI-Microsoft 4-party action)
- Source: `raw/press-releases/2025-07-11_nca-uk_major-scam-centre-targeted-after-international-operation.md` (NCA press release; tier-1 primary)
- Pages created: [[2025-07-11_nca-uk_major-scam-centre-targeted-after-international-operation]] (source summary), [[india-cbi-noida-tech-support-scam-takedown-2025]] (operation, case_id `CYB-2025-206`)
- Pages updated: [[india]], [[united-kingdom]], [[united-states]] (operations_participated); [[cbi-india]], [[uk-nca]], [[fbi]], [[city-of-london-police]], [[microsoft]] (operations_participated); [[online-fraud-ic]] (notable_operations + sources + body Reference row); [[public-private-cooperation]], [[informal-cooperation]] (operations_using); related_operations cross-links to [[uk-nigeria-meta-scam-centre-disruption-2026]], [[korea-cambodia-philippines-73-extradition-2026]]; index/master indexes reconciled.
- Key findings: 2025-07-07 CBI raid on Noida tech-support scam call-centre after 18-month four-party (CBI / NCA / FBI / Microsoft) collaboration. 2 arrests. £390,000+ UK losses across 100+ UK victims; US citizens also targeted. Tactics: Microsoft-impersonation pop-ups, spoofed phone numbers, multi-country VoIP routing. First wiki record of NCA International Liaison Officer network (US, Delhi, Washington DC) as primary intelligence-sharing channel + UK-US operational arrangement on call-centre fraud (2024) as foundational bilateral instrument. Demonstrates CBI-as-action-day-lead pattern in a Western-LE-supported transnational cooperation, complementing the wiki's Operation Chakra series.

## [2026-05-09] ingest | USAO-WDTX 2024-12-18 — US v. Sokolovsky / Raccoon Infostealer (NL-IT-US joint dismantle + Netherlands extradition)
- Source: `raw/press-releases/2024-12-18_doj-wdtx_ukrainian-national-sentenced-raccoon-infostealer.md` (USAO-WDTX press release; tier-1 primary)
- Pages created: [[2024-12-18_doj-wdtx_ukrainian-national-sentenced-raccoon-infostealer]] (source summary), [[us-v-sokolovsky-raccoon-infostealer]] (case)
- Pages updated: [[united-states]], [[netherlands]], [[italy]], [[ukraine]] (notable_cases); [[fbi]], [[us-doj]] (notable_cases); [[malware-ic]] (notable_cases + sources + body Reference row); [[extradition]] (cases_using); index/master indexes reconciled.
- Key findings: Mark Sokolovsky (28, Ukrainian national; aliases Photix / raccoonstealer / black21jack77777) sentenced 2024-12-18 to 60 months federal prison plus USD 23,975 forfeiture and ≥USD 910,844.61 restitution on one count of conspiracy to commit computer intrusion. March 2022: arrested by Dutch authorities concurrent with FBI + Italy + Netherlands joint dismantle of Raccoon Infostealer infrastructure. February 2024: extradited from Netherlands to US (24-month gap during contested-extradition appeal). October 2024: guilty plea. Raccoon Infostealer was a malware-as-a-service operation leased at ~USD 200/month in cryptocurrency that compromised 52M+ user credentials worldwide. First wiki record of an explicit FBI + Italy + Netherlands joint infrastructure-dismantle for a MaaS operation paired with single-defendant Schengen-region extradition prosecution.

## [2026-05-09] ingest | IRS-CI 2026-03-30 — Operation Token Mirrors (FBI/IRS-CI crypto wash-trading undercover op, US-Singapore extradition)
- Source: `raw/press-releases/2026-03-30_irs-ci_ten-foreign-nationals-charged-crypto-market-manipulation.md` (IRS-CI press release, tier-1 primary)
- Pages created: [[2026-03-30_irs-ci_ten-foreign-nationals-charged-crypto-market-manipulation]] (source summary), [[operation-token-mirrors-2026]] (operation, case_id `CYB-2026-038`)
- Pages updated: [[united-states]], [[singapore]] (operations_participated); [[fbi]], [[office-of-international-affairs]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); [[extradition]], [[mlat-process]] (operations_using); index/master indexes reconciled.
- Key findings: 3 federal grand-jury indictments (Gotbit / Vortex / Contrarian-Antier) returned across 2025 against 10 foreign-national executives + employees of cryptocurrency 'market maker' firms. FBI undercover op in which the FBI itself created cryptocurrency tokens to bait wash-trading. 5 arrests effected (Tsao @ JFK 2025-03-30; Popov @ SFO; Gora + Singh + Sharma in Singapore 2025-10-02 → extradited to US). 2 guilty pleas before announcement (Tsao 2025-06-02; Popov 2026-02-10). USD 1M+ crypto seized to date. First wiki record of Singapore-as-extradition-source for a US-led cryptocurrency-fraud prosecution; first wiki record of FBI undercover-token creation methodology as an IC mechanism class.

## [2026-05-09] ingest | Europol 2026-04-28 — Black Axe Switzerland takedown (Zurich-led, 10 arrests, CH-DE)
- Source: `raw/press-releases/2026-04-28_europol_black-axe-switzerland-10-arrests.md` (Europol newsroom press release; tier-1 primary)
- Pages created: [[2026-04-28_europol_black-axe-switzerland-10-arrests]] (source summary), [[black-axe-switzerland-takedown-2026]] (operation, case_id `CYB-2026-037`)
- Pages updated: [[switzerland]], [[germany]] (operations_participated); [[europol-ec3]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); related_operations cross-links to [[operation-jackal]], [[operation-jackal-iii]], [[black-axe-bec-2021]]; index/master indexes reconciled.
- Key findings: Zurich-led (Staatsanwaltschaft II Zürich + Kantonspolizei + Stadtpolizei + 5 other Swiss cantons) action day on 2026-04-28 with German support (Bavarian State Criminal Police Office); 10 arrests including Black Axe "Regional Head" for Southern Europe; predicate offences are romance scams + other cyber-fraud + money laundering, with damages in millions of CHF. Europol contributed information analysis and a data sprint held in Madrid. First wiki record of the @ON Network (Project ISF4@ON, EU-funded) led by the Italian Antimafia Investigation Directorate (DIA) as an analytical-support mechanism for a non-Italian Black Axe action day. Switzerland (non-EU) acting as action-day lead with a single named EU participating country (Germany) is a novel pattern in the Black Axe corpus.

## [2026-05-09] ingest | Eurojust 2025-11-04 — €600M cryptocurrency money-laundering takedown (FR-BE-CY-DE-ES, JIT-anchored)
- Source: `raw/press-releases/2025-11-04_eurojust_600m-cryptocurrency-money-laundering-takedown.md` (Eurojust press release, tier-1 primary)
- Pages created: [[2025-11-04_eurojust_600m-cryptocurrency-money-laundering-takedown]] (source summary), [[eurojust-600m-crypto-money-laundering-takedown-2025]] (operation, case_id `CYB-2025-205`)
- Pages updated: [[france]], [[belgium]], [[cyprus]], [[germany]], [[spain]] (operations_participated); [[eurojust]], [[france-gendarmerie]] (operations_participated); [[online-fraud-ic]], [[money-laundering-ic]] (notable_operations + sources + body Reference rows); [[eurojust-100m-crypto-investment-fraud-takedown-2025]] (related_operations cross-link); index/master indexes reconciled.
- Key findings: France-Belgium JIT extended via Eurojust coordination meetings to non-JIT jurisdictions (Cyprus, Germany, Spain) for synchronised 2025-10-27 / 2025-10-29 action days — 9 arrests at home addresses, EUR 800k bank / EUR 415k crypto / EUR 300k cash frozen, ~EUR 600M laundered through dozens of fake crypto-investment platforms with social-media / cold-call / fake-celebrity recruitment. Pairs structurally with the September-2025 €100M Eurojust crypto-investment-fraud takedown to evidence a recurring 2025 EU JIT-anchored crypto-investment-fraud enforcement model.

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


## [2026-05-09] ingest | DOJ 2026-02-20 — U.S. v Dragomir (Romanian Initial-Access Broker)
- Source: raw/press-releases/2026-02-20_justice-gov_romanian-national-pleads-guilty-selling-access-oregon-state.md (DOJ Press Release 26-171, full-text via TLS-spoof)
- Pages created: wiki/cases/us-v-dragomir-romanian-iab.md, wiki/sources/2026-02-20_justice-gov_romanian-national-pleads-guilty-selling-access-oregon-state.md
- Pages updated: 2 country pages (US, RO — `notable_cases`), 4 organization pages (us-doj, fbi, office-of-international-affairs, romania-public-ministry — `notable_cases`), 1 crime-type page (hacking-ic — `notable_cases` + sources). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Catalin Dragomir, 45, Romanian national formerly of Constanta, pleaded guilty 2026-02-19 in D.Or. to one count of obtaining information from a protected computer and one count of aggravated identity theft (max 5y + mandatory 2y consecutive). Sentencing scheduled 2026-05-26.
  - US-Romania bilateral extradition: arrest November 2024 in Romania → US custody January 2025 (~2-month transit, materially faster than the comparable US-Italy / US-Spain / US-Georgia bilateral extradition pathways).
  - IAB conduct documented in DOJ-charging language: gained unauthorized access to a computer on the network of an Oregon state government office in June 2021, then sold the access (with samples of personal identifying information for prospective buyers); also sold access to numerous other US-victim networks for cumulative losses of at least USD 250,000.
  - First wiki-recorded US-Romania bilateral extradition pathway record. Names the Romanian Ministry of Justice's Directorate for International Law and Judicial Cooperation as the operational counterpart for DOJ Office of International Affairs.
  - Private-sector cooperation partner: Darkweb IQ named in the DOJ release as having assisted the investigation.


## [2026-05-09] enrichment | DOJ USAO-MD 2026-03-04 — U.S. v Ptitsyn (Phobos administrator, Korea-extradited) — KOREA-LED EXTRADITION TO US
- Source: raw/press-releases/2026-03-04_justice-gov-md_russian-ransomware-administrator-pleads-guilty-phobos.md (DOJ USAO-Maryland press release, full-text via TLS-spoof; quotes from US Attorney Hayes, AAG Duva, AD Leatherman, SAC Paul preserved verbatim)
- Pages updated: wiki/cases/us-v-evgenii-ptitsyn.md (replaced thin auto-stub with full case record — case status moved from "prosecuted" to "pleaded-guilty", participating-jurisdictions expanded from US-only to US + South Korea + Russia + UK + Japan + Spain + Belgium + Poland + Czech Republic + France + Romania, defendant nationality and 20-year statutory maximum recorded, sentencing scheduled 2026-07-15); wiki/sources/2026-03-04_justice-gov-md_russian-ransomware-administrator-pleads-guilty-phobos.md created. 11 country pages and 4 organization pages backlinked via `notable_cases`; 2 crime-type pages backlinked.
- Key findings:
  - **Korea-led extradition of a Russian ransomware administrator to the US** — Evgenii Ptitsyn (43, Russian) was extradited from South Korea in November 2024 to face Phobos administrator-tier prosecution in the District of Maryland. **First wiki-recorded instance of Korean-led extradition of a Russian ransomware administrator to the United States.**
  - Phobos cohort scale (verbatim from plea): 1,000+ public and private entities worldwide victimised, USD 39 million+ extorted in ransom payments since November 2020.
  - Phobos RaaS financial-flow architecture documented in DOJ-charging language: each Phobos deployment assigned a unique alphanumeric string matching its decryption key; affiliates paid decryption-key fees from unique cryptocurrency wallets; from December 2021 to April 2024 these fees flowed to a wallet Ptitsyn controlled, plus Ptitsyn received a portion of ransom payments made by victims.
  - 10-country cooperation roster (verbatim): South Korea, United Kingdom, Japan, Spain, Belgium, Poland, Czech Republic, France, Romania, plus Europol and the US Department of Defense Cyber Crime Center. Korea named first in the verbatim roster — one of the wider multilateral rosters in the wiki for a single ransomware-administrator case.
  - This case is exceptionally project-relevant for the Korean cybercrime IC corpus: it adds a fifth distinct Korean cooperation data point in the 2024-2026 window alongside the 2025-11-01 Korea-China MOU, 2025-11-10 Korea-Cambodia 코리아전담반 MOU, 2026-03-03 Korea-Philippines MOU, and 2026-04-27 Korea-Cambodia-Philippines 73-person extradition.


## [2026-05-09] ingest | DOJ 2026-05-07 — DPRK IT worker laptop farms US sentencings (Knoot/Prince) — KOREA-RELEVANT (US-ROK joint advisory)
- Source: raw/press-releases/2026-05-07_justice-gov_two-us-nationals-sentenced-dprk-it-worker-laptop-farms.md (DOJ Press Release 2026-05-07, full-text via TLS-spoof)
- Pages created: wiki/cases/us-v-knoot-prince-dprk-laptop-farms-2026.md, wiki/sources/2026-05-07_justice-gov_two-us-nationals-sentenced-dprk-it-worker-laptop-farms.md, wiki/countries/north-korea.md (stub — first wiki entry for North Korea / DPRK)
- Pages updated: 6 country pages (US, KP, CN, MX, NL, KR — `notable_cases`), 2 organization pages (us-doj, fbi — `notable_cases`), 2 crime-type pages (online-fraud-ic, hacking-ic — `notable_cases` + sources). South Korea sources list also updated with the 2026-05-07 DOJ source. Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Two US-based "laptop farmers" — Matthew Isaac Knoot (Nashville, TN; MDTN, sentenced 2026-05-01) and Erick Ntekereze Prince (New York; SDFL, sentenced 2026-05-07) — each received 18 months for facilitating DPRK remote IT worker schemes. Combined schemes generated USD 1.2M+ revenue for DPRK and impacted nearly 70 US victim companies.
  - 7th and 8th US-based laptop-farmer sentencings in 5 months under the joint NSD + FBI **DPRK RevGen: Domestic Enabler Initiative**.
  - Co-conspirator structure: Mexican national Pedro Ernesto Alonso de los Reyes in Netherlands custody awaiting US extradition; DPRK nationals Jin Sung-il and Pak Jin-Song fugitives.
  - **Korean angle**: DOJ release explicitly references the **October 2023 joint US-ROK guidance** on DPRK IT worker threats — public-record bilateral US-Korea cooperation reference embedded in a non-Korean-victim DPRK-revenue-generation prosecution.
  - First wiki entry for North Korea / DPRK as a country page (stub) — establishes DPRK as a non-cooperative threat-source state in the public IC corpus.
  - Verbatim DPRK IT worker collective revenue: hundreds of millions of dollars annually; individual workers up to USD 300,000/year for designated entities including DPRK Ministry of Defense.


## [2026-05-09] ingest | DOJ 2025-09-09 — U.S. v Tymoshchuk (LockerGoga/MegaCortex/Nefilim administrator-tier)
- Source: raw/press-releases/2025-09-09_justice-gov_lockergoga-megacortex-nefilim-ransomware-administrator-tymoshchuk-charged.md (DOJ Press Release 25-929, full-text via TLS-spoof)
- Pages created: wiki/cases/us-v-tymoshchuk-nefilim-megacortex-lockergoga.md, wiki/sources/2025-09-09_justice-gov_lockergoga-megacortex-nefilim-ransomware-administrator-tymoshchuk-charged.md
- Pages updated: 10 country pages (US, UA, FR, CZ, DE, LT, LU, NL, NO, CH — `notable_cases`), 5 organization pages (us-doj, fbi, office-of-international-affairs, europol-ec3, eurojust — `notable_cases`), 2 crime-type pages (ransomware-ic — `notable_cases` + sources; hacking-ic — `notable_cases`), and 1 sister case (us-v-stryzhak-nefilim — `related_operation` now points to this admin-tier case). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - Volodymyr Viktorovich Tymoshchuk (Ukrainian, aliases deadforz/Boba/msfv/farnetwork) charged in EDNY superseding indictment with administering LockerGoga/MegaCortex/Nefilim ransomware schemes from December 2018 to October 2021. Fugitive; US State Department TOC reward up to USD 11 million.
  - Administrator-tier counterpart to the Stryzhak affiliate-tier prosecution. The two cases together provide the most complete public-record administrator-affiliate cross-attribution for a single ransomware-as-a-service cluster in the wiki corpus. The 20% administrator/affiliate revenue split is documented in both releases.
  - Multilateral cooperation roster: 9 countries (FR, CZ, DE, LT, LU, NL, NO, CH, UA) plus Europol and Eurojust via ICHIP The Hague.
  - 250+ US victims plus hundreds worldwide; named victim countries: US, France, Germany, Netherlands, Norway, Switzerland.
  - September 2022 No More Ransomware Project decryption-key release for LockerGoga + MegaCortex documented as concrete public-record outcome of the underlying multilateral investigation, complementing the named-suspect indictment approach.
  - Charges: 7 counts including 2 conspiracy counts, 3 intentional-damage counts, 1 unauthorized-access count, and 1 threat-to-disclose-confidential-information count.


## [2026-05-09] ingest | Europol 2025-10-17 — Latvia SIM-box Cybercrime-as-a-Service network takedown
- Source: raw/press-releases/2025-10-17_europol_cybercrime-as-a-service-sim-box-takedown-latvia.md (Europol newsroom press release; verbatim body captured from `window.SERVER_DATA.body` JSON via TLS-spoof + JSON-extraction)
- Pages created: wiki/operations/latvia-sim-box-cybercrime-as-a-service-takedown-2025.md, wiki/sources/2025-10-17_europol_cybercrime-as-a-service-sim-box-takedown-latvia.md
- Pages updated: 4 country pages (LV, AT, EE, FI — `operations_participated`), 3 organization pages (europol-ec3, eurojust, finland-nbi — `operations_participated`), 2 crime-type pages (online-fraud-ic, hacking-ic — `notable_operations` + sources). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - October 2025 action day in Latvia dismantled a SIM-box cybercrime-as-a-service network. JIT (Joint Investigation Team) partners: Austria, Estonia, Latvia. Supporting jurisdiction: Finland. Coordinated by Europol + Eurojust with the Shadowserver Foundation as private-sector partner.
  - Action-day results: 5 arrests, 26 searches, ~1,200 SIM-box devices seized (operating 40,000 SIM cards), hundreds of thousands of further SIM cards seized, 5 servers, 2 websites taken down (gogetsms.com, apisim.com), EUR 431,000 + USD 333,000 frozen, 4 luxury vehicles seized.
  - Operational scale: more than 49 million online accounts allegedly created via the illegal SIM-box service; telephone numbers from 80+ source-countries.
  - Title-vs-body arrest count discrepancy noted: title says "7 arrested" but body says "5 individuals arrested" on the action day; the 5-figure used for `results.arrests` and the 7-figure flagged.
  - Crime types facilitated by the network include phishing, smishing, fraud, extortion, migrant smuggling, CSAM distribution, daughter-son scam, investment fraud, fake shops, fake bank websites, and fake-police-officer schemes targeting Russian-speaking victims.
  - First wiki record explicitly capturing a JIT 4-jurisdiction CaaS-takedown pattern with a private-sector technical partner. Korean involvement not named.


## [2026-05-09] ingest | Eurojust 2025-09-23 — €100M cryptocurrency investment fraud takedown (Spain-Lithuania JIT, 23-country corpus)
- Source: raw/press-releases/2025-09-23_eurojust_100m-cryptocurrency-investment-fraud-takedown.md (Eurojust newsroom press release, full-text via TLS-spoof)
- Pages created: wiki/operations/eurojust-100m-crypto-investment-fraud-takedown-2025.md, wiki/sources/2025-09-23_eurojust_100m-cryptocurrency-investment-fraud-takedown.md
- Pages updated: 8 country pages (ES, PT, IT, RO, BG, LT, DE, FR — `operations_participated`), 3 organization pages (eurojust, europol-ec3, romania-diicot — `operations_participated`), 2 crime-type pages (online-fraud-ic, money-laundering-ic — `notable_operations` + sources). Indexes regenerated via tools/reconcile_indexes.py.
- Key findings:
  - 5 arrests including the alleged main perpetrator. EUR 100M+ defrauded from 100+ victims in Germany, France, Italy, and Spain. Active since at least 2018.
  - 23-country corpus (proceeds-laundering or victim jurisdictions); 6 named action-day countries (Spain, Portugal, Italy, Romania, Bulgaria, Lithuania).
  - Lithuanian bank accounts identified as the primary proceeds-laundering route — adds to wiki documentation of Lithuanian financial-system exposure to EU-wide crypto-fraud schemes alongside the Tymoshchuk Lithuania-cooperation track record.
  - Cooperation mechanism architecture: Spain-Lithuania JIT joined by Europol; European Arrest Warrant + European Investigation Orders + freezing orders executed under Eurojust coordination; Europol cryptocurrency-expert deployed in-country to Portugal for action-day crypto-asset seizure.
  - One of the most fully-articulated multi-instrument JIT records in the wiki corpus for a single operation, layering JIT + EAW + EIO + freezing orders + cryptocurrency-expert deployment within a single joint action day.
  - Korean involvement not named.

## [2026-05-09] ingest | Operation OCTOPUS — Czech-Ukrainian investment-fraud call-centre takedown (Kyiv, 17 arrests, CZK 33M)
- Source: raw/press-releases/2025-12-16_policie-cz_operation-octopus-investment-fraud-takedown-kyiv.md (Policie ČR / NCTEKK, kpt. Jakub Vinčálek; cs)
- Pages created: wiki/sources/2025-12-16_policie-cz_operation-octopus-investment-fraud-takedown-kyiv.md, wiki/operations/operation-octopus-investment-fraud-czechia-ukraine-2025.md (provisional, source_count=1)
- Pages updated: organizations (eurojust, czechia-police, ukraine-sbu, ukraine-police), countries (czech-republic, ukraine), crime-types (online-fraud-ic, organized-crime-ic, money-laundering-ic), mechanisms (joint-investigation-team, eurojust-coordination-meeting, search-seizure, electronic-evidence, asset-freezing), related operations (ukraine-fraudulent-call-centres-takedown-2025, dnipro-fraudulent-call-centre-takedown-2026, operation-eur-3m-online-investment-fraud-2025)
- Key findings:
  - Bilateral CZ-UA JIT under Eurojust coordination targeting investment-fraud call-centre in Kyiv. Action day 2025-11-20: 19 house searches, 17 detentions, ~CZK 33M seized.
  - 138 identified victims, CZK 43M confirmed losses; principal organizer named as 31-year-old from Donetsk region.
  - Operationally distinct from Operation CONNECT (already in wiki) despite joint announcement: different JIT membership (CZ-UA vs. CZ-UA-LT-LV), different fraud scheme (investment fraud vs. police/bank impersonation), different action day (2025-11-20 vs. 2025-12-09).
  - Provisional record: published below preferred source_count>=5 threshold because tier-1 primary uniquely names this branch.

## [2026-05-09] ingest | Operation OTF GRIMM (Operational Taskforce GRIMM) — Sweden-led Europol VaaS taskforce one-year anniversary
- Source: raw/press-releases/2026-04-29_europol_otf-grimm-one-year-anniversary-280-arrests.md (Europol ESOCC; en)
- Pages created: wiki/sources/2026-04-29_europol_otf-grimm-one-year-anniversary-280-arrests.md, wiki/operations/operation-otf-grimm.md (provisional, source_count=1)
- Pages updated: 11 country pages (BE+DK+FI+FR+DE+IS+NL+NO+ES+SE+UK), 11 agency pages (sweden-police, europol-ec3, belgium-federal-police, denmark-police, finland-nbi, france-gendarmerie, germany-bka, netherlands-politie, norway-kripos, spain-national-police, uk-nca), crime-types (organized-crime-ic, cyberstalking-ic), mechanisms (european-arrest-warrant, informal-cooperation, public-private-cooperation, extradition).
- Key findings:
  - First wiki record of "violence-as-a-service" (VaaS) as a cyber-investigative subject — online recruitment-and-assignment surface for physical violence (encrypted-messaging, gaming platforms, mainstream social media).
  - 280 arrests across 11 participating countries in 12 months (193 in first 6 months).
  - 1,400+ individuals identified as VaaS-linked; ~14,000 digital recruitment accounts mapped.
  - Three OTF GRIMM-linked fugitives newly published on EU Most Wanted (2 Swedish, 1 German).
  - Tier-1 release does NOT designate OTF GRIMM as a JIT and does NOT name Eurojust — taskforce is structured as a Europol Operational Taskforce (ESOCC-coordinated) rather than a JIT/Eurojust instrument. Cross-border enforcement spine: domestic powers + EAW + Europol-channelled police-to-police + provider-side cooperation (Google/Meta/TikTok/Snapchat).
  - Six-month role taxonomy (193): 63 perpetrators / 84 recruiters / 40 enablers / 6 instigators — enforcement currently denser at operational tier than principal tier.

## [2026-05-09] ingest | Hellenic Police DAOE crypto-investment Ponzi takedown — €14.5M, 12 arrests, 8 countries
- Source: raw/press-releases/2026-03-06_astynomia-gr_daoe-crypto-investment-fraud-takedown.md (Hellenic Police HQ Directorate for the Confrontation of Organised Crime / Δ.Α.Ο.Ε.; el)
- Pages created: wiki/sources/2026-03-06_astynomia-gr_daoe-crypto-investment-fraud-takedown.md, wiki/operations/greek-daoe-crypto-investment-fraud-2026.md (provisional, source_count=1)
- Pages updated: 8 country pages (GR+FR+DE+MT+UK+IE+DK+BG), crime-types (online-fraud-ic, money-laundering-ic, organized-crime-ic), mechanisms (european-investigation-order, mutual-legal-assistance, search-seizure), 3 related operations (albania-austria-call-centre-investment-fraud-2026, operation-eur-100m-crypto-investment-fraud-2025, operation-eur-600m-crypto-scam-network-2025).
- Key findings:
  - Single national-led organised-crime takedown exercising **both EIO and classical MLA in parallel** — EIO to FR/DE/MT (EU Member States), MLA to UK (post-Brexit) / IE (EIO opt-out) / DK (EIO opt-out) — confirms continued necessity of MLA channel even within European judicial space.
  - 12 arrests; €14.5M total illicit gain; 73 identified victims; €760,900 confirmed direct losses; >USD 2M digital-currency circulation on seized devices.
  - Combined financial-supervisory authority (Hellenic Capital Market Commission) and police organised-crime unit on action day — on-scene certification-status assessment alongside law-enforcement seizure.
  - Ponzi structure documented: 4-person leadership / 3 senior recruiters / 7 operational + support; 21 internal ranks; 90-day in-house "academy"; rebranding pattern.
  - Greek FIU traced 4 offshore companies in Bulgaria linked to 2 organisation members.
  - First wiki record sourced from astynomia.gr — confirms curl_cffi chrome120 viable bypass for Hellenic Police Cloudflare wall (LESSONS L11/L20).
- LESSONS update: L11 working pattern confirmed for astynomia.gr — chrome120 succeeded on first try, no chrome124 fallback or Wayback needed.

## [2026-05-09] ingest | NPA AFU R43M restraint vs Bryanston call-centre fraud syndicate (South Africa, POCA s.26)
- Source: raw/press-releases/2026-04-21_npa-gov-za_afu-r43m-restraint-bryanston-call-centre-syndicate.md (National Prosecuting Authority of South Africa; en)
- Pages created: wiki/sources/2026-04-21_npa-gov-za_afu-r43m-restraint-bryanston-call-centre-syndicate.md, wiki/cases/bryanston-call-centre-investment-fraud-syndicate-2026.md (provisional, source_count=1)
- Pages updated: 6 country pages (ZA+IL+AU+NZ+CA+US), south-africa-hawks, south-africa-saps, three crime-types (online-fraud-ic, money-laundering-ic, organized-crime-ic), two mechanisms (asset-freezing, asset-recovery), concept (extraterritorial-jurisdiction, applied_in_cases backlink).
- Key findings:
  - First wiki record sourced from npa.gov.za — South African National Prosecuting Authority publishes Asset Forfeiture Unit press releases as tier-1 IC primary on the asset-recovery side of cross-border fraud.
  - POCA s.26 provisional restraint of R43.9M (~USD 2.4M) — multiple Gauteng immovable properties + luxury vehicle inventory (Mercedes-Benz A45S AMG, Aston Martin DB9, VW Golf 8 GTI, Toyota Fortuner, Jaguar E-Pace, Ford Ranger, Toyota Hilux).
  - "International Israeli syndicate" Bryanston call centres targeting AU/NZ/CA/US victims — fact pattern is transnational but tier-1 source describes the asset-restraint phase as domestic ZA inter-agency (DPCI + NPA SCCU + NPA AFU) only.
  - Cooperation channel: domestic-only at the visible asset-restraint phase; foreign LE participation (UK NCA, US DHS/Secret Service, AFP, INTERPOL Project Jackal) appears in non-tier-1 reporting but is NOT asserted on the case page per L19.
  - 27 January 2026 arrest action; 26 February 2026 restraint order; 14 April 2026 execution; 4 June 2026 next criminal-case date (Palm Ridge Magistrates' Court).
- Local build: web/build_static.py executed successfully at iter 90 milestone (last build was iter 80).

## [2026-05-09] ingest | Hungary-Romania Discord swatting/doxing joint investigation
- Source: raw/press-releases/2026-01-26_police-hu_swatting-doxing-hungary-romania-joint-investigation.md (Hungarian National Police KR NNI Cybercrime Combatting Department; hu)
- Pages created: wiki/sources/2026-01-26_police-hu_swatting-doxing-hungary-romania-joint-investigation.md, wiki/operations/hungary-romania-swatting-doxing-discord-2026.md (provisional, source_count=1)
- Pages updated: 2 country pages (HU, RO), romanian-police agency, cyberstalking-ic crime-type, three mechanisms (informal-cooperation, search-seizure, electronic-evidence), two related operations (operation-bremerton-..., operation-us-v-california-teenager).
- Key findings:
  - First wiki record sourced from police.hu (curl_cffi chrome120 bypass for HU national police Cloudflare-403 wall — confirms LESSONS L11 working pattern for Hungarian police domain).
  - Bilateral HU-RO informal cooperation pattern with **direct cross-border physical participation by Hungarian KR NNI cyber investigators in Bihor County (Romania) search alongside Romanian investigators** — structurally novel pattern not previously documented in wiki for HU-RO axis.
  - 6-month investigation (Jul 2025 → 20-Jan-2026 raid); 4 suspects ages 16-20 (3 HU + 1 RO Bihor County); 17-year-old Romanian charged with terrorcselekmény (terrorist act) for swatting-style bomb threats — illustrates how **bomb-threat-style swatting can rise to terrorism prosecutions** in EU member states.
  - Discord platform disputes documented as pre-cursor pattern for swatting/doxing — first such pattern record in wiki.
  - Counter Terrorism Centre (TEK) participation during reconnaissance phase rather than only after attribution.
  - No Eurojust/Europol involvement named — informal bilateral with overlapping participation rather than sequential MLA/JIT.

## [2026-05-09] ingest | NBI Parañaque US-impersonation cyber-scam takedown — Li Zhenjie 2025
- Source: raw/press-releases/2025-11-28_nbi-gov-ph_paranaque-cyber-scam-li-zhenjie-us-impersonation.md (NBI Cybercrime Division Philippines, OIC Director Atty. Angelito DLP Magno; en)
- Pages created: wiki/sources/2025-11-28_nbi-gov-ph_paranaque-cyber-scam-li-zhenjie-us-impersonation.md, wiki/operations/nbi-paranaque-cyber-scam-li-zhenjie-us-impersonation-2025.md (provisional, source_count=1)
- Pages updated: countries/philippines, three crime-types (online-fraud-ic, extortion-ic, identity-theft), two mechanisms (search-seizure, electronic-evidence), two related operations (seoul-eastern-clark-philippines-voice-phishing-arrest-extradition-2026, korea-cambodia-philippines-73-extradition-2026).
- Key findings:
  - First wiki record sourced from nbi.gov.ph — Philippine NBI Cybercrime Division publishes English-language tier-1 IC press releases.
  - Single-state takedown of outbound transnational scam: Chinese national (Li Zhenjie) operating from Parañaque condo, impersonating New Haven PD (Connecticut, USA) + FBI Washington over spoofed numbers, demanding USD 3,000-5,000 in cryptocurrency to alias "GENERAL" from US victims.
  - Procedural fast-path documented: WSSECD (Warrant to Search, Seize, and Examine Computer Data) under Philippine Rule on Cybercrime Warrants (A.M. No. 17-11-03-SC) enabled 1-day turnaround between issuance (2025-11-20) and execution/arrest (2025-11-21). Relevant for future US MLAT or preservation-request workflow under Budapest Convention.
  - RA 12010 (AFASA, Anti-Financial Account Scamming Act) §4(b)(1) Social Engineering Schemes invoked in relation to RA 10175 (Cybercrime Prevention Act 2012) — first wiki record of AFASA application.
  - **Operational chain in tier-1 release purely domestic Philippine** — no foreign LE counterpart named. Per L19, participating_countries kept to philippines only; cross-border conduct (US victims, US-impersonated agencies, Chinese national) recorded in body and missing_fields without IC-cooperation assertion.
- New LESSONS entry: L22 — nbi.gov.ph requires HTTP plain (HTTPS WRONG_VERSION_NUMBER fail). Fallback order updated: chrome120 → chrome124 → **HTTP plain** → Wayback → ABORT.

## [2026-05-09] ingest | Latvia €2M vishing money-mule case — 4-jurisdiction (LV+EE+DE+UA) Eurojust-coordinated
- Source: raw/press-releases/2026-03-18_prokuratura-lv_telephone-fraud-2-million-euros-170-money-mules.md (Latvijas Republikas prokuratūra; lv)
- Pages created: wiki/sources/2026-03-18_prokuratura-lv_telephone-fraud-2-million-euros-170-money-mules.md, wiki/operations/latvia-phone-fraud-money-mule-network-takedown-2026.md (provisional, source_count=1)
- Pages updated: 4 country pages (LV, EE, DE, UA), latvia-state-police, eurojust, two crime-types (online-fraud-ic, money-laundering-ic), three mechanisms (eurojust-coordination-meeting, extradition, asset-freezing), latvia-sim-box-cybercrime-as-a-service-takedown-2025 related op.
- Key findings:
  - First wiki record sourced from prokuratura.lv (Latvia Prosecutor General's Office) — Latvian-language tier-1 IC primary.
  - **4-jurisdiction cooperation arc** on a single vishing-plus-laundering OCG: LV (lead, victim country, prosecution) + EE (cooperation in 2024 DE detention; convicting forum for group leader) + DE (where group leader detained 2024) + UA (2 fugitives detained Ivano-Frankivsk 2026-03-12, Eurojust-supported).
  - **"Convict-in-third-state" pattern** — group leader detained in DE in cooperation with EE, then convicted in EE rather than LV. EU-internal flexibility in choosing convicting jurisdiction based on evidence center of gravity.
  - Vishing typology benchmark: police-and-bank impersonation → AnyDesk remote-access deployment → internet-banking credential exfiltration. Recorded verbatim by tier-1 prosecutorial source.
  - Money-mule downstream layer: 170+ mules, 90 recognised as suspects; 1 illegal crypto-asset exchanger sentenced >6 years (sentencing-severity precedent for laundering-conduit role distinct from call-centre operator role).
  - €2M victim losses across 35 consolidated criminal matters (2023-09 → 2024-09); €829,650 under criminal-process asset arrest.
  - 13 fraudulent call-centre operators detained; 3 LV group members each sentenced 3 years.

## [2026-05-09] ingest | Hakkari illegal-betting + qualified-fraud network — 18-province TR sweep + Sarajevo Red Notice arrest (TR+BA, 2026)
- Source: raw/press-releases/2026-03-31_anadolu-agency_hakkari-illegal-betting-fraud-network-bosnia-arrest.md (Anadolu Ajansı reproducing T.C. İçişleri Bakanlığı statement; tr)
- Pages created: wiki/sources/2026-03-31_anadolu-agency_hakkari-illegal-betting-fraud-network-bosnia-arrest.md, wiki/operations/hakkari-illegal-betting-fraud-network-bosnia-arrest-2026.md (provisional, source_count=1)
- Pages updated: countries/turkey, countries/bosnia-and-herzegovina, organizations/interpol, three crime-types (online-fraud-ic, money-laundering-ic, organized-crime-ic), three mechanisms (extradition, search-seizure, cryptocurrency-seizure).
- Key findings:
  - First wiki record sourced from aa.com.tr (Anadolu Ajansı, official Turkish state news agency reproducing T.C. İçişleri Bakanlığı statement) — first **Turkish-language tier-1 IC primary** in wiki.
  - Provincial-led Turkish cyber operation reaches intercontinental scope: **Yüksekova Cumhuriyet Başsavcılığı** (Hakkari province prosecutor's office) anchors 18-province sweep with international Red Notice extension via Türkiye **Interpol Daire Başkanlığı** rather than centralised national prosecutor.
  - Cooperation pattern: Interpol Red Notice → Sarajevo apprehension of network's technical-infrastructure architect. 52 detained in TR + 1 in BA.
  - Ministry of Interior characterises **~20 billion Turkish lira cumulative money traffic** as the highest transaction volume ever identified in a Turkish cyber-crime / fraud investigation.
  - Modus operandi documented verbatim: illegal sports-betting platforms + qualified-fraud (nitelikli dolandırıcılık) via IT systems → 24/7 panel-system back-office → third-party-account layering → crypto-asset conversion. Server and management layers explicitly attributed to Bosnia and Herzegovina.
  - Open questions per L19: BiH counterpart agency name (federal Federalna policija / MUP RS / SIPA / cantonal not specified by AA wire); specific MLA/extradition treaty instrument invoked; defendant case numbers.

## [2026-05-09] ingest | KNPA KMSAuto Lithuanian hacker — Korea-Lithuania-Georgia three-state extradition (2020-2025)
- Source: raw/press-releases/2025-12-29_korea-kr_knpa-kmsauto-lithuanian-hacker-georgia-extradition.md (경찰청 국가수사본부 사이버테러대응과 / Korea.kr 정책브리핑; ko)
- Pages created: wiki/sources/2025-12-29_korea-kr_knpa-kmsauto-lithuanian-hacker-georgia-extradition.md, wiki/operations/knpa-kmsauto-lithuanian-hacker-georgia-extradition-2025.md (provisional, source_count=1)
- Pages updated: 3 country pages (KR, LT, GE), 6 agency pages (knpa, knpa-cyber-bureau, ministry-of-justice-korea, supreme-prosecutors-office-korea, lithuania-police, interpol), malware-ic crime-type, 3 mechanisms (extradition, MLA, informal-cooperation).
- Key findings:
  - **Korea-Lithuania-Georgia three-state extradition** is the first wiki record of a fully-articulated KR-led international cyber-extradition arc with explicit Korean involvement: Lithuanian-national suspect tracked from 2020 KR-side investigation → 2024-12 LT joint search (22 items seized) → 2025-04 INTERPOL Red Notice → GE arrest at Lithuania-Georgia border on entry → 2025-12 Korea-Georgia extradition.
  - Total elapsed time: 5 years 4 months from initial case opening to extradition — longest single-suspect cyber-extradition arc currently documented in wiki.
  - **Massive distribution scale at low per-victim yield**: 2.8M KMSAuto-bundled clipper distributions across 234 ISO countries, 3,100 wallets drained in 8,400 events, ~₩1.7B (~USD 1.18M) total stolen — illustrates the long-tail clipper economy where global distribution does not translate to high per-victim losses (8 KR victims for ~₩16M).
  - **Joint task force**: KNPA + Korean MOJ + Korean SPO (대검찰청) jointly filed Korea-Georgia extradition request — three-agency Korean side coordination, not single-agency request.
  - 14 distinct crypto assets affected (BTC, LTC, ETH, XRP … DASH per source).
  - 6 third-country jurisdictions and 6 foreign crypto-related companies engaged in trace-and-attribution phase (counts only, not enumerated; flagged as open question per L19).
  - Distribution period 2020-04-08 → 2023-01-06; KNPA spokesperson 박우현 (Park Woo-hyun, 사이버수사심의관).
  - First wiki record demonstrating **Korea.kr 정책브리핑 PDF attachment as authoritative tier-1 channel** — HTML view shell carries metadata only; full body in PDF/HWPX attachment requiring separate fetch.

## [2026-05-09] ingest | Lai Châu Police + Vietnam MPS — Bokor Hill scam-cell takedown (VN+KH, 28-Oct-2025)
- Source: raw/press-releases/2025-10-29_baochinhphu-vn_lai-chau-cambodia-bokor-transnational-online-fraud-takedown.md (Báo Chính phủ — Vietnam Government Newspaper; vi)
- Pages created: wiki/sources/2025-10-29_baochinhphu-vn_lai-chau-cambodia-bokor-transnational-online-fraud-takedown.md, wiki/operations/lai-chau-cambodia-bokor-transnational-online-fraud-takedown-2025.md (provisional, source_count=1)
- Pages updated: countries/vietnam, countries/cambodia, two crime-types (online-fraud-ic, organized-crime-ic), mechanisms/informal-cooperation, three related operations (korea-cambodia-philippines-73-extradition-2026, korea-cambodia-scam-repatriation, knpa-breaking-chains-2nd-international-operation-meeting-2026).
- Key findings:
  - **First wiki record sourced from baochinhphu.vn** (Báo Chính phủ — Vietnam Government Newspaper, electronic newspaper of the Government Office of the Socialist Republic of Việt Nam) — first **Vietnamese-language tier-1 IC primary** in wiki.
  - 28-Oct-2025 joint takedown at Bokor Hill (Bokor Ecological Park, Tuek Chhou ward, Bokor city, Kampot province, Cambodia). Lead: Lai Châu Provincial Police of Việt Nam, special working group; central support from Criminal Police Department, MPS; in-Cambodia liaison via Representative Office of the MPS of Việt Nam in Cambodia.
  - Direct command: Senior Lieutenant General Nguyễn Văn Long (Deputy Minister, Head of Police Investigation Agency, MPS).
  - 59 on-site arrests (44 male, 15 female), all Vietnamese nationals; 66 total in case to date. Ringleader: Sùng Thị Mải (alias "Vi"), born 1999, Lào Cai province, Việt Nam.
  - **Hand-over pattern**: Cambodian functional forces handed over all 59 suspects + seized physical evidence to Lai Châu Provincial Police for VN-domestic prosecution (no extradition framework cited).
  - Modus: shipper / Police / Military impersonation + romance fraud (lừa đảo tình cảm). Victims: >8,000 nationwide in VN; estimated take >300 billion VND (~USD 12M at late-2025 rates).
  - Diplomatic context: takedown framed in immediate aftermath of Hà Nội Convention (UN Convention against Cybercrime) signing ceremony hosted by Việt Nam in Hà Nội on 25-26 October 2025.
  - L19 applied: Cambodian counterpart agency named only generically ("lực lượng chức năng của Campuchia"); removed `[[cambodian-national-police]]` from participating_agencies and recorded gap in missing_fields. Body prose retains the analytical inference as a hypothesis.

## [2026-05-09] ingest | US v. Szabo swatting ring sentencing — Romania-US extradition (2024-2026)
- Source: raw/press-releases/2026-04-29_us-secret-service_szabo-romania-swatting-sentenced-48-months.md (US Secret Service republishing USAO-DC; en)
- Pages created: wiki/sources/, wiki/cases/us-v-szabo-swatting-ring.md, wiki/operations/operation-us-v-szabo-swatting-ring.md (case+operation pair per existing wiki convention for prosecutions; provisional, source_count=1)
- Pages updated: countries/united-states, countries/romania, four agency pages (us-doj, us-secret-service, fbi, office-of-international-affairs), cyberstalking-ic crime-type, three mechanisms (mutual-legal-assistance, extradition, mlat-process).
- Key findings:
  - Thomasz Szabo (RO national, 27, aka "Plank"/"Jonah"/"Cypher") sentenced 2026-04-29 in USDC-DC to 48 months prison + 3 years supervised release for leading online swatting ring (late Dec 2023 → early Jan 2024) targeting 25+ Members of Congress, 6+ senior US Executive officials, 13+ senior federal LE officials, federal judges, 27+ state officials, 4 religious institutions, multiple journalists. Plus earlier personal threats: Dec 2020 NYC synagogues + Jan 2021 US Capitol explosives/President-elect.
  - **Extradited from Romania to US in November 2024**; Romanian authorities' assistance described as "critical." DOJ Office of International Affairs used MLA requests for foreign evidence.
  - First wiki record of US-RO swatting/bomb-threat extradition demonstrating US capacity to extradite a foreign national for cyber-enabled threat conduct (conspiracy + threats involving explosives) targeting US legislators on the basis of conspiracy charges rather than a single hacking-statute count.
  - In-country liaison framework documented: FBI Legat Bucharest + USSS Bucharest Resident Office as the embedded US LE presence enabling MLA-fast-tracking.
  - Multiple cooperating USAOs (WD WA, D SD, MD FL, SD FL, SD IL, ND NY) — illustrates how a swatting/bomb-threat ring with victims in many federal districts consolidates into a single DC prosecution with USAO-DC lead.
  - L19-strict applied: agent (correctly) did NOT include `[[romania-police]]` / `[[romania-diicot]]` in participating_agencies because tier-1 release names "Romanian authorities" generically; flagged in missing_fields.

## [2026-05-09] ingest | Fiscalía Colombia DECDI cripto-investment fraud takedown — Medellín hub, COP 71B (CO+CL+PE+MX)
- Source: raw/press-releases/2025-11-18_fiscalia-gov-co_red-cripto-medellin-colombia-chile-peru-71b-pesos.md (Fiscalía General de la Nación, Boletín 57752; es)
- Pages created: wiki/sources/2025-11-18_fiscalia-gov-co_red-cripto-medellin-colombia-chile-peru-71b-pesos.md, wiki/operations/fiscalia-colombia-criptoactivos-fraud-network-takedown-2025.md (provisional, source_count=1).
- Pages updated: 4 country pages (CO, CL, PE, MX), three crime-types (online-fraud-ic, money-laundering-ic, organized-crime-ic).
- Key findings:
  - **First wiki record sourced from fiscalia.gov.co** (Fiscalía General de la Nación, Colombia) — first **Spanish-language Colombian tier-1 IC primary** in wiki.
  - 14 captures by DECDI (Dirección Especializada contra los Delitos Informáticos) of an organised crypto-investment fraud network operating from Medellín 2021 → 2025-10. Aggregate criminal proceeds ~COP 71 billion (~USD 17M).
  - 4-country IC scope (countries-named-in-source): CO (jurisdiction) + CL/PE (victim countries) + MX (foreign-national alleged ringleader Alejandro Maximiliano Ronquillo Treviño alias "Daniel"). All four explicitly named in the controlling Boletín.
  - Modus benchmark: social-media advertising → telephone outreach → USD 200-250 entry deposit → fictitious dividend charts → coercion to install Anydesk/"Imperios" remote-access tools → seizure of banking credentials → withdrawal blocked. Verbatim Spanish-source modus pattern recorded for comparable LatAm crypto-fraud cases.
  - Charges (Spanish penal code): estafa por medios informáticos, hurto por medios informáticos, violación de datos personales en modalidad delito masa (Ley 1273 de 2009), concierto para delinquir, lavado de activos, enriquecimiento ilícito.
  - 3/14 to centro carcelario, 11/14 to house arrest. None accepted charges.
  - L19-strict applied: no Colombian agency wikilinks (Fiscalía, DECDI, Policía Nacional, AMERIPOL) added to participating_agencies because no organisation pages exist in wiki and stub-creation barred during ingest. Operation codename "Operación Dominó" and Israeli alleged co-ringleader Boaz Iaakok Derra appear in secondary press only — flagged in missing_fields, not asserted.

## [2026-05-09] ingest | Italy-FBI Riccione cyber-extortion arrest (IT+US, foreign national held on US federal warrant, 2025-07-31)
- Source: raw/press-releases/2025-07-31_polizia-di-stato_riccione-arresto-cybercriminale-internazionale-khlynovskiy.md (Polizia di Stato; it)
- Pages created: wiki/sources/2025-07-31_polizia-di-stato_riccione-arresto-cybercriminale-internazionale-khlynovskiy.md, wiki/operations/italy-riccione-cyber-extortion-arrest-khlynovskiy-2025.md (provisional, source_count=1).
- Pages updated: countries (italy, united-states), agencies (italy-polizia-postale, fbi), crime-types (extortion-ic, ransomware-ic), mechanisms (extradition, informal-cooperation).
- Key findings:
  - **First wiki record sourced from poliziadistato.it** (Polizia di Stato, Italy) — first **Italian-language tier-1 IC primary** in wiki sourced directly from a Polizia di Stato release (existing italy-polizia-postale entries are via Eurojust/Europol or other channels).
  - **Bilateral US federal warrant + Italian execution** — concrete operationalisation pattern documented: US judicial authority issues federal arrest warrant → Italian Polizia Postale Cnaipic + Centro operativo per la sicurezza cibernetica Emilia-Romagna + Sezione operativa Rimini executes → suspect remanded to Italian authorities pending extradition. Cross-border extradition arc on Italian soil.
  - **Liaison-officer/embassy-expert framework explicitly credited** in tier-1 release: "particolarmente rafforzato anche grazie all'istituzione di esperti presso le rispettive ambasciate" — rare named acknowledgement of bilateral liaison-officer infrastructure as cooperation mechanism in a public release.
  - **Tourist-flow detection**: suspect arrested at Riccione hotel while on family holiday — illustrates international wanted-person notice operational effectiveness when subjects travel to MLAT-partner jurisdictions.
  - L19-strict applied: tier-1 deliberately omits suspect identity, USD totals, prison of remand. Italian regional media (Resto del Carlino, RiminiToday) reported these (Roman Khlynovskiy, 42, Kazakh; ~USD 31M; Busto Arsizio remand) but recorded only as contextual notes in raw + missing_fields. NOT asserted in frontmatter (e.g., Kazakhstan NOT in participating_countries).

## [2026-05-09] ingest | GIGN-FBI Saint-Martin crypto-hacker arrest (FR+US, USD 46M recovered, 2026-03-04)
- Source: raw/press-releases/2026-03-06_gendarmerie-interieur-gouv-fr_gign-fbi-saint-martin-cryptocurrency-hacker-arrest.md (Gendarmerie nationale, France; fr)
- Pages created: wiki/sources/2026-03-06_gendarmerie-interieur-gouv-fr_gign-fbi-saint-martin-cryptocurrency-hacker-arrest.md, wiki/operations/gign-fbi-saint-martin-cryptocurrency-hacker-arrest-2026.md (provisional, source_count=1).
- Pages updated: countries (france, united-states), agencies (france-gendarmerie-nationale, fbi), crime-types (hacking-ic, money-laundering-ic), mechanisms (extradition, search-seizure, cryptocurrency-seizure, asset-recovery, informal-cooperation).
- Key findings:
  - First wiki record sourced from gendarmerie.interieur.gouv.fr (French Gendarmerie official institutional press).
  - 24-y-o US national arrested 2026-03-04 in Saint-Martin (Caribbean overseas collectivity of FR) on US international arrest warrant for theft of ~USD 46M crypto. Joint action: ~10 GIGN operators (Antenne Guadeloupe) + 3 SR Saint-Martin investigators + 3 FBI agents. Full USD 46M recovered, EUR 250K cash, IT equipment, wallet credentials, multiple phones, 1 loaded Glock pistol seized.
  - Cooperation channel: FBI → COMGEND Saint-Barthélemy/Saint-Martin → SR "cellule internationale" under parquet général de Guadeloupe. Caribbean tri-national geography (FR overseas + UK + NL) noted but UK/NL roles in 2026-03-04 action only "local partners" (not asserted in participating_countries per L19).
  - 100% asset-recovery outcome — illustrates crypto-extortion case where recovery happens at suspect-arrest moment via wallet-credential seizure rather than blockchain-trace forensics.
  - Caribbean International Intelligence Meeting (FBI-DEA piloted) referenced as environmental context, not operational.

## [2026-05-09] iter 100 milestone integrity sweep
- Lint: HIGH=0 CRITICAL=0 MEDIUM=0 LOW=0
- check_links: broken=2 (both pre-existing LESSONS.md backlinks in unrelated bohemia-cannabia HTML — legacy)
- placeholder strings (`Z`+`ZPROT` / `>P`+`ROT[0-9]`): 0 across wiki/ + docs/
- placeholder wikilinks (literal `challenges`/`concepts`/`wikilink`/`lessons` slugs): 0
- web/build_static.py: 1580 pages built successfully
- Fixed 5 pre-existing build-pipeline bugs found during sweep:
  - 3 missing_page in greek-daoe-crypto-investment-fraud-2026 (lead_agency/coordinating_body plain-text strings auto-linked by builder → emptied frontmatter, descriptive text retained in body)
  - 2 missing_page in hungary-romania-swatting-doxing-discord-2026 + lai-chau-cambodia-bokor-transnational-online-fraud-takedown-2025 (same root cause)
- Wiki freshness audit: most-recent `updated:` distribution shows 887 pages at 2026-04-29, 1030 pages at 2026-04-26, 247 pages at 2026-05-09. The wide 4월-말~5월-9 distribution indicates most entity pages have not been bumped on `updated:` since their pre-iter-87 baseline. This is technically expected (only directly modified pages get bumped) but suggests need for a cross-cutting `last_verified` refresh in subsequent iters.
- Source-count total: 9,201 across 2,745 pages.

## [2026-05-09] ingest | Operation Toy Soldier — GRU Unit 29155 attribution + Estonia indictment (EE+US+UA, 2024-09-05)
- Source: raw/press-releases/2024-09-05_politsei-ee_gru-unit-29155-toy-soldier-cyberattacks-estonia.md (Estonian PPA; en)
- Pages created: wiki/sources/2024-09-05_politsei-ee_gru-unit-29155-toy-soldier-cyberattacks-estonia.md, wiki/operations/operation-toy-soldier-gru-29155-estonia-2024.md (provisional, source_count=1).
- Pages updated: countries (estonia, united-states, ukraine), agencies (fbi), crime-types (hacking-ic, malware-ic), mechanisms (joint-investigation-team, informal-cooperation, extradition).
- Key findings:
  - **First wiki record sourced from politsei.ee** (Estonian Police and Border Guard Board / Politsei- ja Piirivalveamet).
  - **First wiki record of multilateral nation-state attribution operation**: Joint operation Toy Soldier — 14 services across 10 states cooperated on attribution of GRU military unit 29155 (Main Directorate of the General Staff of the Armed Forces of the Russian Federation).
  - 3 Russian nationals indicted in Estonia (Yuri Denisov, Nikolay Korchagin, Vitali Shevchenko); Harju District Court issued in-absentia custody orders. FBI brought parallel charges against Denisov and Korchagin; US State Department $10M reward.
  - **State-sheltered suspect pattern** documented: when suspects are sheltered in Russia (non-cooperative state), the available pressure mechanism is in-absentia custody orders + US bounty + multilateral attribution + IGCI-style coordination. No MLAT/extradition pathway viable.
  - GRU Unit 29155 cyber activity since 2020 against Ukraine and NATO/EU member states including Estonia. Hybrid-warfare framing per Margo Palloson (DG, Estonian Internal Security Service).
  - L19-strict + L23-strict applied. Partner-state names beyond EE/US/UA (10 states / 14 services counts only) NOT asserted in participating_countries.
  - Backlinker bumped `updated:` to today on 9 touched entity pages — first iter applying user's "5/3 freshness" remediation policy.

## [2026-05-09] ingest | KZ-AM Yerevan call-centre investment fraud takedown — bilateral KZ MIA + AM Investigative Committee (2025-02-18)
- Source: raw/press-releases/2025-02-18_sputnik-kz_kazakhstan-armenia-yerevan-call-centre-cybercrime-takedown-41-detained.md (Sputnik Kazakhstan citing MIA RK; ru)
- Pages created: wiki/sources/2025-02-18_sputnik-kz_kazakhstan-armenia-yerevan-call-centre-cybercrime-takedown-41-detained.md, wiki/operations/kazakhstan-armenia-yerevan-call-centre-investment-fraud-2025.md (provisional, source_count=1).
- Pages updated: countries (kazakhstan, armenia), crime-types (online-fraud-ic, money-laundering-ic), mechanisms (joint-investigation-team, informal-cooperation, search-seizure, cryptocurrency-seizure).
- Key findings:
  - **First wiki record from sputnik.kz** (Russian-language) — first Kazakh tier-1 IC primary; Sputnik Kazakhstan reproduces verbatim MIA RK press service statement.
  - **First Central Asia / South Caucasus pairing** in wiki (KZ + AM) — closes coverage gap for post-Soviet bilateral cyber cooperation.
  - 41 detentions in two Yerevan-based call centres targeting KZ and European victims. Multinational suspect pool: AM/GE/IR/SY/LB nationalities — 5-country detainee mix without standard EU/US-led JIT framework.
  - Lead authorities (in body prose): Department for Combating Cybercrime, MIA Kazakhstan (Жандос Сүйінбай) + Main Directorate for Investigation of Especially Important Cases, Investigative Committee of Armenia.
  - Seizure inventory: 70+ computers, ~1 kg gold, 5 vehicles, USD 30K + Russian rubles + Georgian lari, one cold cryptocurrency wallet.
  - L19/L23-strict applied: agencies named in source but NOT in wiki organization corpus → described in prose only, NOT wikilinked. participating_agencies emptied (initial agent output had plain-text strings; replaced with `[]` per L23 to prevent build-pipeline dead links).
  - Total damage to KZ/European victims not quantified in source — flagged in missing_fields.

## [2026-05-09] ingest | Operation PATHFINDER — Czech NCTEKK + Ukrainian SBU bilateral JIT (Zakarpattia 2025)
- Source: raw/press-releases/2025-05-13_policie-gov-cz_uspesna-mezinarodni-operace-pathfinder.md (Policie ČR NCTEKK; cs)
- Pages created: wiki/sources/2025-05-13_policie-gov-cz_uspesna-mezinarodni-operace-pathfinder.md, wiki/operations/operation-pathfinder-czech-ukraine-investment-fraud-takedown-2025.md (provisional, source_count=1).
- Pages updated: countries (czech-republic, ukraine), agencies (czechia-police, czech-police, ukraine-sbu, eurojust), crime-types (online-fraud-ic, money-laundering-ic), mechanisms (joint-investigation-team, europol-jit, eurojust-coordination-meeting).
- Key findings:
  - **Sister operation to OCTOPUS** (already in wiki, iter 87): same NCTEKK + Ukrainian-side bilateral pattern, but PATHFINDER is the May-2025 action against Zakarpattia call-centre (vs. OCTOPUS = Nov-2025 against Kyiv investment-fraud cell). Documents the recurring CZ-UA Eurojust JIT pattern.
  - 6-month bilateral CZ-UA Eurojust JIT (preceded action days 2025-04-29 to 2025-05-02). 70 detentions. 4 main organizers charged under Ukrainian Criminal Code Art 190(5) (fraud, particularly large scale; up to 12 years + asset forfeiture).
  - **Direct on-site participation**: 4-officer Czech NCTEKK Cybercrime Department team participated directly in Ukrainian search-and-seizure in Zakarpattia. Same pattern as Hungary-Romania Discord swatting (HU officers in RO Bihor County) — bilateral cyber cooperation increasingly involves cross-border physical participation.
  - Call-centre infrastructure benchmark: 2-floor admin building, dedicated server room, physical guards, electronic alarm system, dozens of CCTV cameras. Hardened operational security typical of large fraud-as-a-service hubs.
  - Damage attribution: ≥9M CZK across ≥37 identified Czech victims; EU-wide damage in millions of EUR pending forensic analysis.
  - L19/L23-strict applied: agent backlinked czechia-police, czech-police, ukraine-sbu, eurojust correctly (all named in tier-1 source). Eurojust JIT framework, District State Prosecutor's Office in Hradec Králové (CZ), regional prosecutor's office in Zakarpattia (UA).

## [2026-05-09] ingest | CBZC Kraków money-laundering JIT — PL+ES+CZ+HU Eurojust JIT, RO suspects, 5 cash-out countries (2025-12-16)
- Source: raw/press-releases/2025-12-16_cbzc-policja-pl_international-money-laundering-jit-poland-spain-czechia-hungary.md (Polish CBZC; pl)
- Pages created: wiki/sources/..., wiki/operations/cbzc-krakow-money-laundering-jit-2025.md (provisional, source_count=1).
- Pages updated: 4 country pages (PL, ES, CZ, HU), 3 agencies (poland-police, eurojust, czechia-police), 2 crime-types (money-laundering-ic, online-fraud-ic), 5 mechanisms (joint-investigation-team, eurojust-coordination-meeting, search-seizure, asset-freezing, electronic-evidence).
- Key findings:
  - **First wiki record sourced from cbzc.policja.gov.pl** (Polish Centralne Biuro Zwalczania Cyberprzestępczości — fresh Polish-language tier-1 distinct from existing FEVER ingest).
  - **9 countries named in tier-1 source** — extraordinary IC scope: PL+ES+CZ+HU as JIT partners + RO (suspect nationality) + GR/IT/ES/BE/NL as cash-out countries. CBZC Kraków Branch leads under Prokuratura Regionalna w Krakowie.
  - Money-mule cash-out infrastructure pattern: Romanian nationals using forged identity documents (>40 seized) to obtain Polish PESEL numbers → open Polish bank accounts → receive online-fraud proceeds → cash withdrawals across 5 EU member states (GR/IT/ES/BE/NL). ~EUR 2.23M + PLN 717K laundered.
  - 12 charged, 10 in 3-month pretrial detention. Multi-country action days documented:
    - 2025-12-05 Śląskie Voivodeship: 5 RO nationals arrested
    - Czech action day: 3 CZ nationals arrested with direct CBZC Kraków + Czech police participation, 1 immediately remanded
    - Hungarian action day: 1 additional suspect arrested
  - Investigation explicitly marked "rozwojowy" (ongoing) with further action days planned domestically and abroad.
  - L19/L23-strict applied: agent only added wikilinks for entities both named in tier-1 source AND with existing wiki org pages. Spain/Hungary country wikilinks retained but no Spanish/Hungarian agency wikilinks added.

## [2026-05-09] ingest | Operation PANDORA — 12 phone-fraud call-centres takedown (DE-led, AL+BA+XK+LB centres, SI victims; 2024-04-18)
- Source: raw/press-releases/2024-05-03_policija-si_operation-pandora-12-phone-fraud-call-centres-slovenia.md (Slovenian Police; en) + cross-check Europol 2024-05-02
- Pages created: wiki/sources/2024-05-03_policija-si_..., wiki/operations/operation-pandora-12-phone-fraud-call-centres-2024.md (provisional, source_count=2: SI + Europol cross-check).
- Pages updated: 6 country pages (DE, AL, BA, XK, LB, SI), agencies (germany-bka, europol-ec3), crime-types/online-fraud-ic, mechanisms/asset-freezing.
- Key findings:
  - **First wiki record sourced from policija.si** (Slovenska policija) — first Slovenian-language tier-1 IC primary in wiki.
  - 2024-04-18 simultaneous raids on **12 call centres across 4 perpetrator-side countries** (Albania, Bosnia and Herzegovina, Kosovo, Lebanon). 21 detained of 39 identified. ~6 country IC scope (DE+AL+BA+XK+LB+SI). DE LKA BW + BKA-led, Europol-coordinated with mobile offices deployed to all 4 perpetrator-side countries.
  - **Country-specialised fraud-type pattern documented**: BiH = debt-collection fraud; Kosovo = online banking fraud; Albania = investment fraud; Lebanon = prepaid-card fraud — each call-centre cluster specialised in a distinct vertical, not generic shared-fraud model. New benchmark for understanding multi-country call-centre infrastructure beyond a single fraud type.
  - Trigger: Freiburg, Germany bank teller flagged a EUR 100K cash-withdrawal as fake-police-officer scam in Dec 2023 → German LKA BW + BKA opened investigation → ~1.3M scam calls intercepted across 4 months → 7,500+ calls crossed criminal-proceedings threshold → action day.
  - **80% loss-prevention rate in indicted crimes** — high pre-emptive interception efficiency. EUR 10M+ potential damages prevented; EUR 1M cash + assets seized.
  - SI victim arc since 2023-07: ~40 cases against legal persons, ~EUR 3.8M damage; stolen funds routed to bank accounts in Germany — illustrates German banking layer used for SI-victim flow.
  - L19/L23-strict applied: only [[germany-bka]] and [[europol-ec3]] wikilinked in participating_agencies (only ones with wiki org pages); LKA BW, Polizeipräsidium Freiburg, Staatsanwaltschaft Freiburg, Generalstaatsanwaltschaft Karlsruhe, and the AL/BA/XK/LB/SI national police are described in body prose only.
  - legal_basis: [] kept empty per L23 (sources don't enumerate specific JIT/MLAT/EAW instruments).

## [2026-05-09] ingest | Operation Cumberland — Danish-led 19-country AI-CSAM buyer takedown (NSK + Europol J-CAT, 2025-02-28)
- Source: raw/press-releases/2025-02-28_politi-dk_operation-cumberland-ai-csam-international.md (Rigspolitiet NSK; da)
- Pages created: wiki/sources/..., wiki/operations/operation-cumberland-ai-csam-2025.md (provisional, source_count=1).
- Pages updated: 19 country pages (DK + AU/AT/BE/BA/CZ/FI/FR/DE/HU/IS/NL/NZ/NO/PL/ES/SE/CH/UK), 14 agencies (denmark-police + europol-ec3 + 12 NCB-level partners), csam-ic crime-type, j-cat mechanism.
- Key findings:
  - **First wiki record sourced from politi.dk** (Danish National Police / Rigspolitiet) — first Danish-language tier-1 IC primary in wiki.
  - **First wiki record of AI-generated CSAM as a crime category in IC takedown context** — Europol explicitly flags as "one of the first cases involving AI-generated CSAM... lack of national legislation addressing these crimes." Substantive-law gap documented.
  - **19-country IC scope** (DK lead + 18 partners) — among the highest country-named-in-single-source counts in wiki, exceeded only by HAECHI series and OTF GRIMM (11 countries).
  - 273 suspects identified, 25 arrests, 33 house searches, 173 electronic devices seized in coordinated 2025-02-26 action day.
  - Producer chain: 29-y-o Danish national arrested 2024-11 by Østjyllands Politi → convicted at Retten i Randers 2025-01 (1y 3m / 3m unconditional, under appeal) → NSK initiated international buyer-side phase using financial trail (betalingssporet) on platform payment-processor records.
  - Two Danish customer suspects (men aged 30 and 32) charged separately by Nordsjællands Politi.
  - Cooperation pattern: Europol J-CAT operational coordination + EC3 information exchange + analysis. National authorities for the 19 jurisdictions handled action-day coordination.
  - L19/L23-strict applied: 14 agency wikilinks all backed by tier-1 source naming AND existing wiki org pages. Agencies whose org pages don't yet exist (Hungary NNI Cybercrime, Iceland NCP, NZ Police, Belgium DJSOC, Republika Srpska MoI) described in body prose only.
  - legal_basis: [] kept empty per L23 (sources don't enumerate specific JIT/MLAT/EAW instruments — buyer-side phase delegated to national authorities).

## [2026-05-09] ingest | PT-ES EAW surrender of Luso-Angolan cyber-fraud + money-laundering suspect (2025-09-22)
- Source: raw/press-releases/2025-09-22_policiajudiciaria-pt_detido-em-espanha-homem-procurado-em-portugal-por-branqueamento-e-burla-informatica.md (Polícia Judiciária Portugal; pt)
- Pages created: wiki/sources/..., wiki/operations/portugal-spain-luso-angolan-cyber-fraud-money-laundering-eaw-2025.md (provisional, source_count=1).
- Pages updated: 4 country pages (PT, ES, UK, AO), 2 agencies (portugal-policia-judiciaria, spain-national-police), 2 crime-types (online-fraud-ic, money-laundering-ic), 2 mechanisms (european-arrest-warrant, extradition).
- Key findings:
  - **First wiki record sourced from policiajudiciaria.pt** (Portuguese Polícia Judiciária) — first Portuguese-language tier-1 IC primary in wiki.
  - Single-defendant cyber-fraud + money-laundering case demonstrating routine EAW execution arc: PT investigation 2024 (DIAP da Amadora, PJ UNC3T + UCI) → suspect resided UK from April 2025 → ES arrest Sep 2025 → Caya/Elvas border surrender → Criminal Court of Amadora preventive detention.
  - 4-country IC scope (PT prosecuting, ES executing, UK residence, AO suspect dual-nationality).
  - **Routine EAW pattern documented**: matured domestic investigation + EAW + bilateral PT-ES surrender without Eurojust/Europol involvement. Benchmark for "no JIT/no MLA" baseline cooperation in established EU bilateral channels.
  - Modus operandi documented verbatim: cyber-fraud proceeds laundered through online-gaming platforms — gaming-platform laundering layer recorded in wiki for the first time as primary-source-attested.
  - L19/L23-strict applied: only [[portugal-policia-judiciaria]] and [[spain-national-police]] in participating_agencies (named in tier-1 source AND wiki org pages exist). UK and Angolan agencies NOT in participating_agencies (not named at agency level in source).

## [2026-05-09] ingest | Poland CBZC Phobos affiliate arrest — Operation Aether (PL+US, 2026-02-17)
- Source: raw/press-releases/2026-02-17_cbzc-policja-pl_47-latek-phobos-zatrzymany-cbzc.md (Polish CBZC; pl)
- Pages created: wiki/sources/..., wiki/operations/poland-cbzc-phobos-affiliate-arrest-aether-2026.md (provisional, source_count=1).
- Pages updated: countries (PL, US), agencies (poland-police, europol-ec3, us-doj), crime-types/ransomware-ic, mechanisms (search-seizure, extradition).
- Key findings:
  - **First wiki appearance of "Operation Aether" branding** — Europol-coordinated campaign against Phobos ransomware ecosystem (distinct from existing phobos-8base-crackdown 2025-02-11 wave; Operation Aether is the broader umbrella name).
  - 47-y-o Polish national arrested in Małopolskie Voivodeship by joint CBZC team from Katowice + Kielce divisions. Charged Polish Penal Code Art. 269b § 1 (production/acquisition/distribution of hacking tools, max 5 years). Investigation supervised by Prokuratura Okręgowa w Gliwicach.
  - Suspect contacted Phobos ransomware group via encrypted messengers; computer + mobile phones with logins/passwords/credit-card numbers/server IPs seized.
  - Links cited: prior Phobos administrator extradition to USA + 1000+ global victims (US public schools in CA/CT, Maryland healthcare, US DoD contractor) per US DOJ documents → total ransom >USD 16M.
  - PL-US IC scope (PL locus of arrest, US prior extradition + DOJ documents cited as basis).
  - L19/L23-strict applied: 3 agency wikilinks all in tier-1 source AND wiki org pages exist.

## [2026-05-10] ingest | GXC Team / GoogleXcoder phishing-kit CaaS takedown — Guardia Civil + BR Federal Police + Group-IB (2025-10-08)
- Source: raw/press-releases/2025-10-08_guardiacivil-es_gxc-team-googlexcoder-phishing-kits-arrest.md (Spanish Guardia Civil; es)
- Pages created: wiki/sources/..., wiki/operations/gxc-team-googlexcoder-phishing-kits-takedown-2025.md (provisional, source_count=1).
- Pages updated: countries (ES, BR), agencies (spain-guardia-civil, brazil-ministry-of-justice-public-security, group-ib), 4 crime-types (online-fraud-ic, bank-fraud-ic, malware-ic, cybercrime-infrastructure-ic), 4 mechanisms (informal-cooperation, public-private-cooperation, search-seizure, cryptocurrency-seizure).
- Key findings:
  - **First wiki record sourced from web.guardiacivil.es** (Spanish Guardia Civil official).
  - GXC Team / GoogleXcoder Crime-as-a-Service phishing-kit operation dismantled — main developer (25-y-o Brazilian national) arrested in San Vicente de la Barquera (Cantabria). 6 entries-and-searches across Valladolid, Zaragoza, Barcelona, Palma de Mallorca, San Fernando, La Línea de la Concepción.
  - **Telegram-based CaaS distribution model documented**: phishing kits cloning Spanish banking websites + government portals sold under subscription model with customisation, technical support, updates — hundreds of EUR/day. Operator-side Telegram group named "Robarle todo a las abuelas" — captured verbatim as primary-source-attested CaaS marketplace pattern.
  - 6 additional users of the CaaS service identified through >1y device forensics + cryptocurrency-transaction reconstruction.
  - Pre-disruption impact: millions of EUR stolen, thousands of victims, dozens of impersonated entities; Telegram channels deactivated.
  - **Public-private cooperation pattern**: Group-IB provided technical analysis of phishing infrastructure + Telegram-based CaaS distribution. Spanish Guardia Civil UCO Departamento contra el Cibercrimen lead, supervised by Juzgado de Instrucción número 1 de San Vicente de la Barquera.
  - Bilateral ES-BR police-to-police cooperation for identification of Brazilian-national suspect; investigation remains open.
  - L19/L23-strict applied: 3 wikilinked agencies all named in source AND wiki org pages exist. UCO is sub-unit of spain-guardia-civil — described in body prose.

## [2026-05-10] ingest | Operation LoopX — Austrian crypto-coin (fake-ICO) exit-scam takedown (AT+CY+CZ Eurojust+Europol, 2024-05-08)
- Source: raw/press-releases/2024-05-08_eurojust_austrian-crypto-coin-loopx-takedown.md (Eurojust; en) + Europol cross-check
- Pages created: wiki/sources/..., wiki/operations/austrian-crypto-coin-loopx-takedown-2024.md (provisional, source_count=2 — Eurojust + Europol cross-check).
- Pages updated: 3 country pages (AT, CY, CZ), 3 agencies (europol-ec3, eurojust, czech-police), 2 crime-types (online-fraud-ic, money-laundering-ic), 4 mechanisms (european-arrest-warrant, eurojust-coordination-meeting, search-seizure, asset-freezing).
- Key findings:
  - 6 Austrian suspects arrested for fake-ICO crypto exit scam (10M tokens sold Dec 2017–Feb 2018 for BTC+ETH; ~EUR 6M victim losses).
  - 6 house searches executed across AT+CY+CZ on 2024-05-08 action day.
  - **Cooperation toolset documented**: Eurojust coordination centre + Europol Virtual Command Post + Europol mobile office in Cyprus + on-site Austrian police presence in Cyprus + EAW + search warrants + 5 Europol operational meetings + Austrian desk at Eurojust. Comprehensive multi-tool deployment benchmark.
  - **Cyprus mobile-office pattern**: Europol mobile office deployed to Cyprus + Austrian police on-site presence — illustrates expedited evidence-collection model when victim/perpetrator state ≠ host state.
  - Quantified seizure: EUR 750K liquid + EUR 500K+ crypto + EUR 250K fiat + EUR 1.4M property + 2 cars + dozens of bank accounts frozen.
  - Lead Austrian: WKStA + Bundeskriminalamt C4 (no wiki org pages exist; described in body prose only).
  - L19/L23-strict applied: 3 wikilinked agencies all named in source AND wiki org pages exist. lead_agency: "" kept empty (no Austrian agency wiki page); coordinating_body: [[eurojust]].

## [2026-05-10] iter 110 milestone push integrity sweep
- 10 commits since last push (iters 101-110): 7cb1a01eb..[iter 110] pushing 11 commits to origin/master.
- Lint: HIGH=0 CRITICAL=0 MEDIUM=0 LOW=0
- check_links: broken=2 (both pre-existing legacy LESSONS.md backlinks in unrelated bohemia-cannabia HTML)
- placeholder strings (`Z`+`ZPROT` / `>P`+`ROT[0-9]`): 0
- web/build_static.py: completed successfully (background task)
- Source-count total: 9,343 across 2,761 pages (Δ +142 source-count across +16 pages since iter 100 milestone)
- Freshness audit: 248 pages at 2026-05-09 + several at 2026-05-10 (touched-page `updated:` bumps from 9 iters of backlinker-driven freshness remediation working as designed)
- Touched 21 unique tier-1 publishers across iters 101-110: politsei.ee, sputnik.kz, policie.gov.cz (PATHFINDER), cbzc.policja.gov.pl (Kraków + Aether), policija.si, politi.dk, policiajudiciaria.pt, web.guardiacivil.es, eurojust.europa.eu (LoopX). Spans 30+ countries (DE, EE, US, UA, KZ, AM, GE/IR/SY/LB, CZ, AL, BA, XK, LB, SI, PL, ES, HU, RO, GR, IT, BE, NL, DK, AU, AT, FI, FR, IS, NZ, NO, CH, UK, PT, AO, BR, CY).

## [2026-05-10] ingest | SG-HK-MY tri-lateral GSM gateway scam syndicate takedown — FRONTIER+ umbrella (April-June 2025)
- Source: raw/press-releases/2025-06-17_spf-singapore_sg-hk-my-gsm-gateway-scam-syndicate-takedown.md (Singapore Police Force PAD; en)
- Pages created: wiki/sources/..., wiki/operations/sg-hk-my-gsm-gateway-scam-takedown-2025.md (provisional, source_count=1).
- Pages updated: 3 country pages (SG, HK, MY), 3 agencies (singapore-police, hong-kong-police, royal-malaysia-police), 3 crime-types (voice-phishing-ic, online-fraud-ic, cybercrime-infrastructure-ic), 2 mechanisms (informal-cooperation, extradition).
- Key findings:
  - **First wiki record of FRONTIER+ second joint operation** (operationally distinct from existing FRONTIER+ first joint op covered in `frontier-plus-cross-border-anti-scam-2025`). Two-month sustained tri-lateral takedown April-June 2025.
  - 11 persons aged 24-48 arrested across SG+HK+MY. **226 GSM gateway devices seized** (SG: 75, HK: 141, MY: 10).
  - 29-y-o suspect arrested in Malaysia 2025-06-03, **handed over to Singapore and charged 2025-06-05** under Penal Code ss. 420 r/w 120B (max 10 years + fine) — fast cross-border surrender pattern documented.
  - **VoIP GSM gateway infrastructure pattern** documented: cloud-based remote OS linking GSM mobile networks across the three jurisdictions to disguise call origin. Modus operandi benchmark for transnational scam-call infrastructure.
  - SPF units: CAD + CID + PID. Senior officer quote: David Chew (Director CAD).
  - L19/L23-strict applied: 3 wikilinked agencies all named in source AND wiki org pages exist.

## [2026-05-10] ingest | BG-ES bilateral Sofia call-centre online investment fraud takedown (December 2025)
- Source: raw/press-releases/2025-12-12_bta-bg_sofia-call-centre-organized-crime-group-fraudulent-online-investment-platforms-bulgaria-spain-guardia-civil.md (BTA, Bulgarian News Agency state wire relaying Sofia City Prosecutor's Office; en)
- Pages created: wiki/sources/2025-12-12_bta-bg_sofia-call-centre-bulgaria-spain-guardia-civil-investment-fraud.md, wiki/operations/bulgaria-sofia-call-centre-investment-fraud-takedown-2025.md (provisional, source_count=1).
- Pages updated: countries/bulgaria, countries/spain; agencies bulgaria-police, bulgaria-ministry-of-interior, spain-guardia-civil; crime-types online-fraud-ic + money-laundering-ic.
- Key findings:
  - **First wiki record from BTA** (Bulgarian News Agency state wire) — new tier-1 publisher for the wiki.
  - 2025-12-11 Sofia raid by SCPO + GDBOP + GDNP + DANS + National Investigation Service Cybercrime Dept., with Spain's Guardia Civil joint teams under Bulgarian authority direction, against organized crime group running fraudulent online investment platforms targeting EU citizens since mid-2022.
  - **Distinctive seizure mix**: 17 investment gold bars (~BGN 7K each), >BGN 45K cash, 5 hardware crypto wallets (one >USD 230K), 20+ phones, 30+ USB drives, narcotics — physical-asset seizure pattern more typical of organized-crime than pure-cyber takedowns.
  - **BG-ES bilateral pattern under generic "EU police-cooperation mechanisms"** — no JIT, EIO, or named MLAT instrument; structurally distinct from the parallel Eurojust 700M crypto-investment-fraud Phase 2 (2025-11-25/26) which also targeted Bulgaria but via Eurojust/Europol coordination. Treated as standalone bilateral pending Spanish Guardia Civil counterpart release.
  - Suspect count, victim count, total fraud volume, operation codename: NOT published in BTA. Marked under `missing_fields`.
  - L19-strict applied: 3 wikilinked agencies (bulgaria-police, bulgaria-ministry-of-interior, spain-guardia-civil) named in source AND have wiki org pages.
  - L23-strict applied: lead_agency/coordinating_body left empty in frontmatter (SCPO is a prosecutor's office without a wiki org page; descriptive role kept in body prose).

## [2026-05-10] ingest | BE-NL bilateral CaaS phishing-panel supplier arrest (Belgian Federal Police, April 2026)
- Source: raw/press-releases/2026-04-22_police-be_crime-as-a-service-phishingpanelen-leverancier-opgepakt.md (Belgian Federal Police Politie.be / Police.be; nl).
- Pages created: wiki/sources/2026-04-22_police-be_phishingpanelen-leverancier-arrest.md, wiki/operations/fgp-oost-vlaanderen-belgium-phishingpanelen-caas-arrest-2026.md (provisional, source_count=1).
- Pages updated: countries/belgium, countries/netherlands; agencies belgium-federal-police, europol-ec3; crime-types cybercrime-infrastructure-ic + online-fraud-ic + bank-fraud-ic.
- Key findings:
  - **Second wiki record from Belgian Federal Police** — first since 2017 WannaCry victim-call entry; Politie.be / Police.be promoted to fresher tier-1 publisher coverage.
  - 20-year-old NL-based supplier of CaaS phishing panels (panels-as-a-service to phishing crews) arrested in the Netherlands on **2026-01-26**, surrendered to Belgium on **2026-04-16** following Dendermonde investigating-judge-issued European Arrest Warrant. EUR 28,000 cash + multiple data carriers seized.
  - Investigation led by FGP Oost-Vlaanderen (East Flanders Federal Judicial Police) under East Flanders Public Prosecutor's Office direction with Europol coordination support; Dutch executing agency not explicitly named in source.
  - **CaaS supplier-tier arrest pattern** — distinct from end-user phishing-crew arrests; targets the wholesaler/infrastructure layer of the phishing supply chain.
  - L19-strict + L23-strict applied: only `[[belgium-federal-police]]` and `[[europol-ec3]]` named-and-existing-in-wiki used in participating_agencies; FGP Oost-Vlaanderen + East Flanders prosecutor + Dendermonde investigating judge kept in body prose only; lead_agency/coordinating_body emptied to avoid build-pipeline auto-link to missing pages.
  - 4 reference rows appended to mismatched pages; backlinker bumped `updated:` on all 8 touched pages for freshness.

## [2026-05-10] ingest | IT–US extradition of PRC HAFNIUM-campaign hacker Xu Zewei (Polizia di Stato + FBI, Malpensa Jul 2025 → Milan Apr 2026)
- Source: raw/press-releases/2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti.md (Polizia di Stato — Servizio Polizia Postale Commissariato di P.S. on-line; it).
- Pages created: wiki/sources/2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti.md, wiki/operations/italy-china-us-hafnium-hacker-extradition-2026.md (source_count=1).
- Pages updated: countries/italy, countries/united-states; cases/us-v-xu-zewei-hafnium-extradited-italy (related_operation backlink + ref row); 6 agencies (polizia-di-stato, italy-polizia-postale, fbi, fbi-cyber-division, us-doj, office-of-international-affairs); 2 crime-types (hacking-ic, malware-ic); mechanisms/extradition.
- Key findings:
  - **First wiki record from Commissariato di P.S. on-line** (commissariatodips.it) — the public-facing Polizia Postale portal, distinct from poliziadistato.it institutional press releases.
  - **Italian-side operational angle to existing US-side prosecution**: case `us-v-xu-zewei-hafnium-extradited-italy` already documents the indictment + 12,700+ HAFNIUM victims angle; this new operation page captures the Italian extradition operational chain (Malpensa airport interception by Polaria + Polizia Postale; Servizio Cooperazione Internazionale di Polizia INTERPOL-NCB; Corte d'Appello di Milano + Ministro della giustizia authorisation).
  - Cross-bound: case → operation linked via `related_operation`; operation → case via `related_cases`.
  - **PRC-attribution operation** — China is subject-of-attribution per US indictment (alleged MSS Shanghai SSB contractor via Shanghai Powerock) but is NOT a cooperating participant; per L19-strict, `[[china]]` correctly EXCLUDED from `participating_countries`.
  - L23-strict: lead_agency=`[[polizia-di-stato]]` (existing wiki page); coordinating_body left empty.
  - 6 reference rows appended; 14 pages with `updated:` bumped.

## [2026-05-10] ingest | NL/US/FI AvCheck Counter-Antivirus takedown + Schiphol arrest (OM.nl, May 2025–Jan 2026)
- Source: raw/press-releases/2026-01-12_om-nl_avcheck-amsterdam-schiphol-arrest-cybercrime.md (Openbaar Ministerie — Landelijk Parket; nl).
- Pages created: wiki/sources/2026-01-12_om-nl_avcheck-amsterdam-schiphol-arrest-cybercrime.md, wiki/operations/avcheck-counter-antivirus-takedown-and-schiphol-arrest-2025-2026.md (provisional, source_count=1).
- Pages updated: countries/netherlands, countries/united-states, countries/finland; 7 agencies (netherlands-om, netherlands-politie, dutch-nhtcu, us-doj, fbi, us-secret-service, finland-nbi); 3 crime-types (malware-ic, cybercrime-infrastructure-ic, ransomware-ic); operations/operation-endgame (related_operations); legal-frameworks/budapest-convention (operations_enabled + sources); mechanisms/mlat-process (operations_using + sources).
- Key findings:
  - **OM.nl Landelijk Parket** promoted from organizational landing-page-only to operational tier-1 publisher coverage. Under-sourced before this iter (only 4 prior raw entries).
  - **Counter-Antivirus (CAV) service takedown** — May 2025 NL/US/FI tri-lateral op against avcheck.net + crypter domains used by malware developers to test detection evasion. 4 domains seized by US DOJ on 2025-05-27 (per external reporting; OM.nl tier-1 release does not enumerate count).
  - **Schiphol airport arrest follow-up** — 33-y-o Dutch national operator (relocated to UAE) arrested 2026-01-11 transiting Schiphol per international wanted-person flagging (signalering). 2 Amsterdam companies and data carriers seized.
  - **Operation Endgame sub-operation** — Aliases include "Operation Endgame — AvCheck (CAV/crypter sub-operation)"; confirmed via `related_operations: [[operation-endgame]]` bidirectional backlink.
  - L19-strict applied: 7 wikilinked agencies all named in source AND have wiki pages. Koninklijke Marechaussee mentioned in prose only (no wiki page yet).
  - L23-strict applied: lead_agency/coordinating_body left empty (OM.nl release describes a tri-lateral op without designating a single lead/coordinator).
  - 9 reference rows appended; 17 pages with `updated:` bumped.

## [2026-05-10] ingest | NZ-US joint USD 265M cryptocurrency-theft RICO investigation (NZ Police + FBI, May 2025)
- Source: raw/press-releases/2025-05-16_police-govt-nz_wellington-based-man-arrested-international-cryptocurrency-scam-investigation.md (New Zealand Police — Financial Crime Group; en).
- Pages created: wiki/sources/2025-05-16_police-govt-nz_wellington-based-man-arrested-international-cryptocurrency-scam-investigation.md, wiki/operations/nz-fbi-malone-lam-265m-cryptocurrency-scam-2025.md (provisional, source_count=1).
- Pages updated: countries/new-zealand, countries/united-states; agencies fbi, us-doj; crime-types online-fraud-ic + money-laundering-ic + organized-crime-ic; mechanisms joint-investigation-team + search-seizure.
- Key findings:
  - **Second wiki record from NZ Police** (police.govt.nz) — first since a 2016 darknet-drug item; promoted to fresher tier-1 publisher coverage; first NZ-US bilateral cybercrime IC record in the wiki.
  - **Coordinated three-day search-warrant operation** Auckland–Wellington–California: 13 arrests, 1 Wellington-based NZ resident indicted by US DOJ under RICO + wire-fraud + money-laundering conspiracy.
  - **USD 265M / NZD 450M cryptocurrency theft** from 7 victims March–August 2024 by multinational organised crime group; high-profile spending pattern (~USD 9M exotic cars, watches, Hamptons/Miami rentals, private-jet, nightclub spending).
  - Co-defendant of Malone Lam (named in some external reporting; not asserted in NZ release).
  - L19-strict applied: only 2 wikilinked agencies (fbi, us-doj) named in source AND with wiki pages. NZ Police Financial Crime Group kept as plain prose (no wiki org page yet).
  - L23-strict applied: lead_agency=`[[fbi]]`; coordinating_body left empty.
  - 5 reference rows appended; 8 pages with `updated:` bumped.

## [2026-05-10] ingest | Operación Aliados por la Infancia VI — 13-jurisdiction CSAM enforcement (MPF CABA, April 2026)
- Source: raw/press-releases/2026-04-29_mpf-caba_aliados-por-la-infancia-vi-megaoperativo-internacional.md (Ministerio Público Fiscal CABA — Cuerpo de Investigaciones Judiciales; es).
- Pages created: wiki/sources/2026-04-29_mpf-caba_aliados-por-la-infancia-vi-megaoperativo-internacional.md, wiki/operations/aliados-por-la-infancia-vi-mpf-caba-2026.md (provisional, source_count=1).
- Pages updated: 12 country pages (argentina, brazil, panama, dominican-republic, guatemala, uruguay, paraguay, costa-rica, spain, peru, honduras, france); 2 agencies (us-dhs, ncmec); crime-types/csam-ic; mechanisms/informal-cooperation.
- Key findings:
  - **First wiki record from MPF CABA / mpfciudad.gob.ar** — Argentine prosecutor's office (Buenos Aires Autonomous City) — new tier-1 publisher in the wiki.
  - **First wiki record of multi-Latin-America CSAM mega-op coordinating 13 jurisdictions** simultaneously: 270 search warrants (68 AR + 202 abroad), 84 detentions, distribution AR(26) + BR(44) + PA(7) + UY(3) + PE(3) + PR(1).
  - **AR-led coordination model with US partner** (DHS HSI cybercrime division acknowledged in source) — neither MLAT nor a treaty article is cited; cooperation framed as informal multi-jurisdictional sharing supported by NCMEC tip-line / CyberTipline data.
  - Puerto Rico named in source but no wiki page yet → kept in body prose only per L19/L23.
  - Agency-naming gap: foreign-jurisdiction executing agencies NOT enumerated in MPF CABA release — recorded as `missing_fields` for future enrichment.
  - L19-strict applied: only 2 wikilinked agencies (us-dhs, ncmec) named in source AND with wiki pages.
  - L23-strict applied: lead_agency/coordinating_body left empty (MPF CABA + CIJ are prosecutor entities without wiki pages).
  - 3 reference rows appended; 16 pages with `updated:` bumped.

## [2026-05-10] ingest | Polri INTERPOL Red Notice arrest of LCS — Cambodia-base "abbishopee" online-fraud network (Bareskrim Dittipidsiber, May 2026) — iter 118
- Source: raw/press-releases/2026-05-05_polri_lcs-interpol-red-notice-cambodia-online-fraud-arrest.md (Indonesian National Police, Tribrata News national newsroom; id).
- Pages created: wiki/sources/2026-05-05_polri_lcs-interpol-red-notice-cambodia-online-fraud-arrest.md, wiki/operations/polri-lcs-cambodia-abbishopee-red-notice-arrest-2026.md (provisional, source_count=1).
- Pages updated: none (per task scope: backlinks deferred).
- Key findings:
  - **First wiki record from Polri Tribrata News (tribratanews.polri.go.id)** — under-sourced tier-1 Indonesian publisher; previously the wiki had only one direct Polri release (the April 2026 INP-FBI MFA-bypass release on inp.polri.go.id).
  - **Distinct from the April 2026 INP-FBI MFA-bypass case** — different suspects (LCS vs. GWL/FYT), different modus (operator of a branded fraud platform vs. PhaaS MFA-bypass scripts), different foreign partner (INTERPOL Red Notice vs. FBI bilateral), different operating base (Cambodia vs. Indonesia-only).
  - **IC scope (≥2 countries):** Indonesia (host / arrest at Soekarno-Hatta) + Cambodia (named operating base of the fraud network); INTERPOL named as multilateral mechanism.
  - **Pattern: Red Notice + airport-arrest sequencing** for Cambodia-base fugitives — the suspect was arrested at the targeting state's own point of entry rather than via formal extradition from Cambodia, consistent with the broader regional pattern around Cambodia-hosted scam compounds.
  - **Pattern: centralized national handling** — 23+ Laporan Polisi from regions of Indonesia consolidated under Dittipidsiber Bareskrim Polri; three earlier-arrested co-defendants in the same network already convicted at Pengadilan Negeri Jakarta Selatan.
  - Senior official on the record: Brig. Gen. Pol. Himawan Bayu Aji, Director of Cyber Crime, Bareskrim Polri.
  - L19-strict applied: only the explicitly named participating jurisdictions (indonesia, cambodia) are wiki-linked; no third Red Notice country is asserted.
  - L23-strict applied: lead_agency = `[[indonesia-police|...]]` (verified existing org page); coordinating_body = `[[interpol|INTERPOL (Red Notice)]]` (verified existing org page) — no plain-text entity strings.
  - L1 applied: source URL fetched and verified against canonical national portal (`tribratanews.polri.go.id`) plus three regional mirror sub-domains.
- Backlinks applied (orchestrator follow-up): 2 country pages (indonesia, cambodia); 2 agencies (indonesia-police, interpol); crime-types/online-fraud-ic; mechanisms/informal-cooperation; challenges/jurisdictional-conflicts (sources backlink); 3 related operations (indonesia-fbi-mfa-bypass, seoul-eastern-clark, lai-chau-cambodia-bokor). 3 reference rows appended.

## [2026-05-10] ingest | PF Brazil-Belgium passive extradition arrest of Belgian national for IT-forgery + fraud (São Paulo, March 2026)
- Source: raw/press-releases/2026-03-09_pf-gov-br_pf-prende-foragido-belga-fraude-falsificacao-tecnologia-informacao-sao-paulo.md (Polícia Federal — Superintendência Regional em São Paulo; pt-BR).
- Pages created: wiki/sources/2026-03-09_pf-gov-br_pf-prende-foragido-belga-fraude-falsificacao-tecnologia-informacao-sao-paulo.md, wiki/operations/pf-belgium-extradition-arrest-sao-paulo-2026.md (provisional, source_count=1).
- Pages updated: countries/brazil, countries/belgium; organizations/brazil-ministry-of-justice-public-security; crime-types/online-fraud-ic; mechanisms/extradition; 3 related operations (fgp-oost-vlaanderen-belgium-phishingpanelen-caas-arrest-2026, spf-fpb-operation-cryptoscam-2025, operation-dark-bet-pf-brazil-nigeria-2025).
- Key findings:
  - **Third wiki record from gov.br/pf** — under-sourced before (only 2 prior PF entries).
  - **First wiki record of Brazil-Belgium passive extradition (cyber-related forgery)**: Belgian national arrested by PF/SR-SP on STF mandado de prisão para extradição (Belgian charges include falsificação de tecnologia da informação — Budapest Convention Art. 7 territory).
  - **Cross-link to BE-NL CaaS phishing-panel supplier** (iter 113) — Brazil-Belgium and BE-NL records now form a Belgian-cybercrime cooperation cluster in the wiki.
  - Defendant identity withheld in PF release per Brazilian pre-trial practice.
  - L19-strict applied: only `[[brazil-ministry-of-justice-public-security]]` named-and-existing-in-wiki used in participating_agencies. Belgian counterpart authority NOT named in source — kept out of frontmatter.
  - L23-strict applied: lead_agency/coordinating_body left empty (PF/SR-SP and STF mentioned in body prose only).
  - 3 reference rows appended; 12 pages with `updated:` bumped.

## [2026-05-10] ingest | RCMP Toronto iSpoof.cc top-50 subscriber arrest (Mansouri/Alouah, February 2025) — iter 120
- Source: raw/press-releases/2025-02-20_rcmp-grc-gc-ca_ontario-rcmp-shuts-prolific-cyber-fraudsters.md (RCMP Central Region — Ontario; en).
- Pages created: wiki/sources/2025-02-20_rcmp-grc-gc-ca_ontario-rcmp-shuts-prolific-cyber-fraudsters.md, wiki/operations/rcmp-toronto-ispoof-cyber-fraudsters-arrest-2025.md (provisional, source_count=1).
- Pages updated: countries/canada, countries/united-kingdom, countries/netherlands; 5 agencies (canada-rcmp, uk-metropolitan-police, netherlands-politie, europol-ec3, eurojust); crime-types/online-fraud-ic + voice-phishing-ic + access-device-fraud; mechanisms/informal-cooperation + search-seizure.
- Key findings:
  - **Second wiki record from RCMP** (rcmp-grc.gc.ca) — under-sourced previously (only 1 prior op).
  - **First wiki record of CA-side iSpoof.cc downstream subscriber prosecution** — Mansouri (29) + Alouah (31) arrested 2025-02-19 in Greater Toronto Area as alleged top-50 worldwide subscribers of the iSpoof spoofing-as-a-service platform; ≥570 Canadian victims, "millions of dollars" in losses.
  - 5 substantive Canadian Criminal Code charges: s.380(1) Fraud + s.342.1 Unauthorized Use of Computer + s.462.31 Laundering Proceeds + s.430(1.1) Mischief in relation to computer data + s.354 Possession of Proceeds.
  - **Three-country IC scope**: Canada (lead/prosecuting) + UK (London Met origin takedown) + NL (Dutch National Police partner) + EUROPOL + EUROJUST.
  - L19-strict applied: 5 wikilinked agencies all named in source AND with wiki pages.
  - L23-strict applied: lead_agency=`[[canada-rcmp]]` (existing wiki page); coordinating_body left empty (no single coordinator named).
  - 9 reference rows appended; 14 pages with `updated:` bumped.

## [2026-05-10] iter 120 milestone push integrity sweep
- 10 commits since last push (iters 111-120): 5d0383578..[iter 120 head] pushing ~10 commits to origin/master.
- Lint: HIGH=0 CRITICAL=0 MEDIUM=0 LOW=0
- check_links: broken=2 (both pre-existing legacy LESSONS.md backlinks in unrelated bohemia-cannabia HTML)
- placeholder strings (`Z`+`ZPROT` / `>P`+`ROT[0-9]`): 0 across wiki/
- Touched 10 unique tier-1 publishers across iters 111-120: politsei.ee, sputnik.kz, policie.gov.cz (PATHFINDER), bta.bg (Bulgarian News Agency state wire), police.be (Belgian Federal Police), commissariatodips.it (Polizia Postale public portal), om.nl (Landelijk Parket), police.govt.nz (NZ Police Financial Crime Group), mpfciudad.gob.ar (MPF CABA Argentina), tribratanews.polri.go.id (Polri), rcmp-grc.gc.ca (RCMP Central Region), gov.br/pf (Polícia Federal Brazil 3rd record).
- Spans 28+ countries this milestone block: BG, ES, BE, NL, IT, US, CN-attribution, FI, NZ, AR, BR, PA, DO, GT, UY, PY, CR, PE, HN, FR, ID, KH, CA, UK + KE/CR/PA/DO inherited.
- 8 first-wiki structural records this milestone: BTA (state wire); FGP Oost-Vlaanderen East Flanders bilateral CaaS supplier-tier arrest; commissariatodips.it Polizia Postale public portal; OM.nl Landelijk Parket operational; NZ Police Financial Crime Group; MPF CABA prosecutor's office; multi-Latin-America 13-jurisdiction CSAM mega-op; tribratanews.polri.go.id national newsroom.
- 3 first-pattern operations: PRC-attribution operational counterpart to existing prosecution case (HAFNIUM Xu Zewei); Operation Endgame CAV-sub-operation (NL/US/FI AvCheck); INTERPOL Red Notice + airport-arrest pattern documented for Cambodia-base scam-compound fugitives (Polri LCS).
- web/build_static.py: queued for background run after push.

## [2026-05-10] ingest | AFP-RMP-FBI Malaysia myGov phishing-kit-as-a-service syndicate dismantling (Nov 2023)
- Source: raw/press-releases/2023-11-27_afp-gov-au_eight-arrests-malaysia-mygov-phishing-kits.md (Australian Federal Police; en).
- Pages created: wiki/sources/2023-11-27_afp-gov-au_eight-arrests-malaysia-mygov-phishing-kits.md, wiki/operations/afp-jpc3-rmp-fbi-mygov-phishing-kits-malaysia-2023.md (provisional, source_count=1).
- Pages updated: countries/australia, countries/malaysia, countries/united-states; agencies australia-afp, malaysia-police, fbi-cyber-division; crime-types online-fraud-ic + cybercrime-infrastructure-ic + identity-theft + access-device-fraud; mechanisms/informal-cooperation.
- Key findings:
  - **First wiki record from afp.gov.au** as a primary source — only secondary outlets (csoonline) had been ingested before. AU AFP promoted to direct tier-1 publisher coverage.
  - **AU/MY/US tri-lateral phishing-kit-as-a-service takedown** — 35-y-o Malaysian alleged syndicate operator + 7 others arrested 2023-11-06 across Borneo + Malaysian technology park; 4 servers + 60+ TB data + cryptocurrency seed phrases recovered.
  - **myGov + Malaysian Government + US Government phishing-kit templates** all cloned by the syndicate — first wiki record of phishing-kit-as-a-service supplier-tier prosecution from APAC perspective (parallels iter 113 BE-NL CaaS supplier-tier arrest pattern).
  - L19-strict applied: 3 wikilinked agencies (australia-afp, malaysia-police, fbi-cyber-division) named in source AND with wiki pages.
  - L23-strict applied: lead_agency=`[[malaysia-police]]` (existing wiki page); coordinating_body left empty.
  - 7 reference rows appended; 12 pages with `updated:` bumped.
