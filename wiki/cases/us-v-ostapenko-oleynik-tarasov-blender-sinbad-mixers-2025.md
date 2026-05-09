---
type: case
title: "United States v. Ostapenko, Oleynik, and Tarasov (Blender.io / Sinbad.io mixers)"
case_number: "Indictment returned 2025-01-07 (sealed); unsealed 2025-01-10 (N.D. Ga.)"
jurisdiction: "U.S. District Court for the Northern District of Georgia"
jurisdiction_country: "[[united-states]]"
jurisdictions:
  - "[[united-states]]"
  - "[[russia]]"
  - "[[netherlands]]"
  - "[[finland]]"
case_type: prosecution
status: arrested
crime_charged:
  - "[[money-laundering-ic]]"
  - "[[ransomware-ic]]"
defendants:
  - name: "Roman Vitalyevich Ostapenko"
    nationality: "Russian"
    age: 55
    status: "arrested 2024-12-01 (Netherlands FIOD / Finland NBI / FBI coordinated action); pretrial"
    sentence: ""
    location_at_arrest: "Not specified in DOJ release; arrest effected by Netherlands FIOD and Finnish NBI"
    charges:
      - "18 U.S.C. § 1956(h) — conspiracy to commit money laundering (1 count)"
      - "18 U.S.C. § 1960 — operating an unlicensed money transmitting business (2 counts)"
  - name: "Alexander Evgenievich Oleynik"
    nationality: "Russian"
    age: 44
    status: "arrested 2024-12-01 (Netherlands FIOD / Finland NBI / FBI coordinated action); pretrial"
    sentence: ""
    location_at_arrest: "Not specified in DOJ release"
    charges:
      - "18 U.S.C. § 1956(h) — conspiracy to commit money laundering (1 count)"
      - "18 U.S.C. § 1960 — operating an unlicensed money transmitting business (1 count)"
  - name: "Anton Vyachlavovich Tarasov"
    nationality: "Russian"
    age: 32
    status: "at large (fugitive as of 2025-01-10)"
    sentence: ""
    location_at_arrest: ""
    charges:
      - "18 U.S.C. § 1956(h) — conspiracy to commit money laundering (1 count)"
      - "18 U.S.C. § 1960 — operating an unlicensed money transmitting business (1 count)"
related_operation: "[[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]]"
ic_elements:
  mlat_requests: []
  extradition: "Pending — extradition path from Netherlands and/or Finland to United States anticipated; not yet effected as of source date"
  evidence_from_abroad:
    - "[[netherlands]]"
    - "[[finland]]"
  foreign_arrests:
    - "[[netherlands]]"
    - "[[finland]]"
  asset_freezing: []
cooperating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
  - "[[netherlands-fiod]]"
  - "[[finland-nbi]]"
  - "[[us-treasury]]"
legal_frameworks_invoked:
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[money-laundering-ic]]"
  - "[[extraterritorial-jurisdiction]]"
precedent_value: "Likely significant — first U.S. federal prosecution of operators of a Treasury-sanctioned (Sinbad) cryptocurrency mixer where arrests were effected by foreign police partners (Netherlands FIOD + Finland NBI) for non-host-state Russian defendants. Confidence: medium-high; precedent value is contingent on extradition outcomes and conviction."
source_count: 1
sources:
  - "[[2025-01-10_justice-gov_operators-cryptocurrency-mixers-blender-sinbad-charged-money-laundering]]"
created: 2026-05-09
updated: 2026-05-09
---

## Summary

On 10 January 2025 the U.S. Department of Justice unsealed an indictment, returned by a federal grand jury in the [[united-states|U.S.]] District Court for the Northern District of Georgia on 7 January 2025, charging three Russian nationals — **Roman Vitalyevich Ostapenko (55)**, **Alexander Evgenievich Oleynik (44)**, and **Anton Vyachlavovich Tarasov (32)** — with conspiracy to commit money laundering and operating an unlicensed money transmitting business in connection with the cryptocurrency mixers **Blender.io** and its alleged successor **Sinbad.io**. Two of the three defendants (Ostapenko and Oleynik) were arrested on 1 December 2024 in a coordinated international operation conducted by the [[netherlands-fiod|Netherlands Fiscal Information and Investigative Service (FIOD)]] and the [[finland-nbi|Finnish National Bureau of Investigation (NBI)]] in cooperation with the [[fbi|FBI]]; Tarasov remains at large. The case is highly likely to set important precedent on the criminal liability of operators of Treasury-sanctioned cryptocurrency mixing services and on multi-jurisdictional arrest patterns where the home state ([[russia]]) does not cooperate.

## Facts

According to the DOJ release of 10 January 2025:

- The defendants are alleged to have operated **Blender.io** as a cryptocurrency mixing service from approximately 2018 through April 2022. Blender.io was marketed with a "no logs" policy and active deletion of transaction traces.
- Blender.io ceased operations approximately one month before the U.S. Department of the Treasury [[us-treasury|Office of Foreign Assets Control]] sanctioned it on 6 May 2022 — the first such designation of a virtual-currency mixer.
- The same operators are alleged to have relaunched the service in approximately October 2022 under the name **Sinbad.io**. Blockchain-analytics firm Elliptic (February 2023) had previously identified Sinbad as a likely Blender successor; the indictment now formally adopts that succession theory.
- Sinbad.io infrastructure was seized and the entity sanctioned by OFAC on 29 November 2023 (see [[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]]).
- DOJ alleges the mixers laundered proceeds of cryptocurrency thefts attributed to Lazarus Group / [[north-korea|DPRK]] state-sponsored hacking — most notably the Axie Infinity Ronin Bridge heist of approximately USD 620 million (March 2022, laundered through Blender.io). Treasury's 2023 designation also linked Sinbad to DPRK proceeds from the Horizon Bridge (~USD 100M, June 2022) and Atomic Wallet (~USD 100M, June 2023) thefts.
- The mixers are also alleged to have laundered ransomware proceeds, including those of TrickBot, Conti (formerly Ryuk), Sodinokibi (REvil), and GandCrab.

> [!warning] Indictment is an accusation
> The defendants are presumed innocent. All facts above are *as alleged* by the United States in the unsealed indictment.

## International Cooperation Elements

### Evidence Gathering

The release does not disclose specific MLAT or production-order traffic. Available information indicates a multi-year, [[informal-cooperation|informal multilateral coordination]] track involving the [[fbi|FBI]] (Atlanta Field Office), [[netherlands-fiod|Netherlands FIOD]], [[finland-nbi|Finnish NBI]], the Australian Federal Police, and the U.S. Treasury [[us-treasury|OFAC]] sanctions track that began with the Blender designation in May 2022 and continued through the Sinbad seizure in November 2023. Blockchain analytics provided by private-sector partners (Elliptic publicly; others not named in the release) likely contributed evidence of the Blender-to-Sinbad operational succession; this remains an analytical inference (confidence: medium).

### Arrest and Extradition

The 1 December 2024 arrests of Ostapenko and Oleynik form a **discrete tri-national arrest pattern**: investigative coordination by the [[fbi|FBI]] with the [[netherlands-fiod|Netherlands FIOD]] (a financial-investigation rather than general police body, reflecting the financial nature of the offense) and the [[finland-nbi|Finnish NBI]] (general criminal-police body for serious organized crime), with the arrests effected on EU territory. The DOJ release does not specify in which of the two states each defendant was apprehended. Extradition to the United States is anticipated but had not been effected as of the 10 January 2025 release; [[russia]] does not extradite its nationals, so the defendants' presence on Dutch and/or Finnish soil was the necessary precondition for any U.S. prosecution to proceed.

Tarasov's status as a fugitive most likely reflects his presumed presence inside Russia (confidence: medium; the release does not address his location).

### Asset Recovery

The release does not announce specific asset seizures concurrent with the indictment unsealing. The November 2023 Sinbad infrastructure seizure (executed under a separate Treasury / interagency action, not detailed in this case page) preceded these arrests by roughly thirteen months.

## Legal Analysis

### Jurisdiction

U.S. jurisdiction is asserted on extraterritorial effects principles standard in §1956 / §1960 mixer prosecutions: U.S.-located customers, U.S. dollar nexus, and U.S. correspondent banking touchpoints. The defendants' conduct outside the United States is reachable under the broad reach of [[extraterritorial-jurisdiction|§ 1956's extraterritorial provisions]] (§ 1956(f)) when funds or any part of the conduct touches the U.S. financial system.

### Key Legal Issues

- **18 U.S.C. § 1956(h) — money laundering conspiracy**: penalty up to 20 years per count.
- **18 U.S.C. § 1960 — operating an unlicensed money transmitting business**: penalty up to 5 years per count. Section 1960 is a strict-liability-style offense in the registration prong: operation of a money-transmission service touching the United States without FinCEN registration is punishable regardless of whether knowledge of illicit funds is proved. Mixer prosecutions typically anchor on this statute.
- **Sanctions interaction**: although the indictment as charged is a money-laundering / unlicensed-MSB case, the parallel OFAC sanctions on Blender.io (May 2022) and Sinbad.io (November 2023) provide an interagency frame and likely supplied investigative leads.
- **Tri-national arrest of Russian nationals on EU territory**: the case demonstrates that U.S. prosecutors continue to rely on travel-pattern arrest opportunities to circumvent the Russia-extradition gap, a recurring [[informal-cooperation|informal cooperation]] pattern across cyber prosecutions.

### Precedent Value

Likely significant. Confidence: medium-high. The case extends to active operators of a Treasury-sanctioned mixer and depends on EU-state cooperation against Russian nationals. Final precedent value will turn on (i) whether the Netherlands and/or Finland extradite the defendants to the United States, and (ii) the legal theories that survive any pretrial litigation on extraterritoriality and § 1960 scope.

## Proceedings Timeline

| Date | Event |
|---|---|
| 2018 | Blender.io launches as a cryptocurrency mixer (per indictment). |
| 2022-03 | Lazarus Group / DPRK Axie Infinity Ronin Bridge heist (~USD 620M); DOJ alleges proceeds laundered through Blender.io. |
| 2022-04 | Blender.io ceases operations. |
| 2022-05-06 | OFAC sanctions Blender.io — first virtual-currency-mixer designation. |
| 2022-10 | Sinbad.io launches (alleged Blender successor under same operators). |
| 2023-02 | Elliptic publishes analysis identifying Sinbad as likely Blender successor. |
| 2023-11-29 | OFAC sanctions Sinbad; infrastructure seized in coordinated U.S./international action ([[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]]). |
| 2024-12-01 | Ostapenko and Oleynik arrested in coordinated [[netherlands-fiod|Netherlands FIOD]] / [[finland-nbi|Finland NBI]] / [[fbi|FBI]] action. |
| 2025-01-07 | Indictment returned (sealed) by federal grand jury, [[united-states|N.D. Ga.]] |
| 2025-01-10 | Indictment unsealed; DOJ press release. Tarasov remains at large. |

## Cooperation Effectiveness

The pre-arrest investigative phase — running from the May 2022 Blender designation through the December 2024 arrests — illustrates an effective sanctions-to-indictment-to-arrest sequence across U.S. interagency partners ([[us-treasury|Treasury OFAC]], [[fbi|FBI]], [[us-doj|DOJ]] [[office-of-international-affairs|OIA]]) and EU financial / police authorities ([[netherlands-fiod|Netherlands FIOD]], [[finland-nbi|Finnish NBI]]). The ~31-month interval from initial mixer designation to arrest of operators is in line with comparable cyber-monetization timelines; speed cannot be the metric for evaluation given the tradecraft pseudonymity of mixer operators.

The case **does not** demonstrate cooperation with [[russia]]; it demonstrates effective cooperation *around* Russia, conditioned on the defendants' physical presence on EU territory.

## Korean Relevance (한국 관련성)

[[south-korea|South Korea]] is not a participating jurisdiction in this case. The case is nonetheless significant for Korea-related cooperation analysis in two respects (confidence: medium-high):

1. **Lazarus Group / [[north-korea|DPRK]] monetization nexus.** South Korea is a frequent target of Lazarus Group cryptocurrency theft and a long-standing cooperation partner of the [[fbi|FBI]] on DPRK-attributed cyber actor tracking. This case adds Russian-national service operators to the U.S. enforcement perimeter around DPRK virtual-currency monetization, indirectly reinforcing the legal frame within which Korean authorities cooperate.
2. **Mixer-operator liability template.** The legal theory of charging mixer operators under 18 U.S.C. §§ 1956(h) and 1960 establishes a U.S. template that may inform parallel Korean authorities' approaches when virtual-asset service providers operating outside Korean licensing reach are identified as conduits for ransomware and DPRK-attributed proceeds. Korea's 2020 Specified Financial Information Act (특정금융정보법) imposes registration obligations on virtual-asset service providers; a comparable structural argument is in principle available to Korean prosecutors.

## Contradictions & Open Questions

> [!warning] Source-of-record correction
> The project intake brief identified the issuing district as the Northern District of Florida (USAO-NDFL). Verified against the DOJ press release (mirrored at globalsecurity.org), corroborating reporting (The Hacker News 2025-01-11), and the named U.S. Attorney (Ryan K. Buchanan, [[united-states|N.D. Ga.]] at the time), the **correct district is the Northern District of Georgia**. The intake brief's district has been overridden in this page.

Open questions:

- Where exactly were Ostapenko and Oleynik arrested — Netherlands, Finland, or split between the two?
- Will Dutch / Finnish courts grant extradition to the United States, and on what timeline?
- Has any Korean victim entity been identified in the U.S. forfeiture / restitution scope, given the Lazarus Group nexus?
- What additional defendants, if any, are under sealed investigation in successor matters?

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operators of Cryptocurrency Mixers Charged with Money Laundering | U.S. Department of Justice | 2025-01-10 | https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering |
