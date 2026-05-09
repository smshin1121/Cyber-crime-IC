---
type: case
title: "United States v. Rim Jong Hyok"
case_number: "2:24-cr-20061-HLT-ADM"
jurisdiction: "U.S. District Court, District of Kansas (Kansas City Docket)"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: indicted
crime_charged:
  - "[[ransomware-ic]]"
  - "[[hacking-ic]]"
  - "[[money-laundering-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
defendants:
  - name: "Rim Jong Hyok (림종혁)"
    nationality: "Democratic People's Republic of Korea (DPRK / North Korea)"
    status: "indicted; fugitive (last known to be in North Korea — DPRK has no extradition relationship with the United States)"
    sentence: ""
    location_at_arrest: "Not arrested — defendant is in DPRK; charges remain allegations until proven."
related_operation: ""
ic_elements:
  mlat_requests: []
  extradition: "No extradition possible — defendant is in the Democratic People's Republic of Korea, with which the United States has no extradition treaty or extradition relationship; case proceeds as fugitive indictment + State Department Rewards for Justice incentive ($10M)."
  evidence_from_abroad:
    - "[[south-korea]]"
    - "[[united-kingdom]]"
  foreign_arrests: []
  asset_freezing:
    - "[[united-states]]"
cooperating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-treasury]]"
  - "[[knpa]]"
  - "[[national-intelligence-service-korea]]"
legal_frameworks_invoked:
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[extraterritorial-jurisdiction]]"
  - "[[extradition-practice]]"
precedent_value: "Landmark US public-record indictment of an explicitly state-sponsored RGB / Andariel ransomware operator. The case demonstrates the US public-record posture of (a) charging individual DPRK military-intelligence personnel for ransomware against US healthcare critical infrastructure, (b) tying the ransomware revenue stream directly to follow-on espionage operations against US defense and aerospace targets, and (c) coordinating the criminal-law action with a same-day multilateral joint Cybersecurity Advisory (AA24-207A) co-signed by ROK NIS, ROK NPA, and UK NCSC. It is one of the most legible public-record artifacts of US-Korea-UK cybersecurity cooperation against DPRK state-sponsored ransomware."
source_count: 3
sources:
  - "[[2024-07-25_justice-gov_north-korean-government-hacker-charged-rim-jong-hyok-andariel]]"
created: 2026-05-09
updated: 2026-05-09
last_verified: 2026-05-09
summary: "United States v. Rim Jong Hyok charges a North Korean Reconnaissance General Bureau (RGB) cyber operator — publicly known as Andariel / Onyx Sleet / APT45 / Silent Chollima — for conspiracy to commit ransomware attacks against US hospitals and healthcare providers using RGB-developed Maui ransomware, conspiracy to launder the proceeds, and use of those proceeds to fund follow-on intrusions into US Air Force bases (Randolph, Robins), NASA-OIG, and defense / technology / energy targets across the US, Republic of Korea, Taiwan, and the People's Republic of China. The 17-page indictment was returned 2024-07-24 by a grand jury in the District of Kansas (Kansas City Docket); DOJ announced 2024-07-25. Charges: 18 U.S.C. § 371 (CFAA-based conspiracy) and 18 U.S.C. § 1956(h) (money-laundering conspiracy). Same-day joint Cybersecurity Advisory AA24-207A was co-signed by US (FBI, CISA, NSA, US Cyber Command CNMF, DoD Cyber Crime Center DC3), ROK (NIS, NPA), and UK (NCSC). $114K in cryptocurrency proceeds interdicted; State Department Rewards for Justice posted up to $10M for Rim's location or identification."
---

## Summary

On **2024-07-25**, the U.S. Department of Justice announced the unsealing of a grand-jury indictment charging North Korean national **Rim Jong Hyok** (림종혁), an operator of North Korea's **Reconnaissance General Bureau (RGB)** cyber unit publicly known as **Andariel / Onyx Sleet / APT45 / Silent Chollima**, with conspiracy to commit ransomware attacks against US hospitals and healthcare providers using RGB-developed **Maui** ransomware, and conspiracy to launder the resulting ransom proceeds. The indictment (**Case 2:24-cr-20061-HLT-ADM**) was returned by a grand jury on **2024-07-24** in the **U.S. District Court, District of Kansas (Kansas City Docket)**.

The case is high-IC-density on three axes: (1) victims span the US, the Republic of Korea, Taiwan, and the PRC; (2) the same-day **Joint Cybersecurity Advisory AA24-207A** was co-authored by US agencies together with the **Republic of Korea's National Intelligence Service (NIS / 국가정보원)** and **National Police Agency (NPA / KNPA / 경찰청)** and the **United Kingdom's National Cyber Security Centre (NCSC)**; and (3) the **U.S. Department of State Rewards for Justice** program posted a reward of up to **$10 million** for information leading to Rim's location or identification. Rim is reported by the U.S. government as last known to be in North Korea and has not been arrested.

## Facts

### Methodology (per DOJ press release and indictment)

Rim and his RGB co-conspirators allegedly executed a two-stage scheme. **Stage 1 (revenue generation):** the conspirators used **Maui** ransomware (and Maui-similar variants such as files named `m.exe` and `aui.exe`) to encrypt computer networks of US hospitals and healthcare providers, leaving ransom notes demanding cryptocurrency payment for decryption keys. **Stage 2 (espionage):** ransom proceeds, after laundering through Hong Kong-based facilitators (BTC → Tether → Chinese yuan, withdrawn at an ATM in Dandong, China, immediately adjacent to the **Sino-Korean Friendship Bridge** to Sinuiju, North Korea), were used to lease virtual private servers from US cloud-computing providers, which were in turn used to compromise US defense contractors, two USAF bases (**Randolph AFB**, Texas; **Robins AFB**, Georgia), **NASA-OIG**, a Chinese energy company, a Taiwanese defense contractor, and three South Korean entities. Initial access was typically obtained via known but unpatched vulnerabilities, including **Log4Shell** (CVE-2021-44228).

### Victim roster (per indictment paragraphs 4–20)

| # | Indictment pseudonym | Country / district | Date | Class |
|---|---|---|---|---|
| 4 | Kansas Hospital | District of Kansas (US) | May 2021 | Ransomware |
| 5 | Arkansas Healthcare Company | W.D. Ark. (US) | March 2022 | Ransomware (Maui-similar `m.exe`) |
| 6 | Connecticut Healthcare Company | D. Conn. (US) | March 2022 | Ransomware (Maui-similar `m.exe`) |
| 7 | Florida Hospital | M.D. Fla. (US) | March 2022 | Ransomware |
| 8 | Colorado Medical Clinic | D. Colo. (US) | March 2022 | Ransomware (Maui-similar `aui.exe`) |
| 9 | South Korean Manufacturing Company | Republic of Korea | March 2023 | Ransomware (4.3 BTC paid 2023-04-12) |
| 10 | NASA Office of Inspector General | D.D.C. (US) | February 2022 | Exfiltration (>17 GB unclassified) |
| 11 | "California Defense Company" (satellite designer) | C.D. Cal. (US) | March 2022 | Exfiltration |
| 12 | "Michigan Defense Company" | E.D. Mich. (US) | April 2022 | Exfiltration (7-month dwell) |
| 13 | Randolph Air Force Base | W.D. Tex. (US) | April 2022 | Exfiltration (~1 GB unclassified, Log4Shell) |
| 14 | Robins Air Force Base | M.D. Ga. (US) | April 2022 | Exfiltration (>1 GB across 3 sessions, Log4Shell) |
| 15 | "Oregon Defense Company" | D. Or. (US) | April 2022 | Exfiltration (>3 TB compressed; maritime + uranium-processing technical info) |
| 16 | "Massachusetts Defense Company" (military aircraft) | D. Mass. (US) | November 2022 | Exfiltration (>30 GB) |
| 17 | "Chinese Energy Company" | Shenzhen, PRC | 2022 | R&D exfiltration |
| 18 | "Taiwanese Defense Company" (locations also in South Korea) | Taiwan | 2023 | Exfiltration |
| 19 | "South Korean Defense Company 1" | Republic of Korea | 2023 | Exfiltration |
| 20 | "South Korean Defense Company 2" | Republic of Korea | 2023 | Exfiltration |

In April 2023 the conspirators allegedly moved over **250 GB** of stolen data — including technical and design information on tanks, fighter jets, rockets, and torpedoes from the Taiwanese and South Korean defense contractors — to a virtual private server registered under the domain `makingsitebeauty.com` (registered 2023-03-08).

### RGB malware identified by the indictment

In addition to **Maui**, the indictment names the following RGB-developed malware identified by private-sector researchers as associated with this actor set: **Valefor**, **VSingle**, **ValidAlpha**, **YamaBot**, **DTrack**, **TigerRAT**, **MagicRAT**.

### Charges (per indictment)

| Count | Statute | Allegation |
|---|---|---|
| Count 1 | 18 U.S.C. § 371 | Conspiracy embracing CFAA offenses: (a) intentional damage to a protected computer affecting medical care (§ 1030(a)(5)(A) / (c)(4)(B)(i)); (b) extortion via interstate communications (§ 1030(a)(7)(C) / (c)(3)(A)); (c) unauthorized access to US government computers exceeding $5,000 in value (§ 1030(a)(2)(B), (a)(2)(C), (c)(2)(B)) |
| Count 2 | 18 U.S.C. § 1956(h) | Conspiracy to launder ransomware proceeds in promotion of unauthorized-access offenses |
| Forfeiture | 18 U.S.C. §§ 982(a)(1), 982(a)(2)(B), 1030(i); 21 U.S.C. § 853 | Money-judgment forfeiture; substitute-property forfeiture |

## International Cooperation Elements

### Evidence Gathering / Investigation

| Element | Detail |
|---|---|
| Lead investigative office | FBI Kansas City Field Office (SAC Stephen A. Cyrus) |
| Co-investigating US agencies | FBI; Air Force Office of Special Investigations (AFOSI), incl. National Security Detachment; DoD Cyber Crime Center (DC3); NASA-OIG |
| Treasury / financial action | $114K crypto interdicted by DOJ + FBI; $500K prior FBI seizure |
| Cryptocurrency tracing | BTC → Tether → CNY pathway via Hong Kong facilitators; ATM withdrawals at Dandong (PRC) / Sinuiju (DPRK) Sino-Korean Friendship Bridge — China-side facilitator network exposed but not subject of charges in this indictment |

### Multilateral Joint Advisory (AA24-207A, same day)

| Country | Authoring agency on advisory AA24-207A |
|---|---|
| United States | FBI, CISA, NSA, US Cyber Command's Cyber National Mission Force (CNMF), DoD Cyber Crime Center (DC3) |
| Republic of Korea (South Korea) | National Intelligence Service (NIS / 국가정보원) |
| Republic of Korea (South Korea) | National Police Agency (NPA / KNPA / 경찰청) |
| United Kingdom | National Cyber Security Centre (NCSC) |

### Arrest & Extradition

No arrest. Rim is reported by the US government as last known to be in **North Korea**, with which the United States has no extradition treaty or extradition relationship and from which extradition cooperation is not realistically available. The case proceeds as a **fugitive indictment**. The US Department of State **Rewards for Justice** program posted a reward of up to **$10 million** for information leading to Rim's location or identification.

### Asset Recovery

- **$114,000 in virtual currency** interdicted as proceeds of ransomware attacks and related money-laundering transactions (DOJ + FBI announcement, 2024-07-25).
- **~$500,000 in virtual currency** previously seized by the FBI (referenced in the press release).
- Forfeiture-money judgment is pleaded against Rim.

## Legal Analysis

### Jurisdiction

US federal jurisdiction in the **District of Kansas (Kansas City Docket)**. Venue lies in the District of Kansas because the **Kansas Hospital** ransomware victim (paragraphs 4, 30) is located in that district and was the May 2021 entry point into the conspiracy. The indictment recites that the conspiracy spanned May 2021 through April 2023, "in the District of Kansas and elsewhere."

### Key Legal Issues

- **State-sponsored cyber actor as criminal-law defendant** — the indictment treats Rim as an individual criminal defendant (CFAA + § 1956(h)) notwithstanding his role as an RGB military-intelligence operator and explicit attribution to a state organ. This is consistent with the line of post-2014 DOJ indictments of state-sponsored hackers (e.g., the 2018 PLA charges, the 2020 [[3-north-korean-military-hackers-indicted-in-wide-ranging-scheme-to-commit-cyber-attacks-and-financial-crimes-a|3 NK Military Hackers]] indictment) but extends the model to ransomware against critical-infrastructure healthcare providers.
- **Extraterritorial jurisdiction over CFAA conspiracy** — Count 1 reaches conduct occurring entirely outside the US (RGB offices in Pyongyang and Sinuiju) on the basis of effects in protected computers in the US (see [[extraterritorial-jurisdiction]]).
- **Extradition practicality** — DPRK is a non-extradition jurisdiction in the canonical sense (see [[extradition-practice]]). The case therefore relies on the Rewards for Justice incentive and the deterrent / public-record value of unsealing rather than on a realistic extradition pathway.
- **Healthcare-as-critical-infrastructure framing** — § 1030(c)(4)(B)(i) elevates the conspiracy because the ransomware disrupted "medical examination, diagnosis, treatment, or care of one or more individuals." This is a healthcare-specific aggravating element of CFAA worth noting for IC purposes because it tightens the formal cooperation case the US can make to allies on DPRK ransomware.

### Precedent Value

The case is the **first US public-record indictment of an Andariel / Onyx Sleet / APT45 RGB operator for ransomware against US healthcare critical infrastructure**, and the most legible public-record artifact of US–Korea–UK cybersecurity cooperation against DPRK state-sponsored ransomware. The same-day joint Cybersecurity Advisory AA24-207A (co-signed by US, ROK NIS, ROK NPA, UK NCSC) is a tier-1 multilateral IC artifact and a useful comparison point with prior DPRK-indictment-plus-advisory pairings (e.g., the [[3-north-korean-military-hackers-indicted-in-wide-ranging-scheme-to-commit-cyber-attacks-and-financial-crimes-a|3 NK Military Hackers]] case and Lazarus-related advisories).

## Proceedings Timeline

| Date | Event |
|---|---|
| May 2021 | First charged ransomware attack (Kansas Hospital) |
| February 2022 | NASA-OIG intrusion (>17 GB unclassified data exfiltrated) |
| March 2022 | Maui-style ransomware against Arkansas, Connecticut, Florida, Colorado healthcare victims |
| April 2022 | Log4Shell-driven intrusions into Randolph AFB, Robins AFB; further defense-contractor exfiltration |
| March 2023 | South Korean manufacturing company ransomware victim |
| April 2023 | Conspirators move >250 GB of South Korean / Taiwanese defense data to Virtual Private Server 4 |
| **2024-07-24** | Grand jury (District of Kansas) returns indictment (Case 2:24-cr-20061-HLT-ADM) |
| **2024-07-25** | DOJ announces unsealing; CISA / FBI / NSA / CNMF / DC3 / ROK NIS / ROK NPA / UK NCSC release Joint Cybersecurity Advisory AA24-207A; State Dept Rewards for Justice posts $10M reward; DOJ + FBI announce ~$114K crypto interdiction |

## Cooperation Effectiveness

This case is a strong public-record cooperation marker on three axes:

1. **Multilateral co-attribution.** The same-day joint advisory is the highest-density tier-1 attribution co-signature available in the wiki for an Andariel / Onyx Sleet operator: it pairs the US criminal-law action with a co-signed advisory by **ROK NIS + ROK NPA** on the Korean side and **UK NCSC** on the British side. By comparison, prior US DPRK indictments more often pair with US-only advisories.
2. **Cross-border victim corroboration.** The indictment's victim roster crosses US, ROK, Taiwan, and PRC jurisdictions; the South Korean victim ransomware payment in April 2023 is itself a cooperation-relevant data point because it implies tier-1 evidentiary support from the South Korean victim manufacturing company.
3. **Extradition realism.** The case is a clean illustration of the limits of extradition cooperation when a state-sponsored defendant resides in a non-cooperating jurisdiction (DPRK). The Rewards for Justice $10M posting and crypto interdiction are the practical IC tools available; physical-custody cooperation is not.

The IC effectiveness ceiling here is set by the absence of any extradition pathway from DPRK; the *floor* is durably high because of the multilateral advisory co-authorship, the financial interdiction, and the public-record indictment. This pattern (high-floor, ceiling-bounded) is a recurring shape for DPRK cybercrime IC and is well-documented by this case.

## Korean Relevance (한국 관련성)

This case is **directly Korea-relevant** on multiple dimensions visible in the cited tier-1 source itself:

### South Korea as cooperating authority

The same-day Joint Cybersecurity Advisory **AA24-207A** is co-authored by **two Republic of Korea agencies**:

- **National Intelligence Service (NIS / 국가정보원)** — civilian intelligence agency with statutory cybersecurity coordination role (see [[national-intelligence-service-korea]]).
- **National Police Agency (NPA / KNPA / 경찰청)** — national police service responsible for cybercrime investigation via 수사국 (see [[knpa]]; cybercrime-specific framing under [[knpa-cyber-bureau]]).

This is a tier-1 public-record example of US–ROK cybersecurity cooperation against DPRK state-sponsored ransomware, with the unusual feature of pairing a DOJ criminal-law action with a same-day ROK-co-signed advisory.

### South Korea as victim jurisdiction

The indictment names three Republic-of-Korea-located victims:

- A **South Korean manufacturing company** (paragraph 9, March 2023 ransomware victim, 4.3 BTC ransom paid 2024-04-12 [sic 2023-04-12]).
- **South Korean Defense Company 1** (paragraph 19, 2023 exfiltration victim).
- **South Korean Defense Company 2** (paragraph 20, 2023 exfiltration victim).

In April 2023, conspirators moved over 250 GB of stolen technical / design data to Virtual Private Server 4, including data exfiltrated from the Taiwanese Defense Company and the two South Korean Defense Companies, covering tanks, fighter jets, rockets, and torpedoes (paragraph 52). This is a concrete public-record artifact of DPRK Andariel targeting South Korean defense industrial base, distinct from the typical Korea-as-cooperator framing.

### DPRK / RGB context

The indictment's introduction states that the RGB's recent cyber operations have included "cyber attacks on U.S. and South Korea critical infrastructure" — explicitly framing South Korean critical infrastructure as a co-victim category. The U.S. Treasury's 2019 Andariel sanctions designation (referenced in the indictment, paragraph 2) cites Andariel's cybercrime "to generate revenue and target South Korea's government and infrastructure in order to collect information and to create disorder."

### Korean-language verification

- Defendant name in Korean (per indictment cover page): **림종혁** (North Korean spelling; the South Korean spelling would conventionally render as 임종혁).
- The Sino-Korean Friendship Bridge laundering pathway connects **단둥 (Dandong, China)** with **신의주 (Sinuiju, North Korea)**.

## Contradictions & Open Questions

- **Specific Korean victim entities not named.** The indictment uses pseudonyms ("South Korean Manufacturing Company"; "South Korean Defense Company 1"; "South Korean Defense Company 2"); precise corporate identification of these victims is not in the press release or indictment.
- **South Korea–side prosecutorial action not described.** The press release and indictment do not describe whether the Republic of Korea has opened a parallel domestic investigation against the same actor set, or whether South Korean evidence has been transmitted via formal MLA channels rather than via informal joint-advisory cooperation.
- **UK side substantive content.** The UK is co-author on AA24-207A via NCSC, but no UK-side prosecutorial action is named in the cited tier-1 source. Whether NCSC's role was technical IOC sharing, victim notification on UK-side or further substantive cooperation is not described.
- **Co-conspirator status.** The indictment uses pseudonyms "Conspirator 1" and "Conspirator 2"; their identification, location, and any potential separate prosecution is not described. Two **Hong Kong residents** are described as facilitators but are not charged.
- **Reward outcome.** No public update is reflected in this source on the disposition of the $10M Rewards for Justice reward.
- **DOJ press release URL availability.** The original DOJ URL returned a 404 at ingest time (2026-05-09); body text was reconstructed from a contemporaneous mirror cross-validated against the DOJ-hosted indictment PDF and the CISA-hosted advisory. Wayback Machine had no snapshot of the exact slug at the time of ingest. This is a verification-channel observation, not a contradiction in the underlying facts.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2024-07-25_justice-gov_north-korean-government-hacker-charged-rim-jong-hyok-andariel\|North Korean Government Hacker Charged for Involvement in Ransomware Attacks Targeting U.S. Hospitals and Health Care Providers]] | US DOJ (OPA) | 2024-07-25 | https://www.justice.gov/opa/pr/north-korean-government-hacker-charged-involvement-ransomware-attacks-targeting-us |
| [2] | Indictment (Case 2:24-cr-20061-HLT-ADM) | US District Court, District of Kansas | 2024-07-24 | https://www.justice.gov/d9/2024-07/hyok_filed_indictment.pdf |
| [3] | Joint Cybersecurity Advisory AA24-207A — North Korea Cyber Group Conducts Global Espionage Campaign to Advance Regime's Military and Nuclear Programs | CISA / FBI / NSA / CNMF / DC3 / ROK NIS / ROK NPA / UK NCSC | 2024-07-25 | https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a |
