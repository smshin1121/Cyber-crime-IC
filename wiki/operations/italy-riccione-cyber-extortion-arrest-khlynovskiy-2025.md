---
type: operation
title: "Italy Riccione Cyber-Extortion Arrest — Italy-FBI Cooperation (Riccione, 31 July 2025)"
title_ko: "이탈리아 리치오네 사이버 갈취범 체포 — 이탈리아·FBI 공조 (2025년 7월 31일)"
aliases:
  - "Riccione cybercriminal arrest 2025"
  - "Polizia Postale Riccione FBI arrest 2025"
  - "Italian-Australian / Kazakh extortion arrest Riccione 2025"
case_id: CYB-2025-085
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
outcome: success
timeframe:
  announced: 2025-07-31
  start: 2023
  end: 2025-07-31
  ongoing: false
crime_types:
  - "[[extortion-ic]]"
  - "[[ransomware-ic]]"
crime_type: "[[extortion-ic]]"
target_entity: "Foreign national, internationally wanted, accused by U.S. authorities of active involvement in serious cyber-extortion offences committed between 2023 and the first months of 2025 against U.S.-based organisations (strutture statunitensi). Ransom demands attributed to the attacks: millions of U.S. dollars. The Polizia di Stato press release does not name the suspect; Italian regional media report the suspect as 42-year-old Kazakh national Roman Khlynovskiy, with FBI attributing approximately USD 31 million in illicit profit to the underlying scheme."
lead_agency: "[[italy-polizia-postale]]"
coordinating_body: ""
participating_countries:
  - "[[italy]]"
  - "[[united-states]]"
participating_agencies:
  - "[[italy-polizia-postale]]"
  - "[[fbi]]"
legal_basis:
  - "U.S. federal arrest warrant (provvedimento federale) issued by U.S. judicial authority — instrument and issuing court not specified in the Italian primary source"
  - "Bilateral Italy–United States law-enforcement cooperation framework, including the deployment of liaison experts (esperti) at the respective embassies as referenced in the release"
mechanisms_used:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Numerous IT devices seized at the place of arrest (hotel apartment in Riccione)"
    - "Several thousand euros in cash seized"
    - "Suspect remanded to Italian authorities pending extradition proceedings to the United States"
edges:
  - source_actor: italy-polizia-postale
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: fbi
    target_actor: italy-polizia-postale
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "suspect identity (name, nationality, age) — not in Polizia di Stato release; reported by Italian regional media but not asserted as tier-1"
  - "specific U.S. victim organisations — release names only 'strutture statunitensi'"
  - "specific ransom-demand totals — release states 'milioni di dollari' without aggregate USD figure (FBI attribution of ~USD 31 million is media-only)"
  - "prison of remand — Busto Arsizio per media, not in primary source"
  - "issuing U.S. court / district — not named in Italian release"
  - "formal extradition instrument and stage — release describes the arrest only, not the subsequent extradition proceeding"
  - "specific malware family or ransomware brand used in the underlying attacks"
related_cases:
  - "[[us-v-xu-zewei-hafnium-extradited-italy]]"
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Italy–U.S. cyber-extortion cooperation arc executed concretely on Italian soil: a U.S. federal arrest warrant against an internationally wanted suspect was operationalised by the Cnaipic specialist unit of the Italian Polizia Postale, in partnership with the regional Centro operativo per la sicurezza cibernetica Emilia-Romagna and the local Sezione operativa per la Sicurezza cibernetica di Rimini."
  - "Liaison-officer / embassy-expert framework explicitly credited: the press release closes by attributing the result to consolidated institutional cooperation between Italian police and the U.S. law-enforcement community, 'particolarmente rafforzato anche grazie all'istituzione di esperti presso le rispettive ambasciate.' This is a rare named acknowledgement of the bilateral liaison-officer infrastructure as a cooperation mechanism in a public release."
  - "Tourist-flow detection: the suspect was located while on family holiday at a hotel in Riccione. The case illustrates that international wanted-person notices remain operationally effective when subjects travel to mutual-legal-assistance partner jurisdictions, even when their primary residence lies elsewhere."
source_count: 1
sources:
  - "[[2025-07-31_polizia-di-stato_riccione-arresto-cybercriminale-internazionale-khlynovskiy]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional page
> This page is published below the preferred normal-page source threshold (`source_count >= 5`) and is marked provisional. It is anchored on a single Tier-1 primary source from the Italian Polizia di Stato dated 2025-07-31. It will be promoted once additional Tier-1 corroboration (DOJ unsealed indictment, FBI press release, Italian Ministry of Justice extradition decree) is ingested.

## Summary

On **2025-07-31**, officers of the **[[italy-polizia-postale|Italian Polizia di Stato — Servizio Polizia postale e per la sicurezza cibernetica]]** arrested a foreign national at a hotel in **Riccione** (Rimini province, Emilia-Romagna, Italy) who was internationally wanted in connection with serious cyber-extortion offences committed between **2023 and the first months of 2025 against U.S.-based organisations**, with ransom demands totalling **millions of U.S. dollars**. The arrest was executed pursuant to a U.S. federal arrest warrant within an established bilateral cooperation framework with the **[[fbi|U.S. Federal Bureau of Investigation]]**.

The federal warrant was operationalised by the **Centro nazionale anticrimine informatico per la protezione delle infrastrutture critiche (Cnaipic)** of the Polizia Postale, in collaboration with the **Centro operativo per la sicurezza cibernetica Emilia-Romagna** and the **Sezione operativa per la Sicurezza cibernetica di Rimini**. Numerous computing devices and several thousand euros in cash were seized at the place of arrest. The press release does not state the prison of remand or the subsequent extradition stage.

> [!note] Identity not asserted from primary source
> The official Polizia di Stato communiqué does **not** name the suspect, his nationality, or his age. Italian regional outlets (Resto del Carlino, RiminiToday, Corriere Romagna) reported the same day that the arrested individual is **42-year-old Kazakh national Roman Khlynovskiy**, that the FBI attributes approximately **USD 31 million** in illicit profit to the underlying scheme, and that the suspect was remanded to **Busto Arsizio** prison pending extradition. These particulars are noted in the raw-file context block but are flagged in `missing_fields` and are not asserted in tier-1 frontmatter fields, in accordance with L19-strict.

## Background

Between **2023 and the first months of 2025**, an organised cyber-extortion campaign targeted U.S.-based organisations ("strutture statunitensi"), generating ransom demands of millions of U.S. dollars. The Italian primary source does not name the specific U.S. victim entities, the malware family used, or the exact aggregate loss figure beyond "milioni di dollari." The suspect was identified by U.S. authorities as actively involved in the campaign and was the subject of an internationally circulated wanted-person notice and a U.S. federal arrest warrant.

Italian regional media reported, in connection with the arrest, that the FBI considers the underlying actor to be among the most dangerous hackers globally and that approximately USD 31 million was recovered or attributed as illicit gain. These media particulars are not asserted from the tier-1 source.

## Participating Parties

| Role | Party |
|---|---|
| Lead Italian executing authority | [[italy-polizia-postale\|Polizia Postale (Servizio Polizia postale e per la sicurezza cibernetica)]] — Cnaipic, Centro operativo Emilia-Romagna, Sezione operativa di Rimini |
| Foreign investigating partner | [[fbi\|U.S. Federal Bureau of Investigation]] |
| Country of arrest | [[italy\|Italy]] |
| Country of pending extradition | [[united-states\|United States]] |

## Legal Framework

- **Provvedimento federale**: the press release describes the operative arrest authority as a U.S. federal arrest warrant ("provvedimento federale"). The release does not specify the issuing district court, the indictment caption, or the underlying U.S. statute.
- **Bilateral cooperation framework**: the release explicitly credits "consolidata cooperazione" and "condivisa modalità operativa" between Italian and U.S. law-enforcement, "particolarmente rafforzato anche grazie all'istituzione di esperti presso le rispettive ambasciate" (the embassy liaison-officer framework).
- **Italy–United States extradition treaty**: the release does not cite the treaty by article, but the operative pathway (Italian arrest of a person sought by U.S. judicial authority, pending extradition proceedings) is the canonical [[extradition|extradition]] route between the two states.

> [!warning] Legal status check needed
> The Italian primary source does not enumerate the specific U.S. statutes (e.g., 18 U.S.C. § 1030 / § 1951 / § 1956) charged, the indictment number, or the extradition treaty article invoked. These should be filled in from a corresponding U.S. DOJ unsealed indictment when one becomes available.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023 (since) | Cyber-extortion campaign against U.S.-based organisations begins | poliziadistato.it 2025-07-31 |
| 2023 → early 2025 | Multiple ransom demands totalling millions of U.S. dollars | poliziadistato.it 2025-07-31 |
| Pre-2025-07-31 | International wanted-person notice / U.S. federal arrest warrant issued | poliziadistato.it 2025-07-31 |
| 2025-07-31 (morning) | Suspect located by Polizia Postale at a hotel in Riccione during family holiday; arrest executed by Cnaipic with regional cyber-security operational centres | poliziadistato.it 2025-07-31 |
| 2025-07-31 | Italian Polizia di Stato publishes press release | poliziadistato.it 2025-07-31 |

## Results and Impact

- **Arrest**: 1 internationally wanted suspect detained.
- **Seizures**: numerous IT devices and several thousand euros in cash recovered at the hotel.
- **Pending phase**: extradition proceedings to the United States.
- **Underlying scheme**: ransom demands in the millions of U.S. dollars are attributed to the campaign by the Italian release; aggregate USD figure not stated in primary source.

## Cooperation Mechanisms Used

The release names two explicit cooperation arcs:

1. **Italy ↔ United States operational cooperation** — Italian Polizia Postale and the U.S. FBI conducted a "dispositivo internazionale di collaborazione" leading to the suspect's identification at the Riccione hotel and execution of the U.S. federal arrest warrant on Italian soil.
2. **Embassy liaison-officer framework** — the release explicitly attributes the strengthened bilateral cooperation to the deployment of expert liaison personnel at the Italian and U.S. embassies, a rare named acknowledgement of this [[informal-cooperation|liaison-officer mechanism]] in a public communiqué.

The subsequent surrender of the suspect to U.S. authorities is anticipated to proceed under the Italy–U.S. [[extradition|extradition]] treaty, though the release does not detail this stage.

## Challenges and Friction Points

- **Identification while in transit**: the suspect was a tourist at the time of arrest. Italian Polizia Postale relied on hotel registration data plus international wanted-person flagging to detect his presence. Had the suspect used false identity documents, detection would likely have been delayed.
- **No information on victim notification**: the Italian release names the victims only generically as "strutture statunitensi"; whether U.S. victim organisations were notified, and whether ransom payments are recoverable, is not addressed.

## Lessons Learned

- A bilateral liaison-officer / embassy-expert posture, sustained over years, can convert U.S. federal arrest warrants into successful operational arrests on Italian territory within a single day of suspect-location confirmation.
- Cyber-extortion subjects who travel to MLAT-partner jurisdictions for personal reasons (here, family holiday) are exposed to a real apprehension risk that is not always reflected in their operational tradecraft.
- The Cnaipic + regional cyber-security operational centre model (Emilia-Romagna + Rimini section in this case) demonstrates that the Italian Polizia Postale's territorial cyber-units, not only the national Cnaipic core, are now the routine executors of U.S. federal cyber arrest warrants.

## Follow-Up Actions

- **Pending**: extradition proceedings to the United States.
- **Open**: identification of the underlying U.S. indictment, victim entities, and specific U.S. statutes charged when the corresponding DOJ unsealing occurs.
- **Open**: relationship (if any) of the suspect to known ransomware brands or to other 2023–2025 U.S.-targeting cyber-extortion campaigns.

## Korean Involvement (한국의 참여)

None reported. South Korea is not named in the cited Tier-1 source as a participating jurisdiction or victim country.

## Contradictions & Open Questions

- The Italian release does not name the suspect or the underlying U.S. indictment; Italian media-reported particulars (Kazakh nationality, age 42, USD 31 million attributed profit, Busto Arsizio remand) are not asserted from the tier-1 source.
- Whether the underlying campaign involved a specific named ransomware family is not stated.
- The post-arrest extradition stage is not described; subsequent reporting suggests the extradition was reviewed by Italian judicial authorities, but this is not reflected in the original release and would require a separate Italian Ministry of Justice or court source to corroborate.
- Whether this case overlaps with any of the U.S.-side enforcement actions catalogued elsewhere in the wiki (for example DOJ ransomware prosecutions in 2024–2025) is unresolved without a U.S. primary-source counterpart.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-07-31_polizia-di-stato_riccione-arresto-cybercriminale-internazionale-khlynovskiy\|Arrestato a Rimini cybercriminale internazionale]] | Polizia di Stato (Italy) | 2025-07-31 | https://www.poliziadistato.it/articolo/arrestato-a-rimini-cybercriminale-internazionale |
