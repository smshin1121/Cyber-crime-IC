---
type: operation
title: "Sofia Call-Centre Online Investment Fraud Takedown (BG-ES bilateral, December 2025)"
title_ko: "소피아 콜센터 온라인 투자사기 단속 작전 (불가리아-스페인 양자 공조, 2025-12)"
aliases:
  - "BTA Sofia call-centre investment fraud bust 2025-12-11"
  - "Sofia City Prosecutor's Office BG-ES Guardia Civil call-centre operation 2025"
  - "Bulgaria Spain bilateral call-centre fraud takedown December 2025"
case_id: CYB-2025-227
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - search-seizure
outcome: partial
timeframe:
  announced: 2025-12-12
  start: 2025-12-11
  end: 2025-12-11
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Organized crime group composed of Bulgarian and foreign nationals operating multiple call centres in Sofia and multiple websites used to deceive EU citizens into investing in fictitious trading in regulated financial instruments with promises of high returns; scheme operating since mid-2022"
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[bulgaria]]"
  - "[[spain]]"
participating_agencies:
  - "[[bulgaria-police]]"
  - "[[bulgaria-ministry-of-interior]]"
  - "[[spain-guardia-civil]]"
legal_basis:
  - "EU police cooperation mechanisms (general framework, no specific instrument named in the BTA announcement)"
  - "Bulgarian Penal Code investigation led by Sofia City Prosecutor's Office (SCPO)"
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "USD 230,000+ (one of five hardware wallets seized)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "More than 20 mobile phones seized"
    - "Numerous SIM cards seized"
    - "More than 30 USB flash drives seized"
    - "Personal computers, hard drives, notebooks, handwritten notes, lists of employees seized"
    - "Narcotics seized (quantity not specified)"
    - "17 investment gold bars seized, each valued at approximately BGN 7,000"
    - "More than BGN 45,000 in cash seized"
    - "Five hardware cryptocurrency wallets seized; one held >USD 230,000 in cryptoassets"
    - "Suspect count not published in the BTA announcement"
    - "Victim count not published; victims described as EU member state citizens"
edges:
  - source_actor: bulgaria
    target_actor: spain
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
credibility_index: 2.5
source_tier: 2
missing_fields:
  - "arrests"
  - "indictments"
  - "victims_notified"
  - "operation_codename"
  - "total_loss_estimate"
related_cases: []
related_operations:
  - "[[eurojust-600m-crypto-money-laundering-takedown-2025]]"
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2025-12-12_bta-bg_sofia-call-centre-bulgaria-spain-guardia-civil-investment-fraud]]"
created: 2026-05-10
updated: 2026-05-17
last_enriched: 2026-05-17
---

> [!info] Provisional / sparse-source page
> This page is published with a single tier-1/2 source (BTA news article relaying the Sofia City Prosecutor's Office announcement). Suspect count, victim count, and a total fraud-volume estimate are not stated in the available source. The page should be enriched once a Spanish Guardia Civil press release, Bulgarian SCPO official press release, or follow-on Eurojust/Europol report becomes available.

## Summary

On 2025-12-11, Bulgarian authorities led by the Sofia City Prosecutor's Office (SCPO), in close bilateral cooperation with Spain's Guardia Civil and within the framework of EU police-cooperation mechanisms, conducted a coordinated multi-agency operation against an organized crime group running fraudulent online investment platforms via call centres in Sofia. The action was announced by BTA (Bulgarian News Agency) on 2025-12-12 attributed to the SCPO.

The criminal network — described as composed of both Bulgarian and foreign nationals — had operated multiple websites since mid-2022 to lure EU member-state citizens into fictitious trading in regulated financial instruments with promises of high returns. Joint Bulgarian-Spanish teams executed the action under Bulgarian authority direction.

Seizures included over 20 mobile phones, numerous SIM cards, 30+ USB flash drives, personal computers, hard drives, notebooks, handwritten notes, employee lists, narcotics, 17 investment gold bars (~BGN 7,000 each), more than BGN 45,000 in cash, and 5 hardware cryptocurrency wallets — one containing cryptoassets worth more than USD 230,000.

The Bulgarian-side announcement does not publish an operation codename, suspect count, victim count, or total fraud-volume estimate. It does not connect this action to the broader Eurojust-coordinated 700-million-euro cryptocurrency-fraud takedown of October-November 2025, despite some surface-level similarity in modus operandi (call-centre social engineering against EU investment-fraud victims) — see Contradictions & Open Questions.

## Background

### Modus operandi

The targeted scheme, per the BTA-relayed SCPO account, is a **classic Bulgaria-hosted call-centre online investment-fraud (OIF) operation**, operating since **mid-2022**. The criminal pattern works as follows:

- **Lead generation via fictitious investment websites**: Multiple Bulgarian-hosted websites, marketed to EU member-state nationals (predominantly via affiliate-marketing channels), advertise "high-return" trading in *regulated financial instruments* (forex, CFDs, equities, commodities, increasingly cryptoassets). The websites display fabricated trading interfaces, fake performance dashboards, and forged regulatory credentials to project legitimacy.
- **Cold-call / boiler-room conversion**: Inbound leads from the websites are passed to call-centre agents in Sofia, who use **social-engineering scripts** (typical OIF "broker" / "account manager" / "senior trader" persona scripts) to walk victims through opening an account, making an initial small deposit, witnessing fabricated "winning trades" on the dashboard, then escalating to larger deposits.
- **Cash-out denial and fee extortion**: When victims attempt to withdraw funds, agents introduce a cascade of fabricated obstacles — "compliance fees," "tax withholdings," "regulator authorisation charges," "broker bonuses requiring volume" — to extract additional payments before disappearing. This pattern is the canonical "online investment scam" / "boiler room fraud" modus operandi recognised by EU LE and identical in structure to the larger Eurojust-coordinated EUR 700M cryptocurrency-fraud network (see [[eurojust-600m-crypto-money-laundering-takedown-2025]]).

The Sofia call-centres functioned as the **production floor** of the scheme; victim deposits flowed into Bulgarian or other EU-based payment-processor / e-money / shell-company rails before being converted partly into cryptoassets (evidenced by seizure of 5 hardware cryptocurrency wallets), partly into physical gold (17 investment gold bars seized), and partly into cash.

### Victim profile and impact

Victims are **EU member-state citizens** — the BTA report does not enumerate specific source jurisdictions. By analogy with the 2023 Bulgaria-Germany-Greece scams and the Eurojust 700M network, the typical victim demographic of Bulgaria-hosted OIF call-centre operations is **40-70-year-old EU residents responding to online advertising for high-return trading**, with per-victim losses in the range EUR 5,000-100,000+, occasionally far higher when fee-cascade extortion extracts retirement savings. **Neither a verified victim count nor a total-loss estimate is published** in the BTA report; both fields are recorded under `missing_fields`. The mid-2022 scheme start-date and the scale of seized infrastructure (20+ phones, 30+ USB drives, 5 hardware wallets, USD 230,000+ in one wallet alone) imply a victim base in at least the high-hundreds-to-thousands range, but this is not corroborated in the primary source and is **not asserted** here per L19.

### Financial flow

The seizure inventory itself maps the layering and integration stages of the scheme's value-extraction:

- **Layering into cryptoassets**: 5 hardware cryptocurrency wallets seized; **one wallet alone held more than USD 230,000 in cryptoassets** at seizure time. Hardware wallets are the canonical OCG-grade tool for storing the cryptoasset-converted share of victim deposits offline, beyond exchange seizure reach.
- **Layering into physical gold**: 17 investment gold bars, each valued at approximately BGN 7,000 (≈ EUR 3,575 each; aggregate ≈ BGN 119,000 / EUR 60,800). Investment gold is the canonical OCG-grade tool for non-bank, non-cryptoasset value storage with global liquidity.
- **Operating cash float**: more than BGN 45,000 in cash seized (≈ EUR 23,000), consistent with a call-centre's working-capital and small-bribe / agent-cash-pay buffer.
- **Operating infrastructure**: 20+ mobile phones (per-agent call equipment), numerous SIM cards (likely rotation for caller-ID spoofing and bypass of telecom anti-fraud blocking), 30+ USB drives (lead lists and victim CRM exports), personal computers and notebooks (CRM, dialler, dashboard-fabrication tooling), employee lists (call-centre payroll records).

Notably, narcotics were also seized — atypical for a pure call-centre OIF operation and a possible indicator of overlapping OCG activity or in-house agent supply. The total fraud volume is **not stated** in the primary source.

### Criminal organisation structure

The OCG is described in the BTA-relayed SCPO account as a **multi-tier organised crime group composed of both Bulgarian and foreign nationals**, operating multiple Sofia call centres and multiple websites in parallel since mid-2022. The structure inferable from the seizure inventory and the multi-call-centre / multi-website setup is the canonical Bulgaria-hosted boiler-room OCG pattern:

- **Foreign-national leadership / website operators** (often Israeli, Romanian, or Ukrainian nationals in comparable EU OIF networks) controlling the fictitious-investment websites, the affiliate-marketing lead flow, and the cryptoasset / gold layering.
- **Bulgarian-national call-centre management** running the Sofia floor operations, handling employee recruitment, employee payroll, and shift rotation across the multiple call centres.
- **Bulgarian-national agent layer** (the "brokers" / "account managers" / "senior traders") on the phones, working scripted social-engineering against the EU victim base.
- **Local Bulgarian facilitators**: payment-processor / e-money / shell-company operators converting victim card payments into cryptoasset and gold reserves.

**Specific suspect identities, suspect counts, and the foreign-national share of the OCG are not published** in the BTA report (consistent with the pre-charge SCPO procedural posture). The OCG-scale inference is therefore by analogy with comparable Bulgaria-hosted OIF takedowns rather than from the primary source.

### Series context

Bulgaria has a multi-year history of hosting call-centre-style investment-fraud operations targeting victims abroad — see prior takedowns referenced under [[bulgaria]] (online investment scams targeting Germany / Greece in 2023; the November 2025 Eurojust-coordinated 700M cryptocurrency-fraud network where Bulgaria participated in Phase 2 affiliate-marketing-infrastructure searches). The 2025-12-11 action represents a continued bilateral push with Spain — historically a frequent partner with Bulgaria in EU investment-fraud cases — through Spain's Guardia Civil rather than via the formal Eurojust/Europol coordination channel used in the parallel 700M operation.

## Participating Parties

**Lead jurisdiction:** Bulgaria (Sofia City Prosecutor's Office)

**Bulgarian agencies (per BTA):**

- Sofia City Prosecutor's Office (SCPO) — investigation lead and operational supervisor; the SCPO's investigative department also participated.
- National Investigation Service of Bulgaria — its Cybercrime Department assisted with seizures.
- State Agency for National Security (SANS — Bulgarian: Държавна агенция "Национална сигурност" / DANS).
- General Directorate for Combatting Organized Crime (GDCOC — Bulgarian: ГДБОП / GDBOP), within [[bulgaria-ministry-of-interior]] / [[bulgaria-police]].
- General Directorate National Police (GDNP), within [[bulgaria-ministry-of-interior]] / [[bulgaria-police]].

**Foreign partner:** [[spain-guardia-civil]] (Spain's Guardia Civil), via joint teams operating under Bulgarian authority direction within EU police-cooperation mechanisms.

> [!note] Translation note
> Bulgarian agency English names reflect BTA's English-language usage. The native Bulgarian abbreviations (ГДБОП for GDCOC, ДАНС for SANS) are sometimes rendered differently across translations.

## Legal Framework

The BTA announcement does not name a specific Council of Europe / EU instrument (no explicit reference to a [[joint-investigation-team|JIT]], [[european-investigation-order|EIO]], or [[mlat-process|MLAT]]). The announcement describes the joint Bulgarian-Spanish action only as conducted "in close international cooperation … and within the framework of EU police cooperation mechanisms." For the purposes of this page, the joint Bulgarian-Spanish team is treated as a bilateral cooperation under generic EU police-cooperation channels pending more precise instrument identification from a Spanish or Eurojust-side release.

## Operational Timeline

| Date | Event | Source |
|------|-------|--------|
| Mid-2022 | Beginning of the criminal scheme (per BTA) | BTA |
| 2025-12-11 | Sofia raid action day; joint Bulgarian-Spanish teams under SCPO direction; multi-agency searches and seizures | BTA |
| 2025-12-12 | BTA publishes report of the SCPO announcement | BTA |

## Results and Impact

Seizures (full enumeration, per BTA):

- More than 20 mobile phones
- Numerous SIM cards
- More than 30 USB flash drives
- Personal computers, hard drives, notebooks, handwritten notes, employee lists
- Narcotics (quantity not specified)
- 17 investment gold bars, each valued at approximately BGN 7,000 (≈ approx. EUR 3,575 each at ~1 EUR = 1.96 BGN; aggregate ≈ BGN 119,000 / EUR 60,800)
- More than BGN 45,000 in cash
- 5 hardware cryptocurrency wallets — one containing cryptoassets worth over USD 230,000

Arrests, indictments, and victim counts are not stated. The page records 0 in those fields and lists them under `missing_fields`.

> [!warning] Restricted reporting
> The BTA report does not publish suspect identities, suspect counts, or victim counts. This may reflect the early-stage criminal-procedure posture (pre-charge investigation under SCPO supervision) rather than a substantive absence of arrests. Fields should not be populated by inference.

## Cooperation Mechanisms Used

- Bilateral Bulgaria-Spain operational cooperation under generic EU police-cooperation mechanisms.
- The National Investigation Service Cybercrime Department was the principal Bulgarian technical-forensic body assisting search-and-seizure.

The announcement does not name Eurojust, Europol, INTERPOL, [[joint-investigation-team|JIT]], [[european-investigation-order|EIO]], or any specific [[mlat-process|MLAT]]. Operational specifics of the bilateral cooperation channel are not provided.

## Challenges and Friction Points

Per BTA, the network is described as composed of both Bulgarian and foreign nationals using "social engineering" to deceive EU member-state victims through fictitious trading in regulated financial instruments — typical patterns associated with cross-border investment-fraud cases that depend on Bulgaria-side technical infrastructure and Spain-side (or other EU) victim recruitment. Friction points are not enumerated in the source.

## Lessons Learned

Not stated in the source.

## Follow-Up Actions

Not stated in the source. Charging decisions and any extradition steps will likely emerge through subsequent SCPO releases or via a Spanish Guardia Civil counterpart announcement.

## Korean Involvement (한국의 참여)

None. There is no Korean involvement reported. Korean readers may note that the Sofia City Prosecutor's Office–led model — bilateral cooperation with a foreign police service via EU police-cooperation mechanisms, without a formal JIT — is structurally analogous to the Korean National Police Agency's bilateral cybercrime working-arrangement pattern with foreign agencies (e.g., Korea-China voice-phishing operations under bilateral arrangement rather than via a formal MLAT JIT).

## Contradictions & Open Questions

> [!warning] Possible relationship to the Eurojust 700M operation — pending verification
> The Eurojust-coordinated EUR 700-million cryptocurrency-fraud takedown of October-November 2025 (see [[eurojust-600m-crypto-money-laundering-takedown-2025]]) ran a Phase 2 search-and-seizure action against affiliate-marketing infrastructure in Belgium, Bulgaria, Germany, and Israel on 2025-11-25 to 2025-11-26. The 2025-12-11 SCPO operation occurred approximately two weeks later, also targets call-centre / online-investment-fraud infrastructure in Sofia, and also involves Bulgarian and EU-victim elements. The BTA announcement, however, does NOT mention Eurojust, Europol, France, Belgium, Cyprus, Germany, or Israel, and identifies cooperation only with Spain's Guardia Civil. Spain was involved in the Eurojust 700M Phase 1 (2025-10-27) but not in Phase 2. On the available evidence, treat this as a distinct standalone bilateral Bulgaria-Spain operation. Pending: a Spanish Guardia Civil press release or follow-on Eurojust/Europol release confirming or denying linkage.

> [!info] Open question — operation codename
> No operation codename is published in the BTA report. If a Spanish-side release uses a name (Spanish Guardia Civil typically codenames operations), align on that name and update aliases.

> [!info] Open question — suspect and victim counts
> BTA reports neither suspect counts nor victim counts. The Sofia City Prosecutor's Office may release this information at a later procedural stage (formal charges or remand hearings).

> [!info] L26 Background gap — victim count and total loss
> Neither a verified victim count nor a total-loss estimate is published in the BTA-relayed SCPO announcement. By analogy with the contemporaneous Eurojust 700M cryptocurrency-fraud takedown and prior Bulgaria-hosted OIF cases, a victim base in the high-hundreds-to-thousands and per-victim losses of EUR 5,000-100,000+ are *likely* (medium confidence), but neither is asserted on the page until a Spanish Guardia Civil release or follow-on SCPO formal-charge filing publishes the figures.

> [!info] L26 Background gap — OCG nationality composition
> The OCG is described as composed of "both Bulgarian and foreign nationals" but neither the foreign nationalities nor the leadership-versus-floor-agent split is enumerated in the primary source. Inferences in the Background section are by analogy with comparable Bulgaria-hosted OIF takedowns rather than from the primary source.

> [!info] L26 Background gap — narcotics-seizure context
> Narcotics were seized at the Sofia call-centre but no quantity, drug type, or relationship to the OIF scheme (in-house agent supply vs. overlapping OCG drug-trafficking sideline vs. unrelated tenant activity) is given. This is atypical for a pure boiler-room operation and warrants follow-on clarification.
