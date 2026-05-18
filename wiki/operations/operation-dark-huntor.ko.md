## 개요

Operation Dark HunTOR(다크 헌터 작전)은 2021년 10월 26일 발표된 국제 합동 법집행 조치로서, 9개국에 걸쳐 다크웹 마약 거래 용의자 150명을 체포한 결과를 가져왔다. 본 작전을 통해 현금 및 암호화폐 약 2,670만 유로(약 3,100만 미국 달러), 마약 234kg, 총기 45정이 압수되었다. [[europol-ec3|Europol(유럽 경찰청) 유럽사이버범죄센터(EC3)]]와 [[eurojust|Eurojust(유럽사법협력기구)]]가 공동 조율한 Dark HunTOR는 단일 다크웹 시장 압수에서 비롯된 후속 법집행 조치 중 공개적으로 문서화된 최대 규모의 사례이며, 2021년 1월에 단행된 [[darkmarket-takedown|DarkMarket]] 테이크다운을 직접적으로 기반으로 한다.

본 작전은 다크웹 법집행의 "연쇄(cascade)" 모델, 즉 시장 인프라 압수, 판매자에 대한 정보 추출, 그리고 복수 관할 구역에서의 동시 체포 작전 조율을 입증하였다.

## 배경

### Modus operandi — the dark-web vendor sales model

Operation Dark HunTOR가 표적으로 삼은 범죄 활동은 Tor 히든 서비스("다크웹") 시장을 통해 **규제 약물, 총기, 사기 도구 및 위조 물품을 상업적으로 판매하고 이를 암호화폐로 거래**하는 행위였다. DarkMarket과 이와 병행하여 이탈리아 당국에 의해 압수된 DeepSea 및 Berlusconi 시장 전반에 걸쳐 공통적으로 나타난 지배적인 운영 패턴은 다음과 같이 구성되었다.

1. **판매자 온보딩** — 시장 운영자(통상 거래 건당 2~5%의 수수료를 부과)는 판매자 신청 관문을 유지하였고, 판매자는 비트코인으로 보증금을 납부하고, PGP 키를 설정하며, 제품 카테고리를 등록하였다(판매자 기반에는 암페타민, 오피오이드, MDMA, 코카인, 메스암페타민, 처방약, 엑스터시 정제, 총기, 현금 위조 키트, 탈취 자격증명 덤프 등이 포함되었다).
2. **에스크로를 통한 구매자-판매자 매칭** — 구매자(Tor 경유, 비트코인 또는 모네로로 결제)는 등록 상품을 주문하였고, 시장이 보유한 에스크로가 구매자의 배송 확인 시점까지 결제 금액을 보관하였다. 분쟁은 시장 운영진에 의해 중재되었다.
3. **우편 서비스를 통한 물리적 배송** — 주문은 진공 밀봉 은닉 및 미끼 충전재를 사용하여 각국 우편 서비스(USPS, Deutsche Post, Royal Mail, Australia Post)를 통해 배송되었으며, 판매자는 시장 자체에서 운영 기술 도구(은닉 우편 튜토리얼, 미끼 발송 등)를 구매하였다.
4. **암호화폐 현금화** — 판매자 수익은 시장 지갑에서 인출되어 믹서/텀블러(예: Wasabi Wallet, Helix 방식 믹서), P2P 거래소 및 OTC 데스크를 통해 자금세탁된 후 규제 준수 거래소에서 법정화폐로 환전되었다. DarkMarket 플랫폼 한 곳에서만 압수 시점 기준으로 **32만 건 이상의 거래**와 **총 1억 4,000만 유로 이상의 암호화폐 거래량**이 처리되었다.

### 피해자 프로파일 및 영향

"피해자" 집단은 전형적인 사이버범죄 사건보다 더 분산되어 있다. 마약의 최종 구매자는 도착지 국가의 마약법상 가해자이면서도, 동시에 변질된 제품, 과다 복용 및 중독 결과로 인한 피해를 입는다. Operation Dark HunTOR 기간 동안 압수된 25,000정 이상의 엑스터시, 152kg의 암페타민, 27kg의 오피오이드 및 45정의 총기는 그러한 제품을 받게 되었을 최종 사용자에 대한 피해의 *예방*을 의미한다. 영국 NCA(국가범죄청)의 설명은 공중보건 차원을 강조하였다. 즉, 다크웹에서 조달된 오피오이드(불법 제조된 펜타닐 유사체)는 효능이 일정하지 않으며, 참여 관할 구역 다수, 특히 미국에서 초과 과다 복용 사망을 견인하였다. 소비자 피해를 넘어 피해자에는 합법적 우편 시스템 이용자(차단 검사 부담 및 압수 지연에 노출)와 후속 금융 시스템 이용자(다크웹 마약 판매자들이 암호화폐 경로를 통해 밀어붙이는 세탁 처리량에 노출)도 포함된다.

### 자금 흐름

본 작전이 차단한 두 가지 자금 흐름은 다음과 같다.

- **구매자 → 시장**: DarkMarket 처리량 약 1억 4,000만 유로(BTC 우세, 모네로 상승세). 최종적으로 Dark HunTOR 표적 9개국의 최종 구매자들은 시장 통제 입금 주소로 비트코인을 송금하였고, 그 온체인 출처는 이후 Europol의 EC3 분석 허브에 의해 추적되었다.
- **시장/판매자 현금화**: 시장 입금 주소에서 1회 이상의 믹싱/텀블링 라운드를 거쳐 P2P 거래소 또는 KYC가 약한 규제 준수 거래소로 이동하였다. Dark HunTOR 작전 일자 중 압수된 **2,670만 유로(3,100만 미국 달러)**는 판매자 체포 시점의 운영 현금 및 보유 암호화폐, 즉 판매자의 운영 잔액 및 최근 수익을 의미하며, 누적 평생 수익을 의미하지 않는다. 압수 대상 판매자 집단 전체의 누적 세탁 수익은 2,670만 유로 수치를 상당히 초과한다.

### 범죄 조직 구조

표적 집단은 위계적이라기보다 분산적이었다. **9개국에 걸친 150명의 체포자**는 주로 DarkMarket(및 이탈리아 당국에 의해 병행 압수된 DeepSea 및 Berlusconi 시장)에서 자체 등록 상품을 운영하는 **독립적인 판매자**로 기능하였다. 판매자는 통상 1~3인 규모의 팀(조달 → 포장 → 배송 → 암호화폐 현금화)으로 운영되었으며, 시장 순위를 두고 판매자 간 경쟁이 존재하였다. 일부 대형 판매자는 평판을 복수의 물리적 운영자 사이에서 분산하기 위해 "브랜드" 가명을 공유하는 다수의 판매자로 구성된 소규모 네트워크 형태로 운영되었다. 시장 관리자(특히 2021년 1월 DarkMarket 운영자로 지목되어 독일-덴마크 국경에서 체포된 **34세 호주 국적자**)는 정점 계층을 대표하였다. 이탈리아 당국에 의해 병행 체포된 DeepSea 및 Berlusconi 관리자는 각 플랫폼에 대해 이에 상응하는 정점 계층 인물들이었다. Dark HunTOR의 구조적 혁신은 바로 시장 정점이 먼저 압수되고(2021년 1월) 그 정점 계층 데이터를 활용하여 분산된 판매자 집단이 열거되었다는 점에 있으며, 이는 각 판매자를 독립적으로 추적하는 대신 "참수 후 일소(decapitation-then-sweep)" 작업 흐름을 이룬다.

### DarkMarket Takedown (January 2021)

2021년 1월 11일, 독일 당국(인터넷범죄대응중앙부 ZIT 및 [[germany-bka|BKA]])은 당시 세계 최대 불법 다크웹 시장이었던 DarkMarket을 폐쇄하였고, 그 운영자로 추정되는 호주 국적자를 독일-덴마크 국경 인근에서 체포하였다. 폐쇄 시점에 DarkMarket은 약 50만 명의 사용자, 2,400명 이상의 판매자를 보유하였으며, 최소 32만 건의 거래(암호화폐 기준 1억 4,000만 유로 이상 가치)를 중개하였다. 결정적으로, 독일 당국은 몰도바와 우크라이나에 위치한 시장 서버를 압수하였고, 해당 서버에는 판매자, 구매자 및 거래 기록에 관한 광범위한 데이터가 보관되어 있었다.

### Intelligence Exploitation

DarkMarket 압수 이후, [[europol-ec3|Europol EC3]]는 약 10개월에 걸쳐 압수된 인프라로부터 정보 패키지를 편집하여 고가치 표적, 즉 시장을 통해 마약 및 기타 불법 물품을 적극적으로 거래해 온 판매자를 식별하였다. 이 정보는 헤이그 소재 Europol 본부에서 운영되는 합동 사이버범죄 대응 태스크포스(J-CAT)를 통해 참여 기관들과 공유되었다.

### JCODE Partnership

미국 측에서는 [[us-doj|미국 법무부]] 산하 다부처 이니셔티브로서 다크넷에서의 오피오이드 거래 차단에 중점을 둔 합동범죄오피오이드및다크넷집행(Joint Criminal Opioid and Darknet Enforcement, JCODE) 팀이 작전을 주도하였다. JCODE는 FBI, DEA, HSI, USPIS, IRS-CI를 통합하였다.

## 참여 당사자

### Coordinating Bodies

| Body | Role |
|---|---|
| [[europol-ec3]] | 정보 분석, J-CAT 조율, 작전 허브 |
| [[eurojust]] | EU 회원국 간 사법 조율 |

### Participating Countries and Agencies

| Country | Arrests | Key Agencies |
|---|---|---|
| [[united-states]] | 65 | FBI(미국 연방수사국), DEA(미국 마약단속국), HSI, USPIS, IRS-CI (JCODE 경유) |
| [[germany]] | 47 | BKA, ZIT, 주 경찰 기관 |
| [[united-kingdom]] | 24 | [[uk-nca]], NPCC |
| [[italy]] | 4 | Brescia 검찰청, Guardia di Finanza |
| [[netherlands]] | 4 | [[netherlands-politie]] |
| [[france]] | 3 | 국립경찰, 국립헌병대, 관세청 |
| [[switzerland]] | 2 | Zurich 칸톤 경찰 |
| [[bulgaria]] | 1 | 조직범죄대응총국 |
| [[australia]] | 0 | 호주 연방경찰(AFP) — 정보 지원 |

### Policy Framework

본 작전은 EU 안보 우선순위에 대한 전략적 틀을 제공하고 EU 회원국과 제3국 간의 구조화된 협력을 가능하게 하는 유럽 범죄위협 다학제 플랫폼(European Multidisciplinary Platform Against Criminal Threats, EMPACT) 내에서 수행되었다.

## 법적 근거

본 작전은 복수의 법적 수단에 의존하였다.

1. **[[budapest-convention|부다페스트 사이버범죄 협약]]** (제29-35조): 유럽 측 당사국과 미국 간의 국경 간 증거 보전 및 제출 요청의 토대를 제공하였다.
2. **EMPACT**: 다크웹 범죄를 집단적 법집행 표적으로 우선순위화할 권한을 부여한 EU 정책 틀.
3. **양자 MLAT**: 미국(JCODE 경유)과 유럽 측 상대 기관 간 증거 공유는 부다페스트 협약 틀과 함께 가용한 양자 [[mlat-process|형사사법공조조약(MLAT)]] 채널을 활용하였다.
4. **Eurojust 조율**: 복수의 EU 관할 구역에서의 동시 집행 조치에 대한 사법 권한 부여를 촉진하였다.

> [!note] Legal basis detail
> 각 양자 증거 교환에 사용된 정확한 법적 수단은 공개되지 않았다. 위의 평가는 EU-미국 법집행 협력에 활용 가능한 표준적인 법적 틀에 기반한 것이다.

## 작전 타임라인

| Date | Event |
|---|---|
| 2021-01-11 | 독일 당국에 의한 DarkMarket 테이크다운, 운영자 체포, 몰도바 및 우크라이나 소재 서버 압수 |
| 2021-01 ~ 2021-10 | Europol EC3가 압수된 DarkMarket 인프라로부터 정보 패키지 편집, J-CAT를 통한 표적 식별 |
| 2021-10 (정확한 일자 미공개) | 9개국에 걸친 동시 체포 작전 수행 |
| 2021-10-26 | Europol, DOJ 및 참여 기관들이 Operation Dark HunTOR의 결과를 공식 발표 |
| 2021-10-26 | Lisa Monaco 법무부 차관이 기자회견에서 발언, 이탈리아 당국이 DeepSea 및 Berlusconi 시장 압수를 발표 |
| 2021-10-27 | [[uk-nca|영국 NCA]]가 영국 측 결과 발표: 24명 체포, 22만 파운드 이상의 현금/비트코인, 50kg 이상의 마약 |

## 결과 및 영향

### Quantitative Results

| Metric | Amount |
|---|---|
| 체포 | 9개국에 걸쳐 150명 |
| 현금 및 암호화폐 압수 | 2,670만 유로(약 3,100만 미국 달러) |
| 마약 압수 | 총 234kg |
| -- 암페타민 | 152kg |
| -- 오피오이드 | 27kg |
| -- 엑스터시 정제 | 25,000정 이상 |
| -- 코카인 | 약 21.6kg |
| -- MDMA | 약 32.5kg |
| 총기 압수 | 45정 |

### Concurrent Italian Operations

이탈리아 당국은 Dark HunTOR 우산 아래 병행하여 두 개의 추가 다크웹 시장을 폐쇄하였다.
- **DeepSea 시장**: 압수, 관리자 체포
- **Berlusconi 시장**: 압수, 관리자 체포
- 이 두 플랫폼에서 압수된 암호화폐 총액: 360만 유로

### Strategic Impact

Operation Dark HunTOR는 다크웹 법집행에 있어 전략적으로 중요한 세 가지 패턴을 입증하였다.

1. **후속 수사 모델**: 본 작전은 시장 인프라 압수가 초기 테이크다운을 훨씬 넘어 지속적인 법집행 조치를 위한 정보를 산출한다는 것을 입증하였다. DarkMarket 압수와 Dark HunTOR 체포 사이의 10개월 간격은 압수된 데이터의 체계적 활용과 일치한다.

2. **억제 메시지**: Monaco 법무부 차관은 본 작전이 "다크웹에서 불법 물품을 판매하거나 구매하는 모든 자에게 분명한 메시지를 보낸다. 즉, 국제 법집행 공동체는 당신을 추적할 수단과 의지를 모두 가지고 있다"는 메시지를 보냈다고 언급하였다(DOJ, 2021-10-26).

3. **EU-미국 운영 가교**: 본 작전은 EU 중심의 EMPACT 틀과 미국 중심의 JCODE 이니셔티브를 J-CAT를 조율 계층으로 활용하여 성공적으로 연결하였다.

## 활용된 협력 메커니즘

| Mechanism | Role in Operation |
|---|---|
| J-CAT (합동 사이버범죄 대응 태스크포스) | Europol 본부의 주요 조율 계층, 정보 패키지 배포 |
| EMPACT | 집단적 법집행 우선순위를 승인하는 EU 정책 틀 |
| JCODE | 미국 다부처 다크넷 법집행 팀, 미국 측 체포 주도 |
| [[eurojust]] 조율 회의 | 동시적 EU 체포 작전에 대한 사법 권한 부여 |
| Europol 작전 분석 | EC3가 압수된 DarkMarket 서버로부터 정보를 편집 |

## 도전 및 마찰 요인

1. **관할 복잡성**: 9개국에 판매자가 분산되어 있어 각 체포에는 국내 법적 권한 부여가 필요하였고, 이로 인해 시점 동기화와 관련된 조율 문제가 발생하였다.
2. **데이터 주권**: 압수된 서버가 몰도바 및 우크라이나(EU 비회원국)에 위치하여 해당 서버에서 획득한 증거의 EU 법원 내 증거능력에 관한 잠재적 법적 문제가 제기되었다.
3. **암호화폐 추적**: 압수된 2,670만 유로의 암포화폐는 복수의 거래소 및 지갑 유형에 걸친 포렌식 블록체인 분석을 필요로 하였다.

## 교훈

1. **인프라 압수가 연쇄 법집행을 가능하게 함**: DarkMarket에서 Dark HunTOR로 이어진 파이프라인은 압수된 데이터가 체계적으로 활용되는 경우, 단일 시장 테이크다운이 9개국에서 150명 이상의 체포를 위한 정보를 생성할 수 있음을 입증하였다.

2. **대서양 횡단 조율 모델로서의 J-CAT**: Europol의 합동 사이버범죄 대응 태스크포스는 EU 법집행과 미국 JCODE 사이의 중립적 조율 계층으로서, 상이한 법적 전통과 운영 문화를 가교하는 데 효과적임이 입증되었다.

3. **병렬 시장 압수가 영향을 증폭시킴**: Dark HunTOR 우산 아래에서 이탈리아가 DeepSea 및 Berlusconi 시장을 동시 테이크다운한 것은 조율된 다중 표적 작전이 다크웹 생태계의 교란을 증폭시킨다는 것을 입증하였다.

4. **시차를 둔 법집행이 실행 가능함**: DarkMarket 압수와 Dark HunTOR 체포 사이의 10개월 간격은, 인내심 있는 정보 활용이 즉각적인 체포 작전보다 더 생산적일 수 있음을 보여준다.

## 한국의 참여

Operation Dark HunTOR에 대한 한국의 참여를 입증하는 공개 자료는 없다. 본 작전의 범위는 9개국(미국, 독일, 영국, 이탈리아, 네덜란드, 프랑스, 스위스, 불가리아, 호주)에 한정되었으며, 이들은 모두 EU 회원국, 파이브 아이즈(Five Eyes) 파트너 또는 Europol과의 협력이 정립된 파트너국이다.

다만, 본 작전의 후속 수사 모델은 한국의 법집행 실무와 관련성이 있다. 한국 경찰청과 한국인터넷진흥원(KISA)은 [[interpol-igci|INTERPOL(국제형사경찰기구) IGCI]] 채널을 통해 유사한 다크웹 법집행 작전에 참여한 바 있으며, 특히 CSAM 및 마약 거래 수사 맥락에서 그러하다. Dark HunTOR가 보여준 연쇄 정보 모델은 향후 한국이 참여하는 INTERPOL 조율 작전에 적용될 수 있다.

## 모순점 및 미해결 문제

1. **체포자 수 불일치**: 일부 초기 언론 보도는 "150명 이상"의 체포를 인용한 반면, Europol 및 DOJ의 공식 발표는 일관되게 정확히 150명을 명시하였다. NCA의 영국 측 보도자료는 영국 내 24명 체포를 명시하고 있으며, 이는 Europol의 총계와 일치한다. 이는 실질적 모순이 아니라 언론 보도에서의 반올림 문제이다.

2. **DarkMarket 운영자 국적**: 2021년 1월에 체포된 DarkMarket 운영자는 일부 자료에서 "호주 국적자"로 묘사되었으나, 그의 신원, 혐의 및 독일에서의 법적 절차에 대한 세부 사항은 제한적이었다. 본 코퍼스에서 이용 가능한 공개 자료는 2021년 10월 기준 그의 기소 상태를 해소하지 못한다.

3. **MLAT 대 비공식 채널**: EU 국가와 미국 간 증거 공유에 있어 형사사법공조조약(MLAT)에 의한 공식 요청이 사용된 정도와 J-CAT를 통한 경찰 간 비공식 채널이 사용된 정도는 공개적으로 상세히 알려져 있지 않다.

4. **장기 기소 결과**: 150명의 체포는 2021년 10월에 발표되었으나, 이들 체포로부터 비롯된 유죄 판결 비율 및 양형은 가용한 자료 기준으로 종합적으로 보고되지 않았다.

5. **L26 gap note — per-vendor cumulative laundering totals**: 압수된 2,670만 유로 수치는 150명의 판매자 집단 전체에 대한 *체포 시점의 운영 잔액*이며, 평생 세탁 수익이 아니다. 인용된 자료는 판매자별 누적 암호화폐 거래량, 압수 이전에 세탁된 수익의 비율, 또는 OTC 데스크 대 믹서 대 P2P 거래를 통해 합법 금융 시스템에 재진입한 수익의 비율을 열거하고 있지 않다.

6. **L26 gap note — buyer-side prosecutions**: Operation Dark HunTOR의 기소 대상 집단은 DarkMarket의 **판매자**(매도자)로 구성되었다. 인용된 자료는 최종 구매자에 대한 구매자 측 법집행 조치, 즉 DarkMarket 구매자 데이터가 9개 참여 관할 구역 중 어느 곳에서 최종 구매자 기소에 사용되었는지, 또는 구매자 기반이 의도적으로 우선순위에서 배제되었는지를 열거하고 있지 않다.

7. **L26 gap note — DeepSea / Berlusconi vendor cohort**: 이탈리아 당국에 의한 DeepSea 및 Berlusconi 시장의 병행 압수(관리자 체포, 360만 유로 암호화폐 압수)는 인용 자료에서 부수적으로 언급되어 있으나, 이 두 플랫폼의 판매자 집단 및 피해자 영향 데이터는 별도로 열거되어 있지 않다.

> [!note] Source diversity
> 본 페이지는 주로 Europol(2021-10-26), DOJ/DEA(2021-10-26), NCA(2021-10-27)의 공식 보도자료에 기반하며, BleepingComputer 및 SecurityAffairs의 2차 보도가 보충되었다. 추가적인 1차 자료(예: 이탈리아 사법부 진술, 독일 BKA 보도자료)는 본 페이지를 강화할 것이다.

## 후속 조치

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전에 대해 공개적으로 접근 가능한
> 법원 제출 자료는 발견되지 않았다. 가능한 사유: 공개 법원 기록
> 체계가 없는 비미국 관할 구역, 봉인된 절차, 또는 본 작전이
> 공식 기소로 이어지지 않았을 가능성.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2021-10-26: 150 arrested in dark web drug bust as police seize EUR 26 million.
- US DOJ/DEA, 2021-10-26: Department of Justice Announces Results of Operation Dark HunTor.
- US DOJ, 2021-10-26: Deputy Attorney General Lisa O. Monaco Delivers Remarks on Operation Dark HunTor.
- UK NCA, 2021-10-27: International operation targets dark web drugs marketplace.
- Europol, 2021-01-12: DarkMarket: world's largest illegal dark web marketplace taken down.

## Evidence and Attribution Notes

- Operation Dark HunTOR는 2021년 10월 26일에 발표된 국제 합동 법집행 조치로서, 9개국에 걸쳐 다크웹 마약 거래 용의자 150명의 체포라는 결과를 가져왔다.
- 본 작전을 통해 현금 및 암호화폐 약 2,670만 유로(약 3,100만 미국 달러), 마약 234kg, 총기 45정이 압수되었다.
- Europol의 유럽사이버범죄센터(EC3)와 Eurojust가 공동 조율한 Dark HunTOR는 단일 다크웹 시장 압수에서 비롯된 후속 법집행 조치 중 공개적으로 문서화된 최대 규모의 사례이며, 2021년 1월의 DarkMarket 테이크다운을 직접적으로 기반으로 한다.
- DarkMarket은 2021년 1월 11일 폐쇄 시점에 사용자 수 기준 세계 최대의 불법 다크넷 시장이었다.
- 본 테이크다운은 Koblenz 검찰청의 사이버범죄 부서와 독일 연방수사청(BKA)이 주도하였고, Europol의 유럽사이버범죄센터(EC3)를 통해 조율되었다.
- 본 작전은 독일-덴마크 국경 인근에서 34세 호주 국적자의 체포, 몰도바 및 우크라이나 소재 20대 이상의 서버 압수, 그리고 약 50만 명의 사용자와 2,400명의 판매자에 관한 정보 회수를 가져왔다.
- DarkMarket 인프라로부터 수집된 정보는 9개월 후의 Operation Dark HunTOR를 직접적으로 가능하게 하였고, 이는 9개국에 걸쳐 150명의 체포라는 결과를 산출하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US DOJ, 2021-10-26: Monaco Delivers Remarks On Operation Dark HunTor This is archived content from the U.S.
- US DOJ, 2021-10-26: I am pleased to be joined this morning by the Deputy Executive Director of EUROPOL, Jean-Philippe Lecouff, as well as the Assistant Attorney General of the Criminal Division Kenneth Polite Jr., FBI Deputy Director Paul Abbate, DEA Administrator Anne Milgram, and leaders of several law enforcement partners.
- UK NCA, 2021-10-27: International operation targets dark web drugs marketplace - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show submenu for Who we are Our mission Our people Our leadership Governance and transparency Inclusion.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라 DarkMarket 판매자 및 다크웹 마약 거래자에 대한 체포 일소(arrest-sweep)를 기술하므로 정본 작전으로 유지된다. 본 기록은 주도 책임을 Europol EC3에, 조율을 Eurojust에 귀속시키며, 참여 또는 영향을 받은 관할 구역으로 호주, 불가리아, 프랑스, 독일, 이탈리아, 네덜란드, 스위스, 영국, 미국이 기록되어 있다.

협력 모델은 명시된 기관 및 파트너를 통해 문서화된다. Europol Ec3, Eurojust, Fbi Cyber Division, Us Doj, Uk Nca, Germany Bka, Netherlands Politie. 메커니즘: Europol Jit. 법적 근거: Budapest Convention. 집행 태세: 체포, 압수, 자산 동결.

정본 기록에 포착된 작전 결과: 체포 150명. 암호화폐/자산 결과는 현금 및 가상화폐 2,670만 유로(약 3,100만 미국 달러)로 기록됨. 마약 234kg 압수(암페타민 152kg, 오피오이드 27kg, 엑스터시 25,000정 이상). 총기 45정 압수. 이탈리아 당국이 동시에 DeepSea 및 Berlusconi 시장 폐쇄.

정본 자료 집합은 5건의 참고문헌을 포함한다: 2021 10 26 Europol Europa Eu 150 Arrested In Dark Web Drug Bust As Police Seize Eur 26 Million, 2021 10 26 Dea Gov Department Of Justice Announces Results Of Operation Dark Huntor, 2021 10 26 Justice Gov Deputy Ag Lisa Monaco Delivers Remarks On Operation Dark Huntor, 2021 10 27 Nationalcrimeagency Gov Uk International Operation Targets Dark Web Drugs Marketplace, 2021 01 12 Europol Europa Eu Darkmarket World S Largest Illegal Dark Web Marketplace Taken Down.
자료 하한은 정본 작전 기준으로 충족되나, 자료의 폭만으로 모든 후속 체포나 양형이 본 작전의 일부임이 입증되지는 않는다. 후속 기록은 별도로 연결되어야 한다.
프론트매터에 결여 필드 플래그가 현재 본 페이지에 부착되어 있지 않다.
데이터셋 사용 목적상, 본 페이지는 작전 단위 집계 지점으로 다루어져야 한다. 국가, 기관, 메커니즘 및 결과 필드는 조율된 법집행 조치 전체를 기술한다. 후속 기소, 청원, 양형, 범죄인 인도 또는 몰수 조치는 자료가 그것들을 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 부착되어야 한다.
자료 기록에 보다 광범위한 배경, 반복되는 통신사 재게재, 또는 토픽 페이지 자료가 포함될 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 법집행 결과에 직접 결부된 사실에 우선순위를 부여한다. 주변적 자료 제목은 독립적 분류체계나 결과 증거로 다루어지지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌
| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 다크웹 마약 검거에서 150명 체포, 경찰 2,600만 유로 압수 | Europol | 2021-10-26 | https://www.europol.europa.eu/media-press/newsroom/news/150-arrested-in-dark-web-drug-bust-police-seize-%E2%82%AC26-million |
| [2] | 미국 법무부 Operation Dark HunTor 결과 발표 | US DOJ/DEA | 2021-10-26 | https://www.dea.gov/press-releases/2021/10/26/department-justice-announces-results-operation-dark-huntor |
| [3] | 국제 작전, 다크웹 마약 시장을 표적으로 함 | UK NCA | 2021-10-27 | https://www.nationalcrimeagency.gov.uk/news/international-operation-targets-dark-web-drugs-marketplace |
| [4] | Lisa Monaco 법무부 차관 Operation Dark HunTor에 관한 발언 | US DOJ | 2021-10-26 | https://www.justice.gov/archives/opa/speech/deputy-attorney-general-lisa-o-monaco-delivers-remarks-operation-dark-huntor |
| [5] | 경찰, 불법 마약 및 총기를 판매한 다크웹 판매자 150명 체포 | BleepingComputer | 2021-10-26 | https://www.bleepingcomputer.com/news/security/police-arrest-150-dark-web-vendors-of-illegal-drugs-and-guns/ |
