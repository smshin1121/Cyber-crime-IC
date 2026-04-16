---
type: operation
title: "DE-CH Cryptocurrency Mixing Service Takedown (December 2025)"
title_ko: "독일-스위스 가상자산 믹싱 서비스 단속 (2025년 12월)"
aliases:
  - "Eurojust DE-CH Crypto Mixer Takedown 2025"
  - "Germany Switzerland Cryptocurrency Mixer Action"
case_id: "CYB-2025-013"
period: 3
operation_type: "infrastructure-seizure"
status: "completed"
enforcement_type:
  - "seizure"
  - "takedown"
  - "asset_freeze"
outcome: "partial"
timeframe:
  announced: "2025-12-01"
  start: ""
  end: "2025-12-01"
  ongoing: false
crime_type: "[[money-laundering-ic]]"
target_entity: "Unnamed cryptocurrency mixing service used to launder proceeds from drug trafficking, weapons trafficking, online fraud, and other cybercrimes"
lead_agency: "[[eurojust]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[germany]]"
  - "[[switzerland]]"
participating_agencies:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[mutual-legal-assistance|MLAT Process]]"
  - "[[europol-jit|Joint Investigation Team]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 3
  domains_seized: 0
  cryptocurrency_seized: "EUR 25 million"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "3 servers seized"
    - "Cryptocurrency mixing service infrastructure dismantled"
edges:
  - source_actor: "Germany"
    target_actor: "Switzerland"
    cooperation_type: "joint_investigation"
    legal_basis: "MLAT"
    direction: "undirected"
  - source_actor: "Eurojust"
    target_actor: "Germany"
    cooperation_type: "joint_investigation"
    legal_basis: "Budapest_Convention"
    direction: "directed"
  - source_actor: "Eurojust"
    target_actor: "Switzerland"
    cooperation_type: "joint_investigation"
    legal_basis: "bilateral_MOU"
    direction: "directed"
  - source_actor: "Europol"
    target_actor: "Germany"
    cooperation_type: "technical_assistance"
    legal_basis: "informal"
    direction: "directed"
credibility_index: 3.5
source_tier: 1
missing_fields:
  - "operation_name"
  - "service_name"
  - "arrests"
  - "indictments"
  - "start_date"
  - "specific_legal_basis_for_switzerland"
related_operations:
  - "[[cryptex-pm2btc-sanctions]]"
  - "[[2bagoldmule-qqaazz]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Bilateral DE-CH cooperation under Eurojust coordination can deliver significant cryptocurrency seizures even where one participant (Switzerland) is outside the EU"
source_count: 1
sources:
  - "[[2025-12-01-eurojust-de-ch-crypto-mixer-takedown]]"
created: 2026-04-14
updated: 2026-04-14
---

## Summary

On **1 December 2025**, [[eurojust|Eurojust]] announced that authorities from [[germany|Germany]] and [[switzerland|Switzerland]], together with Eurojust and [[europol-ec3|Europol]], had taken down a cryptocurrency mixing service suspected of being used by criminals to launder the proceeds of drug trafficking, weapons trafficking, online fraud, and other cybercrimes. During an action week, **more than EUR 25 million in cryptocurrency was seized and three servers were taken down**.

The Eurojust release does not name the service, the action lead in either country, or the number of arrests. The operation is *likely* one of a continuing series of EU-Switzerland cryptocurrency-laundering enforcement actions but cannot be linked to a publicly named campaign on the basis of the available source.

> [!note] Unnamed operation
> The mixing service and the operation itself are unnamed in the Eurojust press release. The wiki slug `de-ch-crypto-mixer-takedown-2025` is descriptive only. If a name surfaces in follow-up reporting, this page should be renamed.

## Background

Cryptocurrency mixing services (also called "tumblers") obfuscate the on-chain link between source and destination wallets by pooling funds from many users and redistributing them. They are a core piece of the cybercrime laundering pipeline and are used to conceal proceeds from:

- **Ransomware payments**
- **Drug trafficking** (darknet marketplaces)
- **Weapons trafficking**
- **Online fraud and BEC**
- **Other cybercrimes** (carding, account takeover, etc.)

Switzerland's role as a global financial hub and the location of the so-called "Crypto Valley" in Zug make it a *highly likely* host or operating jurisdiction for cryptocurrency-asset service providers. Germany's prosecutorial cybercrime infrastructure — particularly the [[germany-frankfurt-prosecutor|ZIT Frankfurt]] — is *almost certainly* one of the most active in continental Europe on cryptocurrency takedowns.

## Participating Parties

| Country | Role |
|---------|------|
| [[germany]] | Co-lead enforcement; *likely* prosecuted via ZIT Frankfurt or Bundeskriminalamt (BKA) — not stated in source |
| [[switzerland]] | Co-lead enforcement; *likely* coordinated through fedpol — not stated in source |

| Coordinating Body | Role |
|-------------------|------|
| [[eurojust]] | Judicial coordination, including DE-CH bilateral judicial cooperation |
| [[europol-ec3]] | Operational and analytical support |

> [!note] Source gap
> The Eurojust release does not specify which German or Swiss agencies led their respective national components. Switzerland's cooperation role is *likely* limited to asset freezing and server seizure on Swiss territory; this cannot be confirmed from the press release alone.

## Legal Framework

- **[[budapest-convention|Budapest Convention]]**: Both Germany (party 2009) and Switzerland (party 2011) are parties, providing the multilateral framework for cross-border preservation, search and seizure, and MLA.
- **Eurojust-Switzerland cooperation agreement**: Switzerland has a formal cooperation agreement with [[eurojust|Eurojust]] enabling judicial coordination on cross-border cases. This is *likely* the operative framework here, though the press release does not cite it explicitly.
- **National money laundering statutes**: German Strafgesetzbuch (StGB) §§ 261; Swiss Criminal Code (StGB/CP) art. 305bis.

## Operational Timeline

| Date | Event |
|------|-------|
| (Pre-2025) | Investigation initiated; specific start date not stated |
| Action week 2025 | Coordinated DE-CH seizure of 3 servers and EUR 25M+ in cryptocurrency |
| 2025-12-01 | Eurojust announces the takedown via press release |

## Results and Impact

| Metric | Value |
|--------|-------|
| Cryptocurrency seized | **EUR 25 million** (more than) |
| Servers seized | **3** |
| Arrests | not stated |
| Indictments | not stated |

The seizure is *likely* one of the largest single-operation EU-Switzerland cryptocurrency seizures of 2025 based on the disclosed figure, though the absence of an operation name and arrests count limits comparability against named campaigns such as [[cryptex-pm2btc-sanctions|Cryptex/PM2BTC]].

## Cooperation Mechanisms Used

1. **Bilateral DE-CH judicial cooperation** through Eurojust coordination
2. **Europol operational/analytical support** — *likely* including blockchain analytics and infrastructure mapping
3. **Mutual Legal Assistance** — *likely* invoked for cross-border server access and asset freezing

## Challenges and Friction Points

- **Crypto-asset jurisdictional complexity**: Mixing services typically distribute infrastructure across multiple hosting providers and chains.
- **Switzerland's non-EU status**: Coordination required additional bilateral channels rather than EU instruments alone.
- **Information opacity**: The release omits the service name, arrests count, and the specific legal basis used by Switzerland — limiting follow-up cross-checking.

## Lessons Learned

- Bilateral DE-CH cooperation under Eurojust can deliver significant cryptocurrency seizures even when one party (Switzerland) sits outside the EU.
- Eurojust's third-country cooperation agreements *likely* provide a sufficient procedural backbone for routine cross-jurisdictional crypto enforcement.

## Korean Involvement (한국의 참여)

No [[south-korea|South Korean]] participation is documented in this operation. Korean exchanges (Upbit, Bithumb) and the Korean Financial Intelligence Unit (KoFIU) are *likely* monitoring such mixer takedowns for follow-on intelligence on Korean-resident depositors.

## Contradictions & Open Questions

- **What is the name of the mixing service?** The Eurojust release does not identify it.
- **How many arrests, if any, were made?** Not stated in the source.
- **Which German prosecutor (ZIT Frankfurt? a Land prosecutor?) led the German component?** Not stated.
- **What was the legal basis used by Switzerland?** *Likely* the Eurojust-Switzerland cooperation agreement plus Swiss Criminal Code art. 305bis (money laundering), but not confirmed.
- **Is this operation linked to any larger campaign (e.g., Operation Endgame, a sanctions track)?** No linkage is stated in the source.


## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.
