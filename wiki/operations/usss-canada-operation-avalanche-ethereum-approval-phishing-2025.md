---
type: operation
title: "Operation Avalanche (USSS / BC Securities Commission, April 2025) — U.S.–Canada coordinated disruption of an Ethereum 'approval phishing' scam"
title_ko: "Operation Avalanche (미국 비밀경호국 / BC 증권위원회, 2025-04) — 이더리움 'approval phishing' 사기 미·캐 공동 단속"
aliases:
  - "Operation Avalanche 2025"
  - "USSS-BCSC Operation Avalanche"
  - "Ethereum approval phishing operation (USSS, 2025)"
case_id: CYB-2025-997
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - asset_freeze
outcome: partial
timeframe:
  announced: 2025-04-16
  start: ""
  end: ""
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
  - "[[organized-crime-ic]]"
target_entity: "Distributed transnational organized-crime networks running Ethereum-blockchain 'approval phishing' scams: victims were socially engineered (typically as part of a larger 'pig butchering' / investment-fraud scheme) into granting scammers approval permissions on their Ethereum wallets, after which the scammers withdrew funds without the owner's knowledge. The blockchain addresses identified during Operation Avalanche were drained of crypto assets worth an estimated USD 4.3 million; the operation focused on compromised-wallet identification, victim notification, and inter-agency coordination rather than arrests or indictments."
lead_agency: "[[us-secret-service]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[canada]]"
participating_agencies:
  - "[[us-secret-service]]"
  - "[[canada-rcmp]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "USD 4.3 million (estimated value of crypto assets drained from blockchain addresses identified during the operation; the release does not characterise this amount as seized/recovered)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Compromised Ethereum wallet owners notified by Canadian provincial-securities-commission victim-notification programmes (BC Securities Commission, Alberta Securities Commission, L'Autorité des marchés financiers, Ontario Securities Commission) supported by USSS WFO blockchain-analysis personnel"
    - "Operation framed as victim-warning / disruption rather than prosecution; no arrests, no indictments, no asset seizure announced in the tier-1 USSS release"
edges:
  - source_actor: "us-secret-service"
    target_actor: "canada-rcmp"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "us-secret-service"
    target_actor: "bc-securities-commission"
    cooperation_type: "technical_assistance"
    legal_basis: "informal"
    direction: "directed"
credibility_index: 4.2
source_tier: 1
missing_fields:
  - "arrests"
  - "indictments"
  - "victims_notified (specific count)"
  - "legal_basis"
  - "mechanisms_used"
related_cases: []
related_operations:
  - "[[operation-atlantic-approval-phishing-2026]]"
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2025-04-16_secret-service_operation-avalanche-ethereum-approval-phishing-bc-securities]]"
created: 2026-05-16
updated: 2026-05-16
---

## Summary

On 2025-04-16, the U.S. Secret Service (USSS) Washington Field Office publicly disclosed its participation in **Operation Avalanche**, a coordinated U.S.–Canada action led on the Canadian side by the **BC Securities Commission (BCSC)** to identify and notify victims of an "approval phishing" scam operating on the Ethereum blockchain. USSS Investigative and Network Intrusion Forensic Analysts contributed blockchain-analysis capability; Canadian securities regulators and multiple Canadian police forces contributed victim outreach and police authority. The blockchain addresses identified during the operation had been drained of crypto assets worth an estimated **USD 4.3 million**.

> [!note] Operation-name disambiguation
> This operation is **distinct from** [[operation-avalanche|Operation Avalanche (2016)]] — the Europol/Eurojust/U.S. DOJ takedown of the Avalanche fast-flux botnet — and from [[operation-atlantic-approval-phishing-2026|Operation Atlantic (NCA-led, April 2026)]], which is the larger UK-led successor action against approval-phishing/pig-butchering networks. The name "Operation Avalanche" was re-used by Canadian securities regulators and U.S. federal partners in 2025 for a victim-notification programme; the 2026 NCA release describes Atlantic as a co-hosted effort with the U.S. Secret Service and Ontario Provincial Police, suggesting Atlantic 2026 is a scaled-up evolution of the same investigative line.

## Background

"Approval phishing" exploits the smart-contract approval mechanism on the Ethereum blockchain: a victim is socially engineered into signing an approval transaction that grants a scammer's address permission to spend tokens from the victim's wallet. The victim does not lose funds at the moment of approval — funds are drained later, often after the victim has been kept engaged in a long-running "pig butchering" investment-fraud relationship. Approval phishing leaves a discoverable on-chain footprint (approved-but-not-yet-drained allowances), enabling blockchain analysts to identify likely-future victims before the funds are stolen.

The 2025 USSS release frames the operation as the kind of action that "investigative expertise, resources, and long-standing global law enforcement partnerships" make possible against transnational organized-crime cryptocurrency scams.

## Participating Parties

**United States** — [[us-secret-service|U.S. Secret Service]] Washington Field Office (Investigative and Network Intrusion Forensic Analysts); WFO Special Agent in Charge Matt McCool quoted.

**Canada** — Canadian partners explicitly named in the USSS release: the **BC Securities Commission** (lead Canadian agency), the **Ontario Provincial Police**, **Alberta Securities Commission**, **L'Autorité des marchés financiers** (Quebec), **Ontario Securities Commission**, **Delta Police Department**, **Vancouver Police Department**, and the [[canada-rcmp|Royal Canadian Mounted Police]]. Only the RCMP currently has a wiki organization page; the provincial police forces (OPP, Delta PD, Vancouver PD) and the provincial securities commissions (BCSC, ASC, AMF, OSC) are listed here in prose pending entity-page creation when source diversity supports it.

**Private sector** — The release notes participation by "crypto trading platforms and a blockchain analysis firm" without naming them.

> [!info] L24 — participating_countries compliance
> The tier-1 USSS press release explicitly names cooperating LE/regulatory agencies in two jurisdictions: the **United States** (USSS WFO) and **Canada** (RCMP + multiple provincial police and securities commissions). No adversary/origin/destination state is asserted as a participant; the release does not name the geographic origin of the scammers beyond the general phrase "transnational organized crime."

## Legal Framework

The USSS release does not cite a specific bilateral or multilateral framework underlying the cooperation. U.S.–Canada law-enforcement cooperation in financial-cybercrime cases is routinely conducted under informal investigative-agency-to-agency channels (USSS ↔ RCMP), provincial-securities-regulator-to-USSS information sharing, and — where data crosses borders — the U.S.–Canada Mutual Legal Assistance Treaty (1985) and the U.S. CLOUD Act for provider data. The 2025 release does not invoke any of these by name.

## Operational Timeline

- **Pre-April 2025** — On-chain analysis by Canadian regulators identifies Ethereum addresses bearing the approval-phishing signature; USSS WFO analysts are brought in to provide additional blockchain-analysis capacity.
- **April 2025** — Operational phase: compromised wallets identified, owners notified by Canadian provincial-securities-commission victim-outreach programmes; police-side support from OPP, Delta PD, Vancouver PD, RCMP.
- **2025-04-16** — Public disclosure by USSS (Washington Field Office press release).

The release does not specify the precise dates of operational activity, nor the number of wallets or victims contacted.

## Results and Impact

- **USD 4.3 million** — estimated value of crypto assets drained from the blockchain addresses identified during Operation Avalanche. The release does **not** characterise this figure as seized/recovered/frozen; it is the loss figure for the wallets identified.
- **No arrests, indictments, or domain/server seizures** disclosed in the tier-1 USSS release.
- **Victim-notification programme** — the operation's principal output. Specific victim counts are not given.

## Cooperation Mechanisms Used

Informal U.S.–Canada investigative-agency cooperation between USSS WFO and Canadian provincial securities regulators / federal and provincial police forces. The release frames the cooperation through "long-standing global law enforcement partnerships." No formal MLAT request or Budapest Convention provision is invoked in the public communication.

## Challenges and Friction Points

- Cross-border victim-notification at scale: many of the wallets identified belong to retail investors who must be located by jurisdiction (UK/US/Canada — UK explicitly absent from Operation Avalanche 2025, but present in the 2026 Atlantic successor).
- The release does not state whether any funds were recovered for victims — the USD 4.3 million figure is the loss, not a recovery.

## Lessons Learned

- The 2025 USSS release is best read as a **public marker of investigative continuity**: a relatively low-key, single-agency-press-release announcement of an inter-agency operation that, one year later, expanded into the much larger [[operation-atlantic-approval-phishing-2026|Operation Atlantic]] (NCA-led, UK + USSS + Ontario Provincial Police + Ontario Securities Commission). Treating Avalanche-2025 and Atlantic-2026 as a connected investigative line is supported by the partial overlap of named partners (USSS + OPP + OSC + private blockchain-analysis firms) across the two releases.

## Follow-Up Actions

- 2026-04-09 — [[operation-atlantic-approval-phishing-2026|Operation Atlantic]] publicly announced by the U.K. National Crime Agency, reporting USD 12 million frozen and 20,000+ victims identified across the UK, U.S., and Canada in a week-long action co-hosted with USSS, OPP, and OSC.

## Korean Involvement (한국의 참여)

None mentioned in the tier-1 USSS release; the operation is U.S.–Canada bilateral with private-sector blockchain-analysis support. Korean retail investors are common targets of pig-butchering / approval-phishing networks more generally, but no Korean LE participation is asserted here.

## Contradictions & Open Questions

- The USSS release does not state the number of wallets identified, the number of victims notified, the proportion of those victims who were U.S. vs. Canadian residents, or whether any funds were recovered for victims. These should be filled in if/when a corresponding BC Securities Commission, RCMP, or Ontario Provincial Police statement is located.
- The geographic origin of the scammer infrastructure (East Asia / Southeast Asia is the typical pig-butchering origin) is not asserted in the U.S.-side release.
- Whether Operation Avalanche 2025 and Operation Atlantic 2026 are formally the same investigation under different names, or distinct operations along a continuous investigative line, is not stated in either release.

## Audit notes

- **Tier-1 source**: secretservice.gov own-domain press release; retrieved via `curl_cffi` Session(impersonate="chrome124") returning HTTP 200, ~70 KB body.
- **L24 compliance**: ≥2 cooperating LE jurisdictions explicitly named in the primary source (United States — USSS WFO; Canada — RCMP + provincial police + provincial securities commissions). No adversary state included in `participating_countries`.
- **L23 compliance**: `lead_agency` is a verified-existing wikilink ([[us-secret-service]]); `coordinating_body` is empty (the release frames the U.S. side as supporting Canadian-led victim notification rather than naming a single coordinating body); `participating_agencies` lists only verified-existing wikilinks. Canadian provincial agencies are described in prose only.
- **L1**: Source URL fetched and verified to contain the operation described; no filename-vs-content mismatch.
- **L17/L19/L20**: All asserted countries (US, Canada) are verbatim in the tier-1 release.

> [!info] Provisional
> `source_count = 1` at creation. This page is below the preferred publication threshold (≥5 sources). It is retained because the Avalanche-2025 → Atlantic-2026 investigative-line linkage is durable wiki value, and the tier-1 USSS own-domain source is high-reliability/confirmed. Additional Canadian-side sources (BC Securities Commission, RCMP, OPP statements) should be added in future iterations.
