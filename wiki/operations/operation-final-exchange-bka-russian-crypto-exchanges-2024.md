---
type: operation
title: "Operation Final Exchange — 47 Russian-language no-KYC cryptocurrency exchanges seized (BKA / ZIT, 2024-09-19)"
title_ko: "Operation Final Exchange — 47개 러시아어권 무-KYC 암호화폐 거래소 인프라 압수 (독일 BKA / ZIT, 2024-09-19)"
aliases:
  - "Operation Final Exchange"
  - "BKA Final Exchange takedown"
  - "Final Exchange (BKA)"
  - "47 Russian-language no-KYC crypto exchange seizure"
  - "BKA / ZIT 2024 cryptocurrency exchange takedown"
case_id: CYB-2024-099
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2024-09-19
  start: 2024-09-19
  end: 2024-09-19
  ongoing: false
crime_types:
  - "[[money-laundering-ic]]"
  - "[[ransomware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
crime_type: "[[money-laundering-ic]]"
target_entity: "47 Germany-hosted Russian-language no-KYC cryptocurrency exchange services collectively serving as an instant-swap money-laundering layer for the cybercrime underground economy. Named exchanges include Xchange.cash, Bankcomat.com, 60cek.org, CoinBlinker.com, Cryptostrike, Baksman, Prostocash, and Multichange.net. Top three by transaction volume: Xchange.cash, 60cek.org, Bankcomat.com. Xchange.cash had approximately 410,000 user accounts and ~1.28–1.3 million transactions processed. Bankcomat.com had been operating since 2012."
lead_agency: "[[germany-bka]]"
coordinating_body: "[[zit-frankfurt]]"
participating_countries:
  - "[[germany]]"
  - "[[russia]]"
participating_agencies:
  - "[[germany-bka]]"
legal_basis:
  - "[[money-laundering-ic|§ 261 StGB (Geldwäsche)]]"
  - "[[cybercrime-infrastructure-ic|§ 127 StGB (Betreiben krimineller Handelsplattformen im Internet)]]"
mechanisms_used:
  []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 47
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "47 Germany-hosted no-KYC cryptocurrency exchange services shut down on 19 September 2024"
    - "Development servers, production servers, and backup servers seized across the targeted platforms"
    - "Transaction data, registration data, and IP addresses secured for downstream investigations"
    - "Splash banner placed on seized domains via finalexchange.de and www.bka.de/finalexchange"
    - "Single largest cluster of cryptocurrency-exchange infrastructure seized in a single BKA action to date"
    - "Xchange.cash alone: approximately 410,000 user accounts and ~1.28–1.3 million transactions processed (per Chainalysis / The Record)"
    - "Bankcomat.com operating since 2012 — 12-year operational history at time of seizure"
    - "Chainalysis on-chain analysis: 17 of the 47 exchanges had months in which >50% of direct inflows came from illicit sources; 12 had months with >30% from darknet markets; 6 had months with >30% from stolen funds"
edges:
  - source_actor: Germany-BKA
    target_actor: ZIT-Frankfurt
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
credibility_index: 3.8
source_tier: 1
missing_fields:
  - "specific operator names (no arrests enumerated in the 2024-09-19 release)"
  - "specific server count seized (release describes development/production/backup tiers but does not give an integer total)"
  - "complete list of all 47 exchange names (BKA release names a subset; Chainalysis on-chain analysis reaches a fuller subset but no fully consolidated 47-name list is public)"
  - "cryptocurrency seizure value (no value disclosed in the BKA release; this was an infrastructure-data seizure, not a fund seizure)"
related_operations:
  - "[[treasury-garantex-grinex-russian-network-sanctions-2025]]"
  - "[[de-ch-crypto-mixer-takedown-2025]]"
  - "[[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]]"
  - "[[operation-endgame]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
  - "[[data-sovereignty]]"
lessons_learned:
  - "Single-jurisdiction infrastructure-takedown actions can scale to 47 simultaneous services when the targeted platforms cluster on a single national hosting territory — a pattern transferrable to other jurisdictions hosting cybercrime-adjacent infrastructure."
  - "Germany's § 127 StGB (criminal trading platforms) provides a charging basis that targets platform-design intent (knowing facilitation via no-KYC) rather than requiring proof of any specific predicate crime per platform — a model relevant for jurisdictions debating equivalent statutes."
  - "Infrastructure denial without arrests can still produce high-value investigative leads (full transaction logs, registration data, IP addresses) that feed downstream MLAT requests and bilateral cooperation — even where the operators themselves remain in a non-cooperating jurisdiction."
source_count: 6
sources:
  - "[[2024-09-19_bka_operation-final-exchange-47-russian-no-kyc-crypto-exchanges-seized]]"
created: 2026-05-09
updated: 2026-05-09
organizations:
  []
---
## Summary

On **19 September 2024**, the [[germany-bka|Bundeskriminalamt (BKA)]] together with the [[zit-frankfurt|Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT)]] of the [[germany-frankfurt-prosecutor|Generalstaatsanwaltschaft Frankfurt am Main]] announced **Operation Final Exchange**, a coordinated infrastructure takedown that seized 47 Germany-hosted no-KYC cryptocurrency exchange services serving primarily a Russian-speaking clientele. The action targeted what the BKA described as the **digital money-laundering layer of the cybercrime underground economy**, with named user populations including ransomware groups, darknet vendors, and botnet operators. Charges were brought under **§§ 127, 261 Abs. 1 Satz 1 Nr. 2 und Abs. 4 StGB** — operating criminal trading platforms on the internet plus aggravated money laundering. No arrests were announced on the action day; the action is best understood as an infrastructure-denial operation focused on data acquisition (transaction records, registration data, IP addresses) for downstream investigation rather than as an arrest sweep.

The action stands out on the BKA infrastructure-takedown timeline as the **largest single-cluster cryptocurrency-exchange seizure to date**, eclipsing prior single-platform actions such as ChipMixer (2023, ~EUR 90M) and feeding directly into the international body of evidence against Russian-language no-KYC exchanges later targeted by U.S. sanctions actions ([[treasury-garantex-grinex-russian-network-sanctions-2025]]) and German-Swiss bilateral takedowns ([[de-ch-crypto-mixer-takedown-2025]]).

## Background

The BKA release situates Operation Final Exchange in a multi-year strategic shift in German cybercrime enforcement: faced with a non-cooperating Russian Federation that does not extradite its nationals, German authorities have increasingly targeted **the infrastructure of the cybercrime ecosystem** rather than individual operators. Prior anchors in this chronology include ChipMixer (March 2023), the Qakbot and Emotet botnet disruptions, and [[operation-endgame|Operation Endgame]] (May 2024).

The 47 services targeted by Final Exchange formed a discrete sub-ecosystem within this landscape: **instant-swap no-KYC cryptocurrency exchanges**. Unlike mixers — which obscure on-chain trail through coinjoin or pool-mixing primitives — instant-swap exchanges convert one cryptocurrency to another (or to fiat via sanctioned Russian banking rails) without ever requiring user identification, registration, or identity verification. Highly likely (>90%) that the targeted platforms shared a common operational pattern: Russian-language UI, default configuration accepting deposits from sanctioned Russian banks (e.g., Sberbank), Germany-hosted server infrastructure, and product positioning as the laundering off-ramp of choice for the Russian-speaking cybercrime underground.

> [!note] No-KYC instant-swap exchange as a discrete IC pattern
> No-KYC instant-swap exchanges are conceptually distinct from (a) regulated centralized exchanges (which collect KYC and respond — sometimes — to MLAT requests), (b) mixers/tumblers (which obfuscate on-chain trail), and (c) peer-to-peer marketplaces. They form a **single-purpose money-laundering primitive** that takes ransomware/darknet/botnet criminal proceeds in and emits laundered crypto or sanctioned-bank fiat out. Final Exchange is the first major IC action to treat this as a category target rather than chasing individual platforms. The category is likely (55-80%) to be the focus of further multi-jurisdictional actions through 2026.

## Participating Parties

**Lead investigative agency**: [[germany-bka|Bundeskriminalamt (BKA)]].

**Coordinating prosecutorial body**: [[zit-frankfurt|Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT)]] within the [[germany-frankfurt-prosecutor|Generalstaatsanwaltschaft Frankfurt am Main]] (Frankfurt am Main Public Prosecutor General's Office). The ZIT is Germany's specialised central prosecutorial unit for internet crime and is the customary jurisdictional anchor for major German cybercrime infrastructure cases.

**Participating countries**: [[germany|Germany]] is the only **enforcing** state. The release does not announce partner-state participation, which is itself analytically significant. [[russia|Russia]] appears in the operation's frontmatter `participating_countries` as the **target jurisdiction** — the platforms were Russian-language, served a Russian-speaking clientele, were operationally tied to sanctioned Russian banks (e.g., Sberbank), and the operators are presumed (probably-true) Russian-located — but **Russia is not an enforcing partner**. The action proceeded on the basis of German territorial jurisdiction over the Germany-hosted server infrastructure, regardless of operator nationality or end-user nationality.

**Europol / Eurojust**: The 19 September 2024 release does not announce Europol/Eurojust co-coordination. This contrasts with the BKA's later [[de-ch-crypto-mixer-takedown-2025|DE-CH Cryptomixer takedown (2025)]] which was Eurojust-coordinated, and suggests Final Exchange was structured as a single-jurisdiction action.

## Legal Framework

**Statutory basis (verbatim from BKA release):**

> §§ 127, 261 Abs. 1 Satz 1 Nr. 2 und Abs. 4 StGB

| Statute | English short title | Function in this case |
|---|---|---|
| § 127 StGB | Operating criminal trading platforms on the internet (Betreiben krimineller Handelsplattformen im Internet) | Targets the platform itself as the offence — knowing operation of an internet platform whose primary purpose facilitates criminal trades |
| § 261 Abs. 1 Satz 1 Nr. 2 und Abs. 4 StGB | Money laundering (Geldwäsche), aggravated form | Targets the laundering function performed by the platforms |

§ 127 StGB was introduced in Germany's 2021 cybercrime amendments and is one of the few national-law instruments in the world that **directly criminalises the operation of an online platform whose design facilitates criminal trading**, without requiring case-by-case proof of any specific predicate crime by an individual user. Highly likely (80-95%) this statute will become a model for comparative legislative analysis as other jurisdictions consider equivalents (cf. U.S. 18 U.S.C. § 1960 unlicensed money transmitting; UK Online Safety Act).

International framework: Highly likely (>90%) that the action did not invoke or require the [[budapest-convention|Budapest Convention]] or any MLAT instrument, as the targeted infrastructure was Germany-hosted and seized on German territory.

## Operational Timeline

| Date | Event |
|---|---|
| Pre-2024 (multi-year) | BKA / ZIT joint investigation builds Germany-hosted no-KYC exchange landscape; identifies 47 services as targets |
| 2024-09-19 | Action day: BKA seizes development, production, and backup server infrastructure of 47 services; secures transaction data, registration data, and IP addresses; redirects domains to splash banner at finalexchange.de |
| 2024-09-19 | Joint BKA / ZIT press release issued; finalexchange.de and www.bka.de/finalexchange go public |
| 2024-09-26 | First wave of international policy commentary (Duane Morris ESE blog, Chainalysis blog) |
| 2024-10-31 | BKA announces follow-on arrests in Hesse and Rhineland-Palatinate (separate press release; not part of the 19 September action itself) |

Roughly even chance (45-55%) that additional arrests connected to specific Final Exchange platforms remain non-public as of the ingest date due to ongoing investigations.

## Results and Impact

**Action-day seizures (per BKA release):**

- 47 Germany-hosted exchange services taken offline
- Development, production, and backup servers seized across the platforms
- Transaction data, registration data, and IP addresses secured

**Notable single-platform metric — Xchange.cash:**

- Approximately **410,000 user accounts**
- Approximately **1.28–1.3 million transactions** processed
- Top of the 47 by transaction volume

**Notable single-platform metric — Bankcomat.com:**

- Operating since **2012** — 12 years of operational history at time of seizure
- Among top three by transaction volume

**On-chain illicit-exposure findings (Chainalysis post-takedown analysis):**

- 17 of 47 exchanges had months in which >50% of direct on-chain inflows came from illicit sources
- 12 of 47 had months with >30% of inflows from darknet marketplaces
- 6 of 47 had months in which stolen funds exceeded 30% of inflows

**Splash banner text (translated, partial quote):**

> "We have found their servers and seized them … We have their data — and therefore we have your data. Transactions, registration data, IP addresses."

The deliberate communicative framing of the splash banner — addressing **users** of the seized platforms and not just operators — is a hallmark of the BKA infrastructure-takedown style first developed in Operation Endgame and is itself an IC-relevant tactic: it is calculated to chill use of similar services across jurisdictions even where prosecution of any individual user is not feasible.

## Cooperation Mechanisms Used

This was a **single-jurisdiction action** on Germany's own territorial jurisdiction over Germany-hosted infrastructure. No formal cross-border MLAT mechanism was invoked at action time. The IC dimension is forward-looking: the seized **transaction logs, registration data, and IP addresses** become a feeder dataset for outbound German MLAT and police-to-police requests to other jurisdictions where individual users or downstream beneficiaries can be identified.

This pattern — **unilateral infrastructure seizure as a feeder for downstream multilateral enforcement** — is documented across [[de-ch-crypto-mixer-takedown-2025]] and [[operation-endgame]] and is increasingly the dominant operational model for actions against Russian-language cybercrime infrastructure where Russia itself does not cooperate. Likely (55-80%) the Final Exchange dataset has by 2026 fed into U.S. Treasury actions targeting [[treasury-garantex-grinex-russian-network-sanctions-2025|Garantex / Grinex and the broader Russian no-KYC network]].

## Challenges and Friction Points

- **[[jurisdictional-conflicts|Jurisdictional conflicts]]**: targeted platforms operated for Russian-language users with banking nexus to sanctioned Russian banks, but their server infrastructure was Germany-hosted. The action proceeded smoothly because the conflict resolved in Germany's favour by virtue of physical hosting territory; this would not have worked had the platforms been hosted in Russia, in offshore jurisdictions, or in non-cooperating CIS states.
- **[[data-sovereignty|Data sovereignty]]**: seized transaction and registration data covers users in many jurisdictions. Onward sharing of this dataset with non-EU partners (notably the United States) raises GDPR / data-protection considerations that the public release does not address; highly likely (>90%) that ZIT operates a data-handling protocol for foreign-partner sharing under existing instruments.
- **Absence of arrests on action day**: the operation produced no immediate arrests. This is a deliberate design choice — the operators are presumed (probably-true) to be located outside Germany and outside the EU, in jurisdictions where extradition is unlikely. Infrastructure denial substitutes for prosecution where prosecution is not feasible.

## Lessons Learned

1. **No-KYC exchange ecosystem is now a target category, not a target list.** Earlier mixer takedowns ([[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]], [[de-ch-crypto-mixer-takedown-2025]]) treated each platform as a discrete target. Final Exchange establishes that the **entire instant-swap no-KYC sub-ecosystem** can be treated as a single target class for coordinated action when the platforms cluster on a common hosting territory.
2. **§ 127 StGB is exportable as a model.** The German offence of "operating criminal trading platforms on the internet" gives prosecutors a charging basis that does not require predicate-crime-by-predicate-crime proof. Highly likely (80-95%) other EU member states will examine adopting equivalent provisions.
3. **Infrastructure denial without arrests still generates IC value.** The seized transaction logs, registration data, and IP addresses become an investigative dataset that flows into outbound MLAT requests, sanctions designations, and partner-state actions for years afterwards.
4. **Communicative framing matters.** The "we have their data — and therefore we have your data" splash text is itself an IC instrument. It is calculated to chill use of similar services internationally, including in jurisdictions where prosecution of any individual user is impossible.

## Follow-Up Actions

- 2024-10-31: BKA announces follow-on arrests in Hesse and Rhineland-Palatinate (separate press release; partial connection to the Final Exchange dataset is plausible but not explicitly confirmed in the public release).
- The seized dataset is highly likely (80-95%) to feed downstream U.S. Treasury actions against the broader Russian-language no-KYC exchange network, including [[treasury-garantex-grinex-russian-network-sanctions-2025|the 2025 Garantex/Grinex sanctions package]].
- Likely (55-80%) that additional bilateral or multilateral takedowns of remaining Russian-language no-KYC exchanges hosted outside Germany follow on a multi-year timeline as transaction data establishes onward criminal connections.

## Korean Involvement (한국의 참여)

There is **no announced direct Korean (대한민국) participation** in Operation Final Exchange. The action was a single-jurisdiction German operation. However, the operation is **highly relevant to Korean policy** for three reasons:

1. **Ransomware payment laundering**: Korean victims of ransomware groups using Russian-language infrastructure (notably the broader LockBit / Conti ecosystem) routinely had their extorted cryptocurrency laundered through no-KYC exchanges of the type seized in Final Exchange. The seized transaction logs are highly likely (>90%) to contain entries traceable to ransomware payments originating from Korean-jurisdiction victims.
2. **Comparative legislative interest**: Korea's own [Act on Reporting and Use of Specific Financial Transaction Information / 특정금융정보법] imposes KYC obligations on Korean virtual-asset service providers, but does not provide a direct German-style § 127 StGB equivalent for charging the **operation of a no-KYC platform** as such. Korean policymakers studying legislative responses to cross-border laundering may find the German approach instructive.
3. **MLAT downstream**: Korean prosecutors investigating ransomware extortion of Korean victims may be able to request, via the [[mutual-legal-assistance|MLAT]] channel between Korea and Germany, access to specific transaction-log entries from the Final Exchange dataset where probable cause links a specific Korean victim payment to a seized exchange. As of the ingest date, no such request is publicly documented.

## Contradictions & Open Questions

> [!warning] Contradiction
> **Claim A** (The Record, 20 Sep 2024, reliability: medium): Xchange.cash has been operating "since 2012."
> **Claim B** (Heise / Chainalysis, reliability: medium-high): Bankcomat.com has been operating since 2012; Xchange.cash has been operating since 2016 or before.
> **Assessment**: Claim B is *likely* correct. Chainalysis on-chain analysis dates Xchange.cash to 2016+; the 2012 figure consistently attaches to Bankcomat across higher-reliability sources.

> [!info] Open questions
> - Total number of physical servers seized (the BKA describes development/production/backup tiers but does not give an integer total).
> - Total Germany-resident user-account count across all 47 platforms.
> - Whether any of the 47 exchanges had been previously the subject of MLAT requests from non-German partner agencies prior to the takedown.
> - Whether the 31 October 2024 BKA arrests in Hesse and Rhineland-Palatinate are confirmed connected to the Final Exchange operator network (timing is suggestive but the public releases do not explicitly link the two actions).
> - The full enumerated list of all 47 named exchanges (BKA release names a subset; no consolidated 47-name list is public).
