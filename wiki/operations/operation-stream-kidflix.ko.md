> [!note] Source basis
> 본 페이지는 현재 Europol(유럽 경찰청)을 중심으로 수집된 출처 래퍼, Security Affairs 요약본, 그리고 네덜란드 측 서버 조치를 공식적으로 확인한 네덜란드 경찰의 공식 페이지에 기반하고 있다. 본 페이지는 명백한 국경 간 관련성을 가지면서도 참고문헌 섹션을 결여하고 있던, 인코딩이 손상된 기존 초안을 대체한다.

## 개요

**Operation Stream**(스트림 작전, Kidflix CSAM takedown)은 독일이 주도하고 [[europol-ec3|Europol]]이 조정한 작전으로서, 다크웹의 대형 아동 성착취물 스트리밍 플랫폼인 **Kidflix**를 해체하였다. 공개된 기록은 2022년부터 2025년 3월까지 진행된 장기 수사, [[netherlands|네덜란드]]에서의 서버 다운, 그리고 해당 플랫폼의 자금 및 호스팅 인프라와 결부된 전 세계적 용의자 식별 및 검거를 뒷받침한다.

## 배경

### Modus operandi

Kidflix는 2021년부터 다크웹에서 *스트리밍 지향형* CSAM(아동 성착취물) 플랫폼으로 운영되어 왔으며, 이는 과거 Europol(유럽 경찰청)의 단속에서 주로 등장하였던 기존의 다운로드 및 포럼형 CSAM 플랫폼과는 구조적으로 구별되는 모델이다. Bavarian State Criminal Police(BLKA, 바이에른 주 형사경찰)와 Bavarian Central Office for the Prosecution of Cybercrime(ZCB, 바이에른 사이버범죄 수사 중앙청)은 Kidflix를 합법적인 성인 콘텐츠 스트리밍 플랫폼을 모델로 한 고처리량 영상 스트리밍 서비스로 규정하였으며, 카테고리별 탐색, 사용자 계정, 연속 재생 기능을 갖추고 있었다. 해당 플랫폼은 암호화폐 기반 구독/토큰 시스템을 통하여 접근권을 수익화하였다. 즉, 사용자는 토큰(주로 비트코인 및 기타 암호화폐)을 구매하여 시청 시간, 프리미엄 카테고리에 대한 접근권 및 영상 다운로드 권한을 얻었다. 업로더는 자신이 업로드한 콘텐츠가 발생시킨 조회수 및 다운로드 수에 비례하여 토큰 보상을 지급받았으며, 이는 신규 CSAM의 모집 및 공급에 대한 직접적인 경제적 유인을 창출하였다. 단속 시점까지 해당 플랫폼의 라이브러리에는 네덜란드에 위치한 단일 대용량 서버에 호스팅된 약 **72,000개의 영상**이 보관되어 있었다. 카탈로그는 기존 CSAM 저장소로부터의 큐레이션된 일괄 임포트가 아니라, 토큰 보상 체계에 의하여 유인된 사용자 업로드를 통하여 확장되었다.

### Victim profile and impact

피해자는 해당 플랫폼을 통하여 유포된 CSAM 콘텐츠에 등장한 아동들이다. Europol(유럽 경찰청)의 발표에 따르면, 본 작전은 직접적으로 **39명의 아동**의 안전을 확보하는 결과를 도출하였다. 이는 학대가 진행 중이거나 최근 발생한 아동들로서, Kidflix 증거에서 도출된 수사 단서를 통하여 신원이 확인되고, 위치가 파악되어, 유해한 상황으로부터 분리될 수 있었던 아동을 의미한다. 해당 플랫폼의 영향 범위는 전 지구적이었으며, **전 세계적으로 180만 명의 등록 사용자**가 계정에 접근하였고, 플랫폼 이용 데이터, 결제 추적 기록 및 업로더 기록을 토대로 35개국 이상에서 **1,393명의 용의자가 식별**되었다. 따라서 피해는 두 가지 차원에서 작동한다. 즉, (a) 영상에 등장한 아동에 대한 1차 피해(39명의 안전 확보가 확인되었으며, 영상에 등장한 아동들 중 아직 신원이 확인되지 아니한 미지의 더 큰 모집단이 존재함), 및 (b) 스트리밍 모델에 관여한 180만 개의 계정이 야기한 수요 측면의 정상화 효과이다.

### Financial flow

Kidflix는 사용자에서 플랫폼, 다시 업로더로 이어지는 결제 사슬 전반에 걸쳐 암호화폐 결제망을 이용하였다. 사용자는 플랫폼 내 충전 흐름을 통하여 비트코인 및 기타 암호화폐로 시청 토큰을 구매하였고, 플랫폼은 운영자 통제하의 지갑에 통합된 암호화폐 잔고를 보유하였으며, 업로더에 대한 지급 또한 암호화폐로 이루어졌다. TRM Labs 및 Chainalysis 방식의 블록체인 분석(Security Affairs / TRM Labs 보도를 통하여 참조됨)은 운영자 및 고가치 사용자의 상당 부분을 식별한 다년간의 금융 추적을 뒷받침하였다. 구체적인 암호화폐 압수 금액은 공개 기록에서 **미공개**로 기록되어 있다. Europol(유럽 경찰청) 및 네덜란드 경찰의 보도자료는 금융 추적이 용의자 식별의 핵심이었다고 기술하면서도, 압수된 BTC/ETH 또는 USD 환산 총액을 공표하지 아니하였다. 따라서 프런트매터는 수치 대신 `cryptocurrency_seized: undisclosed`로 기재되어 있다.

**Criminal organisation structure.** Kidflix 운영자 그룹은 공개 기록상 스트리밍 인프라를 운용하는 소규모 운영 코어, 그리고 토큰 보상의 대가로 CSAM을 업로드하는 다수의 "업로더" 계층(유인된 사용자), 그리고 수동적인 유료 시청자 계층(180만 개 계정)으로 구성된 것으로 기술되어 있다. 따라서 Operation Stream(스트림 작전, Kidflix CSAM takedown)에서 기록된 79건의 검거는 세 계층 전반에 걸쳐 있다. 즉, (a) 플랫폼 운영자(소수), (b) 다작 업로더(중간 규모), (c) 소지 또는 제작 기록이 확인된 고관여 유료 시청자/사용자(다수)이다. 세 계층 사이의 정확한 분포는 공표되지 아니하였다. Europol(유럽 경찰청)의 발표는 운영자 코어가 위계적 지휘 구조를 갖춘 명명된 OCG(조직범죄단)를 구성한다고 단정하지 아니하며, 해당 모델은 전통적인 조직범죄 위계 구조보다는 소규모 운영팀이 운영하는 "영리형 다크넷 서비스"에 더 가깝다.

**Cross-border investigative cooperation**는 독일(BLKA 및 ZCB)이 주도하였으며, 네덜란드 국가경찰이 독일의 요청에 따라 **2025-03-11**자로 물리적인 서버 다운 조치를 집행하였다. 약 72,000개의 영상을 호스팅하던 서버는 물리적으로 네덜란드 관할권 내에 위치하고 있었다. Europol(유럽 경찰청)은 EC3 채널을 통하여 35개국 이상의 국가 법집행 파트너에게 용의자 식별 결과를 배포·조정하였다.

## 참여 당사자

### Lead / Coordination
- [[germany-bka|바이에른 주 형사경찰 및 바이에른 사이버범죄 검찰]]
- [[europol-ec3|Europol EC3]]

### Confirmed Cross-Border Operational Role
- [[netherlands-politie|네덜란드 국가경찰]]

### Wider International Scope
- Europol(유럽 경찰청) 연계 보도는 35개국 이상이 관여하였다고 진술한다.

## 결과 및 영향

| Metric | Detail |
|--------|--------|
| 검거 | 79건 |
| 식별된 용의자 | 1,393명 |
| 압수된 기기 | 3,000점 이상 |
| 보호된 아동 | 39명 |
| 등록 사용자 | 180만 명 |
| 압수 서버상 영상 수 | 약 72,000개 |

## Cooperation Mechanisms Used

공개 기록은 Europol(유럽 경찰청) 조정, 독일 주도 수사, 네덜란드의 인프라 조치를 중심으로 하는 장기 다국적 수사 모델을 뒷받침한다. 출처들은 또한 거래소 및 관련 서비스를 거치는 암호화폐 거래의 국제적 금융 추적이 있었음을 시사하나, 모든 국가에 대한 법적 도구의 전모를 공개하지는 아니한다.

## Contradictions & Open Questions

- 공개 출처들은 전반적 결과에 대하여는 일치하나, 35개국 이상에 달하는 참여 국가의 완전한 목록은 제공하지 아니한다.
- 압수된 서버의 정확한 수량은 공개적으로 완전히 분개되어 있지 아니하며, 현 시점의 공개 보도는 최소한 네덜란드 호스팅 서버에 대한 조치를 명확히 뒷받침한다.
- 식별된 사용자에 대한 법원 단계의 사건 진행 상황은 대부분 비공개 상태이다.
- **암호화폐 압수 총액은 미공개이다.** Europol(유럽 경찰청), 네덜란드 경찰 및 BLKA는 암호화폐 추적이 용의자 식별의 핵심이었다고 기술하면서도 압수 자금의 수치를 공표하지 아니한다. 프런트매터는 수치 대신 `cryptocurrency_seized: undisclosed`로 기재되어 있다.
- **79건의 검거에 대한 운영자/업로더/시청자 계층별 분포는 공표되지 아니하였다.** 1차 출처는 헤드라인 수준의 검거 건수 및 전 세계적으로 식별된 1,393명의 용의자를 명시하나, 검거 중 어느 정도가 운영자, 다작 업로더, 또는 유료 시청자를 표적으로 하였는지는 분개하지 아니한다.
- **선도적 역할을 한 독일 및 네덜란드 외의 국가별 검거 분포**는 공표되지 아니하였다. 79건의 검거는 35개국 이상에 걸쳐 이루어졌으나, 공식 성명에서 명명된 수사 역할이 부여된 국가는 독일 및 네덜란드에 한정된다.
- **확인된 39명의 안전 확보 아동을 초과하는 전체 식별 아동 모집단**은 공표되지 아니하였다. 압수된 라이브러리 내 약 72,000개의 영상 전부가 피해자 식별 목적으로 처리되었는지, 또는 처리가 진행 중인지 여부는 명시되어 있지 아니하다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol / Security Affairs / TRM Labs, 2025-04-04: Europol 주도 Operation Stream, Kidflix CSAM 플랫폼 다운.
- Security Affairs / TRM Labs, 2025-04-04: Operation Stream / Kidflix.
- 네덜란드 국가경찰, 2025-04-03: 아동음란물 플랫폼 KidFlix 오프라인 조치.
- Security Affairs / TRM Labs, 2025-04-04: Europol 주도 Operation Stream, Kidflix CSAM 플랫폼 다운.
- BleepingComputer, 2025-04-02: 경찰, KidFlix 아동 성착취 플랫폼 폐쇄.
- eucrim, 2025-05-15: 소아성애 플랫폼 'Kidflix' 폐쇄.

## Operational Timeline

- 2022-01-01: 활동 또는 수사 개시.
- 2025-04-04: 공개 발표.
- 2025-03-11: 보고된 집행 종료 시점.
- 2025-04-02: BleepingComputer의 공개 출처 보도.
- 2025-04-03: 네덜란드 국가경찰의 공개 출처 보도.
- 2025-04-04: Europol / Security Affairs / TRM Labs, Security Affairs / TRM Labs의 공개 출처 보도.
- 2025-05-15: eucrim의 공개 출처 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: CSAM(아동 성착취물).
- 기록된 집행 태세: Takedown, Seizure, Arrest.
- 본 기록은 status completed의 takedown으로 분류된다.

## Evidence and Attribution Notes

- Operation Stream(스트림 작전, Kidflix CSAM takedown) — Kidflix CSAM 플랫폼 다운. "Operation Stream"이라 명명된 국제 법집행 작전은 다크웹상의 최대 규모 CSAM(아동 성착취물) 스트리밍 플랫폼 중 하나인 Kidflix를 해체하였다.
- 본 작전은 Bavarian State Criminal Police(Bayerisches Landeskriminalamt, 바이에른 주 형사경찰)와 Bavarian Central Office for the Prosecution of Cybercrime(ZCB, 바이에른 사이버범죄 수사 중앙청)이 주도하였으며, 35개국에 걸쳐 Europol(유럽 경찰청)이 조정하였다.
- **Platform: "** Kidflix — 2021년부터 운영된 CSAM 스트리밍 플랫폼"
- "Operation Stream"이라 명명된 국제 법집행 작전은 다크웹상의 최대 규모 CSAM(아동 성착취물) 스트리밍 플랫폼 중 하나인 Kidflix를 해체하였다.
- ic-statistics-dashboard에 의하여 참조된 출처.
- 네덜란드 경찰은 2025년 3월 11일자로 독일의 요청에 따라 네덜란드 기반 서버 조치가 이루어졌음을 확인한다.
- 해당 발표는 플랫폼이 약 180만 명의 사용자를 보유하였으며 전 세계적으로 1,400명 이상의 사용자가 식별되었음을 확인한다.
- **Operation Stream**(스트림 작전, Kidflix CSAM takedown)은 독일이 주도하고 Europol(유럽 경찰청)이 조정한 작전으로서, 다크웹의 주요 아동 성착취물 스트리밍 플랫폼인 **Kidflix**를 해체하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라, 다크웹의 대형 아동 성착취물 스트리밍 플랫폼인 Kidflix에 대한 다운 조치를 기술하므로, 정본 작전으로서 유지된다. 본 기록은 주도 책임을 Bavarian State Criminal Police(바이에른 주 형사경찰)에 귀속시키고, 조정 책임을 Europol Ec3(유럽 경찰청 EC3)에 귀속시키며, 참여 또는 영향을 받은 관할권은 독일 및 네덜란드로 기록한다.

협력 모델은 명명된 기관 및 파트너를 통하여 문서화된다. 즉, Germany Bka(독일 BKA, 독일 연방수사청), Europol Ec3(유럽 경찰청 EC3), Netherlands Politie(네덜란드 경찰); mechanisms: informal cooperation; enforcement posture: Takedown, Seizure, Arrest.

정본 기록에 포착된 작전 결과: 검거 79건; 압수 서버 1대; 통보 피해자 39명; 암호화폐/자산 결과는 미공개로 기록; 전 세계적으로 1,393명의 용의자가 식별됨; 3,000점 이상의 전자기기가 압수됨; 해당 플랫폼은 180만 명의 등록 사용자를 보유하였음.

정본 출처 집합은 6건의 참고자료를 포함한다: 2025 04 04 Europol Operation Stream Kidflix Takedown, 2025 04 04 Securityaffairs Com Operation Stream Kidflix, 2025 04 03 Politie Nl Kidflix Offline Gehaald, 2025 04 04 Europol Operation Stream Kidflix, 2025 04 02 Bleepingcomputer Com Police Shuts Down Kidflix Child Sexual Exploitation Platform, 2025 05 15 Eucrim Pedophile Platform Kidflix Shut Down.
출처 하한선은 정본 작전 요건을 충족하나, 출처의 광범위함만으로는 모든 하위 단계의 검거 또는 양형이 본 작전의 일부임을 입증하지는 아니한다. 후속 기록은 별도 연계 상태로 유지되어야 한다.
본 페이지에는 현재 어떠한 프런트매터의 누락 필드 플래그도 기재되어 있지 아니하다.
데이터셋 활용 시, 본 페이지는 작전 단위의 집계 지점으로 취급되어야 한다. 즉, 국가, 기관, 메커니즘 및 결과 필드는 조정된 집행 조치 전체를 기술한다. 후속 기소, 답변, 양형, 인도 또는 몰수 조치는, 출처가 이를 새로운 다국적 작전으로 명시적으로 제시하지 아니하는 한, 관련 사건 또는 흡수된 후속 기록으로 부착되어야 한다.
출처 기록이 보다 광범위한 배경, 반복되는 통신사 재게재 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 기관, 그 표적 인프라 또는 범죄 서비스, 그리고 그 측정 가능한 집행 성과에 직접 결부된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류 또는 결과 증거로 취급되지 아니한다.
이로써 정본 기록은 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol 주도 Operation Stream, Kidflix CSAM 플랫폼 다운 | Security Affairs | 2025-04-04 | https://securityaffairs.com/176154/cyber-crime/europol-led-op-shuts-down-csam-platform-kidflix.html |
| [2] | Operation Stream / Kidflix | Security Affairs / TRM Labs | 2025-04-04 | https://securityaffairs.com/176270/cyber-crime/operation-stream-kidflix-takedown.html |
| [3] | 아동음란물 플랫폼 KidFlix 오프라인 조치 | Dutch National Police | 2025-04-03 | https://www.politie.nl/nieuws/2025/april/2/11-kinderpornografisch-platform-kidflix-offline-gehaald.html |
| [4] | 경찰, KidFlix 아동 성착취 플랫폼 폐쇄 | BleepingComputer | 2025-04-02 | https://www.bleepingcomputer.com/news/security/police-shuts-down-kidflix-child-sexual-exploitation-platform/ |
| [5] | 소아성애 플랫폼 'Kidflix' 폐쇄 | eucrim | 2025-05-15 | https://eucrim.eu/news/pedophile-platform-kidflix-shut-down/ |
