---
type: operation
title: "Operation Atlantic — NCA-led UK-US-Canada international action against cryptocurrency 'approval phishing' (NCA + US Secret Service + Ontario Provincial Police + Ontario Securities Commission, March 2026)"
title_ko: "Operation Atlantic — 영국 NCA 주도 영국·미국·캐나다 합동 가상자산 'approval phishing' 사기 단속 (NCA + 미국 비밀경호국 + 온타리오주 경찰 + 온타리오 증권위원회, 2026-03)"
aliases:
  - "Operation Atlantic 2026"
  - "NCA approval phishing operation"
  - "UK-US-Canada cryptocurrency fraud takedown 2026"
case_id: CYB-2026-095
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - asset_freeze
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2026-04-09
  start: ""
  end: ""
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "Distributed cryptocurrency fraud networks operating 'approval phishing' scams that trick victims into granting criminals access to their cryptocurrency wallets, typically marketed as investment opportunities. Networks targeted UK, Canadian, and US victims; victims totalled 20,000+ across the three jurisdictions; cumulative cryptocurrency fraud identified globally totalled USD 45,000,000+; weeklong action froze USD 12,000,000+ in suspected criminal proceeds; per a corresponding US Secret Service release, the operation also identified and disrupted 120+ web domains used by scammers."
lead_agency: "[[uk-nca]]"
coordinating_body: "[[uk-nca]]"
participating_countries:
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[canada]]"
participating_agencies:
  - "[[uk-nca]]"
  - "[[us-secret-service]]"
  - "[[city-of-london-police]]"
organizations:
  - "[[uk-nca]]"
  - "[[us-secret-service]]"
  - "[[city-of-london-police]]"
mechanisms_used:
  - "[[informal-cooperation]]"
legal_basis:
  - "Bilateral / trilateral UK-US-Canada law enforcement cooperation. The cited NCA release does not specify a single legal instrument; the operative framework is a combination of (a) MLAR/MLAT channels for evidence transfer, (b) police-to-police informal cooperation for intelligence sharing, and (c) private-sector voluntary disclosure for real-time blockchain tracing."
  - "UK Proceeds of Crime Act 2002 (POCA): basis for the GBP/USD freezing orders against UK-domestic suspect proceeds."
  - "US Secret Service authorities under 18 U.S.C. § 3056 (Treasury fraud / cyber-financial-crime jurisdiction)."
  - "Ontario Securities Commission authorities under the Ontario Securities Act for cryptocurrency-investment-fraud freezing orders."
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "$12,000,000+ frozen in suspected criminal proceeds (per NCA)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "20,000+ victims identified across UK, Canada, and the United States (per NCA)"
    - "USD 45,000,000+ in cryptocurrency fraud identified globally (per NCA)"
    - "USD 12,000,000+ frozen in suspected criminal proceeds (per NCA)"
    - "120+ web domains used by scammers identified and disrupted (per US Secret Service release; NCA release does not enumerate the domain count)"
    - "One UK victim documented loss > GBP 52,000 (per NCA)"
    - "Format: weeklong NCA HQ-hosted action with multiple LE agencies physically co-located; private-sector partners critical to real-time illicit-transaction tracing and victim identification, enabling funds to be secured before criminals could move them"
    - "Operation date: 'last month' (per 9 April 2026 release) — i.e., approximately early-to-mid March 2026"
edges:
  - source_actor: uk-nca
    target_actor: us-secret-service
    cooperation_type: joint_investigation
    legal_basis: bilateral
    direction: undirected
  - source_actor: uk-nca
    target_actor: ontario-provincial-police
    cooperation_type: joint_investigation
    legal_basis: bilateral
    direction: undirected
  - source_actor: us-secret-service
    target_actor: ontario-provincial-police
    cooperation_type: info_sharing
    legal_basis: bilateral
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific operation dates ('last month' from 9 April → early March, but NCA release does not give exact action-day date range)"
  - "specific other international law enforcement bodies that joined the weeklong action ('and other international law enforcement bodies also joined' is unenumerated)"
  - "specific names of private sector partners that played the 'critical' role (Binance is named only in subsequent reporting; NCA release does not name partners)"
  - "specific arrest counts (the NCA release reports identifications/freezes/disruptions but no arrests)"
  - "specific domain count seized (120+ per Secret Service; NCA release does not enumerate)"
  - "specific cryptocurrency mix (BTC vs. ETH vs. stablecoins) — 'cryptocurrency wallets' generic"
  - "ongoing investigative tracks against fraud-network operators identified during the operation"
related_cases:
  []
related_operations:
  - "[[operation-token-mirrors-2026]]"
  - "[[eurojust-100m-crypto-investment-fraud-takedown-2025]]"
  - "[[eurojust-600m-crypto-money-laundering-takedown-2025]]"
  - "[[usss-canada-operation-avalanche-ethereum-approval-phishing-2025]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "**NCA-led tri-jurisdiction (UK-US-Canada) cooperation pattern** is structurally distinct from previous UK-led joint actions in the wiki, which have typically paired UK with one other jurisdiction or with EU partners. Adds a documented UK-led North-Atlantic cooperation track to the wiki's cryptocurrency-fraud disruption corpus."
  - "**'Approval phishing' as a named cryptocurrency-fraud sub-category** — first explicit wiki record of this technique class. Distinct from (a) credential-phishing (e.g., [[w3ll-phishing-kit-takedown-2026|W3LL]]), (b) investment-scam-impersonation (e.g., [[afp-rtp-bangkok-scam-centre-operation-firestorm-2025|AFP Firestorm]]), and (c) wallet-drainer-toolkit-as-a-service patterns. The technique grants attackers ongoing wallet access rather than one-time credential capture."
  - "**Physical NCA HQ co-location format** — a specific operational pattern in which multiple LE agencies are physically co-located at a coordinating-host HQ for a weeklong action with real-time intelligence sharing. Comparable to Europol J-CAT / data-sprint formats but with a non-EU-host nucleus."
  - "**Private-sector real-time blockchain tracing as a *critical* enablement layer** — the NCA release explicitly characterises private-sector partners as critical to real-time illicit-transaction tracing and victim identification, *meaning their money could be secured before it was moved by criminals*. Establishes a public-private speed advantage as an explicit operational design principle."
  - "**Asset-recovery-as-primary-objective format** — Operation Atlantic prioritised victim identification + funds freezing (USD 12M frozen, 20,000 victims, USD 45M identified) over arrest counts (zero documented in cited release). A different *primary* outcome metric than typical Europol/INTERPOL operations."
source_count: 1
sources:
  - "[[2026-04-09_nca-uk_operation-atlantic-cryptocurrency-fraudsters]]"
created: 2026-05-09
updated: 2026-05-16
---
## Summary

**Operation Atlantic** was an **NCA-led weeklong international action** against cryptocurrency **'approval phishing'** fraud held in approximately early-to-mid March 2026 and announced via NCA Newsroom press release on **9 April 2026**. The operation was co-hosted by the **NCA, US Secret Service, Ontario Provincial Police, and Ontario Securities Commission**, with UK participation from **City of London Police** and the **Financial Conduct Authority** and additional unnamed international law enforcement bodies. The format was physical co-location at NCA London HQ with real-time intelligence sharing, technical capabilities, and victim outreach.

**Outcomes** (per NCA):
- **20,000+ victims identified** across UK, Canada, and the United States
- **USD 12 million+ frozen** in suspected criminal proceeds
- **USD 45 million+** in cryptocurrency fraud identified globally
- One UK victim documented loss > **GBP 52,000**

A corresponding **US Secret Service release** adds that the operation **identified and disrupted 120+ web domains** used by scammers; the NCA release does not enumerate the domain count.

> [!note] 'Approval phishing' technique class
> 'Approval phishing' tricks victims into *granting criminals access* to their cryptocurrency wallets, typically as part of investment scams. The technique gives attackers *ongoing wallet access* rather than one-time credential capture, distinguishing it from generic credential-phishing.

## Background

The operation targeted distributed cryptocurrency fraud networks operating 'approval phishing' scams against UK, Canadian, and US victims. The NCA explicitly framed the action as part of UK government's Fraud Strategy emphasising public-private cooperation; the operation deliberately leveraged private-sector blockchain analytics partners to trace illicit transactions in real-time and identify victims fast enough to secure funds before they could be moved by criminals.

## Participating Parties

| Agency | Country | Role |
|---|---|---|
| [[uk-nca\|UK National Crime Agency]] | United Kingdom | **Lead**; HQ host; tri-jurisdictional coordinator |
| [[us-secret-service\|US Secret Service]] | United States | Co-host; US-side investigative authority for cyber-financial crime |
| Ontario Provincial Police | Canada | Co-host; Canada-side investigative authority |
| Ontario Securities Commission | Canada | Co-host; Canada-side cryptocurrency-investment-fraud regulator |
| [[city-of-london-police\|City of London Police]] | United Kingdom | UK-side fraud-specialist participant |
| Financial Conduct Authority | United Kingdom | UK-side financial-services regulator |
| Other (unenumerated) | various | "other international law enforcement bodies also joined the weeklong action" |
| Private sector | n/a | "critical role in tracing illicit transactions and identifying victims in real-time" — partners not named in NCA release |

## Legal Framework

- **Bilateral / trilateral UK-US-Canada law enforcement cooperation.** Operative framework: MLAR/MLAT for evidence transfer, police-to-police informal cooperation for real-time intelligence sharing, and private-sector voluntary disclosure for blockchain tracing.
- **UK POCA 2002.** Basis for UK-domestic freezing orders against suspect proceeds.
- **US Secret Service authorities (18 U.S.C. § 3056)** for US-side cyber-financial-crime jurisdiction.
- **Ontario Securities Act** for Canada-side cryptocurrency-investment-fraud freezing orders.

> [!warning] Legal status check needed
> The cited release does not specify the precise legal instruments used to effect the USD 12M+ freeze across UK, US, and Canadian assets. Subsequent court filings or proceedings may clarify.

## Operational Timeline

| Date | Event |
|---|---|
| approx. early-to-mid March 2026 | Operation Atlantic action week — physical co-location at NCA London HQ; real-time intelligence sharing; multiple fraud networks disrupted; 20,000+ victims identified; USD 12M+ frozen; USD 45M+ fraud identified globally; 120+ web domains disrupted (per US Secret Service) |
| 9 April 2026 | NCA press release announcement (corresponding US Secret Service release the same day) |

## Results and Impact

| Metric | Value | Notes |
|---|---|---|
| Victims identified | **20,000+** | Across UK, Canada, US |
| Frozen | **USD 12,000,000+** | In suspected criminal proceeds |
| Cryptocurrency fraud identified | **USD 45,000,000+** | Globally |
| Web domains disrupted | **120+** | Per corresponding US Secret Service release; NCA release does not enumerate |
| Highest single UK victim loss documented | **GBP 52,000+** | One identified UK victim |
| Format | Weeklong | NCA London HQ-hosted physical co-location |

## Cooperation Mechanisms Used

- **NCA London HQ-hosted physical co-location** — multi-agency operational room with real-time intelligence sharing
- **Tri-jurisdiction (UK-US-Canada) coordination** complemented by additional unnamed international LE
- **Private-sector real-time blockchain tracing** — explicitly cited by NCA as 'critical' to operation success
- **Asset-recovery-first posture** — primary success metric is funds frozen + victims identified, not arrests

## Challenges and Friction Points

- **Distributed fraud-network architecture** — 'approval phishing' fraud networks are typically distributed across many jurisdictions and many small operators. Disruption requires the kind of breadth Operation Atlantic provided (multi-agency, multi-country, with private-sector tracing) rather than a single targeted indictment.
- **Speed of cryptocurrency flows** — funds must be frozen before being moved by criminals. This is the explicit operational design rationale for the private-sector real-time tracing integration.
- **Asset-recovery-only posture** — no arrests are documented in the cited release. Whether ongoing investigative tracks against fraud-network operators will produce indictments and arrests is *unknown* from the cited release.

## Lessons Learned

1. **NCA-led UK-US-Canada tri-jurisdiction format** as a documented pattern. Distinct from typical UK-EU or UK-bilateral cooperation tracks; adds a North-Atlantic cooperation pattern to the wiki.
2. **'Approval phishing' is a discrete cryptocurrency-fraud technique class**. Technique grants ongoing wallet access (vs. one-time credential capture) and warrants its own analytical category.
3. **NCA HQ physical co-location format** parallels Europol J-CAT / data-sprint formats but with a non-EU coordinating-host nucleus. Validates the pattern outside Europol.
4. **Private-sector real-time blockchain tracing is a critical operational layer** for asset-recovery-first cryptocurrency fraud disruption. Public sector alone *cannot* trace fast enough to secure funds before they are moved.
5. **Asset-recovery-first metric set** (USD 12M frozen + 20,000 victims + USD 45M identified, zero documented arrests) is a deliberate design choice prioritising victim restoration over criminal prosecution as the operation's *primary* success metric.

## Follow-Up Actions

The cited release explicitly notes that NCA and partners will continue to analyse intelligence gathered during Operation Atlantic to support victims and investigate potential criminal activity. Specific follow-on indictments, arrests, or extraditions are not enumerated in the cited release.

## Korean Involvement (한국의 참여)

[[south-korea|South Korea]] has no documented involvement in this operation. Korean victims among the 20,000+ identified are *unknown* from the cited release; the release identifies victims as 'across UK, Canada and the United States' implying tri-jurisdiction focus rather than global. KNPA Cyber Bureau ↔ NCA channel is not enumerated in this case.

## Contradictions & Open Questions

- **NCA vs. US Secret Service domain count**: NCA release does not enumerate domains; US Secret Service same-day release reports 120+. The figures are *complementary*, not contradictory, but illustrate cross-agency framing differences.
- **Specific dates**: 'last month' (per 9 April release) places the action in approximately early-to-mid March 2026, but the cited release does not give the precise action-day date range.
- **Private-sector partners**: 'critical' but unnamed in NCA release. Subsequent reporting names Binance and Chainalysis, but those names are *not* in the tier-1 NCA primary release.
- **Other international LE bodies**: 'other international law enforcement bodies also joined' but unenumerated in the NCA release.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-04-09_nca-uk_operation-atlantic-cryptocurrency-fraudsters\|Fraudsters targeting cryptocurrency stopped and $12 million frozen in NCA-led Operation Atlantic]] | UK National Crime Agency | 2026-04-09 | https://www.nationalcrimeagency.gov.uk/news/fraudsters-targeting-cryptocurrency-stopped-and-12-million-frozen-in-nca-led-operation-atlantic |
