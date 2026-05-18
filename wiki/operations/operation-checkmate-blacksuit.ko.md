## 개요

Operation Checkmate(체크메이트 작전)는 **BlackSuit(랜섬웨어)(구 Royal) 랜섬웨어 그룹**을 와해시키기 위한 국제 공조 작전으로, DOJ(미국 법무부)가 2025년 8월 11일에 발표하였다. 이 작전은 2025년 7월 24일 **서버 4대 및 도메인 9개** 테이크다운으로 정점에 달했다. 압수된 도메인은 BlackSuit이 탈취 데이터를 유출하고 피해자와 랜섬 협상을 진행하는 데 사용되었다. **USD 1,091,453** 상당의 가상자산이 압수되었다.

이 작전에는 미국 5개 기관 — 국토안보수사국(Homeland Security Investigations, HSI), 미국 비밀경호국, IRS 형사수사국(IRS-CI), [[fbi-cyber-division|FBI(미국 연방수사국)]], DOJ — 과 영국, 독일, 아일랜드, 프랑스, 캐나다, 우크라이나, 리투아니아의 국제 법집행기관이 참여하였다.

## 배경

### 수법(모더스 오페란디)

BlackSuit은 **2023년 중반**에 **Royal 랜섬웨어** 그룹의 리브랜드로 등장하였으며, Royal 자체는 2022년 Conti 붕괴 이후 Conti 생태계에서 파생된 그룹이었다. 이 그룹은 **이중 갈취** 모델을 운영하였다. 가맹조직(affiliate)들은 주로 **악성 첨부파일이 포함된 피싱 이메일, 패치되지 않은 경계 장비(VPN, RDP, 인터넷 노출 서버)에 대한 익스플로잇, 유효 자격증명의 악용**을 통해 초기 침투를 확보한 후, Cobalt Strike와 기타 포스트익스플로잇 도구를 배포하여 횡적 이동을 수행하고 백업을 무력화한 다음 BlackSuit 암호화기를 실행하였다. 탈취된 데이터는 행위자가 통제하는 호스팅에 업로드되었으며, 침해 사실은 전용 **Tor 기반 데이터 유출 사이트**(2025년 7월 24일 압수된 9개 도메인 중 하나)에 게시되었다. 피해자 협상은 별도의 Tor 기반 **협상 포털**을 통해 진행되었으며, 이 또한 압수된 인프라의 일부였다.

### 피해자 프로파일 및 영향

DOJ Operation Checkmate 발표에 따르면, BlackSuit/Royal은 **2022년 이래 미국에서만 450명 이상의 피해자**를 침해하였으며, **의료, 교육, 제조, 정부, 중요 인프라** 운영자에 부문별 집중도가 높았다. 독립적 산업 추적(Bitdefender, BleepingComputer, TechRadar)은 누적 **랜섬 요구액을 약 USD 5억**으로 추정하였다. Royal은 수주간 시 행정서비스를 중단시킨 **2023년 5월 텍사스주 댈러스시 공격**의 지목된 공격자였으며, BlackSuit은 미국·캐나다 수천 개 자동차 딜러를 마비시킨 **2024년 6월 CDK Global 사건**의 지목된 공격자였다. 이 두 사례만으로도 수백만 명의 최종 사용자에게 영향을 미쳤다.

### 자금 흐름

랜섬은 **비트코인과 모네로(Monero)**로 요구되었다. Operation Checkmate를 뒷받침하는 DOJ 제출 자료는 **USD 1,091,453 상당의 가상자산**과 별도로 기록된 피해자 랜섬 지급금 **49.3120227 BTC(거래 시점 기준 약 USD 144만 5천)**의 압수를 기록하였다. 이는 BlackSuit이 통제하는 지갑으로 라우팅되었다가 법원 승인 압수 영장을 통해 회수되었다. 모든 피해자에 걸친 총 랜섬 수령액은 공개적으로 정량화되어 있지 않으나, 약 USD 5억의 총 랜섬 요구액은 RaaS 일반 지급률 5–15%를 감안할 때 *높은 확률로* 실제 수령액이 수천만 달러 중·저 수준이었음을 시사한다.

### 범죄 조직 구조

BlackSuit은 Conti와 Royal로부터 계승한 **핵심팀 + 가맹조직** 구조를 유지하였다. 핵심팀은 암호화기 변종(Royal 바이너리의 후속이며 Royal 자체는 Conti 파생), 유출 사이트, 협상 인프라를 관리하였고, 가맹조직은 랜섬의 일정 비율을 받는 대가로 침투를 수행하였다. 미국 법집행기관 및 민간 위협 인텔리전스 업체의 공개 귀속은 핵심 그룹을 **러시아어 사용 운영자**와 연결하며, 이전 Conti 및 Royal 인원과의 중복을 시사한다. 2025년 7월 와해 조치의 일환으로 공개적으로 기소된 BlackSuit 운영자는 없으며, 이는 아래 *모순점 및 미해결 문제*에 명시적으로 기록된 후속 집행 공백으로 남아 있다.

## 참여 당사자

- **미국 기관:** DOJ, DHS 국토안보수사국(HSI), 미국 비밀경호국, IRS 형사수사국, [[fbi-cyber-division|FBI]]
- **국제 파트너:** 영국, 독일, 아일랜드, 프랑스, 캐나다, 우크라이나, 리투아니아
- **총 국가 수:** 8개국

## 결과 및 영향

| 지표 | 값 |
|--------|-------|
| 압수 서버 | 4 |
| 압수 도메인 | 9 |
| 압수 암호화폐 | USD 1,091,453 |
| 미국 피해자 수(2022년 이래) | 450명 이상 |
| 참여 국가 수 | 8 |
| 참여 미국 기관 수 | 5 |

## 한국의 참여

본 작전에 한국 참여는 기록되지 않았다.

## 모순점 및 미해결 문제

- BlackSuit 운영자 중 식별되거나 기소된 자가 있는가? (2025년 7월 와해 조치에는 공개 기소가 동반되지 않았으며, 이는 위 범죄 조직 구조 기록에 명시된 공백이다.)
- BlackSuit/Royal이 모든 피해자로부터 수령한 **총 랜섬 액수**는 얼마인가? (1차 출처는 약 USD 5억의 요구 총액을 보고하지만 총 지급액 수치는 없으며, 이 공백은 위 *자금 흐름*에 표시되어 있다.)
- Royal이 BlackSuit이 되었듯, 이 그룹이 새로운 이름으로 재구성될 것인가?
- 구체적인 가맹조직 명단과 BlackSuit 운영자의 지리적 분포는 DOJ Operation Checkmate 발표에 공개되지 않았으며, 민간 위협 인텔리전스의 러시아어 사용 운영자 귀속은 미국 법집행 기록에 공식적으로 채택되지 않았다.

## 후속 조치

> [!warning] No public court documents found
> 2026년 4월 17일 웹 검색에서는 본 작전에 대한 공개 접근 가능한 법원 제출 자료가 확인되지 않았다. 가능한 이유: 공개 법원 기록 시스템이 없는 비미국 관할권, 봉인 절차, 또는 작전이 공식 기소로 이어지지 않은 경우.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- 미국 법무부, 2025-08-11: 법무부, BlackSuit(Royal) 랜섬웨어 운영에 대한 공조 와해 조치 발표.
- BleepingComputer, 2025-07-24: Operation Checkmate에서 BlackSuit 랜섬웨어 갈취 사이트 압수.
- SC Media, 2025-07-25: Operation Checkmate, BlackSuit의 갈취 사이트 폐쇄.
- Bitdefender, 2025-07-25: USD 5억 랜섬 요구 이후 법집행기관이 BlackSuit 사이트 압수.
- TechRadar, 2025-07-28: 최상위 랜섬웨어 그룹 BlackSuit, 다크웹 갈취 사이트 압수 및 폐쇄.

## Operational Timeline

- 2022년: 활동 또는 수사 시작.
- 2025-08-11: 공개 발표.
- 2025-07-24: 보고된 집행 시점.
- 2025-07-24: BleepingComputer의 공개 보도.
- 2025-07-25: Bitdefender, SC Media의 공개 보도.
- 2025-07-28: TechRadar의 공개 보도.
- 2025-08-11: 미국 법무부의 공개 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: 랜섬웨어 및 다크웹.
- 기록된 집행 형태: 압수, 테이크다운, 자산 동결.
- 본 기록은 status completed의 takedown으로 분류된다.

## Evidence and Attribution Notes

- DOJ 보도자료는 Operation Checkmate 하에 BlackSuit(Royal) 랜섬웨어 그룹에 대한 공조된 국제 와해 조치를 발표하였다.
- 본 작전에는 미국 5개 기관과 7개국의 국제 파트너가 참여하였으며, 데이터 유출 및 랜섬 협상에 사용된 서버 4대와 도메인 9개를 압수하였다.
- 미국 법무부는 2025년 8월 11일에 BlackSuit(Royal) 랜섬웨어 그룹에 대한 공조된 국제 와해 조치를 발표하였다.
- Operation Checkmate라는 암호명의 본 작전에는 2025년 7월 24일의 서버 4대 및 도메인 9개 테이크다운이 포함되었다.
- 압수된 도메인은 BlackSuit이 탈취 데이터를 유출하고 피해자와 랜섬 지급 협상을 진행하기 위해 사용한 도메인이었다.
- BleepingComputer는 BlackSuit의 갈취 및 유출 사이트가 Operation Checkmate에서 압수되었다고 보도하였다.
- 해당 기사는 DOJ가 법원 승인 도메인 압수를 확인하였다고 전하였다.
- 7월 24일 인프라 조치에 관한 최초의 공개 보도를 보존한다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- 미국 법무부, 2025-08-11: The takedown was conducted by the Department of Homeland Security's Homeland Security Investigations (HSI), the U.S.
- 미국 법무부, 2025-08-11: Secret Service, IRS Criminal Investigation (IRS-CI), the FBI, and international law enforcement from the United Kingdom, Germany, Ireland, France, Canada, Ukraine, and Lithuania.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라 BlackSuit(구 Royal) 랜섬웨어 그룹에 대한 테이크다운을 기술하므로 정본 작전(canonical operation)으로 유지된다. 본 기록은 주도 책임을 Fbi Cyber Division에, 조율을 Fbi Cyber Division에 귀속시키며, 참여 또는 영향 관할권은 미국, 영국, 독일, 프랑스로 기록되어 있다.

협력 모델은 명명된 기관 및 파트너를 통해 문서화된다: Fbi Cyber Division; 집행 형태: 압수, 테이크다운, 자산 동결.

정본 기록에 포착된 작전 결과: 서버 4대 압수; 도메인 9개 압수; 암호화폐/자산 결과는 USD 1,091,453로 기록; 2022년 이래 미국 피해자 450명 이상 식별; 한 사건에서 거래 시점 USD 1,445,454.86 상당의 비트코인 랜섬 지급금 49.3120227 BTC 압수.

정본 출처 집합은 5개의 참조를 포함한다: 2025 08 11 Doj Blacksuit Royal Ransomware Takedown, 2025 07 24 Bleepingcomputer Com Law Enforcement Seizes Blacksuit Ransomware Leak Sites, 2025 07 25 Scworld Com Operation Checkmate Shuts Down Blacksuits Extortion Sites, 2025 07 25 Bitdefender Com After 500 Million In Ransom Demands Law Enforcement Seizes Blacksuit Site, 2025 07 28 Techradar Com Top Ransomware Group Blacksuit Has Dark Web Extortion Sites Seized And Shut Down.
정본 작전의 출처 하한은 충족되나, 출처의 폭만으로는 모든 후속 체포나 형 선고가 본 작전의 일부임이 증명되지 않으며, 후속 기록은 별도로 연결되어야 한다.
본 페이지가 여전히 갖고 있는 알려진 메타데이터 공백: Legal Basis, Mechanisms Used, Specific International Agencies.
데이터셋 활용을 위해, 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 공조 집행 조치 전체를 기술한다. 이후의 기소, 답변, 형 선고, 범죄인 인도, 몰수 조치는 출처가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 첨부되어야 한다.
출처 기록이 더 광범위한 배경, 반복되는 와이어 서비스 재게재, 또는 토픽 페이지 자료를 포함할 때, 본 평가는 명명된 작전, 그 참여 기관, 그 표적 인프라 또는 범죄 서비스, 그리고 그 측정 가능한 집행 결과와 직접 연결된 사실에 우선순위를 부여한다. 부수적인 출처 제목은 독립적인 분류 또는 결과 증거로 취급되지 않는다.
이로써 정본 기록은 분석적으로 한정되고 재현 가능하게 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 법무부, BlackSuit(Royal) 랜섬웨어 운영에 대한 공조 와해 조치 발표 | US Department of Justice | 2025-08-11 | https://www.justice.gov/opa/pr/justice-department-announces-coordinated-disruption-actions-against-blacksuit-royal |
| [2] | Operation Checkmate에서 BlackSuit 랜섬웨어 갈취 사이트 압수 | BleepingComputer | 2025-07-24 | https://www.bleepingcomputer.com/news/security/law-enforcement-seizes-blacksuit-ransomware-leak-sites/ |
| [3] | Operation Checkmate, BlackSuit의 갈취 사이트 폐쇄 | SC Media | 2025-07-25 | https://www.scworld.com/brief/operation-checkmate-shuts-down-blacksuits-extortion-sites |
| [4] | USD 5억 랜섬 요구 이후 법집행기관이 BlackSuit 사이트 압수 | Bitdefender | 2025-07-25 | https://www.bitdefender.com/en-us/blog/businessinsights/blacksuit-ransomware-seized-takedown |
| [5] | 최상위 랜섬웨어 그룹 BlackSuit, 다크웹 갈취 사이트 압수 및 폐쇄 | TechRadar | 2025-07-28 | https://www.techradar.com/pro/security/top-ransomware-group-blacksuit-has-dark-web-extortion-sites-seized-and-shut-down |
