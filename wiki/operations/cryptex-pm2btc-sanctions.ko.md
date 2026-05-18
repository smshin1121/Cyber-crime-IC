> [!note] Source basis
> 본 페이지는 이제 미국 재무부 보도자료, FinCEN 자금세탁방지 조치, DOJ 형사 발표, EDVA 사건 발표, 그리고 독립적인 기술 분석을 단일 일반적인 "제재" 항목으로 통합하지 않고 분리하여 다룬다.

## 개요

2024년 9월 Cryptex 및 PM2BTC 조치는 미국의 제재, 자금세탁방지 규제, 형사 기소, 그리고 네덜란드의 인프라 압수를 결합한 것이다. 이러한 조치들은 미국 당국이 랜섬웨어 결제, 다크넷 활동, 그리고 광범위한 사이버범죄 자금에 연계된 것으로 판단한 러시아 가상화폐 자금세탁 생태계를 표적으로 하였다.

## Audit Note

본 페이지는 본 조치가 다국적이기 때문에 유지되지만, 제재, 형사 기소, 그리고 네덜란드 압수의 각 부분은 별도의 법적 계층이다. 이들은 의도적으로 단일한 일반적 단속 서사로 통합되지 않는다.

## 배경

### 수법(모더스 오페란디)
본 조치는 두 명의 명명된 피고에 의해 거의 20년에 걸쳐 주로 운영된 **중첩되는 러시아 가상화폐 자금세탁 서비스의 스택**을 표적으로 하였다. 주요 피고인 러시아 국적자 **세르게이 이바노프(Sergey Ivanov)**("Taleon")는 **UAPS, PinPays, PM2BTC**를 생성하고/하거나 운영한 것으로 주장되며, 이들은 배타적인 러시아어 사용 범죄 포럼에서 사이버범죄자들에게 명시적으로 광고된 결제 처리 및 암호화폐-법정통화 거래 서비스이다. 이바노프의 서비스는 KYC 없이 운영되었으며, **Rescator** 카딩 웹사이트(도용된 미국 결제 카드 데이터)와 **Joker's Stash**(역사상 최대 카딩 마켓플레이스(마켓플레이스) 중 하나), 그리고 랜섬웨어 운영자, 다크넷 마약 시장, 그리고 미국의 주요 기업 데이터 유출에 책임이 있는 해커들의 자금을 처리하였다. 두 번째 피고인 **티무르 샤크마메토프(Timur Shakhmametov)**("JokerStash" / "Vega")는 Joker's Stash 자체를 운영하고 그 수익을 이바노프 스택을 통해 자금세탁한 것으로 주장된다. 별도로, **Cryptex(Cryptex(암호화폐 거래소))**("Cryptex.net" / "Cryptex.one") 암호화폐 거래소는 KYC 준수 없이 "완전한 익명성"을 제공하며 사이버범죄자들에게 직접 광고하였다; Cryptex는 UAPS/PM2BTC와 구조적으로 인접해 있으며, 동일한 공조 조치에서 미국 비밀경호국의 도메인 압수와 네덜란드의 서버 압수를 통해 표적이 되었다.

### 피해자 프로파일 및 영향
피해자는 분석적으로 구별되는 두 부류로 분류되며, 본 사건은 2013년 이후 미국 사이버범죄 피해자 기반의 상당 부분에 걸쳐 있다:
- **직접적 카딩 사기 피해자**: Rescator와 Joker's Stash를 통해 결제 카드 데이터가 판매된 미국 금융 기관 카드 소지자. DOJ 보도자료는 **최대 4,000만 장의 결제 카드**와 **약 7,000만 명의 PII**가 도난되어 Rescator에서 판매를 위해 제공된 2013년 **주요 미국 소매업체 유출 피해자**를 구체적으로 식별한다. 그 단일 유출 사건은 해당 소매업체에게 최소 **2억 200만 달러(USD)**의 비용을 부담시켰으며, 약 7,000만 명의 고객을 후속 신원 도용 시도에 노출시켰다.
- **간접적 사이버범죄 피해자**: 그 수익이 이바노프의 서비스를 통해 흐른 랜섬웨어 결제 피해자 및 다크넷 마약 시장 고객. 이바노프 통제 주소로의 유입금 중 약 **1억 5,800만 달러(USD)**가 일반 사기 수익으로, 약 **880만 달러(USD)**가 **알려진 랜섬웨어 결제**로, 약 **470만 달러(USD)**가 **다크넷 마약 시장**에 귀속된다. Cryptex의 경우, 유입금 중 **2억 9,700만 달러(USD)**가 사기 수익으로, **1억 1,500만 달러(USD)**가 랜섬웨어 결제로 귀속된다(DOJ가 인용한 블록체인 분석에 따름).
- **규모**: Joker's Stash 자체만으로 연간 약 **4,000만 장의 결제 카드**를 제공한 것으로 추정되며, 누적 수익은 **2억 8,000만 달러(USD)에서 10억 달러(USD) 이상**으로 추산된다.

### 자금 흐름
- **이바노프 스택 처리량**: 이바노프의 자금세탁 서비스와 연관된 암호화폐 주소는 **2013년 7월 12일에서 2024년 8월 10일 사이**(DOJ가 인용한 추적 기간)에 약 **11억 5,000만 달러(USD)**를 이동시켰다. 추적된 모든 비트코인 유입 중 약 **32%**가 이미 범죄 활동과 연관된 주소에서 출처되었다 — 이는 일반적인 주류 거래소 기준선 대비 두드러지게 높은 불법 유입 비율이다.
- **Cryptex 처리량**: 약 **62,586 BTC**(거래 시점 가치 환산 시 약 **14억 달러(USD)**)를 포함하는 **37,500건 이상의 거래**. 유입금 중 약 **31%(4억 4,100만 달러(USD))**는 범죄 행위 주소에서 출처되었으며; 또 다른 **9%(1억 6,200만 달러(USD))**는 사이버범죄에 인접한 서비스 주소에서 왔다; 그리고 모든 유출의 **28%**는 이미 미국이 제재한 주체 또는 다크넷 시장으로 갔다.
- **결제 계층**: 카딩 사이트 구매에 대한 결제 처리는 UAPS / PinPays를 통한 비트코인으로 결제되었다; PM2BTC는 암호화폐-법정통화 출구 역할을 하였다; Cryptex는 KYC 없는 거래소 서비스를 제공하였다.
- **압수**: 네덜란드 파트너들은 PM2BTC와 Cryptex를 호스팅하는 서버를 압수하였다; 압수된 서버에서 **700만 달러(USD) 이상의 암호화폐**가 회수되었다. 미국 비밀경호국은 UAPS, PM2BTC, Cryptex.net/.one에 대해 도메인 압수를 집행하였다. OFAC(미국 해외자산통제국)는 Cryptex와 이바노프를 제재하였다; FinCEN은 PATRIOT Act § 311 권한 하에 PM2BTC를 주요 자금세탁 우려처(primary money-laundering concern)로 지정하였다.

### 범죄 조직 구조
본 사건은 더 광범위한 **러시아어 사용 범죄 포럼 생태계**에 내재된 **두 명의 피고가 운영하는 사이버 자금세탁 사업체**를 도식화한다:
- **세르게이 이바노프("Taleon")** — 거의 20년에 걸친 전문 사이버 자금세탁업자로서의 경력으로 주장됨; UAPS, PinPays, PM2BTC를 운영; 은행 사기 공모/방조(Rescator 지원) 및 자금세탁 공모(Joker's Stash 수익) 혐의의 주요 피고. 동부 버지니아 지방법원에서 기소됨. 미국 국무부는 이바노프, 샤크마메토프, 그리고 관련자의 체포 및/또는 유죄 판결로 이어지는 정보에 대해 결합 **1,100만 달러(USD)**까지의 보상을 제공하였다.
- **티무르 샤크마메토프("JokerStash" / "Vega")** — Joker's Stash의 운영자로 주장됨; 은행 사기 공모/방조, 액세스 디바이스 사기 공모, 그리고 자금세탁 공모 혐의로 기소됨.
- **고객 기반**: 2013년 이후 러시아어 사용 사이버범죄 경제 전반에서 활동하는 사이버범죄 마켓플레이스, 랜섬웨어 그룹, 그리고 주요 유출 사건 해커. 피고들은 폐쇄된 러시아어 사용 범죄 포럼에서 광고하였다.
- **Cryptex 운영자**: 공개 보도자료에 명명되지 않음; Cryptex는 EDVA 기소 대신 OFAC 제재와 비밀경호국 도메인 압수를 통해 병행 표적이 되었다.
- **구조**: 이는 위계적 OCG가 아닌 **서비스 계층 인프라 클러스터**이다 — 독립 운영자(이바노프, 샤크마메토프, Cryptex 운영자들)가 인접한 자금세탁 및 거래소 서비스를 운영하며 집합적으로 러시아어 사용 사이버범죄자들에게 중요한 자금세탁 기반을 구성하였다. 두 기소된 피고가 모두 러시아에 거주하기 때문에 단기 체포 및 범죄인 인도는 *매우 어려울 것이다(highly unlikely)*.

## 참여 당사자

### 미국 당국
- [[us-treasury|미국 재무부(Treasury)]]
- FinCEN
- OFAC(미국 해외자산통제국)
- [[us-doj|미국 법무부(DOJ)]]

### 외국 파트너
- [[netherlands-politie|네덜란드 국가경찰]]

## 법적 근거

공공 조치는 제재 및 자금세탁방지 권한을 형사 기소와 결합하였다. FinCEN의 PM2BTC 조치는 OFAC의 Cryptex 제재와 분석적으로 구별되며, DOJ/EDVA 보도자료는 그러한 금융 통제가 어떻게 혐의와 외국 압수 지원과 결합되었는지를 보여준다.

## 작전 타임라인

| 일자 | 사건 |
|------|-------|
| 2024-09-26 | 재무부가 Cryptex, PM2BTC, 그리고 관련 사이버범죄 금융 인프라를 표적으로 한 공조 조치를 발표. |
| 2024-09-26 | FinCEN이 PM2BTC를 주요 자금세탁 우려처로 식별하고 특별 조치를 제안. |
| 2024-09-26 | DOJ와 USAO EDVA가 두 명의 러시아 국적자에 대한 혐의를 발표하고 네덜란드 당국이 관련 서버를 압수하였다고 명시. |

## 결과 및 영향

| 지표 | 세부 사항 |
|--------|--------|
| 공개적으로 명명된 형사 피고 | 2명 |
| 공공 조치가 공개된 국가 | 2개국 |
| 압수된 암호화폐 | 700만 달러(USD) 이상 |
| 결합된 단속 도구 | 제재, AML 특별 조치, 기소, 그리고 서버 압수 |

## 활용된 협력 메커니즘

본 조치는 계층화된 금융 단속의 강력한 예시이다. 재무부와 FinCEN은 자금세탁 채널을 공격하였고, DOJ는 형사 사건 서사를 추가하였으며, 네덜란드 파트너들은 직접적인 인프라 비용을 부과하였다. 그 결합은 단일 단속 계층만 사용될 경우 사이버범죄 거래소가 빠르게 적응하기 때문에 중요하다.

## 모순점 및 미해결 문제

- 재무부와 DOJ 보도자료는 동일한 전체 조치를 상이한 기관 관점에서 기술하므로, 정확한 운영자 귀속은 단일 보도자료가 아닌 문서 전반에 걸쳐 읽어야 한다.
- 공공 보도자료들은 네덜란드 압수 인프라가 Cryptex와 PM2BTC 운영을 얼마나 오래 지원했는지를 완전히 공개하지 않았다.
- 러시아 사이버범죄 현금화 경로에 대한 장기 대체 효과는 여전히 불명확하다.

### L26 배경 누락 사항

> [!note] L26 gap — Cryptex operator identity
> Cryptex는 OFAC 지정 및 비밀경호국 도메인 압수를 통해 표적이 되지만, 공공 보도자료는 Cryptex 거래소의 자연인 운영자(들)를 명명하지 않는다. Cryptex가 이바노프에 의해 운영되는지, 이바노프 인접 관계자에 의해 운영되는지, 또는 구조적으로 별개의 러시아어 사용 행위자에 의해 운영되는지는 1차 출처(tier-1) 공개에서 불명확하다.

> [!note] L26 gap — direct-victim notification programme
> DOJ, 재무부, FinCEN, 또는 USAO-EDVA 보도자료 중 어느 것도 이바노프의 서비스를 통해 자금이 흐른 카드 소지자 또는 랜섬웨어 결제 피해자에 대한 피해자 통지 프로그램을 기술하지 않는다. 2013년 이후 추적 기간과 명명된 소매업체 유출 단독으로 노출된 약 7,000만 PII 기록을 고려할 때, 이 규모에서의 개별 피해자 통지는 *실행 불가능할 가능성이 높다(unlikely)*.

> [!note] L26 gap — Russian extradition prospects
> 이바노프와 샤크마메토프는 모두 러시아에 거주하는 것으로 보고된 러시아 국적자이며; 러시아-미국 협력 동결과 러시아-미국 범죄인 인도 조약의 부재로 인해 협력 관할권으로의 여행이 없는 한 단기 체포는 *매우 어려울 것이다(highly unlikely)*. 보도자료들은 추구 전략 또는 결석재판 경로를 다루지 않는다.

> [!note] L26 gap — victim cohort overlap with prior indictments
> Rescator 2013년 소매업체 유출 피해자는 업계 보도에 따라 Target Corporation으로 널리 이해되지만, DOJ 보도자료에는 명명되지 않는다; 본 작전 페이지는 이 귀속을 주장하지 않는다. 마찬가지로, 이바노프 기소와 이전의 Joker's Stash 테이크다운 활동(2021년 은퇴 공지) 간의 관계는 공공 보도자료에서 완전히 공개되지 않는다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- U.S. Department of the Treasury, 2024-09-26: Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitator.
- US Department of Justice, 2024-09-26: Two Russian Nationals Charged in Connection with Operating Billion Dollar Money Laundering Services.
- Financial Crimes Enforcement Network, 2024-09-26: Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitator.
- Financial Crimes Enforcement Network, 2024-09-26: Imposition of Special Measure Prohibiting the Transmittal of Funds Involving PM2BTC.
- U.S. Attorney's Office, Eastern District of Virginia, 2024-09-26: Two Russian nationals charged in connection with operating billion-dollar money laundering services; Justice Department seizes web domains for..
- Chainalysis, 2024-09-26: OFAC Designates Russian Exchange Cryptex, FinCEN names PM2BTC.

## Evidence and Attribution Notes

- Treasury identified PM2BTC as a primary money laundering concern and sanctioned Cryptex.
- The action was described as part of a coordinated international effort against Russian cybercrime services.
- Treasury linked Cryptex to ransomware-related and broader cybercriminal financial flows.
- This is the lead Treasury announcement for the September 2024 Cryptex and PM2BTC action.
- This DOJ release complements the Treasury sanctions announcement by documenting the related enforcement action.
- FinCEN identified PM2BTC as a primary money laundering concern and framed the move as part of a coordinated international action.
- The release tied PM2BTC to Russian illicit finance and cybercrime services.
- This FinCEN release is the cleanest U.S. financial-regulatory source for the PM2BTC portion of the September 2024 action.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- U.S. Department of the Treasury, 2024-09-26: Department of the Treasury About Treasury Enter Search Term(s): Advanced Search General Information Role of the Treasury Officials Organizational Chart Orders and Directives Offices Domestic Finance Economic Policy General Counsel International Affairs Management Public Affairs Tax Policy Terrorism and Financial Intelligence Tribal and.
- U.S. Department of Justice, 2024-09-26: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs Two Russian Nationals Charged In Connection With Operating Billion Dollar Money Laundering Services This is archived content from the U.S.
- U.S. Department of Justice, 2024-09-26: The actions involved the unsealing of an indictment charging a Russian national with his involvement in operating multiple money laundering services that catered to cybercriminals, as well as the seizure of websites associated with three illicit cryptocurrency exchanges.
- U.S. Attorney's Office, Eastern District of Virginia, 2024-09-26: Attorney Criminal Civil Services & Programs Victim Witness Assistance Project Safe Neighborhoods Reentry Program Report a Crime Find a Court Document Locate An Inmate Whistleblower Non-Prosecution Pilot Program ## Extraction Notes - parser: document - fetcher: doj_fetch - fetched_at: 2026-04-25T14:18:37+00:00 - final_url:

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고 특정 후속 조치가 아닌 Cryptex 거래소, PM2BTC, 그리고 사이버범죄에 연계된 가상화폐 자금세탁 네트워크의 운영자에 대한 인프라 압수를 기술하기 때문에 표준 작전(canonical operation)으로 유지된다. 본 기록은 주도 책임을 Us Treasury에, 조정을 Us Treasury에 귀속시키며, 참여 또는 영향을 받는 관할권은 United States와 Netherlands로 기록된다.

협력 모델은 명명된 기관 및 파트너를 통해 문서화된다: Us Treasury, Us Doj, Netherlands Politie; 단속 자세: Sanction, Seizure, Indictment.

표준 기록에 포착된 작전 결과: 기소 2건; 암호화폐/자산 결과는 USD 700만 달러 이상으로 기록됨; FinCEN이 PM2BTC를 주요 자금세탁 우려처로 지정함; OFAC가 Cryptex와 관련 인프라를 제재함; 네덜란드 당국이 Cryptex와 PM2BTC와 연관된 서버를 압수함.

표준 출처 집합은 6개의 참고자료를 포함한다: 2024 09 26 Treasury Cryptex Pm2btc Coordinated Actions, 2024 09 26 Justice Gov Two Russian Nationals Charged Money Laundering Services, 2024 09 26 Fincen Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency, 2024 09 26 Fincen Imposition Special Measure Prohibiting The Transmittal Of Funds Involving Pm2btc, 2024 09 26 Usao Edva Two Russian Nationals Charged Connection Operating Billion Dollar Money Laundering, 2024 09 26 Chainalysis Ofac Designates Russian Exchange Cryptex Fincen Names Pm2btc.
출처 기준은 표준 작전을 충족하지만, 출처의 폭만으로는 모든 후속 체포 또는 선고가 본 작전의 일부임을 증명하지 않는다; 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 보유한 알려진 메타데이터 누락: Legal Basis 및 Mechanisms Used.
데이터셋 사용을 위해 본 페이지는 작전 수준 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 공조 단속 조치 전체를 기술한다. 이후의 기소, 답변, 선고, 범죄인 인도 또는 몰수 조치는 출처가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 첨부되어야 한다.
출처 기록이 더 광범위한 배경, 반복된 통신사 재발행, 또는 주제 페이지 자료를 포함할 때, 본 평가는 명명된 작전, 그 참여 당국, 그 표적 인프라 또는 범죄 서비스, 그리고 그 측정 가능한 단속 결과와 직접 연관된 사실에 우선순위를 둔다. 주변적인 출처 제목은 독립적인 분류 체계 또는 결과 증거로 취급되지 않는다.
이는 표준 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행처 | 일자 | URL |
|---|-------|----------|------|-----|
| [1] | Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitator | U.S. Department of the Treasury | 2024-09-26 | https://home.treasury.gov/news/press-releases/jy2616 |
| [2] | Two Russian Nationals Charged in Connection with Operating Billion Dollar Money Laundering Services | U.S. Department of Justice | 2024-09-26 | https://www.justice.gov/archives/opa/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering-1 |
| [3] | Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency | Financial Crimes Enforcement Network | 2024-09-26 | https://www.fincen.gov/news/news-releases/treasury-takes-coordinated-actions-against-illicit-russian-virtual-currency |
| [4] | Imposition of Special Measure Prohibiting the Transmittal of Funds Involving PM2BTC | Financial Crimes Enforcement Network | 2024-09-26 | https://www.fincen.gov/resources/statutes-regulations/federal-register-notices/imposition-special-measure-prohibiting-0 |
| [5] | Two Russian Nationals Charged in Connection with Operating Billion-Dollar Money Laundering Services | USAO Eastern District of Virginia | 2024-09-26 | https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering |
| [6] | OFAC Designates Russian Exchange Cryptex and FinCEN Names PM2BTC | Chainalysis | 2024-09-26 | https://www.chainalysis.com/blog/ofac-sanctions-russian-exchange-cryptex-uaps-fraud-shop-2024/ |
