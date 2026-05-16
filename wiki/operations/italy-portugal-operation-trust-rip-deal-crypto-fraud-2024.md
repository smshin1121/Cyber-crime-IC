---
type: operation
title: "Italy–Portugal Operation Trust — Rip-Deal Cryptocurrency Fraud and Laundering Takedown (May 2024)"
aliases:
  - "Operation Trust"
  - "Operazione Trust"
  - "Milan Trust Rip-Deal"
  - "Italy-Portugal crypto Rip deal takedown 2024"
case_id: CYB-2024-996
period: 3
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: partial
timeframe:
  announced: 2024-05-31
  start: 2023-04-01
  end: 2024-05-31
  ongoing: false
crime_types:
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
crime_type: online-fraud-ic
target_entity: "Transnational \"Rip deal\" cryptocurrency-fraud and laundering network (Balkan-origin recruiters mostly resident in France; predominantly Asian crypto-launderers based in Italy)"
lead_agency: "[[italy-polizia-postale]]"
coordinating_body: ""
participating_countries:
  - "[[italy]]"
  - "[[portugal]]"
participating_agencies:
  - "[[italy-polizia-postale]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[europol-ec3]]"
legal_basis: []
mechanisms_used:
  - "[[joint-investigation-team]]"
  - "[[cryptocurrency-seizure]]"
  - "[[search-seizure]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "hundreds of thousands of euros (exact figure not disclosed)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "12 home and IT searches executed in Italy (Milano, Monza, Lodi, Roma, Torino, Cagliari, Nuoro)"
    - "numerous electronic devices seized"
edges:
  - source_actor: "italy-polizia-postale"
    target_actor: "portugal-policia-judiciaria"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "italy-polizia-postale"
    target_actor: "europol-ec3"
    cooperation_type: "technical_assistance"
    legal_basis: "unknown"
    direction: "directed"
  - source_actor: "portugal-policia-judiciaria"
    target_actor: "europol-ec3"
    cooperation_type: "technical_assistance"
    legal_basis: "unknown"
    direction: "directed"
credibility_index: 0.0
source_tier: 1
missing_fields:
  - exact_cryptocurrency_seized_value
  - portuguese_enforcement_results
  - defendant_identity
  - sentencing_status
related_cases: []
related_operations:
  - "[[portugal-spain-luso-angolan-cyber-fraud-money-laundering-eaw-2025]]"
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2024-05-31_poliziadistato-it_operazione-trust-frodi-informatiche-riciclaggio-criptovaluta]]"
created: 2026-05-16
updated: 2026-05-16
---

> [!info] Provisional stub
> This page is published at `source_count: 1` (single tier-1 primary release) pending corroborating Portuguese-side or Europol-side sources. Italian and Portuguese results, exact crypto-seizure figure, and defendant identification remain undisclosed in the released material. To be enriched when secondary tier-1 sources surface.

## Summary

Operation "Trust" (Italian: *operazione "Trust"*) was a joint Italian–Portuguese cybercrime investigation, with Europol technical support, into a transnational organisation specialising in cryptocurrency fraud and crypto money-laundering. The case was coordinated by the Milan Prosecutor's Office (procura di Milano) and operationally led by the Centro operativo per la sicurezza cibernetica della Lombardia, an Italian Polizia Postale regional cyber-security operations centre. Cooperation with Portugal's Polícia Judiciária ran throughout the investigation. On 31 May 2024 the Polizia di Stato announced the close of the operational phase: one arrest, 12 home and IT searches in seven Italian cities, seizure of numerous electronic devices, and seizure of hundreds of thousands of euros in cryptocurrency. The criminal scheme — referred to as a "Rip deal" — targeted digital-currency exchange operations and produced victims in at least six European countries.

## Background

Italian investigators opened the case on the complaint of two young Milanese entrepreneurs who had been targeted by perpetrators posing as representatives of an international investment fund. The recruiters offered the entrepreneurs an attractive financing package for their start-up and arranged "business meetings" in luxury restaurants and hotels. During the meetings the victims were induced to move large amounts of cryptocurrency via digital wallets or mobile-device apps. Before the deal was "finalised," the criminals confirmed that the victims held a real crypto guarantee fund, then — using technical-IT manipulation — drained the digital wallets of the victims, completing the theft before the victims understood what had happened.

The Polizia di Stato press release characterises the scheme as a long-standing "Rip deal" methodology, refitted for cryptocurrency exchanges (Bitcoin, Ethereum, Dogecoin, Stellar Lumen, etc.).

The over-one-year investigation identified two functional roles within the organisation:

- **Recruiters / interlocutors** — primarily of Balkan origin, mostly resident in France, who made first contact with victims and ran the in-person meetings.
- **Cryptocurrency launderers** — predominantly Asian, established in Italy, who handled the on-chain laundering of stolen crypto proceeds.

France-based recruitment activity and Asian-launderer roles are characterised by the issuing authority as offender-side attribution; neither French nor Asian-jurisdiction LE cooperation is named in the 31 May 2024 release, so France and the jurisdictions of the Asian launderers are not recorded as IC-cooperating jurisdictions on this page (see L24 — adversary/origin states do not qualify as `participating_countries`).

## Participating Parties

### Cooperating LE / prosecutorial authorities (named in the tier-1 release)

- **[[italy-polizia-postale|Italian Polizia Postale]] — Centro operativo per la sicurezza cibernetica della Lombardia (C.O.S.C. Lombardia)** — operational lead; conducted Italian searches.
- **[[portugal-policia-judiciaria|Polícia Judiciária (Portugal)]]** — Portuguese partner agency.
- **[[europol-ec3|Europol (EC3 / European Cybercrime Centre)]]** — technical support to the joint case.

### Coordinating prosecutor's office

- **Procura della Repubblica di Milano** (Milan Prosecutor's Office) — coordinated the Italian investigation. The press release does not state which Portuguese judicial authority coordinated on the Portuguese side.

### Cooperation jurisdictions (`participating_countries` frontmatter, per L24)

Italy and Portugal — the two jurisdictions whose LE / prosecutorial agencies are explicitly named in the primary release as collaborating on the investigation.

### Other countries referenced in the release (NOT IC-cooperating, body prose only)

- **Victim states**: Austria, Portugal, Romania, Spain, Switzerland and Italy ("Le vittime individuate provenivano da Austria, Portogallo, Romania, Spagna, Svizzera e Italia"). Of these, only Italy and Portugal have a named cooperating LE/prosecutorial counterpart in the release.
- **Offender base / recruitment**: France ("originari dei Balcani e per lo più residenti in Francia") — referenced as recruiter residence, no French LE counterpart named.
- **Offender origin**: Balkans (multiple states) — recruiter origin, no LE counterpart named.
- **Launderer origin**: predominantly Asian (jurisdictions unspecified) — no Asian LE counterpart named.

> [!note] Why France, Romania, Spain, Switzerland and Austria are not in `participating_countries`
> Per CLAUDE.md / LESSONS L24, `participating_countries` is restricted to jurisdictions whose LE or prosecutorial agencies are explicitly identified as cooperating partners in the tier-1 primary source. The 31 May 2024 Polizia di Stato release names only the Italian Polizia Postale / Lombardia cyber centre and the Portuguese Polícia Judiciária (plus Europol). Victim states and offender-base/origin states are recorded here in prose for analytic completeness but are not asserted as IC participants. If a Portuguese or Europol release surfaces naming additional LE partners, this list should be revised.

## Legal Framework

Not specified in the tier-1 release. The case is most consistent with a Europol-supported cooperation channel involving a bilateral information-sharing track between the Italian and Portuguese judicial police. The release does not state whether a formal joint investigation team (JIT) was established at Eurojust, or whether the cooperation ran through Europol's [[europol-jit|JIT support]] mechanism, a European Investigation Order ([[european-investigation-order]]) or another instrument.

> [!warning] Legal status check needed
> Specific legal instruments (EIO, JIT agreement, MLAT, voluntary cooperation) used between Italian and Portuguese authorities are not disclosed in the 31 May 2024 release. Pending corroborating Portuguese release.

## Operational Timeline

| Date | Event |
|---|---|
| 2023 (approx.) | Two Milanese entrepreneurs file a complaint with Italian authorities after a "Rip deal" attempt; investigation opens. |
| 2023 – May 2024 | Over a year of international investigation, coordinated by the Milan Prosecutor's Office and run by C.O.S.C. Lombardia, jointly with the Portuguese Polícia Judiciária and supported by Europol. |
| May 2024 (action day) | Operational phase: 1 arrest and 12 home/IT searches in Italy; seizure of devices and hundreds of thousands of euros in crypto. |
| 2024-05-31 | Polizia di Stato press release publicly announces Operation Trust. |

## Results and Impact

- **Arrests**: 1 (jurisdiction not specified in the release but presumed Italy, given Italian search locations).
- **Searches**: 12 home and IT searches, executed in Milano, Monza, Lodi, Roma, Torino, Cagliari, Nuoro.
- **Seizures**: numerous electronic devices; hundreds of thousands of euros in cryptocurrency (exact figure not disclosed).
- **Portuguese-side enforcement results**: not disclosed in the Italian release.
- **Victim impact**: an unspecified number of victims across Austria, Portugal, Romania, Spain, Switzerland and Italy were defrauded through the Rip-deal scheme; the release does not quantify aggregate losses.

The outcome is recorded here as `partial` because the release indicates a single Italian-side arrest against a transnational organisation with identified recruiter and launderer roles spread across France, the Balkans, Italy and Asian jurisdictions, none of whose foreign counterparts are reported as detained in this announcement.

## Cooperation Mechanisms Used

- **Italy–Portugal bilateral cooperation** between Polizia Postale (Lombardia C.O.S.C.) and Polícia Judiciária, sustained over more than a year.
- **[[europol-ec3|Europol EC3]] technical support** ("con il supporto di Europol"). The release does not state whether Europol hosted operational coordination meetings, deployed mobile offices on action day, or provided crypto-tracing analytics.
- **[[cryptocurrency-seizure]]** of multi-asset crypto (Bitcoin, Ethereum, Dogecoin, Stellar Lumen are all named in the release as currencies used in the scheme).
- **Domestic [[search-seizure]]** at seven Italian cities under the authority of the Milan Prosecutor's Office.

## Challenges and Friction Points

The release does not enumerate friction points. Implicit challenges visible from the case profile:

- **Multi-jurisdiction offender footprint** — recruiters in France, launderers based in Italy but ethnically tied to Asian jurisdictions, victim outreach across six countries. Only two LE jurisdictions appear to have actively cooperated in the public phase.
- **Crypto laundering across multiple chains** — the scheme used at least four named cryptocurrencies, increasing on-chain tracing complexity.
- **Asymmetric arrest outcome** — only one arrest publicly announced despite year-long investigation and identification of two functional groups within the organisation.

## Lessons Learned

To be added when corroborating Portuguese-side or Europol-side reporting becomes available.

## Follow-Up Actions

- Re-check Polícia Judiciária Portugal newsroom for a parallel Portuguese-language announcement that may name Portuguese arrests or seizures.
- Re-check Europol newsroom for a coordinated press release that may quantify aggregate damage and aggregate seizures across both jurisdictions.

## Korean Involvement (한국의 참여)

None reported. The release names no Asian LE counterpart and does not specify the precise Asian jurisdictions of the launderer cohort.

## Contradictions & Open Questions

- Exact cryptocurrency value seized (release only says "centinaia di migliaia di euro" — hundreds of thousands of euros). Open.
- Whether the single named arrest was in Italy or Portugal. Open — release implies Italy by location of searches but does not state explicitly.
- Whether any Portuguese arrests or searches occurred. Open — not reported in Italian release.
- Whether a formal Eurojust-supported JIT was established. Open.
- Identity of the arrested suspect. Not disclosed.
