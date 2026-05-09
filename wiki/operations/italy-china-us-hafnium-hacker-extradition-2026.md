---
type: operation
title: "Italy–US extradition of a PRC HAFNIUM-campaign hacker (Polizia di Stato + FBI, Malpensa arrest July 2025 → Milan extradition April 2026)"
aliases:
  - "Estradizione hacker cinese HAFNIUM Italia–Stati Uniti"
  - "Italy → US extradition of Xu Zewei (HAFNIUM)"
  - "Polizia Postale + FBI Malpensa cyber-extradition"
case_id: CYB-2026-114
period: 3
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - extradition
outcome: success
timeframe:
  announced: "2026-04-27"
  start: "2025-07"
  end: "2026-04-27"
  ongoing: false
crime_types:
  - "[[hacking-ic]]"
  - "[[malware-ic]]"
crime_type: "[[hacking-ic]]"
target_entity: "Individual PRC-national contract hacker (referred to as 'X. Z.' in the Italian press release; identified as Xu Zewei in the parallel US DOJ release; alleged former general manager of a Shanghai-based technology company; alleged contractor for the PRC Ministry of State Security — Shanghai State Security Bureau via Shanghai Powerock Network Co. Ltd. for the HAFNIUM Microsoft Exchange and COVID-19-research intrusion campaigns)."
lead_agency: "[[polizia-di-stato]]"
coordinating_body: ""
participating_countries:
  - "[[italy]]"
  - "[[united-states]]"
participating_agencies:
  - "[[polizia-di-stato]]"
  - "[[italy-polizia-postale]]"
  - "[[fbi]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
legal_basis:
  - "[[extradition]]"
mechanisms_used:
  - "[[extradition]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 extradition executed Italy → United States (weekend of 2026-04-25/26 per US DOJ; date not enumerated in Italian release)"
    - "Court of Appeal of Milan (Corte d'Appello di Milano) extradition decision + Italian Minister of Justice authorisation"
    - "1 first US federal-court appearance in S.D. Texas Houston Division on 2026-04-27 (per US DOJ release)"
edges:
  - source_actor: "[[polizia-di-stato]]"
    target_actor: "[[fbi]]"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "[[italy-polizia-postale]]"
    target_actor: "[[fbi]]"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "[[italy]]"
    target_actor: "[[united-states]]"
    cooperation_type: "extradition"
    legal_basis: "MLAT"
    direction: "directed"
  - source_actor: "[[office-of-international-affairs]]"
    target_actor: "[[polizia-di-stato]]"
    cooperation_type: "extradition"
    legal_basis: "MLAT"
    direction: "directed"
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "exact arrest date in July 2025 (Italian release: 'agli inizi di luglio del 2025' — early July 2025)"
  - "exact extradition execution date (Italian release does not give a date; US release indicates weekend of 2026-04-25/26)"
  - "name of the Italian extradition treaty article(s) invoked (the Italian release names only 'Corte d'Appello di Milano + Ministro della giustizia' — the standard Italian extradition authorisation chain; no treaty article cited)"
  - "exact role attribution of Polaria di Malpensa beyond the airport interception (no wiki page yet for Polaria/Polizia di Frontiera)"
  - "exact role attribution of Servizio per la Cooperazione Internazionale di Polizia (the Italian INTERPOL-NCB-equivalent unit; no separate wiki page yet)"
related_cases:
  - "[[us-v-xu-zewei-hafnium-extradited-italy]]"
related_operations: []
challenges_encountered: []
lessons_learned:
  - "First wiki record of an Italy → US extradition of a PRC state-sponsored cyber actor sourced from the **Italian primary side** (Polizia di Stato press release) — confirms partner-state agency-chain detail (Polizia Postale + Polaria di Malpensa + Servizio per la Cooperazione Internazionale di Polizia + Corte d'Appello di Milano + Ministro della giustizia) that the US DOJ release summarises only as 'Italian National Police — Cyber Division'."
  - "Schengen-region airport interception pattern: suspect transit through Malpensa intercepted by border police acting on FBI-shared targeting intelligence; analogous to other Schengen-region apprehensions of state-affiliated cyber actors logged in the wiki."
source_count: 1
sources:
  - "[[2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti]]"
created: 2026-05-10
updated: 2026-05-10
---

> [!info] Provisional / sparse-source page
> This page is built from a **single tier-1 primary source** (Polizia di Stato / Polizia Postale press release, 2026-04-27). The corresponding US-side primary source ([[2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy]]) is *not* counted toward this operation page's source count because it is already exhaustively summarised in the related case page [[us-v-xu-zewei-hafnium-extradited-italy]]. This operation page exists to document the **Italian-partner-state operational angle** (the extradition execution + chain-of-Italian-agencies) which the case page (US prosecution angle) does not fully capture. Treat all numeric/temporal claims as provisional pending a second independent primary source from the Italian side (e.g., a future ANSA wire reproducing official statements, or a Ministero della Giustizia release).

## Summary

On **2026-04-27**, the [[polizia-di-stato|Polizia di Stato]] (Italian National Police), through its [[italy-polizia-postale|Polizia Postale]] cyber unit, publicly announced that it had executed the extradition of a Chinese-national hacker (referred to in the Italian release as **"X. Z."** in line with Italian presumption-of-innocence reporting conventions; identified as **Xu Zewei** in the same-day US DOJ press release) to United States authorities. The extradition was the operational endpoint of (a) a **July 2025 arrest** at **Malpensa airport** by the Polizia Postale and Polaria di Malpensa (border police), (b) an **extradition decision by the Court of Appeal of Milan (Corte d'Appello di Milano)**, (c) authorisation by the **Italian Minister of Justice (Ministro della giustizia)**, and (d) handover via the **Servizio per la Cooperazione Internazionale di Polizia** (Italian Service for International Police Cooperation).

The Italian release frames the operation as the culmination of "una lunga collaborazione operativa tra FBI e gli investigatori della polizia italiana" — a long operational collaboration between the FBI and Italian police investigators — rather than a single-shot extradition; this is *highly likely* (per US IC analytic standard, 80–95%) to refer to information-sharing predating the July 2025 airport interception, since the suspect was intercepted while purporting to begin a holiday with his wife (i.e., not during a scheduled appearance), implying real-time targeting intelligence flow from FBI to the Italian investigators.

The underlying alleged conduct is the **HAFNIUM** Microsoft Exchange Server intrusion campaign of 2020–2021 plus prior COVID-19-research intrusions targeting US universities, attributed by US authorities to PRC Ministry of State Security — Shanghai State Security Bureau via the PRC enabling-company Shanghai Powerock Network Co. Ltd. (See [[us-v-xu-zewei-hafnium-extradited-italy]] for full case-prosecution detail.)

## Background

The HAFNIUM Microsoft Exchange Server campaign was publicly disclosed by Microsoft in March 2021 and attributed to PRC MSS by the United States and foreign partners in July 2021. The HAFNIUM campaign **almost certainly** (>95%) compromised 12,700+ US organisations per the US DOJ release of the same date as this Italian release. Phase 1 of the alleged conduct (early 2020) targeted US universities, immunologists and virologists conducting COVID-19 research; Phase 2 (late 2020 – early 2021) was the broader Microsoft Exchange Server compromise.

The named Italian-side timeline for this **extradition operation** is:

- **2025-07 (early July, exact date not enumerated)**: Arrest at Malpensa airport by Polizia Postale + Polaria di Malpensa, with the suspect intercepted alongside his wife.
- **(date not enumerated)**: Corte d'Appello di Milano extradition decision.
- **(date not enumerated)**: Italian Minister of Justice extradition authorisation.
- **2026-04 (weekend of 2026-04-25/26 per US DOJ release)**: Extradition handover executed via Servizio per la Cooperazione Internazionale di Polizia.
- **2026-04-27**: Public announcement by both Polizia di Stato (Italian release, this page's primary source) and US DOJ (US release, [[2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy]]).

## Participating Parties

### Italian side

| Italian agency / authority | Role in this operation |
|---|---|
| **Polizia di Stato** ([[polizia-di-stato]]) | Italian National Police — overall executing law-enforcement body for the operation. |
| **Servizio Polizia Postale e per la Sicurezza Cibernetica (Polizia Postale)** ([[italy-polizia-postale]]) | Cybercrime unit of Polizia di Stato — operational lead on the cyber-related elements of the cooperation with FBI; co-executed the Malpensa arrest. |
| **Polaria di Malpensa (Polizia di Frontiera)** | Border police at Milan-Malpensa airport — co-executed the July 2025 arrest at the airport. *No dedicated wiki page; recorded in prose only.* |
| **Servizio per la Cooperazione Internazionale di Polizia** | Italian Service for International Police Cooperation (Italian INTERPOL National Central Bureau equivalent) — coordinated the extradition handover. *No dedicated wiki page; recorded in prose only.* |
| **Corte d'Appello di Milano** | Court of Appeal of Milan — issued the extradition decision under Italian extradition law. *No dedicated wiki page; recorded in prose only.* |
| **Ministro della giustizia** | Italian Minister of Justice — issued the final political extradition authorisation (standard Italian extradition authorisation chain). *No dedicated wiki page; recorded in prose only.* |

### US side

| US agency | Role in this operation |
|---|---|
| **FBI** ([[fbi]]) | Lead US partnership agency cited explicitly in the Italian release as the cooperation counterpart of the Italian investigators. |
| **FBI Cyber Division** ([[fbi-cyber-division]]) | Underlying campaign-attribution lead within the FBI; the Houston Field Office is recorded as the lead US field office in the parallel US DOJ release. |
| **US Department of Justice** ([[us-doj]]) | Indicting jurisdiction (Southern District of Texas, Houston Division). |
| **DOJ Office of International Affairs** ([[office-of-international-affairs]]) | US-side extradition coordination counterpart of the Servizio per la Cooperazione Internazionale di Polizia. |

### Country-level

- [[italy]] (extradition source state)
- [[united-states]] (extradition destination / requesting state)
- [[china]] is the **subject-of-attribution country** (the alleged sponsoring state per the US indictment) but is **not a cooperating participant** in this extradition operation, and so is *not* listed in `participating_countries`.

## Legal Framework

The Italian release does not cite specific extradition treaty articles. Italy and the United States are bound by a bilateral extradition treaty (Treaty between the Government of the United States of America and the Government of the Republic of Italy on Extradition, signed 1983-10-13, entered into force 1984-09-24, with subsequent supplementary instruments) — *no dedicated wiki page yet for the US-Italy extradition treaty; recorded in prose only.* The Italian extradition authorisation chain documented in the release (Corte d'Appello di Milano + Ministro della giustizia) is the standard Italian-law procedural pathway under Codice di procedura penale Libro XI for treaty-based extraditions.

> [!warning] Legal status check needed
> The specific Italian-treaty-implementation article(s) and the specific US extradition-request submission date are not enumerated in this Italian press release. Update this page when the underlying judicial documents (extradition decree, court-of-appeal opinion) become publicly available, or when a second tier-1 source (e.g., Italian Ministero della Giustizia communication) confirms the procedural chain.

## Operational Timeline

| Date | Event | Source-language confidence |
|---|---|---|
| 2020 – 2021 | Alleged HAFNIUM + COVID-19-research intrusion conduct period | Italian release: "tra il 2020 e il 2021" |
| 2021-03 | Microsoft public disclosure of HAFNIUM campaign | Background, not in Italian release |
| 2021-07 | US + foreign partners attribute HAFNIUM to PRC MSS | Background, not in Italian release |
| 2025-07 (early) | Arrest at Malpensa airport by Polizia Postale + Polaria di Malpensa | Italian release: "agli inizi di luglio del 2025" |
| (between 2025-07 and 2026-04) | Corte d'Appello di Milano extradition decision | Italian release |
| (between 2025-07 and 2026-04) | Ministro della giustizia extradition authorisation | Italian release |
| 2026-04 (weekend of 2026-04-25/26 per US DOJ) | Extradition execution / handover | Italian release: date not enumerated; US DOJ release: weekend |
| 2026-04-27 | Italian Polizia di Stato press release announcing extradition | This page's primary source |
| 2026-04-27 | US DOJ release + first US federal court appearance, Houston | Parallel US source |

## Results and Impact

| Metric | Italian-release value | Notes |
|---|---|---|
| Arrests | 1 | The single PRC-national hacker (X. Z. / Xu Zewei). |
| Extraditions executed | 1 | Italy → US |
| Italian agencies named | 6 | Polizia di Stato, Polizia Postale, Polaria di Malpensa, Servizio per la Cooperazione Internazionale di Polizia, Corte d'Appello di Milano, Ministro della giustizia |
| US agencies named | 1 | FBI (Italian release does not enumerate DOJ / OIA / S.D. Texas — those are recorded from the parallel US DOJ release) |
| Decryption keys / domains / servers / crypto seized | 0 reported | This is an extradition operation, not an infrastructure-seizure operation; no cyber infrastructure seizures recorded. |

The extradition is *almost certainly* (>95%) the **first publicly recorded Italy → US extradition of a PRC state-sponsored cyber actor** — characterised as "rare" in third-party reporting cited in the parallel US case page [[us-v-xu-zewei-hafnium-extradited-italy]]. The Italian release does not itself make a "first" claim; it characterises the Italian-FBI cooperation as "ottima e consolidata" (excellent and consolidated).

## Cooperation Mechanisms Used

- **Bilateral extradition treaty** (US-Italy, 1983/1984) — the legal backbone of the handover; not a wiki entity yet.
- **Informal pre-extradition operational cooperation** — the Italian release explicitly characterises a "lunga collaborazione operativa tra FBI e gli investigatori della polizia italiana", *highly likely* (80–95%) to include FBI targeting intelligence shared with Italian investigators in advance of the July 2025 Malpensa interception.
- **[[extradition|Extradition]]** as a formal mechanism — the Italian release names the full Italian-side chain (Corte d'Appello di Milano + Ministro della giustizia + Servizio per la Cooperazione Internazionale di Polizia).

## Challenges and Friction Points

The Italian release does not enumerate any frictions or challenges. The ~9-month interval between the July 2025 arrest and the April 2026 extradition is consistent with normal Italian extradition timelines; no specific challenge is asserted.

## Lessons Learned

- **Partner-state primary-source documentation is non-redundant.** The US DOJ release summarises Italian participation as a single phrase ("Italian National Police — Cyber Division"), whereas the Italian release names six distinct Italian agencies/authorities and the full judicial-political authorisation chain. For wiki integrity, both sides of an extradition operation must be ingested separately.
- **Italian extradition authorisation chain pattern** (Corte d'Appello di Milano + Ministro della giustizia) is reusable as a template for future Italian-side extradition operations.

## Follow-Up Actions

- US-side proceedings tracked under [[us-v-xu-zewei-hafnium-extradited-italy]].
- Italian-side judicial documents (Corte d'Appello di Milano extradition opinion + Ministro della giustizia decree) may become publicly accessible through Italian judicial transparency channels and would justify a future enrichment pass.
- Co-defendant **Zhang Yu** (named in the US indictment) **remains at large** per the parallel US DOJ release; not addressed in the Italian release.

## Korean Involvement (한국의 참여)

South Korea is not named in the Italian release as a victim, source, or cooperation jurisdiction. The HAFNIUM Microsoft Exchange compromise was *almost certainly* (>95%) global in scope and *likely* (55–80%) included Korean victim organisations given the global Microsoft Exchange installed base, but no Korean operational cooperation in this specific extradition operation is named.

## Contradictions & Open Questions

- The Italian release uses initials only (**"X. Z."**); the US DOJ release names **Xu Zewei** explicitly. The match is **highly likely** (80–95%) given the same-date publication, the matching arrest location (Italy), the matching arrest month (July 2025), the matching campaign (HAFNIUM), the matching defendant nationality (PRC), and the matching destination jurisdiction (Texas court). No contradiction, but the formal identity binding rests on the US-side naming.
- The Italian release does not enumerate the exact arrest date in July 2025; the US DOJ release also does not enumerate the exact day.
- The Italian release does not enumerate the exact extradition execution date; the US DOJ release indicates the weekend of 2026-04-25/26 but neither side gives a specific calendar day.
- The Italian release does not name the underlying US indictment number or charging document; the US DOJ release identifies it as press release 26-404 in S.D. Texas.
- The Italian release uses the phrase "ex general manager di una importante società tecnologica di Shanghai" (former general manager of an important technology company in Shanghai), which **likely** corresponds to Shanghai Powerock Network Co. Ltd. (the PRC enabling company named in the US indictment), but the Italian release does **not** name Powerock — so the "ex general manager" attribution remains an Italian-side characterisation that is not directly tied to a Powerock corporate role in the source.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti\|LA POLIZIA DI STATO ESEGUE L'ESTRADIZIONE DI UN PERICOLOSO HACKER CINESE]] | Polizia di Stato — Servizio Polizia Postale e per la Sicurezza Cibernetica | 2026-04-27 | https://www.commissariatodips.it/notizie/articolo/la-polizia-di-stato-esegue-lestradizione-di-un-pericoloso-hacker-cinese/index.html |
