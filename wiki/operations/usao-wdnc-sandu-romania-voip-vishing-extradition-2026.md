---
type: operation
title: "USAO-WDNC US–Romania Extradition — Gavril Sandu VoIP Vishing / Bank Fraud (2009-2010 conduct, 2017 indictment, 2026 extradition)"
title_ko: "USAO-WDNC 미국–루마니아 범죄인 인도 — 가브릴 산두 VoIP 보이스피싱·은행사기 (2009-2010년 행위, 2017년 기소, 2026년 인도)"
aliases:
  - "Gavril Sandu Romania extradition 2026"
  - "WDNC Sandu vishing extradition"
  - "Sandu VoIP vishing bank fraud Charlotte 2026"
  - "Romanian National Appears in Federal Court Following Extradition from Romania"
case_id: CYB-2026-991
period: 3
operation_type: extradition
status: ongoing
enforcement_type:
  - arrest
  - extradition
outcome: success
timeframe:
  announced: 2026-05-05
  start: 2026-01-09
  end: 2026-04-30
  ongoing: true
crime_types:
  - "[[bank-fraud-ic]]"
  - "[[voice-phishing-ic]]"
  - "[[hacking-ic]]"
crime_type: "[[bank-fraud-ic]]"
target_entity: "Gavril Sandu, 53, Romanian national. Acting as part of a Romanian-resident hacker ring (2009-2010), Sandu and co-conspirators hacked small-business Voice-over-IP (VoIP) telephony systems in the United States and used the compromised infrastructure to conduct automated mass 'vishing' (voice-phishing) campaigns impersonating U.S. financial institutions. Victims surrendered debit-card numbers and PIN codes; Sandu cloned the harvested credentials onto fake physical cards with magnetic stripes and operated as a money mule, withdrawing cash from victims' accounts at U.S. ATMs and remitting a share back to the Romanian-based hacker ring."
lead_agency: "[[fbi]]"
coordinating_body: "[[office-of-international-affairs]]"
participating_countries:
  - "[[united-states]]"
  - "[[romania]]"
participating_agencies:
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
legal_basis:
  - "18 U.S.C. § 1344 (bank fraud)"
  - "18 U.S.C. § 1349 (conspiracy to commit bank fraud)"
  - "1924 United States – Romania extradition treaty"
  - "2003 EU–US extradition agreement (Romania as EU member state)"
mechanisms_used:
  - "[[extradition]]"
  - "[[mlat-process]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 surrender from Romania to United States (2026-04-30)"
    - "First federal court appearance in U.S. District Court for the Western District of North Carolina (Charlotte) (≈ 2026-05-05); defendant remanded into custody pending trial"
edges:
  - source_actor: "FBI Charlotte Field Office"
    target_actor: "Romanian authorities (Romanian National Police; Romanian Court of Appeal; Romanian Ministry of Justice)"
    cooperation_type: "extradition"
    legal_basis: "bilateral_MOU"
    direction: "directed"
  - source_actor: "USAO-WDNC"
    target_actor: "DOJ Office of International Affairs (OIA)"
    cooperation_type: "evidence_transfer"
    legal_basis: "MLAT"
    direction: "directed"
  - source_actor: "FBI Bucharest Legal Attaché (LEAT)"
    target_actor: "Romanian authorities"
    cooperation_type: "info_sharing"
    legal_basis: "bilateral_MOU"
    direction: "undirected"
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "Specific Romanian counterpart agency name (Romanian press release naming DIICOT or IGPR would tighten attribution)"
  - "Total victim count and total dollar loss for the 2009-2010 VoIP-vishing campaign (not disclosed in DOJ press release)"
  - "Co-conspirator identities (referenced but unnamed)"
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "FBI Legal Attaché (LEAT) offices serve as durable in-country liaison nodes that maintain bilateral cybercrime case continuity over multi-year (here: 17-year) fugitive recovery cycles."
  - "Pre-Budapest-Convention bilateral extradition treaties remain operationally effective for cybercrime where the underlying offense maps to traditional bank-fraud / wire-fraud statutes."
  - "Provisional arrest requests via DOJ OIA → Romanian Ministry of Justice succeed where the U.S. indictment was timely sealed (here: 2017 indictment for 2009-2010 conduct, executed in Romania in 2026)."
source_count: 1
sources:
  - "[[2026-05-05_justice-gov_romanian-national-appears-federal-court-following-extradition-romania-bank-fraud]]"
created: 2026-05-17
updated: 2026-05-17
---

## Summary

On **2026-04-30**, Romanian national **Gavril Sandu, 53**, was extradited from Romania to the United States after being arrested by Romanian authorities on **2026-01-09** pursuant to a U.S. provisional arrest request. Sandu had been indicted by a federal grand jury in Charlotte, North Carolina on **2017-11-14** on one count of conspiracy to commit bank fraud (18 U.S.C. § 1349) and one count of bank fraud (18 U.S.C. § 1344). He made his first federal court appearance in U.S. District Court for the Western District of North Carolina (USAO-WDNC) on the Monday following extradition arrival (≈ 2026-05-05) and was remanded into custody pending trial. If convicted, he faces a statutory maximum of 30 years in federal prison.

This case is a clean bilateral US-Romania extradition cooperation operating through the formal **DOJ Office of International Affairs (OIA)** ↔ **Romanian Ministry of Justice** channel under the **1924 US-Romania extradition treaty** (supplemented by the 2003 EU-US extradition agreement after Romania's 2007 EU accession). The investigation acknowledgments section of the USAO-WDNC press release names four cooperating LE/prosecutorial entities verbatim: FBI Charlotte Field Office, DOJ Office of International Affairs, FBI's Attaché Office in Bucharest, and Romanian authorities.

## Background

Between **May 2009 and October 2010**, Sandu and co-conspirators operating from Romania hacked into Voice-over-IP (VoIP) telephony systems of small U.S. businesses. They deployed automated scripts on the compromised PBX infrastructure to dial U.S. bank customers en masse, impersonating financial-institution employees in a classic "vishing" (voice-phishing) social-engineering pattern. Victims were tricked into reading aloud debit-card numbers, expiration dates, and PIN codes. Sandu's specific role was downstream: he received the harvested card data, encoded it onto blank cards with magnetic stripes, and acted as a money mule — visiting U.S. ATMs to withdraw cash from victims' accounts, retaining a share of the proceeds, and remitting the remainder to the Romanian-based hacker ring.

A federal grand jury in the Western District of North Carolina returned a sealed indictment against Sandu on **2017-11-14** charging conspiracy and substantive bank fraud. The indictment remained sealed pending Sandu's apprehension.

## Participating Parties

### United States

- **U.S. Department of Justice — U.S. Attorney's Office, Western District of North Carolina (USAO-WDNC)**: Lead prosecutor's office. U.S. Attorney Russ Ferguson.
- **Federal Bureau of Investigation, Charlotte Field Office** ([[fbi]]): Lead U.S. investigative agency. Special Agent in Charge Reid Davis.
- **DOJ Office of International Affairs (OIA)** ([[office-of-international-affairs]]): Channeled the formal extradition request and provisional arrest request to the Romanian Ministry of Justice.
- **FBI Attaché Office in Bucharest (LEAT)**: In-country liaison maintaining continuous case communication with Romanian counterparts over the 9-year cycle from sealed indictment to arrest.

### Romania

- **Romanian authorities** (named generically in the DOJ acknowledgments; per Romanian extradition procedure this encompasses the Romanian National Police / Politia Romana executing the arrest, the relevant Romanian Court of Appeal authorizing the surrender, and the Romanian Ministry of Justice signing the surrender order).

## Legal Framework

- **18 U.S.C. § 1344** (bank fraud) — substantive offense.
- **18 U.S.C. § 1349** (conspiracy to commit bank fraud) — agreement and acts in furtherance.
- **1924 U.S.–Romania extradition treaty** — bilateral basis for extradition obligation.
- **2003 EU-U.S. extradition agreement** — supplements the 1924 treaty after Romania's 2007 EU accession; standardizes documentation, transmission channels, and time limits for EU member states.
- **Budapest Convention on Cybercrime (CETS 185)** ([[budapest-convention]]) — Both the United States and Romania are States Parties; while not directly invoked in the underlying fraud statutes used here, the Convention's general procedural-cooperation framework reinforces the bilateral cooperation environment.

## Operational Timeline

| Date | Event |
|---|---|
| May 2009 – October 2010 | Underlying VoIP-vishing campaign conducted by Sandu and co-conspirators against U.S. bank customers. |
| 2017-11-14 | Federal grand jury in Charlotte, NC returns sealed indictment against Sandu (conspiracy + bank fraud). |
| 2017–2025 | DOJ OIA transmits provisional arrest request and extradition request to Romanian Ministry of Justice. FBI Bucharest LEAT maintains liaison. |
| 2026-01-09 | Romanian authorities arrest Sandu in Romania pursuant to U.S. provisional arrest request. |
| 2026-01-09 – 2026-04-29 | Romanian Court of Appeal extradition hearings; Romanian Ministry of Justice signs surrender order. |
| 2026-04-30 | Sandu surrendered to U.S. custody and transported to the United States. |
| ≈ 2026-05-05 | First federal court appearance in U.S. District Court for the Western District of North Carolina (Charlotte); remanded into custody. |
| Pending | Arraignment, pretrial motions, and trial. |

## Results and Impact

- **1 fugitive surrendered** from Romania to the United States after 9-year sealed-indictment fugitive-recovery cycle.
- **First federal court appearance** in U.S. District Court WDNC (Charlotte); defendant remanded into custody pending trial.
- **Statutory maximum exposure**: 30 years in federal prison.

## Cooperation Mechanisms Used

- **[[extradition]]** — Formal extradition under the 1924 US-Romania bilateral extradition treaty, supplemented by the 2003 EU-U.S. extradition agreement.
- **[[mlat-process]]** — DOJ OIA ↔ Romanian Ministry of Justice formal channel for transmission of the provisional arrest request, extradition documentation, and supporting evidence.
- **FBI Legal Attaché (LEAT) liaison** — In-country FBI Bucharest LEAT office maintained continuous case communication and operational liaison with Romanian counterparts over the multi-year cycle.

## Challenges and Friction Points

- **9-year sealed-indictment lag** between indictment (2017) and execution of arrest in Romania (2026). The 17-year lag between underlying conduct (2009-2010) and surrender (2026) reflects the operational reality that low-profile cybercrime money mules can evade extradition for over a decade in their home jurisdictions.
- **Generic Romanian counterpart attribution**: DOJ press release names "Romanian authorities" rather than the specific Romanian agency (likely DIICOT — Directorate for Investigating Organized Crime and Terrorism, or Politia Romana). A Romanian Ministry of Justice mirror press release would tighten attribution but does not appear to have been issued in tier-1 form.

## Lessons Learned

- **FBI LEAT durability**: In-country FBI Legal Attaché offices function as durable bilateral cybercrime case-continuity nodes that survive personnel turnover on both the U.S. and host-country sides.
- **Pre-Budapest-Convention treaty resilience**: The 1924 US-Romania extradition treaty remained operationally effective for cybercrime where the underlying offense maps to traditional bank-fraud statutes. This is consistent with the general pattern that cybercrime cooperation benefits from Budapest Convention procedural overlay but does not depend on it for extradition where bilateral treaties already exist.
- **Provisional-arrest-request channel reliability**: DOJ OIA's provisional arrest request via the Romanian Ministry of Justice succeeded in compelling Romanian National Police execution within a routine timeframe (likely days to weeks of submission), indicating mature US-Romania OIA-MoJ workflow.

## Follow-Up Actions

- Trial in U.S. District Court WDNC pending.
- Co-conspirators (referenced but unnamed in the public indictment) remain at large unless separately indicted under sealed dockets; OIA-Romania channel remains open for any follow-on requests.

## Korean Involvement (한국의 참여)

직접적인 한국 측 참여는 없음. 다만 본 건은 한국 검·경의 해외 도피 사이버사범 추적·인도 정책에 다음 두 시사점을 제공한다:

1. **재외 법무·경찰 주재관의 장기 역량 유지**: FBI 부쿠레슈티 LEAT 사무실이 17년에 걸쳐 루마니아 측과 연락을 유지해 결국 신병 인수에 성공했다는 점은, 한국 법무부·경찰청이 해외 공관에 배치한 법무협력관·경찰주재관의 장기 in-country liaison 역할이 결정적임을 보여준다. 단기 부임자가 매번 새로 관계를 구축하는 방식으로는 17년 cold-case 신병 확보가 불가능하다.

2. **부다페스트협약 미가입 시기에도 양자 인도조약 활용 가능**: 1924년 미국–루마니아 인도조약이 사이버범죄 (은행사기 매핑) 에 그대로 적용된 점은, 한국이 부다페스트협약 가입 절차가 진행 중인 동안에도 기존 양자 형사사법공조조약(MLAT)·인도조약으로 동등한 협력이 가능함을 다시 확인한다.

## Contradictions & Open Questions

- **Romanian counterpart agency naming**: The DOJ press release uses the generic "Romanian authorities" rather than naming the specific Romanian agency that executed the arrest. This is likely the Romanian National Police (Politia Romana) under DIICOT (Directorate for Investigating Organized Crime and Terrorism) supervision, but a Romanian-side mirror press release confirming the agency by name has not yet been located.
- **Co-conspirator status**: Press release references unnamed co-conspirators. Their indictment / extradition status is not stated. Likely either (a) still under sealed indictment with pending provisional arrest requests, (b) separately prosecuted in Romania under Romanian cybercrime law, or (c) statute-of-limitations-barred. Open question.
- **Total fraud loss and victim count**: The DOJ press release does not disclose the total dollar loss or total victim count for the 2009-2010 VoIP-vishing campaign. Only Sandu's personal money-mule role (ATM withdrawals) is described.

## Audit Note

| Country | Verification status | Source |
|---|---|---|
| [[united-states]] | Verified — USAO-WDNC + FBI Charlotte + DOJ OIA + FBI Bucharest LEAT all named in tier-1 press release | DOJ USAO-WDNC press release (2026-05-05) |
| [[romania]] | Verified — "Romanian authorities" named generically in tier-1 press release; bilateral cooperation confirmed by execution of provisional arrest (2026-01-09) and surrender (2026-04-30) | DOJ USAO-WDNC press release (2026-05-05); cross-verified in spotmedia.ro, mediafax.ro, g4media.ro |
