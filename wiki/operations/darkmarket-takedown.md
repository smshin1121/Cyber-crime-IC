---
type: operation
title: "DarkMarket Marketplace Takedown"
aliases:
  - "DarkMarket Seizure"
  - "DarkMarket Shutdown"
case_id: CYB-2021-001
period: 2
operation_type: infrastructure-seizure
operation_role: umbrella
parent_operation: ""
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2021-01-12
  start: 2020-01-01
  end: 2021-01-11
  ongoing: false
crime_type: "[[online-fraud-ic|Online Fraud]]"
target_entity: "DarkMarket darknet marketplace"
lead_agency: "[[germany-bka|German BKA]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[germany|Germany]]"
  - "[[australia|Australia]]"
  - "[[united-kingdom|United Kingdom]]"
  - "[[united-states|United States]]"
  - "[[ukraine|Ukraine]]"
  - "[[moldova|Moldova]]"
  - "[[denmark|Denmark]]"
participating_agencies:
  - "[[germany-bka|German BKA]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[australia-afp|Australian Federal Police]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[uk-nca|UK National Crime Agency]]"
  - "[[denmark-police|Danish Police]]"
  - "[[ukraine-police|Ukrainian Police]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention]]"
  - "German Criminal Code (StGB)"
mechanisms_used:
  - "[[mutual-legal-assistance|Mutual Legal Assistance]]"
  - "[[informal-cooperation|Informal Police-to-Police Cooperation]]"
  - "[[joint-investigation-team|Joint Investigation Team]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 20
  domains_seized: 1
  cryptocurrency_seized: "4,650 BTC + 12,800 XMR (~EUR 140 million)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "500,000 users identified"
    - "2,400+ vendors catalogued"
    - "320,000+ transactions recorded"
edges:
  - source_actor: "Germany BKA"
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "Germany BKA"
    target_actor: "Australia AFP"
    cooperation_type: info_sharing
    legal_basis: MLAT
    direction: directed
  - source_actor: "Germany BKA"
    target_actor: "Moldova Police"
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
  - source_actor: "Germany BKA"
    target_actor: "Ukraine Police"
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields: []
related_cases:
  - "[[australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace]]"
related_operations:
  - "[[operation-dark-huntor|Operation Dark HunTOR]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional Conflicts]]"
  - "[[data-sovereignty|Data Sovereignty]]"
lessons_learned:
  - "Seized infrastructure intelligence enables follow-on operations"
  - "Cross-border server seizure requires pre-arranged MLA channels"
  - "Cryptocurrency tracing proved essential for transaction mapping"
source_count: 5
sources:
  - "[[2021-01-12_europol-europa-eu_darkmarket-world-s-largest-illegal-dark-web-marketplace-taken-down]]"
  - "[[2021-01-12_thehackernews-com_authorities-take-down-world-s-largest-illegal-dark-web-marketplace]]"
  - "[[2021-01-12_rferl-org_servers-seized-in-ukraine-moldova-as-germany-takes-down-world-s-largest-illegal]]"
  - "[[2021-01-12_sbs-com-au_australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-ma]]"
  - "[[2021-10-26_dea-gov_department-of-justice-announces-results-of-operation-dark-huntor]]"
created: 2026-04-10
updated: 2026-04-18
summary: "DarkMarket was, at the time of its shutdown on 11 January 2021, the world's largest illegal darknet marketplace by user count. The takedown was led by the cybercrime unit of the Koblenz Public Prosecutor's Office and Germany's Federal Criminal Police Office (BKA), with coordination through Europol EC3. The intelligence gathered from the seized infrastructure later enabled Operation Dark HunTOR."
jurisdictions:
  - "[[germany|Germany]]"
  - "[[australia|Australia]]"
  - "[[united-kingdom|United Kingdom]]"
  - "[[united-states|United States]]"
  - "[[ukraine|Ukraine]]"
  - "[[moldova|Moldova]]"
  - "[[denmark|Denmark]]"
organizations:
  - "[[germany-bka|German BKA]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[australia-afp|Australian Federal Police]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[uk-nca|UK National Crime Agency]]"
  - "[[denmark-police|Danish Police]]"
  - "[[ukraine-police|Ukrainian Police]]"
crime_types:
  - "[[online-fraud-ic|Online Fraud]]"
---
## Summary

DarkMarket was, at the time of its shutdown on 11 January 2021, the world's largest illegal darknet marketplace by user count. The takedown was led by the cybercrime unit of the Koblenz Public Prosecutor's Office and Germany's Federal Criminal Police Office (BKA), with coordination through Europol EC3. The intelligence gathered from the seized infrastructure later enabled [[operation-dark-huntor|Operation Dark HunTOR]].

## Background

DarkMarket facilitated the sale of drugs, counterfeit money, stolen and forged card data, anonymous SIM cards and malware. The public-source set makes clear that the operation combined a physical arrest in Germany with server seizures in Moldova and Ukraine, producing backend data that later became intelligence for follow-on enforcement.

## Results and Impact

- 1 publicly reported operator arrest
- more than 20 servers seized in Moldova and Ukraine
- approximately 500,000 users and 2,400 vendors exposed in public reporting
- intelligence pipeline that directly fed [[operation-dark-huntor]]

## Cooperation And Legal Analysis

DarkMarket is valuable as a model of seizure-then-exploitation. The January 2021 action did not just remove a marketplace. It created a long-lived evidence pool that was later used for arrests in Dark HunTOR. That makes the page more than a marketplace shutdown record; it is an anchor for the repo's wider darknet-enforcement narrative.

The page also preserves a useful legal distinction: the current source set strongly supports the takedown, the arrest and the server seizure, but not a fully documented later prosecution path for the unnamed Australian suspect.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| 1 | DarkMarket: world's largest illegal dark web marketplace taken down | Europol | 2021-01-12 | https://www.europol.europa.eu/media-press/newsroom/news/darkmarket-world-s-largest-illegal-dark-web-marketplace-taken-down |
| 2 | Authorities Take Down World's Largest Illegal Dark Web Marketplace | The Hacker News | 2021-01-12 | https://thehackernews.com/2021/01/authorities-take-down-worlds-largest.html |
| 3 | Servers Seized In Ukraine, Moldova As Germany Takes Down 'World's Largest' Illegal Darknet Marketplace | RFE/RL | 2021-01-12 | https://www.rferl.org/a/ukraine-moldova-servers-seized-germany-busts-darknet-operation/31044327.html |
| 4 | Australian man arrested in Germany accused of running 'world's largest' Darknet marketplace | SBS News | 2021-01-12 | https://www.sbs.com.au/news/article/australian-man-arrested-in-germany-accused-of-running-worlds-largest-darknet-marketplace/pee58pzoh |
| 5 | Department of Justice announces results of Operation Dark HunTOR | DEA / DOJ | 2021-10-26 | https://www.dea.gov/ |
