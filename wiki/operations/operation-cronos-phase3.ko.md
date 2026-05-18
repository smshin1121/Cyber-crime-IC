## 개요

**Operation Cronos Phase 3**(크로노스 작전 3단계)는 **LockBit(랜섬웨어 그룹)**에 대한 국제 집행 캠페인의 세 번째 단계로, 2024년 10월 1일에 발표되었다. 본 단계의 결과로 프랑스, 영국, 스페인 전역에서 4명의 신규 체포가 이루어졌고, 스페인에서 9대의 서버가 압수되었으며, **Evil Corp**와 연계된 강력한 LockBit 어필리에이트에 대해 호주, 영국, 미국이 조율된 **금융 제재**를 부과하였다.

전통적인 형사 집행과 함께 금융 제재를 도입한 것은 *likely* 국제 랜섬웨어 전략의 진화를 나타내는 것으로, 통상적으로 국가안보 대응과 연관되어 온 경제적 압박 수단을 법집행 도구와 결합시킨 사례이다.

## 배경

### 수법(모더스 오페란디)

Phase 1 및 Phase 3와 연관된 Europol, NCA, gov.uk 보도자료에 따르면, LockBit은 약 2019년부터 랜섬웨어서비스형(RaaS) 플랫폼으로 운영되었다. 러시아 국적의 Dmitry Khoroshev(2024년 5월 "LockBitSupp"로 공개 식별됨)가 이끄는 코어 개발팀은 LockBit 암호화 바이너리(LockBit 2.0, LockBit 3.0/Black, LockBit Green을 포함한 버전), 어필리에이트 관리 패널, 그리고 이중 갈취 위협 게시에 사용되는 Tor 유출 사이트를 유지하였다. 어필리에이트는 수익 분배 방식(통상 어필리에이트가 70-80%, LockBit 운영자가 20-30%)으로 암호화기를 임차하였으며, 피싱, 공개 노출 서비스(Citrix Bleed, Fortinet, Confluence, Cisco ASA 취약점) 악용, 초기접근 브로커로부터의 접근 구매, 또는 내부자 모집을 통해 초기 네트워크 접근을 확보한 다음, 민감 데이터를 유출한 뒤 암호화기를 배포하였다. Phase 3는 특히 어필리에이트 생태계를 표적으로 삼았으며 — 스페인에 있는 어필리에이트 명령제어(C2)를 지원하는 방탄 호스팅(bulletproof-hosting) 인프라 포함 — Phase 1 이후의 포렌식 활용 과정에서 식별된 공유 어필리에이트를 통해, Dridex 뱅킹 악성코드 및 BitPaymer/WastedLocker 랜섬웨어의 배후로 알려진 장기적 러시아 사이버범죄 집단인 Evil Corp와의 작전상 연결고리를 밝혀냈다.

**피해자 프로파일 + 영향.** LockBit은 2022-2023년 가장 활발한 랜섬웨어 브랜드였으며, 2024년 5월 7일 영국 외교부(FCDO) 제재 성명에 따르면 전 세계적으로 2,500명 이상의 피해자를 주장하였고, 공개적으로 등재된 피해자에는 병원(토론토 Hospital for Sick Children, Royal Mail, NHS 공급망 제공자), 제조업, 금융 서비스, 교육, 그리고 120개국 이상에 걸친 정부 기관이 포함된다. FCDO 제재 패키지는 전 세계 피해자로부터 갈취한 총 수익을 "미화 10억 달러 초과"로 평가하였다. 주목할 만한 고영향 사건으로는 Royal Mail International에 대한 공격(2023년 초), Boeing에 대한 공격(2023년 10월), 영국 Royal Mail 물류 셧다운, 그리고 미국 재무부 시장 결제를 와해시킨 2023년 11월 ICBC 뉴욕 공격이 포함된다. Phase 3는 새로운 피해자 측 와해 지표를 발표하지 않았지만, Phase 1의 유출 사이트 인수 및 복호화 키 배포에 이어 어필리에이트 와해 압박을 확장하였다.

### 자금 흐름

LockBit 랜섬 지불은 비트코인으로 어필리에이트 통제 지갑으로 흘러갔으며, 수익 분배는 어필리에이트 패널을 통해 오프체인(off-chain)으로 실행되었다. Phase 3 제재 패키지를 지원하는 미국 재무부 OFAC 지정에 따르면, 랜섬 수익은 KYC가 취약한 암호화폐 거래소(이후 제재된 서비스 포함, 예: 2025년 2월에 표적이 된 Zservers 인프라), 믹서, 그리고 러시아 관할 거래소를 통한 법정화폐 전환을 통해 자금세탁되었다. 호주-영국-미국 3자 제재는 Evil Corp와 Phase 3에서 식별된 공유 LockBit 어필리에이트를 지원하는 금융 인프라를 표적으로 삼았으며, 자금세탁 및 출금 역할에 관여한 개인(영국 15명, 미국 6명, 호주 2명)을 명명하였다.

### 범죄 조직 구조

LockBit은 명확한 3계층 구조로 운영되었다: (1) **코어 개발자 / 운영자** — Khoroshev가 이끄는 소규모 러시아어권 팀으로 암호화기, 패널, 유출 사이트, 협상 채팅을 유지; (2) **어필리에이트** — 최정점 시 추정 100-200명의 활성 운영자가 실제 침입에서 암호화까지의 공격을 수행하였으며, RaaS 브랜드 간을 순환하면서도 LockBit 하에서 반복 활동; (3) **지원 역할** — 방탄 호스팅 운영자(Phase 3에서 스페인 관리자 1명 체포), 자금세탁자(제재된 Evil Corp 연계 네트워크), 그리고 네트워크 거점을 판매하는 초기접근 브로커. Phase 3에서 공개된 LockBit-Evil Corp 연결고리 — 두 생태계 모두에서 활동하는 단일 어필리에이트 — 는 RaaS 생태계가 개별 그룹으로 분할된 것이 아니라 공유 운영자를 통해 상호 연결되어 있음을 보여주었다.

Operation Cronos 누적 결과(Phase 1 + Phase 3):
- **총 6명 체포** (Phase 1에서 2명, Phase 3에서 4명)
- **총 43대 서버 압수** (Phase 1에서 34대, Phase 3에서 9대)

## 참여 당사자

### Coordinating Bodies
- [[europol-ec3|Europol(유럽 경찰청)]]
- [[eurojust|Eurojust(유럽사법협력기구)]]

### Participating Countries (12+)
호주, 캐나다, 프랑스, 독일, 일본, 네덜란드, 루마니아, 스페인, 스웨덴, 스위스, 영국, 미국

### Participating Agencies (14)
[[europol-ec3]], [[eurojust]], [[australia-afp|Australian Federal Police(호주 연방경찰)]], [[canada-rcmp|RCMP(캐나다 기마경찰)]], [[france-gendarmerie|French Gendarmerie (C3N, 프랑스 헌병대)]], [[germany-lka|German LKA(독일 주(州)수사청)]], [[germany-bka|German BKA(독일 연방수사청)]], [[japan-npa|Japanese NPA(일본 경찰청)]], [[spain-guardia-civil|Spanish Guardia Civil(스페인 민방위대)]], [[sweden-police|Swedish Police(스웨덴 경찰)]], [[switzerland-fedpol|Swiss Fedpol(스위스 연방경찰)]], [[netherlands-politie|Dutch National Police(네덜란드 국가경찰)]], [[uk-nca|UK NCA(영국 국가범죄청)]], [[fbi-cyber-division|FBI Newark(미국 연방수사국 뉴어크)]]

## 법적 근거

### Criminal Enforcement
- **프랑스:** 의심되는 LockBit 개발자 체포
- **영국:** 어필리에이트 활동을 지원한 2명 체포
- **스페인:** 방탄 호스팅 관리자 1명 체포; 9대 서버 압수

### Financial Sanctions
- **호주, 영국, 미국:** Evil Corp와 연계된 강력한 LockBit 어필리에이트에 대한 공동 제재
- **영국:** Evil Corp 연루 혐의로 러시아 시민 15명 제재
- **미국:** 시민 6명 제재
- **호주:** 시민 2명 제재

이러한 규모의 랜섬웨어 특정 집행 조치 맥락에서, 조율된 금융 제재의 사용은 *likely* 최초의 사례를 나타낸다.

## 결과 및 영향

| 지표 | 수치 |
|--------|-------|
| 신규 체포 | 4 |
| 압수 서버 | 9 (스페인) |
| 제재 부과 국가 | 3 (호주, 영국, 미국) |
| 제재된 러시아 시민(영국) | 15 |
| 제재된 시민(미국) | 6 |
| 제재된 시민(호주) | 2 |

### 체포 내역(Arrests Breakdown)
1. **프랑스:** LockBit 개발자 의심 인물 1명
2. **영국:** LockBit 어필리에이트 활동을 지원한 2명
3. **스페인:** 방탄 호스팅 관리자 1명

## 활용된 협력 메커니즘

- **Europol/Eurojust 조율:** Phase 1의 지속 태스크포스
- **금융 제재 조율:** 호주-영국-미국 3자 제재
- **인텔리전스 공유:** LockBit 어필리에이트와 Evil Corp 구성원 간의 교차 참조

## 교훈

1. **단계적 작전은 압박을 지속시킨다:** Phase 1과 Phase 3 사이의 8개월 간격은, 초기 테이크다운 이후 지속적인 수사가 추가 체포와 인텔리전스를 산출함을 보여준다.
2. **보완 수단으로서의 제재:** 금융 제재는 형사 기소를 넘어 집행 도구상자를 확장시키며, 특히 범죄인 인도가 실행 불가능한 관할권의 행위자에 대해 효과적이다.
3. **범죄 네트워크의 매핑:** 공유 어필리에이트를 통한 LockBit-Evil Corp 연결고리의 식별은, 원래 표적보다 더 광범위한 네트워크에 대한 제재를 가능하게 하였다.

## 후속 조치

> [!warning] No public court documents found
> (한국어 번역: 웹 검색(2026-04-17) 결과, 본 작전에 대한 공개 접근 가능한 법원 문서를 찾지 못하였다. 가능한 사유: 공개 법원 기록 시스템이 없는 비미국 관할권, 봉인된 절차, 또는 작전이 공식 기소로 이어지지 않았을 가능성.)


수사는 *likely* 진행 중이며, 압수된 인프라 및 체포된 개인으로부터 인텔리전스가 활용됨에 따라 추가 단계가 가능할 수 있다.

## 한국의 참여

Operation Cronos Phase 3에서 한국의 직접적 참여는 확인되지 않았다. 일본이 참여국에 포함되었으며, 이는 랜섬웨어 집행에 대한 동아시아의 광범위한 관여를 반영한다.

## 모순점 및 미해결 문제

- 제재의 근거가 된 구체적인 Evil Corp 활동은 무엇이었는가?
- 금융 제재는 표적이 된 개인의 작전을 와해시키는 데 얼마나 효과적이었는가?
- Phase 3를 넘어 추가 Cronos 단계가 계획되어 있는가?
- Phase 3 1차 출처는 Phase 3 특정 피해자 측 영향 지표(보호된 피해자 수, 방지된 랜섬 지불, 데이터 복구)를 공개하지 않는다; Phase 1 및 FCDO 제재 성명의 LockBit 브랜드 누적 피해자 수치만이 가용하다.
- 공유 LockBit-Evil Corp 어필리에이트의 신원("강력한 어필리에이트(prolific affiliate)"로 지정된 것을 넘어)은 공개적으로 가용한 Phase 3 출처에서 완전히 공개되어 있지 않다; OFAC 및 OFSI 제재 명단은 명시적으로 LockBit 연결고리에 각자를 귀속시키지 않은 채 기저 개인을 명명한다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2024-10-01: LockBit power cut: four new arrests and financial sanctions against affiliates - Operation Cronos Phase 3.
- Foreign, Commonwealth & Development Office, 2024-05-07: UK and Allies Sanction Prolific Cyber Hacker.
- Europol, 2024-02-20: Law enforcement disrupt world's biggest ransomware operation - Operation Cronos (LockBit).
- Office of Financial Sanctions Implementation, 2026-01-28: Financial sanctions guidance for ransomware.
- The Record, 2024-10-02: Operation Cronos phase 3 targets LockBit affiliates.

## 작전 타임라인

- 2024-10-01: 활동 또는 수사 시작.
- 2024-10-01: 공개 발표.
- 2024-10-01: 보고된 집행 종료 시점.
- 2024-02-20: Europol의 공개 출처 보도.
- 2024-05-07: Foreign, Commonwealth & Development Office의 공개 출처 보도.
- 2024-10-01: Europol의 공개 출처 보도.
- 2024-10-02: The Record의 공개 출처 보도.
- 2026-01-28: Office of Financial Sanctions Implementation의 공개 출처 보도.

## Evidence and Attribution Notes

- Operation Cronos Phase 3는 4명의 신규 체포로 이어졌다: 의심되는 LockBit 개발자(프랑스), 2명의 어필리에이트 지원자(영국), 1명의 방탄 호스팅 관리자(스페인).
- 호주, 영국, 미국은 Evil Corp와 연계된 강력한 LockBit 어필리에이트에 금융 제재를 부과하였다.
- 영국은 러시아 시민 15명을, 미국은 6명을, 호주는 2명을 Evil Corp 연루 혐의로 제재하였다.
- Operation Cronos 누적 체포 인원: 6명(Phase 1: 2, Phase 3: 4).
- 2024년 10월 1일, Europol은 LockBit 랜섬웨어 그룹을 표적으로 한 **Operation Cronos**의 세 번째 단계를 발표하였으며, 그 결과 4명의 신규 체포가 이루어졌다: LockBit 개발자 의심 인물(프랑스), 어필리에이트 활동을 지원한 2명(영국), 방탄 호스팅 관리자(스페인).
- 호주, 영국, 미국은 Evil Corp와 연계된 강력한 LockBit 어필리에이트에 금융 제재를 부과하였다. 영국은 Evil Corp 연루 혐의로 러시아 시민 15명을 제재하였고, 미국은 시민 6명을, 호주는 시민 2명을 제재하였다.
- 본 조치는 2024년 2월 초기 테이크다운을 토대로 하며, Europol과 Eurojust가 조율한 12개국 이상이 관여하였다.
- 영국, 미국, 호주는 LockBit의 고위 지도자로 식별된 Dmitry Khoroshev를 공동 제재하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- Foreign, Commonwealth & Development Office, 2024-05-07: Today's sanctions target Russian national Dmitry Khoroshev who has been identified, as part of an ongoing international law enforcement investigation, as one of the leaders of LockBit, the ransomware group responsible for extorting over $1 billion from thousands of victims globally.
- Foreign, Commonwealth & Development Office, 2024-05-07: In February the NCA announced that it had infiltrated the group's network and taken control of its services , compromising the entire criminal enterprise.
- Office of Financial Sanctions Implementation, 2026-01-28: Financial sanctions guidance for ransomware - GOV.UK Cookies on GOV.UK We use some essential cookies to make this website work.
- Office of Financial Sanctions Implementation, 2026-01-28: Cyber resilience and mitigating ransomware attacks Print this page © Crown copyright 2026 This publication is licensed under the terms of the Open Government Licence v3.0 except where otherwise stated.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본 작전 평가(Canonical Operation Assessment)

본 페이지는 LockBit 랜섬웨어 그룹 어필리에이트 및 Evil Corp에 대한 일제 체포 작전(arrest-sweep)을 기술하는 정본 작전으로 유지되며, 피고인 특정 후속 조치(defendant-specific follow-on action)가 아니다. 본 기록은 주도 책임을 Europol Ec3에, 조율을 Europol Ec3에 귀속시키며, 참여 또는 영향을 받은 관할권은 호주, 캐나다, 프랑스, 독일, 일본, 네덜란드, 루마니아, 스페인, 스웨덴, 스위스, 영국, 미국으로 기록한다.

협력 모델은 명시된 기관 및 파트너를 통해 문서화된다: Europol Ec3, Eurojust, Australia Afp, Canada Rcmp, France Gendarmerie, Germany Lka, Germany Bka, Japan Npa, Spain Guardia Civil, Sweden Police; 집행 양태(enforcement posture): 체포(Arrest), 압수(Seizure), 자산 동결(Asset Freeze).

정본 기록을 위해 포착된 작전 결과: 체포 4건; 서버 압수 9대; 호주, 영국, 미국에 의한 Evil Corp 어필리에이트에 대한 금융 제재 부과; 영국은 Evil Corp 연루 혐의로 러시아 시민 15명 제재; 미국은 시민 6명 제재; 호주는 시민 2명 제재.

정본 출처 세트는 5건의 참고문헌을 포함한다: 2024 10 01 Europol Operation Cronos Lockbit Phase3, 2024 05 07 Gov Uk Uk And Allies Sanction Prolific Cyber Hacker, 2024 02 20 Europol Operation Cronos Lockbit, 2026 01 28 Gov Uk Financial Sanctions Guidance For Ransomware, 2024 10 02 Therecord Media Operation Cronos Phase 3 Lockbit.
출처 하한선(source floor)은 정본 작전 기준을 충족하지만, 출처의 폭(source breadth) 자체가 모든 하위(downstream) 체포 또는 양형이 본 작전의 일부임을 입증하지는 않는다; 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 안고 있는 알려진 메타데이터 갭: 법적 근거(Legal Basis) 및 활용 메커니즘(Mechanisms Used).
데이터셋 사용 시, 본 페이지는 작전 수준 집계점(operation-level aggregation point)으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조율된 집행 조치 전체를 기술한다. 이후의 기소, 답변(plea), 양형, 범죄인 인도, 자산몰수 조치는, 출처가 이를 새로운 다국적 작전으로 명시적으로 제시하지 않는 한, 관련 사건(related case)으로 첨부되거나 후속 기록(follow-on record)으로 흡수되어야 한다.
출처 기록이 더 광범위한 배경, 반복적 통신사 재게재(wire-service republications), 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명시된 작전, 그 참여 당국, 그 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과에 직접적으로 연결된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류(taxonomy) 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고(재현 가능한) 상태로 유지하기 위함이다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행처 | 날짜 | URL |
|---|---|---|---|---|
| [1] | LockBit power cut: four new arrests and financial sanctions against affiliates - Operation Cronos Phase 3 | Europol | 2024-10-01 | https://www.europol.europa.eu/media-press/newsroom/news/lockbit-power-cut-four-new-arrests-and-financial-sanctions-against-affiliates |
| [2] | UK and Allies Sanction Prolific Cyber Hacker | Foreign, Commonwealth & Development Office | 2024-05-07 | https://www.gov.uk/government/news/uk-and-allies-sanction-prolific-cyber-hacker |
| [3] | Law enforcement disrupt world's biggest ransomware operation - Operation Cronos (LockBit) | Europol | 2024-02-20 | https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation |
| [4] | Financial sanctions guidance for ransomware | Office of Financial Sanctions Implementation | 2026-01-28 | https://www.gov.uk/government/publications/financial-sanctions-guidance-for-ransomware/financial-sanctions-guidance-for-ransomware |
| [5] | Operation Cronos phase 3 targets LockBit affiliates | The Record | 2024-10-02 | https://therecord.media/operation-cronos-phase-3-lockbit |
