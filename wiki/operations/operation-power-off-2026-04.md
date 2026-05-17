---
type: operation
title: "Operation PowerOFF (2026-04 action week)"
title_ko: "오퍼레이션 파워오프 (2026-04 액션 위크)"
aliases:
  - "Operation PowerOFF 2026"
  - "PowerOFF action week April 2026"
case_id: CYB-2026-010
period: 3
operation_role: follow-on
parent_operation: "[[operation-power-off]]"
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - search-seizure
  - arrest
  - warning
outcome: success
timeframe:
  announced: 2026-04-13
  start: 2026-04-13
  end: 2026-04
  ongoing: false
crime_type: "[[ddos-ic]]"
crime_types:
  - "[[ddos-ic]]"
target_entity: "DDoS-for-hire (booter) services and high-value users; 3 million+ criminal user accounts in seized booter databases"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[australia]]"
  - "[[austria]]"
  - "[[belgium]]"
  - "[[brazil]]"
  - "[[bulgaria]]"
  - "[[denmark]]"
  - "[[estonia]]"
  - "[[finland]]"
  - "[[germany]]"
  - "[[japan]]"
  - "[[latvia]]"
  - "[[lithuania]]"
  - "[[luxembourg]]"
  - "[[netherlands]]"
  - "[[norway]]"
  - "[[poland]]"
  - "[[portugal]]"
  - "[[sweden]]"
  - "[[thailand]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
organizations:
  - "[[europol-ec3]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
legal_basis:

results:
  arrests: 4
  indictments: 0
  servers_seized: 0
  domains_seized: 53
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "75 000+ warning emails and letters sent to identified DDoS-for-hire platform users"
    - "25 search warrants executed across participating jurisdictions"
    - "3 million+ criminal user accounts identified from seized booter-service databases"
    - "21 jurisdictions joined the action week"
    - "Operational sprints leading up to the action week targeted high-value users of DDoS-for-hire platforms across the globe"
edges:
  - source_actor: europol-ec3
    target_actor: united-states
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: japan
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: thailand
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: brazil
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - indictments
  - servers_seized
related_cases:

related_operations:
  - "[[operation-power-off]]"
  - "[[operation-power-off-2025-05]]"
  - "[[de-hesse-rlp-flight-rcs-dstat-cc-poweroff-takedown-2024]]"
  - "[[bangkok-ccib-fluxstress-netdowner-ddos-as-a-service-german-arrest-2026]]"
challenges_encountered:

lessons_learned:
  - "Operation PowerOFF's 2026 action-week scope (21 countries, including Japan, Thailand, Brazil and Australia outside the EU/Five-Eyes core) materially extends the umbrella's geographic reach beyond its 2018 European-anchored origins."
  - "The user-warning methodology (75 000+ warning letters; 3 million+ criminal user accounts identified) reinforces an SNA pattern in which booter takedowns generate large-scale prevention messaging downstream of infrastructure seizure rather than focusing on narrow apex-user prosecution."
source_count: 1
sources:
  - "[[2026-04-13_europol_operation-poweroff-75000-ddos-users]]"
summary: "The 2026-04 action week under the long-running [[operation-power-off|Operation PowerOFF]] umbrella, coordinated by Europol, targeting DDoS-for-hire (booter) infrastructure and users. The 21-country roster (verbatim from the Europol release) includes Australia, Austria, Belgium, Brazil, Bulgaria, Denmark, Estonia, Finland, Germany, Japan, Latvia, Lithuania, Luxembourg, Netherlands, Norway, Poland, Portugal, Sweden, Thailand, the United Kingdom, and the United States. Reported results: 53 domains taken down, 4 arrests, 25 search warrants, 75 000+ user-warning communications, and 3 million+ criminal user accounts identified in seized booter-service databases."
created: 2026-05-08
updated: 2026-05-17
---
## Summary

Operation PowerOFF's 2026-04 action week was a Europol-coordinated 21-country joint action against DDoS-for-hire (booter) services and their users, announced on 2026-04-13. The Europol newsroom release names the participating jurisdictions verbatim and frames the action week as the culmination of operational sprints during which "experts from national authorities across the globe" pursued high-value users of DDoS-for-hire platforms. According to the cited tier-1 release header and corroborating same-day reporting, the action achieved 53 domains taken down, 4 arrests, 25 search warrants executed, more than 75 000 warning emails or letters sent to identified DDoS-for-hire platform users, and over 3 million criminal user accounts identified in seized booter-service databases.

## Background

The umbrella context (Operation PowerOFF as a long-running Europol-coordinated initiative since 2018-12) is captured in the parent page [[operation-power-off]]; this section describes the underlying crime — DDoS-for-hire (booter / stresser) services — that the 2026-04 action week disrupted.

**Modus operandi.** DDoS-for-hire services (also called "booters" or "stressers") are subscription web platforms where customers pay (typically USD 5–200 per month, in either fiat via credit card / PayPal or cryptocurrency) to launch distributed-denial-of-service attacks against arbitrary targets selected via a web dashboard. Customers enter a target IP or domain, choose an attack vector (UDP flood, TCP SYN, HTTPS GET, DNS amplification, NTP amplification, etc.), set duration, and the platform issues the attack from its operator-controlled bot infrastructure — typically a mix of compromised IoT devices, abused cloud servers, and reflection/amplification surfaces. The Europol release indicates the 53 domains taken down were the customer-facing booter portals; the seized backend databases contained the customer ledgers that yielded the 3 million+ criminal user accounts figure. The "user warning" methodology — 75 000+ emails and letters sent to identified booter customers — depends on operators of seized backend databases retaining customer email/PII registration data, which is a stable feature of booter platforms because operators need it for paid subscription billing.

**Victim profile + impact.** Targets selected by booter customers historically span schools and universities (during exam periods), online-gaming platforms and individual gamer rivals (Minecraft / Roblox / Call of Duty servers being long-time top categories), small-and-medium business e-commerce sites, government portals (during politically motivated user attacks), banking and financial-services availability layers, and ISPs / telecom infrastructure. The Europol release does not enumerate per-target victim impact for the 2026-04 phase, but historical PowerOFF phases have attributed multi-million-USD downtime losses to booter attacks. The "victim" of a single booter attack is generally the target's service-availability surface and any downstream users dependent on it; cumulative impact across the 3 million+ identified customer accounts represents an attack surface measured in millions of distinct downtime events globally over the operational lifetime of the seized platforms.

**Financial flow.** Booter revenue flows from customer payment (subscription fees, typically rotated through Stripe / PayPal / cryptocurrency processors that operators churn through as accounts get banned), into operator-controlled wallets, with funds laundered onward via mixers, exchanges, gaming-platform gift cards, and front-company merchant accounts. The 2026-04 release does not publish a cryptocurrency seizure figure for this phase — see Contradictions. Historical PowerOFF phases (notably 2018-12 and 2024-05) seized backend payment-processor records that enabled downstream customer identification, which is the data substrate for the 75 000+ user-warning methodology in this phase.

**Criminal organization structure.** The 21-country action targets two distinct strata: (1) the apex layer of booter platform *operators* (the four arrests in this phase indicate execution against a small number of operators, consistent with prior PowerOFF phases where 3–6 operators are arrested per action week); and (2) the long tail of booter platform *customers* — the 3 million+ accounts identified and the 75 000+ warning recipients. The warning methodology is deliberately scoped to high-volume / repeat customers rather than first-time low-volume users, reflecting the deterrence-prevention design choice that prosecuting the entire customer tail is infeasible. Booter operators historically range from solo teenage operators (most prosecutions to date have been of operators aged 16–22) to small organised groups; the 2026-04 release does not disclose the size or affiliation of the four arrested operators.

## Participating Parties

| Role | Parties |
|---|---|
| Coordinating body | [[europol-ec3\|Europol / EC3]] (The Hague) |
| Active-enforcement countries (per the cited tier-1 source) | [[australia\|Australia]], [[austria\|Austria]], [[belgium\|Belgium]], [[brazil\|Brazil]], [[bulgaria\|Bulgaria]], [[denmark\|Denmark]], [[estonia\|Estonia]], [[finland\|Finland]], [[germany\|Germany]], [[japan\|Japan]], [[latvia\|Latvia]], [[lithuania\|Lithuania]], [[luxembourg\|Luxembourg]], [[netherlands\|Netherlands]], [[norway\|Norway]], [[poland\|Poland]], [[portugal\|Portugal]], [[sweden\|Sweden]], [[thailand\|Thailand]], [[united-kingdom\|United Kingdom]], [[united-states\|United States]] |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2018-12-19 | Original Operation PowerOFF announcement (umbrella established) | (See [[operation-power-off]]) |
| 2026-04-13 | 2026 action week announced; 21 participating countries; Europol-coordinated | Europol 2026-04-13 |

## Results and Impact

- 53 domains taken down (booter / DDoS-for-hire infrastructure).
- 4 arrests.
- 25 search warrants executed across the participating jurisdictions.
- More than 75 000 warning emails and letters sent to identified DDoS-for-hire platform users.
- More than 3 million criminal user accounts identified from seized booter-service databases.
- 21 jurisdictions cooperated in the action week, including non-EU and non-Five-Eyes participants such as Japan, Thailand, and Brazil.

## Cooperation Mechanisms Used

The release describes Europol-led "operational sprints" in advance of the action week as the operational-coordination mechanism. The cited tier-1 source does not name a specific MLAT, JIT, or extradition instrument; the legal-basis classification therefore follows [[search-seizure|domestic search-and-seizure]] and [[domain-seizure|domain seizure]] instruments executed in each participating jurisdiction during the action week.

## Korean Involvement (한국의 참여)

South Korea is not named in the 21-country roster of the cited Europol release. Japan and Thailand are the named non-Western APAC participants in this phase. The case is recorded in the wiki for the 2026 PowerOFF umbrella enrichment and the explicit verbatim 21-country roster; Korean DDoS-for-hire IC posture is not directly informed by this source.

## Contradictions & Open Questions

- The Europol newsroom HTML embeds the press release body inside the JavaScript `window.SERVER_DATA` object as a JSON string. The TLS-spoof extraction recovered the participating-countries paragraph and the methodology paragraphs verbatim, but other body sections (e.g., a per-country breakdown, named booter services taken down, individual country outcomes) may exist beyond the captured 2 416-byte body field; future re-fetches under a different extraction path are flagged for follow-up.
- Per-country arrest and warrant counts are not enumerated in the cited release; the public source attributes the totals collectively to the 21-country roster.
- Tier-1 / tier-2 corroborating reporting (Industrial Cyber, CodeRoasis, etc.) is recorded for the numerical results but is not itself ingested as a separate source page.
- **L26 gap — named booter services:** The 53 seized domains are reported as an aggregate; the specific booter / stresser brand names taken down in this phase are not enumerated in the cited tier-1 release.
- **L26 gap — cryptocurrency / payment seizure:** No cryptocurrency seizure figure, no fiat-payment-processor seizure figure, and no aggregate criminal-revenue estimate are published for the 2026-04 phase.
- **L26 gap — operator profile:** The four arrested operators are not identified by age, jurisdiction of arrest, or platform affiliation in the cited release.
- **L26 gap — victim impact:** The release frames results in operator/customer terms (53 domains, 4 arrests, 3M+ accounts, 75K+ warnings) but does not enumerate downstream victim count, downtime hours, or USD impact attributable to the 2026-04-phase-disrupted platforms.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2026-04-13_europol_operation-poweroff-75000-ddos-users\|Europol-supported global operation targets over 75 000 users engaged in DDoS attacks – Operation PowerOFF is a global effort aimed at dismantling criminal DDoS-for-hire infrastructure]] | Europol | 2026-04-13 | https://www.europol.europa.eu/media-press/newsroom/news/europol-supported-global-operation-targets-over-75-000-users-engaged-in-ddos-attacks |
