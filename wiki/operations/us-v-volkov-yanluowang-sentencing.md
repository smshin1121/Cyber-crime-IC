---
type: operation
title: "U.S. v. Aleksei Volkov — Yanluowang Initial-Access Broker Sentencing (SDIN, 2026)"
title_ko: "미합중국 대 알렉세이 볼코프 — 얀루오왕 초기 접속 브로커 형 선고 (SDIN, 2026)"
aliases:
  - "Volkov sentencing 2026"
  - "Volkov Yanluowang IAB sentencing"
  - "Aleksei Volkov SDIN"
case_id: CYB-2026-013
period: 3
operation_type: prosecution
status: completed
enforcement_type:
  - extradition
  - sentencing
outcome: success
timeframe:
  announced: 2026-03-23
  start: 2024-01
  end: 2026-03-23
  ongoing: false
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[hacking-ic]]"
target_entity: "Aleksei Volkov, 26, of St. Petersburg, Russia — initial-access broker for Yanluowang and other ransomware groups; multiple US-victim ransomware attacks (over USD 9 million in actual losses and over USD 24 million in intended losses)"
lead_agency: "[[us-doj]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[united-states]]"
  - "[[italy]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Southern District of Indiana indictment, 4 counts: 18 U.S.C. § 1028 (unlawful transfer of a means of identification); 18 U.S.C. § 1029 (access device fraud); 18 U.S.C. § 1028A (aggravated identity theft); trafficking in access information"
  - "Eastern District of Pennsylvania indictment, 2 counts: conspiracy to commit computer fraud; conspiracy to commit money laundering"
  - "US-Italy extradition treaty (DOJ OIA-coordinated)"
results:
  arrests: 1
  indictments: 6
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Volkov sentenced to 81 months in prison in the Southern District of Indiana on 2026-03-23"
    - "Volkov pleaded guilty on 2025-11-25 to 4 SDIN counts and 2 EDPA counts after consolidation in SDIN"
    - "Restitution ordered: at least USD 9 167 198.19 to known victims; full equipment forfeiture"
    - "Arrest occurred in Rome, Italy in January 2024; extradited to the United States via DOJ OIA cooperation with the Government of Italy"
    - "Volkov operated as an initial-access broker (IAB) — gaining unauthorized access to US-corporate networks and selling that access to ransomware groups including Yanluowang"
    - "Volkov's IAB sales facilitated dozens of US-victim ransomware attacks; attackers demanded tens of millions of dollars and received millions"
edges:
  - source_actor: "us-doj"
    target_actor: "italy"
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: "fbi"
    target_actor: "italy"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific Italian arresting agency (release names only 'Police in Rome, Italy')"
related_cases: []
related_operations:
  - "[[operation-cronos-phase2]]"
challenges_encountered: []
lessons_learned:
  - "Volkov's case is a public-record demonstration that US-Italy ransomware-affiliate extradition pathways are operationally available and tractable on a 12-15 month timeline (Jan 2024 arrest → Mar 2026 sentencing), providing a jurisdiction-pair benchmark for ransomware IAB enforcement against Russian nationals when they travel into US-treaty-partner Schengen states."
  - "The release explicitly frames Volkov's role as 'initial access broker', formally codifying IAB as a category of ransomware-ecosystem actor in DOJ-charging language. This is consistent with the broader 2024-2026 trend toward IAB-targeted prosecutions across the wiki corpus."
source_count: 1
sources:
  - "[[2026-03-23_justice-gov_russian-citizen-sentenced-prison-hacking-us-companies-yanluowang]]"
summary: "On 2026-03-23 the US Justice Department announced the 81-month federal prison sentence in the Southern District of Indiana of Aleksei Volkov, a 26-year-old Russian citizen of St. Petersburg, for his role as an 'initial access broker' enabling the Yanluowang ransomware group and other cybercrime groups to conduct ransomware attacks against US companies. Volkov was indicted in both SDIN and EDPA, the cases were consolidated in SDIN, he pleaded guilty on 2025-11-25 to 4 SDIN counts and 2 EDPA counts, and was sentenced to USD 9 167 198.19+ in restitution. Arrest in Rome, Italy in January 2024; extradition coordinated by DOJ Office of International Affairs with the Government of Italy."
created: 2026-05-08
updated: 2026-05-08
---
## Summary

On 2026-03-23 the US Justice Department announced the 81-month federal prison sentence in the Southern District of Indiana of Aleksei Volkov, a 26-year-old Russian citizen of St. Petersburg, for his role as an "initial access broker" (IAB) enabling the Yanluowang ransomware group and other cybercrime groups to conduct ransomware attacks against US companies. Volkov facilitated dozens of US-victim ransomware attacks, causing over USD 9 million in actual losses and over USD 24 million in intended losses. The court ordered full restitution of at least USD 9 167 198.19 to known victims and the forfeiture of equipment used in the offences.

The case is a US-Italy bilateral extradition record. Volkov was indicted in both the Southern District of Indiana (4 counts) and the Eastern District of Pennsylvania (2 counts), arrested by police in Rome, Italy, in January 2024, extradited to the United States, and pleaded guilty on 2025-11-25 to all six counts after the EDPA case was consolidated in SDIN. The Justice Department's Office of International Affairs is named as the agency that "worked with the Government of Italy to secure the arrest and extradition from Italy of Volkov."

## Background

Volkov operated as an initial-access broker — a type of cybercriminal who gains unauthorized access to corporate computer networks and sells that access to other cybercriminals such as ransomware groups. His co-conspirators used the access he provided to deploy ransomware against US victims, encrypting victim data and demanding cryptocurrency ransom in exchange for restoring data access and not publishing stolen data on a leak site. The release places Volkov's IAB activity within the Yanluowang ransomware ecosystem and explicitly identifies the cooperative ransomware kill chain (IAB sales → ransomware deployment → leak-site coercion → ransom payment shared back to the IAB).

## Participating Parties

| Role | Parties |
|---|---|
| US prosecutorial line (consolidated case) | US Attorney's Office for the Southern District of Indiana; AUSAs MaryAnn T. Mindrum and Matthew B. Miller (SDIN); AUSA Sarah Wolfe (EDPA); Senior Counsel Matthew A. Lamberti (CCIPS); AUSA Edward Chang (D. Conn., on detail to CCIPS) |
| US investigators | [[fbi\|FBI]] Indianapolis Field Office (SAC Timothy O'Malley); FBI Philadelphia Field Office (SAC Wayne A. Jacobs) |
| US international cooperation channel | [[office-of-international-affairs\|US DOJ Office of International Affairs]] |
| Italian arresting authority | Police in Rome, Italy (specific Italian agency not enumerated in the cited tier-1 source); Government of Italy as the extradition partner |
| Source-backed participating countries | [[united-states\|United States]] (charging and prosecuting state); [[italy\|Italy]] (arrest and extradition state); [[russia\|Russia]] (defendant nationality and stated residence) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2021–2022 | Volkov works with members of the Yanluowang ransomware group; facilitates dozens of US-victim ransomware attacks per the indictment narrative | DOJ 2026-03-23 (referencing reporting context) |
| January 2024 | Police in Rome, Italy, arrest Volkov | DOJ 2026-03-23 |
| 2024-2025 | Volkov extradited to the United States; SDIN and EDPA cases consolidated in SDIN | DOJ 2026-03-23 |
| 2025-11-25 | Volkov pleads guilty to 4 SDIN counts and 2 EDPA counts | DOJ 2026-03-23 |
| 2026-03-23 | SDIN sentences Volkov to 81 months in prison; full restitution ordered | DOJ 2026-03-23 (PR 26-280) |

## Results and Impact

- 81-month (6 years 9 months) federal prison sentence in the Southern District of Indiana.
- Restitution ordered: at least USD 9 167 198.19 to known victims, plus full forfeiture of equipment used in the offences.
- USD 24 million+ in intended losses from the attacks Volkov enabled (per court documents).
- Tens of millions of dollars in ransom demanded by Volkov's co-conspirators across the Yanluowang and related ransomware lines; millions actually received.
- Six federal counts: SDIN (unlawful transfer of a means of identification; trafficking in access information; access device fraud; aggravated identity theft) and EDPA (conspiracy to commit computer fraud; conspiracy to commit money laundering).

## Cooperation Mechanisms Used

The cited release describes a [[extradition|US-Italy bilateral extradition]] coordinated by the [[office-of-international-affairs|US DOJ Office of International Affairs]] working with the Government of Italy. The release does not enumerate the specific Italian arresting unit, the underlying treaty article cited in the extradition request, or the timing of the formal extradition hearing under Italian law. The cooperation pattern is therefore captured here as a bilateral OIA-led extradition record without a formally-cited MLAT or Joint Investigation Team designation.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited DOJ release as a victim, source, or cooperation jurisdiction for this operation. The case is recorded in the wiki for the US-Italy bilateral extradition pathway, the public-record IAB-prosecution category in DOJ charging language, and the Yanluowang-line attribution. Korea has separately pursued voice-phishing and online-fraud-affiliated extradition pathways from Cambodia and the Philippines tracked elsewhere in this wiki ([[korea-cambodia-philippines-73-extradition-2026]]); the comparison between US-Italy and Korea-Cambodia/Philippines extradition cycles is a useful structural anchor for SNA edge weighting on Korea-as-requesting-state cooperation.

## Contradictions & Open Questions

- The specific Italian arresting unit ("Police in Rome, Italy") is not enumerated in the cited release; whether it was the Polizia di Stato Rome questore or a specialised cybercrime unit is unstated.
- The exact Italian-court extradition hearing date and formal extradition decision date are not enumerated in the cited release; only the January 2024 arrest and the post-extradition US plea (2025-11-25) and sentencing (2026-03-23) milestones are recorded.
- The full Yanluowang-affiliate cohort beyond Volkov is not enumerated in this cited release; the wiki separately records [[operation-cronos-phase2|Operation Cronos Phase 2]] and other ransomware-attribution waves where the Yanluowang or affiliated lines may overlap, but a definitive cross-link to a single Yanluowang umbrella record is not yet available in this corpus.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-03-23_justice-gov_russian-citizen-sentenced-prison-hacking-us-companies-yanluowang\|Russian Citizen Sentenced to Prison for Hacking into U.S. Companies and Enabling Major Cybercrime Groups to Extort Tens of Millions of Dollars]] | US DOJ (OPA), Press Release 26-280 | 2026-03-23 | https://www.justice.gov/opa/pr/russian-citizen-sentenced-prison-hacking-us-companies-and-enabling-major-cybercrime-groups |
