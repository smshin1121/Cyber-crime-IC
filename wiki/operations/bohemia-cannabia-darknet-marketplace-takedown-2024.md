---
type: operation
title: "Bohemia / Cannabia Darknet Marketplace Takedown (2024)"
aliases:
  - "Bohemia takedown"
  - "Bohemia/Cannabia operation"
  - "Bohemia Market shutdown"
case_id: CYB-2024-107
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2024-10-08
  start: 2022-12-01
  end: 2024-08-31
  ongoing: false
crime_types:
  - "[[dark-web-ic]]"
  - "[[drug-trafficking]]"
  - "[[money-laundering-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
crime_type: dark-web-ic
target_entity: "Bohemia / Cannabia darknet marketplace (dual sister-market under common administration)"
lead_agency: "[[netherlands-politie]]"
coordinating_body: ""
participating_countries:
  - "[[netherlands]]"
  - "[[ireland]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[netherlands-politie]]"
  - "[[netherlands-om]]"
  - "[[ireland-garda]]"
  - "[[uk-nca]]"
legal_basis:
  []
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[cryptocurrency-seizure]]"
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
results:
  arrests: 2
  indictments: 0
  servers_seized: 3
  domains_seized: 0
  cryptocurrency_seized: ">EUR 8,000,000"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Database server, crypto server and web server seized (most located in the Netherlands)"
    - "Bitcoin wallet access keys recovered at Schiphol arrest"
    - "Marketplace peak monthly turnover EUR 12 million (Sep 2023); ~82,000 daily ads; ~67,000 monthly transactions"
    - "Estimated administrator profits ~EUR 5 million"
edges:
  - source_actor: netherlands-politie
    target_actor: ireland-garda
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: netherlands-politie
    target_actor: uk-nca
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: netherlands-politie
    target_actor: united-states
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: netherlands-politie
    target_actor: netherlands-om
    cooperation_type: evidence_transfer
    legal_basis: domestic
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific U.S. agency identity (DOJ named in one tier-2 source only)"
  - "Eurojust / Europol coordination role (not explicitly cited for original takedown)"
  - "specific legal basis (no treaty cited; appears informal + bilateral)"
related_cases:
  []
related_operations:
  - "[[us-colombia-versus-project-darknet-marketplace-schmitz-extradition-2026]]"
challenges_encountered:
  []
lessons_learned:
  - "Multi-year persistence: the investigation continued past the operators' apparent late-2023 exit scam, identifying administrators after the marketplace had gone offline — challenging the assumption that exit-scammed markets are not pursuable."
  - "Server location concentration in the Netherlands enabled domestic search-and-seizure powers to support the Dutch-led investigation, reducing reliance on formal MLAT for infrastructure access."
  - "Recovery of wallet access keys at the point of arrest produced direct cryptocurrency seizure rather than tracing-only outcomes."
source_count: 1
sources:
  - "[[2024-10-08_politie_bohemia-cannabia-darknet-marketplace-takedown]]"
created: 2026-05-09
updated: 2026-05-16
---
# Bohemia / Cannabia Darknet Marketplace Takedown (2024)

## Summary

On **8 October 2024** the Dutch National Police (Politie) publicly announced the takedown of **Bohemia / Cannabia** — described in the Politie statement as the largest and longest-running darkweb marketplace ever encountered by Dutch police. The market, hosting drug listings as well as cybercrime services such as malware and DDoS-for-hire, had peaked at an estimated **EUR 12 million in monthly turnover in September 2023** with approximately 82,000 daily advertisements and 67,000 monthly transactions before going offline at the end of 2023 in an apparent exit scam.

The case is *almost certainly* the highest-grossing darknet-marketplace investigation publicly attributed to a single Dutch-led probe to date (high confidence; primary attribution by Politie itself, corroborated by independent tier-2 reporting). The investigation was conducted by the **Politie Team High Tech Crime (THTC)** within the National Investigation and Intervention Unit, in cooperation with law enforcement in **Ireland, the United Kingdom and the United States** since late 2022.

## Background

Bohemia and its sister market Cannabia operated as a dual storefront under common administration. Tier-1 reporting indicates Dutch investigators opened the case towards the end of 2022 and continued working it after the operators took the markets offline at the end of 2023, despite the operators' apparent attempt to exit-scam users. The administrators were identified during the latter half of the investigation, leading to coordinated arrests in mid-2024.

## Participating Parties

### Lead and prosecution
- [[netherlands-politie|Politie]] — Team High Tech Crime (THTC), National Investigation and Intervention Unit. Led the investigation.
- [[netherlands-om|Openbaar Ministerie (OM)]] — Dutch public prosecution; the first arrested administrator was brought before the Rotterdam court.

### Foreign partners (explicitly named)
- [[ireland-garda|An Garda Síochána]] — Ireland; conducted the second administrator's arrest in August 2024.
- [[uk-nca|National Crime Agency (NCA)]] — United Kingdom.
- [[united-states|United States]] — "U.S. law enforcement" partner. One tier-2 outlet specifically names the U.S. Department of Justice; this is *likely* but not asserted as fact on this page absent direct primary confirmation.

> [!warning] Source coverage divergence — Germany / BKA
> One tier-2 outlet (The Record, 2024-10-09) listed Germany's Bundeskriminalamt among partners. Other tier-2 sources covering the same Politie statement (BleepingComputer, The Register) and the WebSearch index excerpt of the politie.nl page itself do **not** corroborate this. Per LESSONS.md L17 / L19, Germany is **not** asserted as a participant on this page until a direct primary-source fetch confirms it. If subsequent verification confirms BKA involvement, frontmatter and country links must be updated.

> [!note] Coordinating-body note
> Available source material does not explicitly attribute the original Bohemia/Cannabia takedown to Eurojust coordination or to a formal Joint Investigation Team. A separate downstream Europol-coordinated operation (Operation RapTor, May 2025) used Bohemia evidence to pursue buyers and sellers; that is a distinct operation and is not coded on this page.

## Legal Framework

No specific treaty (e.g. [[budapest-convention|Budapest Convention]]) is cited in the public Politie statement. The investigation appears to have proceeded through **bilateral informal police cooperation** ([[informal-cooperation]]) among NL, IE, UK and US partners, supported by Dutch domestic search-and-seizure powers because most of the marketplace infrastructure was hosted in the Netherlands. The first administrator's arrest was effected under Dutch criminal procedure following his arrival at Schiphol; the second under Irish authority.

## Operational Timeline

| Date | Event |
|---|---|
| Late 2022 | Politie THTC opens investigation into Bohemia/Cannabia. |
| Throughout 2023 | Joint investigation with IE, UK and US partners proceeds; operators allegedly become aware of police interest. |
| End of 2023 | Marketplace goes offline in an apparent exit scam by the operators. |
| Sep 2023 | Recorded peak monthly turnover of EUR 12 million (the metric on which the "world's largest" characterisation is based). |
| **2024-06-27** | First administrator (20-year-old British national) arrested at Schiphol Airport, Amsterdam. Electronic devices and Bitcoin wallet access keys seized. |
| August 2024 | Second administrator (23-year-old Irish national) arrested in Ireland by [[ireland-garda|An Garda Síochána]]. |
| **2024-10-08** | Politie publicly announces the takedown via press release. Suspect appears in Rotterdam court. |

## Results and Impact

| Metric | Value | Notes |
|---|---|---|
| Administrators arrested | 2 | NL (Schiphol), IE. Further arrests anticipated per Politie. |
| Cryptocurrency seized | > **EUR 8 million** | Combined seizure from both administrators' wallets, including keys recovered at Schiphol. |
| Servers seized | 3+ | Database server + crypto server + web server, most located in the Netherlands. |
| Marketplace status | Offline | Already exit-scammed end of 2023; takedown finalised infrastructure seizure and admin identification. |
| Forensic evidence | Yes | Politie statement: *"All data from the database server, crypto server and webserver have been seized and will be used for further investigation."* |

The marketplace metrics published by Politie:

- ~82,000 advertisements added per day worldwide.
- ~67,000 transactions per month.
- EUR 12 million peak monthly turnover (Sep 2023).
- ~EUR 5 million in estimated administrator profits prior to exit scam.
- ≥14,000 transactions valued at ~EUR 1.7 million attributed to sellers shipping from the Netherlands.

## Cooperation Mechanisms Used

- **[[informal-cooperation|Informal police cooperation]]** — bilateral channels among Politie THTC and counterpart cybercrime units in Ireland (Garda), the UK ([[uk-nca|NCA]]) and the United States. No formal JIT or Eurojust-facilitated framework is cited in the primary statement.
- **[[search-seizure|Search and seizure]]** — Dutch domestic powers used against marketplace infrastructure hosted in the Netherlands.
- **[[cryptocurrency-seizure|Cryptocurrency seizure]]** — direct seizure of Bitcoin wallets via access keys recovered at Schiphol; combined with separate seizures from the second administrator.
- **[[domain-seizure|Server / infrastructure seizure]]** — database, crypto and web servers placed under Politie control.

## Challenges and Friction Points

- **Exit-scam timing**: the operators took the market offline before law enforcement publicly moved, which *likely* removed real-time disruption value but did not prevent administrator identification.
- **Cross-border arrests**: the second administrator's arrest required Irish action; specific mechanism (informal handover, EAW, or other) is not detailed in available coverage.
- **Tier-1 source access**: the original Politie URL is behind Cloudflare bot protection and could not be WebFetch'd directly during this ingest (per [LESSONS.md](../../LESSONS.md) L11 / L13). All facts here are derived from triangulation across three tier-2 outlets covering the same statement; this is *almost certainly* sufficient for the reported facts but leaves residual uncertainty about partner-agency completeness (see Contradictions below).

## Lessons Learned

- A successful exit scam by marketplace operators does not preclude eventual law-enforcement attribution and arrest — multi-year investigative persistence can recover identities and proceeds even after the platform itself disappears (high confidence).
- Concentration of marketplace infrastructure in a single jurisdiction (in this case the Netherlands) provides a substantial cooperation-effort discount: partners contribute leads and arrests in their jurisdictions while the host country handles infrastructure seizure under domestic law (medium-high confidence).
- Direct seizure of cryptocurrency wallet keys at the point of physical arrest is operationally more productive than post-hoc tracing alone for marketplace-administrator cases (medium confidence; pattern observed across multiple recent darknet operations).

## Follow-Up Actions

- Politie indicated additional arrests are anticipated as analysis of seized infrastructure continues. Buyer/seller-side actions using the same data set surfaced via the Europol-coordinated **Operation RapTor** in May 2025 (treated as a distinct operation; not coded here).
- Direct fetch of the Politie press release via TLS-impersonating tooling (`tools/web_verify_tls.py`, per L20) is recommended to verify (a) U.S. agency identity, (b) presence/absence of Germany/BKA, (c) any Eurojust coordination language not surfaced in tier-2 summaries.

## Korean Involvement (한국의 참여)

No Korean agency, suspect, victim or jurisdictional element is identified in available source coverage. Korean involvement *almost certainly not* applicable to this operation (high confidence).

## Contradictions & Open Questions

> [!warning] Open question — Germany / BKA
> One tier-2 source (The Record) names Germany's Bundeskriminalamt among partners; other tier-2 sources do not. Resolution requires direct fetch of the Politie press release. Until then, Germany is **not** included in `participating_countries` or `participating_agencies`.

> [!warning] Open question — U.S. agency identity
> The Politie statement (per WebSearch and tier-2 summary) refers to "the United States" / "U.S. law enforcement". The Record specifies the U.S. Department of Justice. Other tier-2 outlets do not specify. The frontmatter therefore lists `[[united-states]]` as a participating country but does not assert a specific U.S. agency wikilink.

> [!warning] Open question — Eurojust / Europol coordination
> No Eurojust release matching the Politie URL pattern was located. The original takedown does not appear to have been Eurojust-coordinated. Operation RapTor (Europol-coordinated, May 2025) used Bohemia evidence but is downstream and operationally distinct.
