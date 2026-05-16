---
type: operation
title: "France–Georgia–INTERPOL Belarusian Ransomware Hacker Sentencing (Yauhen Horbach / 'JohnSmith' / 'Daniel', 2020–2025)"
title_ko: "프랑스–조지아–인터폴 벨라루스 랜섬웨어 해커 검거·인도·실형 (Yauhen Horbach, 2020–2025)"
aliases:
  - "Belarusian ransomware hacker Paris sentencing 2025"
  - "Yauhen Horbach ransomware case"
  - "JohnSmith ransomware Rennes investigation"
  - "Gendarmerie SR Rennes first-in-France ransomware incarceration"
  - "Coriolis Composites Morbihan ransomware investigation 2020"
case_id: CYB-2025-995
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - extradition
  - prosecution
  - sentencing
outcome: success
timeframe:
  announced: 2025-05-14
  start: 2020-02
  end: 2025-04-28
  ongoing: false
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[extortion-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Yauhen Horbach, Belarusian national in his thirties, operating under the pseudonym 'JohnSmith' and nicknamed 'Daniel' by French investigators (after Daniel Craig). Responsible for approximately 2,300 cryptolocker-class ransomware attacks worldwide, of which 65 in France (one in Morbihan), targeting primarily enterprises; bitcoin ransom proceeds approximately USD 750,000 (~EUR 661,000)."
lead_agency: "[[france-gendarmerie]]"
coordinating_body: ""
participating_countries:
  - "[[france]]"
  - "[[georgia]]"
participating_agencies:
  - "[[france-gendarmerie]]"
  - "[[france-junalco]]"
  - "[[interpol]]"
legal_basis:
  - "INTERPOL Red Notice (notice rouge) — issued at the request of French authorities, enabled the foreign arrest of Yauhen Horbach in Georgia in August 2022."
  - "Georgia-to-France extradition (procédure d'extradition) — Horbach extradited from Georgia to France approximately 8 months after his August 2022 arrest (i.e. around April 2023)."
  - "French Code pénal provisions on ransomware-related offences (extorsion en bande organisée, accès et maintien frauduleux dans un système de traitement automatisé de données, atteinte à un STAD, blanchiment) — Paris tribunal judiciaire sentencing on 28 April 2025 of 5 years (4 firm, 1 suspended) and EUR 100,000 fine."
  - "JUNALCO (Juridiction nationale de lutte contre la criminalité organisée) — exercised judicial supervision (information judiciaire) of the French proceedings between extradition and sentencing."
mechanisms_used:
  - "[[interpol-i24-7]]"
  - "[[extradition]]"
  - "[[informal-cooperation]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Yauhen Horbach (Belarusian national) sentenced to 5 years' imprisonment (4 firm, 1 suspended) and EUR 100,000 fine by the tribunal judiciaire de Paris on 28 April 2025."
    - "Approximately 2,300 victim cyberattacks worldwide attributed to the defendant, including 65 in France."
    - "Approximately USD 750,000 (~EUR 661,000) in bitcoin ransom proceeds documented in the suspects' own structured 'tableau de bord' (victim-and-ransom dashboard) recovered by investigators."
    - "Position-of-first-in-France: the Gendarmerie SR Rennes Antenne C3N is described in the primary source as the first French unit to have secured incarceration of a ransomware author at the conclusion of a French-led investigation (a national-precedent milestone)."
credibility_index: 3.6
source_tier: 1
missing_fields:
  - "Specific ransomware-family designator (the press release uses only the generic 'cryptolocker' lower-case class label and does not name a brand such as LockBit, Ryuk, REvil, Phobos, etc.)."
  - "Specific Georgian agency that effected the arrest (e.g., Sakartvelos Shinagan Sakmeta Saministro / MIA, State Security Service of Georgia, or other) — the source refers only generically to authorities of 'la Géorgie'."
  - "Specific Paris-court chamber and case docket number for the 28 April 2025 sentencing."
  - "Whether any bitcoin ransom proceeds were recovered/seized/returned, and any cryptocurrency exchange-side cooperation."
  - "Identity and roles of the 'plusieurs personnes' described as complicit with the suspect."
  - "Whether any of the 2,300 worldwide victim attacks resulted in parallel foreign prosecutions in third countries."
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "INTERPOL Red Notice + Georgia-as-arrest-venue is a working pipeline for medium-tempo French ransomware cases: French Gendarmerie cyber-investigators identify the suspect through patient digital forensics and cryptocurrency-flow analysis, INTERPOL issues a Red Notice, and a third country (here, Georgia) physically arrests and extradites — even when the Belarusian state of nationality offers no cooperation."
  - "Long-tail digital forensics works on ransomware author attribution: the four-year Gendarmerie investigation succeeded by chaining one operational error (a forgotten/old email address) with cryptocurrency financial-flow analysis and an intercepted passport photo, demonstrating that ransomware operator anonymity is fragile over multi-year horizons."
  - "Belarusian state non-cooperation is structurally absorbed by the third-country-arrest route: because Belarus did not cooperate, the case was made workable only by Horbach physically transiting through (or being arrested in) Georgia — a route that depended on a Georgian extradition arrangement and on INTERPOL's Red Notice infrastructure."
  - "The Gendarmerie's framing of the case as 'une enquête 100 % française' is a French-side investigative-pride framing that obscures the indispensable role of Georgian LE arrest action and the INTERPOL Red Notice. From an IC perspective the case is in fact a France + Georgia + INTERPOL three-party pipeline, with Belarus excluded by non-cooperation."
source_count: 1
sources:
  - "[[2025-05-14_gendarmerie-fr_belarusian-ransomware-hacker-yauhen-horbach-paris-sentencing]]"
created: 2026-05-16
updated: 2026-05-16
summary: "Four-year French Gendarmerie cyber-investigation (February 2020 – April 2025) led by the Antenne C3N of the Section de recherches (S.R.) de Rennes, culminating in the 28 April 2025 sentencing by the tribunal judiciaire de Paris of Belarusian national Yauhen Horbach (a/k/a 'JohnSmith', 'Daniel') to 5 years imprisonment (4 firm, 1 suspended) and EUR 100,000 fine for approximately 2,300 cryptolocker-class ransomware attacks worldwide (65 in France) and approximately USD 750,000 in bitcoin ransom proceeds. The investigation was triggered by an attempted breach on Coriolis Composites (Morbihan, France) in February 2020, then progressed through patient digital forensics (IP traceback, server identification, intercepted email address, cryptocurrency-flow analysis, intercepted passport photo). After an INTERPOL Red Notice was issued, Horbach was arrested and incarcerated by Georgian authorities in August 2022, then extradited to France approximately 8 months later. JUNALCO supervised the judicial investigation through to sentencing. The Gendarmerie SR Rennes Antenne C3N is described in the primary source as the first French unit to have secured a ransomware author's incarceration at the conclusion of a French-led investigation."
jurisdictions:
  - "[[france]]"
  - "[[georgia]]"
organizations:
  - "[[france-gendarmerie]]"
  - "[[france-junalco]]"
  - "[[interpol]]"
---

## Summary

On **28 April 2025**, the **tribunal judiciaire de Paris** sentenced **Yauhen Horbach**, a Belarusian national in his thirties — operating online under the pseudonym **"JohnSmith"** and nicknamed **"Daniel"** by French investigators (in reference to a perceived resemblance with the British actor Daniel Craig) — to **5 years' imprisonment** (4 firm + 1 suspended) and a **EUR 100,000 fine** for his role in approximately **2,300 ransomware attacks worldwide**, of which 65 in France (including one in the Morbihan département). Bitcoin ransom proceeds were estimated at approximately **USD 750,000 (~EUR 661,000)**.

The sentencing concluded a **four-year French Gendarmerie cyber-investigation** (February 2020 – April 2025) led by the **Antenne C3N** of the **Section de recherches (S.R.) de Rennes** (Ille-et-Vilaine). The investigation was triggered when **Coriolis Composites** — a Morbihan-based company specialising in aeronautics-robotics design — was targeted by an attempted ransomware breach in February 2020, blocked the maliciel installation, preserved digital traces, and reported the incident to the Gendarmerie.

Working through patient digital forensics — IP-address traceback from Coriolis Composites, identification of the cybercriminal's server, discovery of a forgotten/old email address linking to Yauhen Horbach, cryptocurrency financial-flow analysis revealing suspicious bitcoin movements, and the interception of a passport photo (allegedly required for certain bitcoin operations) — the cybergendarmes built attribution. After **INTERPOL** issued a **Red Notice (notice rouge)**, Horbach was **arrested and incarcerated by Georgian authorities in August 2022**, then **extradited to France approximately eight months later**, and placed in pre-trial detention while judicial investigation continued under **JUNALCO** (Juridiction nationale de lutte contre la criminalité organisée) authority.

The Gendarmerie press release positions the Antenne C3N of the S.R. Rennes as the **first French unit** to have secured the incarceration of a ransomware author at the conclusion of a French-led investigation — a national-precedent milestone for the Gendarmerie's cyber-investigative capacity.

## Background

In **February 2020**, **Coriolis Composites** — a Morbihan-based aeronautics-robotics company — detected an attempt to install a **cryptolocker-class maliciel** on its information systems. The company **blocked the installation, preserved the digital trace evidence, and notified the Gendarmerie**. This evidence-preservation-and-report pattern by the victim allowed the investigators of the **Antenne C3N** of the **Section de recherches (S.R.) de Rennes** to begin a four-year inquiry.

The suspect operated under the pseudonym **"JohnSmith"** and maintained a structured **"tableau de bord"** (dashboard) listing victims, ransom amounts demanded, and case progress — recovered by investigators after they gained server-side access through the initial IP-address traceback. The financial side of the operation ran in bitcoin.

## Participating Parties

| Role | Entity | Notes |
|---|---|---|
| **Lead investigative agency** | [[france-gendarmerie]] — Section de recherches (S.R.) de Rennes, Antenne du Centre de lutte contre les criminalités numériques (C3N) | Conducted the four-year investigation; lieutenant Armel is identified on the record as head of the antenne. |
| **Lead prosecution authority** | [[france-junalco]] (Juridiction nationale de lutte contre la criminalité organisée) | Supervised the information judiciaire from extradition through sentencing. |
| **Sentencing court** | Tribunal judiciaire de Paris | 28 April 2025 sentencing: 5 years (4 firm + 1 suspended) + EUR 100,000 fine. |
| **Foreign arrest authority** | Authorities of **[[georgia]]** | Arrested and incarcerated Yauhen Horbach in August 2022; extradited him to France approximately 8 months later. |
| **International-alerting mechanism** | [[interpol]] | Issued the Red Notice (notice rouge) that triggered the Georgian arrest. |

> [!note] Belarus
> Belarus is **not** listed as a participating country: Belarus is the suspect's state of nationality only, and is not credited with any cooperative role in the primary source. The pattern is consistent with the broader observation that Belarus has been a structural non-cooperator on cybercrime cases — circumvented in this case by Georgia-as-arrest-venue.

## Legal Framework

- **INTERPOL Red Notice** — international alerting mechanism that enabled the Georgian arrest.
- **Georgia-to-France extradition arrangement** — the specific bilateral instrument is not named in the primary source; the source refers only to Horbach being "extradé vers la France huit mois plus tard."
- **French Code pénal** — predicate offences include extorsion (extortion), accès et maintien frauduleux dans un système de traitement automatisé de données (STAD, unauthorized access), and blanchiment (money laundering). Exact charging instrument and articles are not specified in the press release.
- **JUNALCO competence** — the Juridiction nationale de lutte contre la criminalité organisée is the French jurisdictional centre for organised crime cases above a defined threshold; its handling of the case implicitly classifies the ransomware operation as organised-crime grade.

## Operational Timeline

| Date | Event |
|---|---|
| **Feb 2020** | Attempted ransomware (cryptolocker) breach on Coriolis Composites (Morbihan, France); company blocks installation and reports to Gendarmerie. |
| **2020–2022** | Gendarmerie S.R. Rennes Antenne C3N investigation: server identification via IP-traceback; discovery of suspect's "tableau de bord" listing victims and ransom amounts; chain of investigative breakthroughs including an old email address linked to Yauhen Horbach; cryptocurrency financial-flow analysis; intercepted passport photo. |
| **2022** | INTERPOL Red Notice issued at French request. |
| **Aug 2022** | Yauhen Horbach arrested and incarcerated in Georgia. |
| **~Apr 2023** | Extradited from Georgia to France (8 months after Georgian arrest); placed in pre-trial detention under JUNALCO supervision. |
| **2023–2025** | French judicial investigation (information judiciaire) under JUNALCO authority. |
| **28 Apr 2025** | Tribunal judiciaire de Paris sentences Horbach to 5 years' imprisonment (4 firm + 1 suspended) + EUR 100,000 fine. |
| **14 May 2025** | Gendarmerie nationale publishes Gendinfo press release describing the case. |

## Results and Impact

- **1 conviction** (Yauhen Horbach) with 5-year sentence (4 firm + 1 suspended) and EUR 100,000 fine.
- **Approximately 2,300 ransomware attacks worldwide attributed** (including 65 in France, 1 in Morbihan).
- **Approximately USD 750,000 (~EUR 661,000) in bitcoin ransom proceeds** documented from the suspect's own internal records.
- **Real damage** described by lieutenant Armel as exceeding the ransom figure: "Des entreprises ont en effet fait faillite, des gens ont perdu leur travail" (companies went bankrupt, people lost their jobs).
- **National precedent**: the Antenne C3N of the S.R. Rennes is described as the first French unit to incarcerate a ransomware author at the conclusion of a French-led investigation.

## Cooperation Mechanisms Used

| Mechanism | Role |
|---|---|
| [[interpol-i24-7]] / INTERPOL Red Notice | Triggered the Georgian arrest. |
| [[extradition]] | Georgia-to-France extradition (~April 2023). |
| [[informal-cooperation]] | Day-to-day investigative coordination between France and Georgia in the run-up to the extradition. |

The primary-source phrase **"enquête 100 % française"** ("100% French investigation") is an investigative-pride framing referring to the *digital forensics and attribution phase*. From an international cooperation perspective the case is in fact a **France + Georgia + INTERPOL three-party pipeline**, with Belarus excluded by non-cooperation.

## L24 cooperating-jurisdictions verbatim

The primary-source Gendarmerie release explicitly names **two distinct cooperating LE jurisdictions**:

> *"Après la diffusion par Interpol d'une notice rouge, l'homme est interpellé, puis incarcéré en Géorgie, en août 2022. Il est extradé vers la France huit mois plus tard, et placé en détention provisoire, tandis que l'information judiciaire se poursuit sous l'autorité de la Juridiction nationale de lutte contre la criminalité organisée (JUNALCO)."*

— France (Gendarmerie SR Rennes Antenne C3N + JUNALCO) and Georgia (arresting + extraditing authorities), connected via INTERPOL.

## Challenges and Friction Points

- **Belarusian state non-cooperation**: Belarus offered no cooperative pathway, requiring the case to be made workable only by a third-country arrest in Georgia.
- **Generic ransomware-family attribution**: the source uses only the lower-case generic class label "cryptolocker" and does not identify a specific ransomware brand, limiting cross-comparison with named-family operations (e.g. [[operation-cronos-phase1|Operation Cronos]] / LockBit).
- **No documented bitcoin recovery**: the press release does not report any seizure or recovery of the ~USD 750,000 in bitcoin ransom proceeds, only the documentation of those proceeds from the suspect's tableau de bord.

## Lessons Learned

- **INTERPOL Red Notice + Georgia-as-arrest-venue** is a working pipeline for medium-tempo French ransomware cases where the state of nationality (here, Belarus) is non-cooperative.
- **Operator-error harvesting at multi-year horizon**: the four-year investigation succeeded by chaining a single operational error (a forgotten/old email address) with cryptocurrency financial-flow analysis and an intercepted passport photo — demonstrating that ransomware-operator anonymity is fragile over long horizons even when the suspect uses bitcoin and a generic Anglo pseudonym.
- **Victim evidence-preservation matters**: Coriolis Composites' decision to block the maliciel installation, preserve digital traces, and report to Gendarmerie was the trigger for the entire investigative chain — an instance where the victim's first-hour response shaped the eventual sentencing.
- **JUNALCO as cybercrime-grade prosecution forum**: the case implicitly elevates a ~USD 750K ransomware operation to organised-crime status by routing it through JUNALCO.

## Follow-Up Actions

The primary source does not document any follow-up actions (e.g., subsequent foreign prosecutions in third countries among the 2,300 worldwide victims, additional arrests of the "plusieurs personnes" referenced as complicit, or bitcoin asset-recovery proceedings).

## Korean Involvement (한국의 참여)

The primary source does not mention any Korean involvement. Among the 2,300 worldwide victim attacks, no Korean victim is specifically identified.

## Contradictions & Open Questions

- The Gendarmerie's positioning of the case as **"une enquête 100 % française"** stands in tension with the indispensable Georgian arrest and INTERPOL Red Notice role. The framing reflects a French investigative-pride formulation and does not undermine the multi-jurisdiction reality of the operational pipeline.
- The specific ransomware-family designator (LockBit, Ryuk, REvil, Phobos, etc.) is not named in the source — preventing direct cross-comparison with the wiki's named-family operation pages.
- The specific Georgian agency that effected the arrest is not named.
- The specific bilateral legal instrument relied upon for the Georgia-to-France extradition is not specified.
- Whether any of the ~USD 750,000 in bitcoin ransom proceeds were recovered or returned to victims remains undocumented in the primary source.
