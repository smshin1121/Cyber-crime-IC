---
type: operation
title: "Indonesia INP-FBI MFA-Bypass Phishing Syndicate Takedown (2026)"
title_ko: "INP-FBI MFA 우회 피싱 신디케이트 검거 (2026)"
aliases:
  - "INP FBI Jakarta phishing arrest 2026"
  - "GWL FYT Jakarta MFA-bypass phishing"
  - "Indonesia $20 million phishing syndicate 2026"
case_id: CYB-2026-064
period: 3
operation_role: standalone
parent_operation: ""
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
outcome: partial
timeframe:
  announced: 2026-04-23
  start: 2018
  end: 2026-04-22
  ongoing: false
crime_type: "[[bec-ic|Business Email Compromise]]"
crime_types:
  - "[[bec-ic|Business Email Compromise]]"
  - "[[online-fraud-ic|Online Fraud]]"
  - "[[cybercrime-infrastructure-ic|Cybercrime Infrastructure]]"
  - "[[malware-ic|Malware]]"
target_entity: "Indonesian phishing-as-a-service couple (GWL, developer; FYT, crypto-laundering) selling MFA-bypass scripts to BEC actors"
lead_agency: "[[indonesia-police|Indonesian National Police (INP) - Bareskrim]]"
coordinating_body: "[[indonesia-police|Indonesian National Police (INP) - Bareskrim]]"
participating_countries:
  - "[[indonesia]]"
  - "[[united-states]]"
jurisdictions:
  - "[[indonesia]]"
  - "[[united-states]]"
participating_agencies:
  - "[[indonesia-police|Indonesian National Police (INP) - Bareskrim]]"
  - "[[fbi|U.S. Federal Bureau of Investigation (FBI)]]"
organizations:
  - "[[indonesia-police|Indonesian National Police (INP) - Bareskrim]]"
  - "[[fbi|U.S. Federal Bureau of Investigation (FBI)]]"
mechanisms_used:
  - "[[informal-cooperation|Informal Police Cooperation]]"
legal_basis:
  - "Indonesia: Electronic Information and Transactions Law (Undang-Undang ITE) — maximum 15 years"
results:
  arrests: 2
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Couple GWL (developer) and FYT (cryptocurrency-proceeds manager) detained in Jakarta, Indonesia on 2026-04-22."
    - "17,000 user accounts compromised globally; 34,000 victims globally per the INP release."
    - "Nine Indonesian corporate entities named (without identification) as victims."
    - "United States victims named in source but not enumerated."
    - "Estimated total losses: USD 20 million."
    - "Phishing-script development active since 2018, indicating ~8-year operational lifespan prior to disruption."
credibility_index: 3.4
source_tier: 1
missing_fields:
  - "FBI field office / specific unit not identified in source"
  - "Suspect full names withheld (initials GWL/FYT only) per Indonesian pre-trial reporting practice"
  - "Specific MFA-bypass technique (session-token theft vs. real-time relay) not detailed"
  - "Identification of the cryptocurrency exchanges or mixers used by FYT not provided"
  - "Whether US prosecution will follow Indonesian one not stated"
  - "No identification of the specific Indonesian or U.S. corporate victims"
related_cases:
  []
related_operations:
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[oag-fedpol-real-time-phishing-uk-conviction-2025]]"
  - "[[veriftools-fake-id-marketplace-followup-arrests-2026]]"
  - "[[polri-lcs-cambodia-abbishopee-red-notice-arrest-2026]]"
sister_operation: "[[w3ll-phishing-kit-takedown-2026]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional conflicts]] — Indonesia is not a party to the Budapest Convention as of 2026-05, so cooperation operates outside the Article 35 24/7 Network and any other Budapest tooling."
  - "MFA-bypass capability defeats victim-side credential rotation, increasing pre-disruption dwell time."
  - "Cryptocurrency proceeds management (FYT role) raises the bar on asset recovery; no asset-seizure number reported."
lessons_learned:
  - "Direct INP–FBI bilateral channels can produce arrest-stage outcomes against a non-Budapest-Convention partner; treaty membership is not a precondition for joint investigation."
  - "Long-running PhaaS infrastructure (here ~8 years from 2018 to 2026) is detectable through victim-side intelligence aggregation in the requesting state (US/FBI) when the developer is in a non-extradition-friendly jurisdiction; prosecution-in-place by the host state is a viable alternative to extradition."
  - "Two-suspect division of labour (developer + crypto-launderer) is consistent with mature PhaaS operations and supports separate evidentiary tracks (technical artefacts vs. financial flows)."
source_count: 2
sources:
  - "[[2026-04-23_inp-polri_inp-fbi-global-phishing-mfa-bypass-syndicate]]"
  - "[[2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll]]"
summary: "On 22 April 2026, the Indonesian National Police (INP) Criminal Investigation Agency (Bareskrim) arrested an Indonesian couple - identified by initials GWL and FYT - in Jakarta, Indonesia, in a joint cross-border investigation with the U.S. Federal Bureau of Investigation (FBI). GWL is alleged to have developed and sold malicious phishing scripts since 2018 that bypassed Multi-Factor Authentication (MFA), enabling Business Email Compromise (BEC) at scale; FYT is alleged to have managed proceeds through cryptocurrency wallets. The syndicate's tools reportedly compromised 17,000 accounts and victimised 34,000 people globally - including United States victims and nine Indonesian corporate entities - with estimated losses of USD 20 million. Both suspects face up to 15 years' imprisonment under Indonesia's Electronic Information and Transactions (ITE) Law. INP was the announcing party (23 April 2026); the FBI's role and channel were not described in detail. A second tier-1 own-domain source — the FBI Atlanta Field Office press release of 10 April 2026 — identifies the kit as **W3LL** with its supporting **W3LLSTORE** marketplace, names the US-side prosecutor (USAO Northern District of Georgia), and characterises the case as the **first coordinated US-Indonesia action against a phishing kit developer**."
created: 2026-05-09
updated: 2026-05-17
---
# Indonesia INP-FBI MFA-Bypass Phishing Syndicate Takedown (2026)

> [!info] Provisional record
> This page rests on **two tier-1 own-domain primary sources** as of iter 179 (2026-05-17):
> 1. INP English-language newsroom (`inp.polri.go.id`) dated 23 April 2026 — the Indonesian announcement, focused on the on-site arrest, suspect initials (GWL/FYT), and ITE Law charging context.
> 2. FBI Atlanta Field Office press release (`fbi.gov/contact-us/field-offices/atlanta/news/...`) dated 10 April 2026 — the US announcement, which identifies the kit by name (**W3LL**), the supporting marketplace (**W3LLSTORE**), the US prosecuting office (**USAO Northern District of Georgia**), and the FBI Atlanta Special Agent in Charge **Marlo Graham**. The FBI page identifies the suspect by initials **G.L.** (consistent with INP's "GWL").
>
> It remains below the preferred 5-source threshold and is filed as a provisional joint-investigation record. It will be promoted when (a) Antara/Kompas/Detik Indonesian-language coverage is ingested with corroborating detail, (b) DOJ Main / USAO-NDGA publishes a charging document or further US press release, or (c) Indonesian charging documents are released.
>
> **Note on sister operation page.** The related page [[w3ll-phishing-kit-takedown-2026]] (case_id CYB-2026-088) was created from the FBI Atlanta release and treats the same underlying takedown from the US-side framing. The present page (CYB-2026-064) treats the same takedown from the INP-side framing. The two are sister-record entries pending consolidation in a future curation pass; both now share the FBI Atlanta source for cross-reference integrity.

## Summary

On **Wednesday, 22 April 2026**, the **Indonesian National Police** (Kepolisian Negara Republik Indonesia, "Polri") through its **Criminal Investigation Agency** (*Badan Reserse Kriminal*, "Bareskrim") arrested an Indonesian couple in Jakarta in a cross-border joint investigation with the **U.S. Federal Bureau of Investigation (FBI)**. The couple is identified by initials **GWL** (the technical developer) and **FYT** (the cryptocurrency-proceeds manager). The arrest was announced on **23 April 2026** through the INP's English-language newsroom.

The syndicate's product was a **phishing-as-a-service** capability whose distinguishing feature was the ability to bypass **Multi-Factor Authentication (MFA)**. Per the INP release, GWL had been developing and selling these "malicious scripts" since **2018**, giving the operation an approximately **8-year operational lifespan** before disruption. The scripts compromised **17,000 accounts** and victimised **34,000 people globally**, including United States victims and **nine Indonesian corporate entities**. Total losses are estimated at **USD 20 million**.

This case qualifies for the IC corpus because it is conducted as a direct **Indonesia–United States** joint investigation, with INP as lead agency and FBI as the named foreign cooperating agency, and because Indonesia is **not** a party to the Budapest Convention as of 2026-05-09, illustrating that bilateral cybercrime cooperation can occur outside Council of Europe instruments.

## Background

Phishing-as-a-service (PhaaS) — where a small number of skilled developers package phishing infrastructure (kits, hosting, evasion tooling, mule networks) for sale to a wider population of less-skilled fraudsters — has been a recurring pattern in international cybercrime cooperation, with prior examples including the Swiss real-time-phishing case ([[oag-fedpol-real-time-phishing-uk-conviction-2025]]) and the W3LL phishing-kit takedown ([[w3ll-phishing-kit-takedown-2026]]).

The distinguishing technical claim in the present operation is that the seller's scripts **bypass MFA**. The INP release does not specify whether this was achieved through real-time SMS interception, session-token replay, adversary-in-the-middle (AiTM) proxying, or other means, but the operational consequence — the ability to defeat MFA at scale — is consistent with the senior-tier PhaaS profile documented in the [[w3ll-phishing-kit-takedown-2026|W3LL]] record.

## Participating Parties

| Role | Party |
|---|---|
| **Lead investigating agency (Indonesia)** | [[indonesia-police\|Indonesian National Police (INP) - Bareskrim]] |
| **Indonesian senior official cited** | Inspector General Nunung Syaifuddin, Deputy Chief of Bareskrim (Criminal Investigation Agency) |
| **Foreign cooperating agency (US)** | [[fbi\|U.S. Federal Bureau of Investigation]] — specifically the **FBI Atlanta Field Office** per the FBI Atlanta press release of 10 April 2026 |
| **US senior official cited** | **Special Agent in Charge Marlo Graham** (FBI Atlanta Field Office) |
| **US prosecuting office** | **U.S. Attorney's Office for the Northern District of Georgia (USAO-NDGA)** — provided "assistance" to FBI Atlanta in identifying and seizing US-side phishing-service infrastructure (per the FBI Atlanta release) |
| **Indonesian communicating arm** | INP Public Relations Division (Divisi Humas Polri) |

Both tier-1 own-domain sources describe the cooperation as a joint investigative effort. The FBI Atlanta release goes further by characterising the case as the **"first coordinated action against a phishing kit developer between the United States and Indonesia"**, indicating that the cooperation channel was a direct bilateral track between FBI Atlanta and INP Bareskrim, with USAO-NDGA handling the US-side prosecutorial vehicle for infrastructure seizures. The specific procedural channel (FBI Legat Jakarta, INTERPOL NCB, bilateral MLAR, or informal liaison) is still not named in either release.

## Legal Framework

**Indonesia (charging state):**

- **Electronic Information and Transactions Law** (*Undang-Undang Informasi dan Transaksi Elektronik*, "UU ITE") — Indonesia's primary cybercrime statute, originally enacted in 2008 and amended in 2016 and 2024. The release identifies "up to 15 years in prison" as the maximum charge, consistent with the aggravated provisions for unauthorized access combined with financial gain or harm.

**United States:**

- No US charging instrument is identified in the INP release. The FBI's role is described only as a co-investigator. A separate US indictment, if any, has not yet been observed.

**Treaty / cooperation framework:**

- Indonesia is **not a party to the [[budapest-convention|Budapest Convention on Cybercrime]]** as of 2026-05-09 (no signature, no accession). The Article 35 24/7 Network is therefore not the channel of record.
- No specific bilateral MLAT, MOU, or other instrument is named in the release. The cooperation appears to have run on **informal police-to-police** lines, consistent with how FBI Legat and INP Bareskrim typically interact in non-Budapest-Party jurisdictions in Southeast Asia.

> [!warning] Legal status check needed
> The exact ITE Law article(s) charged are not specified in the release. Indonesian press coverage (Antara) and any subsequent charging document should be ingested to identify the specific provisions invoked.

## Operational Timeline

| Date | Event |
|---|---|
| ~2018 | Suspect GWL begins developing phishing tools (per INP attribution) |
| 2018-2026 | Approximately 17,000 accounts compromised, 34,000 victims accumulated globally; USD 20 million in cumulative losses |
| (date unknown) | INP–FBI joint investigation initiated |
| **2026-04-22 (Wed)** | INP Bareskrim arrests GWL and FYT in Jakarta |
| **2026-04-23** | INP English-language newsroom (`inp.polri.go.id`) publishes the announcement at 02:30:00 (per pubdate metadata) |

The release does not state when the joint INP–FBI investigation formally began, when arrest warrants were issued by Indonesian courts, or when the suspects' charging will be formalised by Indonesian prosecutors.

## Results and Impact

| Metric | Value | Source |
|---|---|---|
| Arrests (Indonesia) | 2 (GWL/G.L. + FYT) | INP release; FBI Atlanta names developer as "G.L." |
| Compromised accounts targeted (2023–2024) | 17,000+ | INP + FBI Atlanta release |
| Total victims (global) | 34,000 | INP release |
| Indonesian corporate victims | 9 | INP release |
| US victims | "yes" (count not given) | INP release |
| Losses (USD, attempted fraud) | 20,000,000+ | INP + FBI Atlanta release |
| Phishing kit name | **W3LL** | FBI Atlanta release |
| Supporting marketplace | **W3LLSTORE** | FBI Atlanta release |
| Kit price | ≈ USD 500 per access | FBI Atlanta release |
| W3LLSTORE compromised-account sales (2019–2023) | 25,000+ | FBI Atlanta release |
| Servers seized | not enumerated | (n/a) |
| Cryptocurrency seized | not stated | (n/a) |
| Domains seized | "**key domains**" seized in coordination with INP | FBI Atlanta release |
| US-side infrastructure seizure | identified and seized by FBI Atlanta + USAO-NDGA | FBI Atlanta release |

The INP release does not enumerate any infrastructure seizure. The FBI Atlanta release adds that **FBI Atlanta, with assistance from USAO-NDGA, identified and seized infrastructure facilitating the phishing service** and that **key domains tied to the operation were seized**, addressing the asset-recovery gap noted earlier from the INP-only record.

The outcome is logged as **partial**: arrests are confirmed, but no seizure of infrastructure or proceeds is reported, and downstream prosecution and conviction outcomes are pending.

## Cooperation Mechanisms Used

The operation ran on **direct bilateral police-to-police cooperation** between **INP Bareskrim** (Indonesia) and **FBI Atlanta Field Office** (US), with **USAO-NDGA** handling the US-side prosecutorial vehicle for infrastructure seizures. Neither release names a specific mechanism such as the [[24-7-network|Article 35 24/7 Network]] (inapplicable since Indonesia is not a Budapest Party), the [[interpol-i24-7|INTERPOL I-24/7]] system, the FBI Legat channel, or a [[joint-investigation-team|Joint Investigation Team]] in the European sense.

In the absence of a named mechanism, the cooperation is best classified as **[[informal-cooperation|Informal Police Cooperation]]** with a long-standing bilateral character. The FBI Atlanta release elevates the precedent value by explicitly framing the case as the **"first coordinated action against a phishing kit developer between the United States and Indonesia"** — implying that prior US-Indonesia cybercrime cooperation existed at the level of victim notification and intelligence sharing but had not produced an operational action against an upstream tool developer until this case.

## Challenges and Friction Points

1. **Non-Budapest-Convention partner.** Indonesia is not a party to the Budapest Convention as of 2026-05; cooperation cannot rely on Article 35 24/7 contact, on harmonized substantive offences, or on the Second Additional Protocol's direct-disclosure mechanisms. This makes preservation of volatile electronic evidence (logs, cryptocurrency wallet attribution) procedurally heavier.
2. **MFA-bypass capability.** Defeats the principal mitigation that institutional victims (the nine Indonesian corporates and the unnamed US victims) had likely deployed, increasing the pre-disruption dwell time and the loss aggregate.
3. **Cryptocurrency-proceeds laundering.** Suspect FYT's role — managing proceeds via crypto wallets — raises the bar on asset recovery. The release does not report cryptocurrency seizure, suggesting either that tracing is incomplete, that seizure orders are pending, or that funds have been moved beyond reach.
4. **Pre-trial reporting opacity.** Suspects identified only by initials (GWL, FYT) per Indonesian pre-trial practice; until charging documents are filed, identity attribution and prior-conduct evidence are not externally verifiable.

## Lessons Learned

- **Bilateral channels can substitute for treaty channels.** A direct INP–FBI investigation produced an arrest-stage outcome despite Indonesia's non-membership in the Budapest Convention, demonstrating that treaty membership is not a precondition for cybercrime joint investigation.
- **Prosecution-in-place is viable for non-extradition jurisdictions.** Where the developer is in a country whose extradition treaty with the US is limited, prosecution by the host state under domestic cyber-statute (here, the ITE Law's 15-year maximum) is a substantive alternative to extradition.
- **PhaaS division of labour is consistent across operations.** The two-suspect structure (developer + crypto-launderer) recurs across [[w3ll-phishing-kit-takedown-2026|W3LL]] and [[oag-fedpol-real-time-phishing-uk-conviction-2025|OAG/fedpol Swiss-UK]] — a signature pattern that may inform future targeting.

## Follow-Up Actions

- Ingest Indonesian-language Antara, Kompas, and/or Detik coverage to confirm the specific ITE Law article(s) charged.
- Watch for any USAO-NDGA charging document, DOJ Main press release, or parallel US indictment relating to the same syndicate.
- Consolidate with the sister page [[w3ll-phishing-kit-takedown-2026]] in a future curation pass (both describe the same underlying takedown from opposite-side framings: INP-side arrest record vs. FBI Atlanta-side infrastructure-seizure record).
- Re-evaluate this page for promotion to non-provisional status when ≥3 additional independent sources beyond the two current tier-1 own-domain releases are available.

## Korean Involvement (한국의 참여)

No Korean involvement is reported in the source. There is no indication that the Korean National Police Agency, the Supreme Prosecutors' Office, or any Korean financial institution was identified as a victim or cooperating agency.

The case is, however, of regional interest because it concerns a **Southeast-Asian-hosted PhaaS operator targeting global victims**, a profile structurally similar to the Cambodia/Philippines voice-phishing dynamics that drive Korean-led operations such as [[korea-cambodia-philippines-73-extradition-2026]] and [[seoul-eastern-clark-philippines-voice-phishing-arrest-extradition-2026]]. Korean financial institutions and email systems are plausible secondary victims of an MFA-bypass PhaaS toolkit even when not named in the announcing release.

## Contradictions & Open Questions

- **Total-victims arithmetic.** The INP release reports both "17,000 accounts" and "34,000 victims globally" — a ~2:1 ratio. The FBI Atlanta release independently confirms "17,000 victims worldwide" for the 2023–2024 window, and separately reports "25,000 compromised accounts sold" via W3LLSTORE during 2019–2023, suggesting that the 34,000 figure in the INP release may aggregate across the full operational lifespan (2018–2026) rather than the 2023–2024 sub-window.
- **FBI role characterisation.** The FBI Atlanta release positions FBI Atlanta as the investigating lead on the US side (with FBI Atlanta SAC Marlo Graham as quoted senior official), with USAO-NDGA as the prosecutorial partner. The INP release described the FBI as a co-uncoverer. Net: both sources are mutually consistent — joint investigation, both sides active — but neither identifies who held initial source intelligence.
- **Asset recovery — partial resolution.** The FBI Atlanta release confirms **US-side infrastructure seizure** and **key domain seizures**, addressing one gap from the INP-only record. **Cryptocurrency / fiat seizure** is still not reported despite FYT's named role; this gap persists.
- **Prosecution forum.** Both releases indicate Indonesian prosecution under the ITE Law. No US indictment is identified in either tier-1 source. Whether USAO-NDGA will pursue a parallel indictment remains unanswered.
- **Suspect-naming convention divergence.** The INP release uses initials **GWL** and **FYT** (per Indonesian pre-trial reporting practice). The FBI Atlanta release uses **"G.L."** for the developer (a US redaction style with periods between letters). The two are consistent in referring to the same developer; FYT is not separately named in the FBI Atlanta release, which focuses on the developer alone.

> [!note] Translation note
> The INP English-language release uses "INP" (Indonesian National Police) consistently, while Indonesian-language sources will use "Polri" (Polisi Republik Indonesia). Both refer to the same agency. "Bareskrim" is the standard short form for *Badan Reserse Kriminal*, the Criminal Investigation Agency.
