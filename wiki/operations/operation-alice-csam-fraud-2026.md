---
type: operation
title: "Operation Alice — German-led 23-country takedown of 373,000+ dark web CSAM/CaaS-fraud onion domains (BLKA + ZKI + BKA + Europol, March 2026)"
title_ko: "Operation Alice — 독일 주도 23개국 다크웹 CSAM/CaaS 사기 도메인 373,000개 일제 단속 (BLKA + ZKI + BKA + Europol, 2026-03)"
aliases:
  - "Operation Alice 2026"
  - "Alice with Violence CP takedown"
  - "373000 dark web sites takedown"
  - "23-country CSAM dark web fraud takedown"
case_id: CYB-2026-079
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2026-03-21
  start: 2026-03-09
  end: 2026-03-19
  ongoing: false
crime_type: "[[csam-ic]]"
crime_types:
  - "[[csam-ic]]"
  - "[[online-fraud-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "Single-perpetrator dark web platform empire — a 35-year-old man based in the People's Republic of China who, between November 2019 and early 2026, operated up to 287 servers (peak), 105 of which were located in Germany, hosting 373,000+ Tor onion domains. Of those domains, 90,000+ advertised CSAM 'packages' (EUR 17–215, GB to TB sizes) for Bitcoin payment from Feb 2020 to Jul 2025; the remaining ~283,000 onion domains advertised cybercrime-as-a-service (CaaS) offerings (credit card data, access to foreign systems). The platforms were *purely fraudulent*: CSAM and CaaS goods were advertised and previewed but never delivered. Operator earned EUR 345,000+ in profit from approximately 10,000 paying customers worldwide; investigators identified 440 of those customers, with active prosecutions ongoing against 100+."
lead_agency: "[[germany-bka]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[australia]]"
  - "[[austria]]"
  - "[[belgium]]"
  - "[[canada]]"
  - "[[croatia]]"
  - "[[czechia]]"
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[hungary]]"
  - "[[italy]]"
  - "[[lithuania]]"
  - "[[netherlands]]"
  - "[[poland]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[slovenia]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[switzerland]]"
  - "[[ukraine]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[switzerland-fedpol]]"
  - "[[polizia-di-stato]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[spain-guardia-civil]]"
  - "[[uk-nca]]"
organizations:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
mechanisms_used:
  - "[[informal-cooperation]]"
legal_basis:
  - "Europol regulation (Regulation (EU) 2016/794) — basis for Europol analytical, intelligence-sharing, and coordination support."
  - "German criminal procedure governing the international arrest warrant against the 35-year-old PRC-based operator."
  - "23 national criminal-procedure regimes for CSAM offences applied to the customer-side prosecutions."
results:
  arrests: 0
  indictments: 0
  servers_seized: 105
  domains_seized: 373000
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Domains seized: 373,000+ Tor onion domains operated by a single perpetrator"
    - "Of seized domains: 90,000+ advertised CSAM 'packages' (Feb 2020–Jul 2025); ~283,000 advertised cybercrime-as-a-service (CaaS) offerings (credit card data, access to foreign systems)"
    - "Servers seized: 105 (out of 287 at peak network size, 105 located in Germany)"
    - "Operator: 1 individual identified — 35-year-old man based in the People's Republic of China; international arrest warrant issued by German authorities"
    - "Customers identified: 440 worldwide; 100+ subject to ongoing investigations"
    - "Operator profit (Feb 2020–Jul 2025): EUR 345,000+ from ~10,000 paying customers"
    - "CSAM 'package' price range advertised: EUR 17 to EUR 215 (paid in Bitcoin)"
    - "Investigation duration: ~5 years (from mid-2021 forensic investigation against 'Alice with Violence CP' platform identified in earlier reporting)"
    - "Pre-action precedent: August 2023, Bavarian BLKA searched home of a 31-year-old father who paid EUR 20 for a 70 GB package — convicted; demonstrating sustained customer-tracking capability years before the action sweep"
    - "Electronic devices seized: computers, mobile phones, electronic data carriers"
edges:
  - source_actor: germany-bka
    target_actor: europol-ec3
    cooperation_type: technical_assistance
    legal_basis: europol-regulation-2016-794
    direction: directed
  - source_actor: germany-bka
    target_actor: china
    cooperation_type: extradition_request
    legal_basis: international-arrest-warrant
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "name of the dark web platform — earlier media reporting identifies 'Alice with Violence CP' as the originating investigation target, but the Europol release does not name a single platform brand"
  - "specific arrest counts for the operator (the operator was 'identified' — international arrest warrant issued, but no apprehension is enumerated; he resides in PRC)"
  - "specific extradition request status China-Germany (the cited release notes only the international arrest warrant; PRC-Germany extradition arrangements are limited)"
  - "specific charges per jurisdiction against the 440 customers (CSAM-purchase or attempt-to-purchase varies by national criminal code)"
  - "specific cryptocurrency seizure totals beyond the EUR 345,000 operator profit figure"
  - "specific Eurojust JIT or coordination-meeting structure (the cited release frames Europol as the coordinator without explicit Eurojust JIT attribution)"
related_cases: []
related_operations: []
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "Largest documented dark-web onion-domain takedown in the wiki corpus by domain count: 373,000+ onion sites seized, dwarfing typical takedowns (tens of domains). Establishes a baseline for the *industrial-scale single-perpetrator* dark web fraud model."
  - "First wiki record of the **fraud-CSAM hybrid pattern** — a perpetrator simultaneously running 90,000+ CSAM-fraud onion domains and ~283,000 CaaS-fraud onion domains under a unified infrastructure. Adds a structural variant to the wiki's CSAM coverage (which has otherwise concentrated on actual-distribution platforms) and to its dark-web-marketplace coverage (which has concentrated on actually-traded goods)."
  - "Establishes the **paying-customer-as-suspect** prosecutorial model in CSAM-fraud cases — Europol explicitly framed paying customers as suspects 'even though they never received the material'. The *attempted purchase* itself becomes the predicate. This is structurally important because it broadens the prosecutable set beyond actual CSAM possession to include CSAM-purchase intent."
  - "23-country participation makes Operation Alice the **largest CSAM-related Europol-coordinated cooperation in the wiki corpus to date**, exceeding prior Europol-AFP/INTERPOL CSAM operations of comparable thematic scope."
  - "Documents the **PRC-based perpetrator + EU-located infrastructure pattern** — operator in PRC controlling 105 servers physically in Germany. The international-arrest-warrant route via Germany is the practical extradition mechanism in absence of a PRC-Germany extradition treaty governing this offence class — likely the upper bound of what is achievable in a non-cooperative-extradition jurisdiction."
  - "Demonstrates **multi-year customer-tracking capability** preceding action day: the August 2023 Bavarian BLKA search of a EUR 20 / 70 GB package customer (later convicted) shows ~2.5 years of pre-action customer-side investigation feeding into the March 2026 multi-country sweep."
  - "Suggests **cryptocurrency tracing as the dominant attribution mechanism** — Europol explicitly cites tracing Bitcoin payments and delivering intelligence to the countries involved as a key Europol contribution."
source_count: 1
sources:
  - "[[2026-03-21_europol_global-cybercrime-crackdown-373000-dark-web-sites-operation-alice]]"
created: 2026-05-09
updated: 2026-05-09
---

## Summary

**Operation Alice** (action days **9–19 March 2026**, press release **21 March 2026**) was a German-led, **23-country**, Europol-coordinated takedown of a single-perpetrator dark web platform empire comprising **373,000+ Tor onion domains** that *fraudulently advertised* CSAM and cybercrime-as-a-service (CaaS) products without delivering them. The operator — a **35-year-old man based in the People's Republic of China** — operated up to 287 servers at peak (Nov 2019–early 2026), of which 105 were located in Germany. Between February 2020 and July 2025 he advertised CSAM 'packages' (EUR 17–215, GB to TB sizes) for Bitcoin payment on **90,000+** of the onion domains, while the remaining ~283,000 onion sites advertised CaaS offerings (credit card data, access to foreign systems). Operator profit: **EUR 345,000+** from ~10,000 paying customers; **440 customers** identified worldwide (100+ subject to ongoing investigations).

> [!note] Largest dark-web onion-domain takedown by site count
> 373,000+ onion sites is the largest documented dark-web onion-domain takedown in this wiki corpus by site count. The pattern — *one operator, vast onion-domain footprint, fraudulent advertising of CSAM and CaaS* — is structurally distinct from actually-distributing CSAM platforms (e.g., [[archetyp-market-takedown-operation-deep-sentinel-2025|Archetyp Market]]) and from genuinely-trading dark-web marketplaces.

## Background

The investigation began with the dark web platform commonly identified in earlier media reporting as 'Alice with Violence CP' (operation namesake). Over **nearly five years** of investigation, German authorities — led by the Bavarian State Criminal Police Office (BLKA), the Bavarian Central Office for the Prosecution of Cybercrime (ZKI), and the Federal Criminal Police Office (BKA) — established that a single individual was operating an industrial-scale onion-domain hosting empire across two parallel deception verticals:

1. **CSAM-fraud track** (90,000+ onion domains, Feb 2020–Jul 2025): advertised CSAM 'packages' for Bitcoin (EUR 17–EUR 215, GB to TB volumes), accepted payment, but never delivered material.
2. **CaaS-fraud track** (~283,000 onion domains): advertised credit card data, access to foreign systems, and other CaaS offerings without delivering them.

The Bavarian BLKA established multi-year customer-tracking capability before action day. In August 2023 — roughly two and a half years before the March 2026 sweep — BLKA searched the home of a 31-year-old father who had transferred EUR 20 to purchase a 70 GB CSAM package; the man was later convicted for the *attempted* CSAM purchase. This established the **paying-customer-as-suspect** prosecutorial model that scaled to the 440 worldwide customers identified during Operation Alice.

## Participating Parties

| Country | Lead Agency / Unit |
|---|---|
| Australia | Australian Federal Police (AFP) |
| Austria | Criminal Intelligence Service (Bundeskriminalamt) |
| Belgium | Federal Judicial Police (Federale Gerechtelijke Politie) |
| Canada | Royal Canadian Mounted Police (RCMP) – National Child Exploitation Crime Centre (NCECC) |
| Croatia | National Cybercrime Department (Služba kibernetičke sigurnosti) |
| Czech Republic | Czech National Police (USKPV) Bureau of Criminal Police and Investigation Service |
| Denmark | National Cyber Crime Centre (NC3) Special Crime Unit (SCU/NSK) and Danish National Police |
| France | Police department for the protection of children (OFMIN) of the National Directorate of Judicial Police (DNPJ) |
| Germany | **Lead** — Bavarian State Criminal Police (BLKA), Bavarian Central Office for the Prosecution of Cybercrime (ZKI), Federal Criminal Police Office (BKA) |
| Hungary | National Bureau of Investigation Cybercrime Department |
| Italy | National Police – Postal and Cyber Security Police Service (Polizia Postale) |
| Lithuania | Lithuanian Criminal Police Bureau |
| Netherlands | National Police (Politie) |
| Poland | Central Cybercrime Bureau (CBZC) |
| Portugal | Judicial Police (Polícia Judiciária) |
| Romania | Romanian Police (Poliția Română) |
| Slovenia | Slovenian Criminal Police |
| Spain | Guardia Civil – Criminal Intelligence Unit (UTPJ) and Central Investigations Unit (UCO) |
| Sweden | National Cybercrime Centre (SC3), regional units (Syd, Väst, Bergslagen) |
| Switzerland | Federal Office of Police fedpol; Lucerne Police; Cantonal Police of St. Gallen, Thurgau, Zurich |
| Ukraine | National Police of Ukraine |
| United Kingdom | National Crime Agency (NCA) |
| United States | Homeland Security Investigations (HSI) |
| EU coordinator | **Europol** (information exchange, analytical support, cryptocurrency tracing, intelligence delivery to participating countries) |

## Legal Framework

- **Europol regulation (Regulation (EU) 2016/794)** — basis for Europol analytical, intelligence-sharing, and coordination support, and for tracing cryptocurrency payments.
- **German criminal procedure** — basis for the *international arrest warrant* against the 35-year-old PRC-based operator (the practical extradition route in absence of a PRC-Germany extradition treaty governing this offence class).
- **23 national CSAM-and-cybercrime statutes** — basis for the customer-side prosecutions worldwide. The cited release does not enumerate per-jurisdiction charges.

> [!warning] Legal status check needed
> The cited release does not enumerate the specific national CSAM statutes that ground the customer-side prosecutions in each of the 23 jurisdictions. Whether the *attempted-purchase* theory survives in each jurisdiction (common-law vs. civil-law variation) is not addressed in the source.

## Operational Timeline

| Date | Event |
|---|---|
| Nov 2019 | Operator's network of up to 287 servers begins operation |
| Feb 2020 – Jul 2025 | CSAM fraud advertising on 90,000+ onion domains; ~10,000 paying customers transact via Bitcoin |
| mid-2021 | German authorities open investigation against the 'Alice with Violence CP' dark web platform |
| Aug 2023 | Bavarian BLKA searches home of 31-year-old father who paid EUR 20 for 70 GB package — first documented customer-side enforcement (later convicted) |
| 9–19 March 2026 | Operation Alice action days — 23 countries, 373,000+ onion domains shut down, 105 servers seized in Germany, 440 customers identified |
| 21 March 2026 | Europol Newsroom press release announcement |

## Results and Impact

| Metric | Value | Notes |
|---|---|---|
| Onion domains shut down | **373,000+** | 90,000+ advertised CSAM; ~283,000 advertised CaaS |
| Servers seized | **105** | All located in Germany (out of 287 at peak network size) |
| Operator identified | **1** | 35-year-old man, PRC; international arrest warrant issued |
| Customers identified | **440 worldwide** | 100+ subject to ongoing investigations |
| Operator profit | **EUR 345,000+** | ~10,000 paying customers, Feb 2020–Jul 2025, Bitcoin payment |
| CSAM 'package' prices | EUR 17 – EUR 215 | Advertised data volumes: GB to TB |
| Electronic devices seized | many | Computers, mobile phones, data carriers |

## Cooperation Mechanisms Used

- **Europol-coordinated 23-country information exchange and analytical support** — the central coordination format
- **Cryptocurrency tracing and intelligence delivery** — Europol contribution explicitly cited as 'key role in tracing cryptocurrency payments and delivering intelligence to the countries involved'
- **German-issued international arrest warrant** — the extradition pathway against the PRC-based operator (no specific PRC-Germany cooperation channel cited)
- **National-jurisdiction customer prosecutions** — 23 national criminal-procedure regimes applied in parallel to the 440 identified customers

## Challenges and Friction Points

- **PRC-based operator vs. German-located infrastructure** — operator physically located in PRC while 105 of 287 servers were located in Germany. The *international arrest warrant* route is the practical extradition mechanism in absence of a PRC-Germany extradition treaty for this offence class — *likely* the upper bound of what is achievable in a non-cooperative-extradition jurisdiction.
- **Customer-side prosecutorial heterogeneity** — the *attempted-purchase* theory of CSAM liability varies across the 23 jurisdictions (common-law vs. civil-law). Whether all 440 customers face equivalent charges is *unlikely* given that variation.
- **Sheer onion-domain scale** — 373,000+ onion domains is operationally distinct from typical takedowns (tens of domains). The claim that *one perpetrator* operated all of them suggests an automated provisioning system; the cited release does not specify how the 373,000 onion-domain inventory was generated technically.
- **CaaS half (283,000 domains)** — the cited release devotes most attention to the CSAM half (90,000 domains, EUR 345,000 profit) but provides no detail on the financial scale or victim-impact of the larger CaaS half. The CaaS-fraud track is the larger volume but the lower-profile output of the operation.

## Lessons Learned

1. **Largest dark-web onion-domain takedown in the wiki corpus**. 373,000+ onion sites dwarf typical takedown counts and establish a benchmark for industrial-scale single-perpetrator fraud.
2. **Fraud-CSAM hybrid model**. A single operator running 90,000 CSAM-fraud + 283,000 CaaS-fraud onion domains under unified infrastructure is a structural variant not previously documented in the wiki — distinct from actual-distribution CSAM (e.g., previous CSAM-marketplace takedowns) and from genuinely-trading dark-web markets (e.g., [[archetyp-market-takedown-operation-deep-sentinel-2025|Archetyp]]).
3. **Paying-customer-as-suspect prosecutorial model**. Customers prosecuted under their national CSAM laws even though no CSAM was actually delivered — the *attempted purchase* is the predicate. This broadens the prosecutable set beyond actual CSAM possession.
4. **23-country participation** is the largest CSAM-related Europol-coordinated cooperation in the wiki corpus to date.
5. **Cryptocurrency tracing as primary attribution mechanism** — Europol's contribution centres on Bitcoin tracing and intelligence delivery, suggesting that for cross-jurisdictional fraud-CSAM cases the financial-flow vector dominates the IP-attribution vector.
6. **Multi-year customer-tracking capability** (August 2023 BLKA search → March 2026 multi-country sweep) demonstrates that customer-side enforcement is not bound to action-day timing — individual prosecutions can precede the takedown by years.

## Follow-Up Actions

- Ongoing customer-side prosecutions in 100+ open investigations across the 23 participating jurisdictions.
- German extradition/apprehension efforts against the 35-year-old PRC-based operator under the international arrest warrant — outcome dependent on PRC cooperation or third-country apprehension.

## Korean Involvement (한국의 참여)

[[south-korea|South Korea]] is *not listed* among the 23 participating countries in Operation Alice. The operation's diaspora and customer-base is global; Korean customer presence is *unknown* from the cited release. Bilateral Germany-Korea cooperation channels (KNPA Cyber Bureau ↔ BKA) could in principle handle Korea-side leads not surfaced here.

## Contradictions & Open Questions

- The Europol release does not name the specific dark-web platform brand. Earlier media reporting (CyberNews, BitDefender) identifies the platform as 'Alice with Violence CP', from which the Operation Alice name derives.
- The 287-vs-105 server count is internally consistent (105 in Germany at peak, 287 worldwide network) but raises an open question on whether the remaining ~182 servers (at peak) were located in non-participating jurisdictions and remain operational.
- The CaaS half (~283,000 onion domains) is under-described — its CaaS catalogue (credit card data, access to foreign systems) is enumerated but not quantified in financial-impact terms.
- The release does not specify whether Eurojust facilitated judicial coordination via JIT or coordination meetings; only Europol is named as the coordinator.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-03-21_europol_global-cybercrime-crackdown-373000-dark-web-sites-operation-alice\|Global cybercrime crackdown: over 373 000 dark web sites shut down (Operation Alice)]] | Europol | 2026-03-21 | https://www.europol.europa.eu/media-press/newsroom/news/global-cybercrime-crackdown-over-373-000-dark-web-sites-shut-down |
