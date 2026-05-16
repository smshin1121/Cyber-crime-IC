---
type: operation
title: "Ragnar Locker ransomware gang takedown — 11-country international police swoop (October 2023)"
title_ko: "Ragnar Locker 랜섬웨어 조직 단속 — 11개국 국제공조 작전 (2023년 10월)"
aliases:
  - "Ragnar Locker takedown 2023"
  - "Operation Ragnar Locker"
  - "Ragnar Locker eleven-country action week"
case_id: CYB-2023-820
period: 1
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - takedown
  - infrastructure-seizure
  - online-content-takedown
outcome: success
timeframe:
  announced: 2023-10-20
  start: 2023-10-16
  end: 2023-10-20
  ongoing: false
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[extortion-ic]]"
target_entity: "Ragnar Locker ransomware group — active since December 2019; double-extortion criminal operation that targeted critical infrastructure worldwide, including the Portuguese national carrier (TAP Air Portugal) and an Israeli hospital. Operated Windows-targeting ransomware exploiting exposed services such as RDP, with a Tor-hosted 'Wall of Shame' data leak site."
lead_agency: "[[france-gendarmerie]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[czechia]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[latvia]]"
  - "[[netherlands]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[ukraine]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[france-gendarmerie]]"
  - "[[czechia-police]]"
  - "[[germany-bka]]"
  - "[[italy-polizia-postale]]"
  - "[[japan-npa]]"
  - "[[latvia-state-police]]"
  - "[[netherlands-politie]]"
  - "[[spain-guardia-civil]]"
  - "[[sweden-police]]"
  - "[[ukraine-police]]"
  - "[[fbi]]"
  - "[[interpol]]"
mechanisms_used:
  - "[[europol-jit]]"
  - "[[joint-investigation-team]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[empact]]"
  - "[[j-cat]]"
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
legal_basis:
  - "EMPACT — European Multidisciplinary Platform Against Criminal Threats (cyber-attacks priority)"
  - "Eurojust case opened at the request of French authorities (May 2021), five coordination meetings hosted, action-week coordination centre"
  - "Europol EC3 operational coordination + J-CAT (Joint Cybercrime Action Taskforce) liaison support"
  - "Domestic computer-misuse, ransomware/extortion, and search-seizure powers in eleven cooperating jurisdictions"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Key target (suspected developer) arrested 2023-10-16 in Paris, France, and brought before examining magistrates of the Paris Judicial Court"
    - "Five additional suspects interviewed in Spain and Latvia during 2023-10-16 to 2023-10-20 action week"
    - "House search executed in Czechia at the key target's residence"
    - "Ransomware infrastructure seized in the Netherlands, Germany, and Sweden"
    - "Tor-hosted 'Wall of Shame' data leak website taken down in Sweden"
    - "Builds on October 2021 first-wave arrests of two prominent Ragnar Locker operators in Ukraine"
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "exact number of servers seized (Europol stated 'infrastructure ... seized in the Netherlands, Germany and Sweden' without numeric count)"
  - "value of cryptocurrency seized (not disclosed)"
  - "total number of victims (Europol notes 'numerous high-profile attacks against critical infrastructure' but no global victim count)"
related_cases: []
related_operations:
  - "[[operation-endgame]]"
source_count: 1
sources:
  - "[[2023-10-20_europol_ragnar-locker-ransomware-gang-taken-down-international-police-swoop]]"
created: 2026-05-16
updated: 2026-05-16
---

# Ragnar Locker ransomware gang takedown — 11-country international police swoop (October 2023)

## Summary

Between **16 and 20 October 2023**, law enforcement and judicial authorities from **eleven countries** — Czechia, France, Germany, Italy, Japan, Latvia, the Netherlands, Spain, Sweden, Ukraine, and the United States — executed a coordinated action week against the [Ragnar Locker](https://en.wikipedia.org/wiki/Ragnar_Locker) ransomware group, coordinated at the international level by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and [[eurojust|Eurojust]] and led operationally by the [[france-gendarmerie|French National Gendarmerie's Cybercrime Centre (C3N)]].

The action's "key target," a suspected developer of the Ragnar group, was arrested in Paris on 16 October 2023 and brought before examining magistrates of the Paris Judicial Court; his home in Czechia was searched. Five additional suspects were interviewed in Spain and Latvia. The group's ransomware infrastructure was seized in the Netherlands, Germany, and Sweden, and its Tor "Wall of Shame" data leak website was taken down in Sweden.

> [!info] Confidence: Highly likely (>80%)
> The full participant roster (eleven countries with named LE units) is published verbatim in the Europol newsroom JSON-LD payload (datePublished 2023-10-20T15:35:26+00:00, EMPACT-flagged, structured `countries` field listing ISO codes CZ-FR-DE-IT-JP-LV-NL-ES-SE-UA-US). One numeric gap remains: Europol describes "infrastructure seized in the Netherlands, Germany and Sweden" without a server count, and does not disclose a victim total or any cryptocurrency-seizure figure.

## Background

Ragnar Locker, active since December 2019, was a double-extortion ransomware strain that exploited exposed services such as Remote Desktop Protocol (RDP) on Windows systems, encrypted victim networks, and threatened publication of stolen data on its Tor-hosted "Wall of Shame" leak site. Recent victims at the time of the takedown included the Portuguese national carrier (publicly reported as TAP Air Portugal) and an Israeli hospital. The group explicitly warned victims against contacting law enforcement, stating that contact would trigger publication of stolen data.

This action was the second wave of a multi-year investigation. A first wave in October 2021 saw two prominent Ragnar Locker operators arrested in Ukraine in an operation conducted jointly by the French Gendarmerie, the [[fbi|US FBI]], [[europol-ec3|Europol]], [[interpol|INTERPOL]], and the [[ukraine-police|Ukrainian National Police]].

## Participating Parties

Europol's published participant list (verbatim):

| Country | Authority |
|---|---|
| Czechia | National Counter-Terrorism, Extremism and Cybercrime Agency of Police of the Czech Republic ([[czechia-police|NCOZ — Czech Police]]) |
| France | National Cybercrime Centre of the French Gendarmerie (Gendarmerie Nationale – C3N) ([[france-gendarmerie]]) |
| Germany | State Criminal Police Office Sachsen (Landeskriminalamt Sachsen); Federal Criminal Police Office ([[germany-bka|Bundeskriminalamt]]) |
| Italy | State Police (Polizia di Stato); Postal and Communication Police ([[italy-polizia-postale|Polizia Postale e delle Comunicazioni]]) |
| Japan | National Police Agency ([[japan-npa|NPA]]) |
| Latvia | State Police ([[latvia-state-police|Latvijas Valsts Policija]]) |
| Netherlands | Police of East Netherlands (Politie Oost-Nederland) ([[netherlands-politie]]) |
| Spain | Civil Guard ([[spain-guardia-civil|Guardia Civil]]) |
| Sweden | Swedish Cybercrime Centre ([[sweden-police|SC3]]) |
| Ukraine | Cyberpolice Department of the National Police of Ukraine (Національна поліція України) ([[ukraine-police]]) |
| United States | Atlanta Field Office of the [[fbi|Federal Bureau of Investigation]] |
| Coordination | [[europol-ec3|Europol European Cybercrime Centre (EC3)]] + [[eurojust|Eurojust]] |

## Legal Framework

- **EMPACT (European Multidisciplinary Platform Against Criminal Threats)** — the investigation was carried out under the EMPACT cyber-attacks priority for the 2022-2025 policy cycle.
- **Eurojust case file** — opened in May 2021 at the request of the French authorities; the Agency hosted five coordination meetings before the action week to facilitate judicial cooperation and set up a coordination centre during 16-20 October 2023 to enable rapid judicial-authority cooperation.
- **Europol EC3 operational coordination** — organised 15 coordination meetings and two week-long sprints to prepare the action; provided analytical, malware, forensic, and crypto-tracing support; ran a virtual command post during the action week.
- **J-CAT (Joint Cybercrime Action Taskforce)** — cybercrime liaison officers posted to Europol's headquarters facilitated close cooperation between the involved LE authorities.
- **Domestic powers** — each of the eleven jurisdictions executed arrest, search, seizure, and judicial-presentation authorities under its own ransomware/computer-misuse and extortion statutes.

## Operational Timeline

| Date | Event |
|---|---|
| December 2019 | Ragnar Locker ransomware strain first observed; double-extortion operation begins. |
| May 2021 | Eurojust opens case at request of French authorities. |
| October 2021 | First-wave Ukrainian arrests of two prominent Ragnar Locker operators (French Gendarmerie + US FBI + Europol + INTERPOL + Ukrainian National Police). |
| 2021-2023 | Multi-year intelligence development; Europol EC3 organises 15 coordination meetings + two week-long sprints. |
| 2023-10-16 | Key target (suspected developer) arrested in Paris by French Gendarmerie. Home search executed in Czechia. |
| 2023-10-16 to 2023-10-20 | Searches in Czechia, Spain, Latvia; five additional suspects interviewed in Spain and Latvia; infrastructure seized in the Netherlands, Germany, Sweden; Tor data leak site taken down in Sweden. |
| 2023-10-20 | Key perpetrator brought before examining magistrates of the Paris Judicial Court. Europol announces the international action. |

## Results and Impact

- **1 key target arrested** (Paris, 16 October 2023; suspected developer of the Ragnar Locker ransomware) — brought before examining magistrates of the Paris Judicial Court at the end of the action week.
- **5 additional suspects interviewed** in Spain and Latvia.
- **House search executed in Czechia** at the key target's residence.
- **Infrastructure seizures** in the Netherlands, Germany, and Sweden (Europol does not specify server count).
- **Tor "Wall of Shame" data leak site taken down** in Sweden — eliminating the group's primary public extortion-leverage channel.
- **Builds on October 2021** first-wave arrests of two prominent operators in Ukraine, demonstrating sustained multi-year follow-through.

## Cooperation Mechanisms Used

- [[europol-jit]] — Europol-coordinated joint investigative effort (formal Joint Investigation Team structure under Eurojust auspices for the French-led core)
- [[eurojust-coordination-meeting]] — five pre-action coordination meetings + action-week coordination centre
- [[empact]] — European Multidisciplinary Platform Against Criminal Threats (cyber-attacks priority)
- [[j-cat]] — Joint Cybercrime Action Taskforce liaison officers at Europol HQ
- [[search-seizure]] — coordinated searches across Czechia, Spain, Latvia
- [[domain-seizure]] — Tor data leak site (Sweden)
- Europol virtual command post + 24/7 analytical, malware, forensic, and crypto-tracing support

## Challenges and Friction Points

- **Multi-jurisdictional Tor infrastructure** — the data leak site was hosted infrastructure that required coordinated takedown action (Sweden) while servers were geographically distributed across the Netherlands, Germany, and Sweden.
- **Two-year case duration** — Eurojust opened the case in May 2021 but the action week did not occur until October 2023, reflecting the complexity of coordinating eleven jurisdictions across two cycles of EMPACT operational planning.
- **Critical-infrastructure victim diplomacy** — public attribution to victims (TAP Air Portugal, an Israeli hospital) implicated host-state legal interests beyond the eleven action-week participants.
- **Double-extortion deterrent messaging** — Ragnar Locker's explicit threats against victims who contacted LE compounded the difficulty of victim cooperation and intelligence-gathering before the action.

## Lessons Learned

- **Multi-year, multi-wave model** — the 2021 Ukrainian arrests + 2023 European action week show that sustained EC3/Eurojust coordination across cycles can deliver follow-through against resilient ransomware groups.
- **Coordinator-led participation breadth** — including Japan's [[japan-npa|NPA]] and the [[fbi|US FBI]] alongside nine European LE/judicial agencies demonstrates the reach of EC3-coordinated actions beyond EU borders.
- **EMPACT framework value** — formal EMPACT designation supplied a stable multi-year planning vehicle for the cyber-attacks priority that survived turnover in national operational priorities.

## Follow-Up Actions

- Subsequent prosecution of the key target in France through the examining-magistrate procedure of the Paris Judicial Court.
- Continued Europol EC3 tracking of remaining Ragnar Locker affiliates and any reconstitution attempts.
- Public-private partnership outreach with cyber-threat-intelligence firms via the J-CAT framework.

## Korean Involvement (한국의 참여)

No direct Korean LE participation is documented in the Europol press release. [[japan-npa|Japan's National Police Agency (NPA)]] is the only Asian LE participant named. Korea-relevant takeaways:

- The eleven-country roster (CZ-FR-DE-IT-JP-LV-NL-ES-SE-UA-US) demonstrates the EC3/Eurojust action-week model that Korean LE could engage with via the [[mlat-process|MLAT]] or via [[interpol|INTERPOL]] notice channels if a future ransomware investigation has a Europe-touching nexus.
- Korea's accession status to the Budapest Convention (invited 2023, not yet a party as of 2026-05-16) limits direct judicial-cooperation channels with Europol-coordinated cases of this nature; observers in [[knpa-cyber-bureau|KNPA Cyber Bureau]] / Korean Prosecution Service can study the EMPACT-flagged playbook for future inbound or outbound ransomware investigations.

## Contradictions & Open Questions

- **Exact server count seized** — Europol's wording "infrastructure ... seized in the Netherlands, Germany and Sweden" lacks numeric detail; subsequent unsealing or trial documents may clarify.
- **Cryptocurrency seizure value** — not disclosed in the press release; Europol notes crypto-tracing support but does not quantify recovered or frozen assets.
- **Full count of indictments downstream** — only one arrest is named for the action week itself; how many of the five interviewed suspects in Spain and Latvia were subsequently charged is not detailed in the source.
- **TAP Air Portugal / Israeli hospital attribution** — Europol references "the Portuguese national carrier" and "a hospital in Israel" without naming them; cross-source corroboration (Portuguese press, Israeli MoH advisories) would close the attribution loop.
