## 개요

**2025년 12월 1일**, [[eurojust|Eurojust(유럽사법협력기구)]]는 [[germany|독일]]과 [[switzerland|스위스]] 당국이 Eurojust(유럽사법협력기구) 및 [[europol-ec3|Europol(유럽 경찰청)]]과 함께 마약 거래, 무기 거래, 온라인 사기 및 기타 사이버범죄 수익을 자금세탁하는 데 사용된 것으로 의심되는 암호화폐 믹서 서비스를 단속하였다고 발표하였다. 작전 주간 동안 **2,500만 유로 이상의 암호화폐가 압수되고 3개의 서버가 폐쇄**되었다.

Eurojust(유럽사법협력기구) 보도자료는 서비스명, 양국의 작전 주도 기관, 또는 체포 인원 수를 명명하지 않는다. 본 작전은 지속적인 EU-스위스 암호화폐 자금세탁 단속 패턴에 부합하지만, 입수 가능한 출처 세트는 본 작전을 공개적으로 명명된 캠페인과 연결하지 않는다.

> [!note] Unnamed operation
> 믹서 서비스와 작전 자체는 Eurojust(유럽사법협력기구) 보도자료에서 명명되지 않았다. 위키 슬러그 `de-ch-crypto-mixer-takedown-2025`는 단지 기술적 명칭일 뿐이다. 후속 보도에서 명칭이 드러날 경우 본 페이지는 개명되어야 한다.

## 배경

### 수법(모더스 오페란디) (the crime)

**Cryptomixer (cryptomixer.io)**는 **2016년부터 2025년 11월까지 지속적으로** 운영된 하이브리드 클리어웹 + 다크웹 비트코인 믹싱("텀블링") 서비스였다 — 이는 EU 법집행기관이 단속한 가장 오랫동안 운영된 믹서 중 하나로 자리매김한다. 본 서비스는 별개의 다수 범죄 고객으로부터 유입되는 BTC 예금을 풀링하고, 운영자가 통제하는 대규모 지갑 풀을 통해 믹싱하여 온체인 추적을 끊은 후, 고객이 선택한 목적지 주소로 정화된 BTC 출력을 재분배하였다. Cryptomixer는 **KYC/AML 통제 없이** 고객 결제를 수락하였으며, 믹스당 수수료 비율을 부과하였고(운영자가 보유한 마진이 범죄 수익화임), 블록체인 분석 클러스터링을 무력화하기 위해 고객이 구성 가능한 시간 지연 및 출력 분할 옵션을 제공하였다. 본 서비스는 클리어웹(`cryptomixer.io`)과 병행 Tor 히든 서비스 주소를 통해 모두 접근 가능하였다 — 이는 운영자에 대한 부인 가능성을 보존하면서 유입되는 고객 도달을 최대화하기 위한 하이브리드 자세였다.

### 피해자 프로파일 및 영향

믹서 자체는 1차 직접 피해자가 없다 — 그 피해는 **하류 가능화**적이다: 범죄 출처 BTC를 사전 범죄 가해자가 사용 가능한 BTC로 변환하는 자금세탁 병목 지점 기능을 한다. Europol(유럽 경찰청) 보도자료에 따르면, Cryptomixer를 사용한 고객 범죄자들은 다음과 같은 사전 범죄를 수행하였다:

- **랜섬웨어 결제** (명시적으로 명명됨 — Cryptomixer는 피해자가 지불한 BTC 몸값을 수령하는 랜섬웨어 운영자의 일상적 자금세탁 장소로 식별됨)
- **언더그라운드 경제 포럼** (카딩 시장, 자격증명 시장, 도난 데이터 재판매)
- **다크웹 마켓플레이스** (마약 거래, 무기 거래)
- **온라인 사기 / BEC** (비즈니스 이메일 손상 수익, 투자 사기, 로맨스 사기)
- **결제카드 사기** (도난 후 현금화 사이클)

따라서 2차 피해자 풀은 2016년에서 2025년 사이에 Cryptomixer를 통과한 지불 BTC를 가진 글로벌 랜섬웨어 피해자 및 사기 피해자 인구이다 — *highly likely* (≥80%) 관할권 전반에서 수만 명에 달할 것이나, 인용된 Europol(유럽 경찰청) 보도자료에는 피해자별 열거가 제공되지 않는다.

### 자금 흐름

Cryptomixer를 통한 평생 자금세탁 거래량: **13억 유로 이상의 비트코인**(2025년 11월 단속 시점 기준 Europol(유럽 경찰청) 귀속 수치). 3개의 스위스 서버에서 압수된 12TB 이상의 작전 데이터는 유입 예금 → 믹싱 풀 → 유출 정화 측 주소를 연결하는 거래 그래프를 포함하며, *highly likely* (≥80%) 하류 Cryptomixer 고객에 대한 진행 중인 후속 수사의 기본 증거 기반이 될 것이다. 작전 일자에 **2,500만 유로 상당의 비트코인**이 직접 압수되었다. AML Intelligence 보도에 따르면, 온체인 거래량 수치(약 15억 미국 달러)는 Cryptomixer를 **ChipMixer**(2023년 3월, 단속 시점 9,000만 유로 압수) 및 **Tornado Cash**(2022년 제재)와 같이 이전에 해체된 믹서와 동일한 거래량 등급에 위치시키지만, 사건당 압수 비율(2,500만 유로 / 13억 유로 = 약 1.9%)은 이미 세탁된 암호화폐를 회수하는 구조적 어려움을 반영한다.

### 범죄 조직 구조

인용된 Eurojust(유럽사법협력기구) 및 Europol(유럽 경찰청) 보도자료는 **Cryptomixer의 운영자 신원, 조직 인원 수, 또는 계층 구조를 열거하지 않는다**. 인프라 발자취 — 스위스 내 서버 3개, 클리어넷 도메인 1개, 12TB 이상의 작전 데이터 — 는 대규모 계층 OCG가 아닌 소규모-중간 규모 기술 운영자 팀(아마도 10명 미만의 핵심 운영자)과 일치한다. 스위스 서버 호스팅과 독일 검찰 연결은 운영자(들)가 두 관할권 중 어느 하나와 연계되었을 가능성을 시사하지만, 작전 일자에 체포는 발표되지 않았다. 인용된 보도자료에 따르면 단속 이후 **기소가 열거되지 않았다** — 모순점의 격차 노트 참조.

### 작전 지리(LE 측)

스위스의 글로벌 금융 허브 역할과 Zug에 위치한 이른바 "Crypto Valley"의 위치는 스위스를 암호화폐 자산 서비스 제공자에게 높은 관련성을 가진 호스트 또는 운영 관할권으로 만든다. 독일의 검찰 사이버범죄 인프라 — 특히 [[germany-frankfurt-prosecutor|ZIT(독일 사이버범죄 중앙청) Frankfurt]] — 는 암호화폐 단속에 있어 주요 대륙 유럽 중심지이다.

## 참여 당사자

| Country | Role |
|---------|------|
| [[germany]] | 공동 주도 집행; 공개 출처는 ZIT(독일 사이버범죄 중앙청) Frankfurt, BKA(독일 연방수사청), 또는 다른 독일 당국이 국내 구성요소를 주도했는지 식별하지 않음 |
| [[switzerland]] | 공동 주도 집행; 공개 출처는 fedpol 또는 다른 스위스 당국이 국내 구성요소를 주도했는지 식별하지 않음 |

| Coordinating Body | Role |
|-------------------|------|
| [[eurojust]] | DE-CH 양자 사법 협력을 포함한 사법 조율 |
| [[europol-ec3]] | 작전 및 분석 지원 |

> [!note] Source gap
> Eurojust(유럽사법협력기구) 보도자료는 어떤 독일 또는 스위스 기관이 각각의 국내 구성요소를 주도했는지 명시하지 않는다. 공개 기록은 자산 동결 및 서버 압수에 대한 스위스의 참여를 뒷받침하지만, 보다 세부적인 기관 귀속은 인용된 보도자료에서 입수할 수 없다.

## 법적 근거

- **[[budapest-convention|Budapest Convention(부다페스트 협약)]]**: 독일(2009년 당사국)과 스위스(2011년 당사국) 모두 당사국으로, 국경 간 보존, 수색 및 압수, 그리고 형사사법공조(MLA)에 대한 다자간 프레임워크를 제공한다.
- **국내 자금세탁 법률**: 독일 형법(StGB) §§ 261; 스위스 형법(StGB/CP) art. 305bis.

## 작전 타임라인

| Date | Event |
|------|-------|
| (2025년 이전) | 수사 개시; 구체적 시작일 비공개 |
| 2025년 작전 주간 | DE-CH 조율 하의 서버 3개 및 2,500만 유로 이상 암호화폐 압수 |
| 2025-12-01 | Eurojust(유럽사법협력기구), 보도자료를 통해 단속 발표 |

## 결과 및 영향

| Metric | Value |
|--------|-------|
| Cryptocurrency seized | **2,500만 유로** (이상) |
| Servers seized | **3** |
| Arrests | 비공개 |
| Indictments | 비공개 |

본 압수는 2025년에 공개된 EU-스위스 암호화폐 압수 중 더 큰 규모에 속하지만, 작전명과 체포 수의 부재는 [[cryptex-pm2btc-sanctions|Cryptex/PM2BTC]]와 같이 명명된 캠페인과의 비교 가능성을 제한한다.

## 활용된 협력 메커니즘

1. Eurojust(유럽사법협력기구) 조율을 통한 **DE-CH 양자 사법 협력**
2. **Europol(유럽 경찰청) 작전/분석 지원** — 인프라 및 금융 추적에 대한 분석 지원을 포함하며, 기술적 세부 사항은 공개되지 않음
3. **형사사법공조(MLA)** — 본 작전은 국경 간 서버 접근 및 자산 동결이 필요했기 때문에 MLA(형사사법공조)와 호환됨

## 도전 및 마찰 요인

- **암호화폐 자산 관할권 복잡성**: 믹싱 서비스는 일반적으로 여러 호스팅 제공자와 체인에 인프라를 분산시킨다.
- **스위스의 비-EU 지위**: 조율은 EU 도구 단독이 아닌 추가적인 양자 채널을 요구하였다.
- **정보 불투명성**: 보도자료는 서비스명, 체포 수, 그리고 스위스가 사용한 구체적 법적 근거를 생략하여 — 후속 교차 확인을 제한한다.

## 교훈

- Eurojust(유럽사법협력기구) 하의 DE-CH 양자 협력은 한 당사자(스위스)가 EU 외부에 있는 경우에도 상당한 암호화폐 압수를 달성할 수 있다.
- Eurojust(유럽사법협력기구)의 제3국 협력 협정은 일상적 국경 간 암호화폐 집행을 위한 절차적 척추를 제공한다.

## 한국의 참여

본 작전에서 [[south-korea|한국]]의 참여는 문서화되지 않았다. 한국 거래소(Upbit, Bithumb)와 한국 금융정보분석원(KoFIU)은 한국 거주 예금자에 대한 후속 정보를 위해 이러한 믹서 단속을 모니터링할 수 있다.

## 모순점 및 미해결 문제

- **믹싱 서비스의 명칭은 무엇인가?** Eurojust(유럽사법협력기구) 보도자료는 이를 식별하지 않는다; 후속 CoinDesk, AML Intelligence, TechRadar, heise 보도와 Europol(유럽 경찰청) 2025-11-26 보도자료는 서비스를 **Cryptomixer / cryptomixer.io**로, 작전 코드명을 **Operation Olympia**로 식별한다.
- **체포가 있었다면 몇 명이 체포되었는가?** 인용된 출처는 이를 비공개로 남긴다.
- **어떤 독일 검찰(ZIT(독일 사이버범죄 중앙청) Frankfurt? Land 검찰?)이 독일 구성요소를 주도하였는가?** 인용된 출처는 이를 비공개로 남긴다.
- **스위스가 사용한 법적 근거는 무엇이었는가?** 후보 법적 근거에는 Eurojust(유럽사법협력기구)-스위스 협력 협정과 스위스 형법 art. 305bis(자금세탁)가 포함되지만, 인용된 출처는 해당 도구를 확인하지 않는다.
- **본 작전은 보다 큰 캠페인(예: Operation Endgame, 제재 트랙)과 연결되어 있는가?** 출처에는 연결성이 명시되지 않는다.

**L26 Background gap notes** (인용된 tier-1 출처에서 누락된 범죄 실체):
- **Cryptomixer 운영자 신원 / OCG 인원 수 / 운영자 국적** — 체포가 열거되지 않았고, 운영자 신원은 인용된 Europol(유럽 경찰청) 및 Eurojust(유럽사법협력기구) 보도자료에서 비공개로 유지된다.
- **고객-범죄자 분할** — 13억 유로의 평생 자금세탁 풀에 대한 고객별 분할 분해(랜섬웨어 vs 다크넷 vs BEC vs 카딩)는 인용된 1차 출처에 제공되지 않는다.
- **피해자 수준 열거** — 2차 피해자 수(Cryptomixer를 통과한 지불 BTC를 가진 하류 랜섬웨어 및 사기 피해자)는 공개되지 않는다; 13억 유로 수치는 피해자가 아닌 범죄 고객 전반에 걸쳐 집계된 것이다.
- **수수료 구조 / 운영자 마진** — Cryptomixer의 믹스당 수수료 비율과 누적 운영자 수익(범죄 수익화)은 인용된 보도자료에 명시되지 않는다.


## 후속 조치

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전과 관련하여 공개적으로 접근 가능한 법원 문서가 확인되지 않았다. 가능한 사유: 공개 법원 기록 시스템이 없는 비-미국 관할권, 봉인된 절차, 또는 작전이 공식 기소로 이어지지 않은 경우 등이다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Eurojust, 2025-12-01: Cryptocurrency mixing service used to launder money taken down.
- CoinDesk, 2025-12-01: European authorities seize Bitcoin-mixing service Cryptomixer.
- AML Intelligence, 2025-12-01: EU takes down Cryptomixer, used to mix EUR 1.3bn in Bitcoin.
- TechRadar, 2025-12-02: Huge cryptomixer takedown sees feds seize over USD 30 million.
- heise online, 2025-12-01: Illegaler 'Cryptomixer' von Strafverfolgern zerschlagen.

## Evidence and Attribution Notes

- Germany and Switzerland, with Eurojust and Europol, took down a cryptocurrency mixing service used to launder proceeds from drug trafficking, weapons trafficking, online fraud and other cybercrimes (action published 1 December 2025)
- More than EUR 25 million in cryptocurrency seized during the action week
- Operation not publicly named in the Eurojust release; descriptive slug used in wiki
- CoinDesk reported that European authorities seized Cryptomixer infrastructure, including three servers and the domain.
- The article attributed the action to German and Swiss authorities with Europol and Eurojust support.
- CoinDesk reported that European authorities seized **Cryptomixer** infrastructure with German and Swiss participation.
- AML Intelligence identified the service as Cryptomixer and reported server, domain, and crypto seizures.
- The report linked the action to German and Swiss authorities with Eurojust and Europol.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against Unnamed cryptocurrency mixing service used to launder proceeds from drug trafficking, weapons trafficking, online fraud, and other cybercrimes, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Eurojust and coordination to Eurojust, with participating or affected jurisdictions recorded as Germany and Switzerland.

The cooperation model is documented through named agencies and partners: Eurojust and Europol Ec3; mechanisms: MLAT Process and Joint Investigation Team; legal basis: Budapest Convention and mutual legal assistance; enforcement posture: Seizure, Takedown, Asset Freeze.

Operational results captured for the canonical record: 3 servers seized; cryptocurrency/asset result recorded as EUR 25 million; 3 servers seized; Cryptocurrency mixing service infrastructure dismantled.

The canonical source set contains 5 reference(s): 2025 12 01 Eurojust De Ch Crypto Mixer Takedown, 2025 12 01 Coindesk Com Cryptomixer Takedown, 2025 12 01 Amlintelligence Com Cryptomixer Used To Mix 13bn In Bitcoin, 2025 12 02 Techradar Com Huge Cryptomixer Takedown Sees Feds Seize Over Usd30milion, 2025 12 01 Heise De Illegaler Cryptomixer Von Strafverfolgern Zerschlagen.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Operation Name, Service Name, Arrests, Indictments, Start Date, Specific Legal Basis For Switzerland.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 자금세탁에 사용된 암호화폐 믹싱 서비스 단속 | Eurojust | 2025-12-01 | https://www.eurojust.europa.eu/news/cryptocurrency-mixing-service-used-launder-money-taken-down |
| [2] | 유럽 당국, 비트코인 믹싱 서비스 Cryptomixer 압수 | CoinDesk | 2025-12-01 | https://www.coindesk.com/policy/2025/12/01/european-authorities-seize-usd1-51b-bitcoin-laundering-service-cryptomixer |
| [3] | EU, 13억 유로 비트코인 믹싱에 사용된 Cryptomixer 단속 | AML Intelligence | 2025-12-01 | https://www.amlintelligence.com/2025/12/latest-eu-takes-down-cryptomixer-used-to-mix-e1-3bn-in-bitcoin/ |
| [4] | 대규모 cryptomixer 단속, 연방수사관이 3,000만 미국 달러 이상 압수 | TechRadar | 2025-12-02 | https://www.techradar.com/pro/security/huge-cryptomixer-takedown-sees-feds-seize-over-usd30milion |
| [5] | 불법 'Cryptomixer'를 법집행기관이 분쇄 | heise online | 2025-12-01 | https://www.heise.de/news/Illegaler-Cryptomixer-von-Strafverfolgern-zerschlagen-11098583.html |
| [6] | [[2025-11-26_europol_cryptomixer-operation-olympia-takedown\|Europol과 파트너, 'Cryptomixer' 폐쇄 (Operation Olympia)]] | Europol | 2025-11-26 | https://www.europol.europa.eu/media-press/newsroom/news/europol-and-partners-shut-down-cryptomixer |
