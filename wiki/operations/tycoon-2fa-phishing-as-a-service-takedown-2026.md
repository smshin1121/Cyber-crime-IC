---
type: operation
title: "Tycoon 2FA Phishing-as-a-Service Platform Takedown (Europol EC3 + Microsoft + 6-country LE coalition, 2026-03-04)"
title_ko: "Tycoon 2FA 피싱-서비스(PhaaS) 플랫폼 단속 (Europol EC3 + Microsoft + 6개국 법집행 연합, 2026-03-04)"
aliases:
  - "Tycoon 2FA takedown 2026"
  - "Tycoon 2FA PhaaS disruption"
  - "Global phishing-as-a-service platform taken down 2026"
  - "Europol CIEP Tycoon 2FA operation"
case_id: CYB-2026-118
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - domain-seizure
  - search-seizure
outcome: success
timeframe:
  announced: 2026-03-04
  start: 2023-08
  end: 2026-03-04
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[online-fraud-ic]]"
  - "[[hacking-ic]]"
target_entity: "Tycoon 2FA — phishing-as-a-service (PhaaS) platform active since at least August 2023; among the largest phishing operations worldwide. At peak generated tens of millions of phishing emails per month and facilitated unauthorised access to nearly 100 000 organisations globally including schools, hospitals, and public institutions. By mid-2025 accounted for roughly 62% of all phishing attempts blocked by Microsoft."
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[latvia]]"
  - "[[lithuania]]"
  - "[[portugal]]"
  - "[[poland]]"
  - "[[spain]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[latvia-state-police]]"
  - "[[lithuania-police]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[poland-police]]"
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[uk-nca]]"
  - "[[microsoft]]"
  - "[[trend-micro]]"
  - "[[shadowserver]]"
organizations:
  - "[[europol-ec3]]"
  - "[[latvia-state-police]]"
  - "[[lithuania-police]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[poland-police]]"
  - "[[spain-national-police]]"
  - "[[spain-guardia-civil]]"
  - "[[uk-nca]]"
  - "[[microsoft]]"
  - "[[trend-micro]]"
  - "[[shadowserver]]"
mechanisms_used:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Europol European Cybercrime Centre (EC3) coordination role under Regulation (EU) 2016/794 (Europol Regulation)"
  - "Europol Cyber Intelligence Extension Programme (CIEP) — first-of-its-kind public-private operational framework hosting private-sector experts at The Hague alongside EC3 analysts"
  - "EC3 Advisory Groups — steady-state public-private intelligence-sharing forums that disseminated the initial Trend Micro intelligence"
  - "Microsoft-led technical disruption (domain takedowns + control-panel disablement) in parallel with national LE seizure operations"
  - "National investigative authority of each participating country: Latvia State Police; Lithuania Criminal Police Bureau; Portugal Judicial Police; Poland Central Cybercrime Bureau (Centralne Biuro Zwalczania Cyberprzestępczości / CBZC); Spain National Police and Guardia Civil; UK National Crime Agency"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 330
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "330 domains forming the core infrastructure of the Tycoon 2FA service (phishing pages + control panels) taken down"
    - "Technical disruption led by Microsoft with a coalition of private partners (Cloudflare, Coinbase, Intel471, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro)"
    - "Seizure of infrastructure and other operational measures carried out by law enforcement in 6 countries — Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom — coordinated by Europol"
    - "Underlying disrupted ecosystem: PhaaS platform active since August 2023; tens of millions of phishing emails per month at peak; nearly 100 000 organisations globally with credentials harvested or accessed"
    - "Pre-disruption Microsoft-blocked share: ~62% of all phishing attempts blocked by Microsoft (mid-2025)"
    - "Arrests / suspect identification not enumerated in the cited primary release"
edges:
  - source_actor: europol-ec3
    target_actor: microsoft
    cooperation_type: technical_assistance
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: europol-ec3
    target_actor: trend-micro
    cooperation_type: info_sharing
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: europol-ec3
    target_actor: latvia-state-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: lithuania-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: portugal-policia-judiciaria
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: poland-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: spain-national-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: spain-guardia-civil
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: uk-nca
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific action day(s) on which infrastructure seizures were executed (the cited release announces the disruption on 2026-03-04 but does not enumerate a discrete action-day date for the LE seizures)"
  - "arrests and / or named suspects (the cited release does not enumerate arrests; it focuses on infrastructure disruption)"
  - "specific judicial authority orchestrating each national seizure"
  - "specific Europol command-post / coordination-centre arrangement (e.g., on-site coordination centre vs. virtual command post) is not enumerated in the cited release"
related_cases:
  []
related_operations:
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[lumma-stealer-takedown]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[leakbase-takedown-2026]]"
  - "[[xss-is-cybercrime-forum-takedown-2025]]"
  - "[[operacion-kaerb-iserver-phishing-as-a-service-takedown-2024]]"
challenges_encountered:
  []
lessons_learned:
  - "First wiki record of the Europol Cyber Intelligence Extension Programme (CIEP) as a discrete IC mechanism class — a first-of-its-kind Europol programme that physically embeds private-sector experts at The Hague alongside EC3 analysts and investigators on specific operational projects. Distinct from the EC3 Advisory Groups (steady-state info-sharing) and from one-off Europol mobile-office deployments to national LE."
  - "Two-tier public-private cooperation pattern: EC3 Advisory Groups (steady-state info-sharing) → CIEP (operational embedding). The Tycoon 2FA case is described as the first publicised CIEP-driven operational outcome."
  - "Microsoft-led technical takedown + LE-led seizure split is reaffirmed as a recurring pattern in PhaaS / cybercrime-infrastructure disruption (compare with [[labhost-phishing-as-a-service-takedown-2024|LabHost]] and [[lumma-stealer-takedown|Lumma Stealer]])."
  - "Six-country EU + UK LE coalition (Latvia, Lithuania, Portugal, Poland, Spain, UK) reflects a slim-but-targeted PhaaS-takedown footprint — significantly smaller than LabHost (19 countries) but with deeper private-sector integration through CIEP."
  - "Eight-private-partner roster (Cloudflare, Coinbase, Intel471, Microsoft, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro) is one of the broadest publicly-named private-sector coalitions in a Europol-coordinated cybercrime-infrastructure takedown to date."
source_count: 1
sources:
  - "[[2026-03-04_europol_global-phishing-service-platform-tycoon-2fa-taken-down]]"
summary: "On 2026-03-04 Europol announced the coordinated public-private disruption of Tycoon 2FA — one of the largest phishing-as-a-service (PhaaS) platforms worldwide, active since at least August 2023. 330 domains forming the platform's core infrastructure (phishing pages + control panels) were taken down. Technical disruption led by Microsoft with a coalition of private partners (Cloudflare, Coinbase, Intel471, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro). Seizures and other operational measures carried out by law enforcement in 6 countries — Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom — coordinated by Europol's European Cybercrime Centre (EC3). The investigation began after intelligence-sharing by Trend Micro through Europol's EC3 Advisory Groups, escalating into operational embedding via the Cyber Intelligence Extension Programme (CIEP), a first-of-its-kind Europol public-private framework. At peak Tycoon 2FA generated tens of millions of phishing emails per month and facilitated unauthorised access to nearly 100 000 organisations globally including schools, hospitals, and public institutions; by mid-2025 it accounted for ~62 % of all phishing attempts blocked by Microsoft."
created: 2026-05-09
updated: 2026-05-17
---
## Summary

On **2026-03-04**, Europol announced the coordinated public-private disruption of **Tycoon 2FA** — one of the **largest phishing-as-a-service (PhaaS) platforms worldwide**, active since at least **August 2023**. **330 domains** forming the platform's core infrastructure (phishing pages + control panels) were taken down. The technical disruption was led by **Microsoft** with a coalition of private partners; seizure of infrastructure and other operational measures were carried out by law enforcement in **six countries** — **Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom** — coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]].

## Background

(This section describes the **crime substance** — modus operandi, victim profile + impact, financial flow, and criminal-organisation structure of the Tycoon 2FA PhaaS platform. Operation context — how Europol mounted the disruption — appears in Summary and Cooperation Mechanisms.)

### Modus operandi — adversary-in-the-middle 2FA bypass as a service

Tycoon 2FA was a **phishing-as-a-service (PhaaS) platform** active since at least **August 2023**. Its principal value proposition was an **adversary-in-the-middle (AiTM)** phishing kit specifically engineered to bypass **two-factor authentication (2FA)** on Microsoft 365 and Google Workspace accounts. The platform operated as a subscription service marketed to thousands of cybercriminal customers ("traffers" or "phishers"); customers paid the operators (Telegram-channel-mediated, cryptocurrency-denominated) for access to a control panel, ready-to-deploy phishing-page templates impersonating Microsoft / Google login flows, and operator-maintained backend infrastructure.

The end-to-end attack sequence (as described by the cited Europol release and by tier-2 industry reporting from coalition partners — Trend Micro, Microsoft, Proofpoint, Sekoia):

1. **Lure delivery**: customer launches a phishing campaign (typically QR-code, OneDrive/SharePoint share-notification, or DocuSign-spoof emails) directing victims to a Tycoon-2FA-hosted landing URL.
2. **CAPTCHA + filtering layer**: the landing page presents a Cloudflare-Turnstile or invisible-CAPTCHA challenge to filter out automated-scanning and security-tool inspection traffic.
3. **AiTM proxy layer**: upon CAPTCHA pass, the victim is presented with a pixel-perfect Microsoft / Google login page that proxies authentication requests to the real Microsoft/Google authentication backend in real time.
4. **Credential + session token capture**: the platform captures the victim's username, password, **and the 2FA-completed session cookie/token** — bypassing TOTP, push-prompt, FIDO-non-resident, and SMS-based 2FA in a single user session.
5. **Tokens delivered to customer**: the captured session token is delivered to the cybercriminal customer's control panel, who can then replay it from a customer-controlled browser to take over the victim's Microsoft 365 / Google Workspace account without re-authenticating.

This AiTM-with-token-replay design is what makes the platform a 2FA-bypass kit — distinct from older credential-only phishing kits — and is what gave Tycoon 2FA its ~62% share of all phishing attempts blocked by Microsoft at mid-2025.

### Victim profile and impact

Per the cited Europol release:

- **Nearly 100 000 organisations globally** with credentials harvested or accounts accessed via Tycoon-2FA-driven campaigns.
- **Victim sectors named in the cited release**: schools, hospitals, and public institutions, alongside the implied corporate-employee victim base (the AiTM kit's design target is Microsoft 365 / Google Workspace tenants).
- **Tens of millions of phishing emails per month** at peak — the customer-driven email-volume signature of a successful PhaaS subscription model.
- **62 %** of all phishing attempts blocked by Microsoft at mid-2025 used Tycoon 2FA infrastructure — making it the **single largest phishing platform** in Microsoft's telemetry at that point.
- **Post-takeover damage typology** (industry coverage; not explicitly enumerated by the cited Europol release): business-email-compromise (BEC) wire fraud against the victim organisation's customers, internal lateral movement, ransomware initial-access handoff, payroll-redirection fraud, and onward credential harvesting from the compromised tenant.

> [!note] Gap on victim-side financial damage
> The cited Europol release publishes the "100,000 organisations" footprint but does **not** enumerate aggregate victim-side financial losses, per-victim-sector damage breakdowns, or per-country victim counts. See Contradictions.

### Financial flow

- **Operator-side revenue**: the cited Europol release does not enumerate aggregate operator revenue, per-subscription pricing, or cryptocurrency-wallet recoveries. Industry reporting from coalition partners (Trend Micro, Sekoia, Proofpoint) describes Tycoon 2FA's monthly subscription tiers in the historical USD 120 – USD 1,500 range (depending on number of phishing-domain slots, duration, and feature tier), payable in Bitcoin or USDT through Telegram-channel-mediated escrow. These industry figures are **not** carried in the cited tier-1 release.
- **Customer-side downstream proceeds**: each Tycoon-2FA-driven account compromise typically feeds BEC wire-fraud, ransomware-deployment, or credential-resale revenue streams for the customer; aggregate downstream proceeds are not quantified in the cited release.
- **Cryptocurrency seized during the takedown**: empty per the cited release (`cryptocurrency_seized` field). Coinbase and Cloudflare are named as private-coalition partners, which is consistent with cryptocurrency-tracing and DNS-/account-disablement support roles, but no specific Coinbase-side seizure figure is disclosed.

> [!note] Gap on financial flow
> Operator revenue, subscription pricing, cryptocurrency wallet identifications, and aggregate customer-side downstream proceeds are not enumerated in the cited tier-1 Europol release. See Contradictions.

### Criminal organisation structure

The cited Europol release frames Tycoon 2FA as a **service platform with a thousands-strong customer cohort**, not a single hierarchical OCG. Structural elements visible from the cited tier-1 source and the broader PhaaS literature:

- **Operator team** — the platform's developers and administrators, who maintain the AiTM-proxy codebase, the customer control panel, the CAPTCHA-filter layer, and the back-end domain-and-hosting rotation. The cited Europol release does **not** publicly name Tycoon 2FA operators; the release focuses on infrastructure disruption rather than on operator identification. Industry reporting indicates a Russian-speaking origin, but operator identities are not publicly disclosed in tier-1 sources.
- **Reseller / Telegram-channel intermediaries** — customer onboarding, subscription sales, technical support, and feature-update announcements were conducted via operator-controlled Telegram channels (typical PhaaS marketing pattern). The cited release does not name specific channels.
- **Customer / "phisher" base** — thousands of cybercriminal subscribers, dispersed globally and not part of a single hierarchical organisation. Each customer runs independent phishing campaigns against their own selected victim base, using the operator-supplied tooling.
- **Downstream customer-of-customer**: ransomware affiliates and BEC fraud crews who purchase 2FA-bypassed account-takeover access from Tycoon-2FA customers as a feed into their own pipelines. Tier-1 release does not enumerate this layer.

> [!note] Gap on OCG structure
> The cited Europol release does not publicly name Tycoon 2FA operators, individual cybercriminal customers, or downstream customer-of-customer linkages (notably to ransomware groups). The "arrests / suspect identification not enumerated" note in the cited release `results.other` confirms that the takedown was infrastructure-focused rather than operator-arrest-focused. See Contradictions.

### Investigation triggering and Europol pipeline

The investigation was triggered by intelligence shared by **Trend Micro**. Europol disseminated this information through its **EC3 Advisory Groups** and operational networks, enabling a coordinated operational strategy to be developed. A number of Advisory Group members were subsequently brought into the investigation to support the disruption effort, and through Europol's **Cyber Intelligence Extension Programme (CIEP)**, Microsoft and Trend Micro worked alongside law enforcement authorities providing technical expertise and infrastructure analysis.

## Participating Parties

| Country / Sector | Authority / Partner |
|---|---|
| Coordinating | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] (central hub between private partners and investigators; CIEP framework operator) |
| Latvia | [[latvia-state-police\|Latvia State Police]] |
| Lithuania | [[lithuania-police\|Lithuania Criminal Police Bureau]] |
| Portugal | [[portugal-policia-judiciaria\|Portugal Judicial Police]] |
| Poland | [[poland-police\|Poland Central Cybercrime Bureau (CBZC)]] |
| Spain | [[spain-national-police\|Spanish National Police]]; [[spain-guardia-civil\|Guardia Civil]] |
| United Kingdom | [[uk-nca\|UK National Crime Agency]] |
| Private — technical lead | [[microsoft\|Microsoft]] |
| Private — initial intelligence | [[trend-micro\|Trend Micro]] |
| Private — coalition (named) | Cloudflare; Coinbase; Intel471; Proofpoint; [[shadowserver\|Shadowserver Foundation]]; SpyCloud |

## Legal Framework

- **Europol European Cybercrime Centre (EC3) coordination role** under Regulation (EU) 2016/794 (Europol Regulation).
- **Europol Cyber Intelligence Extension Programme (CIEP)** — described in the cited release as a first-of-its-kind Europol programme that brings private-sector experts to The Hague to work temporarily side-by-side with EC3 analysts and investigators on specific operational projects.
- **EC3 Advisory Groups** — Europol's steady-state public-private intelligence-sharing forums that disseminated the initial Trend Micro intelligence.
- **Microsoft-led technical disruption** (domain takedowns and control-panel disablement) executed in parallel with national LE seizure operations.
- **National investigative authority** of each participating country (Latvia State Police; Lithuania Criminal Police Bureau; Portugal Judicial Police; Poland CBZC; Spain National Police + Guardia Civil; UK NCA).

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023-08 (at least) | Tycoon 2FA platform begins operation | Europol 2026-03-04 |
| (undated) | Trend Micro shares intelligence; Europol disseminates through EC3 Advisory Groups | Europol 2026-03-04 |
| (undated) | Coordinated operational strategy developed; Advisory Group members brought into the investigation | Europol 2026-03-04 |
| (undated) | CIEP-framework collaboration: Microsoft + Trend Micro work alongside LE in The Hague | Europol 2026-03-04 |
| Mid-2025 | Tycoon 2FA at peak ~62 % of all phishing attempts blocked by Microsoft | Europol 2026-03-04 |
| (undated, pre-2026-03-04) | Action / disruption phase: 330 domains taken down by Microsoft + private coalition; LE seizures in 6 countries | Europol 2026-03-04 |
| 2026-03-04 | Europol announces the disruption | Europol 2026-03-04 |

## Results and Impact

- **330 domains** forming the core infrastructure (phishing pages + control panels) **taken down**.
- **6-country LE coalition** executes seizures and operational measures: Latvia, Lithuania, Portugal, Poland, Spain, UK.
- **8 named private partners** in the disruption coalition: Cloudflare, Coinbase, Intel471, Microsoft, Proofpoint, Shadowserver Foundation, SpyCloud, Trend Micro.
- **Underlying disrupted ecosystem**: ~30 months of operation (Aug 2023 to early 2026); tens of millions of phishing emails per month at peak; nearly 100 000 organisations globally accessed; ~62 % share of Microsoft-blocked phishing attempts at mid-2025.
- **Arrests / named suspects**: not enumerated in the cited primary release. The release focuses on infrastructure disruption, not on prosecutions.

## Cooperation Mechanisms Used

The cited release describes three discrete IC mechanism classes for this operation:

1. **Europol Cyber Intelligence Extension Programme (CIEP)** — first-of-its-kind Europol public-private operational framework that hosts private-sector experts at The Hague to work side-by-side with EC3 analysts and investigators on specific operational projects. The Tycoon 2FA case is described as the first publicised CIEP-driven operational outcome.
2. **EC3 Advisory Groups** — Europol's steady-state public-private intelligence-sharing forums; the entry-point for Trend Micro's initial intelligence and the recruitment pool for the eventual CIEP-embedded private partners.
3. **Microsoft-led technical disruption + national LE seizure split** — the platform-level disruption (domain takedowns + control-panel disablement) is led by Microsoft with a coalition of private partners, while infrastructure seizures and other operational measures are carried out by national LE in 6 countries, all coordinated by Europol. Compare with [[labhost-phishing-as-a-service-takedown-2024|LabHost (April 2024)]] and [[lumma-stealer-takedown|Lumma Stealer (May 2025)]].

## Challenges and Friction Points

The cited release does not enumerate specific challenges. *Likely* (analyst inference): a 6-country + 8-private-partner coalition coordinated through a brand-new CIEP framework would face the usual public-private friction (NDAs, evidentiary chain-of-custody for industry-derived telemetry, varying national admissibility standards for private-sector intrusion data). None of these is documented in the source.

## Lessons Learned

- First wiki record of the **Europol Cyber Intelligence Extension Programme (CIEP)** as a discrete IC mechanism class.
- Two-tier public-private cooperation pattern: **EC3 Advisory Groups** (steady-state info-sharing) → **CIEP** (operational embedding).
- Microsoft-led technical takedown + LE-led seizure split is reaffirmed as a recurring pattern in PhaaS / cybercrime-infrastructure disruption.
- A six-country EU + UK LE coalition with eight named private-sector partners is one of the broadest publicly-named private-sector coalitions in a Europol-coordinated cybercrime-infrastructure takedown to date.

## Follow-Up Actions

The cited release does not enumerate downstream prosecutions or sanctions. *Likely* (analyst inference): operator-identification and / or money-laundering follow-on prosecutions in one or more of the 6 LE-coalition jurisdictions, but none is documented in the source.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Europol release among the participating jurisdictions or private partners. The case is recorded in the wiki for the new CIEP IC mechanism class and the Microsoft-led + 6-country-LE PhaaS-takedown pattern. Korean exposure to Tycoon 2FA as a phishing platform — given the global ~100 000 organisations affected and the platform's worldwide scale — is *likely* present but is not enumerated in this source.

## Contradictions & Open Questions

- The cited release does not enumerate a discrete action-day date for the LE seizures, only the announcement date of 2026-03-04.
- Arrests / named suspects are not enumerated; the release focuses entirely on infrastructure disruption.
- Specific judicial authorities orchestrating each national seizure are not enumerated.
- Specific Europol command-post / coordination-centre arrangement (on-site vs. virtual) is not enumerated, in contrast with the more detailed [[xss-is-cybercrime-forum-takedown-2025|xss.is takedown]] release.
- The release frames Tycoon 2FA as having ~62 % of mid-2025 Microsoft-blocked phishing share but does not provide an aggregate post-disruption phishing-blocked share to quantify residual / displacement effects.
- **L26 gap — victim-side damage**: the cited Europol release publishes the 100,000-organisation footprint but does **not** enumerate aggregate victim-side financial losses, per-victim-sector damage breakdowns, or per-country victim counts. Downstream BEC / ransomware / payroll-fraud losses driven by Tycoon-2FA account-takeovers are not separately tracked.
- **L26 gap — financial flow**: operator subscription pricing, operator revenue, cryptocurrency-wallet identifications, and any Coinbase-side wallet recoveries are not disclosed in the cited tier-1 release. Industry-reporting historical price ranges (USD 120 – USD 1,500 / month) are not confirmed by the cited tier-1 source.
- **L26 gap — OCG structure**: the cited Europol release does not publicly name Tycoon 2FA operators, Telegram-channel intermediaries, individual cybercriminal customers, or downstream customer-of-customer linkages (notably to ransomware groups). The release confirms the takedown was infrastructure-focused rather than operator-arrest-focused, so operator-identification work remains a follow-on intelligence task.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-03-04_europol_global-phishing-service-platform-tycoon-2fa-taken-down\|Global phishing-as-a-service platform taken down in coordinated public-private action]] | Europol | 2026-03-04 | https://www.europol.europa.eu/media-press/newsroom/news/global-phishing-service-platform-taken-down-in-coordinated-public-private-action |
