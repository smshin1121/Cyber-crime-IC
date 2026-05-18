## 개요

**Operation Cronos Phase 1**(크로노스 작전 1단계)은 2022년 이래 전 세계적으로 가장 많이 배포된 랜섬웨어 변종인 **LockBit(랜섬웨어 그룹)**을 와해시킨 기념비적 국제 법집행 조치였다. 2024년 2월 20일, 10개국의 기관들이 [[uk-nca|UK National Crime Agency(NCA, 영국 국가범죄청)]]의 주도와 [[europol-ec3|Europol(유럽 경찰청)]] 및 [[eurojust|Eurojust(유럽사법협력기구)]]의 조율 하에 LockBit 인프라를 조율 테이크다운하였다.

본 작전의 결과로 8개국에 걸쳐 34대의 서버가 압수되었으며, 2명이 체포되고, 5건의 기소가 이루어졌으며, 200개 이상의 암호화폐 계정이 동결되고, 14,000개 이상의 비인가(rogue) 계정이 식별되었다. 무료 복호화 도구는 "No More Ransom" 포털을 통해 전 세계 피해자에게 제공되었다.

이는 표적의 규모(LockBit은 전 세계적으로 지배적 랜섬웨어 변종이었음)와 관련된 국제공조의 폭 양 측면에서 *거의 확실히(almost certainly)* 역사상 가장 중요한 랜섬웨어 와해 작전 중 하나였다.

## 배경

### 수법(모더스 오페란디)

LockBit은 **2019년 말**(초기에는 "ABCD" 랜섬웨어로 알려짐)에 등장하여, 2022년에는 **전 세계적으로 가장 많이 배포되는 랜섬웨어 변종**이 되었다. 본 그룹은 **랜섬웨어서비스형(RaaS)** 플랫폼으로 운영되었다: LockBit의 코어 개발팀은 암호화 바이너리, 어필리에이트(affiliate) 관제 패널, 그리고 공개적으로 운영되는 데이터 유출 사이트(`lockbitsupp` / `lockbitsupp.gov.uk` 형태의 Tor 미러)를 유지하였으며, 계층화된 어필리에이트 네트워크가 실제 침입을 수행하였다. 어필리에이트는 구매한 자격증명, 공개 노출 취약점(예: Fortinet, Citrix, ESXi) 악용, 그리고 피싱을 통해 초기 접근을 확보하였고; 정찰 및 측면이동(lateral-movement) 도구(Cobalt Strike, Mimikatz)를 배포하였으며; StealBit이나 rclone 같은 도구를 통해 데이터를 유출한 후; 최종적으로 피해자 환경 전체에 LockBit 암호화기를 폭발(detonate)시켰다. 본 그룹은 **이중 갈취(double-extortion)** 모델 — 암호화 후 유출 — 을 사용하였으며, LockBit 2.0 이후로는 운영자들이 **삼중 갈취(triple-extortion)** 요소(지불을 거부한 피해자에 대한 DDoS 압박)를 실험하였다.

### 피해자 프로파일 및 영향

동일 수사에 연계된 이후의 미국 DOJ 기소 자료(see [[operation-cronos-phase2]])에 따르면, LockBit은 **최소 120개국에서 2,500명 이상의 피해자**를 공격하였으며, 그중 미국에서만 **약 1,800명**의 피해자가 포함된다. 피해자 부문은 **병원 및 의료기관, 학교 및 대학, 핵심 인프라 운영자, 다국적 기업, 중소기업, 그리고 정부 및 법집행 기관**에 걸쳐 있다. 영국 NCA의 2024년 2월 와해 발표에서는 LockBit이 "수십억 파운드"의 피해를 야기했다고 특징지었고; 영국 FCDO의 2024년 5월 제재 성명은 전 세계 수천 명의 피해자로부터 갈취한 수익을 **"미화 10억 달러 초과"**로 명시하였다.

### 자금 흐름

랜섬 지불은 **비트코인**으로 어필리에이트 통제 지갑에 송금되었다. 표준 분배 비율은, 이후 미국 DOJ의 LockBit 개발자 Dmitry Khoroshev 기소 문서에서 확인된 바와 같이, **개발자 20% / 어필리에이트 80%** 분배였다. 2024년 2월 와해 시점에 NCA 주도의 인프라 접근으로 대규모 암호화폐 자금세탁 증거가 드러났으며, 작전일에 본 그룹과 연결된 **200개 이상의 암호화폐 계정이 동결되었다**. Khoroshev 개인은 이후(Phase 2) 개발자 분배금 지급으로 **최소 미화 1억 달러**의 암호화폐를 수령한 것으로 주장되었다.

### 범죄 조직 구조

LockBit은 **코어 개발자 + 어필리에이트** 모델로 운영되었다. 소규모 코어 팀(Khoroshev 및 관련자들)이 랜섬웨어 코드베이스, 어필리에이트 패널, 데이터 유출 사이트, 그리고 협상 채팅 인프라를 유지하였다. 패널 접근 권한을 부여받기 전에 검증을 거친 어필리에이트들에는 이후 미국/프랑스/폴란드/우크라이나 기소 문서에 명시된 다음 인물들이 포함된다: Mikhail Vasiliev(러시아-캐나다 이중국적, 2022년 캐나다에서 체포, 2024년 미국으로 이송), Ruslan Astamirov(러시아 국적, 2023년 애리조나에서 체포), Mikhail Matveev / "Wazawaka" / "Boriselcin", Artur Sungatov, Ivan Kondratyev / "Bassterlord". 이는 *highly likely* 2022-2024년 RaaS 조직의 전형적(modal) 패턴이다.

### Investigation Origins

장기간에 걸친 다년간의 준비가 와해에 선행하였다: [[europol-ec3|Europol]]은 **27차례의 작전 회의와 4회의 기술 스프린트**를 조직하였고, 참여 기관 간에 추정 **1,000건 이상의 SIENA 메시지**가 교환되었다. 영국 [[uk-nca|National Crime Agency]]가 작전 축을 주도하였으며, 어필리에이트 패널 및 코어 서버에 대한 은밀한 접근을 확보하고 있었다; 프랑스 사법당국은 작전일 폴란드 및 우크라이나에서의 체포를 촉발한 체포영장 프레임워크를 제공하였다.

## 참여 당사자

### Lead Agency
- [[uk-nca|UK National Crime Agency (NCA, 영국 국가범죄청)]]

### Coordinating Bodies
- [[europol-ec3|Europol(유럽 경찰청)]] — 작전 조율, 분석 지원, 27차례 작전 회의
- [[eurojust|Eurojust(유럽사법협력기구)]] — 사법 조율

### Participating Countries (10)
프랑스, 독일, 네덜란드, 스웨덴, 호주, 캐나다, 일본, 영국, 미국, 스위스

### Supporting Countries (4)
핀란드, 폴란드, 뉴질랜드, 우크라이나

### Participating Agencies (12)
[[uk-nca]], [[europol-ec3]], [[eurojust]], [[france-gendarmerie|French Gendarmerie(프랑스 헌병대)]], [[germany-bka|German BKA(독일 연방수사청)]], [[netherlands-politie|Dutch National Police(네덜란드 국가경찰)]], [[sweden-police|Swedish Police(스웨덴 경찰)]], [[australia-afp|Australian Federal Police(호주 연방경찰)]], [[canada-rcmp|RCMP(캐나다 기마경찰)]], [[japan-npa|Japanese NPA(일본 경찰청)]], [[fbi-cyber-division|FBI(미국 연방수사국)]], [[switzerland-fedpol|Swiss Fedpol(스위스 연방경찰)]]

## 법적 근거

본 작전은 복수 관할권에서의 사법 조치를 수반하였다:
- **프랑스 당국**은 체포영장 및 기소를 발부
- **미국 당국**은 기소 발부(프랑스와 미국 합산 5건)
- **체포**는 프랑스 사법당국의 요청에 따라 폴란드 및 우크라이나에서 집행

> [!info] Legal-basis note
> (한국어 번역: 국경 간 집행 조치에 대한 구체적인 법적 근거(조약 규정, 국내 권한)는 추가 출처를 통해 확인할 필요가 있다.)

## 작전 타임라인

| 날짜 | 사건 |
|------|-------|
| Pre-2024 | 27차례 Europol 작전 회의를 포함한 다년간 수사 |
| Pre-2024 | 4회 기술 스프린트 수행 |
| 2024-02-20 | 조율 작전일: 8개국에 걸쳐 34대 서버 압수 |
| 2024-02-20 | 폴란드 및 우크라이나에서 2명 체포 |
| 2024-02-20 | 200개 이상의 암호화폐 계정 동결 |
| 2024-02-20 | 14,000개 이상의 비인가 계정 식별 |
| 2024-02-20 | No More Ransom에 복호화 도구 공개 |

## 결과 및 영향

| 지표 | 수치 |
|--------|-------|
| 체포 | 2 (폴란드, 우크라이나) |
| 국제 체포영장 | 3 |
| 기소 | 5 (프랑스, 미국) |
| 압수 서버 | 34 (8개국 전역) |
| 동결 암호화폐 계정 | 200+ |
| 식별된 비인가 계정 | 14,000+ |
| 작전 회의 | 27 |
| 기술 스프린트 | 4 |
| 교환 SIENA 메시지 | 1,000+ |

"No More Ransom" 포털(37개 언어로 제공되며, 150여 종의 랜섬웨어에 대한 120여 개의 솔루션을 포함)에 무료 복호화 도구를 공개한 것은 *highly likely* 전 세계 피해자에게 즉각적인 구제를 제공한 것으로 평가된다.

## 활용된 협력 메커니즘

- **SIENA**(Secure Information Exchange Network Application): 1,000건 이상의 작전 메시지 교환
- **Europol 작전 회의:** 27차례 회의가 계획 및 조율을 위해 조직됨
- **기술 스프린트:** 조율된 기술 분석을 위한 4회 스프린트
- **No More Ransom 포털:** 피해자 복호화 도구 배포를 위한 민관 공동 이니셔티브

## 교훈

1. **다년 조율의 효용성:** 27차례의 작전 회의 및 4회의 기술 스프린트에 대한 지속적 투자는, 표적이 인프라를 이전하지 못하도록 막는 데 필수적인 다국적 동시 조치를 가능하게 하였다.
2. **피해자 중심 접근:** No More Ransom을 통한 신속한 복호화 도구 공개는, 작전 산출물이 단순히 집행 목적뿐만 아니라 피해자에게도 직접적인 이익이 될 수 있음을 보여주었다.
3. **SIENA의 중추적 역할:** 1,000건 이상의 SIENA 메시지는 본 플랫폼이 대규모 EU 조율 작전을 위한 핵심 보안 통신 채널임을 확인시켰다.
4. **단계적 접근:** 본 작전은 지속적인 캠페인(1단계)으로 설계되었으며, 후속 조치가 계획되었다 — 이는 *highly likely* 랜섬웨어 생태계에 대한 지속적 압박을 유지하기 위한 의도적 설계였다.

## 후속 조치

- [[operation-cronos-phase3|Operation Cronos Phase 3]] (2024년 10월): 추가 4명 체포, 서버 9대 압수, Evil Corp 어필리에이트에 대한 금융 제재

## 한국의 참여

Operation Cronos Phase 1에서 한국의 직접적 참여는 확인되지 않았다. 다만, LockBit 피해자는 전 세계 기관을 포함하고 있고, 한국이 2024년 [[budapest-convention]]에 가입함으로써 유사 작전을 위한 향후 협력 채널이 강화되었으므로, 본 작전은 한국의 사이버범죄 협력 프레임워크와 관련성을 가진다.

## 모순점 및 미해결 문제

- 폴란드 및 우크라이나에서의 국경 간 체포에 대해 구체적으로 어떤 법적 근거(조약 규정)가 원용되었는가?
- 작전일 이전 수사 단계의 정확한 범위와 시기는 무엇이었는가?
- 공개된 복호화 도구의 직접적 지원을 받은 피해자는 몇 명인가?
- Phase 1 프론트매터는 작전일(폴란드, 우크라이나)의 2명 체포만 기록하고 있으나, 어필리에이트별 식별(Vasiliev, Astamirov, Matveev, Sungatov, Kondratyev, Khoroshev)은 2022년부터 2024-05 제재까지 점진적으로 축적된 것이며; Phase 1 페이지는 "체포"를 의도적으로 2024-02-20 작전일에 한정하여 범위를 설정한다 — 누적 미국 기소 파이프라인은 [[operation-cronos-phase2]]를 참조하라.
- "미화 10억 달러 초과"라는 총 랜섬 수익 수치(FCDO 2024-05-07)는 *highly likely* DOJ의 체인 분석과 NCA의 인프라 접근을 결합한 집행 측 추정치이며; 정확한 방법론은 공개되지 않았다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2024-02-20: Law enforcement disrupt world's biggest ransomware operation - Operation Cronos (LockBit).
- Foreign, Commonwealth & Development Office, 2024-05-07: UK and Allies Sanction Prolific Cyber Hacker.
- US DOJ (District of New Jersey), 2024-07-18: Two Foreign Nationals Plead Guilty to Participation in LockBit Ransomware Group.
- DOJ NJ, 2024-07-22: LockBit case summary page.
- Europol, 2024-10-01: Operation Cronos Phase 3.
- National Crime Agency, 2024-12-04: Operation Destabilise: NCA disrupts multi-billion money laundering networks.
- Office of Financial Sanctions Implementation, 2026-01-28: Financial sanctions guidance for ransomware.

## Evidence and Attribution Notes

- Operation Cronos Phase 1은 2024년 2월 20일, 2022년 이래 전 세계적으로 가장 많이 배포된 랜섬웨어인 LockBit을 와해시켰다.
- 10개국이 12개 기관과 함께 참여하였으며, 영국 NCA가 주도하고 Europol 및 Eurojust가 조율하였다.
- 8개국에 걸쳐 34대 서버 압수, 2명 체포(폴란드, 우크라이나), 5건 기소, 200개 이상의 암호화폐 계정 동결.
- 150여 종의 랜섬웨어를 다루는 무료 복호화 도구가 No More Ransom 포털에 공개되었다.
- Europol은 27차례의 작전 회의와 4회의 기술 스프린트를 조직하였으며, 1,000건 이상의 SIENA 메시지가 교환되었다.
- 2024년 2월 20일, 10개국의 법집행기관이 **Operation Cronos**로 알려진 합동수사를 통해 LockBit 랜섬웨어 작전을 와해시켰으며, 본 합동수사는 영국 National Crime Agency가 주도하고 Europol과 Eurojust가 조율하였다.
- LockBit은 2019년 말 등장한 이래 2022년부터 전 세계적으로 가장 많이 배포된 랜섬웨어 변종이었다.
- 본 작전의 결과로 8개국에 걸쳐 34대 서버 압수, 2명 체포, 5건 기소, 200개 이상의 암호화폐 계정 동결, 14,000개의 비인가 계정 식별이 이루어졌다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- Foreign, Commonwealth & Development Office, 2024-05-07: Today's sanctions target Russian national Dmitry Khoroshev who has been identified, as part of an ongoing international law enforcement investigation, as one of the leaders of LockBit, the ransomware group responsible for extorting over $1 billion from thousands of victims globally.
- Foreign, Commonwealth & Development Office, 2024-05-07: In February the NCA announced that it had infiltrated the group's network and taken control of its services , compromising the entire criminal enterprise.
- DOJ NJ, 2024-07-22: 24-299 Case Summary : Defendants Matveev, Vasiliev, Astamirov, Sungatov, Kondratyev, and Khoroshev have been charged for their role in a conspiracy to deploy a ransomware variant known as "LockBit," a prolific form of malware and, at relevant times, the most deployed ransomware variant across the world.
- DOJ NJ, 2024-07-22: law, LockBit victims anywhere in the world are entitled to certain rights as a crime victim with respect to the ongoing LockBit prosecutions, including the right to claim restitution and/or to submit a victim impact statement to the Court for consideration at the sentencing of any LockBit defendant.
- National Crime Agency, 2024-12-04: Operation Destabilise: NCA disrupts $multi-billion Russian money laundering networks with links to, drugs, ransomware and espionage, resulting in 84 arrests - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show.
- Office of Financial Sanctions Implementation, 2026-01-28: Financial sanctions guidance for ransomware - GOV.UK Cookies on GOV.UK We use some essential cookies to make this website work.
- Office of Financial Sanctions Implementation, 2026-01-28: Cyber resilience and mitigating ransomware attacks Print this page © Crown copyright 2026 This publication is licensed under the terms of the Open Government Licence v3.0 except where otherwise stated.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본 작전 평가(Canonical Operation Assessment)

본 페이지는 LockBit 랜섬웨어 그룹에 대한 테이크다운을 기술하는 정본 작전으로 유지되며, 피고인 특정 후속 조치(defendant-specific follow-on action)가 아니다. 본 기록은 주도 책임을 Uk Nca에, 조율을 Europol Ec3에 귀속시키며, 참여 또는 영향을 받은 관할권은 프랑스, 독일, 네덜란드, 스웨덴, 호주, 캐나다, 일본, 영국, 미국, 스위스, 핀란드, 폴란드, 뉴질랜드, 우크라이나로 기록한다.

협력 모델은 명시된 기관 및 파트너를 통해 문서화된다: Uk Nca, Europol Ec3, Eurojust, France Gendarmerie, Germany Bka, Netherlands Politie, Sweden Police, Australia Afp, Canada Rcmp, Japan Npa; 집행 양태(enforcement posture): 체포(Arrest), 압수(Seizure), 테이크다운(Takedown), 기소(Indictment), 자산 동결(Asset Freeze).

정본 기록을 위해 포착된 작전 결과: 체포 2건; 기소 5건; 서버 압수 34대; 암호화폐/자산 결과는 200개 이상의 계정 동결로 기록; 14,000개 이상의 비인가 계정이 제거 대상으로 식별; No More Ransom 포털에 무료 복호화 도구 공개; 국제 체포영장 3건 발부.

정본 출처 세트는 7건의 참고문헌을 포함한다: 2024 02 20 Europol Operation Cronos Lockbit, 2024 05 07 Gov Uk Uk And Allies Sanction Prolific Cyber Hacker, 2024 07 18 Nj Lockbit Astamirov Vasiliev Pleas, 2024 07 22 Justice Gov Lockbit Case Summary Page, 2024 10 01 Europol Europa Eu Operation Cronos Phase 3, 2024 12 04 Nationalcrimeagency Gov Uk Operation Destabilise Nca Disrupts Multi Billion Money Laundering Networks, 외 1건.
출처 하한선(source floor)은 정본 작전 기준을 충족하지만, 출처의 폭(source breadth) 자체가 모든 하위(downstream) 체포 또는 양형이 본 작전의 일부임을 입증하지는 않는다; 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 안고 있는 알려진 메타데이터 갭: 법적 근거(Legal Basis) 및 활용 메커니즘(Mechanisms Used).
데이터셋 사용 시, 본 페이지는 작전 수준 집계점(operation-level aggregation point)으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조율된 집행 조치 전체를 기술한다. 이후의 기소, 답변(plea), 양형, 범죄인 인도, 자산몰수 조치는, 출처가 이를 새로운 다국적 작전으로 명시적으로 제시하지 않는 한, 관련 사건(related case)으로 첨부되거나 후속 기록(follow-on record)으로 흡수되어야 한다.
출처 기록이 더 광범위한 배경, 반복적 통신사 재게재(wire-service republications), 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명시된 작전, 그 참여 당국, 그 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과에 직접적으로 연결된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류(taxonomy) 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고(재현 가능한) 상태로 유지하기 위함이다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행처 | 날짜 | URL |
|---|---|---|---|---|
| [1] | Law enforcement disrupt world's biggest ransomware operation - Operation Cronos (LockBit) | Europol | 2024-02-20 | https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation |
| [2] | UK and Allies Sanction Prolific Cyber Hacker | Foreign, Commonwealth & Development Office | 2024-05-07 | https://www.gov.uk/government/news/uk-and-allies-sanction-prolific-cyber-hacker |
| [3] | Two Foreign Nationals Plead Guilty to Participation in LockBit Ransomware Group | US DOJ (District of New Jersey) | 2024-07-18 | https://www.justice.gov/usao-nj/pr/two-foreign-nationals-plead-guilty-participation-lockbit-ransomware-group |
| [4] | LockBit case summary page | DOJ NJ | 2024-07-22 | https://www.justice.gov/usao-nj/lockbit |
| [5] | Operation Cronos Phase 3 | Europol | 2024-10-01 | https://www.europol.europa.eu/media-press/newsroom/news/lockbit-power-cut-four-new-arrests-and-financial-sanctions-against-affiliates |
| [6] | Operation Destabilise: NCA disrupts multi-billion money laundering networks | National Crime Agency | 2024-12-04 | https://www.nationalcrimeagency.gov.uk/news/operation-destabilise-nca-disrupts-multi-billion-russian-money-laundering-networks-with-links-to-drugs-ransomware-and-espionage-resulting-in-84-arrests |
| [7] | Financial sanctions guidance for ransomware | Office of Financial Sanctions Implementation | 2026-01-28 | https://www.gov.uk/government/publications/financial-sanctions-guidance-for-ransomware/financial-sanctions-guidance-for-ransomware |
