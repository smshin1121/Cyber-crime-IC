## 개요

**2024년 4월 14일부터 17일까지**, **영국 런던 경시청(London Metropolitan Police)**이 주도하고 **Europol(유럽 경찰청) 유럽사이버범죄센터(EC3)** 및 Europol 본부에 설치된 **합동사이버범죄대응팀(Joint Cybercrime Action Taskforce, J-CAT)**의 지원을 받아 진행된 국제 수사는 **19개국**에 걸쳐 **70건의 수색**을 집행하였으며, **37명의 체포**를 산출하였다. 여기에는 사이트 운영과 관련된 **영국 내 4명**이 포함되며, **LabHost 원개발자**도 그중 한 명이다. **LabHost 피싱서비스형(PhaaS) 플랫폼**(LabHost(피싱 플랫폼))은 폐쇄되었다. LabHost는 사이버범죄자에게 구독제(월 평균 249달러) 방식으로 피싱 키트, 위장 페이지 호스팅 인프라, **170개 이상의 위장 웹사이트 템플릿**, 그리고 **이중인증(2FA) 코드**를 캡처할 수 있는 통합 캠페인 관리 도구 **LabRat**을 제공하였다. 수사를 통해 LabHost와 연계된 **최소 40,000개의 피싱 도메인**과 **전 세계 약 10,000명의 사용자**가 확인되었다.

## 배경

사이버범죄서비스형(CaaS)은 위협 행위자가 다른 사이버범죄자에게 공격 도구, 전문성, 서비스를 임대하거나 판매하여 공격을 수행하게 하는, 범죄 환경에서 급성장하는 비즈니스 모델이 되었다. 이 모델은 랜섬웨어 그룹(예: [[operation-cronos-phase1|Operation Cronos / LockBit]])에서 잘 정립되어 있지만, 피싱과 같은 사이버범죄의 다른 영역에서도 채택되어 왔다. LabHost는 피싱을 상품화하여 맞춤형, 클릭 배포 가능한 키트를 제공하였으며, 구독 단계별로 금융기관, 우편 배송 서비스, 통신사업자를 포함한 다양한 타깃군에 대한 접근 권한을 부여하였다.

LabHost가 특히 파괴적이었던 점은 통합 캠페인 관리 도구 **LabRat**으로, 이를 통해 사이버범죄자들은 자신의 공격을 실시간으로 모니터링하고 통제할 수 있었다. LabRat은 **이중인증 코드와 자격증명**을 캡처하도록 특별히 설계되어, 범죄자들이 강화된 보안 조치를 우회할 수 있도록 하였다.

## 참여 당사자

| 국가 | 주관 기관 |
|---|---|
| 호주 | 호주연방경찰 주도 합동치안사이버범죄조정센터(AFP / JPC3); 빅토리아 경찰, 퀸즐랜드 경찰청, NSW 경찰, WA 경찰과 합동(Operation Nebulae) |
| 오스트리아 | 형사정보국(Bundeskriminalamt) |
| 벨기에 | 브뤼셀 연방사법경찰 |
| 캐나다 | 캐나다 왕립기마경찰(RCMP) |
| 체코 | 형사경찰수사국 |
| 에스토니아 | 에스토니아 경찰·국경수비청 |
| 핀란드 | 국가경찰(Poliisi) |
| 아일랜드 | 안 가르다 시오하나(An Garda Síochána) |
| 리투아니아 | 리투아니아 경찰 |
| 몰타 | 몰타 경찰청 |
| 네덜란드 | 중부 네덜란드 경찰(Politie Midden-Nederland) |
| 뉴질랜드 | 뉴질랜드 경찰 |
| 폴란드 | 사이버범죄대응중앙국(Centralne Biuro Zwalczania Cyberprzestępczości) |
| 포르투갈 | 사법경찰(Polícia Judiciária) |
| 루마니아 | 루마니아 경찰(Poliția Română) |
| 스페인 | 국가경찰(Policía Nacional) |
| 스웨덴 | 스웨덴 경찰청(Polisen) |
| 영국 | 런던 경시청(주도) |
| 미국 | 미국 비밀경호국(USSS) + FBI(미국 연방수사국) |
| 조정 | [[europol-ec3\|Europol 유럽사이버범죄센터(EC3)]] + 합동사이버범죄대응팀(J-CAT) |

## 작전 타임라인

| 일자 | 사건 | 출처 |
|---|---|---|
| 2023년 9월 | Europol(유럽 경찰청)이 사건 지원 시작 | Europol 2024-04-18 |
| (일자 미기재) | 19개 참여국 전원과 함께 Europol 본부에서 운영 스프린트 진행, 각 관할에서 LabHost 사용자 및 피해자 식별 | Europol 2024-04-18 |
| 2024-04-14~2024-04-17 | 작전일: 전 세계 70건 수색; 37명 체포; LabHost 개발자 포함 영국 내 4명 체포; Europol 전문가가 네덜란드 국가경찰에 현장 배치 | Europol 2024-04-18 |
| 2024-04-17 | 호주(Operation Nebulae, AFP JPC3 + 빅토리아/퀸즐랜드/NSW/WA 경찰): 5개 주(빅토리아 14건, 퀸즐랜드 2건, NSW 3건, 남호주 1건, 서호주 2건)에 걸쳐 22건의 압수수색영장 집행, AFP 및 주·준주 경찰관 200명 이상 투입; 5명 체포(LabHost 사용자 혐의 사이버범죄로 멜버른 1명 + 애들레이드 1명; 마약 혐의로 멜버른 3명 추가); 207개 범죄용 서버 폐쇄 | AFP 2024-04-18 |
| 2024-04-18 | Europol 공개 발표; LabHost 플랫폼 폐쇄. AFP가 빅토리아/퀸즐랜드/NSW/WA 경찰과 합동 보도자료로 호주 측 작전 발표 | Europol & AFP 2024-04-18 |

## 결과 및 영향

- 2024-04-14 ~ 2024-04-17 작전일 동안 **37명 체포**.
- 전 세계에서 **70개 주소 수색**.
- 사이트 운영과 연결된 **영국 내 4명 체포**, **LabHost 원개발자 포함**.
- **LabHost 플랫폼 폐쇄**(기존에는 공개 웹에서 이용 가능).
- LabHost와 연계된 **40,000개 이상의 피싱 도메인**.
- **전 세계 약 10,000명의 LabHost 사용자**.
- **LabRat 2FA 캡처 도구** 무력화.

### 호주 (Operation Nebulae — AFP JPC3 + 주 경찰)

2024-04-18 자 [[2024-04-18_afp-gov-au_global-sting-sees-australian-offenders-arrested-cybercrime-and-phishing|AFP 합동 보도자료]](빅토리아 경찰, 퀸즐랜드 경찰청, NSW 경찰, WA 경찰과 합동 발표)에 따르면:

- 2024-04-17 **호주 내 5명 체포** — 멜버른 남성 1명 + 애들레이드 남성 1명이 LabHost 사용자 혐의로 사이버범죄 혐의 기소; 영장 집행 중 멜버른 남성 3명이 추가로 마약 관련 혐의로 기소.
- 5개 주에 걸쳐 **호주 내 22건의 압수수색영장** 집행: 빅토리아 14건, 퀸즐랜드 2건, NSW 3건, 남호주 1건, 서호주 2건. AFP 및 주·준주 경찰관 200명 이상 투입.
- AFP JPC3에 의해 **207개 범죄용 서버 폐쇄**(LabHost가 생성한 사기 피싱 웹사이트를 호스팅하던 서버).
- 호주 피해자를 표적으로 한 **호주 내 LabHost 사용 용의자 100명 이상 식별**.
- LabHost 피싱 캠페인을 통해 **94,000명 이상의 호주인이 표적**이 됨.
- 도난당한 호주 자격증명 판매로 호주인에게 발생한 잠재적 피해 추정액 **호주달러 2,800만**(AFP 사이버사령부 부보좌관 Chris Goldsmid).
- LabHost 기원 귀속(AFP): "2021년 캐나다에서 시작되어 북미를 표적으로 하였으며, 영국(UK)과 아일랜드로 확장한 후 글로벌화. 호주 범죄자들이 상위 3개 사용국 안에 드는 것으로 추정된다."

## 활용된 협력 메커니즘

해당 보도자료는 이 작전에 대한 세 가지 별개의 국제공조 메커니즘 유형을 기술한다:

1. **Europol 합동사이버범죄대응팀(J-CAT)** — Europol 본부에 설치된 다자 조정 도구로, 19개국 합동 작전일 기획 및 실행을 위한 제도적 장(場)을 제공한다.
2. **Europol EC3 운영 스프린트** — 본부에서 모든 참여국과 함께 진행한 작전일 이전 정보 개발 메커니즘으로, 각 참여 관할의 LabHost 사용자 및 피해자를 식별하기 위한 것이다.
3. **작전 단계 Europol 전문가의 현장 배치** — 네덜란드 국가경찰에 대한 배치로, [[eurojust-100m-crypto-investment-fraud-takedown-2025|2025년 Eurojust 1억 유로 암호화폐 투자사기 단속]]에서 포르투갈에 배치된 Europol 암호화폐 전문가와 구조적으로 유사한 메커니즘이나, 본 사건에서는 암호자산 인프라가 아닌 피싱 플랫폼 인프라에 적용되었다.

## 한국의 참여

한국은 인용된 Europol 보도자료에서 19개 참여 관할에 명시되어 있지 않다. 본 사건은 PhaaS 상품화 패턴과 19개국 J-CAT 작전일 모델로서 위키에 기록된다. 전 세계 약 10,000명의 사용자/약 40,000개 도메인 규모를 고려할 때 한국이 LabHost 연계 피싱 캠페인에 노출되었을 가능성은 *높다(likely)*고 판단되나, 이 출처에는 열거되어 있지 않다.

## 모순점 및 미해결 문제

- Europol 1차 출처와 AFP 합동 보도자료 모두 LabHost 원개발자 또는 다른 영국 체포자 3명의 신원을 명시하지 않는다.
- AFP 합동 보도자료는 "94,000명 이상 호주 피해자" 수치를 1차 출처(tier-1) 귀속으로 확인하나, 나머지 18개 참여 관할의 국가별 피해자 총수는 두 1차 출처 어디에도 열거되어 있지 않다.
- CNN 등 2차 보도의 구체적 은행카드/PIN/비밀번호 총수치(48만/6만 4천/100만 이상)는 인용된 두 1차 출처 어디에도 열거되어 있지 않다.
- 체포 후 기소 일정, 기소 건수, 양형 일정은 AFP 보도자료에 명시된 사이버범죄 혐의 호주인 2명과 마약 혐의 호주인 3명 이외에는 열거되어 있지 않다.
- **LabHost 구독 가격 불일치**: Europol 1차 출처는 "월 평균 249달러"라고 기재한 반면, AFP 보도자료는 "월 270달러까지 낮은 가격"이라고 기재한다. 두 수치는 단계별 가격 범위(249달러 평균 / 270달러 입문 단계)로 조정될 수 있으나, 두 1차 출처 어디에도 이를 명시적으로 조정하지 않는다.

## 참고문헌

| # | 제목 | 발행처 | 일자 | URL |
|---|-------|-----------|------|-----|
| [1] | [[2024-04-18_europol_international-investigation-disrupts-phishing-service-platform-labhost\|International investigation disrupts phishing-as-a-service platform LabHost]] | Europol | 2024-04-18 | https://www.europol.europa.eu/media-press/newsroom/news/international-investigation-disrupts-phishing-service-platform-labhost |
| [2] | [[2024-04-18_afp-gov-au_global-sting-sees-australian-offenders-arrested-cybercrime-and-phishing\|Global sting sees Australian offenders arrested for cybercrime and phishing attacks]] | Australian Federal Police (빅토리아 경찰, 퀸즐랜드 경찰청, NSW 경찰, WA 경찰과 합동) | 2024-04-18 | https://www.afp.gov.au/news-centre/media-release/global-sting-sees-australian-offenders-arrested-cybercrime-and-phishing |
