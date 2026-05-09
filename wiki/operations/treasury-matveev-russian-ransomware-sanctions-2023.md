---
type: operation
title: "Treasury OFAC Sanctions and DOJ Indictments of Mikhail Matveev (2023)"
aliases:
  - "OFAC Matveev designation"
  - "Treasury JY-1486"
  - "Matveev sanctions and indictment"
case_id: CYB-2023-099
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - asset-freeze
  - indictment
outcome: success
timeframe:
  announced: 2023-05-16
  start: 2023-05-16
  end: 2023-05-16
  ongoing: false
crime_types:
  - "[[ransomware-ic]]"
crime_type: ransomware-ic
target_entity: "Mikhail Pavlovich Matveev (Russian national; aliases include 'Wazawaka', 'm1x', 'Boriselcin', 'Uhodiransomwar') — described by Treasury as a key actor in the development and deployment of the LockBit, Babuk, and Hive ransomware variants"
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[us-doj]]"
  - "[[fbi]]"
legal_basis:
  - "Executive Order 13694 (April 1, 2015), section 1(a)(ii)(C), as amended by E.O. 13757 (December 28, 2016) — blocking property of persons engaging in significant malicious cyber-enabled activities"
  - "U.S. Department of State Transnational Organized Crime Rewards Program (22 U.S.C. § 2708, Narcotics Rewards Program / TOCRP authority)"
  - "U.S. federal criminal statutes underlying the unsealed District of New Jersey and District of Columbia indictments (Computer Fraud and Abuse Act and conspiracy/wire-fraud charges, per parallel DOJ filings)"
mechanisms_used: []
results:
  arrests: 0
  indictments: 2
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "OFAC SDN List designation of Mikhail Matveev (2023-05-16)"
    - "Two unsealed federal indictments (U.S. District Court for the District of New Jersey; U.S. District Court for the District of Columbia)"
    - "U.S. Department of State reward of up to USD 10 million offered under the Transnational Organized Crime Rewards Program"
edges: []
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific count of victim organizations attributable to Matveev"
  - "cryptocurrency seizure / asset freezing totals (none disclosed in JY-1486)"
  - "wallet identifiers (published in OFAC Recent Actions 20230516, not transcribed in this ingest)"
related_cases: []
related_operations:
  - "[[operation-cronos-phase1]]"
  - "[[hive-ransomware-takedown]]"
challenges_encountered: []
lessons_learned:
  - "When the suspect is in a non-cooperative jurisdiction, the U.S. defaults to a parallel-track posture: administrative sanctions + criminal indictment + reward offer, rather than relying on MLA / extradition."
  - "OFAC designations operate as financial-isolation tools that are independent of physical custody and do not require host-state cooperation."
source_count: 1
sources:
  - "[[2023-05-16_treasury_matveev-russian-ransomware-actor-sanctions-jy1486]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional / single-source
> This operation page is published below the preferred 5-source threshold because the Treasury press release is itself a tier-1 primary source for the administrative action it announces. Enrichment from the parallel DOJ-NJ and DOJ-DC indictments and from the State Department Rewards for Justice listing is anticipated.

# Treasury OFAC Sanctions and DOJ Indictments of Mikhail Matveev (2023)

## Summary

On **2023-05-16**, the U.S. Department of the Treasury's Office of Foreign Assets Control ([[us-treasury|OFAC]]) designated Russian national **Mikhail Pavlovich Matveev** to the Specially Designated Nationals and Blocked Persons (SDN) List under [Executive Order 13694, as amended by E.O. 13757](https://home.treasury.gov/news/press-releases/jy1486), for cyber-enabled activity targeting U.S. law enforcement, businesses, and critical infrastructure (Treasury press release JY-1486). On the same day, the [[us-doj|U.S. Department of Justice]] unsealed two parallel federal indictments — one in the **U.S. District Court for the District of New Jersey** and one in the **U.S. District Court for the District of Columbia** — and the U.S. Department of State announced a reward of up to **USD 10 million** under its Transnational Organized Crime Rewards Program for information leading to Matveev's arrest and/or conviction.

Treasury characterizes Matveev as a "central figure in the development and deployment of the Hive, LockBit, and Babuk ransomware variants, among others," with attribution to a 2021 Babuk affiliate attack on the police department of a major U.S. city. The action is highly likely an example of the **administrative-plus-criminal parallel-track pattern** that the United States deploys when the suspect is located in a jurisdiction (here, Russia) from which extradition is not realistically available.

## Background

The release situates Matveev within a broader U.S. government posture toward Russia-linked ransomware. Treasury cites Financial Crimes Enforcement Network ([FinCEN](https://www.fincen.gov/sites/default/files/2022-11/Financial%20Trend%20Analysis_Ransomware%20FTA%202_508%20FINAL.pdf)) data attributing 75% of ransomware-related incidents reported July–December 2021 to Russia, its proxies, or persons acting on its behalf, and notes that the Hive variant alone had targeted more than 1,500 victims in over 80 countries before its [[hive-ransomware-takedown|January 2023 disruption]].

Matveev is also described as having been "vocal about his illegal activities" — giving public media interviews, releasing exploit code, and stating that his activities would be tolerated by local authorities so long as he remained loyal to Russia. This open posture is itself the evidentiary basis Treasury foregrounds for the designation.

## Participating Parties

| Role | Entity |
|---|---|
| Lead designating authority | [[us-treasury\|U.S. Department of the Treasury]] (OFAC) |
| Concurrent prosecuting authority | [[us-doj\|U.S. Department of Justice]] (USAO-NJ and USAO-DC) |
| Investigative agency | [[fbi\|U.S. Federal Bureau of Investigation]] (referenced indirectly via the Treasury-DOJ tri-track action) |
| Reward-issuing authority | U.S. Department of State (Transnational Organized Crime Rewards Program) |
| Country whose institutions acted | [[united-states]] |
| Country of nexus to the target | [[russia]] (Matveev's location and nationality) |

## Legal Framework

- **Executive Order 13694** (April 1, 2015) — *Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities* — as amended by **E.O. 13757** (December 28, 2016). OFAC invoked **section 1(a)(ii)(C)**, which addresses cyber-enabled activity reasonably likely to cause significant disruption to the availability of a computer or network of computers.
- **Transnational Organized Crime Rewards Program** (TOCRP), administered by the U.S. Department of State, authorising rewards of up to USD 25 million (Matveev offered up to USD 10 million).
- The two **unsealed federal indictments** (D.N.J. and D.D.C., 2023-05-16) — referenced but not detailed in JY-1486; their specific charging statutes are documented on the parallel DOJ press pages, not on Treasury's.

> [!note] Legal status check needed
> The specific charging statutes in the District of New Jersey and District of Columbia indictments are not transcribed in this Treasury source. Subsequent ingest of the DOJ press releases (DOJ-NJ and DOJ-DC, 2023-05-16) is required to populate the criminal-statute layer.

## Operational Timeline

- **2021** — Babuk ransomware affiliates linked to Matveev attack the police department of a major U.S. city; he claims responsibility in a public interview.
- **July–December 2021** (FinCEN reporting window) — 75% of U.S. reported ransomware incidents are linked to Russia or its proxies, contextualizing later targeting of Matveev.
- **2023-05-16** — OFAC designation announced (JY-1486); D.N.J. and D.D.C. indictments unsealed; State Department TOCRP USD-10M reward announced — all on the same day.

## Results and Impact

| Outcome dimension | Status |
|---|---|
| Arrests | 0 — Matveev remains in Russia (highly likely; not announced in JY-1486 and consistent with the reward-offer posture) |
| Indictments | 2 (D.N.J. and D.D.C., unsealed 2023-05-16) |
| Sanctions | 1 individual added to OFAC SDN List under E.O. 13694, as amended |
| Reward | Up to USD 10 million offered by U.S. Department of State (TOCRP) |
| Asset seizure | None disclosed in JY-1486 |

The action's primary measurable effect is **financial isolation**: U.S. persons are prohibited from dealing with Matveev's property, virtual currency wallets associated with him are subject to OFAC blocking, and ransomware payments to him expose payers to secondary sanctions risk under OFAC's [October 2020 / September 2021 Updated Advisory on Potential Sanctions Risk for Facilitating Ransomware Payments](https://ofac.treasury.gov/media/912981/download?inline) referenced in the release.

## Cooperation Mechanisms Used

This action is, by design, **predominantly U.S.-unilateral**. The mechanisms identifiable from JY-1486 are:

1. **Inter-agency coordination within the U.S. executive branch** — Treasury OFAC, DOJ (two USAOs), FBI, and State Department coordinated a same-day tri-track action.
2. **Inter-court coordination** — the District of New Jersey and District of Columbia indictments were unsealed simultaneously to align with the OFAC designation.

Treasury's release does not name any foreign cooperating agency for this specific action — consistent with the assessment (almost certainly correct) that this action targets a target in a non-cooperative jurisdiction and therefore relies on tools that do not require host-state assent.

## Challenges and Friction Points

- **Russia haven**: Treasury explicitly characterizes Russia as "a haven for ransomware actors." Matveev's own public statements (cited in JY-1486) describe an implicit non-prosecution understanding with local authorities conditional on loyalty to Russia. This makes extradition unlikely (highly likely assessment).
- **Practical reach of E.O. 13694**: Designation blocks U.S.-jurisdiction property only; assets held outside U.S. financial channels are unaffected unless secondary jurisdictions follow suit.
- **No host-state cooperation pathway**: Conventional [[mlat-process|MLAT]]-style requests are not viable in this scenario, and the [[budapest-convention|Budapest Convention]]'s 24/7 Network is unavailable to the United States vis-à-vis Russia, which has historically been outside the Budapest framework.

## Lessons Learned

1. The 2023 Matveev action establishes a template — already used in earlier ransomware sanctions (e.g., Evil Corp, 2019; TrickBot/Conti members, 2023) — for **simultaneous OFAC + DOJ + State reward** moves against suspects in non-cooperative jurisdictions.
2. Multi-variant attribution (Hive + LockBit + Babuk) on a single individual signals an analytic shift: U.S. agencies now publicly link individuals to ransomware *ecosystems* rather than only to single brands, enabling sanctions to apply across multiple ongoing investigations.
3. The action interlocks with later cooperative takedowns of the same ransomware brands ([[hive-ransomware-takedown]] in January 2023; [[operation-cronos-phase1]] in February 2024) — the 2023 designation pre-positions financial-isolation pressure that international takedown operations later exploit.

## Follow-Up Actions

- Subsequent OFAC actions targeting LockBit affiliates and operators (2024) build on the 2023 Matveev designation by designating additional individuals under the same E.O. 13694 authority — likely; to be cross-referenced as those ingests are completed.
- The TOCRP reward offer remains outstanding as of the publish date (no public arrest reported in the source).

## Korean Involvement (한국의 참여)

JY-1486 does not name South Korea ([[south-korea]]) or any Korean agency among participants. There is no direct Korean involvement in this U.S.-unilateral administrative action.

The relevance for Korean practice is **secondary but real**: South Korean financial institutions and virtual-asset service providers operating in or transiting U.S. dollars are subject to OFAC's secondary-sanctions regime. The Korean Financial Intelligence Unit (KoFIU) and Financial Services Commission–supervised reporting entities are highly likely to treat OFAC SDN designations such as Matveev's as automatic triggers for screening — even though no Korean enforcement or MLA action arises from the U.S. designation itself.

> [!note] Translation note
> "Specially Designated Nationals and Blocked Persons List" is rendered in Korean financial-compliance practice as "특별지정제재대상자 명단" (SDN 명단). Korean financial-sector compliance treats inclusion on this list as a hard screening rule.

## Contradictions & Open Questions

- The Treasury press release identifies Matveev as central to **three** ransomware variants (Hive, LockBit, Babuk). The relative weight of his role in each is not quantified, and subsequent operations against each variant attributed leadership to other named individuals. **Open question**: was Matveev a developer, an affiliate, an operator-broker, or some combination across the three brands? JY-1486 does not resolve this.
- JY-1486 announces the existence of the D.N.J. and D.D.C. indictments but does not specify charges. **Open question**: which statutes were charged in each district, and were the two indictments based on overlapping or distinct conduct? The parallel DOJ press releases (separate ingests) are required to answer this.
- No cryptocurrency-wallet identifiers or victim counts attributable specifically to Matveev are published in JY-1486 (these appear in the linked OFAC "Recent Actions 20230516" page). **Open question**: how many distinct intrusions and what total ransom volume does OFAC attribute to Matveev personally, as opposed to the Hive/LockBit/Babuk ecosystems collectively?
- No outstanding asset-freezing totals are disclosed. **Open question**: did any U.S.-jurisdiction blocked property exist at the time of designation, or was the action prospective?

## Sources

- [[2023-05-16_treasury_matveev-russian-ransomware-actor-sanctions-jy1486|Treasury JY-1486 (2023-05-16)]]
