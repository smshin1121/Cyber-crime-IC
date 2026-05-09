---
type: operation
title: "LabHost Phishing-as-a-Service Takedown (UK Met-led, 19-country joint action, 2024-04-14 to 2024-04-17)"
title_ko: "LabHost 피싱 서비스 플랫폼 단속 (영국 경시청 주도, 19개국 합동 작전, 2024-04-14~2024-04-17)"
aliases:
  - "LabHost takedown"
  - "LabHost phishing-as-a-service disruption"
  - "Operation LabHost"
case_id: CYB-2024-202
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2024-04-18
  start: 2024-04-14
  end: 2024-04-17
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[malware-ic]]"
target_entity: "LabHost — phishing-as-a-service platform offering subscription access to phishing kits, hosting infrastructure, fake-website templates (170+), and the integrated LabRat campaign-management tool capturing 2FA codes; ~10,000 users worldwide; ≥40,000 LabHost-linked phishing domains; $249/month average subscription"
lead_agency: "[[uk-metropolitan-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[austria]]"
  - "[[belgium]]"
  - "[[canada]]"
  - "[[czechia]]"
  - "[[estonia]]"
  - "[[finland]]"
  - "[[ireland]]"
  - "[[lithuania]]"
  - "[[malta]]"
  - "[[netherlands]]"
  - "[[new-zealand]]"
  - "[[poland]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[uk-metropolitan-police]]"
  - "[[fbi]]"
  - "[[us-secret-service]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[ireland-garda]]"
organizations:
  - "[[europol-ec3]]"
  - "[[uk-metropolitan-police]]"
  - "[[fbi]]"
  - "[[us-secret-service]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[ireland-garda]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Per-country domestic search-and-arrest warrants executed under the lead authority's domestic procedural code"
  - "Europol J-CAT (Joint Cybercrime Action Taskforce, hosted at Europol HQ) as the supporting multilateral coordination instrument"
  - "Europol EC3 operational sprint at HQ with all 19 participating countries; Europol specialist on-site deployment to Dutch National Police during the action phase"
results:
  arrests: 37
  indictments: 0
  servers_seized: 0
  domains_seized: 40000
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "37 arrests during 2024-04-14 → 2024-04-17 action days"
    - "70 addresses searched across the world"
    - "4 arrests in the United Kingdom linked to the running of the site, including LabHost's original developer"
    - "LabHost platform shut down (previously available on the open web)"
    - "≥40,000 phishing domains linked to LabHost; ~10,000 users worldwide"
    - "LabRat campaign-management tool with 2FA-code capture capability disrupted"
edges:
  - source_actor: uk-metropolitan-police
    target_actor: europol-ec3
    cooperation_type: coordination
    legal_basis: europol-j-cat
    direction: undirected
  - source_actor: europol-ec3
    target_actor: netherlands
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
  - source_actor: fbi
    target_actor: uk-metropolitan-police
    cooperation_type: info_sharing
    legal_basis: bilateral
    direction: undirected
  - source_actor: us-secret-service
    target_actor: uk-metropolitan-police
    cooperation_type: info_sharing
    legal_basis: bilateral
    direction: undirected
  - source_actor: australia-afp
    target_actor: europol-ec3
    cooperation_type: info_sharing
    legal_basis: europol-j-cat
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific identities of the 4 UK arrestees / LabHost developer (charging documents not enumerated in this release)"
  - "specific victim totals per country"
  - "victims recovered or notified count"
  - "post-arrest charging timelines and indictment counts"
related_cases:

related_operations:
  - "[[operation-cronos-phase1]]"
  - "[[operation-endgame]]"
  - "[[latvia-sim-box-cybercrime-as-a-service-takedown-2025]]"
  - "[[2bagoldmule-qqaazz]]"
  - "[[project-compass-the-com-network-2025]]"
  - "[[xss-is-cybercrime-forum-takedown-2025]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
challenges_encountered:

lessons_learned:
  - "Demonstrates the most fully-articulated 19-country action-day enumeration in the wiki for a phishing-as-a-service takedown, covering EU member states, EFTA partners, Five Eyes (US, UK, Canada, Australia, NZ), and the Pacific."
  - "Establishes the Europol J-CAT (Joint Cybercrime Action Taskforce, hosted at Europol HQ) as a discrete IC mechanism class for organising multilateral cybercrime takedowns — supplementing the bilateral MLAT and EU JIT models tracked elsewhere in the wiki."
  - "Demonstrates the PhaaS commoditisation pattern with explicit pricing ($249/month), feature menu (170+ fake-website templates), and integrated 2FA-capture tooling (LabRat) — a benchmark for evaluating later phishing-platform takedowns."
  - "Action-phase Europol specialist on-site deployment to the Dutch National Police is a discrete supporting mechanism class — Europol cryptocurrency-expert deployment to Portugal in the [[eurojust-100m-crypto-investment-fraud-takedown-2025|2025 Eurojust €100M crypto fraud takedown]] is a structurally similar pattern for crypto-asset rather than phishing infrastructure."
source_count: 1
sources:
  - "[[2024-04-18_europol_international-investigation-disrupts-phishing-service-platform-labhost]]"
summary: "Between 14 and 17 April 2024, a UK London Metropolitan Police-led international investigation supported by Europol EC3 and the Joint Cybercrime Action Taskforce (J-CAT) executed 70 searches across 19 countries (Australia, Austria, Belgium, Canada, Czechia, Estonia, Finland, Ireland, Lithuania, Malta, Netherlands, New Zealand, Poland, Portugal, Romania, Spain, Sweden, United Kingdom, United States) producing 37 arrests including 4 in the UK linked to the running of the site (the LabHost original developer among them). The LabHost phishing-as-a-service platform — $249/month subscription, ≥40,000 LabHost-linked phishing domains, ~10,000 users worldwide, 170+ fake-website templates, and the integrated LabRat campaign-management tool capturing 2FA codes — was shut down. Investigation supported since September 2023 with an operational sprint at Europol HQ; Europol specialist on-site deployment to the Dutch National Police during the action phase."
created: 2026-05-09
updated: 2026-05-09
---
## Summary

Between **14 and 17 April 2024**, a **UK London Metropolitan Police-led** international investigation, supported by **Europol's European Cybercrime Centre (EC3)** and the **Joint Cybercrime Action Taskforce (J-CAT)** hosted at Europol HQ, executed **70 searches** across **19 countries** producing **37 arrests** — including **4 individuals in the United Kingdom** linked to the running of the site, **including LabHost's original developer**. The **LabHost phishing-as-a-service (PhaaS) platform** was shut down. LabHost provided cybercriminals with a subscription-based ($249/month average) menu of phishing kits, infrastructure for hosting fake pages, **170+ fake-website templates**, and the **LabRat** integrated campaign-management tool capable of capturing **two-factor authentication (2FA) codes**. The investigation uncovered **at least 40,000 phishing domains** linked to LabHost and **~10,000 users worldwide**.

## Background

Cybercrime-as-a-service has become a rapidly growing business model in the criminal landscape whereby threat actors rent or sell tools, expertise, or services to other cybercriminals to commit their attacks. While this model is well established with ransomware groups (e.g. [[operation-cronos-phase1|Operation Cronos / LockBit]]), it has also been adopted in other aspects of cybercrime, such as phishing. LabHost commoditised phishing by offering a customisable, click-deployable kit, with subscription tiers granting access to escalating target sets including financial institutions, postal delivery services, and telecommunication providers.

What made LabHost particularly destructive was its integrated campaign management tool **LabRat**, which allowed cybercriminals to monitor and control their attacks in real time. LabRat was specifically designed to capture **two-factor authentication codes and credentials**, allowing the criminals to bypass enhanced security measures.

## Participating Parties

| Country | Lead Authority |
|---|---|
| Australia | Australian Federal Police-led Joint Policing Cybercrime Coordination Centre (AFP / JPC3) |
| Austria | Criminal Intelligence Service (Bundeskriminalamt) |
| Belgium | Federal Judicial Police Brussels |
| Canada | Royal Canadian Mounted Police (RCMP) |
| Czechia | Bureau of Criminal Police and Investigation Service |
| Estonia | Estonian Police and Border Guard Board |
| Finland | National Police (Poliisi) |
| Ireland | An Garda Síochána |
| Lithuania | Lithuania Police |
| Malta | Malta Police Force |
| Netherlands | Central Netherlands Police (Politie Midden-Nederland) |
| New Zealand | New Zealand Police |
| Poland | Central Office for Combating Cybercrime (Centralne Biuro Zwalczania Cyberprzestępczości) |
| Portugal | Judicial Police (Polícia Judiciária) |
| Romania | Romanian Police (Poliția Română) |
| Spain | Policía Nacional |
| Sweden | Swedish Police Authority (Polisen) |
| United Kingdom | London Metropolitan Police (lead) |
| United States | US Secret Service (USSS) + Federal Bureau of Investigation (FBI) |
| Coordinating | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] + Joint Cybercrime Action Taskforce (J-CAT) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| September 2023 | Europol begins supporting the case | Europol 2024-04-18 |
| (date not enumerated) | Operational sprint at Europol HQ with all 19 participating countries to identify users and victims in their jurisdictions | Europol 2024-04-18 |
| 2024-04-14 to 2024-04-17 | Action days: 70 searches globally; 37 arrests; 4 UK arrests including LabHost developer; Europol specialist deployed on-site to Dutch National Police | Europol 2024-04-18 |
| 2024-04-18 | Public announcement; LabHost platform shut down | Europol 2024-04-18 |

## Results and Impact

- **37 arrests** during 2024-04-14 → 2024-04-17 action days.
- **70 addresses searched** across the world.
- **4 UK arrests** linked to the running of the site, **including LabHost's original developer**.
- **LabHost platform shut down** (previously available on the open web).
- **≥40,000 phishing domains** linked to LabHost.
- **~10,000 LabHost users worldwide.**
- **LabRat 2FA-capture tool** disrupted.

## Cooperation Mechanisms Used

The cited release describes three discrete IC mechanism classes for this operation:

1. **Europol Joint Cybercrime Action Taskforce (J-CAT)** — multilateral coordination instrument hosted at Europol HQ, providing the institutional venue for 19-country joint action-day planning and execution.
2. **Europol EC3 operational sprint** at HQ with all participating countries — pre-action-day intelligence-development mechanism for identifying LabHost users and victims in each participating jurisdiction.
3. **Action-phase Europol specialist on-site deployment** to the Dutch National Police — a structurally similar mechanism to the Europol cryptocurrency-expert deployment to Portugal in the [[eurojust-100m-crypto-investment-fraud-takedown-2025|2025 Eurojust €100M crypto investment fraud takedown]], applied here to phishing-platform infrastructure rather than crypto-asset infrastructure.

## Korean Involvement (한국의 참여)

South Korea is not named among the 19 participating jurisdictions in the cited Europol release. The case is recorded in the wiki for the PhaaS commoditisation pattern and the 19-country J-CAT action-day model. Korean exposure to LabHost-linked phishing campaigns is *likely* present given the global ~10,000-user / ~40,000-domain scale but is not enumerated in this source.

## Contradictions & Open Questions

- The cited release does not name the LabHost original developer or the other 3 UK arrestees by identity.
- Specific victim totals per country (including the AFP-stated "94,000+ Australians") are not enumerated in the cited Europol release; that figure comes from secondary AFP commentary rather than this primary source.
- Specific bank-card / PIN / password totals (480,000 / 64,000 / 1M+ per CNN secondary reporting) are not enumerated in the cited Europol release.
- Post-arrest charging timelines, indictment counts, and sentencing schedules are not enumerated.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2024-04-18_europol_international-investigation-disrupts-phishing-service-platform-labhost\|International investigation disrupts phishing-as-a-service platform LabHost]] | Europol | 2024-04-18 | https://www.europol.europa.eu/media-press/newsroom/news/international-investigation-disrupts-phishing-service-platform-labhost |
