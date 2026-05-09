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
updated: 2026-05-09
---
## Summary

In October 2025, a Latvian-led action day dismantled a sophisticated **cybercrime-as-a-service (CaaS) SIM-box network** that offered rented telephone numbers from **more than 80 source countries** for use in a wide range of smishing, phishing, fraud, extortion, migrant smuggling, child sexual abuse material distribution, and impersonation schemes. The action was coordinated by [[europol-ec3|Europol]] and [[eurojust|Eurojust]] under a Joint Investigation Team (JIT) framework with **Austria, Estonia, and Latvia** as JIT partners and **Finland** as a supporting jurisdiction. The Shadowserver Foundation served as a private-sector cooperation partner for technical infrastructure dismantling. The operation was announced publicly on **2025-10-17**.

The CaaS network operated two websites — **gogetsms.com and apisim.com** — that were taken over by law enforcement and replaced with seizure splash pages. Action-day results: 26 searches, 5 arrests, approximately 1,200 SIM-box devices seized (operating 40,000 SIM cards), hundreds of thousands of further SIM cards seized, 5 servers, EUR 431,000 in bank accounts and USD 333,000 in cryptocurrency accounts frozen, and 4 luxury vehicles seized. The operation's underlying scale, per Europol: **more than 49 million online accounts** were created via the illegal service.

## Background

The criminal network's SIM-box service allowed perpetrators worldwide to set up fake accounts on social media and communication platforms while obscuring their true identity and location. Crime types facilitated by the network are described verbatim in the Europol release as including phishing, smishing, fraud, extortion, migrant smuggling, and the distribution of child sexual abuse material. Specific named schemes include:

- Fraud on online second-hand marketplaces (mass fake-account creation).
- "Daughter–son scam" via WhatsApp, demanding urgent four-figure payments.
- Investment fraud with telephone outreach and remote-access software deployment.
- Fake shops and fake bank websites.
- **Fake-police-officer schemes targeting Russian-speaking victims** with forged IDs and personal cash collection.

One of the main suspects was previously under investigation in Estonia for arson and extortion — a public-record cross-domain criminal-actor link.

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

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-10-17_europol_cybercrime-as-a-service-sim-box-takedown-latvia\|Cybercrime-as-a-service takedown: 7 arrested (Latvia SIM-box CaaS network dismantled)]] | Europol | 2025-10-17 | https://www.europol.europa.eu/media-press/newsroom/news/cybercrime-service-takedown-7-arrested |
