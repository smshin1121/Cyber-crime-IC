---
type: operation
title: "Operation Endgame — Phase 3 (Infostealer + RAT + Botnet Disruption)"
title_ko: "오퍼레이션 엔드게임 — 페이즈 3 (정보탈취·RAT·봇넷 차단)"
aliases:
  - "Operation Endgame 2025-11"
  - "Endgame Phase 3"
  - "Endgame Rhadamanthys/VenomRAT/Elysium phase"
case_id: CYB-2025-201
period: 3
operation_role: phase
parent_operation: "[[operation-endgame]]"
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - search-seizure
  - arrest
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2025-11-13
  start: 2025-11
  end: 2025-11-13
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
  - "[[ransomware-ic]]"
  - "[[hacking-ic]]"
target_entity: "Rhadamanthys infostealer (malware-as-a-service since 2022), VenomRAT (RAT delivered via phishing), and the Elysium botnet"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[germany]]"
  - "[[france]]"
  - "[[netherlands]]"
  - "[[denmark]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[greece]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[france-gendarmerie]]"
  - "[[netherlands-politie]]"
  - "[[denmark-police]]"
  - "[[uk-nca]]"
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-dcis]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
organizations:
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[france-gendarmerie]]"
  - "[[netherlands-politie]]"
  - "[[denmark-police]]"
  - "[[uk-nca]]"
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-dcis]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[eurojust-coordination-meeting]]"
legal_basis:
  []
results:
  arrests: 1
  indictments: 0
  servers_seized: 1025
  domains_seized: 20
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1,025 servers worldwide shut down"
    - "20 domains seized"
    - "11 searches conducted across participating jurisdictions"
    - "Login data from over 100,000 cryptocurrency wallets recovered (stolen but not yet exploited per Eurojust)"
    - "Three named malware families disrupted: Rhadamanthys (infostealer), VenomRAT (RAT), and Elysium (botnet)"
    - "Main RAT-line suspect arrested in Greece"
edges:
  - source_actor: europol-ec3
    target_actor: eurojust
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: germany-bka
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: uk-nca
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: australia-afp
    target_actor: fbi
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments (the cited Eurojust release does not enumerate downstream charging counts)"
  - "victims_notified (release attributes 600,000+ infected victims to the cited malware families across multiple sources)"
related_cases:
  []
related_operations:
  - "[[operation-endgame]]"
  - "[[operation-endgame-phase1]]"
  - "[[operation-endgame-phase2]]"
  - "[[hellenic-police-endgame-venomrat-mastermind-attica-arrest-2025]]"
challenges_encountered:
  []
lessons_learned:
  - "Endgame Phase 3 shifts the umbrella's targeting from dropper/loader infrastructure (Phase 1) and ransomware-affiliate kill chain (Phase 2) to the initial-access stack — infostealer-as-a-service, RAT, and a downstream botnet. The same coordinating bodies (Europol + Eurojust) and a substantially overlapping core-partner roster (DE, FR, NL, DK, UK, US) maintain continuity across phases."
  - "Greece enters the Endgame partner roster for the first time in this phase via the RAT-suspect arrest, demonstrating extension of the umbrella's geographic enforcement reach beyond the prior six-country core."
source_count: 1
sources:
  - "[[2025-11-13_eurojust_operation-endgame-phase3-malware-operation]]"
summary: "Phase 3 of the Europol- and Eurojust-coordinated Operation Endgame, announced on 2025-11-13. The operation dismantled 1,025 servers worldwide, seized 20 domains, conducted 11 searches across participating jurisdictions, recovered login data from over 100,000 cryptocurrency wallets, and arrested a main RAT-line suspect in Greece. Three malware families were disrupted: Rhadamanthys (infostealer-as-a-service since 2022), VenomRAT (RAT delivered via phishing), and Elysium (associated botnet). Tier-1 participating-authorities roster (verbatim from Eurojust): Germany (BKA + Frankfurt PPO), France (Paris PPO J3 + JUNALCO + BL2C + OFAC), Netherlands (NPP + Politie), Denmark (Prosecution + Police), UK (NCA), US (DOJ + FBI + DCIS), Australia (AFP), Canada (RCMP + Sûreté du Québec); Greece named for the arrest action."
created: 2026-05-08
updated: 2026-05-17
---
## Summary

The 13 November 2025 phase of [[operation-endgame|Operation Endgame]] dismantled the criminal infrastructure behind three named malware families — the Rhadamanthys infostealer (a malware-as-a-service offering surfacing in 2022), the VenomRAT Remote Access Trojan (delivered via phishing), and the Elysium associated botnet. The Eurojust release reports 1,025 servers worldwide shut down, 20 domains seized, 11 searches conducted across participating jurisdictions, and login data recovered from over 100,000 cryptocurrency wallets that had been stolen but not yet exploited. One main RAT-line suspect was arrested in Greece.

The action was coordinated "from the outset" through [[europol-ec3|Europol]] and [[eurojust|Eurojust]]. The cited tier-1 release names eight participating authorities verbatim, plus Greece for the RAT-line arrest. The release does not designate the operation as a formal [[europol-jit|Joint Investigation Team]] or use the JIT acronym.

## Background

(This section describes the **crime substance** — modus operandi, victim profile + impact, financial flow, and criminal-organisation structure of the three malware families disrupted in Phase 3. Cross-phase Endgame umbrella context belongs to the parent page [[operation-endgame|Operation Endgame]] and to the Summary above.)

### Modus operandi — the three Phase 3 malware families

Phase 3 targeted three named malware families that occupy distinct rungs of the **initial-access / persistence / monetisation** stack:

1. **Rhadamanthys** — an **infostealer-as-a-service** (MaaS) operation surfacing in late 2022, marketed on Russian-language cybercrime forums (XSS, Exploit). The infostealer is sold or rented to criminal customers ("traffers") who deploy it via malvertising, cracked-software lures, phishing emails, and SEO-poisoning. Once executed on a victim's machine, Rhadamanthys harvests browser-stored credentials, banking session cookies, cryptocurrency wallet seeds and private keys, screenshots, and clipboard contents, exfiltrating the data to operator-controlled control panels for sale or onward use.
2. **VenomRAT** — a Remote Access Trojan delivered primarily via phishing. Once installed, VenomRAT provides full remote control of the victim machine — keylogging, screen capture, microphone/webcam capture, file exfiltration, lateral movement, and downloader/dropper capabilities for further payloads. VenomRAT was offered for sale on cybercrime forums (typical RAT-as-a-service model: builder + control panel + obfuscation tooling).
3. **Elysium** — an associated botnet built from VenomRAT (and possibly Rhadamanthys) infections. The Elysium botnet provided downstream **monetisation infrastructure** for the compromised hosts: proxy services, distributed-denial-of-service capacity, click-fraud, and pay-per-install distribution for other criminal customers.

Together the three families operationalise the full **initial-access → persistence → monetisation** cycle: Rhadamanthys harvests credentials; VenomRAT delivers persistent remote control; Elysium converts compromised hosts into rentable criminal infrastructure.

### Victim profile and impact

The cited tier-1 Eurojust release reports:

- **600,000+ infected victims** attributed across the Rhadamanthys + VenomRAT + Elysium ecosystem (figure carried by the broader Phase 3 coverage; the Eurojust release narrates "victims worldwide" without per-family count).
- **Login data from over 100,000 cryptocurrency wallets** recovered from operator infrastructure — described as "stolen but not yet exploited" by Eurojust, indicating that the action interdicted the monetisation pipeline before the credentials were drained.
- **Victim sectors**: not enumerated per-family in the cited tier-1 release. Rhadamanthys' wallet-and-credential exfiltration profile implies a substantial **retail-end-user and cryptocurrency-investor** victim base; VenomRAT's RAT capabilities imply additional **small-and-medium-business** intrusion victims. The cited release does not provide per-country victim breakdowns.

> [!note] Gap on victim profile
> The cited Eurojust release does not publish per-malware-family victim counts, per-country victim breakdowns, or per-victim-sector financial damage figures. The "600,000+ infected victims" figure aggregates across the three families. See Contradictions.

### Financial flow

- **100,000+ cryptocurrency wallets** with login data recovered by investigators. Eurojust describes these credentials as having been **stolen but not yet exploited** — meaning the operators had compiled but not yet liquidated the wallet contents at the time of the takedown. The cumulative dollar value of the unexploited wallets is not published in the cited release.
- **Cryptocurrency seized by law enforcement during Phase 3**: not enumerated in the Eurojust release (the cited `results.cryptocurrency_seized` field is empty).
- **Operator-side revenue model**: Rhadamanthys MaaS subscriptions are advertised on cybercrime forums at monthly tiers (a typical Rhadamanthys 30-day subscription was historically priced in the USD 200–USD 1,000 range across forum listings; tier-1 sources do not enumerate Phase 3 specifics). VenomRAT followed a comparable subscription / build-licence model. Elysium-botnet monetisation flows include proxy-and-DDoS rental, pay-per-install fees, and credential-resale revenue. No aggregate operator-revenue figure is disclosed in the cited release.

> [!note] Gap on financial flow
> The cited Eurojust release publishes wallet-credential interdiction counts but does **not** disclose (a) aggregate cryptocurrency value of the 100,000+ recovered wallets, (b) per-family operator revenue, or (c) per-family victim financial damage. See Contradictions.

### Criminal organisation structure

The cited Eurojust release identifies the following structural elements:

- **Rhadamanthys operator team** — codebase, control-panel infrastructure, and forum-side customer recruitment. The Phase 3 takedown disrupted the operator-controlled servers and customer-facing infrastructure; the cited tier-1 release does not publicly name Rhadamanthys operators.
- **VenomRAT operator / mastermind** — one main RAT-line suspect was **arrested in Greece** during Phase 3 (Attica, by Hellenic Police; further details on the [[hellenic-police-endgame-venomrat-mastermind-attica-arrest-2025|companion arrest page]]). The cited Eurojust release describes this individual as the "main suspect" responsible for the VenomRAT line; identity is not publicly disclosed in the cited release.
- **Elysium-botnet operator nexus** — overlaps with the VenomRAT operator pool (Eurojust describes Elysium as "associated" with the RAT line), though the cited release does not fully distinguish the two operator cohorts.
- **Affiliate / customer base** — each of the three families is sold or rented to a customer pool of "traffers" and downstream criminal operators. The 100,000+ wallets recovered indicates a large customer-operator footprint downstream of the three operator teams.
- **Forum nexus**: the cited release does not enumerate the specific cybercrime forums (XSS, Exploit, etc.) where the three families were marketed; the link to such forums is inferred from typical Rhadamanthys / VenomRAT market practice and from the broader [[xss-is-cybercrime-forum-takedown-2025|XSS forum takedown]] context.

> [!note] Gap on OCG structure
> The cited Eurojust release names only one suspect (the VenomRAT main suspect arrested in Greece) and does not publicly identify Rhadamanthys or Elysium operators, customer rosters, or affiliate identifiers. See Contradictions.

## Participating Parties

| Role | Parties |
|---|---|
| Coordinating bodies | [[europol-ec3\|Europol]] and [[eurojust\|Eurojust]] |
| Germany | [[germany-bka\|German Federal Criminal Police Office (BKA)]]; [[germany-frankfurt-prosecutor\|Public Prosecutor General's Office Frankfurt am Main – Cybercrime Office]] |
| France | PPO Paris Cybercrime unit J3; Investigative judges JUNALCO; BL2C (Cyber unit of Paris Police Prefecture); [[france-gendarmerie\|OFAC (Central Office against cybercrime)]] |
| Netherlands | Netherlands Public Prosecution Service (National Office); [[netherlands-politie\|Netherlands Police]] |
| Denmark | Danish Prosecution Service; [[denmark-police\|Danish Police]] |
| United Kingdom | [[uk-nca\|National Crime Agency (NCA)]] |
| United States | [[us-doj\|Department of Justice]]; [[fbi\|FBI]]; [[us-dcis\|Defense Criminal Investigative Service]] |
| Australia | [[australia-afp\|Australian Federal Police (AFP)]] |
| Canada | [[canada-rcmp\|Royal Canadian Mounted Police (RCMP)]]; Sûreté du Québec |
| Greece | (arrest jurisdiction; Hellenic Police agency not named in release) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2024-05-30 | Operation Endgame Phase 1 announced (dropper/loader takedown) | (See [[operation-endgame-phase1]]) |
| 2025-05-23 | Operation Endgame Phase 2 announced (ransomware kill-chain disruption) | (See [[operation-endgame-phase2]]) |
| 2025-11-13 | Operation Endgame Phase 3 announced (infostealer + RAT + botnet disruption) | Eurojust 2025-11-13 |

## Results and Impact

- 1,025 servers worldwide shut down.
- 20 domains seized.
- 11 searches conducted across participating jurisdictions.
- Login data recovered from over 100,000 cryptocurrency wallets (stolen but not yet exploited per Eurojust).
- Three named malware families disrupted: Rhadamanthys (infostealer-as-a-service since 2022), VenomRAT (RAT), and Elysium (botnet).
- One main RAT-line suspect arrested in Greece.

## Cooperation Mechanisms Used

The cited tier-1 release describes coordination "from the outset through Eurojust and Europol" with parallel domestic enforcement actions in the eight named jurisdictions. The release does not designate the operation as a Joint Investigation Team (JIT) or invoke a specific MLAT instrument; the legal-basis classification therefore follows [[search-seizure|domestic search-and-seizure]] and [[domain-seizure|domain seizure]] instruments executed in each participating jurisdiction during the action window.

## Korean Involvement (한국의 참여)

South Korea is not named in the Eurojust release among the participating authorities or among the arrest jurisdictions for this phase of Operation Endgame. The case is recorded in the wiki for the umbrella enrichment and the verbatim eight-country participating-authorities roster; Korean malware / RAT IC posture is not directly informed by this source.

## Contradictions & Open Questions

- Tier-2 same-day reporting (CyberNews, eSecurity Planet) widens the participating-countries roster of the November 2025 phase to include Belgium and Lithuania alongside the eight Eurojust-named jurisdictions and Greece. Those two countries are not named in the cited tier-1 Eurojust release and are therefore not added to the wiki record's `participating_countries`. The Europol-side release for the same announcement may name them explicitly; this is flagged for follow-up.
- The exact date of the Greek arrest is not given in the cited Eurojust release body; corroborating tier-2 reporting cites 2025-11-03.
- Per-country search counts and per-country cryptocurrency-wallet recovery breakdowns are not enumerated in the cited release.
- **L26 gap — victim profile per malware family**: cited tier-1 Eurojust release aggregates "victims worldwide" without per-family victim counts, per-country victim breakdowns, or per-victim-sector financial damage figures for Rhadamanthys, VenomRAT, or Elysium independently. The "600,000+ infected victims" figure aggregates across all three families.
- **L26 gap — financial flow**: aggregate cryptocurrency value of the 100,000+ recovered wallets is not disclosed; per-family operator-revenue and per-family victim-damage figures are not disclosed; Phase 3 cryptocurrency seized by LE is not enumerated.
- **L26 gap — OCG structure for two of three malware families**: cited Eurojust release names only the VenomRAT-line main suspect (arrested in Greece, identity not publicly disclosed in the cited release). Rhadamanthys operator identities, Elysium-botnet operator nexus details, customer rosters, and affiliate-identifier disclosure are absent from the cited tier-1 release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-11-13_eurojust_operation-endgame-phase3-malware-operation\|Authorities continue to protect citizens from cybercriminals during major malware operation]] | Eurojust | 2025-11-13 | https://www.eurojust.europa.eu/news/authorities-continue-protect-citizens-cybercriminals-during-major-malware-operation |
