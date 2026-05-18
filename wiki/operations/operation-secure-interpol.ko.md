## 개요

Operation Secure(시큐어 작전, INTERPOL infostealer)는 INTERPOL(국제형사경찰기구)이 주도하여 2025년 1월부터 4월까지 아시아·태평양 26개국에 걸쳐 수행된 작전으로, 인포스틸러(infostealer) 악성코드 인프라를 표적으로 삼았다. 본 작전은 32명 체포, 2만 개 이상의 악성 IP 및 도메인 차단, 41대의 서버와 100GB 이상의 데이터 압수, 21만 6,000명 이상의 피해자에 대한 통지로 이어졌다.

본 작전은 감염된 시스템에서 자격증명, 금융 데이터 및 개인정보를 수집하는 정보탈취형 악성코드(인포스틸러)에 특화되었다. Group-IB, Kaspersky, Trend Micro로부터의 민간 부문 인텔리전스가 본 작전을 지원하였다.

> [!note] Naming disambiguation
> 본 작전은 유럽평의회(Council of Europe)의 역량 강화 훈련 프로그램인 "Operation SECURE"(Excel 데이터 6행)와 혼동되어서는 안 된다. 후자는 훈련 프로그램이며, 집행 작전이 아니다.

## 배경

### Modus operandi

Operation Secure(시큐어 작전, INTERPOL infostealer)는 인포스틸러-악성코드 영역, 즉 피해자 엔드포인트(일반적으로 피싱, 크랙 소프트웨어 미끼, 악성 광고, 드라이브-바이 다운로드를 통해)를 감염시킨 뒤 브라우저 저장 자격증명, 브라우저 쿠키 및 세션 토큰, 자동완성 데이터, 암호화폐 지갑 시드, 이메일 계정 자격증명, 로컬 캐시 문서 및 양식 데이터를 공격자 통제하의 명령제어(C2) 서버로 유출하는 정보탈취형 트로이목마를 표적으로 삼았다. 수집된 자격증명 묶음("로그")은 이후 사이버범죄 마켓플레이스에서 초기접근중개(Initial Access Broker, IAB) 재고로 재판매되어 랜섬웨어, 비즈니스 이메일 침해, 계정 탈취, 암호자산 절도 파이프라인에 공급된다. 인용된 1차 출처(INTERPOL) 보도자료는 특정 악성코드 패밀리를 명시하지 않으나, Kaspersky의 같은 날 지원 발표는 본 위키가 [[operation-magnus-redline-meta-stealer-takedown-2024|Operation Magnus]] 및 관련 조치 하에 별도로 추적하는 Lumma / Redline / Meta / Risepro 인포스틸러 패밀리 생태계 전반에 본 작전을 위치시킨다.

본 작전은 최종 사용자 기기보다 인프라 계층 자산을 타격하였다: 2만 개 이상의 악성 IP와 도메인이 차단되었고, 41대의 서버가 압수되었으며, 100GB 이상의 데이터가 증거로 확보되었다. 본 조치는 (실시간 유출 세션을 위한) C2 인프라와 인포스틸러 로그가 판매되는 재판매 플랫폼 인프라 모두를 표적으로 삼았다.

### Victim profile and impact

INTERPOL은 본 작전을 통해 21만 6,000명 이상의 피해자에게 통지가 이루어졌다고 보고한다. 인용된 보도자료는 피해자를 국가별, 수집된 자격증명의 언어별 또는 하위 사기 피해액별로 세분화하지 않는다. 아시아·태평양 작전 영역(26개 관할권)을 감안할 때, 자격증명 모집단은 본 위키 다른 곳에서 추적되는 음성 피싱, 로맨스 스캠, 계정 탈취 수법의 상류 공급원이 되는 한국 거주자의 자격증명을 포함하여 아시아·태평양 지역 사용자에 상당히 편중되었을 가능성이 높다. 통지된 피해자 코호트 전반의 종합 사기 손실액은 인용 출처에서 정량화되지 않는다.

### Financial flow

인포스틸러 경제의 수익금은 주로 다음 경로로 흐른다:

1. 로그별 판매 (Russian Market, 2easy, Genesis 유사 플랫폼 등 재판매 마켓플레이스에서 자격증명 묶음당 일반적으로 1~25 USD),
2. 기업 자격증명 묶음의 IAB 재판매를 통한 랜섬웨어 운영자로의 공급 (랜섬 1건당 5~7자리 수익화 가능), 그리고
3. 수집된 암호화폐 지갑 시드 및 거래소 계정 자격증명의 직접 수익화.

인용된 INTERPOL 보도자료는 Operation Secure(시큐어 작전, INTERPOL infostealer)에 대한 암호화폐 압수 수치를 기록하지 않으며, 수익화 채널별로 수익금을 분리하지 않는다. 압수된 100GB의 데이터는 증거이며 세탁된 수익금이 아니다.

### Criminal organization structure

32명의 체포는 26개국 명단 전반의 코호트 합계로 보고되며, 인용된 1차 출처는 특정 OCG(조직범죄단), 악성코드 패밀리 운영자, 마켓플레이스 관리자 또는 국가별 체포 내역을 명시하지 않는다. 인포스틸러 생태계는 일반적으로 — 스틸러 빌드를 판매하는 서비스형 악성코드(MaaS) 운영자, 스팸/피싱 캠페인을 운영하는 제휴 배포자, 로그 집계 마켓플레이스, 하위 IAB 재판매업자 — 가 느슨하게 연합된 제휴 구조로 구성되며, 통합된 위계구조가 아니다. 보도자료는 32명의 체포자가 어느 계층 또는 역할에 속하는지, 그들이 MaaS 운영자, 인프라 제공자, 로그 재판매자를 포함하는지 여부를 공개하지 않는다.

인포스틸러는 랜섬웨어, 사기 및 신원 도용 작전의 초기 접근 벡터 역할을 한다. INTERPOL의 아시아·남태평양 사이버범죄 작전 데스크는 [[operation-synergia-ii|Operation Synergia II]] 모델의 대규모 인프라 takedown(차단·압수)의 후속으로서 본 권역 단속을 조정하였다.

## 참여 당사자

### Law Enforcement
- **주도(Lead)**: [[interpol-igci|INTERPOL]] (아시아·남태평양 사이버범죄 작전 데스크)
- **INTERPOL이 보고한 26개국 아시아·태평양 연합**: 브루나이, 캄보디아, 피지, 홍콩(중국), 인도, 인도네시아, 일본, 카자흐스탄, 키리바시, [[south-korea|한국]], 라오스, 마카오(중국), 말레이시아, 몰디브, 나우루, 네팔, 파푸아뉴기니, 필리핀, 사모아, 싱가포르, 솔로몬제도, 스리랑카, 태국, 동티모르, 통가, 바누아투, 베트남. INTERPOL은 본 노력을 26개국 규모로 표기하며, 공개 명단에는 여러 영토/지역이 포함되어 있어 국가 페이지 메타데이터는 기존 국가 기록이 있는 부분집합만을 추적하는 한편 공식 공개 명단 전체는 본문에 보존된다.

### Private Sector Partners
- Group-IB
- Kaspersky
- Trend Micro

## 결과 및 영향

| 지표 | 값 |
|--------|-------|
| 체포 | 32명 |
| 압수 서버 | 41대 |
| 차단된 악성 IP/도메인 | 20,000개 이상 |
| 압수 데이터 | 100GB 이상 |
| 통지된 피해자 | 216,000명 이상 |
| 국가 | 26개국 |

## Cooperation Mechanisms Used

> [!warning] Missing data
> 구체적 법적 근거 및 협력 메커니즘은 가용 출처에서 상세화되어 있지 않다. INTERPOL I-24/7 네트워크 및 양자 협력 협정일 가능성이 높다.

## Korean Involvement (한국의 참여)

한국(대한민국)은 INTERPOL의 2025-06-11 발표문에서 Operation Secure(시큐어 작전, INTERPOL infostealer)의 26개 아시아·태평양 협력 관할권 중 하나로 명문으로 명시되었다. 인용된 1차 출처는 어느 한국 기관 또는 작전 단위가 참여했는지, 차단 조치에 의해 영향을 받은 한국 인포스틸러 인프라 자산의 수가 얼마인지, 21만 6,000명 이상의 통지된 피해자 중 한국 거주자의 비율이 어느 정도인지에 대해 세분화하지 않는다. 한국 측 조정 채널로는 [[knpa|대한민국 경찰청(KNPA)]] 및 [[knpa-cyber-bureau|경찰청 사이버수사국]]이 유력하며, 이는 INTERPOL 조정 사이버 작전 및 Operation Secure(시큐어 작전, INTERPOL infostealer)가 조직된 아시아·남태평양 사이버범죄 공동작전(ASPJOC) 프로젝트의 통상적인 한국 측 연락 지점이다.

본 사례는 인포스틸러로부터 도출된 자격증명이 본 위키 다른 곳에서 추적되는 한국 음성 피싱, 로맨스 스캠, 계정 탈취 수법의 반복적인 상류 공급원임을 감안할 때, 한국에 있어 인포스틸러-국제공조의 강력한 데이터 포인트이다.

## Contradictions & Open Questions

- 국가별 체포 및 인프라 조치 내역은 인용된 1차 출처에서 공개되지 않는다. 32명 체포, 41대 서버, 100GB 이상의 압수 데이터, 2만 개 이상의 차단된 IP/도메인은 코호트 합계로 보고된다.
- **L26 결여 — modus operandi 구체성**: 인용된 INTERPOL 보도자료는 표적이 된 특정 악성코드 패밀리(Lumma, RedLine, Meta, RisePro, Raccoon, Vidar 등)를 명시하지 않으며, 본 작전은 "인포스틸러 인프라" 추상화 수준에서만 기술된다.
- **L26 결여 — 자금 흐름**: 인용된 보도자료는 인포스틸러 로그 재판매 수익, IAB 하위 수익화, 또는 압수된 인프라를 통해 공급된 로그에 추적 가능한 종합 랜섬웨어 귀속 손실을 정량화하지 않는다.
- **L26 결여 — OCG 구조**: 32명의 체포자의 역할(MaaS 운영자 / 인프라 제공자 / 마켓플레이스 관리자 / 제휴 배포자)은 공개되지 않으며, 32명 체포 코호트가 조정된 OCG를 대표하는지 또는 26개 관할권 전반의 독립 행위자들인지는 명시되지 않는다.
- **L26 결여 — 피해자 정량화**: 관할권별 피해자 내역, 수집된 자격증명의 언어/지역, 21만 6,000명 이상의 통지된 모집단 전반의 하위 사기 손실 합계는 공개되지 않는다.
- 위키 기록의 `participating_countries` 프론트매터는 현재 INTERPOL 26개국 명단 중 본 위키에 기존 국가 페이지가 있는 19개 관할권을 포착한다: 브루나이, 캄보디아, 홍콩, 인도, 인도네시아, 일본, 카자흐스탄, 라오스, 마카오, 말레이시아, 몰디브, 네팔, 필리핀, 한국, 싱가포르, 스리랑카, 태국, 동티모르, 베트남. 나머지 7개 출처 명시 관할권 — 피지, 키리바시, 나우루, 파푸아뉴기니, 사모아, 솔로몬제도, 통가, 바누아투 — 는 인용된 INTERPOL 보도자료에 명문으로 명시되어 있으나 본 위키에 아직 국가 페이지가 없으므로 본문 명단에만 수록된다. (8개 항목으로 집계됨; 여덟 번째 태평양 항목인 마카오는 INTERPOL 본문에서 중국 지역으로 처리되어 위 본문에 별도로 포착됨.)
- 26개 관할권 전반의 국경 간 데이터 공유의 법적 근거는 인용된 1차 출처에서 명시되지 않으며, 같은 날 INTERPOL 보도에서 명명된 작전 프레임은 상설 아시아·남태평양 사이버범죄 공동작전(ASPJOC) 프로젝트 구조이다.

## Follow-Up Actions

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전과 관련하여 공개적으로 접근 가능한 법원 제출 문서가 발견되지 않았다. 가능한 사유: 공개 법원 기록 시스템이 없는 비(非)미국 관할권, 봉인 절차, 또는 공식 기소로 이어지지 않은 작전 등.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- INTERPOL, 2025-06-11: 20,000 malicious IPs and domains taken down in INTERPOL infostealer crackdown.
- Kaspersky, 2025-06-11: Operation Secure: Kaspersky supports INTERPOL in curbing infostealer threat.
- Help Net Security, 2025-06-11: Infostealer crackdown: Operation Secure takes down 20,000 malicious IPs and domains.

## Operational Timeline

- 2025-01-01: 활동 또는 수사 개시.
- 2025-06-11: 공식 발표.
- 2025-04-30: 보고된 집행 종료 시점.
- 2025-06-11: Help Net Security, INTERPOL, Kaspersky로부터의 공개 출처 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: 해킹, 랜섬웨어, 악성코드.
- 본 기록은 status completed의 infrastructure-seizure로 분류된다.

## Evidence and Attribution Notes

- INTERPOL은 Operation Secure(시큐어 작전, INTERPOL infostealer)가 2025년 1월부터 4월까지 진행되었으며 2025-06-11에 공식 발표되었다고 보고함.
- Operation Secure(시큐어 작전, INTERPOL infostealer)는 INTERPOL이 주도하여 2025년 1월부터 4월까지 아시아·태평양 26개국에 걸쳐 수행된 작전으로, 인포스틸러 악성코드 인프라를 표적으로 함.
- 본 작전은 32명 체포, 2만 개 이상의 악성 IP 및 도메인 차단, 41대의 서버와 100GB 이상의 데이터 압수, 21만 6,000명 이상의 피해자에 대한 통지로 이어짐.
- Kaspersky는 Operation Secure(시큐어 작전, INTERPOL infostealer)를 26개국 인포스틸러 인프라에 대한 아시아·태평양 단속으로 기술함.
- 발표문은 2만 개 이상의 악성 IP 및 도메인 차단과 21만 6,000명 이상의 피해자 통지를 본 작전에 귀속시킴.
- Kaspersky는 **Operation Secure(시큐어 작전, INTERPOL infostealer)**를 인포스틸러 인프라에 대한 26개국 아시아·태평양 집행 조치로 기술함.
- Help Net Security는 동일한 2만 개 이상 차단, 41대 서버 압수, 32명 체포, 21만 6,000명 피해자 통지 수치를 보고함.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라 아시아·태평양 전역의 인포스틸러 악성코드 인프라와 운영자에 대한 infrastructure-seizure를 기술하므로 정본(canonical) 작전으로 보존된다. 기록은 주도 책임을 Interpol Igci에, 조정 책임을 Interpol Igci에 귀속시키며, 참여 또는 영향을 받은 관할권은 인도, 인도네시아, 일본, 한국, 싱가포르, 태국으로 기록되어 있다.

협력 모델은 주로 주도/조정 기관 및 국가 명단을 통해 드러나며; 상세한 법적 메커니즘 필드는 여전히 희소하다.

정본 기록에 포착된 작전 결과: 32명 체포; 41대 서버 압수; 216,000명 피해자 통지.

정본 출처 집합은 3건의 참고문헌을 포함한다: 2025 04 01 Interpol Operation Secure Infostealer, 2025 04 01 Kaspersky Com Kaspersky Supports Interpol Operation Secure, 2025 04 01 Helpnetsecurity Com Operation Secure Disrupts Global Infostealer Malware Operations.
정본 작전에 요구되는 출처 하한은 충족되나, 출처의 범위만으로 모든 하위 체포 또는 양형이 본 작전의 일부임이 입증되지는 않으며, 후속 기록은 별도로 연결되어 유지되어야 한다.
현재 본 페이지에 부여된 프론트매터의 missing-field 플래그는 없다.
데이터셋 활용 측면에서, 본 페이지는 작전 수준 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조정된 집행 조치 전체를 기술한다. 이후 기소, 유죄 인정, 양형, 인도, 몰수 조치는 출처가 이를 새로운 다국적 작전으로 명시적으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 연결되어야 한다.
출처 기록이 더 광범위한 배경, 통신사 재게시 반복, 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 결부된 사실을 우선시한다. 주변적 출처 제목은 독립적 분류 체계 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 상태로 유지하기 위함이다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | INTERPOL 인포스틸러 단속에서 2만 개의 악성 IP 및 도메인 차단 | INTERPOL | 2025-06-11 | https://www.interpol.int/en/News-and-Events/News/2025/20-000-malicious-IPs-and-domains-taken-down-in-INTERPOL-infostealer-crackdown |
| [2] | Operation Secure: Kaspersky, INTERPOL의 인포스틸러 위협 억제 지원 | Kaspersky | 2025-06-11 | https://www.kaspersky.com/about/press-releases/operation-secure-kaspersky-supports-interpol-in-curbing-infostealer-threat |
| [3] | 인포스틸러 단속: Operation Secure, 2만 개의 악성 IP 및 도메인 차단 | Help Net Security | 2025-06-11 | https://www.helpnetsecurity.com/2025/06/11/operation-secure-cybercrime-infostealer-crackdown/ |
