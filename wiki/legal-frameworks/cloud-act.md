---
type: legal-framework
title: "CLOUD Act (Clarifying Lawful Overseas Use of Data Act)"
official_name: "Clarifying Lawful Overseas Use of Data Act"
official_name_ko: "해외데이터합법적사용명확화법"
aliases: ["CLOUD Act", "H.R. 4943", "Pub.L. 115-141"]
framework_type: "bilateral-treaty"
adopted_date: "2018-03-23"
entry_into_force: "2018-03-23"
depositary: ""
sponsoring_body: "[[us-doj]]"
status: "in-force"
parties:
  states_parties: 2
  signatories: 0
  notable_non_parties: ["South Korea", "Japan", "Germany", "France"]
key_provisions:
  - article: "Section 103"
    topic: "Required disclosure — US providers must comply regardless of data location"
    relevance: "US warrant/order authority extends to data held by US providers abroad; eliminates Microsoft Ireland gap"
  - article: "Section 104"
    topic: "Comity analysis for motions to quash"
    relevance: "Providers may move to quash if disclosure conflicts with foreign law; multi-factor comity test"
  - article: "Section 105"
    topic: "Executive agreements framework"
    relevance: "Authorizes bilateral agreements allowing qualifying foreign governments to directly order US providers to disclose data — bypasses MLAT"
  - article: "Executive Agreement certification"
    topic: "Qualifying foreign government requirements"
    relevance: "Foreign government must demonstrate: rule of law, adequate privacy protections, independent judicial oversight"
scope:
  substantive_law: false
  procedural_law: true
  international_cooperation: true
  jurisdiction: true
  evidence: true
  data_protection: true
related_frameworks:
  - "[[budapest-convention]]"
  - "[[second-additional-protocol]]"
implementing_mechanisms: []
operations_enabled: []
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

The CLOUD Act (Clarifying Lawful Overseas Use of Data Act) is a **US federal law** enacted on 2018-03-23 that addresses the critical problem of cross-border access to electronic evidence held by US-based service providers. The Act has two primary components: (1) it clarifies that US legal process (warrants, subpoenas, court orders) applies to data held by US providers regardless of where the data is stored globally, and (2) it creates a framework for **executive agreements** with qualifying foreign governments, enabling those governments to directly order US providers to disclose data without going through the traditional [[mlat-process|MLAT process]].

The Act was passed in direct response to the *Microsoft Ireland* litigation (United States v. Microsoft Corp., 584 U.S. ___ (2018)), which raised the question of whether a US warrant could compel Microsoft to disclose email data stored in Ireland. The CLOUD Act resolved this by asserting extraterritorial reach of US legal process to US providers.

As of April 2026, the **United Kingdom** is the only country with a fully operational executive agreement (signed 2019-10-03, entered into force 2022-10-03). Australia has signed an agreement (2021-12-15) that is *likely* in force or near entry into force.

## Historical Context

- **2013:** Microsoft refuses to comply with US warrant for data stored in Ireland
- **2014-2017:** *United States v. Microsoft Corp.* litigated through courts; Second Circuit rules in Microsoft's favor (data abroad not reachable by US warrant)
- **2018-03-23:** CLOUD Act enacted as part of the Consolidated Appropriations Act, 2018
- **2018-04:** Supreme Court vacates *Microsoft Ireland* as moot following CLOUD Act passage
- **2019-10-03:** US-UK executive agreement signed (first under CLOUD Act)
- **2021-12-15:** US-Australia executive agreement signed
- **2022-10-03:** US-UK agreement enters into force
- **Ongoing:** Negotiations with EU, Canada, and other partners

## Key Provisions for International Cooperation

### Section 103: Extraterritorial Reach

US providers (Google, Meta, Apple, Microsoft, etc.) must comply with US legal process (warrants under 18 U.S.C. 2703, pen register/trap-and-trace orders, etc.) **regardless of where the data is stored**. This applies to any provider subject to US jurisdiction.

**IC implication:** Foreign governments seeking data from US providers can use the MLAT channel to request the US to issue domestic process against the provider. The CLOUD Act ensures the US can compel disclosure even if data is stored in a third country.

### Section 104: Comity Analysis

Providers may file a motion to quash or modify US legal process if:
1. The customer/subscriber is not a US person, and
2. Disclosure would create a material risk of violating the laws of a qualifying foreign government

The court applies a **multi-factor comity analysis** weighing US government interests, foreign government interests, data location, customer nationality, and provider ties.

### Section 105: Executive Agreements

The most significant IC innovation. The Act authorizes the US Attorney General (with SecState concurrence) to enter into executive agreements with qualifying foreign governments. Under such agreements:

- **Foreign government authorities** may directly order US providers to disclose data for serious crime investigations
- **US authorities** may directly order providers in the foreign partner's territory
- Bypasses the traditional MLAT channel entirely for qualifying requests
- Orders must target **specific persons or accounts** (no bulk surveillance)
- Orders must comply with the foreign government's domestic law

**Qualifying foreign government requirements:**
1. Robust substantive and procedural protections for privacy and civil liberties
2. Respect for rule of law and non-discrimination
3. Adherence to applicable international obligations (including human rights)
4. Independent judicial oversight or independent oversight mechanism

### Executive Agreement Flow

```
Foreign LEA identifies need         US LEA identifies need
for US-held data                    for foreign-held data

Foreign LEA obtains domestic        US LEA obtains US legal process
legal authorization (e.g.,          (warrant, court order)
court order under local law)

Foreign authority serves order      US authority serves order
directly on US provider             directly on foreign provider

Provider discloses data             Provider discloses data
to foreign authority                to US authority

No MLAT, no diplomatic channel, no central authority routing
```

## Parties and Participation

| Country | Agreement Status | Date | Notes |
|---------|-----------------|------|-------|
| [[united-kingdom]] | In force | 2022-10-03 | First CLOUD Act executive agreement; covers content and non-content data |
| [[australia]] | Signed | 2021-12-15 | Implementation status to be confirmed |
| EU | Under negotiation | Ongoing | Complex due to GDPR considerations and 27 member states |
| Canada | Under negotiation | Ongoing | |

> [!warning] Legal status check needed
> Additional executive agreements may have been signed or entered into force since this page was created. The US DOJ OIA website should be consulted for current status.

## Implementation in Practice

### UK Executive Agreement

The US-UK agreement is the primary implementation reference:
- UK authorities (primarily NCA and Crown Prosecution Service) can directly serve orders on US providers
- Orders must target specific accounts, not bulk data
- UK authorities cannot target US persons
- Reciprocal: US authorities can serve orders on UK-based providers
- Reporting and review mechanisms built into the agreement

### Practical Impact

The CLOUD Act and executive agreements have *likely* significantly reduced evidence access delays for qualifying partners:
- **MLAT average:** 6-18 months for US-held data
- **CLOUD Act executive agreement:** Days to weeks (provider response time)

However, the impact is limited to **countries with executive agreements** — currently a very small number.

## Relationship to Other Frameworks

### Budapest Convention

The CLOUD Act and [[budapest-convention]] are complementary:
- Budapest provides the broad multilateral IC framework (MLA, preservation, 24/7 Network)
- CLOUD Act executive agreements offer a fast bilateral channel for data access from US providers
- Both can operate simultaneously; CLOUD Act does not replace MLAT obligations

### Second Additional Protocol

The [[second-additional-protocol]] addresses similar problems (direct provider access, expedited disclosure) through a multilateral treaty mechanism. The Protocol's Art. 6-7 (direct cooperation with service providers) and the CLOUD Act's executive agreements represent **parallel approaches** developed in the same period.

### UN Cybercrime Convention

The [[un-cybercrime-convention-2024]] IC chapter may eventually provide an alternative multilateral framework, but the CLOUD Act's bilateral executive agreement model is *likely* to remain the fastest channel for US-held data access.

## Criticisms and Debates

### Extraterritorial Reach

The CLOUD Act's assertion that US process reaches data stored anywhere in the world has been criticized as:
- **Unilateral extraterritoriality:** Imposing US legal authority on data in foreign jurisdictions without consent
- **Sovereignty tension:** Other nations may enact blocking statutes or data localization laws in response
- **Conflicting obligations:** US providers may face conflicting legal obligations when US process conflicts with foreign data protection laws (e.g., GDPR)

### Privacy Concerns

- Executive agreements enable **foreign government access to data held in the US** — critics argue this circumvents warrant protections that US persons enjoy
- The "qualifying foreign government" requirements may be applied loosely under diplomatic pressure
- Limited public transparency about agreement negotiations and implementation

### Selectivity and Inequality

- Only countries that meet US certification standards can obtain executive agreements
- This creates a **two-tier system:** Agreement partners get fast access; all others remain on the slow MLAT track
- Developing countries with weaker rule-of-law indicators are *unlikely* to qualify for executive agreements in the near term, exacerbating the digital divide in IC capacity

### EU/GDPR Tension

EU data protection authorities have expressed concern about:
- US providers disclosing EU residents' data to non-EU authorities under CLOUD Act executive agreements
- Adequacy of safeguards in the CLOUD Act compared to GDPR Chapter V (international transfers)
- Impact on the EU-US Data Privacy Framework

## Korean Perspective (한국 관점)

South Korea does **not** currently have a CLOUD Act executive agreement with the United States. This has significant implications:

### Current Situation

Korean law enforcement agencies (경찰청 사이버수사국 [[knpa-cyber-bureau]], 대검찰청 국제협력과) seeking data from US-based providers (Google, Meta, Apple, Microsoft) must rely on:
1. **MLAT channel:** Korea-US MLAT (2000) through central authorities — 6-18 months typical
2. **Emergency preservation:** Budapest Convention Art. 29 via [[24-7-network]] for preservation only (since 2024 accession) — hours/days for preservation, but production still requires MLAT
3. **Voluntary provider disclosure:** Direct requests to provider law enforcement response teams — limited scope, no compulsion
4. **Provider offices in Korea:** Some providers maintain Korean offices that may facilitate certain requests under Korean domestic legal process

### Strategic Implications

A CLOUD Act executive agreement would *likely* significantly improve Korean LEA access to US-held data, reducing evidence access times from months to days. However:
- Korea would need to demonstrate compliance with US certification requirements (rule of law, privacy protections, independent oversight)
- Korea's Personal Information Protection Act (개인정보 보호법, PIPA) provides a strong data protection framework that *likely* supports qualification
- Political and diplomatic considerations (US-Korea alliance context) are *likely* favorable
- The Korean National Assembly (국회) would need to approve any implementing legislation

### Open Question

Whether Korea should prioritize a CLOUD Act executive agreement, ratification of the [[second-additional-protocol]], or both remains an open policy question. The two approaches are not mutually exclusive but require separate diplomatic and legislative tracks.

> [!note] Translation note
> "해외데이터합법적사용명확화법" is the commonly used Korean translation. The Act's full English title is "Clarifying Lawful Overseas Use of Data Act." Korean legal commentary also refers to it as "클라우드법" (transliteration).

## Contradictions & Open Questions

1. **EU executive agreement:** Will the EU negotiate a collective agreement or leave it to individual member states? GDPR implications make this the most complex pending negotiation.
2. **Korean agreement prospects:** What is the timeline for a US-Korea CLOUD Act executive agreement? No public negotiations have been announced.
3. **Proliferation:** As more executive agreements are signed, will the web of bilateral obligations become unmanageable? Some argue a multilateral approach (Protocol or UN Convention) is preferable.
4. **Provider compliance disparities:** Do all US providers respond to executive agreement orders with equal speed and completeness? Anecdotal reports suggest significant variation.
5. **Australia agreement status:** Has the US-Australia executive agreement entered into force? Public reporting is limited.
