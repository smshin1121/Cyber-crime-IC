## 개요

Operation Onymous(어나니머스 작전, FBI/Europol dark web takedown)는 2014년 11월 5-6일 [[fbi-cyber-division|FBI]], [[europol-ec3|Europol]], [[eurojust|Eurojust]], [[us-dhs|미국 국토안보부(U.S. Department of Homeland Security)]]가 공동으로 수행한 국제 법집행 작전으로, Tor 네트워크상의 다크넷 마켓 및 기타 히든 서비스를 표적으로 삼았다. 본 작전을 통해 Silk Road 2.0, Cloud 9, Hydra를 포함한 27개 별개 웹사이트에 걸친 267개의 .onion 주소를 압수하고, 17명을 체포하였으며, 약 100만 미국 달러 상당의 비트코인과 더불어 현금, 마약, 무기, 컴퓨터를 압수하였다. Silk Road 2.0의 운영자로 지목된 Blake Benthall(가명 "Defcon")은 샌프란시스코에서 체포되었다. 본 작전에는 17개 유럽 국가와 미국이 참여하였으며 당시 Tor 히든 서비스를 겨냥한 최대 규모의 공조 작전이었다. 그러나 Tor 히든 서비스 익명성 해제(deanonymization)에 사용된 방법에 관하여, 특히 Carnegie Mellon University 연구진의 익스플로잇이 활용되었을 가능성에 대하여 상당한 논란이 발생하였다.

## 배경

### 2014년 다크넷 마켓 지형

Operation Onymous(어나니머스 작전, FBI/Europol dark web takedown)는 2013년 10월 [[silk-road-takedown|원조 Silk Road 단속]]과 창립자 Ross Ulbricht의 체포 이후 이루어졌다. Silk Road 폐쇄에 이어 Tor 네트워크상에 다수의 후속 마켓이 등장하였고, Silk Road 2.0은 원조 압수 후 수 주 이내에 개설되었다. 2014년 중반에 이르러 수십 개의 다크넷 마켓이 운영되고 있었으며, Tor 기반 범죄에 대한 법집행 대응 역량이 제한적이라는 인식이 형성되어 있었다.

### Silk Road 2.0

Silk Road 2.0은 2013년 11월 개설되었으며, 가명 "Defcon"으로 활동한 26세의 전(前) SpaceX 직원 Blake Benthall이 운영하였다. 본 마켓은 원조 Silk Road의 기능을 그대로 재현하여 불법 마약, 무기, 위조 문서 및 기타 밀수품의 거래를 매개하였다. 2014년 11월 시점에서 사이트는 월 수백만 달러의 매출을 창출하고 있었으며 수천 명의 판매자와 구매자를 보유하고 있었다.

### 수사 기법

FBI의 Silk Road 2.0 수사에는 다음과 같은 다중 기법이 동원되었다.

1. **잠입 수사**: HSI(국토안보수사국, Homeland Security Investigations) 특수요원이 Silk Road 2.0의 운영 지원 인력으로 성공적으로 침투하여 비공개 관리 영역에 접근하고 Benthall과 직접 소통하였다
2. **서버 식별**: 정부 수사관이 외국 소재의 Silk Road 2.0 서버 위치를 특정하여 복제 목적으로 잠시 오프라인 처리하였다. 그 결과 발생한 자동 알림 이메일이 Benthall의 개인 이메일로 발송되었고, Google이 IP 주소 기록을 통해 이를 서버와 연결지었다
3. **Tor 익명성 해제**: FBI는 2014년 5월 Benthall의 신원을 익명성 해제하였다고 진술하였는데, 이는 Carnegie Mellon University CERT/CC 연구진이 Tor 네트워크 취약점을 식별하였던 시기(약 2014년 2월부터 7월까지 활성화)와 일치한다

## 참여 당사자

### 주관 기관
- **[[fbi-cyber-division|FBI(미국 연방수사국)]]** — Silk Road 2.0 수사 주관 및 미국 측 작전 조정
- **[[europol-ec3|Europol(유럽 경찰청) EC3]]** — 유럽 법집행 작전 조정

### 미국 기관
| Agency | Role |
|--------|------|
| [[fbi-cyber-division\|FBI]] | 미국 수사 주관, Benthall 체포 |
| [[us-dhs\|DHS / HSI (ICE)]] | Silk Road 2.0 잠입 수사 |
| [[eurojust\|Eurojust]] | 유럽 측 사법 공조 조정 |

### 유럽 국가 (16개국)
[[bulgaria|불가리아]], [[czech-republic|체코]], [[finland|핀란드]], [[france|프랑스]], [[germany|독일]], 헝가리, [[ireland|아일랜드]], [[latvia|라트비아]], [[lithuania|리투아니아]], 룩셈부르크, [[netherlands|네덜란드]], [[romania|루마니아]], [[spain|스페인]], [[sweden|스웨덴]], [[switzerland|스위스]], [[united-kingdom|영국]]

> [!note] 참여국 수 불일치
> Europol은 Operation Onymous에 "17개국"이 참여하였다고 발표하였다. 상기 16개 유럽 국가와 미국을 합산하면 17개국이 된다. 일부 출처는 "21개국"이 참여하였다고 기술하는데, 이러한 불일치는 공식 보도자료에서 개별적으로 확인되지 않은 추가적인 비(非)유럽 파트너 국가를 포함하여 집계한 데에서 비롯된 것으로 보인다.

## 법적 근거

- **[[budapest-convention|Budapest Convention]]** — 다수가 협약 당사국인 유럽 참여국들 간의 국경 간 공조에 대한 일차적 틀을 제공
- **미국 컴퓨터 사기 및 남용 방지법(Computer Fraud and Abuse Act, 18 U.S.C. § 1030)** — Benthall에 대한 연방 기소의 근거
- **EU 골격결정 2005/222/JHA(EU Framework Decision 2005/222/JHA)** — 정보시스템에 대한 공격에 관한 결정으로, EU 회원국 간 조화된 범죄 정의를 제공
- **국내 형법** — 각 참여국은 자국법에 의거하여 압수 명령을 집행

Blake Benthall에 대한 기소는 뉴욕남부지방법원(맨해튼 연방법원, Southern District of New York)에 제기되었으며, 마약 거래 공모, 컴퓨터 해킹 공모, 자금세탁 혐의가 포함되었다.

## 작전 타임라인

| Date | Event |
|------|-------|
| 2013-10 | 원조 [[silk-road-takedown\|Silk Road 단속]]; Ross Ulbricht 체포 |
| 2013-11 | Blake Benthall("Defcon") 주도로 Silk Road 2.0 개설 |
| 2014-05 | FBI가 Benthall 신원을 익명성 해제하였다고 주장 |
| 2014-02 ~ 2014-07 | Carnegie Mellon CERT/CC Tor 취약점이 활성화되었던 것으로 보고 |
| 2014-07-04 | Tor Project가 CERT 연구진이 활용한 취약점에 대한 패치 배포 |
| 2014-11-05 | Blake Benthall, 샌프란시스코에서 체포 |
| 2014-11-05 ~ 11-06 | 27개 사이트에 걸친 267개 .onion 주소에 대한 공조 단속 |
| 2014-11-07 | FBI와 Europol, Operation Onymous 공식 발표 |
| 2015-11 | 법원 문서에서 CERT/Tor 취약점 활용에 관한 의문 제기 |

## 결과 및 영향

### 정량적 결과
- 참여국 전반에 걸친 **17명 체포**
- 27개 별개 히든 서비스 웹사이트에 걸친 **267개 .onion 주소 압수**
- **100만 미국 달러** 상당의 비트코인 압수
- **현금, 마약, 무기, 컴퓨터** 압수 (구체적 수량은 공개적으로 집계되지 않음)
- **주요 마켓 폐쇄**: Silk Road 2.0, Cloud 9, Hydra (2022년 폐쇄된 러시아어권 Hydra 마켓과는 별개)

### 핵심 체포: Blake Benthall
Blake Benthall은 2014년 11월 5일 샌프란시스코에서 체포되어 맨해튼 연방법원에서 마약 거래 공모, 컴퓨터 해킹 공모, 자금세탁 혐의로 기소되었다. 그는 가명 "Defcon"으로 Silk Road 2.0을 운영한 혐의를 받았다.

### 억제 효과
Operation Onymous는 Tor 기반 히든 서비스가 법집행 작전에 면역이 아니라는 강력한 신호를 발신하였다. 직후의 양상은 다음과 같다.
- 일부 다크넷 마켓이 자진 폐쇄
- 포럼 논의에서 Tor의 보안에 대한 운영자 및 이용자의 불확실성이 증가한 양상 반영
- Tor Project 자체가 사용된 방법에 대한 우려를 표명하는 블로그 게시물 발표

### 한계
작전의 규모에도 불구하고 새로운 다크넷 마켓이 계속 등장하였다. "두더지 잡기(whack-a-mole)" 양상이 지속되어 [[alphabay-takedown|AlphaBay]] 및 기타 후속 마켓들이 Silk Road 2.0 및 압수된 여타 사이트의 공백을 빠르게 메웠다.

## Cooperation Mechanisms Used

1. **[[joint-investigation-team|Joint Investigation Team]]** — 공조된 유럽 작전을 위해 활용되었을 가능성이 높으나, 구체적인 JIT 세부사항은 공개적으로 문서화되어 있지 않다
2. **[[mutual-legal-assistance|Mutual Legal Assistance]]** — 국경 간 증거 수집 및 서버 식별을 위한 공식 MLA(형사사법공조) 요청
3. **[[informal-cooperation|Informal Police-to-Police Cooperation]]** — Europol의 보안 통신 채널을 통한 FBI와 유럽 법집행 기관 간 실시간 정보 교환
4. **[[eurojust|Eurojust]] 사법 공조** — 16개 유럽 관할권에 걸친 동시 법적 조치 가능
5. **잠입 작전** — HSI 요원의 Silk Road 2.0 직원 침투가 핵심 정보 출처로 작용

## Challenges and Friction Points

### Tor 익명성 해제 논란
Operation Onymous를 둘러싼 가장 중대한 논란은 히든 서비스 운영자 및 서버 위치를 식별하는 데 사용된 방법에 관한 것이다. 2015년 11월에 공개된 법원 문서에 따르면 다음과 같다.

- FBI의 히든 서비스 익명성 해제는 2014년 5월에 이루어졌는데, 이는 Carnegie Mellon University CERT/CC가 Tor 네트워크의 취약점을 식별하고 활용하고 있던 시기와 동일하다
- Tor Project는 2014년 7월 4일 본 취약점을 패치하였다
- 2015년 11월 Tor Project는 FBI가 Carnegie Mellon에 100만 미국 달러를 지불하여 Tor 취약점을 활용해 히든 서비스 이용자를 식별하게 하였다고 공개적으로 주장하였으며, FBI는 이를 부인하였다
- 본 사안은 연구 윤리, 학술적 보안 연구와 법집행 지원의 경계, 영장 없는 Tor 활용이 불법 수색에 해당하는지 여부에 대한 중대한 의문을 제기하였다

### 규모 불일치
초기 발표는 "400개 이상의" 히든 서비스 웹사이트가 압수되었다고 주장하였다. 실제로 확인된 수치는 27개 별개 사이트에 걸친 267개 .onion 주소였다. 이러한 불일치는 개별 .onion 주소(미러 및 중복 포함)와 별개 웹사이트 운영을 각각 집계한 데에서 비롯된 것으로 보인다.

### 관할권의 복잡성
17개국 이상이 관여하고 다중 관할권에 호스팅된 인프라가 압수됨에 따라, 각 관할권에서 압수 명령의 법적 유효성을 확보하기 위한 광범위한 사전 공조가 요구되었다. 구체적으로 직면한 도전 과제는 공개적으로 상세히 문서화되지 않았다.

## Lessons Learned

1. **Tor는 난공불락이 아니다**: Operation Onymous는 법집행기관이 Tor 히든 서비스를 익명성 해제할 역량을 보유하거나 획득할 수 있음을 증명함으로써, 다크넷 마켓 운영자의 위험 계산을 근본적으로 변화시켰다.
2. **잠입 침투는 여전히 매우 효과적이다**: 인적 정보 요소(Silk Road 2.0 직원으로 잠입한 위장 요원)는 기술적 방법만으로는 확보하기 어려웠을 결정적 증거를 제공하였다.
3. **공조 다국가 단속은 억제 효과를 지닌다**: Operation Onymous의 규모 — 17개국, 27개 사이트, 17명 체포 — 는 상당한 언론 보도를 창출하였으며 다크넷 운영자 행태에 적어도 일시적으로 가시적 영향을 미쳤다.
4. **수사 방법은 투명성을 요한다**: CERT/Tor 논란은 사이버 수사에서 투명한 법적 절차의 중요성을 강조하였는데, 익명성 해제 방법의 적법성에 관한 의문이 기소 자체를 훼손할 가능성이 있었기 때문이다.
5. **시장의 이동은 지속된다**: 작전의 규모에도 불구하고 다크넷 마켓은 신속히 재구성되었으며, 이는 단속만으로는 근본적 수요를 해소하지 않는 한 본 현상을 제거할 수 없음을 시사한다.

## Korean Involvement (한국의 참여)

Operation Onymous에 대한 한국의 공개적으로 보고된 참여는 없다. 본 작전은 [[south-korea|한국]]이 국제 사이버범죄 공조 체제에 본격적으로 관여하기 이전에 이루어졌다. 그러나 본 작전은 한국에 다음과 같은 의의를 지닌다.

- 다크넷 범죄에 대한 대규모 국제공조의 실현 가능성을 보여준 기초 사례
- 한국 기관이 참여한 이후 작전들의 선구자적 사례
- 한국 법집행기관이 향후 수사에서 직면할 가능성이 높은 Tor 익명성 해제의 법적·윤리적 도전 과제에 관한 연구

## Contradictions & Open Questions

- **Carnegie Mellon / FBI 관계**: Carnegie Mellon CERT/CC와 FBI 간 관계의 정확한 성격은 여전히 다툼의 여지가 있다. FBI는 100만 미국 달러 지급을 부인하였으나, 법집행과의 공조 속에서 Tor 취약점이 어떻게 활용되었는지에 대한 대안적 설명은 제시하지 않았다. Tor Project는 자신의 주장을 견지하고 있다.
- **참여국 수**: 출처에 따라 17개국, 18개국, 21개국이라고 다양하게 보고된다. 이러한 불일치는 공식적으로 해명된 바 없다.
- **히든 서비스 수**: 당초 주장된 "400개 이상" 사이트는 267개 .onion 주소 / 27개 사이트로 수정되었다. 최초 과장의 사유는 불분명하다.
- **증거의 법적 유효성**: Tor 익명성 해제가 영장 없이 개발된 익스플로잇에 기초하였다면, 이로부터 파생된 증거의 증거능력은 다툼의 여지가 있을 수 있다. Benthall 사건에서 본 법적 쟁점의 해소는 널리 문서화되어 있지 않다.
- **Benthall 사건 결과**: Blake Benthall 체포 이후 사건의 최종 처리는 공개 보도가 제한적이다. 그의 답변 및 양형 결과는 입수 가능한 출처에 명확히 문서화되어 있지 않다.

## Follow-Up Actions

> [!warning] 공개 법원 문서 미발견
> 웹 검색(2026-04-17) 결과 본 작전에 대한 공개적으로 접근 가능한
> 법원 제출 서류가 발견되지 않았다. 가능한 사유: 공개 법원 기록 체계가
> 없는 미국 외 관할권, 비공개 절차, 또는 본 작전이 공식 기소로
> 이어지지 않았을 가능성.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2015-01-01: IOCTA 2015 — Darknets.
- Wikipedia, 2026-04-17: Operation Onymous.
- FBI, 2014-11-06: Operator of Silk Road 2.0 Website Charged in Manhattan Federal Court.
- ICE / HSI, 2014-11-06: International probe leads to the arrest of the alleged operator of "Silk Road 2.0".
- Swansea University, 2015-01-01: GDPO Situation Analysis — Operation Onymous.

## Evidence and Attribution Notes

- Operation Onymous(어나니머스 작전, FBI/Europol dark web takedown)는 2014년 11월 5-6일 FBI, Europol, Eurojust, 미국 국토안보부가 공동으로 수행한 국제 법집행 작전으로, Tor 네트워크상의 다크넷 마켓 및 기타 히든 서비스를 표적으로 삼았다.
- 본 작전을 통해 Silk Road 2.0, Cloud 9, Hydra를 포함한 27개 별개 웹사이트에 걸친 267개 .onion 주소를 압수하고, 17명을 체포하였으며, 약 100만 미국 달러 상당의 비트코인과 더불어 현금, 마약, 무기, 컴퓨터를 압수하였다.
- Silk Road 2.0의 운영자로 지목된 Blake Benthall(가명 "Defcon")은 샌프란시스코에서 체포되었다.
- 본 작전에는 17개 유럽 국가와 미국이 참여하였으며 당시 Tor 히든 서비스를 겨냥한 최대 규모의 공조 작전이었다.
- 그러나 Tor 히든 서비스 익명성 해제에 사용된 방법에 관하여, 특히 Carnegie Mellon University 연구진의 익스플로잇이 활용되었을 가능성에 대하여 상당한 논란이 발생하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인별 후속 조치가 아닌, Silk Road 2.0, Cloud 9, Hydra 및 기타 Tor 히든 서비스에 대한 단속을 기술하므로 정본 작전 페이지로 보존된다. 본 기록은 주관 책임을 FBI에, 조정 책임을 Europol EC3에 귀속시키며, 참여 또는 영향받은 관할권으로 미국, 영국, 불가리아, 체코, 핀란드, 프랑스, 독일, 헝가리, 아일랜드, 라트비아, 리투아니아, 룩셈부르크, 네덜란드, 루마니아, 스페인, 스웨덴, 스위스를 기록한다.

공조 모델은 명명된 기관 및 파트너를 통해 문서화된다: FBI, Europol EC3, Eurojust, 미국 국토안보부; 메커니즘: Joint Investigation Team, Mutual Legal Assistance, Informal Police-to-Police Cooperation; 법적 근거: Budapest Convention, U.s. Computer Fraud And Abuse Act, Eu Framework Decision 2005/222/jha On Attacks Against Information Systems; 집행 태세: 체포, 압수, 단속.

정본 기록을 위해 기재된 작전 결과: 17명 체포; 267개 도메인 압수; 암호화폐/자산 결과는 100만 미국 달러 상당 비트코인으로 기재; 27개 별개 사이트에 걸친 267개 .onion 주소 압수; Silk Road 2.0 폐쇄; Cloud 9 및 Hydra 마켓 폐쇄; 샌프란시스코에서 Blake Benthall(Silk Road 2.0 운영자) 체포.

정본 출처 세트는 5개의 참고문헌을 포함한다: [europol Iocta 2015 — Darknets](https://www.europol.europa.eu/iocta/2015/darknets.html), [wikipedia — Operation Onymous](https://en.wikipedia.org/wiki/operation Onymous), [fbi Press Release — Silk Road 2.0 Charged](https://www.fbi.gov/contact Us/field Offices/newyork/news/press Releases/operator Of Silk Road 2.0 Website Charged In Manhattan Federal Court), [ice Press Release — International Probe Leads To Arrest](https://www.ice.gov/news/releases/international Probe Leads Arrest Alleged Operator Silk Road 20), [gdpo Situation Analysis (jan 2015)](https://www.swansea.ac.uk/media/operation Onymous.pdf).
출처 하한선은 정본 작전 요건을 충족하나, 출처 폭만으로는 모든 하위 체포 또는 양형이 본 작전의 일부임을 입증하지는 않으므로, 후속 기록은 별도로 연결되어야 한다.
현재 본 페이지에 결손-필드 플래그(missing-field flags)는 부여되어 있지 않다.
데이터셋 활용을 위해, 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 공조된 집행 조치 전체를 기술한다. 이후의 기소, 답변, 양형, 인도, 몰수 조치는 출처가 명시적으로 새로운 다국가 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 첨부되어야 한다.
출처 기록이 더 광범위한 배경, 반복된 통신 서비스 재게시, 또는 주제 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실에 우선순위를 부여한다. 주변적인 출처 표제는 독립적인 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Silk Road 2.0 웹사이트 운영자, 맨해튼 연방법원 기소 | FBI | 2014-11-06 | https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/operator-of-silk-road-2.0-website-charged-in-manhattan-federal-court |
| [2] | "Silk Road 2.0"의 운영자로 지목된 인물의 체포로 이어진 국제 수사 | ICE / HSI | 2014-11-06 | https://www.ice.gov/news/releases/international-probe-leads-arrest-alleged-operator-silk-road-20 |
| [3] | GDPO 상황 분석 — Operation Onymous | Swansea University | 2015-01-01 | https://www.swansea.ac.uk/media/Operation-Onymous.pdf |
| [4] | Operation Onymous | Wikipedia | 2026-04-17 | https://en.wikipedia.org/wiki/Operation_Onymous |
