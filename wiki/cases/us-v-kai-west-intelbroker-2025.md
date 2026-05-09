---
type: case
title: "United States v. Kai West (IntelBroker) (2025)"
case_number: "Press Release No. 25-149 (S.D.N.Y. unsealed 2025-06-25); indictment and complaint filed under separate dockets — specific docket numbers not in the press release"
jurisdiction: "U.S. District Court for the Southern District of New York"
jurisdiction_country: "[[united-states]]"
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[france]]"
case_type: prosecution
status: arrested
crime_charged:
  - "[[hacking-ic]]"
  - "[[extortion-ic]]"
  - "[[cybercrime-forum-ic]]"
defendants:
  - name: "Kai West (a/k/a 'IntelBroker', a/k/a 'Kyle Northern')"
    nationality: British
    age: 25
    status: "arrested in France ~February 2025; held in French pre-trial detention pending U.S. extradition"
    sentence: ""
    location_at_arrest: France
related_operation:
  - "[[leakbase-takedown-2026]]"
  - "[[us-v-jubair-scattered-spider-2025]]"
ic_elements:
  mlat_requests:
    - "France (assistance acknowledged)"
    - "Spain (assistance acknowledged)"
    - "United Kingdom (assistance acknowledged)"
    - "Netherlands (assistance acknowledged)"
  extradition: "United States seeking extradition of Kai West from France (US-France extradition treaty track; pre-trial detention in France since ~Feb 2025)"
  evidence_from_abroad:
    - France
    - Spain
    - "United Kingdom"
    - Netherlands
  foreign_arrests:
    - "France (~February 2025)"
  asset_freezing:
    []
cooperating_agencies:
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
legal_frameworks_invoked:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[mlat-process]]"
  - "[[extradition]]"
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[dual-criminality]]"
precedent_value: "Illustrates Office of International Affairs (OIA) coordination of a four-jurisdiction (FR/ES/UK/NL) law-enforcement assistance package supporting an SDNY indictment plus a France-based arrest and extradition track for an English-language cybercrime-forum operator."
source_count: 1
sources:
  - "[[2025-06-25_justice-gov-sdny_serial-hacker-intelbroker-kai-west-charged-25m-damages]]"
created: 2026-05-09
updated: 2026-05-09
---
> [!info] Provisional case page (source_count = 1)
> Below the preferred publication threshold of source_count >= 5. The page is published as a provisional record because the SDNY press release is a tier-1 primary source and the case has clear durable IC value (US-France extradition track + four-jurisdiction MLA assistance + BreachForums nexus). Should be promoted to a full case page once additional tier-1 filings (indictment PDF, complaint PDF, extradition order) are ingested.

## Summary

On 25 June 2025, the U.S. Attorney's Office for the Southern District of New York and the FBI's New York Field Office announced the unsealing of a four-count criminal Indictment and Complaint charging Kai West, 25, a British national operating under the online aliases "IntelBroker" and "Kyle Northern," with a years-long hacking and stolen-data resale scheme. According to the SDNY release, West led a hacking group ("CyberN[------]") that compromised more than 40 victim organizations — including a U.S.-based telecommunications provider, a municipal healthcare provider, and an Internet service provider — between approximately January 2023 and February 2025, then offered the stolen data on a hacker marketplace identified in the release only as "Forum-1." Across the period, West posted approximately 158 forum threads (41 sale offers, 117 free or credit-based distributions, with at least 16 priced threads totalling $2,467,000+ in asking price), seeking at least $2 million and causing aggregate victim damages of at least $25 million. From August 2024 to January 2025, "IntelBroker" was publicly identified on Forum-1 as the site's "owner."

West was arrested in France in February 2025 and is being held pending U.S. extradition. The case has been assigned to U.S. District Judge Katherine Polk Failla and is being prosecuted by SDNY's Complex Frauds and Cybercrime Unit (AUSA Ryan B. Finkel).

## Facts

- **Defendant**: Kai West, 25, British national; aliases "IntelBroker," "Kyle Northern."
- **Conduct period**: approximately January 2023 to February 2025 (per Forum-1 post review). The press release also references the conduct as "years-long" running through 2025.
- **Method**: West allegedly led an online hacking group ("CyberN[------]"), exploited misconfigured servers and other intrusion vectors, exfiltrated customer data and corporate marketing data, and resold the data via Forum-1 posts. Payment was solicited in **Monero**, a privacy-enhancing cryptocurrency. At least one priced post (March 6, 2023) offered patient data from a municipal healthcare provider including names, Social Security numbers, dates of birth, gender, health-plan and employer information.
- **Forum-1 ownership**: From approximately August 2024 to January 2025, "IntelBroker" was identified on Forum-1 as the forum's owner. The press release does not name the forum, but the IntelBroker handle and ownership window are widely associated externally with BreachForums; the case is therefore likely (55–80% confidence based on press-release content alone) part of the broader BreachForums marketplace ecosystem comparable to [[leakbase-takedown-2026]].
- **Activity counts**: ~158 threads; ~41 sale offers; ~117 free / credit-based distributions; ~16 priced threads totalling at least $2,467,000 asked; at least 41 of 158 threads sold data from U.S.-based companies; at least 46 of 158 threads indicate co-conspirator "CC-1" involvement.
- **Damages**: at least $25,000,000 across more than 40 victim organizations.
- **Arrest**: France, February 2025. Pre-trial detention in France pending U.S. extradition request.

## International Cooperation Elements

### Evidence Gathering

The SDNY release explicitly thanks **French, Spanish, British, and Dutch authorities** for their assistance, alongside FBI New York and the **DOJ Office of International Affairs** ([[office-of-international-affairs]]). The release does not specify the legal vehicle (MLAT vs. informal police cooperation vs. Budapest Convention Article 31/32 production requests), but a four-jurisdiction package on a cybercrime-forum operator typically combines MLAT requests for stored content, informal LE-to-LE coordination via [[europol-ec3]] / national cyber units, and Budapest-Convention-style preservation orders. **Likely** (55–80%) that the Spanish and Dutch assistance reflects evidence on Forum-1 hosting infrastructure and on co-conspirators rather than custody of the principal defendant.

### Arrest and Extradition

- **Foreign arrest**: France, ~February 2025 (per SDNY release). Whether by Police Nationale, Gendarmerie cyber unit (C3N), or the Paris cybercrime parquet (J3) is not specified in the release.
- **Extradition track**: United States is seeking extradition under the US-France extradition treaty framework. As of the case-page creation date (2026-05-09), the SDNY release describes West as still detained in France and the US as still "seeking" extradition; current extradition status should be re-verified against subsequent filings.
- **Dual criminality** ([[dual-criminality]]): the four federal counts (computer-intrusion conspiracy, wire-fraud conspiracy, unauthorized access, wire fraud) all map onto French *atteintes aux systèmes de traitement automatisé de données* (Code pénal Art. 323-1 et seq.) and *escroquerie en bande organisée* — therefore **highly likely** (80–95%) that dual criminality is satisfied.

### Asset Recovery

The press release does not identify any seized assets, frozen wallets, or recovered cryptocurrency. West's stated payment instrument was Monero, which presents well-documented forensic challenges for asset tracing relative to Bitcoin or Ethereum. Asset recovery, if any, will appear in subsequent filings.

## Legal Analysis

### Jurisdiction

SDNY personal/conduct jurisdiction is grounded in (i) at least 41 of 158 Forum-1 threads selling data from U.S.-based victim companies, (ii) a U.S.-based telecommunications-provider victim, and (iii) wire-fraud venue based on transmissions in interstate or foreign commerce affecting the Southern District of New York. Foreign-defendant U.S. cybercrime indictments based on extraterritorial conduct against U.S. victims have an established post-*Skinner / In re Warrant* line; venue and jurisdictional challenges are foreseeable but unlikely to defeat the core counts.

### Key Legal Issues

- **[[dual-criminality]]** and the French extradition decision (likely turns on substantive equivalence of U.S. and French computer-intrusion offenses, which is well established).
- **Specialty / Rule of Specialty** (post-extradition limit on prosecution to charged conduct) — relevant if SDNY later supersedes the indictment.
- **Evidence admissibility** for foreign-collected forum content under the "good faith" and Federal Rules of Evidence Rule 901 authentication framework, particularly where evidence is gathered via four-jurisdiction MLA.

### Precedent Value

Modest at this stage (pre-extradition). The case is most useful as a contemporary illustration of OIA-coordinated multi-MLA fan-out around a single English-language cybercrime-forum operator and as a parallel to [[leakbase-takedown-2026]] — both reflect a 2024–2026 enforcement turn toward forum operators rather than only end-user buyers.

## Proceedings Timeline

| Date | Event |
|---|---|
| ~2023-01 | Earliest Forum-1 ("BreachForums") posts attributed to "IntelBroker" identified in the indictment review window. |
| 2023-03-06 | Forum-1 post offering municipal healthcare provider patient data (per press release). |
| 2024-08 | "IntelBroker" identified as Forum-1 owner (start of ownership window). |
| 2025-01 | End of "IntelBroker" Forum-1 ownership window. |
| 2025-02 | Kai West arrested in France. |
| 2025-06-25 | SDNY/FBI NY unseal four-count Indictment and Complaint (Press Release No. 25-149); case assigned to Judge Katherine Polk Failla. |
| 2025-06-26 | Press release page updated. |
| (pending) | French extradition decision; U.S. arraignment after surrender. |

## Cooperation Effectiveness

- **Speed**: Arrest occurred ~February 2025; SDNY indictment unsealed June 25, 2025 — a roughly four-month interval consistent with coordinated MLAT/extradition packages where the foreign authority has executed a custody arrest first.
- **Breadth**: Four foreign jurisdictions named for assistance (FR, ES, UK, NL) plus OIA coordination — a relatively dense cooperation footprint for a single-defendant cybercrime indictment, **likely** indicating that Forum-1 / BreachForums infrastructure or co-conspirator evidence sits across all four.
- **Frictions identified in the public record**: none disclosed. Monero use will create forensic friction at the asset-tracing stage; this is not a cooperation friction per se but interacts with whether MLA-recovered evidence can establish proceeds value.

## Korean Relevance (한국 관련성)

The press release does not identify Korean victims, Korean-based infrastructure, or Korean LE participation. Indirect relevance:

- The case reinforces the value of the FBI/DOJ 24/7 channel and OIA-coordinated multi-MLA fan-out, which Korean authorities ([[knpa-cyber-bureau]] equivalent successor and the [[supreme-prosecutors-office-korea|대검 사이버수사과]]) routinely engage with for inbound BreachForums-related intrusions.
- Forum-1 (BreachForums) has historically been a marketplace for data exfiltrated from Korean targets; a successful US-led prosecution of its alleged owner has **likely** (55–80%) downstream evidentiary value for Korean victim notifications and for Korean-side investigations of Korean buyers/sellers on the same forum, but this is not asserted by the source.

## Contradictions & Open Questions

> [!note] Forum-1 / BreachForums identification
> The SDNY release names the marketplace only as "Forum-1." Identification of Forum-1 as BreachForums in this case page is an external attribution based on the IntelBroker handle, the August 2024 to January 2025 ownership window, and contemporaneous reporting. Should be cited explicitly to a tier-1 source (indictment PDF or complaint PDF) once ingested.

> [!warning] Legal status check needed
> Status field is "arrested" (held in French pre-trial detention pending U.S. extradition) as of the press release dated 2025-06-25 and updated 2025-06-26. As of the case-page creation date (2026-05-09), the actual extradition decision and any superseding indictment are not yet ingested; status, sentence, and extradition outcome should be re-verified.

> [!note] Translation note
> Underlying French penal-code anchors for dual criminality (Code pénal Art. 323-1 *accès frauduleux à un système de traitement automatisé de données*; Art. 323-3 *modification frauduleuse*; Art. 313-2 *escroquerie aggravée*) are added by this case page based on standard French equivalence; they are not quoted in the SDNY release.

Open questions:

1. Identity of "Forum-1" — confirm against the unsealed indictment PDF (cited in the release as `u.s._v._west_indictment.pdf`).
2. Roles of co-conspirator "CC-1" and "CyberN[------]" — does either map to a separately charged or already-indicted defendant?
3. Specific role of Spanish, British, and Dutch authorities — infrastructure seizure? co-conspirator interview? content production from a hosting provider?
4. Whether Monero traceability efforts produced any seized cryptocurrency.
5. Current French extradition status and any French-court ruling on dual criminality / specialty.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2025-06-25_justice-gov-sdny_serial-hacker-intelbroker-kai-west-charged-25m-damages\|Serial Hacker 'IntelBroker' Charged For Causing $25 Million In Damages To Victims]] | US DOJ USAO-SDNY | 2025-06-25 | https://www.justice.gov/usao-sdny/pr/serial-hacker-intelbroker-charged-causing-25-million-damages-victims |
