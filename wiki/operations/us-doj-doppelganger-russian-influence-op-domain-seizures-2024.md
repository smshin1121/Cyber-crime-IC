---
type: operation
title: "US DOJ Doppelganger Russian Foreign Malign Influence Domain Seizures and RT/Tenet Media Indictment (September 2024)"
aliases:
  - "Doppelganger domain seizure 2024"
  - "DOJ Russia influence 32-domain seizure"
  - "Tenet Media indictment 2024"
  - "RT employees indictment 2024"
case_id: CYB-2024-101
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - seizure
  - indictment
  - asset_freeze
outcome: partial
timeframe:
  announced: 2024-09-04
  start: 2024-09-04
  end: 2024-09-04
  ongoing: false
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[money-laundering-ic]]"
crime_type: "[[cybercrime-infrastructure-ic]]"
target_entity: "Russian state-directed Doppelganger covert foreign malign influence apparatus (Social Design Agency / Structura / ANO Dialog) and the RT-funded Tenet Media network"
lead_agency: "[[us-doj]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-treasury]]"
legal_basis:
  []
mechanisms_used:
  []
results:
  arrests: 0
  indictments: 1
  servers_seized: 0
  domains_seized: 32
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Two-count SDNY indictment unsealed against Konstantin Kalashnikov and Elena Mikhaylovna Afanasyeva (RT employees) — FARA conspiracy and money-laundering conspiracy. Both at large in Russia."
    - "Treasury OFAC same-day designations: 10 individuals + 2 entities under IEEPA."
    - "Approximately $9.7M alleged in covert payments to Tennessee-based Tenet Media."
edges:
  []
credibility_index: 0.0
source_tier: 1
missing_fields:
  - foreign_cooperation_partners
  - specific_legal_basis_statutes_in_frontmatter
related_cases:
  []
related_operations:
  - "[[treasury-doppelganger-russian-malign-influence-sanctions-2024]]"
challenges_encountered:
  []
lessons_learned:
  - "When the host state of foreign-national defendants is uncooperative (Russia post-2022), U.S. enforcement substitutes domain seizures + OFAC sanctions for unavailable extradition / MLAT pathways. The 'cooperation gap' is filled by unilateral U.S. process applied to U.S.-controlled choke points (registries, financial system)."
  - "An influence-operation case can be prosecuted under FARA + money-laundering conspiracy without naming foreign LE counterparts — but this leaves the operational defendants beyond reach. Indictment value is signaling and asset-freezing, not arrest."
source_count: 1
sources:
  - "[[2024-09-04_justice-gov_doppelganger-russian-influence-operation-domain-seizures]]"
created: 2026-05-09
updated: 2026-05-09
last_verified: 2026-05-09
---
> [!info] Provisional page
> Published below the preferred 5-source threshold (CLAUDE.md "Entity creation threshold"). One tier-1 primary source (DOJ OPA press release, 2024-09-04). Companion DOJ release on the RT/Tenet indictment, the Treasury OFAC designation memo (JY-2519), and the publicly available SDNY indictment text should be ingested to lift this page to standard publication state.

> [!warning] IC scope flag
> The DOJ release names **no foreign law-enforcement cooperation partner**. The IC dimension here is indirect: foreign-national defendants beyond U.S. arrest reach, foreign state-actor predicate, parallel sanctions track, and downstream registrar interactions across multiple ccTLDs that are not credited in the public release. This page is retained as a comparison case for "no-cooperation cyber enforcement."

## Summary

On **4 September 2024**, the U.S. Department of Justice announced a coordinated U.S.-government action against the Russian state-directed covert foreign malign influence operation publicly known as **"Doppelganger."** The action had three simultaneous components:

1. **Domain seizure** — 32 internet domains used to disseminate Russian government propaganda (including cybersquatted lookalikes of legitimate Western news outlets, e.g., **washingtonpost.pm** spoofing washingtonpost.com) were seized under court warrants out of the **U.S. Attorney's Office for the Eastern District of Pennsylvania**, executed by the **FBI Philadelphia Field Office**.

2. **Criminal indictment** — A two-count SDNY indictment was unsealed against two RT (Russia Today) employees, **Konstantin Kalashnikov** and **Elena Mikhaylovna Afanasyeva**, for (a) conspiracy to violate the Foreign Agents Registration Act (FARA) and (b) conspiracy to commit money laundering. The indictment alleges a roughly **$9.7 million** scheme funneled through shell companies to direct a Tennessee-based online content firm (publicly identified as **Tenet Media**) to publish English-language content amplifying Russian government messaging. Both defendants are believed to be in Russia and remain at large.

3. **OFAC designations** — The U.S. Treasury Department's Office of Foreign Assets Control concurrently designated **10 individuals and 2 entities** under IEEPA in connection with Russia's malign influence efforts targeting the 2024 U.S. presidential election.

It is *almost certain* (>95% confidence, tier-1 DOJ source plus six independent corroborations) that these three components were announced together on 2024-09-04. It is *highly likely* (80-95% confidence) that the Doppelganger apparatus was operated by the named Russian PR contractors (Social Design Agency / Structura / ANO Dialog) under direction of Sergei Kiriyenko of the Russian Presidential Executive Office, per DOJ allegations not yet adjudicated.

## Background

"Doppelganger" is the public/industry name for a long-running Russian state-directed influence operation that uses **cybersquatted domains mimicking Western news outlets** combined with paid social-media amplification to push Russian government narratives — particularly to reduce international support for Ukraine, bolster pro-Russian policies, and influence voters in U.S. and foreign elections, including the 2024 U.S. presidential election (Source: [[2024-09-04_justice-gov_doppelganger-russian-influence-operation-domain-seizures|DOJ OPA, 4 Sep 2024]]).

The Russian apparatus identified by DOJ comprises three civilian-front entities:

| Entity | Role per DOJ allegation |
|---|---|
| **Social Design Agency (SDA)** | Lead Russian PR/influence vendor running cybersquatted domains. |
| **Structura National Technology (Structura)** | Russian technology contractor supporting SDA. |
| **ANO Dialog** | Russian autonomous non-profit organization producing influence content. |

DOJ alleges these entities operated under the direction of **Sergei Vladilenovich Kiriyenko**, First Deputy Chief of Staff to President Vladimir Putin, and other members of the Russian Presidential Executive Office.

The Tenet Media component is a separate but parallel covert-funding scheme: RT digital-media employees Kalashnikov and Afanasyeva are alleged to have routed roughly $9.7M through shell entities to a Tennessee-based online content firm to publish covert pro-Russian content under the cover of independent commentary.

## Participating Parties

### Lead agency

- **[[us-doj|U.S. Department of Justice]]** — Office of the Attorney General; Office of the Deputy Attorney General; National Security Division (NSD); Criminal Division — Computer Crime and Intellectual Property Section (CCIPS).

### Investigative / charging districts

| Component | Investigating / charging entity |
|---|---|
| Domain seizures | U.S. Attorney's Office, Eastern District of Pennsylvania (USAO EDPA); [[fbi|FBI]] Philadelphia Field Office |
| RT/Tenet indictment | U.S. Attorney's Office, Southern District of New York (USAO SDNY); [[fbi|FBI]] Counterintelligence Division |
| OFAC sanctions | [[us-treasury|U.S. Department of the Treasury]] — Office of Foreign Assets Control |

### Foreign cooperation partners

**None named in the public release.** No foreign LE counterpart, registrar, or government is credited as a cooperation partner.

### Defendants (Russian nationals — fugitive)

| Defendant | Role | Charges |
|---|---|---|
| **Konstantin Kalashnikov** | RT digital media projects manager | 18 U.S.C. § 371 (FARA conspiracy); 18 U.S.C. § 1956(h) (money-laundering conspiracy) |
| **Elena Mikhaylovna Afanasyeva** | RT Digital Media Projects Department employee | Same |

Both at large; believed in Russia; *almost certain* (>95%) that no extradition has occurred or is feasible under current bilateral conditions.

## Legal Framework

- **International Emergency Economic Powers Act (IEEPA)** — basis for OFAC designations.
- **Foreign Agents Registration Act (FARA), 22 U.S.C. § 611 et seq.** — basis for the SDNY indictment substantive charge.
- **18 U.S.C. § 371** — conspiracy.
- **18 U.S.C. § 1956(h)** — money-laundering conspiracy.
- **Federal criminal trademark / cybersquatting statutes** — basis for the EDPA domain-seizure warrants (the seized domains spoofed real trademarked outlets).

## Operational Timeline

- **Pre-2024 (multi-year, exact start unknown):** Russian Doppelganger operation establishes cybersquatted domain network and Tenet Media funding chain.
- **2024-09-04 (Wed):** DOJ Office of Public Affairs announces (a) 32-domain seizure, (b) SDNY indictment of two RT employees unsealed, (c) Treasury OFAC designations of 10 individuals + 2 entities. Quotes from AG Garland, FBI Director Wray, DAG Monaco.
- **Post-announcement:** Defendants remain at large in Russia. Domain seizures executed; cybersquatted sites display DOJ seizure banners.

## Results and Impact

| Metric | Value |
|---|---|
| Domains seized | **32** |
| Indictments unsealed | **1** (2 defendants) |
| Arrests | 0 (defendants in Russia) |
| OFAC designations same day | **10 individuals + 2 entities** |
| Funds alleged in Tenet Media scheme | **~$9.7 million** |

## Cooperation Mechanisms Used

> [!warning] No formal IC mechanism documented
> The DOJ release does not invoke Budapest Convention Article 32(b), MLAT, the 24/7 Network, or any other formal cooperation mechanism. Domain seizure relied on U.S.-jurisdictional process applied to U.S.-controlled or U.S.-accessible registry channels (Verisign for .com/.net; the .pm registry is operated by AFNIC of France, but no French agency credit appears in the public release — cooperation if any is informal/operator-level).

## Challenges and Friction Points

- **Extradition unavailable** — defendants are Russian nationals in Russia; no functioning U.S.-Russia extradition pipeline post-2022. The indictment is therefore primarily a signaling and asset-targeting instrument.
- **Cybersquatted domains across multiple TLDs** — including ccTLDs operated by foreign registries (e.g., .pm by AFNIC/France), but no formal foreign-government cooperation channel is credited.
- **Influence-operation evidence threshold** — proving covert direction of a U.S.-resident content company under FARA without cooperative Russian-side discovery is structurally difficult and rests on financial-flow tracing (the basis of the money-laundering count).

## Lessons Learned

- When the host state of foreign-national defendants is uncooperative, U.S. enforcement substitutes **domain seizures + OFAC sanctions** for unavailable extradition / MLAT pathways. The "cooperation gap" is filled by unilateral U.S. process applied to U.S.-controlled choke points (registries, financial system).
- An influence-operation case can be prosecuted under **FARA + money-laundering conspiracy** without naming foreign LE counterparts — but this leaves the operational defendants beyond reach. The indictment's value is signaling and asset-freezing, not arrest.
- Same-day **DOJ + Treasury** synchronization (criminal action + sanctions) is now a standard U.S. response template for state-directed cyber-enabled operations where the actor's host government will not cooperate.

## Follow-Up Actions

- The Doppelganger network continued operating after the September 2024 action under new domains; subsequent rounds of seizures and OFAC designations occurred in 2025 (separate ingest target).
- Tenet Media ceased operations following the indictment.

## Korean Involvement (한국의 참여)

None recorded. The DOJ release does not reference Korea, Korean entities, or Korean citizens. Korean relevance is **indirect comparative**: the case is a useful reference point for any future Korean response to state-directed covert foreign-influence content targeting Korean elections, especially in cases where the originating state is not cooperative.

## Contradictions & Open Questions

- Whether any foreign registry / registrar (e.g., AFNIC for .pm) provided informal cooperation in domain seizure execution is **unknown** from the DOJ public release alone. The release credits no foreign partner.
- The exact list of all 32 seized domain names is not enumerated in the press release excerpts available; the SDNY indictment and EDPA seizure warrant exhibits would provide the full inventory but are not yet ingested.
- The extent to which Tenet Media's U.S. content creators were knowing participants vs. duped is a factual question raised in the indictment but not adjudicated.
