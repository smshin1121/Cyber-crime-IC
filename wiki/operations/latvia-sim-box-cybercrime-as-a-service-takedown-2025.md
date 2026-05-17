---
type: operation
title: "Latvia SIM-Box Cybercrime-as-a-Service Network Takedown (2025)"
title_ko: "라트비아 SIM-박스 CaaS 네트워크 단속 (2025)"
aliases:
  - "Latvia SIM-box CaaS takedown"
  - "gogetsms apisim takedown"
case_id: CYB-2025-203
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - arrest
  - search-seizure
  - asset-freeze
  - online-content-takedown
outcome: success
timeframe:
  announced: 2025-10-17
  start: 2025-10
  end: 2025-10-17
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[online-fraud-ic]]"
  - "[[hacking-ic]]"
target_entity: "Latvian-hosted SIM-box cybercrime-as-a-service (CaaS) network operating gogetsms.com and apisim.com — offering rented telephone numbers from 80+ countries for smishing, phishing, fraud, extortion, migrant smuggling, CSAM distribution, daughter-son scams, investment fraud, fake shops, fake bank websites, and fake-police-officer schemes"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[latvia]]"
  - "[[austria]]"
  - "[[estonia]]"
  - "[[finland]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[finland-nbi]]"
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[finland-nbi]]"
mechanisms_used:
  - "[[europol-jit]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[asset-freezing]]"
  - "[[public-private-cooperation]]"
legal_basis:
  - "Joint Investigation Team (JIT) — partners Austria, Estonia, Latvia; supporting jurisdiction Finland"
results:
  arrests: 5
  indictments: 0
  servers_seized: 5
  domains_seized: 2
  cryptocurrency_seized: "USD 333,000"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "26 searches carried out"
    - "approximately 1,200 SIM-box devices seized, operating 40,000 SIM cards"
    - "Hundreds of thousands of further SIM cards seized"
    - "2 websites (gogetsms.com and apisim.com) taken over by law enforcement"
    - "EUR 431,000 frozen in suspects' bank accounts"
    - "USD 333,000 frozen in suspects' cryptocurrency accounts"
    - "4 luxury vehicles seized"
    - "Title of the cited Europol release says '7 arrested' but the verbatim body records 5 action-day arrests; the 5-figure is used as `results.arrests` and the title figure is flagged"
    - "More than 49 million online accounts allegedly created via the illegal SIM-box service"
    - "Telephone numbers from 80+ countries source-jurisdictions, used to register the rented numbers"
edges:
  - source_actor: europol-ec3
    target_actor: latvia
    cooperation_type: joint_investigation
    legal_basis: europol-jit
    direction: undirected
  - source_actor: europol-ec3
    target_actor: austria
    cooperation_type: joint_investigation
    legal_basis: europol-jit
    direction: undirected
  - source_actor: europol-ec3
    target_actor: estonia
    cooperation_type: joint_investigation
    legal_basis: europol-jit
    direction: undirected
  - source_actor: europol-ec3
    target_actor: finland-nbi
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments (post-action-day charging not enumerated)"
  - victims_notified
related_cases:

related_operations:
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[latvia-phone-fraud-money-mule-network-takedown-2026]]"
challenges_encountered:

lessons_learned:
  - "The cited Europol release is one of the wider verbatim public-record CaaS-tier-prosecution captures in the wiki corpus, with a detailed enumeration of crime-types-enabled by the network and explicit private-sector cooperation with the Shadowserver Foundation for technical infrastructure dismantling."
  - "The fake-police-officer-against-Russian-speaking-victims scheme is a notable IC-relevant data point that overlaps with the broader 2025-2026 EU-wide Russian-speaking-victim cybercrime targeting pattern, including the Korea-Russian-victim Phobos prosecution context (Ptitsyn) and broader Russian-language criminal forums (LeakBase, RAMP)."
  - "Joint Investigation Team (JIT) cooperation pattern with three core partners (Austria, Estonia, Latvia) plus a supporting jurisdiction (Finland) is a discrete IC mechanism class for 4-jurisdiction CaaS-takedown operations."
source_count: 1
sources:
  - "[[2025-10-17_europol_cybercrime-as-a-service-sim-box-takedown-latvia]]"
summary: "On 2025-10-17 Europol announced a Latvian-led action day in October 2025 dismantling a cybercrime-as-a-service (CaaS) SIM-box network that offered rented telephone numbers from 80+ countries for use in smishing, phishing, fraud, extortion, migrant smuggling, CSAM distribution, daughter-son scams, investment fraud, fake shops, fake bank websites, and fake-police-officer schemes. Joint Investigation Team partners: Austria, Estonia, Latvia + Finland support. Coordinated by Europol + Eurojust with Shadowserver Foundation as private-sector partner. Action-day results: 26 searches, 5 arrests, ~1,200 SIM-box devices seized (40,000 SIM cards), 5 servers seized, 2 websites taken down (gogetsms.com, apisim.com), EUR 431,000 + USD 333,000 frozen, 4 luxury vehicles seized. More than 49 million online accounts allegedly created via the illegal service."
created: 2026-05-09
updated: 2026-05-17
---
## Summary

In October 2025, a Latvian-led action day dismantled a sophisticated **cybercrime-as-a-service (CaaS) SIM-box network** that offered rented telephone numbers from **more than 80 source countries** for use in a wide range of smishing, phishing, fraud, extortion, migrant smuggling, child sexual abuse material distribution, and impersonation schemes. The action was coordinated by [[europol-ec3|Europol]] and [[eurojust|Eurojust]] under a Joint Investigation Team (JIT) framework with **Austria, Estonia, and Latvia** as JIT partners and **Finland** as a supporting jurisdiction. The Shadowserver Foundation served as a private-sector cooperation partner for technical infrastructure dismantling. The operation was announced publicly on **2025-10-17**.

The CaaS network operated two websites — **gogetsms.com and apisim.com** — that were taken over by law enforcement and replaced with seizure splash pages. Action-day results: 26 searches, 5 arrests, approximately 1,200 SIM-box devices seized (operating 40,000 SIM cards), hundreds of thousands of further SIM cards seized, 5 servers, EUR 431,000 in bank accounts and USD 333,000 in cryptocurrency accounts frozen, and 4 luxury vehicles seized. The operation's underlying scale, per Europol: **more than 49 million online accounts** were created via the illegal service.

## Background

### Modus operandi (the crime)

The criminal network operated a **cybercrime-as-a-service (CaaS) SIM-box infrastructure** — approximately **1,200 SIM-box devices** orchestrating **40,000 active SIM cards** at action time, with hundreds of thousands of additional SIM cards held in reserve. SIM boxes are hardware concentrators that allow a remote customer to "rent" outbound calls or SMS originating from a chosen country code — the call/SMS appears to the recipient mobile network as a domestic origination from a local SIM card, defeating both caller-ID-based fraud filters and geolocation-based account-registration controls. The Latvian operators commercialised this capability as two public-facing services — **gogetsms.com** and **apisim.com** — selling time-limited rental of telephone numbers from **80+ countries** via web-based subscription, paid in cryptocurrency. Customers used the rented numbers to bulk-register fake accounts on social media, messaging apps (WhatsApp, Telegram), online marketplaces, and banking platforms, and to send smishing campaigns plus voice-phishing outbound calls. The Europol release quantifies the throughput: **more than 49 million online accounts** were allegedly created via the illegal service over its operational lifetime.

### Victim profile and impact

Crime types facilitated by the network are described verbatim in the Europol release. Specific named schemes targeting downstream victims:

- **Fraud on online second-hand marketplaces** — mass fake-account creation enables buyer/seller impersonation scams (victim base: retail consumers across EU and 80+ source-number countries).
- **"Daughter–son scam"** via WhatsApp — impersonators message parents claiming to be the child in urgent financial distress, demanding immediate four-figure transfers (victim base: parents, predominantly aged 50+, in German-speaking and Eastern European markets).
- **Investment fraud with telephone outreach** — cold-call victims and deploy remote-access software (AnyDesk, TeamViewer) for direct account drainage (victim base: retail investors across EU).
- **Fake shops and fake bank websites** — phishing infrastructure for credential and payment-card theft (victim base: online shoppers, banking customers).
- **Fake-police-officer schemes targeting Russian-speaking victims** — perpetrators impersonate police using forged IDs and personal cash collection at the victim's home, exploiting Russian-speaking diaspora communities across the EU (victim base: predominantly elderly Russian-speaking migrants in Germany, Austria, Baltic states).
- **CSAM distribution and migrant smuggling** — fake accounts used to operate communication channels for these predicate offences.

No aggregate victim count or aggregate financial-loss figure is provided in the cited Europol release. Given the 49M-account creation throughput and the scheme catalogue, the downstream victim pool is *highly likely* (≥80%) in the hundreds of thousands across the EU and the 80+ source-number jurisdictions.

### Financial flow

The cited release does not disclose the per-rental price of SIM-box numbers, but the **action-day asset freezes** quantify the operators' realised criminal proceeds: **EUR 431,000** frozen in suspects' bank accounts, **USD 333,000** frozen in cryptocurrency accounts, plus **4 luxury vehicles** seized — *likely* (55-80%) cash-equivalent in the high-six-figure to low-seven-figure EUR range. Customer payments to the CaaS operators *highly likely* flowed via cryptocurrency (the seized USD 333K crypto position is consistent with this), while downstream-victim funds (from the predicate schemes above) flowed to separate customer-controlled accounts not part of the seizures. The CaaS operator-revenue share is therefore distinct from the downstream-victim-loss pool — the operators monetise per-number-rental fees regardless of customer outcome.

### Criminal organisation structure

The Europol release names **5 action-day arrests** with the title figure of 7 (see Contradictions). One of the main suspects was previously under investigation in **Estonia for arson and extortion** — a public-record cross-domain criminal-actor link suggesting at least one OCG principal had prior offline-criminal exposure before the SIM-box CaaS pivot. The 5-arrest cohort plus 26 searches across Latvia, Austria, Estonia (and supporting Finland) indicates a **distributed-cell structure** — *highly likely* (≥80%) with technical operators concentrated in Latvia (server hosting + SIM-box warehouse) and customer-recruitment / cashout layers distributed across the JIT partner jurisdictions. The cited Europol release does not enumerate role-specific responsibilities, headcount-per-cell, or whether the network had hierarchical leadership vs flat-partner structure. **No indictments enumerated** as of the action-day release.

## Participating Parties

| Role | Parties |
|---|---|
| Coordinating bodies | [[europol-ec3\|Europol / EC3]] (specialists deployed to Riga); [[eurojust\|Eurojust]] |
| JIT partners | Austria, Estonia, Latvia |
| Supporting jurisdiction | [[finland\|Finland]] (incl. [[finland-nbi\|Finnish NBI]]) |
| Austria | Federal Criminal Intelligence Service (Bundeskriminalamt); Criminal Investigation Department Salzburg (Landeskriminalamt Salzburg); Vienna Public Prosecutor's Office (Staatsanwaltschaft Wien) |
| Estonia | Estonian Police (Politsei); Northern District Prosecutor's Office (Põhja ringkonnaprokuratuur) |
| Finland | Finnish Police (Poliisi); National Cyber-enabled Crimes Unit (NCCU Finland); [[finland-nbi\|National Bureau of Investigation (Keskusrikospoliisi)]] |
| Latvia | Latvian State Police (Valsts policija); Rīga Judicial Region Prosecution Office; Rīga Northern Prosecution Office |
| Private-sector partner | Shadowserver Foundation (technical infrastructure dismantling collaboration) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| October 2025 (approx 10) | Action day in Latvia | Europol 2025-10-17 |
| 2025-10-17 | Public announcement; press release published; video updated 12:25 PM CET 2025-10-17 | Europol 2025-10-17 |

## Results and Impact

- **5 arrests** (action day; release title says "7 arrested" — see Contradictions).
- **26 searches** carried out.
- **~1,200 SIM-box devices** seized (operating **40,000 SIM cards**).
- **Hundreds of thousands of further SIM cards** seized.
- **5 servers** seized.
- **2 websites taken over**: gogetsms.com and apisim.com.
- **EUR 431,000** frozen in suspects' bank accounts.
- **USD 333,000** frozen in suspects' cryptocurrency accounts.
- **4 luxury vehicles** seized.
- **49+ million online accounts** allegedly created via the illegal service.

## Cooperation Mechanisms Used

The release explicitly names a **Joint Investigation Team (JIT)** with Austria, Estonia, and Latvia as JIT partners, plus Finland as a supporting jurisdiction. [[europol-ec3|Europol]] and [[eurojust|Eurojust]] provided coordination, financial support for technical equipment, travel and translation costs, weekly meetings between law-enforcement authorities, prosecutors and Eurojust desks, and on-the-spot forensic support during the action day. Europol deployed specialists to Riga. The **Shadowserver Foundation** is named as a private-sector partner that collaborated with Europol on technical infrastructure dismantling.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Europol release as a participating jurisdiction or victim country for this operation. The case is recorded in the wiki for the JIT cooperation pattern, the verbatim CaaS-tier methodology description, and the Russian-speaking-victim fake-police-officer scheme — which has structural parallels to broader Russian-language criminal targeting documented elsewhere in the corpus (Phobos, Conti-successor brand cluster, LeakBase) but does not directly inform Korean voice-phishing or scam-compound IC posture.

## Contradictions & Open Questions

- **Title-vs-body arrest count discrepancy** — the cited Europol release title says "7 arrested" but the verbatim body records "5 individuals arrested" on the action day. The wiki record uses the 5-figure for `results.arrests` and flags the title-vs-body delta as an open question. The 7-figure may include earlier related arrests.
- The cited release does not enumerate the indictment or charging counts in the participating jurisdictions (Austria, Estonia, Latvia).
- The cited release does not enumerate the specific identities of the Russian-speaking victim cohort.
- The relationship between this CaaS network and broader scam-compound infrastructure documented elsewhere in the corpus (e.g., Cambodia/Philippines compounds) is not described.

**L26 Background gap notes** (crime substance missing from cited tier-1 source):
- **Aggregate downstream-victim count and aggregate financial-loss figure** — Europol release quantifies LE asset freezes (EUR 431K + USD 333K + 4 vehicles) but does not aggregate victim losses across the predicate-scheme catalogue.
- **Per-rental price-list of the SIM-box CaaS service** — gogetsms.com / apisim.com per-number-rental fee schedule and operator revenue history not disclosed.
- **OCG hierarchical structure** — role-specific responsibilities, headcount-per-cell, principal-vs-affiliate relationships across the 5-arrest cohort are not enumerated.
- **Per-customer-segment breakdown of the 49M-account throughput** — what share went to daughter-son scams vs investment fraud vs fake-police vs CSAM is not provided.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-10-17_europol_cybercrime-as-a-service-sim-box-takedown-latvia\|Cybercrime-as-a-service takedown: 7 arrested (Latvia SIM-box CaaS network dismantled)]] | Europol | 2025-10-17 | https://www.europol.europa.eu/media-press/newsroom/news/cybercrime-service-takedown-7-arrested |
