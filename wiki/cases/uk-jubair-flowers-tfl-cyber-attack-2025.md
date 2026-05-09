---
type: case
title: "R v. Jubair and Flowers (TfL Cyber Attack) (2025)"
case_number: "Westminster Magistrates Court (charged 2025-09-18); committed to Southwark Crown Court (first hearing scheduled 2025-10-16) — specific docket numbers not in the press release"
jurisdiction: "Westminster Magistrates Court → Southwark Crown Court (England and Wales)"
jurisdiction_country: "[[united-kingdom]]"
jurisdictions:
  - "[[united-kingdom]]"
  - "[[united-states]]"
case_type: prosecution
status: arrested
crime_charged:
  - "[[hacking-ic]]"
  - "[[ransomware-ic]]"
defendants:
  - name: "Thalha Jubair"
    nationality: "British (resident East London)"
    age: 19
    status: "Arrested 2025-09-16; charged 2025-09-18 at Westminster Magistrates Court; remanded into custody; due Southwark Crown Court 2025-10-16"
    sentence: ""
    location_at_arrest: "East London, United Kingdom"
    charges:
      - "Conspiring to commit unauthorised acts against TfL — Computer Misuse Act 1990"
      - "Failure to disclose pin/passwords for seized devices — Regulation of Investigatory Powers Act 2000 (RIPA) s.49"
  - name: "Owen Flowers"
    nationality: "British (resident Walsall, West Midlands)"
    age: 18
    status: "Initially arrested 2024-09-06 (TfL attack); re-arrested 2025-09-16; charged 2025-09-18; remanded; due Southwark Crown Court 2025-10-16"
    sentence: ""
    location_at_arrest: "Walsall, West Midlands, United Kingdom"
    charges:
      - "Conspiring to commit unauthorised acts against TfL — Computer Misuse Act 1990"
      - "Conspiring to infiltrate and damage the networks of SSM Health Care Corporation (US) — Computer Misuse Act / fraud-related charges (per CPS statement)"
      - "Attempting to infiltrate and damage the networks of Sutter Health (US) — Computer Misuse Act / fraud-related charges (per CPS statement)"
related_operation:
  - "[[us-v-jubair-scattered-spider-2025]]"
ic_elements:
  mlat_requests:
    []
  extradition: "None — both defendants are UK nationals arrested on UK soil and prosecuted in UK courts. No US extradition request announced; UK prosecution covers Flowers' alleged offences against US healthcare entities directly."
  evidence_from_abroad:
    - "United States (SSM Health Care Corporation and Sutter Health victim incident evidence — likely (55-80%) supplied via FBI cooperation, not specified in source)"
  foreign_arrests:
    []
  asset_freezing:
    []
cooperating_agencies:
  - "[[uk-nca]]"
  - "[[city-of-london-police]]"
  - "[[fbi]]"
legal_frameworks_invoked:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[mlat-process]]"
key_legal_issues:
  - "[[dual-criminality]]"
precedent_value: "Illustrates the UK's standalone cybercrime prosecution capability for cross-border attacks on US victim organisations: UK-resident UK-national defendants prosecuted in UK courts under Computer Misuse Act 1990 for offences against US healthcare networks, without an extradition request from the US. Also illustrates use of RIPA s.49 (compelled password disclosure) as a charged-offence pressure mechanism in cybercrime prosecutions."
source_count: 1
sources:
  - "[[2025-09-18_nca-uk_two-charged-tfl-cyber-attack-jubair-flowers]]"
created: 2026-05-09
updated: 2026-05-09
---
> [!info] Provisional case page (source_count = 1)
> Below the preferred publication threshold of source_count >= 5. The page is published as a provisional record because the NCA press release is a tier-1 primary source and the case has clear durable IC value (UK-as-venue prosecution for cross-border attacks on US victims; RIPA s.49 password-disclosure charge; Scattered Spider attribution). Should be promoted to a full case page once additional tier-1 filings (CPS charge sheet, Crown Court indictment, judgment) are ingested.

## Summary

On 18 September 2025, the UK National Crime Agency announced that two men had been charged at Westminster Magistrates Court in connection with the 31 August 2024 cyber attack on Transport for London (TfL). Thalha Jubair, 19, of East London, and Owen Flowers, 18, of Walsall, West Midlands, were arrested at their home addresses on 16 September 2025 by NCA officers and City of London Police. Both face a conspiracy charge under the Computer Misuse Act 1990 for unauthorised acts against TfL's network. NCA attributes the TfL intrusion to the online criminal collective known as **Scattered Spider**.

Two further charges sets are notable. First, Flowers — who was initially arrested on 6 September 2024 in connection with the TfL attack and re-arrested on 16 September 2025 — has additionally been charged with conspiring to infiltrate and damage the networks of two US healthcare entities, **SSM Health Care Corporation** and **Sutter Health**, both based in the United States. Second, Jubair has additionally been charged under the Regulation of Investigatory Powers Act 2000 (RIPA) for failing to disclose the pin or passwords for devices seized from him. Both defendants were remanded into custody and were due at Southwark Crown Court on 16 October 2025.

The case is significant for international cooperation on two grounds: it demonstrates that the United Kingdom is capable of prosecuting domestically resident UK nationals for cybercrimes targeting overseas victim organisations without an extradition request, and it documents an explicit FBI partnership channel for the Scattered Spider investigations more broadly.

## Facts

- **Defendants**: Thalha Jubair, 19, East London; Owen Flowers, 18, Walsall, West Midlands. Both UK nationals resident in the UK.
- **Underlying conduct (TfL)**: Network intrusion against Transport for London on 31 August 2024 (per NCA). NCA attributes the intrusion to the **Scattered Spider** online criminal collective. The release describes "significant disruption" and "millions in losses to TfL, part of the UK's critical national infrastructure" without quoting a specific monetary figure.
- **Underlying conduct (US healthcare — Flowers only)**: Conspiring with others to infiltrate and damage the networks of **SSM Health Care Corporation** and attempting to do the same to **Sutter Health's** networks, both based in the US. The release does not specify dates, victim counts, or financial impact for the US-side conduct, beyond Flowers' role.
- **Arrest sequence**: Flowers initially arrested 6 September 2024 in connection with the TfL attack. NCA officers state that, at that point, they identified "further potential evidence of offending against US healthcare companies." Both Flowers and Jubair re-arrested 16 September 2025 (Tuesday) at their home addresses by NCA + City of London Police.
- **Charging**: 18 September 2025, Westminster Magistrates Court, after CPS authorisation.
- **Charges (Jubair)**: (i) conspiring to commit unauthorised acts against TfL under the Computer Misuse Act 1990; (ii) RIPA offence — failure to disclose pin/passwords for seized devices.
- **Charges (Flowers)**: (i) conspiring to commit unauthorised acts against TfL under the Computer Misuse Act 1990; (ii) conspiring to infiltrate and damage SSM Health Care Corporation networks; (iii) attempting to infiltrate and damage Sutter Health networks.
- **Custody**: Both remanded into custody. Next hearing Southwark Crown Court, 16 October 2025.
- **UK supporting agencies**: West Midlands Regional Organised Crime Unit; British Transport Police.
- **International partner named**: FBI.

## International Cooperation Elements

### Evidence Gathering

The NCA release names the **FBI** as an "international partner" in the broader Scattered Spider effort and acknowledges UK domestic supporting bodies (West Midlands ROCU, British Transport Police, City of London Police). It does **not** specify the legal vehicle for any US-side evidence used to support the SSM Health / Sutter Health charges. **Likely** (55–80%) that US-side evidence — victim incident reports, server logs, intrusion telemetry — was supplied via informal FBI-to-NCA cooperation channels and/or formal MLAT requests pursuant to the [[budapest-convention]] preservation/production framework, given the routine FBI-NCA cybercrime liaison; this is an inference, not a stated fact in the source.

### Arrest and Extradition

- **No extradition required**: Both defendants are UK nationals resident in the UK, arrested on UK soil. No US extradition request has been announced. The UK CPS has decided to prosecute Flowers' US-victim conduct in UK courts under UK statute. This is the **opposite pattern** to many high-profile cybercrime cases (e.g., [[us-v-kai-west-intelbroker-2025]], where a UK national arrested in France faces a US extradition track).
- **Dual criminality** ([[dual-criminality]]) **not directly engaged** for arrest because no extradition is at issue. It will indirectly become relevant if the United States later supersedes with a parallel indictment that would require coordination on specialty / non-bis-in-idem with the UK conviction; the press release does not mention any such US filing.
- **Compelled disclosure (RIPA s.49)**: Jubair's RIPA charge for failing to disclose pin/passwords for seized devices is a UK-specific procedural-law mechanism (Part III RIPA, s.49–53) without a clean equivalent in many cooperating jurisdictions and is itself a recurrent IC friction point — foreign authorities cannot directly invoke it on UK-seized devices, and the UK cannot directly require it on devices seized abroad even with MLAT cooperation.

### Asset Recovery

The NCA release does not identify any seized devices' contents (beyond the implied existence of password-protected devices triggering Jubair's RIPA charge), frozen assets, or recovered cryptocurrency. Asset recovery, if any, will appear in subsequent CPS or Crown Court filings.

## Legal Analysis

### Jurisdiction

UK criminal jurisdiction over the TfL conduct is grounded in standard UK territoriality (defendants resident in the UK; victim TfL based in the UK; conduct against UK critical national infrastructure). Jurisdiction over Flowers' SSM Health / Sutter Health conduct is grounded in the Computer Misuse Act 1990 s.4 / s.5 extraterritoriality framework, which gives UK courts jurisdiction over offences under ss.1–3 / s.3ZA where there is a "significant link with the domestic jurisdiction" — typically satisfied by the defendant operating from within the UK at the time of the offence. **Highly likely** (80–95%) that this is the jurisdictional basis being relied upon for the US-victim charges, though the press release does not explicitly cite it.

### Key Legal Issues

- **Computer Misuse Act 1990 § 3 (and § 1 for unauthorised access)**: Unauthorised acts with intent to impair operation of a computer / unauthorised access. Applied as a conspiracy charge under common-law conspiracy principles or the Criminal Law Act 1977 conspiracy statute.
- **RIPA s.49 (Regulation of Investigatory Powers Act 2000, Part III)**: Notice to disclose protected information / encryption keys; non-compliance is itself an offence. Applied here to Jubair as a stand-alone charge separate from the substantive Computer Misuse Act count.
- **CMA s.4–5 extraterritoriality**: Engaged for Flowers' US-victim conduct; turns on the "significant link with domestic jurisdiction" doctrine.
- **Scattered Spider attribution**: NCA's public attribution to the Scattered Spider collective is a statement of investigative belief rather than a charged conspiracy with named co-conspirators. Convicting on the conspiracy count does not require proving membership of Scattered Spider; it requires proving an agreement between Jubair and Flowers (and others) to commit unauthorised acts against TfL.

### Precedent Value

Modest at this charging stage (no trial yet). The case is most useful as a contemporary illustration of:
- **UK-as-prosecution-venue** for a UK-national defendant whose alleged conduct includes attacks on US victim organisations — with no extradition track in evidence — running in parallel to the **US-as-prosecution-venue, France-as-arrest-venue** track in [[us-v-kai-west-intelbroker-2025]];
- **RIPA s.49** charged offence as a procedural pressure mechanism in cybercrime prosecutions, which does not have a clean equivalent in many cooperating jurisdictions;
- **Scattered Spider attribution** in a tier-1 UK law enforcement statement, anchoring later analyses of UK / English-speaking-country cyber-criminal ecosystems.

## Proceedings Timeline

| Date | Event |
|---|---|
| 2024-08-31 | Network intrusion against Transport for London (TfL); NCA later attributes to Scattered Spider. |
| 2024-09-06 | Flowers initially arrested in connection with the TfL attack; further potential evidence of offending against US healthcare companies identified at this stage. |
| 2025-09-16 | Jubair and Flowers arrested at home addresses by NCA + City of London Police. |
| 2025-09-18 | Both charged at Westminster Magistrates Court under the Computer Misuse Act for conspiracy against TfL. Flowers additionally charged in respect of SSM Health and Sutter Health. Jubair additionally charged under RIPA s.49. Both remanded. |
| 2025-10-16 | Scheduled first hearing at Southwark Crown Court (per press release; outcome not in source). |
| (pending) | Plea, trial, verdict, sentence; any US-side superseding indictment (none announced). |

## Cooperation Effectiveness

- **Speed**: TfL intrusion 2024-08-31 → first arrest (Flowers) 2024-09-06 (~1 week) → joint arrest + charge 2025-09-16/18 (~12.5 months). The 12-month gap between Flowers' initial arrest and the joint charging is consistent with a complex digital-forensics-led investigation involving cross-border evidence on the US-victim charges.
- **Breadth**: The named cooperation footprint is comparatively narrow on the public record — UK domestic agencies (NCA, City of London Police, West Midlands ROCU, British Transport Police, CPS) plus the FBI as a generic "international partner." No other foreign LE or non-FBI US bodies are credited in the release.
- **Frictions identified in the public record**: None disclosed by NCA. RIPA s.49 charge implies the existence of encrypted/password-protected devices that would otherwise frustrate evidence extraction — an internal UK procedural-pressure response rather than a cooperation friction per se.
- **Notable absence**: No reference to ECHR-based mutual recognition mechanisms, no reference to the Council of Europe Budapest Convention by name, and no acknowledgement of any third-country LE assistance. The release frames the case as an NCA-led UK domestic prosecution that incidentally covers offences against US victims.

## Korean Relevance (한국 관련성)

The press release does not identify Korean victims, Korean-based infrastructure, or Korean LE participation. Indirect relevance:

- **UK-as-venue model**: Korean authorities ([[knpa-cyber-bureau]] equivalent successor, [[supreme-prosecutors-office-korea|대검 사이버수사과]]) regularly pursue cybercrime suspects who target Korean victims from third countries; the Jubair–Flowers case illustrates the converse — a destination state (UK) prosecuting its own residents for offences against foreign (US) victims without waiting for an extradition request. This is a model worth considering for Korean-resident defendants whose alleged victims are abroad. Likely (55–80%) relevant for future cross-border Korean cybercrime prosecutions where the suspect is a Korean national.
- **RIPA-style compelled disclosure**: Korean criminal procedure does not have a direct analogue to RIPA s.49 (compelled password disclosure as a stand-alone offence). The case adds to the comparative-procedural-law inventory of how different jurisdictions overcome encryption-on-seizure problems.
- **Scattered Spider exposure to Korean targets**: Scattered Spider is widely associated with attacks on telecommunications, hospitality, retail, and casino targets globally; Korean exposure has been mentioned in industry threat intel but is not asserted by this NCA source.

## Contradictions & Open Questions

> [!note] "£39 million loss" figure
> Public reporting on the TfL incident (UK financial press, TfL annual reporting) commonly cites approximately **£39 million** in losses. The NCA press release uses only the qualitative phrase "millions in losses" and does not state the figure. The case page therefore deliberately does not record £39M as a fact derived from this source. To be reconciled when a tier-1 UK source (TfL annual report, court sentencing remarks) is ingested.

> [!warning] Legal status check needed
> Status field is "arrested / charged / remanded" as of the press release dated 2025-09-18. As of the case-page creation date (2026-05-09), the 16 October 2025 Southwark Crown Court hearing outcome and any plea / further hearings are not yet ingested; status, plea, and any sentencing should be re-verified.

> [!note] Translation note
> "Conspiring together to commit unauthorised acts" is the NCA's plain-English description; the precise statutory wording is **Computer Misuse Act 1990 s.3** ("Unauthorised acts with intent to impair, or with recklessness as to impairing, operation of computer, etc.") and (likely) **Criminal Law Act 1977 s.1** for conspiracy. The exact charge statement on the indictment is not quoted in the release.

Open questions:

1. Specific Computer Misuse Act subsection(s) charged (s.1, s.3, s.3ZA, or combinations) — confirm against the CPS charge sheet or Crown Court indictment.
2. Precise legal vehicle for any US-side evidence (FBI informal cooperation, MLAT, Budapest Convention preservation/production order, CLOUD Act provider request) supporting the SSM Health / Sutter Health charges.
3. Whether the United States intends to seek extradition or file a parallel indictment, and how specialty / *non bis in idem* would be coordinated with the UK proceedings.
4. Identity and roles of the unnamed "others" with whom Flowers is alleged to have conspired against the US healthcare networks — separately charged or only referenced in the conspiracy count?
5. Outcome of the 16 October 2025 Southwark Crown Court hearing.
6. Whether the £39M figure cited in public reporting is reconcilable with TfL's audited financial impact.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2025-09-18_nca-uk_two-charged-tfl-cyber-attack-jubair-flowers\|Two charged for TfL cyber attack]] | UK National Crime Agency | 2025-09-18 | https://www.nationalcrimeagency.gov.uk/news/two-charged-for-tfl-cyber-attack |
