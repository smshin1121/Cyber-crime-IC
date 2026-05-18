## 개요

Carding Action 2020은 2020년 9월부터 11월 사이 [[europol-ec3|Europol(유럽 경찰청) 유럽사이버범죄센터(EC3)]]가 조율한 3개월 간의 정보 주도형 작전이다. 본 작전은 다크웹 카드 상점 및 마켓플레이스에서 침해된 결제카드 데이터를 거래하는 행위자를 표적으로 삼았다. [[italy|이탈리아]], [[hungary|헝가리]], [[united-kingdom|영국]]의 법집행 기관이 유일한 민간부문 사이버보안 파트너인 [[group-ib|Group-IB]] 및 주요 카드 결제 스킴과 협력하여 약 90,000건의 도난 카드 데이터를 분석하였다. 본 작전은 약 EUR 4,000만(약 USD 4,800만)의 잠재적 사기 손실을 예방한 것으로 평가된다. 공개적으로 발표된 체포는 없었다; 본 작전은 주로 정보 주도형이며 예방적 성격을 띤다.

## 배경

결제카드 사기(카딩(카드 사기))는 사이버 가능형 금융범죄에서 가장 흔한 형태 중 하나로 남아 있다. 도난 카드 데이터는 일반적으로 피싱 웹사이트, 최종사용자 기기를 감염시키는 뱅킹 트로이, 침해된 전자상거래 플랫폼에 주입된 자바스크립트 스니퍼(JS 스니퍼 또는 Magecart 유형 공격)를 통해 수집된다. 이후 이 데이터는 다크웹 "카드 상점" — 도난 카드 번호, CVV, 관련 개인식별정보가 대량으로 판매되는 전용 마켓플레이스 — 에서 거래된다.

2020년경 가맹점 POS 시스템과 전자상거래 사이트를 표적으로 한 e-스키밍 공격의 확대는 다크웹에서 유통되는 침해 카드 데이터의 상당한 증가에 기여하였다. [[europol-ec3|Europol EC3]]는 사기가 발생하기 전에 이 공급망을 와해하기 위해 Carding Action 2020을 개시하였으며, 순수한 단속 주도 전략보다 사전적, 예방 중심의 접근을 채택하였다.

## 참여 당사자

### 주도 및 조정

| 역할 | 기관 |
|------|--------|
| 조정자 | [[europol-ec3|Europol EC3]] |
| 운영 분석 | Europol 분석가 |

### 법집행 파트너

| 국가 | 기관 | 역할 |
|---------|--------|------|
| [[italy]] | 이탈리아 법집행 | 공동 주도 |
| [[hungary]] | 헝가리 법집행 | 공동 주도 |
| [[united-kingdom]] | 카드·결제범죄전담반(DCPCU), 런던 메트로폴리탄 경찰 및 시티 오브 런던 경찰 | 운영 지원 |

### 민간부문 파트너

| 기관 | 역할 |
|--------|------|
| [[group-ib|Group-IB]] | 유일한 사이버보안 기업; 90,000건의 침해 카드 기록 분석 제공 |
| 주요 카드 스킴 | 침해 계정에 대한 정보 공유 (이름 비공개이나 Visa, Mastercard 포함 추정) |

> [!note] Participant scope
> 참여국 목록은 Europol과 Group-IB 보도자료에 지명된 국가로 한정된다. Europol 정보공유 채널을 통해 기여한 추가 국가가 있을 수 있으나 공개적으로 인정되지는 않았다.

## 법적 근거

본 작전은 공식 형사사법공조(MLA) 절차가 아니라 [[public-private-cooperation|민관 협력]] 메커니즘에 의존하였다. [[europol-ec3|Europol EC3]]는 EU 회원국의 사이버범죄 대응을 지원하는 권한 하에서 법집행 당국과 민간부문 파트너 간의 조정과 정보 교환을 촉진하였다. [[budapest-convention|사이버범죄에 관한 부다페스트 협약]]은 모든 참여국이 당사국인 점에 비추어 국경 간 협력의 기저 법적 틀을 제공한 것으로 추정된다.

## 작전 타임라인

| 일자 | 사건 |
|------|-------|
| 2020년 9월 | 작전 개시; 데이터 수집 및 분석 단계 시작 |
| 2020년 9–11월 | Group-IB가 약 90,000건의 침해 카드 데이터를 분석 |
| 2020년 9–11월 | 카드 스킴과 법집행이 침해 데이터를 활성 계정과 교차 참조 |
| 2020-11-26 | Europol이 본 작전과 그 결과를 공개 발표 |

## 결과 및 영향

| 지표 | 수치 |
|--------|-------|
| 분석된 침해 카드 기록 | 약 90,000 |
| 예방된 추정 손실 | EUR 4,000만 (~USD 4,800만) |
| 공개적으로 확인된 체포 | 0 |
| 식별된 카드 데이터 출처 | 피싱 사이트, 뱅킹 트로이, 전자상거래 사이트의 JS 스니퍼 |

Group-IB가 분석한 90,000건의 카드 기록 전부는 카드 전체 데이터(카드번호, 만료일, CVV, 다수의 경우 카드 소지자 이름과 주소)를 포함하였다. 침해 출처는 다음과 같다:

- 정당한 은행 또는 결제 포털을 사칭하는 **피싱 웹사이트**
- 최종사용자 기기에 설치된 **뱅킹 트로이**
- 탈취된 전자상거래 가맹점 웹사이트에 주입된 **JS 스니퍼**(Magecart 유형 스크립트)

주요 성과는 예방적이었다: 침해된 카드는 사기 거래가 완료되기 전에 차단 또는 강화 모니터링을 위해 발급 은행에 통보되었다.

## 활용된 협력 메커니즘

1. **[[public-private-cooperation|민관 협력]]**: 본 작전의 결정적 특징. 침해 카드 데이터에 대한 Group-IB의 위협 정보가 Europol과 공유되었고, Europol은 신속한 완화를 위해 국내 법집행과 카드 스킴에 그 배포를 조정하였다.

2. **[[informal-cooperation|비공식 경찰 협력]]**: Europol은 공식 형사사법공조조약(MLAT) 요청 없이 참여 기관 간 실시간 정보 교환을 촉진하여 침해 계정의 신속한 식별을 가능하게 하였다.

3. **Europol 운영 지원**: Europol 분석가는 대용량 데이터에 대한 운영 분석과 결제카드 사기 분야의 전문성을 제공하였다.

## 도전 및 마찰 요인

- **귀속 곤란성**: 익명화 도구와 암호화폐 결제로 인해 다크웹 카드 상점 운영자 배후 개인을 식별하는 것은 여전히 기술적으로 도전적이다.
- **[[jurisdictional-conflicts|관할권 복잡성]]**: 침해 카드 데이터는 전 세계 피해자로부터 발생하고, 다수 관할권의 서버에서 판매되며, 또 다른 관할권의 사기범에 의해 구매되어 단속 조치가 복잡하다.
- **문제의 규모**: 90,000건의 기록은 어느 시점이든 다크웹에서 유통되는 도난 카드 데이터 총량의 일부에 불과하다.

## 교훈

1. **전략으로서의 예방**: Carding Action 2020은 체포나 테이크다운을 요구하지 않고도 사전적 분석과 통보가 상당한 금전적 손실을 예방할 수 있음을 입증하였다.

2. **민간부문 정보의 필수성**: [[group-ib|Group-IB]]의 기여는 결정적이었다. 법집행 단독으로는 전문 사이버보안 기업이 보유한 다크웹 카드 상점에 대한 동등한 가시성을 갖지 못한다.

3. **확장 가능한 모델**: 본 작전은 향후 카딩 단속 작전의 템플릿을 확립하였다. Europol은 이후 본 민관 협력 모델을 기반으로 유사 작전을 수년에 걸쳐 수행하였다.

## 한국의 참여

Carding Action 2020에 한국의 참여는 공개적으로 문서화되어 있지 않다. 그러나 [[south-korea|한국]]은 상당한 카드 사기 도전에 직면하고 있으며, 한국 결제카드 데이터가 다크웹 카드 상점에서 발견된 바 있다. Europol 주도 카딩 단속의 향후 반복은 [[knpa|한국 경찰청]] 사이버범죄 부서 및 한국 금융기관과의 협력에서 이익을 얻을 수 있을 것이다.

## 모순점 및 미해결 문제

- **체포 수 불분명**: Europol 또는 참여 기관에 의해 공개적으로 발표된 체포는 없다. 수집된 정보가 본 작전에 공개적으로 귀속되지 않은 후속 법집행 조치로 이어졌는지는 여전히 불확실하다.
- **민간부문 참여의 범위**: Europol은 "카드 스킴"을 언급했지만 이름을 지명하지 않았다. Group-IB 이외 민간부문 참여의 전체 범위는 불분명하다.
- **후속 작전**: 본 작전의 정보가 후속 단속 조치에 공급되었는지 여부는 공개적으로 공개되지 않았다.


## 후속 조치

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전에 대한 공개적으로 접근 가능한 법원
> 문서는 발견되지 않았다. 가능한 사유: 공개 법원 기록 시스템이 없는
> 비미국 관할권, 봉인 절차, 또는 작전이 공식 기소에 이르지 않음.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- UK Finance, 2020-11-26: DCPCU works with Europol on operation Carding Action 2020.
- CISO MAG, 2020-12-01: Operation Carding Action 2020 Cracks Down Credit Card Scammers.
- EAST, 2020-11-30: Carding Action by Police prevents EUR 40 million in losses.
- Group-IB, 2020-11-26: Carding Action 2020: Group-IB supports Europol-backed operation saving EUR 40 million.
- WeLiveSecurity, 2020-11-27: Europol and partners thwart credit card fraud scheme.
- Europol, 2020-11-26: Officers foil fraudsters stealing EUR 40 million in payment card scam.

## Evidence and Attribution Notes

- UK Finance는 Europol의 Carding Action 2020에 대한 DCPCU 지원을 묘사하였다.
- 본 발표는 해당 단속 조치가 GBP 4,000만의 손실 예방에 도움이 되었다고 밝혔다.
- UK Finance는 Carding Action 2020에서 카드·결제범죄전담반(DCPCU)의 역할을 묘사하였다.
- CISO MAG는 Carding Action 2020과 그 EUR 4,000만 손실 예방 수치를 요약하였다.
- 동지는 이탈리아, 헝가리, 영국, Europol, Group-IB의 협력을 강조하였다.
- EAST는 3개월간의 Carding Action 2020과 90,000건 카드 데이터 분석을 요약하였다.
- 본 보고서는 Europol 조정과 민간부문 협력을 묘사하였다.
- EAST는 보안 거래 부문 관점에서 Carding Action 2020을 다루었다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a joint-investigation against Dark web card shops and compromised payment card data traders, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Europol EC3 and coordination to Europol EC3, with participating or affected jurisdictions recorded as Italy, Hungary, United Kingdom.

The cooperation model is documented through named agencies and partners: Europol EC3 and Group-IB; mechanisms: Public-Private Cooperation and Informal Police Cooperation; legal basis: Budapest Convention; enforcement posture: Seizure.

Operational results captured for the canonical record: 90,000 pieces of compromised card data analysed; EUR 40 million in potential losses prevented.

The canonical source set contains 6 reference(s): 2020 11 26 Ukfinance Org Uk Dcpcu Works With Europol On Operation Carding Action 2020, 2020 12 01 Cisomag Com Operation Carding Action 2020 Cracks Down Credit Card Scammers, 2020 11 30 Association Secure Transactions Eu Carding Action By Police Prevents E40 Million In Losses, 2020 11 26 Group Ib Com Carding Action 2020, 2020 11 27 Welivesecurity Com Europol Partners Thwart Credit Card Fraud Scheme, 2020 11 26 Europol Europa Eu Officers Foil Fraudsters Stealing Eur 40 Million In Payment Card Scam.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Arrests (none Publicly Confirmed) and Case Id.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행자 | 일자 | URL |
|---|---|---|---|---|
| [1] | DCPCU works with Europol on operation Carding Action 2020 | UK Finance | 2020-11-26 | https://www.ukfinance.org.uk/press/press-releases/dcpcu-works-with-europol-on-operation-carding-action-2020 |
| [2] | Operation Carding Action 2020 Cracks Down Credit Card Scammers | CISO MAG | 2020-12-01 | https://cisomag.com/credit-card-scammers-arrested-in-carding-scam-2020/ |
| [3] | Carding Action by Police prevents EUR 40 million in losses | EAST | 2020-11-30 | https://www.association-secure-transactions.eu/carding-action-by-police-prevents-e40-million-in-losses/ |
| [4] | Carding Action 2020: Group-IB supports Europol-backed operation saving EUR 40 million | Group-IB | 2020-11-26 | https://www.group-ib.com/it/media-center/press-releases/carding-action-2020/ |
| [5] | Europol and partners thwart credit card fraud scheme | WeLiveSecurity | 2020-11-27 | https://www.welivesecurity.com/2020/11/27/europol-partners-thwart-credit-card-fraud-scheme/ |
| [6] | Officers foil fraudsters stealing EUR 40 million in payment card scam | Europol | 2020-11-26 | https://www.europol.europa.eu/newsroom/news/officers-foil-fraudsters-stealing-%E2%82%AC40-million-in-payment-card-scam |
