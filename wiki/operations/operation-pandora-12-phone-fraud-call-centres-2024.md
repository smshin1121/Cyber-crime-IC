---
type: operation
title: "Operation PANDORA — 12 Phone-Fraud Call Centres Takedown (Germany / Albania / Bosnia and Herzegovina / Kosovo / Lebanon, 2023–2024)"
title_ko: "오퍼레이션 PANDORA — 12개 전화사기 콜센터 단속 (독일·알바니아·보스니아·코소보·레바논, 2023–2024)"
aliases:
  - "Operation PANDORA"
  - "PANDORA call centre takedown 2024"
  - "Europol Operation Pandora phone fraud"
  - "Operation PANDORA Freiburg"
case_id: CYB-2024-PND
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2024-05-02
  start: 2023-12
  end: 2024-04-18
  ongoing: false
crime_types:
  - "[[online-fraud-ic]]"
crime_type: "[[online-fraud-ic]]"
target_entity: "Multi-country criminal network operating 12 call centres in Albania, Bosnia and Herzegovina, Kosovo and Lebanon, conducting telephone fraud against German residents (and other European victims, including in Slovenia) using shock-call, fake-police-officer, fake-bank-employee, investment-fraud, debt-collection-fraud, prepaid-card-fraud and romance-scam scripts. Each country specialised in a distinct fraud type — Bosnia-Herzegovina: debt-collection fraud; Kosovo: online banking fraud; Albania: investment fraud; Lebanon: prepaid-card fraud."
lead_agency: "[[germany-bka]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[germany]]"
  - "[[albania]]"
  - "[[bosnia-and-herzegovina]]"
  - "[[kosovo]]"
  - "[[lebanon]]"
  - "[[slovenia]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
legal_basis: []
mechanisms_used:
  - "[[asset-freezing]]"
results:
  arrests: 21
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "12 call centres raided and shut down in Albania, Bosnia and Herzegovina, Kosovo and Lebanon (action day 2024-04-18)"
    - "39 suspects identified by Operation PANDORA in total"
    - "21 persons taken into custody on the action day"
    - "Over 1.3 million scam calls intercepted and recorded by German investigators from December 2023 to April 2024"
    - "Over 7,500 calls passed the threshold to initiate criminal proceedings within four months"
    - "Financial losses prevented in over 80% of indicted crimes; potential damages would have totalled over EUR 10 million"
    - "Cash and assets totalling EUR 1 million seized; data carriers, documents and a large amount of electronic evidence seized"
    - "Slovenian police independently prevented hundreds of thousands of euros in losses to Slovenian victims (since 2023-07, ~40 cases, ~EUR 3.8 million reported damage to Slovenian legal persons, with stolen funds routed to bank accounts in Germany)"
edges:
  - source_actor: germany-bka
    target_actor: europol-ec3
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: germany-bka
    target_actor: albania
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: directed
  - source_actor: germany-bka
    target_actor: bosnia-and-herzegovina
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: directed
  - source_actor: germany-bka
    target_actor: kosovo
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: directed
  - source_actor: germany-bka
    target_actor: lebanon
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: directed
  - source_actor: slovenia
    target_actor: germany-bka
    cooperation_type: info_sharing
    legal_basis: unknown
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "explicit Joint Investigation Team (JIT) registration vs informal Eurojust/Europol coordination"
  - "indictments enumerated separately from arrests"
  - "specific cooperation instruments (Budapest Convention articles, MLAT references) not named in the primary releases"
related_cases: []
related_operations:
  - "[[albania-austria-call-centre-investment-fraud-2026]]"
challenges_encountered: []
lessons_learned:
  - "Europol can host an entire 'operational coordination centre' at HQ on action day, with mobile Europol offices deployed abroad — a force-multiplying model for short-window simultaneous raids across non-EU jurisdictions (Albania, Bosnia-Herzegovina, Kosovo, Lebanon)."
  - "A single suspicious EUR-100,000 cash withdrawal at a Freiburg bank counter in December 2023 escalated into a five-country call-centre takedown by April 2024, illustrating how front-line bank-staff training and timely police escalation can seed a major IC investigation."
  - "Country-by-country specialisation of fraud types within a single criminal network (BiH=debt-collection, Kosovo=online banking, Albania=investment, Lebanon=prepaid cards) is now documented verbatim by a Tier-1 EU primary source, providing a benchmark fact pattern for Western Balkans + Lebanon call-centre typologies."
  - "German investigators set up a counter-call-centre at the Baden-Württemberg State Criminal Police Office, monitoring up to 30 conversations simultaneously and recording 1.3 million calls — a real-time interception model that prevented losses in 80% of indicted crimes."
  - "The victim-state perspective (Slovenia) reveals a separate but adjacent layer: Slovenian victim funds flowed into German bank accounts, structurally tying the call-centre takedown to a downstream money-mule pipeline that the action-day raids alone did not dismantle."
source_count: 2
sources:
  - "[[2024-05-03_policija-si_operation-pandora-12-phone-fraud-call-centres-slovenia]]"
  - "[[2024-05-02_europol_operation-pandora-shuts-down-12-phone-fraud-call-centres]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional page
> This page is published below the preferred normal-page source threshold (`source_count >= 5`) and is marked provisional. It is anchored on a single Tier-1 primary source — the Slovenian Police press release dated 2024-05-03 — which itself cross-references and links to the Europol primary release of 2024-05-02. The Europol release was independently fetched and parsed for this ingest (via curl_cffi + SPA inline-JSON extraction) but is not separately filed as a `wiki/sources/` summary in this iteration. Page will be promoted to a fully sourced standalone page if and when additional Tier-1 corroboration (Eurojust press release, German prosecutor releases, Albanian/Bosnian/Kosovar/Lebanese police releases) is ingested.

## Summary

**Operation PANDORA** was a Europol-supported, **German-led** multi-country takedown of a transnational telephone-fraud network operating **12 call centres** across Albania, Bosnia and Herzegovina, Kosovo and Lebanon. The operation culminated in a coordinated action day on **18 April 2024**, when raids on the 12 call centres resulted in **21 persons taken into custody** out of **39 identified suspects**. The investigation traces back to a single suspicious EUR-100,000 cash-withdrawal request at a bank counter in Freiburg, Germany, in December 2023; from there it expanded into a four-month interception campaign by the Baden-Württemberg State Criminal Police Office that secured the content of over **1.3 million scam calls** and **prevented losses in over 80% of indicted crimes**, with potential damages totalling over **EUR 10 million**. The criminal network specialised by country: Bosnia-Herzegovina ran debt-collection fraud, Kosovo handled online banking fraud, Albania ran investment fraud, and Lebanon specialised in prepaid-card fraud. Cash and assets totalling **EUR 1 million** were seized.

A separate but adjacent **Slovenian victim arc** is independently reported by [[slovenia|Slovenian Police]]: since **July 2023**, more than 40 vishing cases targeting Slovenian **legal persons** (companies) under the guise of bank technical assistance were detected, with reported damages of approximately **EUR 3.8 million** and stolen funds routed to **bank accounts in Germany**. Slovenian police "took an active part" in Operation PANDORA based on "months of intensive cooperation, in particular with the German law enforcement authorities."

## Background

In December 2023, a customer of a Freiburg, Germany, bank requested a cash withdrawal of over EUR 100,000. The bank teller grew suspicious, learned that the customer believed they were assisting in a "fake police officer scam" investigation, and informed the **Freiburg Police (Polizeipräsidium Freiburg)**. Officers arrested the cash collectors at the moment of pickup, and surveillance was placed on the victim's phone line. Investigators quickly determined that the telephone numbers used by the perpetrators were linked to **over 28,000 scam calls in only 48 hours**.

The case was escalated to the **Baden-Württemberg State Criminal Police Office (Landeskriminalamt Baden-Württemberg, LKA BW)**, supported by the **Federal Criminal Police Office (Bundeskriminalamt, BKA)** — see [[germany-bka|Germany BKA]]. Prosecutorial supervision was provided first by the **Freiburg Public Prosecutor's Office (Staatsanwaltschaft Freiburg)** and subsequently by the **Karlsruhe Public Prosecutor's Office (Generalstaatsanwaltschaft Karlsruhe)**.

Investigators identified that the call centres responsible for the German victims were located across **[[albania|Albania]], [[bosnia-and-herzegovina|Bosnia and Herzegovina]], [[kosovo|Kosovo]] and [[lebanon|Lebanon]]**. A coordinated criminal network operated all four locations, with each country specialising in a distinct fraud script:

| Country | Specialised fraud type |
|---|---|
| [[bosnia-and-herzegovina\|Bosnia and Herzegovina]] | Debt-collection fraud |
| [[kosovo\|Kosovo]] | Online banking fraud |
| [[albania\|Albania]] | Investment fraud |
| [[lebanon\|Lebanon]] | Prepaid-card fraud |

Across all four locations, scammers also ran shock-call scripts (impersonating relatives, bank employees, customer-service agents and police officers), fake-lottery payouts, and romance scams.

In parallel, the **[[slovenia|Slovenian police]]** had since July 2023 been detecting a wave of fraudulent calls targeting Slovenian **legal persons** under the guise of bank technical-assistance staff, with stolen funds flowing to bank accounts in Germany — placing Slovenia on the victim-side of the same broader typology.

## Participating Parties

| Role | Party |
|---|---|
| Lead investigating jurisdiction | [[germany\|Germany]] |
| Lead operational coordinator | [[germany-bka\|Federal Criminal Police Office (Bundeskriminalamt, BKA)]] |
| Lead investigative unit | Baden-Württemberg State Criminal Police Office (Landeskriminalamt Baden-Württemberg) |
| Local detection and initial arrests | Freiburg Police (Polizeipräsidium Freiburg) |
| Lead prosecutor (initial) | Freiburg Public Prosecutor's Office (Staatsanwaltschaft Freiburg) |
| Lead prosecutor (subsequent) | Karlsruhe Public Prosecutor's Office (Generalstaatsanwaltschaft Karlsruhe) |
| EU operational coordinator | [[europol-ec3\|Europol]] (operational coordination centre at HQ; mobile offices deployed abroad on action day) |
| Action-day raiding jurisdiction | [[albania\|Albania]] (police forces) |
| Action-day raiding jurisdiction | [[bosnia-and-herzegovina\|Bosnia and Herzegovina]] (police forces) |
| Action-day raiding jurisdiction | [[kosovo\|Kosovo]] (police forces; status designation per UNSCR 1244/1999) |
| Action-day raiding jurisdiction | [[lebanon\|Lebanon]] (police forces) |
| Cooperating victim state | [[slovenia\|Slovenia]] (Slovenska policija — months of intensive cooperation, in particular with German law enforcement) |

## Legal Framework

The Europol primary release does not enumerate the formal cross-border instruments used (Budapest Convention articles, MLAT, European Investigation Order, Joint Investigation Team registration). Cooperation with non-EU jurisdictions ([[albania|Albania]], [[bosnia-and-herzegovina|Bosnia and Herzegovina]], [[kosovo|Kosovo]], [[lebanon|Lebanon]]) implies bilateral channels and Europol-facilitated coordination rather than purely EU-internal mutual-recognition mechanisms. The Slovenian release also does not name a specific instrument for the Slovenia–Germany cooperation arc.

> [!warning] Legal status check needed
> Specific instruments (Budapest Convention articles, MLAT, European Investigation Order, Joint Investigation Team registration) are not named in the cited Tier-1 primary sources. The frontmatter `legal_basis` is intentionally empty. The wiki record uses the more general [[asset-freezing]] mechanism tag rather than asserting unverified instruments.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2023-07 onwards | Slovenian police begin detecting vishing calls under the guise of bank technical assistance, mainly targeting Slovenian legal persons; >40 cases later identified, ~EUR 3.8 million damage; stolen funds flow to German bank accounts | policija.si 2024-05-03 |
| 2023-12 (date unspecified) | A bank teller in Freiburg, Germany flags a EUR 100,000 cash-withdrawal request as a suspected "fake police officer scam"; cash collectors arrested by Freiburg Police; 28,000+ scam calls linked to associated phone numbers in 48 hours | Europol 2024-05-02 (cited via policija.si) |
| 2023-12 → 2024-04 | Investigation expands; Baden-Württemberg State Criminal Police Office takes over, supported by BKA; 100+ German officers run a counter-call-centre, monitoring up to 30 calls at once and securing content of over 1.3 million calls; 7,500+ calls cross criminal-proceedings threshold; financial loss prevented in >80% of indicted crimes | Europol 2024-05-02 |
| 2023-12 → 2024-04 | Slovenian police cooperate with German law-enforcement authorities for "months", preventing losses to Slovenian citizens of "hundreds of thousands of euros" | policija.si 2024-05-03 |
| 2024-04-18 (early hours) | Action day: simultaneous raids on 12 call centres in Albania, Bosnia and Herzegovina, Kosovo and Lebanon, conducted by 60+ German officers and hundreds of local police, supported by Europol mobile offices abroad; 21 persons taken into custody; EUR 1 million in cash and assets seized | Europol 2024-05-02 |
| 2024-05-02 | Europol publishes primary press release announcing Operation PANDORA conclusion | europol.europa.eu |
| 2024-05-03 | Slovenska policija publishes parallel release confirming Slovenian victim arc and bilateral cooperation with German authorities | policija.si 2024-05-03 |

## Results and Impact

- **Call centres dismantled:** 12 (all four "perpetrator" countries combined).
- **Suspects identified:** 39.
- **Persons taken into custody on action day:** 21.
- **Calls intercepted and recorded:** over 1,300,000 over four months (December 2023 – April 2024).
- **Calls crossing criminal-proceedings threshold:** over 7,500.
- **Loss-prevention rate:** financial losses prevented in over 80% of indicted crimes.
- **Potential damages prevented:** over EUR 10 million.
- **Cash and assets seized:** EUR 1 million.
- **Other seizures:** data carriers, documents, large amount of electronic evidence enabling further investigation of additional call centres and fraudsters.
- **Slovenian victim-side detection (separate but adjacent figures):** more than 40 cases since 2023-07, approximately EUR 3.8 million in reported damage to Slovenian legal persons, with stolen funds traced to bank accounts in Germany; "hundreds of thousands of euros" in further losses prevented through Slovenia–Germany police cooperation.

## Cooperation Mechanisms Used

The Europol primary release describes the following cooperation pattern (informal but well-documented in the public record):

1. **Europol-hosted operational coordination.** Europol hosted multiple operational meetings before the action day and provided operational coordination plus financial support in preparation for the planned raids. On the action day, Europol hosted the **operational coordination centre** at its HQ (The Hague) and deployed officers with **mobile offices** to locations abroad in Albania, Bosnia and Herzegovina, Kosovo and Lebanon, facilitating the on-site collection and analysis of forensic evidence.
2. **German-led real-time interception with cross-border push.** From December 2023 onward, the Baden-Württemberg State Criminal Police Office monitored the actual conversations from the foreign call centres in real time, recording over 1.3 million calls, and ran a counter-call-centre to warn potential victims as the calls happened.
3. **Bilateral Slovenia–Germany cooperation.** Slovenian police cooperated for "months" with German law-enforcement authorities, preventing losses to Slovenian citizens. The release does not name a specific formal instrument.
4. **[[asset-freezing|Asset freezing]] / seizure on action day.** EUR 1 million in cash and assets, plus data carriers and electronic evidence, were seized at the 12 raided call centres.

## Challenges and Friction Points

- **Cross-border-with-non-EU coordination at scale.** Four of the five "perpetrator-side" jurisdictions (Albania, Bosnia and Herzegovina, Kosovo, Lebanon) are non-EU. The action day required Europol mobile offices to be physically deployed to each location to support evidence collection.
- **Real-time interception across multiple jurisdictions.** Recording over 1.3 million calls and processing 7,500+ over the criminal-proceedings threshold within four months required dedicated 24/7 staffing of a counter-call-centre by 100+ German officers.
- **Money-laundering downstream.** The Slovenian-side release identifies that stolen funds from Slovenian victims flowed to **bank accounts in Germany** — i.e. the action-day raids on the call centres did not, by themselves, dismantle the downstream money-mule and laundering pipeline.
- **Multilingual victim outreach.** The deployed officers had to identify victims as calls happened, in real time, and reach out to warn them — implying multilingual capability across the German victim base.

## Lessons Learned

- A single front-line bank-counter referral can seed a multi-month, multi-jurisdiction call-centre takedown. Bank-staff training in detecting fake-police-officer / fake-bank-employee withdrawal scripts is a high-leverage, low-cost upstream intervention.
- Real-time call-content interception with concurrent victim-warning is a workable counter-measure model when sustained at industrial scale (100+ officers, 1.3 million calls), and converts what would have been a reactive fraud-loss investigation into a near-real-time prevention operation.
- Country-by-country specialisation of fraud scripts within a single criminal network is now documented verbatim by a Tier-1 EU primary source: BiH = debt-collection, Kosovo = online banking, Albania = investment, Lebanon = prepaid-card. Comparable Western Balkans + Lebanon call-centre cases can be benchmarked against this fact pattern.
- The **victim-state perspective** (Slovenia) is essential for understanding the laundering downstream. Even when an Europol release names "participating countries", additional victim-state press releases (here: [[slovenia|Slovenia]]) reveal the further hops in the value chain (e.g., Slovenian victims' funds → German bank accounts → money mules abroad).

## Follow-Up Actions

- Court proceedings against the **39 identified suspects** (21 in custody on action day) were forthcoming after the 2024-05-02 announcement; the cited primary releases do not record final convictions or sentences, and these are not captured in the present record.
- Further investigation of "possible further call centres and more fraudsters" using the seized electronic evidence is explicitly anticipated by the Europol primary release.

## Korean Involvement (한국의 참여)

None reported. South Korea is not named in the cited Tier-1 primary sources as a participating jurisdiction or victim country. The fake-bank-employee / fake-police-officer + remote-instruction call-script typology is structurally similar to typologies used in Korean voice-phishing cases (보이스피싱), but the present operation has no direct Korean nexus.

## Contradictions & Open Questions

- The Europol primary release names five "Participating countries" (Germany, Albania, Bosnia and Herzegovina, Kosovo, Lebanon) but the Slovenian primary release describes Slovenian police as having "took an active part in the operation Pandora as well." The frontmatter `participating_countries` therefore includes [[slovenia|Slovenia]] in addition to the five Europol-listed states, on the basis of the Slovenian Police primary source. This is not a contradiction so much as a difference in scope between the Europol roster (action-day raiding states) and the Slovenian self-report (victim/cooperating state).
- The cited primary sources do not name a Joint Investigation Team registration, MLAT, or specific Budapest Convention articles, and the wiki record reflects this absence (`legal_basis: []`).
- Final court outcomes for the 21 in-custody and 39 identified suspects are not captured in the cited primary sources.
- The relationship (if any) between Operation PANDORA and the broader [[albania-austria-call-centre-investment-fraud-2026|Albania–Austria call-centre investment-fraud takedown (2026)]] is not addressed in any cited source. Both involve Albania-based call centres but the perpetrators, victim base, lead investigators and time periods differ.
- The release does not name [[eurojust|Eurojust]] as a coordinating body — Europol alone is named — so the wiki record does not assert Eurojust participation.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2024-05-03_policija-si_operation-pandora-12-phone-fraud-call-centres-slovenia\|Victims also from Slovenia. Europol's international operation Pandora shuts down 12 phone fraud call centres]] | Slovenska policija (Slovenian Police) | 2024-05-03 | https://www.policija.si/eng/newsroom/news-archive/news-archive/121805-victims-also-from-slovenia-europol-s-international-operation-pandora-shuts-down-12-phone-fraud-call-centres |
| [2] | Operation PANDORA shuts down 12 phone fraud call centres – 39 fraudsters organised flood of unsettling telephone scams, shocking and cheating thousands of victims | Europol | 2024-05-02 | https://www.europol.europa.eu/media-press/newsroom/news/operation-pandora-shuts-down-12-phone-fraud-call-centres |
