---
type: operation
title: "Treasury Sanctions Targeting Garantex, Grinex, and Russian Sanctions-Evasion Network (August 2025)"
aliases:
  - "OFAC SB-0225"
  - "Garantex re-designation"
  - "Grinex designation"
case_id: CYB-2025-112
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - asset_freeze
outcome: success
timeframe:
  announced: 2025-08-14
  start: 2025-08-14
  end: 2025-08-14
  ongoing: false
crime_types:
  - "[[ransomware-ic]]"
  - "[[money-laundering-ic]]"
crime_type: money-laundering-ic
target_entity: "Garantex Europe OU (re-designated); Grinex (successor exchange); 3 Garantex executives (Sergey Mendeleev, Aleksandr Mira Serda, Pavel Karavatsky); 6 associated companies in Russia and the Kyrgyz Republic (A7 LLC, A71 LLC, A7 Agent LLC, Old Vector, InDeFi Bank, Exved). Ransomware nexus: Conti, Black Basta, LockBit, NetWalker, Phoenix Cryptolocker."
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[us-secret-service]]"
  - "[[fbi]]"
legal_basis:
  []
mechanisms_used:
  - "[[asset-freezing]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 cryptocurrency exchange re-designated (Garantex)"
    - "1 successor cryptocurrency exchange newly designated (Grinex)"
    - "3 individuals designated (Garantex executives)"
    - "6 associated companies designated (Russia and Kyrgyz Republic)"
    - "USD 5 million State Department reward offer for Mira Serda; USD 1 million for other Garantex leaders"
edges:
  - source_actor: us-treasury
    target_actor: us-secret-service
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: us-treasury
    target_actor: fbi
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  []
related_cases:
  []
related_operations:
  - "[[cryptex-pm2btc-sanctions]]"
  - "[[operation-final-exchange-bka-russian-crypto-exchanges-2024]]"
challenges_encountered:
  []
lessons_learned:
  - "Sanctions-evasion infrastructure can be reconstituted within days of an enforcement action; designating successor entities is necessary to close the loophole."
  - "Coordination between cyber-authority sanctions (E.O. 13694) and country-specific sanctions (E.O. 14024) can layer pressure on dual-purpose criminal-state finance networks."
source_count: 1
sources:
  - "[[2025-08-14_treasury_garantex-grinex-russian-network-cyber-criminals-sanctions-evasion]]"
created: 2026-05-09
updated: 2026-05-09
---
> [!info] Provisional page
> This operation page is published below the preferred 5-source threshold (current `source_count: 1`). It is retained because the action is a high-salience tier-1 government primary-source designation that closes a specific sanctions-evasion loophole opened by the March 2025 [[us-secret-service|USSS]]-led Garantex disruption already documented in the wiki. The page should be enriched as additional reporting (Chainalysis, TRM Labs, OFAC SDN list entries, follow-on indictments) becomes available.

## Summary

On 14 August 2025, the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) issued press release SB-0225 announcing a layered sanctions package against the Garantex cryptocurrency exchange ecosystem. The action (1) **re-designated** Garantex Europe OU under E.O. 13694 (cyber authority), supplementing its prior April 2022 designation under E.O. 14024 (Russia financial services sector); (2) **designated Grinex**, the successor exchange created by Garantex employees in the days after the March 2025 law enforcement disruption; (3) designated three Garantex executives (Sergey Mendeleev, Aleksandr Mira Serda, Pavel Karavatsky); and (4) designated six associated companies operating in Russia and the Kyrgyz Republic (A7 LLC, A71 LLC, A7 Agent LLC, Old Vector, InDeFi Bank, Exved) that supported the exchange's role in laundering ransomware proceeds and Russia-linked sanctions evasion.

The action is **highly likely** the most consequential sanctions-side response to the post-disruption migration pattern observed in cryptocurrency exchange enforcement: when an exchange is taken down, customer funds and infrastructure are reconstituted in a successor brand. The August 2025 designation closes that loophole for the Garantex case by sanctioning the successor (Grinex) under the same cyber authority and adding the executives and infrastructure providers who enabled the migration.

## Background

Garantex was founded in late 2019, originally registered in Estonia, with operational center in Moscow and Saint Petersburg. In February 2022 it lost its Estonian digital asset license after Estonia's Financial Intelligence Unit identified AML/CFT deficiencies and links to wallets used for criminal activity. OFAC first designated Garantex on **5 April 2022** under E.O. 14024 for operating in the financial services sector of the Russian Federation. Despite the designation, Garantex continued to operate, developing infrastructure to obscure attribution of cryptocurrency wallet addresses back to the exchange.

According to OFAC, Garantex received millions of dollars in cryptocurrency directly from the proceeds of Russia-linked ransomware operations including **Conti, Black Basta, LockBit, NetWalker, and Phoenix Cryptolocker**, and provided account/exchange services to **Ryuk**-associated actors. OFAC states that over USD 100 million of known Garantex transactions are associated with illicit actors since 2019.

On **6 March 2025**, the U.S. Secret Service (USSS), in partnership with German and Finnish law enforcement, took disruptive measures against Garantex's computer infrastructure, seizing its web domain and freezing over USD 26 million in cryptocurrency. On **7 March 2025**, the U.S. Department of Justice unsealed indictments against Garantex executives Aleksandr Mira Serda and Aleksej Besciokov; Besciokov was subsequently arrested in India. Within days, Garantex officers transferred customer deposits to a newly created exchange, **Grinex**, and used a ruble-backed token (**A7A5**), issued by Kyrgyzstani firm Old Vector for Russian A7 LLC, to compensate customers whose Garantex funds had been frozen. The August 2025 OFAC action targets that reconstitution.

## Designated Targets

**Re-designated entity (added cyber authority):**
- **Garantex Europe OU** — designated under E.O. 13694, as further amended by E.O. 14144 and E.O. 14306 (cyber-enabled malicious activity), in addition to existing E.O. 14024 designation.

**Newly designated entity:**
- **Grinex** — successor cryptocurrency exchange; designated under E.O. 13694 for being owned/controlled by Garantex.

**Newly designated individuals:**
- **Sergey Mendeleev** — Garantex co-founder; controls InDeFi Bank and Exved.
- **Aleksandr Mira Serda** — Garantex co-owner and Chief Commercial Officer; subject of USD 5 million State Department reward.
- **Pavel Karavatsky** — Garantex co-owner and regional director.

**Newly designated companies (6):**
- **A7 Limited Liability Company (A7)** — Russian cross-border settlement platform provider; co-owned by sanctioned Moldovan oligarch Ilan Shor and sanctioned Russian bank Promsvyazbank (PSB).
- **A71 Limited Liability Company** — A7 subsidiary.
- **A7 Agent Limited Liability Company** — A7 subsidiary.
- **Old Vector** — Kyrgyzstani firm; A7A5 token issuer.
- **Independent Decentralized Finance Smartbank and Ecosystem (InDeFi Bank)** — Mendeleev-controlled.
- **Exved** — payment platform facilitating cryptocurrency-mediated cross-border trade for sanctions evasion; Mendeleev-controlled.

## Participating Parties

- [[united-states]] — designating jurisdiction (sole sanctions authority for this action).
- [[russia]] — host jurisdiction of Garantex operations and most designated entities. Russia is **not** a cooperating party; the designation targets actors physically located in Russia.
- The press release names the **Kyrgyz Republic** as the host jurisdiction of Old Vector; Kyrgyzstan is similarly not a cooperating party for this action.
- [[us-treasury]] (OFAC) — lead agency.
- [[us-secret-service]] (Cyber Investigative Section) — explicitly named as collaborating agency.
- [[fbi]] — providing assistance.
- U.S. Department of Justice (parallel: March 2025 indictments).
- U.S. Department of State (parallel: Transnational Organized Crime Rewards Program offers).

## Legal Framework

The August 2025 designations rely on **Executive Order 13694** ("Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities," April 2015), as amended by **E.O. 14144** and **E.O. 14306**. Garantex's prior April 2022 designation under **E.O. 14024** ("Blocking Property With Respect to Specified Harmful Foreign Activities of the Government of the Russian Federation") is retained. The simultaneous use of cyber-authority and Russia-authority sanctions layers two distinct U.S. unilateral sanctions regimes against the same target.

> [!note] Inline reference only
> E.O. 13694, E.O. 14024, E.O. 14144, and E.O. 14306 do not currently have dedicated `legal-frameworks/` pages in this wiki and are referenced in prose only.

## Operational Timeline

| Date | Event |
|---|---|
| Late 2019 | Garantex founded, registered in Estonia. |
| Feb 2022 | Estonia FIU revokes Garantex digital asset license. |
| 2022-04-05 | OFAC first designates Garantex under E.O. 14024. |
| 2023-11-03 | OFAC designates Ekaterina Zhdanova (Garantex-using money launderer) under E.O. 14024. |
| 2024-09 | OFAC sanctions Cryptex; FinCEN identifies PM2BTC ([[cryptex-pm2btc-sanctions]]). |
| 2025-03-06 | USSS-led disruption (with German and Finnish LE): domain seizure + USD 26 million crypto freeze. |
| 2025-03-07 | DOJ unseals indictments of Mira Serda and Besciokov; Besciokov arrested in India. |
| Days after 2025-03-06 | Garantex officers transfer customer deposits to Grinex; A7A5 token used to compensate users. |
| **2025-08-14** | **OFAC SB-0225: Garantex re-designation under E.O. 13694; Grinex, 3 executives, 6 companies designated.** |

## Results and Impact

- **Designations:** 1 entity re-designated (Garantex), 1 entity newly designated (Grinex), 3 individuals newly designated, 6 companies newly designated. Total newly added to SDN List: **10**.
- **Property blocking:** All property and interests in property of designated persons within U.S. jurisdiction are blocked; 50%-rule applies to subsidiaries.
- **Secondary effect:** Financial institutions and other persons engaging in transactions with the sanctioned entities risk secondary sanctions or enforcement action.
- **Reward offers:** USD 5 million for Mira Serda; USD 1 million for other key Garantex leaders (State Department TOC Rewards Program).
- **Quantitative impact** (per OFAC, not independently verified): Garantex processed over USD 100 million in illicit-actor transactions since 2019; Grinex has facilitated billions of dollars in cryptocurrency transactions since its creation.

The downstream operational effect on Grinex is **highly likely** to mirror the post-2022 Garantex pattern: continued operation from Russia, reduced access to compliant fiat off-ramps, and progressive isolation from regulated virtual asset service providers. Confidence is medium that Grinex will substantially curtail operations in the short term given the precedent of Garantex's continued activity post-2022.

## Cooperation Mechanisms Used

- **[[asset-freezing]]** — primary mechanism (OFAC SDN listing).
- **Inter-agency U.S. coordination** — Treasury (OFAC) + USSS Cyber Investigative Section + FBI + DOJ (parallel) + State Department (rewards). This is informal cooperation within a single jurisdiction rather than international cooperation in the MLAT sense.
- **Historical international cooperation** (March 2025 antecedent, not part of this August action): U.S.–Germany–Finland coordinated infrastructure seizure; India arrest of Besciokov; prior Estonia FIU enforcement (2022).

## Challenges and Friction Points

- **Sanctions evasion through successor entities.** The Garantex-to-Grinex migration completed within days of the March 2025 enforcement action, demonstrating that infrastructure-level enforcement and individual-level sanctions designation operate on different time scales. The August 2025 action is responsive rather than preventive.
- **Cross-jurisdictional reach into Russia.** Most designated persons are physically located in Russia and have no incentive to comply; sanctions impact is therefore largely on third-country financial institutions' willingness to interact with the network.
- **Stablecoin and ruble-backed token workarounds.** The A7A5 token issued via Kyrgyz Republic infrastructure illustrates active substitution of dollar-denominated stablecoins (e.g., USDT) with sovereign-friendly alternatives. The technical and jurisdictional challenge of interdicting such substitutes is **likely** to be a recurring problem.
- **No counterpart enforcement in Russia or Kyrgyzstan.** No mutual legal assistance, extradition, or joint investigation is reported with either host jurisdiction.

## Lessons Learned

- Sanctions actions against cryptocurrency exchanges should anticipate successor-entity migration and prepare follow-on designations as part of a single enforcement strategy rather than as separate actions months later.
- Layering cyber-authority sanctions (E.O. 13694) on top of country-specific sanctions (E.O. 14024) increases the legal basis for secondary sanctions and reduces the risk that delisting under one authority would lift the freeze.
- Public attribution of specific ransomware variants (Conti, Black Basta, LockBit, NetWalker, Phoenix Cryptolocker, Ryuk) to a money-laundering exchange supports **likely** civil liability theories for victim recovery and gives compliance teams concrete blocklisting signals.

## Follow-Up Actions

- Designation of A7A5 token addresses (not announced in this release; to be tracked).
- Potential coordinated EU and UK designations of Grinex and the A7 network (not announced as of publication; **likely** based on prior Garantex-related coordination patterns).
- Continued DOJ pursuit of Mira Serda (rewarded but at large) and other indicted executives.

## Korean Involvement (한국의 참여)

No direct Korean participation is identified in the press release. Korean virtual asset service providers (VASPs) and financial institutions are subject to U.S. secondary sanctions exposure if they transact with designated persons. **Likely** indirect impact: Korean compliance teams will need to update SDN screening to capture Grinex, the A7 network, Old Vector, InDeFi Bank, Exved, and the A7A5 token.

## Contradictions & Open Questions

- **Quantitative claims.** OFAC's "over USD 100 million" (Garantex illicit transactions) and "billions of dollars" (Grinex transactions) figures are not sourced to specific blockchain-analysis methodology in the press release. Confidence: **likely** accurate at order-of-magnitude given OFAC evidentiary practice, but precise figures are not independently verifiable from this source alone.
- **Status of Aleksej Besciokov** as of the August 2025 release. The press release notes his March 2025 arrest in India but does not address subsequent extradition status; this is left open.
- **Effectiveness of the re-designation against an already-designated target.** Whether the cyber-authority overlay produces meaningful incremental compliance behavior (versus the 2022 E.O. 14024 designation alone) is an open empirical question.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2025-08-14_treasury_garantex-grinex-russian-network-cyber-criminals-sanctions-evasion\|Treasury Sanctions Cryptocurrency Exchange and Network Enabling Sanctions Evasion and Cyber Criminals]] | US Department of the Treasury (OFAC), Press Release SB-0225 | 2025-08-14 | https://home.treasury.gov/news/press-releases/sb0225 |
