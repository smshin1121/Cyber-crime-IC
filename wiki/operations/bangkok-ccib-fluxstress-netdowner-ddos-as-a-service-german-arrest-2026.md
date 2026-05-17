---
type: operation
title: "Bangkok CCIB–Immigration Bureau arrest of Fluxstress/Netdowner DDoS-as-a-Service operator — German fugitive on INTERPOL Red Notice (2026)"
aliases:
  - "CCIB Fluxstress Netdowner DDoS-for-hire takedown Bangkok 2026"
  - "Noah Christopher Thonglor arrest April 2026"
  - "Thai Cyber Police–Immigration Bureau German DDoS kingpin Bangkok 2026"
case_id: CYB-2026-175
period: 3
operation_role: standalone
parent_operation: ""
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - evidence-seizure
outcome: success
timeframe:
  announced: 2026-04-11
  start: 2026-04-11
  end: 2026-04-11
  ongoing: false
crime_type: "[[ddos-ic]]"
crime_types:
  - "[[ddos-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "Noah Christopher (27, German national) — alleged developer and principal operator of the Fluxstress and Netdowner DDoS-as-a-Service / 'stresser-booter' platforms (active 2021–2025) selling cryptocurrency-paid Distributed Denial-of-Service attack services against organisational targets worldwide; also alleged to have developed ransomware and broader Cybercrime-as-a-Service (CaaS) tooling."
lead_agency: "[[thailand-royal-police]]"
coordinating_body: "[[interpol]]"
participating_countries:
  - "[[thailand]]"
  - "[[germany]]"
jurisdictions:
  - "[[thailand]]"
  - "[[germany]]"
participating_agencies:
  - "[[thailand-royal-police]]"
  - "[[germany-bka]]"
  - "[[interpol]]"
organizations:
  - "[[thailand-royal-police]]"
  - "[[germany-bka]]"
  - "[[interpol]]"
mechanisms_used:
  - "[[interpol-i24-7]]"
  - "[[extradition]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "INTERPOL Red Notice issued at the request of the Federal Republic of Germany — 74 outstanding German arrest warrants underlying the Red Notice"
  - "Thai Criminal Procedure Code authority for arrest of a foreign national subject to an INTERPOL Red Notice on Thai territory; Immigration Act authority for visa revocation (executed by Immigration Bureau on 9 April 2026, two days prior to the arrest)"
  - "Pending bilateral extradition request from the Federal Republic of Germany to the Kingdom of Thailand under the Thailand–Germany Extradition Treaty framework, in preparation as of the date of the primary release"
  - "European Union arrest warrants underlying additional charges (per Thai Examiner coverage of the CCIB press conference)"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "1 hardware cryptocurrency wallet (value not disclosed in primary release)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Electronic devices seized: 1 computer, 3 iPads, 1 tablet, 3 mobile phones, 1 hardware crypto wallet, miscellaneous documentation"
    - "74 outstanding German arrest warrants against the suspect (basis for the Red Notice — not an arrest count itself)"
    - "Thai immigration visa revoked 9 April 2026 (two days prior to arrest)"
edges:
  - source_actor: "[[thailand-royal-police]]"
    target_actor: "[[germany-bka]]"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "[[germany-bka]]"
    target_actor: "[[interpol]]"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "directed"
  - source_actor: "[[interpol]]"
    target_actor: "[[thailand-royal-police]]"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "directed"
credibility_index: 0.0
source_tier: 1
missing_fields:
  - "cryptocurrency_seized (value)"
  - "victims_notified (count)"
  - "extradition outcome (pending as of release date)"
related_cases: []
related_operations:
  - "[[operation-power-off-2026-04]]"
  - "[[operation-power-off]]"
  - "[[ddos-for-hire-sweep-2016]]"
challenges_encountered: []
lessons_learned: []
source_count: 2
sources:
  - "[[2026-04-11_ccib-go-th_fluxstress-netdowner-ddos-german-arrest-bangkok]]"
  - "[[2026-04-16_bka-de_operation-poweroff-fluxstress-netdowner-thai-custody]]"
created: 2026-05-17
updated: 2026-05-17
---


> [!info] Provisional / dual-source entry
> This page is published with `source_count: 2` (below the wiki's preferred publication threshold of 5) but corroborated by two **independent tier-1 own-domain releases from two cooperating jurisdictions**: (1) the Royal Thai Police Cybercrime Investigation Bureau (CCIB) release of 2026-04-11 (Thai LE side, names the German federal authorities and INTERPOL General Secretariat as cooperating partners), and (2) the joint Bundeskriminalamt (BKA) + Generalstaatsanwaltschaft Frankfurt am Main / Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT) release of 2026-04-16 (German LE side, explicitly confirms that the German national in Thai custody is the alleged operator of Fluxstress and Netdowner and that a § 127 StGB arrest warrant underlies the case). The page will be expanded further as Thai extradition proceedings progress and German federal indictment is filed.

## Summary

On 11 April 2026, officers of the Royal Thai Police Cyber Crime Investigation Bureau (CCIB / กองบัญชาการตำรวจสืบสวนสอบสวนอาชญากรรมทางเทคโนโลยี — บช.สอท.) together with the Immigration Bureau Investigation Division arrested a 27-year-old German national, Noah Christopher, at a luxury condominium on Thonglor Soi 25 in Watthana District, Bangkok. The arrest was executed pursuant to an INTERPOL Red Notice underpinned by 74 outstanding arrest warrants issued by German federal authorities. The CCIB statement explicitly identifies cooperation with "law-enforcement authorities of the Federal Republic of Germany and the INTERPOL General Secretariat."

The suspect is alleged to be the developer and principal operator of two DDoS-as-a-Service platforms — **Fluxstress** and **Netdowner** — active between 2021 and 2025, which sold cryptocurrency-paid Distributed Denial-of-Service ("stresser/booter") attacks against organisational servers worldwide. CCIB further attributes to him the development of ransomware tooling and a broader Cybercrime-as-a-Service (CaaS) offering.

## Background

**Modus operandi (DDoS-as-a-Service / "stresser-booter" platforms).** Fluxstress and Netdowner are two **DDoS-as-a-Service (DDoSaaS)** platforms — colloquially "stresser" or "booter" services — that the suspect is alleged to have developed and operated between **2021 and 2025**. Stresser-booter platforms expose a web-front-end (typically with self-service registration, tiered subscription plans, and a payment gateway) through which **paying customers select a target IP address or domain, choose attack vector(s)** (e.g., UDP flood, TCP SYN flood, HTTP/HTTPS layer-7 flood, amplification via DNS / NTP / Memcached reflectors), **attack duration (commonly seconds to tens of minutes per shot), and concurrency tier**, then receive on-demand Distributed Denial-of-Service traffic delivered against the chosen target. Behind the customer-facing storefront, the operator maintains a **back-end attack infrastructure of compromised servers, booter nodes, and amplification reflectors** that generate the actual attack traffic. The BKA + ZIT release of 2026-04-16 reports **40+ servers linked to the suspect identified and seized** during the Operation PowerOFF 2026-04 sprint, consistent with the back-end-infrastructure profile of a serious DDoSaaS platform. The CCIB also attributes to the suspect the development of **ransomware tooling and a broader Cybercrime-as-a-Service (CaaS) offering** beyond pure DDoSaaS, indicating a multi-product CaaS operator rather than a DDoSaaS-only operator. Fluxstress and Netdowner are part of the long-running DDoS-for-hire ecosystem that has been a recurring target of international LE disruption (see [[operation-power-off]] and the [[operation-power-off-2026-04]] global April 2026 action week).

**Victim profile and impact.** **Victim count and victim profile are not enumerated in the cited primary releases.** DDoSaaS platforms in this 2021-2025 generation typically deliver tens of thousands to hundreds of thousands of paid attacks per year against a victim cohort dominated by **online gaming services, gaming-platform users (Minecraft / FiveM / Discord-server-hosted communities), competitive-esports rivals, web-hosting customers, individual creators / streamers, small-and-medium business websites, and selectively against government / law-enforcement / journalism targets**. The CCIB release describes the targeting class generically as "organisational servers worldwide." The BKA + ZIT release links the suspect to a broader Operation PowerOFF 2026-04 sprint context that targets the DDoSaaS ecosystem as a whole, implying that the German federal investigation has developed a victim-attribution dataset beyond what the CCIB arrest release discloses publicly. Per-victim or aggregate loss figures, downtime hours, and target categorisation are pending German prosecution disclosure and digital-forensic analysis of the seized devices.

**Financial flow.** The CCIB release reports that the platforms operated on **cryptocurrency payment** for the four-year period 2021-2025 (specific cryptocurrencies are not enumerated; BTC and the privacy-coin Monero are the standard DDoSaaS payment-mode pair in this generation). Customer payments would have flowed via the platform's customer-facing payment gateway into operator-controlled wallets, with subsequent conversion / fiat off-ramp / spending across the suspect's multi-jurisdiction residency footprint (UAE, China, Thailand). The action-day seizure of **1 hardware cryptocurrency wallet** is the key forensic asset for reconstructing the operator's proceeds-of-crime holdings; **value is not disclosed in the cited release** and will be developed through forensic analysis. Cross-jurisdictional spending pattern is consistent with the suspect's lifestyle profile (luxury condominium in Thonglor district, Bangkok). Aggregate four-year cryptocurrency throughput across the two platforms is not enumerated in the cited releases.

**Criminal organisation structure.** The cited CCIB primary release describes the suspect — **Noah Christopher, 27, German national** — as the **developer and principal operator** of both Fluxstress and Netdowner, without naming co-conspirators, affiliates, customer-base scale, or upstream-developer / downstream-reseller relationships. The OCG profile is therefore **a single-principal operator** at the public-attribution layer, though the back-end infrastructure scale (40+ servers per the BKA release) and the parallel ransomware + broader CaaS tooling attribution suggest that some operational support (hosting procurement, payment-processing front-end maintenance, customer-support handling) is either self-operated or contracted via untraced affiliates. The BKA + ZIT release of 2026-04-16 confirms a single-suspect § 127 StGB arrest-warrant target for the Fluxstress/Netdowner case, consistent with the CCIB single-principal framing. Co-conspirators (if any) are not named in either tier-1 release.

**Evasion trajectory.** Per the CCIB release and Thai press coverage, the suspect had evaded German authorities for several years by moving among the **United Arab Emirates, China and Thailand** before settling at a high-end Bangkok condominium. German federal LE traced his Thai presence and coordinated with the Thai CCIB; Thai Immigration revoked his visa on **9 April 2026** — two days before the joint CCIB–Immigration Bureau operation executed the arrest.

## Participating Parties

**Thailand:**
- [[thailand-royal-police|Royal Thai Police — Cyber Crime Investigation Bureau (CCIB)]] — lead operational agency
- Immigration Bureau (สำนักงานตรวจคนเข้าเมือง) Investigation Division — co-executing agency; visa revocation; arrest execution
  - Commander Phanop Warathanachakun
  - Deputy Commanders Ratchot Chotikun and Chitdecha Songhong
  - Superintendent Pisit Sri-on
- International Criminal Investigation Bureau (Division 2) — international liaison support
- Royal Thai Police Division 3 (Legal Proceedings) — extradition paperwork

**Germany:**
- [[germany-bka|German federal law-enforcement]] — issuing authority for the 74 arrest warrants; intelligence partner that traced the suspect's Thai location and coordinated with Thai CCIB

**Multilateral:**
- [[interpol|INTERPOL General Secretariat]] — issued the Red Notice on behalf of Germany; provided coordination channel between German and Thai LE

## Legal Framework

The arrest rests on three layered instruments:

1. **74 German domestic arrest warrants** — substantive criminal charges (specific German statute identifiers not enumerated in the CCIB release; per Thai press reports, charges span hacking, extortion, ransomware, cryptocurrency-payment-channel cybercrime)
2. **INTERPOL Red Notice** — international apprehension request based on the German warrants, issued by INTERPOL General Secretariat and propagated via the [[interpol-i24-7|INTERPOL I-24/7 secure communications network]] to all member countries' National Central Bureaus
3. **Thai Criminal Procedure Code + Immigration Act** authority for arrest of a foreign national subject to a valid Red Notice on Thai territory, executed with prior visa revocation by the Immigration Bureau

European Union–level warrants are also reported to be among the 74 warrants underlying the arrest, indicating that the substantive criminal liability extends across multiple EU jurisdictions beyond Germany alone.

Extradition proceedings to return the suspect to Germany are in preparation as of the date of the primary release; they will proceed under the Thailand–Germany [[extradition|extradition]] treaty framework.

## Operational Timeline

| Date | Event |
|---|---|
| 2021 | Fluxstress / Netdowner DDoS-as-a-Service platforms begin operating (per CCIB statement) |
| 2025 | Platforms remain active through approximately end of period (per CCIB statement) |
| (Multi-year prior to 2026) | Suspect reportedly evades German authorities by moving between United Arab Emirates, China, and Thailand |
| 2026-04-09 | Thai Immigration Bureau revokes the suspect's Thai visa |
| 2026-04-11 | CCIB and Immigration Bureau Investigation Division execute joint arrest at Thonglor Soi 25, Watthana District, Bangkok |
| 2026-04-11 (same day) | CCIB hosts press conference announcing arrest; identifies cooperation with German federal LE and INTERPOL |
| 2026-04-11 onwards | Digital forensic analysis of seized devices commences; Thai authorities finalising paperwork for extradition to Germany |
| 2026-04-16 | Bundeskriminalamt (BKA) and Generalstaatsanwaltschaft Frankfurt am Main / ZIT issue joint press release on the broader [[operation-power-off-2026-04|Operation PowerOFF 2026-04]] sprint; confirm that the German national in Thai custody is the ZIT-led suspect alleged to operate Fluxstress and Netdowner under a § 127 StGB arrest warrant; report 40+ servers linked to the suspect identified and seized |

## Results and Impact

- **1 arrest** (Noah Christopher, 27, German national)
- **74 outstanding German/EU warrants** activated for surrender via extradition
- **Seizures**: 1 computer, 3 iPads, 1 tablet, 3 mobile phones, 1 hardware cryptocurrency wallet, miscellaneous documentation
- **Visa revoked** by Thai Immigration two days before arrest (pre-arrest deportability lever)

The CCIB release does not quantify the global victim population of Fluxstress and Netdowner customers, nor the cryptocurrency throughput across the four years of platform operation; these figures are expected to be developed during the German prosecution and through digital-forensic analysis of the seized devices.

## Cooperation Mechanisms Used

- **[[interpol-i24-7|INTERPOL I-24/7]] / Red Notice channel** — primary international coordination instrument that connected the German arrest-warrant base to the Thai operational arrest
- **[[informal-cooperation|Informal police-to-police cooperation]]** — direct intelligence-sharing between German federal LE and the Thai CCIB to localise the suspect in Bangkok
- **Visa-revocation lever** (Thai Immigration Act) — used to weaken the suspect's legal residency status two days prior to arrest, ensuring deportability/extraditability
- **[[extradition|Bilateral extradition]]** — Thai–German extradition procedure in preparation as of the date of release; will determine the post-arrest legal pathway

## Challenges and Friction Points

- Multi-year evasion across UAE, China, and Thailand — illustrates persistent challenges in pursuing DDoS-as-a-Service operators who shift hosting and physical presence between jurisdictions with varying LE engagement profiles
- Cryptocurrency payment channel — complicates victim attribution and proceeds-of-crime tracing; the seized hardware wallet is a key forensic asset
- 74-warrant breadth — implies coordination between German federal and state (Land) prosecutors and possibly multiple EU member-state warrants; the CCIB release does not disambiguate

## Korean Involvement (한국의 참여)

None identified in the primary release. No Korean victims or LE involvement reported.

## Contradictions & Open Questions

- **Suspect age**: CCIB and most Thai press list the suspect as 27 years old; one Twitter/X report cited "26-year-old". The 27 figure is the version in the primary CCIB release and Bangkok Post coverage of the press conference.
- **Press-release date**: The CCIB site lists the release under the URL slug "2026-april-6", but the arrest itself occurred on 11 April 2026 according to the CCIB statement, Thai press, and English-language Thai/international coverage. The "april-6" string in the URL appears to be an internal slug rather than the publication date.
- **Platform name**: "Netdowner" appears in most reports; some sources render it "Neldowner". Both are referenced to a single platform.
- **European Union warrants**: Thai Examiner coverage refers to EU-issued warrants in addition to the German warrants, but the CCIB release does not enumerate them separately; the relationship between the German-state warrants and the EU-level warrant base will become clearer through the extradition record.
- **Specific German agency**: CCIB release uses the generic phrasing "law-enforcement authorities of the Federal Republic of Germany". The BKA + ZIT release of 2026-04-16 ([[2026-04-16_bka-de_operation-poweroff-fluxstress-netdowner-thai-custody]]) resolves this: the German lead-prosecution authority is the **Generalstaatsanwaltschaft Frankfurt am Main – Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT)** with **Bundeskriminalamt (BKA)** as the federal-police investigative partner. The originating Landeskriminalamt is still not separately identified.
- **L26 gap notes**: (a) Aggregate victim count, per-victim downtime impact, and target categorisation (gaming-platform users vs. SME web hosts vs. government / journalism targets) are not enumerated in the cited tier-1 releases; pending German prosecution disclosure. (b) Aggregate cryptocurrency throughput across the four-year platform-operating period and the value held on the seized hardware wallet are not disclosed. (c) Co-conspirators (back-end infrastructure operator, payment-processor operator, customer-support staff) are not named in the cited tier-1 releases; the CCIB and BKA + ZIT frames are single-principal.

## Sources

- [[2026-04-11_ccib-go-th_fluxstress-netdowner-ddos-german-arrest-bangkok]] — Royal Thai Police CCIB primary press release (11 April 2026; ccib.go.th own-domain)
- [[2026-04-16_bka-de_operation-poweroff-fluxstress-netdowner-thai-custody]] — Bundeskriminalamt (BKA) + Generalstaatsanwaltschaft Frankfurt am Main / ZIT joint press release on Operation PowerOFF 2026-04 sprint (16 April 2026; bka.de own-domain). Explicitly confirms the German national in Thai custody is the alleged operator of Fluxstress and Netdowner; § 127 StGB arrest warrant.
