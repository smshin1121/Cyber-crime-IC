---
type: operation
title: "Operazione Cagliostro / Voltaiko Photovoltaic Ponzi — Italy–France Crypto-Wallet Freezing via Eurojust (USD 7.5M Seized, April 2026)"
title_ko: "오페라치오네 칼리오스트로 / Voltaiko 태양광 폰지 사기 — 이탈리아·프랑스 가상자산 동결 공조 (Eurojust 경유, 2026년 4월 7.5M USD 압수)"
aliases:
  - "Operazione Cagliostro"
  - "Voltaiko Ponzi case"
  - "Voltaiko photovoltaic fraud"
  - "Italy USD 7.5M crypto seizure 2026"
  - "Italy-France crypto wallet freezing 2026 Eurojust"
case_id: CYB-2026-275
period: 3
operation_type: joint-investigation
operation_role: standalone
parent_operation: ""
status: ongoing
enforcement_type:
  - asset_freeze
  - seizure
outcome: partial
credibility_index: 4.4
source_tier: 1
edges:
  - source_actor: "[[polizia-di-stato]]"
    target_actor: "[[italy-polizia-postale]]"
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: "[[italy]]"
    target_actor: "[[france]]"
    cooperation_type: asset_recovery
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: "[[eurojust]]"
    target_actor: "[[italy]]"
    cooperation_type: technical_assistance
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: "[[eurojust]]"
    target_actor: "[[france]]"
    cooperation_type: technical_assistance
    legal_basis: bilateral_MOU
    direction: undirected
missing_fields:
  - "names of specific French judicial authorities involved (release names only 'autorita' francesi competenti', no individual French agency)"
  - "exact crypto-exchange platform(s) on which wallets were located in France"
  - "arrest counts (release does not enumerate any arrests as of 2026-04-29; the announced action is a seizure / asset-freezing, not an arrest sweep)"
  - "indictment counts / suspects' identities (release does not name suspects or indictments)"
  - "specific Italian Criminal Code articles or French Penal Code articles invoked"
timeframe:
  announced: 2026-04-29
  start: 2025-10
  end: ""
  ongoing: true
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
crime_type: "[[online-fraud-ic]]"
target_entity: "Transnational organised criminal group running an online photovoltaic-investment Ponzi scheme branded 'Voltaiko' (website voltaiko.com) that allegedly defrauded approximately 6,000 Italian retail investors by promising returns from purported 'green' photovoltaic infrastructure investments abroad which were in fact non-existent, then converting fraud proceeds into cryptocurrency on exchange platforms — including wallets located in French jurisdiction — to obstruct traceability and enable money-laundering. No suspect identities are published in the Italian primary source as of 2026-04-29."
lead_agency: "[[polizia-di-stato]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[italy]]"
  - "[[france]]"
participating_agencies:
  - "[[polizia-di-stato]]"
  - "[[italy-polizia-postale]]"
  - "[[eurojust]]"
legal_basis:
  - "[[asset-freezing]]"
  - "[[european-investigation-order]]"
mechanisms_used:
  - "[[asset-freezing]]"
  - "[[eurojust-coordination-meeting]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 1
  cryptocurrency_seized: "USD 7.5+ million (reported by Polizia di Stato as the largest cryptocurrency seizure ever performed in Italy)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "95 bank accounts frozen (in earlier phases since October 2025)"
    - "voltaiko.com website obscured / taken offline"
    - "2 villas seized in Rimini province"
    - "Electronic devices, luxury goods and gold bullion seized"
    - "Total non-crypto seizures since October 2025: approximately EUR 2 million"
related_cases:
related_operations:
  - "[[de-ch-crypto-mixer-takedown-2025]]"
  - "[[eurojust-100m-crypto-investment-fraud-takedown-2025]]"
  - "[[greek-daoe-crypto-investment-fraud-2026]]"
challenges_encountered:
lessons_learned:
  - "Italian Eurojust desk acting as supranational coordinator for cross-border cryptocurrency-wallet freezing is a recurring pattern in 2025–2026 Italian-led investment-fraud takedowns; this case extends that pattern to France."
  - "USD 7.5 million crypto seizure is described by the Italian Postal Police as the single largest crypto seizure ever performed in Italy as of April 2026, providing a benchmark for future Italian asset-recovery operations."
source_count: 1
sources:
  - "[[2026-04-29_poliziadistato-it_operazione-cagliostro-fotovoltaico-cripto-italia-francia]]"
created: 2026-05-10
updated: 2026-05-10
---
> [!info] Provisional / sparse-source page
> This page is built from a **single tier-1 primary source** (Polizia di Stato press release, 2026-04-29). The investigation is **ongoing** as of the publish date; no arrests, no indictments and no defendant identities are published. French primary-source corroboration of the cooperation is not available because the release names only "le autorita' francesi competenti" (the competent French authorities) without identifying a specific French agency, and as of 2026-05-10 no French primary source mirrors the Italian release. Treat all numeric / temporal claims as provisional pending a second independent primary source — for example a future Eurojust press release, a French Procureur de la Republique announcement, or an Italian Procura di Bologna update.

## Summary

On **2026-04-29**, the [[polizia-di-stato|Polizia di Stato]] (Italian National Police), through its [[italy-polizia-postale|Polizia Postale (Servizio polizia postale e per la Sicurezza cibernetica)]] cyber unit and the COSC Emilia-Romagna cyber operations centre, jointly with the Guardia di Finanza Comando provinciale di Bologna and under the coordination of the **Procura della Repubblica di Bologna**, announced the seizure of more than **USD 7.5 million in cryptocurrency** in operation **"Cagliostro"**. The Polizia di Stato press release describes this as the single largest cryptocurrency seizure ever performed in Italy (almost certainly true within Italy on the basis of this Italian-side official statement).

The seized cryptocurrencies are part of the illicit proceeds of the **"Voltaiko" transnational Ponzi scheme** (website: voltaiko.com), which allegedly defrauded approximately **6,000 Italian retail investors** by inducing them to transfer money in exchange for promised returns on supposed "green" photovoltaic-infrastructure investments abroad — investments that were, in fact, non-existent. To obstruct traceability and enable subsequent money-laundering, the fraud proceeds were transferred onto cryptocurrency-exchange platforms and converted into virtual currency, with at least some of the resulting digital wallets located in **French jurisdiction**.

The release explicitly acknowledges the international-cooperation chain: **the Italian desk at [[eurojust|Eurojust]] handled supranational coordination for executing the cryptocurrency-asset-freezing orders and maintained contacts with the competent French authorities, enabling the freezing of the digital wallets**. This is the L24-qualifying ≥2-country IC element of the operation: Italy LE / prosecutorial (Polizia di Stato + Guardia di Finanza + Procura Bologna) + France LE / judicial authorities (unnamed individually, but explicitly characterised as cooperating counterparts via Eurojust), with cooperation explicitly acknowledged in the tier-1 primary source.

## Background

The investigation was opened by the Procura della Repubblica di Bologna in **October 2025** following indications that an organised criminal group was running a transnational online-investment-fraud scheme advertising "green" photovoltaic investments abroad. The Postal Police, the Emilia-Romagna Cybersecurity Operations Centre and the Guardia di Finanza Bologna built a joint financial-and-cyber investigation that integrated traditional economic-financial competencies with advanced cyber-investigation techniques to identify the illicit proceeds, reconstruct flows, and trace conversion into cryptocurrency.

By the time of the 2026-04-29 announcement, the earlier phases of the operation had already produced:

- The **website voltaiko.com** obscured (taken offline)
- **95 bank accounts** frozen
- **Two villas** in Rimini province seized
- Electronic devices, luxury goods, and gold bullion seized
- Total non-crypto asset value: approximately **EUR 2 million**

The 2026-04-29 announcement adds the USD 7.5+ million crypto seizure on top of these earlier results.

## Participating parties

### Italy

- **[[polizia-di-stato|Polizia di Stato]]** (Italian National Police), through:
  - **Servizio Polizia Postale e per la Sicurezza Cibernetica** ([[italy-polizia-postale|Postal Police and Cybersecurity Service]]) — lead cyber-investigation unit
  - **Centro Operativo per la Sicurezza Cibernetica Emilia-Romagna (COSC Emilia-Romagna)** — regional cyber-operations support
- **Guardia di Finanza** — **Comando provinciale di Bologna** (Italian Financial Guard, Bologna provincial command — financial-economic investigative arm). *No standalone wiki page yet for Guardia di Finanza; described here in prose per LESSONS.md L23.*
- **Procura della Repubblica di Bologna** (Public Prosecutor's Office of Bologna) — lead prosecutor coordinating the joint investigation. *No standalone wiki page yet; described here in prose per LESSONS.md L23.*

### France

- **"Le autorita' francesi competenti"** — competent French judicial authorities (not named individually in the Italian primary source). Their role per the press release is to execute the cryptocurrency-asset-freezing orders within French jurisdiction, where the digital wallets are located.

### Coordinator

- **[[eurojust|Eurojust]]** — through its **Italian desk**, which the press release explicitly identifies as the body that "handled supranational coordination for executing the crypto-freezing orders and maintained contacts with the competent French authorities."

## Legal framework

The Italian primary source does not cite specific Italian Criminal Code or French Penal Code articles. The operational framing is consistent with Italian transnational fraud + money-laundering investigations under standard articles for:

- Italian Criminal Code (Codice Penale): truffa aggravata (aggravated fraud, art. 640) and riciclaggio (money laundering, art. 648-bis) — *not explicitly cited; inference from operational pattern.*
- The international cooperation channel is Eurojust judicial coordination — coherent with the [[european-investigation-order|European Investigation Order]] / [[asset-freezing|asset-freezing]] regime for cross-border judicial cooperation between Italy and France within the EU framework. *Specific instrument not cited in the release.*

> [!warning] Legal status check needed
> The Italian primary source does not cite specific articles or treaty instruments. The framing above is inferred from operational pattern and standard Italy-France EU judicial-cooperation mechanisms. Re-verify against any subsequent Eurojust press release or Italian Ministero della Giustizia statement.

## Operational timeline

| Date | Event |
|---|---|
| 2025-10 | Investigation opened by Procura della Repubblica di Bologna |
| 2025-10 → 2026-04 | Early operational phases: voltaiko.com taken offline; 95 bank accounts frozen; 2 Rimini villas seized; electronic devices, luxury goods and gold bullion seized; total ≈ EUR 2 million |
| 2026-04-29 (announced) | USD 7.5+ million cryptocurrency seizure executed via Italy → France judicial-cooperation chain coordinated by the Italian Eurojust desk; public announcement by Polizia di Stato |

## Results and impact

- **Cryptocurrency seized**: USD 7.5+ million — described by Polizia di Stato as the single largest crypto seizure ever performed in Italy.
- **Earlier non-crypto seizures**: ~EUR 2 million (95 bank accounts frozen; 2 Rimini villas; electronic devices; luxury goods; gold bullion).
- **Domain action**: voltaiko.com obscured.
- **Estimated victims**: ~6,000 Italian retail investors. Per-victim recovery prospects are not addressed in the release.
- **Arrests / indictments**: none enumerated in this release (the investigation is ongoing).

## Cooperation mechanisms used

- **Eurojust judicial coordination** — the Italian Eurojust desk acted as the cross-border judicial-cooperation conduit between the Italian investigators / Procura Bologna and the competent French authorities for executing the cryptocurrency-asset-freezing orders.
- **Asset-freezing** ([[asset-freezing|cross-border asset-freezing]]) — applied to digital wallets located in French jurisdiction.
- **Implicit instrument** (not explicitly named in the release): EU-internal judicial-cooperation mechanisms — most likely the [[european-investigation-order|European Investigation Order]] regime, which is the standard EU-internal channel for asset-freezing measures in another Member State; this is highly likely (80–95%) given the case is intra-EU and Eurojust-coordinated, but not asserted in the primary source.

## Challenges and friction points

- **Cryptocurrency-tracing complexity** — fraud proceeds were converted into virtual currency on exchange platforms specifically to frustrate traceability. The Italian-side press release frames the integration of "traditional economic-financial competencies and advanced cyber-investigation techniques" by Polizia Postale + COSC Emilia-Romagna + Guardia di Finanza Bologna as the technical solution.
- **Cross-border crypto-wallet freezing** — required Italian → French judicial cooperation through Eurojust to reach wallets located in French jurisdiction; resolution time from investigation opening (October 2025) to crypto seizure (April 2026) is roughly six months, consistent with the typical Eurojust-coordinated EU-internal asset-freezing timeline.
- **Suspect attribution / arrests** — as of 2026-04-29, no suspect identities or arrest counts are public. Whether the underlying network has been dismantled or whether the seizure precedes future enforcement actions is not stated in the release.

## Lessons learned

- The Italian Eurojust desk's role as supranational coordinator for cross-border cryptocurrency-asset-freezing is a recurring pattern in 2025–2026 Italian-led investment-fraud takedowns; this case extends that pattern to France specifically.
- The USD 7.5 million crypto seizure represents a benchmark for the largest single-operation crypto seizure performed by Italian authorities as of April 2026 (per the Italian primary source's framing). Future Italian asset-recovery operations exceeding this threshold should be flagged.
- The operational sequence — domain takedown + bank-account freezing + physical-asset seizure first, cryptocurrency-wallet freezing later (after cross-border judicial cooperation completes) — illustrates the practical sequencing of a Eurojust-coordinated crypto-investment-fraud takedown when the wallets are in another EU Member State.

## Follow-up actions

- Watch for a French primary-source release (Parquet de Paris JUNALCO or competent French Procureur) which would name the French agency and confirm the French-side legal basis.
- Watch for a subsequent Eurojust press release that may name the specific French agencies and the EU instrument invoked.
- Watch for arrest / indictment announcements by Procura di Bologna which would update arrest / indictment counts here.

## Korean involvement (한국의 참여)

None reported. This is an EU-internal Italy ↔ France judicial-cooperation case with no Korean participants or victim cohort identified in the primary source.

## Contradictions and open questions

- **Crypto-seizure-record claim** — the press release states this is "the most significant cryptocurrency seizure ever effected in Italy". This is *almost certainly true* within Italy at the level of a single operation, but the release does not benchmark against multi-year aggregate seizures or against international peers; do not over-extrapolate.
- **L24 boundary** — France is named as cooperating jurisdiction via "le autorita' francesi competenti" without an individual French agency. This satisfies L24's requirement that ≥2 countries' LE / prosecutorial cooperation be explicitly acknowledged in the tier-1 primary source (since "competent French authorities" + the explicit Eurojust contact-channel sentence is an explicit acknowledgement), but the lack of a named French agency means the page should be re-verified once a French primary source becomes available.
- **Legal-basis specificity** — the underlying EU instrument used to execute the freezing order in France is not named (most likely European Investigation Order; possibly Mutual Legal Assistance bilateral channel). Re-verify against later Eurojust or French primary source.
