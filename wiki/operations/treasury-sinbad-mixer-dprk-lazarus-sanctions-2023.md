---
type: operation
title: "Treasury Sanctions Sinbad.io Virtual Currency Mixer for Laundering DPRK Lazarus Group Heists (November 2023)"
title_ko: "Sinbad.io 가상화폐 믹서 미 재무부 제재 — DPRK 라자루스 그룹 자금세탁 (2023년 11월)"
aliases:
  - "OFAC JY-1933 Sinbad.io Designation"
  - "Sinbad.io Mixer Sanctions 2023"
  - "Treasury Sinbad DPRK Lazarus Mixer Action"
case_id: CYB-2023-100
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - asset-freeze
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2023-11-29
  start: ""
  end: 2023-11-29
  ongoing: false
crime_type: "[[money-laundering-ic]]"
crime_types:
  - "[[money-laundering-ic]]"
  - "[[ransomware-ic]]"
target_entity: "Sinbad.io — a Bitcoin-based virtual currency mixer described by OFAC as a 'preferred mixing service' for the DPRK Lazarus Group, used to launder a significant portion of three major DPRK cryptocurrency heists totaling approximately $820 million: the Axie Infinity / Ronin Bridge heist ($620M, March 2022), the Horizon Bridge heist ($100M, June 2022), and the Atomic Wallet heist ($100M, June 3, 2023). Sinbad is also documented as serving non-state cybercriminals for sanctions evasion, drug trafficking, CSAM purchases, and darknet marketplace transactions."
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[north-korea]]"
participating_agencies:
  - "[[us-treasury]]"
organizations:
  - "[[us-treasury]]"
mechanisms_used:
  - "[[asset-freezing]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Executive Order 13694 (as amended by E.O. 13757) — Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities"
  - "Executive Order 13722 — Blocking the Property of the Government of North Korea and the Workers' Party of Korea, and Prohibiting Certain Transactions With Respect to North Korea"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 entity designated: Sinbad.io (Sinbad), a Bitcoin-based virtual currency mixer"
    - "All Sinbad.io property and interests in property in U.S. jurisdiction blocked under SDN List inclusion"
    - "Sinbad linked to laundering significant portions of three DPRK heists: Atomic Wallet ($100M, 2023-06-03), Axie Infinity ($620M, March 2022), Horizon Bridge ($100M, June 2022)"
    - "Cumulative DPRK Lazarus Group theft figure cited by Treasury: over $2 billion in digital assets across multiple thefts in 10+ years"
    - "Secondary sanctions exposure flagged for non-U.S. persons transacting with Sinbad"
    - "Designation extends OFAC's mixer-targeting enforcement pattern: Blender.io (2022-05-06) → Tornado Cash redesignation (2022-11-08) → DPRK-linked OTC traders (2023-04-24) → Sinbad.io (2023-11-29)"
edges:
  - source_actor: us-treasury
    target_actor: north-korea
    cooperation_type: asset_recovery
    legal_basis: e.o.-13694-13722
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "cryptocurrency_seized (release announces blocking of property/interests but does not state on-chain seizure dollar amount)"
  - "identity of operators/jurisdiction of Sinbad.io infrastructure (the entity is sanctioned without naming a host country or natural persons)"
  - "specific partner-state actions concurrent with this designation (e.g., whether South Korea, Japan, or EU coordinated)"
  - "post-designation outcome of Sinbad.io domain/service availability (release does not record domain seizure or operator arrest)"
related_cases: []
related_operations:
  - "[[treasury-sanctions-dprk-bankers-laundering-cybercrime-2025]]"
  - "[[treasury-sanctions-dprk-it-worker-network-andreyev-chinyong-2025]]"
  - "[[treasury-matveev-russian-ransomware-sanctions-2023]]"
  - "[[de-ch-crypto-mixer-takedown-2025]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
  - "[[extraterritorial-jurisdiction]]"
lessons_learned:
  - "Virtual-currency mixer designations are a primary OFAC tool against state-sponsored crypto theft laundering pathways, and form an iterative enforcement sequence (Blender → Tornado Cash → Sinbad) where each successor service is designated after replacing its predecessor."
  - "A single mixer can be tied to multiple discrete state-sponsored heists (Sinbad: Axie Infinity + Horizon Bridge + Atomic Wallet), making mixer-level designation a high-leverage chokepoint compared with chasing individual transactions."
  - "Secondary-sanctions exposure for non-U.S. persons is the principal indirect lever for offshore mixers; absent a host-jurisdiction takedown, a designation alone does not seize infrastructure."
  - "Mixer designations target a multi-purpose laundering vehicle: state-sponsored cyber theft funds and ordinary cybercriminal proceeds (drug trafficking, CSAM, darknet sales) are commingled in the same service, so the IC benefit accrues across multiple crime types simultaneously."
source_count: 1
sources:
  - "[[2023-11-29_treasury_sinbad-mixer-dprk-lazarus-virtual-currency-laundering-jy1933]]"
created: 2026-05-09
updated: 2026-05-09
---
> [!info] Provisional page
> This operation page is published from a single tier-1 source (OFAC press release JY-1933). Per the project's preferred publication threshold (`source_count >= 5`), it is treated as provisional pending corroborating sources (Chainalysis/TRM Labs blockchain analysis, Justice Department companion actions, partner-state designations, follow-on Atomic Wallet / Axie Infinity / Horizon Bridge prosecution documents).

## Summary

On 2023-11-29, the U.S. Department of the Treasury's Office of Foreign Assets Control ([[us-treasury|OFAC]]) issued press release JY-1933, designating Sinbad.io — a Bitcoin-based virtual-currency mixer — as a "key money-laundering tool" of the previously-designated DPRK [[north-korea|Lazarus Group]]. The release ties Sinbad to laundering significant portions of three high-profile DPRK cryptocurrency heists totaling approximately $820 million across 2022–2023: the Axie Infinity / Ronin Bridge heist ($620M, March 2022), the Horizon Bridge heist ($100M, June 2022), and the Atomic Wallet heist ($100M, 2023-06-03). Designation is made under Executive Orders 13694 (as amended by E.O. 13757) for cyber-enabled malicious activity and E.O. 13722 for materially supporting the DPRK government. The action is described by industry observers as targeting a highly likely successor to Blender.io, the first-ever virtual-currency mixer designated by OFAC in May 2022.

## Background

The Lazarus Group is a state-sponsored cyber actor of the DPRK, formally designated by OFAC on 2019-09-13 under E.O. 13722 as an agency, instrumentality, or controlled entity of the Government of North Korea. Per the JY-1933 release, the group has operated for more than ten years and is "believed to have stolen over $2 billion worth of digital assets across multiple thefts," with revenue applied to DPRK weapons of mass destruction (WMD) and ballistic missile programs.

By late 2023, OFAC had developed a recurring enforcement pattern targeting the virtual-currency laundering infrastructure used by Lazarus Group:

- **2022-05-06** — OFAC sanctioned Blender.io, the first-ever virtual-currency mixer designation.
- **2022-11-08** — OFAC redesignated Tornado Cash for providing mixing services to Lazarus Group.
- **2023-04-24** — OFAC sanctioned two over-the-counter virtual-currency traders who facilitated conversion of stolen virtual currency to fiat for DPRK actors working with Lazarus Group.
- **2023-11-29** — OFAC sanctioned Sinbad.io (this action). Industry experts believe Sinbad is highly likely a successor to Blender.io.

Sinbad's mixer-as-money-laundering-vehicle pattern for state-sponsored cyber theft is the operational core of this action: a single Bitcoin-based mixing service is tied directly to three discrete heists ($620M + $100M + $100M = $820M cumulative laundering nexus) attributable to a single state-sponsored actor.

## Participating Parties

- **Lead/coordinating agency:** [[us-treasury|U.S. Department of the Treasury (OFAC)]].
- **Country jurisdiction of action:** [[united-states]] (designating authority).
- **Subject jurisdiction of designee:** [[north-korea]] (Sinbad designated as a money-laundering tool of the DPRK Lazarus Group; the release does not state Sinbad's operator nationality or infrastructure host country).

The release does not name specific cooperating foreign agencies. Treasury Deputy Secretary Wally Adeyemo's statement references "U.S. government partners" generically, which is unlikely to indicate any single named foreign government coordinated this designation.

## Legal Framework

The legal authorities cited verbatim in the release are:

- **E.O. 13694** (as amended by **E.O. 13757**) — "Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities." Sinbad designated for "having materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services to or in support of a cyber-enabled activity" with significant economic harm.
- **E.O. 13722** — "Blocking the Property of the Government of North Korea and the Workers' Party of Korea, and Prohibiting Certain Transactions With Respect to North Korea." Sinbad additionally designated for materially supporting the DPRK Government (a person blocked under E.O. 13722, by reference to the prior 2019 Lazarus Group designation).

The release does **not** invoke E.O. 13551 or E.O. 13810 (DPRK financial-network authorities used in the 2025 DPRK banker designations) and does **not** invoke E.O. 13687. The designation frames Sinbad as a cyber-enabled and DPRK-government-supporting target, not as a DPRK financial institution as such.

> [!note] Legal precision
> E.O. 13694 was amended by E.O. 13757 (2017-01-03) to expand cyber-enabled designation authority. The release cites E.O. 13694 "as amended by E.O. 13757" — both texts must be read together for the operative authority.

## Operational Timeline

| Date | Event |
|---|---|
| 2019-09-13 | OFAC designates Lazarus Group under E.O. 13722 as a DPRK government instrumentality. |
| 2022-03 | Axie Infinity / Ronin Bridge heist (~$620M); Lazarus Group attribution by U.S. authorities. |
| 2022-05-06 | OFAC sanctions Blender.io — first-ever virtual-currency mixer designation, used by Lazarus Group. |
| 2022-06 | Horizon Bridge heist (~$100M); attributed to Lazarus Group. |
| 2022-11-08 | OFAC redesignates Tornado Cash (mixer used by Lazarus Group). |
| 2023-04-24 | OFAC sanctions two OTC virtual-currency traders facilitating fiat conversion for DPRK actors. |
| 2023-06-03 | Atomic Wallet heist (~$100M); subsequently attributed in part to Lazarus Group. |
| 2023-11-29 | **OFAC press release JY-1933 — Sinbad.io designated** (this operation). |

## Results and Impact

Per the verbatim release:

- **1 entity designation**: Sinbad.io (Sinbad).
- **All property and interests in property** of Sinbad in U.S. jurisdiction or under U.S. person control are **blocked** and must be reported to OFAC.
- **All dealings by U.S. persons or within the United States** that involve any property or interests in property of Sinbad are generally prohibited.
- **Secondary-sanctions exposure** flagged for non-U.S. persons transacting with Sinbad.
- **Compliance enrichment** — designation supports virtual-asset service provider screening (likely accompanied by SDN List entry with cryptocurrency addresses, though the press release itself does not enumerate them; identification page referenced separately).

The release does not state a specific dollar amount of frozen U.S. assets. The dollar figures cited (Atomic Wallet $100M, Axie Infinity $620M, Horizon Bridge $100M) describe upstream stolen-funds volumes laundered through Sinbad, not seized amounts.

## Cooperation Mechanisms Used

- **[[asset-freezing]]** — primary mechanism; SDN List blocking action triggers U.S. jurisdictional asset freeze for Sinbad and any property/interests under U.S. person control.
- **[[informal-cooperation]]** — the release alludes generally to "U.S. government partners" and references the 2020 DPRK Cyber Threat Advisory (a Treasury / [[fbi|FBI]] / CISA joint product). This is unlikely to constitute formal mutual legal assistance; rather, it indicates an interagency informal-coordination posture supporting the designation.

The release does not document any formal MLAT request, extradition, or joint investigation. Sinbad.io infrastructure host jurisdiction is not stated, so this designation operates as a unilateral U.S. action with extraterritorial reach via secondary sanctions exposure.

## Challenges and Friction Points

- **[[jurisdictional-conflicts]]** — Virtual-currency mixers operate without a stated host jurisdiction, complicating direct enforcement. OFAC designation is a U.S.-jurisdiction blocking action; without a parallel host-country takedown of Sinbad's infrastructure, the service can technically continue to operate from non-cooperating jurisdictions, with the principal U.S. lever being secondary-sanctions exposure for participants.
- **[[extraterritorial-jurisdiction]]** — Secondary sanctions on non-U.S. persons transacting with Sinbad are the indirect mechanism by which the designation exerts cross-border effect. This raises standard tensions around U.S. extraterritorial assertion of sanctions jurisdiction over foreign actors.
- **Mixer infrastructure resilience** — Industry experts cited in the release believe Sinbad is highly likely a successor to the previously-designated Blender.io, indicating that designation alone does not eliminate DPRK access to mixing services; successor mixers can be expected to emerge.
- **Multi-purpose laundering vehicle** — The release explicitly notes Sinbad serves not only Lazarus Group but also non-state cybercriminals laundering proceeds from drug trafficking, CSAM purchases, and darknet sales. This means designation produces benefit across multiple crime types but also creates collateral disruption to ordinary criminal-laundering markets that may shift to alternative mixers.

## Lessons Learned

- Mixer-level OFAC designation is a high-leverage chokepoint when a single laundering vehicle is tied to multiple discrete state-sponsored heists. Sinbad's role across three Lazarus heists (Axie Infinity + Horizon Bridge + Atomic Wallet) made designating the mixer more efficient than chasing transaction-by-transaction asset freezes.
- The Blender → Tornado Cash → Sinbad enforcement sequence demonstrates that DPRK laundering networks adapt by migrating to successor services. Sustained iterative designation is highly likely required, not one-time enforcement.
- Secondary-sanctions exposure is the principal indirect lever for offshore mixers absent a host-state takedown.
- A multi-purpose laundering vehicle generates IC benefit across multiple crime types simultaneously: a single Sinbad designation disrupts state-sponsored cyber theft laundering, sanctions evasion, drug trafficking proceeds, CSAM purchases, and darknet trade in one action.

## Follow-Up Actions

The release indicates that OFAC and "U.S. government partners stand ready to deploy all tools at their disposal to prevent virtual currency mixers, like Sinbad, from facilitating illicit activities." Subsequent OFAC actions against DPRK-linked financial enablers (e.g., the 2025 DPRK bankers and IT-worker network designations — see [[treasury-sanctions-dprk-bankers-laundering-cybercrime-2025]] and [[treasury-sanctions-dprk-it-worker-network-andreyev-chinyong-2025]]) are highly likely part of the same sustained-pressure campaign. Parallel enforcement against future successor mixers is highly likely over the medium term given the Blender → Sinbad replacement pattern.

## Korean Involvement (한국의 참여)

The release does not document direct involvement by [[south-korea]] (ROK) law enforcement or financial regulators in this U.S. action. South Korea is highly likely to have substantial investigative interest in Sinbad-laundered DPRK funds for two reasons:

- The Axie Infinity / Ronin Bridge developer (Sky Mavis) has Asian-Pacific operations, and South Korean victims are common in DPRK-linked crypto thefts.
- South Korea is among the principal targets of DPRK cyber-enabled financial theft and has its own sanctions and AML enforcement against DPRK actors.

Whether ROK financial intelligence (KoFIU) or law enforcement provided informal information sharing supporting the JY-1933 designation is roughly even chance to have occurred but is not documented in this primary source. Korean translation of the action will commonly use 가상화폐 믹서 (virtual currency mixer) and 라자루스 그룹 (Lazarus Group); the term 자금세탁 (money laundering) maps directly to the OFAC framing.

## Contradictions & Open Questions

- **Sinbad operator identity and host jurisdiction** — The release sanctions the Sinbad.io entity but does not name natural persons operating it nor identify the infrastructure host country. Subsequent industry analyses are needed to verify operator identification.
- **Successor-to-Blender.io claim** — The release states industry experts "believe" Sinbad to be a successor to Blender.io. This is highly likely but explicitly hedged; on-chain forensic confirmation (e.g., Chainalysis or TRM Labs analysis) would strengthen this claim.
- **Atomic Wallet attribution** — As of the JY-1933 release date (2023-11-29), the Atomic Wallet $100M heist (2023-06-03) is implicitly tied to Lazarus Group via Sinbad's role; explicit U.S. government attribution of the Atomic Wallet heist itself to Lazarus Group is not stated in this release.
- **Partner-state coordination** — The release does not document concurrent partner-state designations. Whether the EU, UK, Japan, or South Korea issued parallel designations of Sinbad or its operators is roughly even chance to have occurred and warrants cross-checking.
- **Effect on Sinbad service availability** — The release is a designation only, not an infrastructure seizure. Whether Sinbad.io domain access or service operation continued post-designation is not addressed.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2023-11-29_treasury_sinbad-mixer-dprk-lazarus-virtual-currency-laundering-jy1933\|Treasury Sanctions Mixer Used by the DPRK to Launder Stolen Virtual Currency]] | US Department of the Treasury (OFAC), Press Release JY-1933 | 2023-11-29 | https://home.treasury.gov/news/press-releases/jy1933 |
