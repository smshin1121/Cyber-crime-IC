---
type: operation
title: "U.S.–Romania Swatting Ring Prosecution (Szabo)"
aliases:
  - "United States v. Thomasz Szabo"
  - "Plank / Jonah / Cypher swatting ring case"
case_id: CYB-2026-721
period: 3
operation_type: prosecution
status: completed
enforcement_type:
  - arrest
  - extradition
  - indictment
outcome: success
timeframe:
  announced: 2026-04-29
  start: 2024
  end: 2026-04-29
  ongoing: false
crime_types:
  - "[[cyberstalking-ic]]"
crime_type: "[[cyberstalking-ic]]"
target_entity: "Thomasz Szabo (Romanian, 27), aka 'Plank' / 'Jonah' / 'Cypher' — leader of online swatting / bomb-threat ring whose victims included 25+ Members of Congress, 6+ senior U.S. Executive officials, 13+ senior federal LE officials, federal judges, 27+ state officials, 4 religious institutions, multiple journalists."
lead_agency: "[[us-doj]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[united-states]]"
  - "[[romania]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[us-secret-service]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
legal_basis:
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
mechanisms_used:
  - "[[mlat-process]]"
  - "[[extradition]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Conviction by guilty plea (2025-06-02): conspiracy + threats involving explosives"
    - "48-month federal prison sentence + 3 years supervised release (2026-04-29); prosecutors had requested 57 months"
    - "Extradition from Romania to United States (November 2024)"
edges:
  - source_actor: Romania
    target_actor: "United States"
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: Romania
    target_actor: "United States"
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "case_number / indictment number"
  - "U.S. Code statutes for the two counts of conviction"
  - "named subordinate co-conspirators"
  - "Szabo's online platform and group-name"
  - "Romanian counterpart agency formally named (the U.S. release names only 'Romanian authorities' generically)"
related_cases:
  - "[[us-v-szabo-swatting-ring]]"
related_operations:
  []
challenges_encountered:
  []
lessons_learned:
  - "Tier-1 U.S. release names a foreign country (Romania) and a foreign-evidence MLA channel as the operational hinge of an extradition for cyber-enabled threat conduct, not financial cybercrime — useful as a non-financial precedent for `[[mlat-process]]` and `[[extradition]]` reuse."
  - "U.S. inter-agency stack: Secret Service (lead investigator) + FBI Counterterrorism + U.S. Capitol Police + DOJ NSD Counterterrorism Section + DOJ Office of International Affairs + multiple cooperating USAOs. Pattern: Secret Service / Capitol Police primacy when victims are sitting U.S. legislators."
source_count: 1
sources:
  - "[[2026-04-29_us-secret-service_szabo-romania-swatting-sentenced-48-months]]"
created: 2026-05-09
updated: 2026-05-09
---
> [!info] Provisional / single-source
> Source count is 1 (the 2026-04-29 sentencing release). The 2024 indictment and the 2025-06-02 plea announcement exist as additional primary tier-1 sources but are not yet ingested. This operation page is published because the underlying release explicitly names ≥2 countries (United States + Romania) and frames international cooperation (MLA + extradition) as the central success factor; it is not a thin domestic-only follow-on stub.

## Summary

Single-defendant transnational prosecution: Romania-based ringleader Thomasz Szabo extradited to the United States and ultimately sentenced (2026-04-29) for leading an online swatting / bomb-threat group that conducted a December 2023 – January 2024 spree against more than 75 senior U.S. public officials. Operationally significant because the core international-cooperation mechanisms (`[[mlat-process]]` for evidence and `[[extradition]]` for the defendant) are the explicit, on-the-record drivers of the U.S. side's success. Romania's authorities were credited as "critical" by the U.S. press release.

## Background

According to court documents summarised in the 2026-04-29 release, Szabo had founded and led the swatting / bomb-threat online community starting in **late 2020**, including personal threats against NYC synagogues (Dec 2020) and the U.S. Capitol / President-elect (Jan 2021). The December 2023 – January 2024 spree, with victims spanning Congress, senior Executive officials, federal LE leadership, federal judges, state officials, religious institutions, and journalists, escalated the case to its U.S.-multi-agency posture.

## Participating Parties

**Lead U.S. prosecutor:** U.S. Attorney's Office for the District of Columbia (announced by U.S. Attorney Jeanine Ferris Pirro). Treated under `[[us-doj]]` until a dedicated USAO-DC page is added.

**U.S. investigative agencies:**

- `[[us-secret-service]]` — Washington Field Office (SAIC Tara McLeese), Criminal Investigative Division, plus Bucharest Resident Office, Miami Field Office, Syracuse Resident Office, Springfield Resident Office.
- `[[fbi]]` — Washington Field Office Counterterrorism Division (SAIC Michael Burgwald), Minneapolis Field Office (SAIC Christopher D. Dotson), and the FBI Legat Office in Bucharest.
- U.S. Capitol Police (Chief Michael Sullivan) — quoted; agency-level wikilink not asserted (no existing wiki page; per L19-strict).

**U.S. coordination / extradition channel:**

- `[[office-of-international-affairs]]` (DOJ Office of International Affairs) — credited with substantial assistance in securing arrest, extradition, and evidence from abroad through MLA requests.
- DOJ National Security Division Counterterrorism Section — credited; not separately wikilinked here.
- Cooperating U.S. Attorney's Offices for the Western District of Washington, the District of South Dakota, the Middle District of Florida, the Southern District of Florida, the Southern District of Illinois, and the Northern District of New York.

**Foreign side:**

- `[[romania]]` (Romanian authorities) — credited generically as "critical." The 2026-04-29 release does **not** specify which Romanian agency executed the arrest or processed the extradition; per L19-strict, Romanian sub-agencies (e.g. `[[romanian-police]]`, `[[romania-diicot]]`, `[[romania-public-ministry]]`) are NOT asserted in `participating_agencies` and are flagged in `missing_fields` instead.

## Legal Framework

- Charges of conviction (per the release): one count of **conspiracy** + one count of **threats involving explosives**.
- Cooperation legal basis: `[[mutual-legal-assistance]]` (MLA requests for foreign evidence) + `[[extradition]]` from Romania to the United States.

## Operational Timeline

| Date | Event |
|---|---|
| late 2020 | Szabo founds the online swatting / bomb-threat community. |
| 2020-12 | Szabo personal threat: NYC synagogues mass shooting. |
| 2021-01 | Szabo personal threat: U.S. Capitol explosives + threat against President-elect. |
| 2023-12-24 → early 2024-01 | Group spree against 75+ U.S. public officials, religious institutions, and journalists. |
| 2024 | Indictment filed (number not stated in this release). |
| 2024-11 | Szabo extradited from Romania to the United States. |
| 2025-06-02 | Szabo pleads guilty: conspiracy + threats involving explosives. |
| 2026-04-29 | Sentenced: 48 months prison + 3 years supervised release. |

## Results and Impact

- 1 arrest (Romania, 2024).
- 1 extradition (Romania → United States, November 2024).
- 1 conviction by guilty plea (2025-06-02).
- 48-month federal prison sentence + 3 years supervised release (2026-04-29).
- *Likely* deterrence value publicly framed by U.S. officials ("we will cross the globe to track threats down" — U.S. Capitol Police Chief Michael Sullivan).

## Cooperation Mechanisms Used

- **MLA / evidence requests** (`[[mlat-process]]`, `[[mutual-legal-assistance]]`) — DOJ Office of International Affairs used MLA requests to secure evidence from abroad.
- **Extradition** (`[[extradition]]`) — formal extradition from Romania to the United States, executed November 2024.
- **In-country liaison** — FBI Legat Bucharest and U.S. Secret Service Bucharest Resident Office acted as in-country U.S. liaison points to Romanian counterparts.

## Challenges and Friction Points

Not stated in the source. The release projects an unambiguously successful cooperation narrative.

## Lessons Learned

- A non-financial cyber case (cyber-enabled threats / swatting) was successfully extradited from a Council of Europe jurisdiction (Romania) within roughly 12 months of arrest — useful as a counter-example to the common assumption that swatting / hoax-threat cases are too low-priority for transnational extradition.
- The U.S. Secret Service, not the FBI, was named as the **lead investigator** because the victims included senior protected officials (Members of Congress, cabinet officials, former Presidents). FBI's role was packaged through its Counterterrorism Division. This is the operational fingerprint when swatting victims are U.S. protectees rather than ordinary civilians.

## Follow-Up Actions

- Ingest the 2024 indictment and the 2025-06-02 guilty-plea announcement when accessible to add case_number and statutory provisions.
- Cross-check whether any subordinate U.S.-based co-conspirators have been separately charged; if so, file in `wiki/cases/` as siblings of `[[us-v-szabo-swatting-ring]]`.
- Confirm or refute whether this case is operationally linked to the separately documented `[[hungary-romania-swatting-doxing-discord-2026]]` (different lead agencies, different time period, different victim set; treated here as **separate** operations until a tier-1 source links them).

## Korean Involvement (한국의 참여)

None reported.

## Contradictions & Open Questions

- The 2026-04-29 release does **not** name the Romanian agency that effected Szabo's arrest or processed his extradition, making it impossible to assert a Romanian sub-agency wikilink without violating L19-strict. Listed in `missing_fields`.
- The release does not list the named co-conspirators or the size of Szabo's online group, leaving the network's structure not yet documentable.
- The operational relationship (if any) between this case and `[[hungary-romania-swatting-doxing-discord-2026]]` is not established by any tier-1 source available to this wiki at ingest time.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Romanian Citizen Sentenced in D.C. for 'Swatting' Members of Congress, Churches, and Former U.S. President | U.S. Secret Service (republishing U.S. Attorney's Office, District of Columbia) | 2026-04-29 | https://www.secretservice.gov/newsroom/releases/2026/04/romanian-citizen-sentenced-dc-swatting-members-congress-churches-and |
