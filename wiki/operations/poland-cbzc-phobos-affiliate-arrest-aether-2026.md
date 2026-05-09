---
type: operation
title: "Poland CBZC arrest of Phobos-linked tooling suspect (Operation Aether, February 2026)"
title_ko: "폴란드 CBZC, Phobos 도구 공급 혐의 47세 남성 체포 (Operation Aether, 2026년 2월)"
aliases:
  - "CBZC 47-year-old Phobos arrest February 2026"
  - "Operation Aether Polish arrest 2026"
  - "Małopolskie Phobos hacking-tools arrest"
case_id: CYB-2026-009
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search-seizure
outcome: success
timeframe:
  announced: 2026-02-17
  start: ""
  end: 2026-02-17
  ongoing: false
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
target_entity: "47-year-old Polish national in Małopolskie Voivodeship suspected of producing, acquiring and distributing hacking tools (Polish Criminal Code Art. 269b § 1) and of contacting the Phobos ransomware group via encrypted messengers"
lead_agency: "[[poland-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[poland]]"
  - "[[united-states]]"
participating_agencies:
  - "[[poland-police]]"
  - "[[europol-ec3]]"
  - "[[us-doj]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[extradition]]"
legal_basis:
  - "Polish Criminal Code Article 269b § 1 (production, acquisition and distribution of programs designed to unlawfully obtain information stored in IT systems; max 5 years imprisonment)"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "One 47-year-old male suspect detained in Małopolskie Voivodeship by joint CBZC team from the Katowice and Kielce divisions on/around 2026-02-17"
    - "Computer and mobile phones seized from suspect's apartment, containing logins, passwords, credit card numbers and server IP addresses described by CBZC as usable for breaches and ransomware attacks"
    - "Charges filed under Polish Criminal Code Article 269b § 1 (hacking-tools offence); investigation supervised by the District Prosecutor's Office in Gliwice (Prokuratura Okręgowa w Gliwicach)"
    - "Arrest publicly framed by CBZC as part of Europol-coordinated Operation Aether, the broader law enforcement campaign against the Phobos ransomware ecosystem"
edges:
  - source_actor: "poland-police"
    target_actor: "europol-ec3"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "europol-ec3"
    target_actor: "us-doj"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "servers_seized"
  - "domains_seized"
  - "cryptocurrency_seized"
  - "victims_notified"
  - "indictments"
related_cases: []
related_operations:
  - "[[phobos-8base-crackdown]]"
  - "[[operation-us-v-evgenii-ptitsyn]]"
challenges_encountered: []
lessons_learned:
  - "CBZC's framing of the arrest under the named Europol-coordinated 'Operation Aether' branding is a useful primary-source data point linking the broader Phobos/8Base international campaign across action waves: the February 2025 [[phobos-8base-crackdown|Phobos/8Base arrest sweep]], the [[operation-us-v-evgenii-ptitsyn|November 2024 South Korea-to-USA extradition of the alleged Phobos administrator]], and this February 2026 Polish tooling-supply arrest are all referenced by CBZC under the same operational umbrella."
  - "The charge (Art. 269b § 1) is a tooling/preparatory offence, not a direct extortion charge, even though the suspect allegedly communicated with the Phobos group. This is consistent with how affiliate-side cybercrime cases are commonly built in Polish practice when the link to specific encryption events cannot yet be evidenced."
source_count: 1
sources:
  - "[[2026-02-17_cbzc-policja-pl_47-latek-phobos-zatrzymany-cbzc]]"
summary: "On 2026-02-17 the Polish Central Bureau for Combating Cybercrime (CBZC) announced the arrest of a 47-year-old man in Małopolskie Voivodeship for producing, acquiring and distributing hacking tools (Polish Criminal Code Art. 269b § 1) and for allegedly communicating with the Phobos ransomware group via encrypted messengers. CBZC frames the arrest as part of Europol-coordinated Operation Aether, the wider international law enforcement campaign against Phobos that previously included the extradition of the alleged Phobos administrator to the United States and coordinated arrests in Europe and beyond."
created: 2026-05-10
updated: 2026-05-10
---

> [!note] Provisional / single-source page
> This page is published below the standard preferred source threshold (`source_count >= 5`). It is retained as a provisional record because the Polish CBZC press release is a tier-1 primary source documenting (a) a previously unrecorded action wave of the Europol-coordinated Operation Aether campaign and (b) the first appearance of "Operation Aether" as a named umbrella in the wiki's primary-source corpus. It should be enriched as Europol/Eurojust corroborating sources are added.

## Summary

On **2026-02-17** the Polish [[poland-police|Central Bureau for Combating Cybercrime (CBZC)]] announced the arrest in **Małopolskie Voivodeship** of a 47-year-old Polish national suspected of producing, acquiring and distributing computer programs used to unlawfully obtain information stored in IT systems (Polish Criminal Code Article 269b § 1; maximum 5 years imprisonment). On the suspect's computer, police seized digital data including logins, passwords, credit card numbers and server IP addresses that CBZC described as usable for various attacks, including [[ransomware-ic|ransomware]]. The 47-year-old allegedly used encrypted messengers to contact the **Phobos** ransomware group.

CBZC explicitly attributes the arrest to its participation in **Operation Aether**, coordinated by [[europol-ec3|Europol]]. The press release identifies the prior extradition of the alleged Phobos administrator to the [[united-states|United States]] and "coordinated arrests in Europe and beyond" as elements of the same campaign, alongside technical actions against cybercriminal infrastructure.

## Background

Phobos has been the target of an evolving international law enforcement campaign tracked elsewhere in this wiki under [[phobos-8base-crackdown|the Phobos/8Base ransomware crackdown]] and [[operation-us-v-evgenii-ptitsyn|United States v. Evgenii Ptitsyn]] (the South Korea–to–USA extradition of the alleged Phobos administrator). The CBZC release describes Phobos as a Ransomware-as-a-Service (RaaS) organized cybercriminal group with more than 1,000 victims worldwide, including hospitals, schools, non-profit organizations, public bodies and private companies. According to [[us-doj|US Department of Justice]] documents cited by CBZC, total ransom proceeds associated with Phobos activity exceeded USD 16 million.

The 2026-02-17 Polish arrest is one of the first publicly named Operation Aether enforcement events in the wiki's primary-source corpus and the first to surface the "Aether" branding in CBZC's own communication.

## Participating Parties

| Role | Party |
|---|---|
| Lead apprehending authority | [[poland-police\|Polish CBZC — joint Katowice and Kielce divisions]] |
| Domestic prosecutorial supervision | District Prosecutor's Office in Gliwice (Prokuratura Okręgowa w Gliwicach) |
| Coordinating body | [[europol-ec3\|Europol]] (named on-source as coordinator of Operation Aether) |
| Cooperating jurisdiction (named in source) | [[united-states\|United States]] — referenced through the prior extradition of the alleged Phobos administrator to the USA and via [[us-doj\|US Department of Justice]] documents on Phobos ransom totals |
| Source-backed participating countries | [[poland\|Poland]], [[united-states\|United States]] |

> [!note] Audit note on participating_countries
> Per L17 / L19, only countries explicitly named in the tier-1 primary source are asserted as `participating_countries`. The CBZC release names Poland (locus of arrest) and the USA (extradition recipient and DOJ documents). Other Europe-or-beyond jurisdictions referenced as participating in Operation Aether are not named individually in this source and are left out of the country list pending corroboration.

## Legal Framework

- **Substantive charge**: Polish Criminal Code (Kodeks karny) **Article 269b § 1** — producing, acquiring or distributing computer programs designed to unlawfully obtain information stored in IT systems (hacking tools). Maximum 5 years imprisonment. This is a tooling/preparatory offence, distinct from direct extortion charges typically used against ransomware operators in [[united-states|US]] indictments.
- **Procedural channel for international cooperation**: [[europol-ec3|Europol]]-coordinated operational platform (Operation Aether) is the public mechanism cited in the release. Specific MLA instruments are not named in the press release.
- **Related international instrument**: the [[budapest-convention|Budapest Convention on Cybercrime]] is the prevailing legal basis for cross-border cooperation on ransomware-tooling offences for both Poland and the United States, although it is not specifically cited in the CBZC release.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| Pre-2026-02 | CBZC, Katowice and Kielce divisions, develop intelligence on a Małopolskie-based suspect supplying hacking tooling and communicating with the Phobos group via encrypted messengers | CBZC 2026-02-17 |
| 2026-02 (on/before publication) | CBZC executes search of suspect's apartment in Małopolskie Voivodeship; seizes computer, mobile phones and digital data (logins, passwords, credit card numbers, server IP addresses) | CBZC 2026-02-17 |
| 2026-02 (on/before publication) | Charges filed under Polish Criminal Code Art. 269b § 1; investigation supervised by Prokuratura Okręgowa w Gliwicach | CBZC 2026-02-17 |
| 2026-02-17 | Public announcement of the arrest by CBZC press service; arrest publicly attributed to Europol-coordinated Operation Aether | CBZC 2026-02-17 |

## Results and Impact

- One arrest in Małopolskie Voivodeship (Polish national, age 47).
- Search-and-seizure of computer and mobile phones containing logins, passwords, credit card numbers and server IP addresses.
- Charges filed under Polish Criminal Code Article 269b § 1; maximum 5-year sentence on the books.
- No reported direct decryption-key recovery, server takedown, domain seizure, cryptocurrency seizure or victim notification reported in this specific Polish action.
- The release positions the arrest within the wider Operation Aether campaign that also produced the prior extradition of the alleged Phobos administrator to the United States.

## Cooperation Mechanisms Used

The mechanisms publicly named in the CBZC release are:
- Europol operational coordination under the named "Operation Aether" branding ([[europol-ec3|Europol]]).
- Domestic Polish [[search-seizure|search and seizure]] executed by CBZC under Polish criminal procedure.
- Reference to a prior cross-jurisdiction [[extradition|extradition]] event delivering the alleged Phobos administrator to the United States, framed as part of the same campaign.

The release does not name a Joint Investigation Team, an MLAT request, an European Investigation Order, or any specific bilateral instrument as the basis for this particular arrest.

## Challenges and Friction Points

- The charge is a tooling/preparatory offence under Polish Article 269b § 1 rather than a direct extortion charge tied to a specific Phobos encryption event. This is consistent with affiliate-side cybercrime case-building when the evidentiary chain to specific victim incidents is not yet sufficient.
- Cryptocurrency-tracing and Darknet usage are flagged in the CBZC release as obstacles to precise revenue attribution for Phobos activity overall.

## Lessons Learned

- CBZC's public framing of the arrest under "Operation Aether" provides a primary-source data point linking action waves of the broader Phobos campaign across years and jurisdictions, including the [[phobos-8base-crackdown|February 2025 Phobos/8Base arrest sweep]] and the [[operation-us-v-evgenii-ptitsyn|November 2024 South Korea-to-USA extradition of the alleged Phobos administrator]].
- Affiliate/tooling-supply prosecutions remain a core enforcement modality against RaaS ecosystems even as direct attribution to specific intrusion events stays evidentiarily hard.

## Follow-Up Actions

- Trial proceedings against the 47-year-old suspect in Polish courts (Prokuratura Okręgowa w Gliwicach supervising) — outcome not yet public as of the source date.
- Further Operation Aether enforcement actions implied by the release ("coordinated arrests in Europe and beyond") to be tracked as Europol/Eurojust corroborating sources are ingested.

## Korean Involvement (한국의 참여)

The CBZC release does not name the Republic of Korea or any Korean agencies. It is, however, contextually linked to the Phobos campaign whose [[operation-us-v-evgenii-ptitsyn|November 2024 extradition]] from the Republic of Korea to the United States is recorded elsewhere in this wiki. The 2026-02-17 Polish action is therefore part of a broader Phobos enforcement arc to which Korean cooperation has previously contributed, even though Korea is not a participant in this specific Polish arrest.

## Contradictions & Open Questions

- The CBZC release does not name additional specific countries in the "Europe and beyond" coordinated arrest cohort tied to Operation Aether — those are asserted only through secondary reporting and are not added to `participating_countries` here.
- The exact arrest date (versus publication date 2026-02-17) is not stated; the press release does not give a precise day for the search and apprehension prior to publication.
- The relationship between Operation Aether's "Aether" naming and earlier Europol-coordinated Phobos enforcement (e.g. the February 2025 [[phobos-8base-crackdown|Phobos/8Base crackdown]]) is not formally defined in the CBZC release; it remains unclear whether Aether is a renaming, a successor phase, or a parallel umbrella.
- No specific Joint Investigation Team, MLAT request, or European Investigation Order is identified as the legal basis for cross-border information exchange in this particular Polish action.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-02-17_cbzc-policja-pl_47-latek-phobos-zatrzymany-cbzc\|47-latek związany z grupą Phobos zatrzymany przez policjantów CBZC (47-year-old linked to Phobos group arrested by CBZC officers)]] | Centralne Biuro Zwalczania Cyberprzestępczości (CBZC) | 2026-02-17 | https://cbzc.policja.gov.pl/bzc/aktualnosci/823,47-latek-zwiazany-z-grupa-Phobos-zatrzymany-przez-policjantow-CBZC.html |
