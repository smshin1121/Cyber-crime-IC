---
type: operation
title: "Black Basta ransomware ringleader arrest warrant and Ukrainian searches (BKA-ZIT-led DE/UA/CH/NL/UK action, January 2026)"
title_ko: "Black Basta 랜섬웨어 그룹 수괴 체포영장 발부 및 우크라이나 가택수색 (BKA·ZIT 주도 5개국 공조, 2026년 1월)"
aliases:
  - "Black Basta ringleader public manhunt 2026"
  - "BKA ZIT Black Basta arrest warrant January 2026"
  - "DE UA CH NL UK Black Basta takedown 2026"
case_id: CYB-2026-010
period: 3
operation_type: joint-investigation
status: ongoing
enforcement_type:
  - search-seizure
  - arrest
outcome: partial
timeframe:
  announced: 2026-01-15
  start: ""
  end: ""
  ongoing: true
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
target_entity: "Black Basta ransomware group — alleged ringleader (Russian citizen, also previously a Conti business partner) plus Ukrainian-citizen members suspected of hash-cracking and crypter roles supporting intrusion tradecraft. Active 2022-03 through at least 2025-02; ≥100 victims in Germany and ≈600 additional organizations worldwide; proceeds in the three-digit-million-EUR range."
lead_agency: "[[germany-bka]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[switzerland]]"
  - "[[ukraine]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[dutch-nhtcu]]"
  - "[[switzerland-fedpol]]"
  - "[[ukraine-police]]"
  - "[[europol-ec3]]"
  - "[[interpol]]"
mechanisms_used:
  - "[[europol-ec3]]"
  - "[[interpol]]"
  - "[[mutual-legal-assistance]]"
legal_basis:
  - "German Criminal Code (Strafgesetzbuch) — formation of a criminal organization (Bildung einer kriminellen Vereinigung), commercial-and-gang extortion (gewerbs- und bandenmäßige Erpressung), and computer sabotage (Computersabotage)"
  - "Ukrainian Criminal Code provisions invoked by the Office of the Prosecutor General of Ukraine for the Ivano-Frankivsk and Lviv search authorities (specific articles not enumerated in the BKA release)"
  - "Bilateral request channels between German ZIT/BKA and Ukrainian Cyber Police / Office of the Prosecutor General of Ukraine for the Aug 2025 Kharkiv-area search and the Jan 2026 Ivano-Frankivsk / Lviv searches"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Public arrest warrant issued by ZIT/BKA against the alleged Black Basta ringleader (Russian citizen)"
    - "Two residences in Ukraine (Ivano-Frankivsk and Lviv regions) searched in January 2026 against suspects accused of hash-cracking; evidence seized; suspects not reported as taken into custody in this release"
    - "Earlier Aug 2025 action wave: residence near Kharkiv searched at ZIT/BKA request, with the Ukrainian-citizen suspect (alleged crypter) questioned and evidence seized"
    - "Public manhunt published via Europol Most Wanted (eumostwanted.eu) and BKA Öffentlichkeitsfahndung 69 with photos and description"
    - "Reported attribution scope: ≥100 extortion victims in Germany plus ≈600 additional organizations worldwide between March 2022 and February 2025; proceeds in the three-digit-million EUR range, including >EUR 20 million from Germany alone"
edges:
  - source_actor: "germany-bka"
    target_actor: "germany-frankfurt-prosecutor"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "germany-bka"
    target_actor: "ukraine-police"
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: "germany-bka"
    target_actor: "dutch-nhtcu"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "germany-bka"
    target_actor: "switzerland-fedpol"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "germany-frankfurt-prosecutor"
    target_actor: "ukraine-police"
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
  - source_actor: "europol-ec3"
    target_actor: "germany-bka"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
  - source_actor: "interpol"
    target_actor: "germany-bka"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "arrests"
  - "indictments"
  - "servers_seized"
  - "domains_seized"
  - "cryptocurrency_seized"
  - "decryption_keys_recovered"
  - "victims_notified"
related_cases: []
related_operations:
  - "[[operation-endgame]]"
  - "[[operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti-ransomware-conspiracies]]"
  - "[[operation-us-v-galochkin-trickbot-conti]]"
  - "[[poland-cbzc-phobos-affiliate-arrest-aether-2026]]"
challenges_encountered: []
lessons_learned:
  - "The BKA release frames the action as a continuation of pre-existing cooperation — the Aug 2025 Kharkiv-area search preceded the Jan 2026 Ivano-Frankivsk/Lviv searches — illustrating how German-Ukrainian ransomware cooperation under wartime conditions has remained operational across multiple 2025-2026 action waves."
  - "Russian citizenship of the alleged ringleader functions as a structural barrier: the public arrest warrant + Europol/Interpol Most Wanted publication is the realistically available enforcement vector when the suspect is presumed to be in a non-cooperating jurisdiction."
  - "ZIT (Generalstaatsanwaltschaft Frankfurt am Main — Zentralstelle zur Bekämpfung der Internetkriminalität) appears as the consistent German prosecutorial counter-party for ransomware international cooperation cases (cf. Operation Endgame, the 2025 Crimenetwork takedown, and the Aisuru/Kimwolf 2026 botnet action)."
source_count: 1
sources:
  - "[[2026-01-15_bka-de_fahndung-nach-kopf-der-ransomware-gruppierung-black-basta]]"
summary: "On 2026-01-15 the German Bundeskriminalamt (BKA) and the Frankfurt am Main Generalstaatsanwaltschaft — Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT) — announced a public arrest warrant for the alleged ringleader of the Black Basta ransomware group, identified as a Russian citizen with previous Conti links, and confirmed January 2026 searches in the Ukrainian Ivano-Frankivsk and Lviv regions of two suspected Ukrainian-citizen members accused of hash-cracking. The action is the public phase of an internationally coordinated investigation by ZIT/BKA together with the Dutch NHTCU, Swiss fedpol and Bundesanwaltschaft, the British SEROCU, and the Ukrainian Cyber Police and Office of the Prosecutor General of Ukraine, supported by Europol and Interpol via the Most Wanted publication channels."
created: 2026-05-10
updated: 2026-05-10
---

> [!note] Provisional / single-source page
> This page is published below the standard preferred source threshold (`source_count >= 5`). It is retained as a provisional record because the BKA press release is a tier-1 primary source documenting (a) a previously unrecorded multi-country (DE/NL/CH/UK/UA) law-enforcement coalition explicitly named in a single official statement, and (b) the public arrest-warrant phase of an active Black Basta investigation. It should be enriched as Europol/Eurojust/Politie/fedpol/NCA corroborating sources are added.

## Summary

On **2026-01-15** the [[germany-bka|Bundeskriminalamt (BKA)]] and the [[germany-frankfurt-prosecutor|Generalstaatsanwaltschaft Frankfurt am Main — Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT)]] announced that they had issued a public arrest warrant for the alleged ringleader of the **Black Basta** [[ransomware-ic|ransomware]] group, identified as a Russian citizen with prior alleged ties to the **Conti** ransomware group as a business partner. Photos and descriptions are published via the BKA's Öffentlichkeitsfahndung 69 entry and via Europol/Interpol Most Wanted channels (eumostwanted.eu).

The same release confirmed that searches were carried out in [[ukraine|Ukraine]] against two suspected Ukrainian-citizen members of Black Basta in the **Ivano-Frankivsk** and **Lviv** administrative regions. The Ukrainian searches were executed by the [[ukraine-police|Cyber Police (Cyberpolizei)]] of the National Police of Ukraine and the Office of the Prosecutor General of Ukraine; both suspects are accused of *hash cracking* — systematically computing captured hash values to obtain credentials enabling lateral movement inside victim networks. Evidence was seized; the BKA release does not report whether the suspects were taken into custody.

The release explicitly attributes the joint, internationally coordinated investigation to the following counter-party agencies: ZIT and BKA (Germany), [[switzerland-fedpol|Bundesamt für Polizei (fedpol)]] and Bundesanwaltschaft (Switzerland), [[dutch-nhtcu|National High Tech Crime Unit (NHTCU)]] (Netherlands), and the **South East Regional Organised Crime Unit (SEROCU)** (United Kingdom), together with independent investigations of the Ukrainian National Police in Kyiv and Kharkiv and the Ukrainian Prosecutor General's Office. The public manhunt is supported by [[europol-ec3|Europol]] and [[interpol|Interpol]].

Black Basta is described in the release as responsible — between March 2022 and February 2025 — for extorting more than 100 entities in Germany and approximately 600 additional organizations worldwide, with proceeds in the three-digit-million-EUR range, including more than EUR 20 million obtained from Germany alone. Reported victim categories include companies, hospitals, public institutions and government authorities.

## Background

The 2026-01-15 action is described as the *continuation of an ongoing cooperation*. The release names a prior action wave: at the end of August 2025, Ukrainian officials, acting on a request from ZIT and BKA, searched the residence of another Black Basta member near **Kharkiv**, secured evidence and questioned the suspect. That suspect is alleged to have served as a *crypter* — ensuring that the Black Basta malware was not flagged by antivirus engines.

Black Basta is one of the most active ransomware groups of 2022–2025; the BKA release places it among the most damaging extortion ecosystems to have targeted German industrial, healthcare and public-sector targets in the period. The alleged ringleader's previous association with the [[operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti-ransomware-conspiracies|Conti ransomware ecosystem]] is asserted in the BKA release.

## Participating Parties

| Role | Party |
|---|---|
| Lead investigative authority (DE) | [[germany-bka\|Bundeskriminalamt (BKA)]] |
| Lead prosecutorial authority (DE) | [[germany-frankfurt-prosecutor\|Generalstaatsanwaltschaft Frankfurt am Main — Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT)]] |
| Cooperating LE (NL) | [[dutch-nhtcu\|National High Tech Crime Unit (NHTCU)]] |
| Cooperating LE (CH) | [[switzerland-fedpol\|Bundesamt für Polizei (fedpol)]] |
| Cooperating prosecutor (CH) | Bundesanwaltschaft (federal Office of the Attorney General, BA) |
| Cooperating LE (UK) | South East Regional Organised Crime Unit (SEROCU) |
| Executing LE (UA) | [[ukraine-police\|National Police of Ukraine — Cyber Police (Cyberpolizei)]]; Office of the Prosecutor General of Ukraine |
| Coordinating body | [[europol-ec3\|Europol]] |
| Coordinating body | [[interpol\|Interpol]] |
| Source-backed participating countries | [[germany\|Germany]], [[netherlands\|Netherlands]], [[switzerland\|Switzerland]], [[ukraine\|Ukraine]], [[united-kingdom\|United Kingdom]] |

> [!note] Audit note on participating_countries (L17 / L19 / L24)
> Only the five jurisdictions explicitly named in the BKA tier-1 release (Germany, Netherlands, Switzerland, Ukraine, United Kingdom) are asserted as `participating_countries`. The alleged ringleader's Russian citizenship and the Conti antecedent are noted as attribution facts in prose only — the Russian Federation is **not** a cooperating LE jurisdiction in this action and is therefore excluded from `participating_countries` per L24.

## Legal Framework

- **Substantive German charges**: formation of a criminal organization (§ 129 StGB), commercial-and-gang extortion (gewerbs- und bandenmäßige Erpressung, §§ 253, 263a in conjunction with § 263 (3) StGB) and computer sabotage (Computersabotage, § 303b StGB). The BKA release names these offence categories without citing specific paragraph numbers.
- **Ukrainian execution authority**: searches in Ivano-Frankivsk and Lviv regions and an earlier search near Kharkiv were carried out under Ukrainian criminal procedure with the Office of the Prosecutor General of Ukraine as the supervising authority. Specific articles of the Ukrainian Criminal Code are not enumerated in the BKA release.
- **Cross-border channel**: the BKA describes the cooperation as *international coordinated investigations* supplemented by *independent investigations of the Ukrainian National Police* — implying both [[mutual-legal-assistance|mutual legal assistance]] requests (for the search authorities) and parallel domestic Ukrainian proceedings. No specific JIT or Eurojust-coordinated channel is named in this release.
- **Public manhunt vector**: Europol Most Wanted (eumostwanted.eu) and Interpol public-notice channels.

> [!warning] Legal status check needed
> The BKA release is dated 2026-01-15. Several elements (custody status of the two Ukrainian suspects, status of any extradition request for the named ringleader, formal Ukrainian criminal-procedure articles invoked) are not specified and may have evolved. Re-verify before citing custody or charge details in downstream work.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2022-03 → 2025-02 | Black Basta active period; >100 German victims and ≈600 additional global organizations attributed; proceeds in three-digit-millions EUR (>EUR 20 million from Germany alone) | BKA 2026-01-15 |
| Late 2025-08 | Ukrainian officials, at ZIT/BKA's request, search the residence of an alleged crypter near Kharkiv; evidence seized and suspect questioned | BKA 2026-01-15 |
| 2026-01 (on/before publication) | Two residences searched in Ivano-Frankivsk and Lviv regions of Ukraine; Ukrainian-citizen suspects accused of hash-cracking; evidence seized | BKA 2026-01-15 |
| 2026-01-15 | ZIT and BKA publicly announce arrest warrant against the alleged Russian-citizen ringleader of Black Basta; public manhunt activated through Europol Most Wanted and Interpol channels | BKA 2026-01-15 |

## Results and Impact

- **Public arrest warrant** for the alleged Black Basta ringleader (Russian citizen with prior Conti links) issued by ZIT and BKA; suspect is publicly wanted via BKA Öffentlichkeitsfahndung 69 + Europol/Interpol Most Wanted publications.
- **Two Ukrainian search-and-seizure actions** (Ivano-Frankivsk and Lviv regions) executed against suspected Black Basta hash-crackers; evidence seized; custody status not stated in this release.
- **Earlier Kharkiv-area search** (Aug 2025) executed at ZIT/BKA's request against a suspected crypter; evidence seized and suspect questioned.
- **No publicly reported infrastructure takedown, server seizure, domain seizure, decryption-key recovery or large-scale arrest sweep** in this specific BKA release. Reporting frame is investigative continuation rather than infrastructure-takedown action day.
- **Attributional scope** disclosed by BKA: >100 German extortion victims plus ≈600 additional organizations worldwide between March 2022 and February 2025; proceeds in the three-digit-million-EUR range, including >EUR 20 million from Germany alone.

## Cooperation Mechanisms Used

The mechanisms publicly named in or directly inferable from the BKA release are:
- [[europol-ec3|Europol]] support for the public manhunt and operational coordination among the Western European cooperating LE counter-parties.
- [[interpol|Interpol]] public-notice publication channel ("Internationale Fahndungen von Europol und Interpol").
- [[mutual-legal-assistance|Mutual legal assistance]] / inter-prosecutorial channel between the Frankfurt am Main ZIT and the Office of the Prosecutor General of Ukraine for the Ukrainian search authorities.
- Bilateral / informal LE-to-LE cooperation among ZIT/BKA, fedpol/Bundesanwaltschaft, NHTCU and SEROCU prior to the action day. The release does not specifically name a Joint Investigation Team, an Eurojust-coordinated case file, or a CLOUD Act / European Investigation Order.

## Challenges and Friction Points

- The alleged ringleader's Russian citizenship and presumed location in a non-cooperating jurisdiction make immediate apprehension highly unlikely; the realistic enforcement vector is therefore the **public manhunt + travel-restriction** posture (Europol Most Wanted, Interpol notices) rather than direct extradition.
- Ukraine continues to operate as the principal cooperating jurisdiction for ransomware-affiliate enforcement against eastern-Slavic-language operators despite ongoing wartime conditions; this confirms (consistent with [[operation-endgame|Operation Endgame]] and adjacent investigations) that Ukrainian Cyber Police capacity for German-led ransomware cases has remained operational.
- The BKA release does not enumerate specific Joint Investigation Team, Eurojust-coordinated case file, or European Investigation Order — the cross-border channel is described in informal terms ("international coordinated investigations" plus "independent investigations" of the Ukrainian authorities).

## Lessons Learned

- The Frankfurt am Main ZIT continues to function as the German prosecutorial focal point for ransomware international cooperation cases (cf. Operation Endgame, the 2026-05 Crimenetwork relaunch takedown, and the 2026-03 Aisuru/Kimwolf botnet action).
- Multi-jurisdictional coalitions of (DE + NL + CH + UK + UA) without a named Joint Investigation Team continue to be a viable governance form for ransomware investigations targeting Western European industrial victims.
- The dual structure — German-led prosecutorial backbone + Ukrainian executive search authority — appears to be a stable operating model for ransomware affiliate enforcement.

## Follow-Up Actions

- Custody and charge status of the two Ukrainian suspects in Ivano-Frankivsk and Lviv to be tracked.
- Status of the public manhunt against the alleged Russian-citizen ringleader (Europol Most Wanted entry).
- Possible parallel actions or indictments by the United States (Black Basta has been the subject of [[us-doj|US Department of Justice]] and Treasury attention in earlier reporting cycles outside this release).

## Korean Involvement (한국의 참여)

The BKA release does not name the Republic of Korea or any Korean agencies. Black Basta has previously been reported as having impacted multiple Korean enterprise victims in open-source threat reporting, but no Korean-LE participation is asserted in this 2026-01-15 action.

## Contradictions & Open Questions

- The BKA release names "Strafverfolgungsbehörden aus den Niederlanden, der Schweiz, der Ukraine und dem Vereinigten Königreich" (LE authorities from Netherlands, Switzerland, Ukraine, UK) at the top, then later enumerates fedpol + Bundesanwaltschaft (CH), NHTCU (NL), SEROCU (UK), Ukrainian Cyber Police + Prosecutor General's Office (UA). No additional EU member-state LE counter-parties are named — secondary reporting that adds further countries is not asserted on this page.
- The release does not specify the Bundesanwaltschaft's specific case docket, NHTCU operational naming, or SEROCU operational naming — the German release uses each agency by its institutional name only.
- The Aug 2025 Kharkiv-area search and the Jan 2026 Ivano-Frankivsk / Lviv searches are described as part of an *ongoing cooperation* but the formal legal vehicle (MLAT vs. bilateral LE channel vs. JIT) is not enumerated.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-01-15_bka-de_fahndung-nach-kopf-der-ransomware-gruppierung-black-basta\|Fahndung nach Kopf der Ransomware-Gruppierung „Black Basta"]] | Bundeskriminalamt (BKA) | 2026-01-15 | https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2026/Presse2026/260115_PM_Black_Basta.html |
