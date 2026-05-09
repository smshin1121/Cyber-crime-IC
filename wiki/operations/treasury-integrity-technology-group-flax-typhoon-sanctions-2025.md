---
type: operation
title: "U.S. Treasury OFAC Sanctions Designation of Integrity Technology Group (Flax Typhoon, PRC) — January 2025"
aliases:
  - "Treasury Integrity Tech sanctions 2025"
  - "OFAC Integrity Technology Group designation"
  - "Flax Typhoon sanctions January 2025"
  - "jy2769 OFAC sanctions"
case_id: CYB-2025-130
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - asset_freeze
outcome: success
timeframe:
  announced: 2025-01-03
  start: 2025-01-03
  end: 2025-01-03
  ongoing: false
crime_types:
  - "[[hacking-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
crime_type: "[[cybercrime-infrastructure-ic]]"
target_entity: "Integrity Technology Group, Inc. (Flax Typhoon)"
lead_agency: "[[us-treasury]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[china]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[fbi]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "OFAC designation of Integrity Technology Group, Incorporated (Beijing-based, publicly-traded) under EO 13694 as amended by EO 13757."
    - "All property and interests of Integrity Tech in the United States or in possession/control of U.S. persons blocked; reporting to OFAC required."
    - "U.S. persons prohibited from transactions involving the entity unless OFAC-licensed; foreign financial institutions facilitating significant transactions face secondary-sanctions risk."
    - "Entities owned 50% or more by Integrity Tech also blocked under OFAC 50% Rule."
edges: []
credibility_index: 0.0
source_tier: 1
missing_fields:
  - "OFAC SDN list entry identifiers (SDN program code, listing ID)"
  - "Specific U.S. critical-infrastructure sectors identified as Flax Typhoon victims (release does not enumerate sectors)"
  - "Direct ingest of primary Treasury URL — fetch timed out; reconstructed from secondary mirrors per L11"
related_cases: []
related_operations:
  - "[[us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024]]"
challenges_encountered: []
lessons_learned:
  - "Targeted financial sanctions (OFAC designation) are now the standard third-track instrument in the U.S. response to PRC-contractor cyber operations, following court-authorized takedown (DOJ/FBI) and FVEY joint cybersecurity advisory — staged over ~3.5 months in the Flax Typhoon case."
  - "OFAC designation can name a publicly-traded foreign cybersecurity company directly as a state-sponsored APT enabler, attaching reputational and economic cost to the corporate entity rather than only individuals."
  - "The IC scope of an OFAC designation is structurally narrow when no parallel partner-state sanctions are issued — the action's cooperative dimension is limited to prior FVEY information-sharing (the September 2024 joint advisory) rather than coordinated multilateral financial measures."
source_count: 1
sources:
  - "[[2025-01-03_treasury_sanctions-integrity-technology-group-flax-typhoon]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional page
> Published below the preferred 5-source threshold (CLAUDE.md "Entity creation threshold"). One tier-1 primary source (Treasury OFAC press release jy2769, 3 January 2025; reconstructed from three independent secondary mirrors per L11 — primary URL fetch timed out). Companion artifacts to ingest in subsequent rounds: (a) the OFAC SDN list entry for Integrity Tech, (b) any subsequent FBI/CISA advisory updates citing the designation, (c) any later UK/AU/CA/NZ parallel actions if issued.

> [!warning] IC scope flag — U.S. unilateral sanction
> This is a **U.S. unilateral targeted financial designation** by OFAC. Unlike the September 2024 DOJ Raptor Train takedown, this action is **not accompanied by parallel partner-state sanctions** in the United Kingdom, Australia, Canada, or New Zealand on the announcement date (per the source release). The "Five Eye partners" reference in the press release applies retrospectively to the **September 18, 2024 joint cybersecurity advisory** — not to this OFAC designation. The IC dimension here is therefore limited to **prior cooperative attribution** (FVEY advisory) rather than **coordinated financial measures**. Per CLAUDE.md "Entity creation threshold" and L19, only `[[united-states]]` (designating authority) and `[[china]]` (target nationality) are asserted as participating_countries.

> [!warning] Per L19 — only entities explicitly named in the primary source are asserted
> Asserted: **U.S. Treasury OFAC** (designating authority), **FBI** (named in the release as the agency whose September 2024 advisory documents Integrity Tech's role), and **Integrity Technology Group, Inc.** (target entity, [[china|People's Republic of China]]). NSA, USCYBERCOM CNMF, and FVEY partner cyber agencies are referenced only via the September 2024 joint advisory — they are not co-actors of this January 2025 OFAC action and are not asserted here.

## Summary

On **3 January 2025**, the **U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC)** designated **Integrity Technology Group, Incorporated** — a Beijing-based, publicly-traded cybersecurity company assessed by the FBI as the corporate entity behind the China-based hacker activity industry tracks as **Flax Typhoon** — for its role in computer intrusion incidents targeting U.S. victims and U.S. critical infrastructure (Source: [[2025-01-03_treasury_sanctions-integrity-technology-group-flax-typhoon|Treasury OFAC press release jy2769, 3 Jan 2025]]).

The designation is issued under **Executive Order 13694** ("Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities," 1 April 2015) **as amended by Executive Order 13757** (28 December 2016). Its legal effect is to block all Integrity Tech property and interests in the United States or in U.S.-person control, prohibit U.S.-person transactions absent OFAC license, and expose foreign financial institutions facilitating significant transactions to secondary-sanctions risk.

This designation is the **targeted-sanction companion** to the September 18, 2024 [[us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024|DOJ court-authorized Raptor Train botnet disruption]]. The U.S. response to Flax Typhoon / Integrity Technology Group is therefore now a **three-track package**: (i) court-authorized infrastructure takeover (DOJ/FBI, Sept 2024), (ii) FVEY joint cybersecurity advisory (FBI + NSA + USCYBERCOM CNMF + AU/CA/NZ/UK partner cyber agencies, Sept 2024), and (iii) OFAC targeted financial designation (Treasury, Jan 2025). The three actions are spaced approximately **3.5 months** apart.

It is **almost certain** (>95% confidence, tier-1 Treasury source) that the designation occurred on the announced date with the stated authority and target. It is **likely** (55-80%) that follow-on or parallel partner-state designations could be issued by FVEY allies in subsequent rounds, but **no such parallel action is documented in this primary source**.

## Background

**Flax Typhoon** is the industry name for a PRC state-sponsored cyber group active since at least 2021 (Microsoft Threat Intelligence assessment, corroborated by FBI investigation). Per the Treasury release, Flax Typhoon has compromised computer networks in **North America, Europe, Africa, and across Asia, with a particular focus on Taiwan**. Its operating model exploits publicly known vulnerabilities for initial access and uses legitimate remote access software for persistence.

Between **summer 2022 and fall 2023**, Flax Typhoon used infrastructure tied to **Integrity Technology Group** during network exploitation activities against multiple victims, regularly transmitting and receiving information through Integrity Tech systems. The underlying botnet (publicly named **"Raptor Train"** by Lumen Technologies' Black Lotus Labs in July 2023) comprised more than **260,000 internet-connected devices** at peak (IP cameras, NAS appliances, SOHO routers).

The DOJ's September 18, 2024 court-authorized takedown disrupted the Raptor Train C2 infrastructure (>200,000 devices at takedown). The companion FBI/NSA/CNMF/FVEY joint cybersecurity advisory issued the same day publicly documented Flax Typhoon TTPs and Integrity Tech's support role. The OFAC designation 3.5 months later applies a financial-sanctions consequence to the corporate entity that DOJ had previously disrupted.

## Participating Parties

### Designating authority

- **[[us-treasury|U.S. Department of the Treasury]] — Office of Foreign Assets Control (OFAC)** — issued the designation under EO 13694 as amended by EO 13757.

### U.S. components named or referenced

- **[[fbi|Federal Bureau of Investigation]]** — named in the press release as the agency whose September 18, 2024 joint cybersecurity advisory documented Flax Typhoon TTPs and Integrity Tech's support role. The FBI's investigative attribution underpins the OFAC designation.

### Quoted official

- **Bradley T. Smith** — Acting Under Secretary of the Treasury for Terrorism and Financial Intelligence (TFI). Quote: *"The Treasury Department will not hesitate to hold malicious cyber actors and their enablers accountable for their actions."*

### Target

- **Integrity Technology Group, Incorporated** — Beijing-headquartered, publicly-traded ([[china|People's Republic of China]]). Public brand "KRLab" per companion DOJ Raptor Train release. FBI assesses Integrity Tech is responsible for activity industry tracks as **Flax Typhoon**.

### Partner-state sanctions on this date

- **None documented.** No parallel UK / Australia / Canada / New Zealand sanctions issued the same day. See IC scope flag above.

## Legal Framework

The designation rests on:

- **Executive Order 13694** — "Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities" (1 April 2015). Establishes OFAC authority to designate persons (including entities) responsible for or complicit in cyber-enabled activities posing a significant threat to U.S. national security, foreign policy, or economic health/financial stability.
- **Executive Order 13757** — Amends EO 13694 (28 December 2016). Expands and clarifies the scope of cyber-sanctions authority.
- Both EOs are issued under the **International Emergency Economic Powers Act (IEEPA)** and the **National Emergencies Act (NEA)** as the underlying statutory frameworks (not separately enumerated in this release per L19).

> [!warning] Legal status check needed — specific SDN program coding
> The Treasury press release does not enumerate the specific OFAC SDN program code(s) used (e.g., CYBER2). The OFAC SDN list entry for Integrity Tech should be ingested as a separate authoritative source for full programmatic detail.

## Operational Timeline

- **Since at least 2021** — Flax Typhoon (industry name) active as a PRC state-sponsored cyber group; targets U.S. critical infrastructure and entities in North America, Europe, Africa, and Asia (particular focus on Taiwan).
- **Summer 2022 – fall 2023** — Flax Typhoon uses infrastructure tied to Integrity Technology Group during network exploitation against multiple U.S. victims (Treasury release).
- **July 2023** — Lumen / Black Lotus Labs publishes initial description of the botnet, naming it "Raptor Train".
- **18 September 2024** — DOJ announces court-authorized takedown of Raptor Train (Press Release 24-1173); same-day FBI/NSA/CNMF/FVEY joint cybersecurity advisory documents Flax Typhoon TTPs and Integrity Tech's support role. (See [[us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024|companion operation]].)
- **3 January 2025** — Treasury OFAC issues press release jy2769 designating Integrity Technology Group under EO 13694 as amended by EO 13757. Bradley T. Smith (Acting Under Secretary for TFI) quoted.
- **Post-3 Jan 2025** — Property freezes take immediate effect; SDN list entry published; secondary-sanctions exposure begins for foreign financial institutions.

## Results and Impact

| Metric | Value |
|---|---|
| Entity designated | **Integrity Technology Group, Incorporated** (Beijing) |
| Authority | **EO 13694 as amended by EO 13757** |
| Designating agency | **OFAC** (Treasury) |
| Property in U.S. blocked | **All Integrity Tech property and interests; entities owned ≥50% by Integrity Tech also blocked** |
| U.S.-person transaction prohibition | **In force absent OFAC license** |
| Foreign financial institution exposure | **Secondary-sanctions risk for significant transactions** |
| Partner-state parallel sanctions on this date | **None documented** |
| Press release number | **jy2769** |
| Quoted official | **Bradley T. Smith, Acting Under Secretary, TFI** |
| Companion DOJ operation | **[[us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024]]** (24-1173, 18 Sep 2024) |
| Time gap from companion DOJ takedown | **~3.5 months** |

> [!note] Practical economic effect
> The asset-freeze and U.S.-person transaction prohibition apply to a publicly-traded Beijing entity. Practical effect is concentrated in the **financial-system perimeter** (USD-clearing, U.S.-person counterparties, foreign correspondent banks); direct asset seizure inside the PRC is not available. The designation's primary IC value is **public attribution + reputational/economic deterrence + secondary-sanctions leverage on third-country financial institutions**, not direct enforcement against the entity in its home jurisdiction.

## Cooperation Mechanisms Used

- **OFAC unilateral targeted designation** — primary mechanism. U.S. domestic authority (EO 13694 as amended by EO 13757; IEEPA/NEA underlying). No treaty mechanism invoked.
- **Prior FVEY information-sharing as predicate** — the September 18, 2024 joint cybersecurity advisory (FBI + NSA + USCYBERCOM CNMF + AU/CA/NZ/UK partner cyber agencies) provides the public-attribution predicate that supports the OFAC designation. This is **not a contemporaneous cooperation mechanism** for the January 2025 action but a **prior-track input**.
- **No MLAT, no Budapest Convention 24/7 Network, no extradition channel** — the target entity is in a host state (PRC) that does not cooperate on cybercrime IC pathways. The U.S. response is therefore **financial-system leverage** rather than evidence-and-arrest cooperation.

## Challenges and Friction Points

- **PRC host-state non-cooperation** — direct enforcement against Integrity Tech inside the PRC is not available. The designation works through extraterritorial financial-system leverage (USD-clearing, U.S.-person rules, secondary sanctions on foreign banks).
- **Borderline IC scope** — without parallel UK/AU/CA/NZ designations, the action's cooperative dimension is limited to prior attribution (FVEY advisory). This is a recurring challenge in U.S. cyber sanctions: many designations are unilateral despite the underlying intelligence being multilateral.
- **Designation does not equal disablement** — the entity remains operational in the PRC. The designation imposes financial cost and reputational signal but does not prevent further malicious activity. Continuity with reconstituted infrastructure is *highly likely* (80-95%) absent further enforcement.
- **Public-attribution-to-sanction lag** — ~3.5 months elapsed between the FBI/DOJ public attribution (Sept 2024) and the OFAC designation (Jan 2025). This lag is consistent with Treasury's diligence requirements for sanctions designations (legal sufficiency review, SDN listing process) but creates a gap during which the named entity could attempt asset relocation.

## Lessons Learned

- **OFAC targeted sanctions are now the standard third-track instrument** in U.S. responses to PRC-contractor cyber operations: court-authorized takedown (DOJ/FBI) + FVEY joint cybersecurity advisory + Treasury OFAC designation, staged over months. The Flax Typhoon / Integrity Technology Group sequence (Sept 2024 → Jan 2025) is the clearest example to date.
- **Naming a publicly-traded foreign cybersecurity contractor as the entity behind an APT** is a more aggressive disclosure pattern than naming the APT cluster only — it places direct reputational and economic cost on a foreign company. Consistent with the 2024-2025 U.S. shift toward naming PRC commercial intermediaries (Integrity Tech, i-Soon, Sichuan Silence, etc.).
- **Three-track package vs. single-track action** — OFAC alone is structurally narrower than the FVEY+DOJ package. The IC value of an OFAC designation is highest when paired with prior multilateral attribution; standalone designations have weaker cooperation footprint.
- **Primary-source fetch resilience matters** — the Treasury URL timed out during ingest; cross-validation against three independent secondary mirrors enabled reliable reconstruction (per LESSONS.md L11). For tier-1 government cyber-sanctions sources, redundant fetch paths (mirrors, archived PDFs, OFAC SDN list entries) are essential.

## Follow-Up Actions

- Ingest the **OFAC SDN list entry** for Integrity Tech as a separate authoritative source (program code, listing ID, address details).
- Retry primary Treasury URL fetch for verbatim text capture; replace reconstructed body if obtained.
- Monitor for **parallel UK / AU / CA / NZ designations** in 2025-2026 — none documented as of the source date but possible follow-on.
- Ingest the September 18, 2024 **FBI/NSA/CNMF + AU/CA/NZ/UK joint cybersecurity advisory** (companion artifact to both this designation and the DOJ Raptor Train takedown).
- Track any **subsequent OFAC designations of PRC cybersecurity contractors** (i-Soon, Sichuan Silence, etc.) for comparative analysis of the U.S. naming-and-sanctioning pattern.

## Korean Involvement (한국의 참여)

**None recorded.** The Treasury press release does not reference Korea, Korean entities, or Korean citizens. Korean relevance is **indirect comparative**:

- ROK does not currently have a domestic cyber-sanctions authority equivalent to EO 13694. Asset-freezing of a foreign cybersecurity contractor for state-sponsored cyber activity would require either (i) UN Security Council sanctions designation (politically blocked for PRC entities), (ii) ad hoc 외교부-led sanctions under existing frameworks (rare in cyber context), or (iii) bilateral coordination with U.S./EU sanctions regimes.
- The **three-track U.S. response model** (court-authorized takedown + FVEY advisory + Treasury sanctions) is not directly available to Korea given (a) Korea is not part of FVEY, (b) Korean criminal procedure does not currently provide an analog to U.S. court-authorized infrastructure takeover, and (c) Korea lacks an OFAC-equivalent cyber-sanctions program.
- For Korean victim entities of Flax Typhoon-class activity, **secondary effects of the OFAC designation** (prohibition on USD-clearing transactions involving Integrity Tech) provide indirect enforcement leverage if Korean financial institutions wish to avoid U.S. correspondent-banking exposure.

## Contradictions & Open Questions

- **Specific U.S. critical-infrastructure sectors targeted by Flax Typhoon** — the press release references "U.S. critical infrastructure sectors" but does not enumerate them. Telecom, energy, water, and government are *likely* (55-80%) included based on prior Flax Typhoon reporting, but not asserted from this primary source per L19.
- **Whether parallel UK/AU/CA/NZ designations were considered or are forthcoming** — unknown from this source. The FVEY pattern would predict eventual parallel actions, but as of 3 January 2025 none are documented.
- **OFAC SDN program code** — not enumerated in the press release. Likely **CYBER2** (the program established by EO 13694 as amended), but not asserted from this source.
- **Direct downstream criminal indictment of Integrity Tech personnel** — none announced as of this source. Whether DOJ will follow with named-individual charges is *unknown*.
- **Effect on Integrity Tech's public-trading status** — the company is described as "publicly traded" (per companion DOJ release). Whether the OFAC designation has triggered delisting or trading suspension on PRC exchanges is not addressed in this source.
