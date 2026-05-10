---
type: operation
title: "US DOJ Raptor Train (Flax Typhoon / Integrity Technology Group) PRC IoT Botnet Court-Authorized Disruption (September 2024)"
aliases:
  - "Raptor Train botnet takedown"
  - "Flax Typhoon botnet disruption 2024"
  - "Integrity Technology Group botnet takedown 2024"
  - "DOJ Raptor Train"
  - "WDPA Raptor Train operation 2024"
case_id: CYB-2024-105
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2024-09-18
  start: ""
  end: 2024-09-18
  ongoing: false
crime_types:
  - "[[hacking-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[malware-ic]]"
crime_type: "[[cybercrime-infrastructure-ic]]"
target_entity: "Integrity Technology Group (PRC-based publicly-traded company, public brand 'KRLab') — assessed by FBI as the entity behind the activity industry tracks as 'Flax Typhoon'. Operated the Raptor Train IoT botnet (>200,000 SOHO routers, IP cameras, DVRs, NAS devices)."
lead_agency: "[[fbi]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[france]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[new-zealand]]"
  - "[[united-kingdom]]"
  - "[[china]]"
participating_agencies:
  - "[[fbi]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
legal_basis:
  []
mechanisms_used:
  - "[[search-seizure]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Court-authorized takeover of the adversary's command-and-control infrastructure (DOJ asserts FBI 'took control of the hackers' computer infrastructure')."
    - "More than 200,000 compromised IoT consumer devices worldwide (SOHO routers, IP cameras, DVRs, NAS) had disabling commands issued to the malware via the seized C2 channel."
    - "Adversary DDoS counter-attack against the FBI's operational infrastructure during the takedown — ultimately unsuccessful."
    - "Same-day Joint Cybersecurity Advisory co-published by FBI, NSA, USCYBERCOM CNMF, and partner cyber agencies in Australia, Canada, New Zealand, and the United Kingdom."
    - "FBI provides victim notice to U.S. owners of affected devices via their internet service providers."
edges:
  []
credibility_index: 0.0
source_tier: 1
missing_fields:
  - "specific_legal_basis_statutes (court order/affidavit not yet ingested as a separate raw source)"
  - "named_partner_agencies_in_FVEY_advisory (ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK inferred but not asserted from this source per L19)"
  - "specific_French_authority_named (only 'French authorities' credited; no agency name)"
related_cases:
  []
related_operations:
  - "[[911-s5-botnet-takedown]]"
  - "[[treasury-integrity-technology-group-flax-typhoon-sanctions-2025]]"
challenges_encountered:
  []
lessons_learned:
  - "When the host state of a threat actor (PRC) is uncooperative for IC purposes, U.S. court-authorized takeover of adversary infrastructure substitutes for unavailable MLAT pathways — the U.S. asserts jurisdiction by reaching into the C2 layer rather than into the foreign nation's territory."
  - "Five Eyes joint cybersecurity advisory (FBI + NSA + USCYBERCOM CNMF + AU/CA/NZ/UK partner cyber agencies) is the standard parallel-track instrument for state-attributed activity in 2024 — it provides multilateral attribution and information-sharing without requiring a treaty mechanism."
  - "Bilateral foreign LE assistance (France, named) + multilateral cyber-agency advisory (FVEY) + private-sector technical attribution (Lumen / Black Lotus Labs) is now a recurring three-track IC pattern in U.S. botnet takedown operations."
  - "Adversary in-operation counter-attack (DDoS during takedown) is a documented tactical reality and should be expected for high-value PRC contractor operations."
source_count: 1
sources:
  - "[[2024-09-18_justice-gov_court-authorized-operation-disrupts-raptor-train-botnet-flax-typhoon]]"
created: 2026-05-09
updated: 2026-05-09
last_verified: 2026-05-09
---
> [!info] Provisional page
> Published below the preferred 5-source threshold (CLAUDE.md "Entity creation threshold"). One tier-1 primary source (DOJ OPA press release, 2024-09-18, Press Release Number 24-1173). Companion artifacts to ingest in subsequent rounds: (a) the same-day Joint Cybersecurity Advisory (defense.gov-hosted PDF, FBI+NSA+USCYBERCOM+AU/CA/NZ/UK), (b) Lumen Technologies / Black Lotus Labs technical writeup ("Derailing the Raptor Train"), (c) the WDPA court-order/affidavit referenced in the press release, (d) FBI Director Wray's Aspen Cyber Summit announcement (FBI.gov), (e) NCSC-UK companion guidance ("Defending against China-nexus covert networks of compromised devices").

> [!warning] Per L19 — only countries explicitly named in the primary DOJ source are asserted as participating_countries
> Asserted: **United States** (lead), **France** (named — "French authorities"), **Australia / Canada / New Zealand / United Kingdom** (named as partner cyber agencies' countries co-signing the joint advisory), and **China** (target nationality of the named PRC-contractor entity Integrity Technology Group). Specific partner agency names (ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK) are NOT linked here — they require the companion joint advisory PDF as a separate tier-1 source. The press release's "partner agencies in Australia, Canada, New Zealand and the United Kingdom" phrase does not enumerate agency names.

## Summary

On **18 September 2024**, the U.S. Department of Justice announced a **court-authorized law enforcement operation**, conducted under court orders unsealed in the **U.S. District Court for the Western District of Pennsylvania**, that disrupted a worldwide IoT botnet of **more than 200,000 consumer devices** (small-office/home-office routers, IP cameras, digital video recorders, network-attached storage). The botnet — known publicly as **"Raptor Train"** since Lumen Technologies' Black Lotus Labs first described it in July 2023 — was developed and controlled by **Integrity Technology Group**, a publicly-traded Beijing-based company that the FBI assesses as responsible for the China-based hacker activity industry tracks as **"Flax Typhoon"** (Source: [[2024-09-18_justice-gov_court-authorized-operation-disrupts-raptor-train-botnet-flax-typhoon|DOJ OPA, 18 Sep 2024]]).

The operation **took control of the adversary's command-and-control infrastructure** and used that infrastructure to send **disabling commands** to the malware on infected devices. Integrity Technology Group attempted a **distributed denial-of-service (DDoS) counter-attack** against the FBI's operational infrastructure during the takedown — the counter-attack was unsuccessful. The press release explicitly characterizes the takedown as **"an international operation with partners"** (FBI Deputy Director Paul Abbate quote).

It is **almost certain** (>95% confidence, tier-1 DOJ source) that the operation occurred on the announced date with the stated scope and target entity. It is **highly likely** (80-95%) that the four FVEY partner countries' cyber agencies (ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK) are the unnamed "partner agencies" referenced in the advisory paragraph, pending direct ingest of the companion joint advisory.

## Background

**Raptor Train** is the public/industry name (assigned by Lumen's Black Lotus Labs, July 2023) for a long-running PRC-state-aligned botnet built on compromised consumer-grade IoT devices. According to the DOJ release and corroborated public reporting:

- Compromised device classes: **SOHO routers, IP cameras, DVRs, NAS** appliances.
- The malware connected the >200,000 infected devices into a botnet **controlled by Integrity Technology Group**, used to disguise malicious cyber activity as routine consumer internet traffic.
- Integrity Technology Group's online control application was branded **"KRLab"**, with a malicious-command menu tool called **"vulnerability-arsenal"** sold to customers as a service.
- The FBI assesses Integrity Technology Group is responsible for activity industry tracks as **Flax Typhoon**, described by Microsoft Threat Intelligence as PRC-based nation-state actors active since 2021, targeting government, education, critical manufacturing, and IT organizations in **Taiwan and elsewhere**. The FBI's investigation extends the target set to U.S. and foreign **corporations, universities, government agencies, telecommunications providers, and media organizations**.

This is the **second PRC-contractor botnet** disrupted by DOJ in 2024 — AAG Olsen's quote ("for the second time this year, we have disrupted a botnet used by PRC proxies") connects this to the May 2024 [[911-s5-botnet-takedown|911 S5]] takedown.

## Participating Parties

### Lead U.S. components

- **[[fbi|Federal Bureau of Investigation]]** — San Diego Field Office (Special Agent in Charge Stacey Moy) and **[[fbi-cyber-division|Cyber Division]]**.
- **[[us-doj|U.S. Department of Justice]]** — National Security Division (NSD) National Security Cyber Section (AAG Matthew G. Olsen); Criminal Division — Computer Crime and Intellectual Property Section (CCIPS); Criminal Division — Office of International Affairs (OIA).
- **U.S. Attorney's Office for the Western District of Pennsylvania** (USAO WDPA) — U.S. Attorney Eric G. Olshan; this is the court venue where seizure orders were unsealed.

### Same-day Joint Cybersecurity Advisory co-signers

| Country | Co-signing role per DOJ release |
|---|---|
| **[[united-states\|United States]]** | FBI, **NSA**, **U.S. Cyber Command — Cyber National Mission Force (CNMF)** |
| **[[australia\|Australia]]** | "partner agencies" (specific agency name not enumerated in DOJ release) |
| **[[canada\|Canada]]** | "partner agencies" (specific agency name not enumerated in DOJ release) |
| **[[new-zealand\|New Zealand]]** | "partner agencies" (specific agency name not enumerated in DOJ release) |
| **[[united-kingdom\|United Kingdom]]** | "partner agencies" (specific agency name not enumerated in DOJ release) |

> [!note] Agency-name attribution
> Per L19, the operation page does not assert specific FVEY partner-agency wikilinks (ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK) from this source alone. The DOJ press release credits **partner agencies** at the country level only.

### Foreign government cooperation (named explicitly)

- **[[france|France]]** — "French authorities" credited for "collaboration of partners" alongside Lumen. The specific French agency is not named in the press release.

### Private-sector partner

- **Lumen Technologies / Black Lotus Labs** — first identified and described the botnet (named "Raptor Train") in **July 2023**; credited as a critical contributor to the takedown's success.

### Target / threat actor

- **Integrity Technology Group** — publicly-traded, Beijing-headquartered ([[china|People's Republic of China]]). Public brand **"KRLab"**.
- **Flax Typhoon** (industry name) — PRC state-sponsored cyber actor active since 2021 (Microsoft Threat Intelligence assessment, corroborated by FBI investigation).

## Legal Framework

> [!warning] Specific charging and seizure statutes not enumerated in the press release
> The press release describes a **court-authorized law enforcement operation** with **court documents unsealed in the Western District of Pennsylvania**. The specific statutory basis (e.g., Federal Rule of Criminal Procedure 41 search-and-seizure warrants; 18 U.S.C. § 1030 Computer Fraud and Abuse Act predicate; civil-injunction precedents from prior PRC-botnet takedowns) is not identified in the DOJ public release. The court order and its supporting affidavit ("View the affidavit here") are referenced but not yet ingested as a separate raw source. Per CLAUDE.md "Legal precision rules", this is flagged as `Legal status check needed` until the underlying court documents are ingested.

The operation legally rests on the U.S. court's authority to issue orders directed at infrastructure used to commit predicate offenses against U.S. victims, even when the operators are foreign nationals operating from outside the U.S. — analogous to recent precedent operations against PRC-attributed botnets ([[911-s5-botnet-takedown|911 S5]], May 2024) and earlier Russia/U.S.-sanctions actions.

## Operational Timeline

- **July 2023** — Lumen Technologies' Black Lotus Labs publishes initial description of the botnet, naming it **"Raptor Train"**.
- **2021 → 2024-09** (per Microsoft / FBI assessment) — Flax Typhoon / Integrity Technology Group activity targets government, education, telecom, media, and DIB sectors in Taiwan, U.S., and elsewhere; >200,000 IoT devices compromised globally.
- **Pre-2024-09-18** (date unstated) — Court orders sought and granted in the Western District of Pennsylvania; FBI prepares and tests disabling commands.
- **2024-09-18** (Wed) — FBI executes the takeover of adversary C2 infrastructure; disabling commands issued to malware on infected devices.
- **During the takedown** — Integrity Technology Group launches a DDoS counter-attack against the FBI's operational infrastructure; counter-attack unsuccessful.
- **2024-09-18** — DOJ Office of Public Affairs issues Press Release Number **24-1173**; same-day joint cybersecurity advisory published by FBI + NSA + USCYBERCOM CNMF + AU/CA/NZ/UK partner cyber agencies (defense.gov-hosted PDF); same-day Lumen Black Lotus Labs technical writeup ("Derailing the Raptor Train") published.
- **Post-2024-09-18** — FBI provides victim notice to U.S. owners of affected devices via their internet service providers; FBI continues to investigate Integrity Technology Group / Flax Typhoon.

## Results and Impact

| Metric | Value |
|---|---|
| Devices in botnet | **>200,000** (SOHO routers, IP cameras, DVRs, NAS) |
| Adversary infrastructure controlled | **Yes** ("the court-authorized operation took control of the hackers' computer infrastructure") |
| Disabling commands issued to malware on infected devices | **Yes** |
| Adversary DDoS counter-attack | Yes — **unsuccessful** |
| Arrests | 0 (threat actor in PRC; no indictment in this announcement) |
| Indictments | 0 (this is a court-authorized takedown, not a charging announcement) |
| Joint cybersecurity advisory co-signers | **5 countries** (US + AU + CA + NZ + UK) |
| Bilateral foreign LE partner named | **France** |
| Private-sector partner named | **Lumen Technologies / Black Lotus Labs** |
| Press release number | **24-1173** |

> [!note] Confidence and quantification
> The "more than 200,000" figure is from the DOJ release. Companion reporting (Lumen, NPR, FBI Director Wray's Aspen Cyber Summit remarks) describes peak botnet size as ~260,000 devices in June 2024 and approximately 250,000 devices at takedown — those figures are *highly likely* (80-95%) accurate but are not asserted in the DOJ primary source ingested here.

## Cooperation Mechanisms Used

- **Court-authorized infrastructure takeover** — the U.S. exercises jurisdiction over adversary C2 infrastructure under WDPA court orders. This relies on `[[search-seizure]]`-style mechanisms applied to digital infrastructure rather than a foreign-cooperation channel.
- **Five Eyes joint cybersecurity advisory** — multilateral information-sharing and public attribution instrument, co-signed by FBI + NSA + USCYBERCOM CNMF + partner cyber agencies in Australia, Canada, New Zealand, and the United Kingdom. This is a **non-treaty cooperation mechanism** that runs in parallel with the takedown rather than as an evidence-transfer channel.
- **Bilateral foreign-LE assistance** — French authorities credited (specific French agency not named); pathway not specified (could be informal police-cooperation or formal MLAT — the press release does not say).
- **Public-private partnership** — Lumen Technologies / Black Lotus Labs technical attribution and operational support. The release credits the partnership as essential to success.

> [!warning] No formal MLAT or Budapest Convention reference
> The DOJ release does not name MLAT, the Budapest Convention 24/7 Network, or any treaty-based mechanism. The OIA component listing in the press release footer is consistent with foreign-cooperation routing (likely for the French collaboration), but the precise instrument is not identified.

## Challenges and Friction Points

- **PRC host state uncooperative** — no extradition, no MLAT pathway to China for the threat actor (Integrity Technology Group is a Beijing-based publicly-traded company). The U.S. response is **unilateral court-authorized infrastructure takeover** rather than an evidence-or-arrest cooperation chain with the host state.
- **Adversary live counter-action during takedown** — Integrity Technology Group's DDoS attempt during the operation is a documented tactical reality. The release notes it was unsuccessful but discloses the contestation, which is unusual for such announcements.
- **Botnet rebuild risk** — The release does not claim permanent dismantlement of the actor (only of "this" botnet). Independent reporting (Lumen, Wray Aspen remarks) describes Flax Typhoon as likely able to attempt rebuild on new infrastructure, consistent with the FBI's ongoing investigation note in the release.
- **Partner-agency attribution opacity** — DOJ names FVEY partner countries but not their specific agencies. This is a recurring opacity in U.S. takedown announcements involving the FVEY mechanism.

## Lessons Learned

- **Court-authorized infrastructure takeover is now the U.S. default response** to PRC-contractor IoT botnets when the host state will not cooperate (cf. [[911-s5-botnet-takedown|911 S5]] in May 2024 and Raptor Train in September 2024 — both within four months in 2024).
- **Five Eyes joint cybersecurity advisory is the standard multilateral attribution instrument** for PRC-attributed activity; it does not require treaty negotiation and runs as a parallel track to U.S. enforcement.
- **Bilateral foreign LE assistance + multilateral cyber-agency advisory + private-sector technical attribution** is a recurring three-track IC pattern in U.S. botnet takedown operations as of 2024.
- **In-operation adversary counter-attack** (DDoS during takedown) is a documented operational reality for high-value PRC-contractor operations and should be expected.
- **Public attribution naming a contractor company** (Integrity Technology Group / "KRLab" / "vulnerability-arsenal") is a more aggressive disclosure pattern than naming an APT only — it places direct reputational and economic cost on a publicly-traded foreign company. This is consistent with the 2024 U.S. shift toward naming PRC commercial intermediaries.

## Follow-Up Actions

- The **Joint Cybersecurity Advisory** co-published the same day (FBI + NSA + USCYBERCOM CNMF + AU/CA/NZ/UK) provides TTPs for defenders. Ingest as a separate tier-1 source.
- **Lumen Black Lotus Labs technical writeup** ("Derailing the Raptor Train") provides device-class breakdowns, geographic distribution, and Mirai-variant malware analysis. Ingest as a tier-1 industry source.
- **WDPA court order and supporting affidavit** — referenced in the press release ("View the affidavit here"); ingest as a primary court-document source for the legal-basis frontmatter.
- **FBI Director Christopher Wray's Aspen Cyber Summit remarks** (FBI.gov) — public attribution announcement of Flax Typhoon's identification with Integrity Technology Group; ingest as a tier-1 FBI source.
- **NCSC-UK companion guidance** ("Defending against China-nexus covert networks of compromised devices") — UK-side companion artifact; ingest to confirm UK partner agency is NCSC-UK (currently inferred but not asserted per L19).
- **Subsequent Raptor Train activity** — monitor for botnet rebuild attempts and any follow-on PRC-contractor disclosures by FBI / FVEY partners.

## Korean Involvement (한국의 참여)

**None recorded.** The DOJ press release does not reference Korea, Korean entities, or Korean citizens. Korean relevance is **indirect comparative**: the case is a useful reference point for any future Korean response to PRC-state-contractor IoT botnets affecting Korean consumer devices or operating against Korean targets, particularly given:

- Microsoft / FBI assessments of Flax Typhoon target Taiwan-and-elsewhere — a regional scope that may include Korea-relevant collateral compromise.
- The U.S. court-authorized infrastructure takeover model is not directly available under current Korean criminal procedure (한국 형사소송법 압수·수색 절차) without analogous cybercrime-specific authorizations.
- The Five Eyes joint cybersecurity advisory mechanism does not currently include Korea as a co-signer; comparable Korea-inclusive joint-attribution products would require alternative frameworks (e.g., bilateral US-ROK cyber statements, ROK-NIS / KISA / KNPA channels).

## Contradictions & Open Questions

- **Specific FVEY partner agencies** — the press release names countries (AU, CA, NZ, UK) but not agencies. ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK are *highly likely* (80-95%) the unnamed partner agencies based on the recurring pattern of FVEY cyber CSAs, but per L19 this should be confirmed by ingesting the companion joint advisory PDF.
- **Specific French agency** — only "French authorities" credited; specific agency (likely ANSSI or a cyber-prosecutorial / OFAC-CCNUM unit) is not named.
- **Exact botnet size** — the DOJ release says "more than 200,000"; companion reporting suggests peak ~260,000 in June 2024. The discrepancy is between conservative court-document language and threat-intelligence telemetry.
- **Court-order legal basis** — specific statutes and rule (likely Rule 41) are not enumerated in the DOJ release; the affidavit referenced in the release would clarify.
- **Persistence of disruption** — the release does not claim the threat actor is permanently dismantled; the FBI's continuing-investigation note implies expected reconstitution attempts.
- **2bagoldmule-style criminal indictment** — no individual is charged in this announcement. Whether downstream criminal indictments of Integrity Technology Group personnel or Flax Typhoon operators will follow is *unknown* from this source.
