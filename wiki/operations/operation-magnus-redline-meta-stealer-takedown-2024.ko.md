> [!info] Provisional page
> 본 작전 페이지는 권장 5-출처 임계치(CLAUDE.md "Entity creation threshold") 미만으로 게재된다. 단일 tier-1 1차 출처(Eurojust(유럽사법협력기구) 보도자료, 2024-10-29)에 기반한다. 추가 동반 출처(DOJ(미국 법무부) 기소 공개, IRS-CI 페이지, 네덜란드 경찰 보도자료)가 수집되어 페이지를 표준 게재 상태로 끌어올려야 한다.

## 개요

**Operation Magnus(매그너스 작전)** 은 조정된 국제 법집행 활동으로, **2024년 10월 28일** 두 개의 다작 malware-as-a-service 정보 탈취 악성코드(infostealer) — **RedLine(infostealer)** 과 **Meta Stealer(infostealer)** — 의 운영 인프라를 해체하고 RedLine 개발자 중 한 명에 대한 미국 형사 기소를 공개하였다. 본 작전은 **[[eurojust|Eurojust(유럽사법협력기구)]]** 가 조정하였으며, 6개 관할구역의 당국을 결집시켰다. 네덜란드, 미국, 벨기에, 포르투갈, 영국, 호주이다. 작전은 네덜란드에서 서버 3건 압수, 도메인 2건 압수, 벨기에에서 2명 체포, 미국 기소 공개, 그리고 RedLine/META 유료 고객 데이터베이스 회수를 산출하였다(출처: [[2024-10-29_eurojust-europa-eu_operation-magnus-redline-meta-infostealer-takedown|Eurojust 보도자료, 2024-10-29]]).

본 작전이 2024년 10월 28일에 이루어졌고 거명된 6개국이 참여 관할구역이라는 사실은 *almost certain*(>95% 신뢰도, 단일 tier-1 1차 출처 및 공개 동반 피해자 사이트 기반)이다. "Operation Magnus(매그너스 작전)" 코드명은 공개 피해자 대응 사이트인 operation-magnus.com에 표시되나 Eurojust(유럽사법협력기구) 보도자료 헤드라인에는 사용되지 않으며, 별칭으로 기록된다.

## 배경

### Modus operandi

RedLine(infostealer)과 Meta Stealer(infostealer)는 **malware-as-a-service(MaaS)** 모델로 운영되는 일반 상품형 **정보 탈취 악성코드**(infostealer) 계열이다. 범죄 고객("affiliates" 또는 "clients")은 구독 또는 일회성 요금을 지불하여 본인의 패널 제어 인스턴스를 운영하였고, 일반적인 사회공학 벡터를 통해 피해 단말로 전달되었다. 즉, 피싱 이메일의 악성 링크와 첨부물, 검색엔진 결과 페이지 및 소프트웨어 다운로드 포털의 악성 광고("malvertising"), 트로이목마화된 "크랙" 소프트웨어 번들, 가짜 브라우저 업데이트 및 게임 치트 설치파일, 그리고 악성 압축파일로 유인하는 YouTube 댓글란 미끼이다. Windows 호스트에서 실행되면 스틸러는 로컬 환경에서 민감 자료를 수집하여 운영자 통제 명령제어(C2) 서버로 유출한다. Eurojust(유럽사법협력기구) 발표에 따르면 수집되는 데이터 범주는 브라우저 자격증명 저장소에 저장된 사용자명과 비밀번호, 자동 저장된 폼 데이터(우편 주소, 이메일 주소, 전화번호), **암호화폐 지갑 콘텐츠**(인기 지갑 소프트웨어 및 브라우저 확장 지갑의 로컬 저장 시드 문구/개인키 파일 포함), 그리고 **브라우저 쿠키**(이미 인증된 계정에서 다중 요소 인증을 우회할 수 있는 인증 세션 쿠키 포함)이다.

### Victim profile and impact

Eurojust(유럽사법협력기구)는 피해자 규모를 전 세계 **"수백만"** 으로 특징지었다. 감염 발자국은 단말 차원에서 글로벌하고 비차별적이다. 즉, 악성 미끼를 클릭한 패치되지 않은 Windows 호스트 운영자라면 누구나 감염될 수 있다. 그러나 도난 데이터의 *악용*은 후속 단계에서 (a) 암호화폐 지갑 보유자(직접 자금 인출 대상), (b) 도난 비밀번호가 계정 탈취용으로 지하 시장에서 재판매되는 소비자 및 소상공인 운영자, 그리고 (c) 도난 세션 쿠키가 초기 침투 브로커에게 기업 SaaS, RDP, VPN 환경으로의 경로를 제공하여 이후 랜섬웨어 affiliate에게 판매되는 기업 사용자에게 집중된다. 수사 중 매핑된 감염/운영 서버는 수십 개국에 걸쳐 **1,200대 이상**으로, 이는 고객 기반과 후속 피해자 노출이 동시에 다수 지역 및 위협 행위자 분야에 걸쳐 있었음을 시사한다.

### Financial flow

MaaS 구독 모델은 수익을 운영자/개발자 계층에 집중시킨다. 즉, 고객은 패널 및 업데이트 접근을 위해 플랫폼(RedLine의 경우 미국 측 공개된 기소장에 따르면 Maxim Rudometov)에 비용을 지불하고, 고객은 직접 후속 채널을 통해 도난 로그를 수익화한다. 즉, 인출된 지갑으로부터의 직접 암호화폐 절도, 다크웹 시장의 계정-탈취-서비스 제공, 그리고 Russian Market과 Genesis Market(후자는 2023년 [[operation-cookie-monster]]에서 해체됨)와 같은 시장에서의 "logs"(감염 호스트별 수집 자격증명 + 쿠키 + 지갑 데이터의 zip 압축파일) 대량 판매이다. Eurojust(유럽사법협력기구) 발표는 수사 중 포착된 수익에 대한 구체적 달러 수치를 열거하지 않는다. RedLine 및 META 플랫폼에서 회수된 **고객 데이터베이스**는 전 세계 비거명 관할구역의 구독자에 대한 후속 조치를 위한 주요 증거 산물이다.

### Criminal organisation structure

RedLine/META 운영은 정전적 **MaaS 3계층 구조**를 보여준다. (1) 소규모 개발자/관리자 핵심(미국 기소장은 RedLine에 대해 단일 거명 주범 Maxim Rudometov를 명시하고 있으며, META 운영자는 Eurojust(유럽사법협력기구) 발표에서 공개적으로 거명되지 않음)으로 코드 유지, 인프라 관리, 패널/제어 소프트웨어, 고객 지원을 담당한다. (2) 접근을 구매하고 자체 캠페인을 운영하는 유료 **customer/affiliate** 계층이다. (3) affiliate 계층의 산출물을 소비하는 지하 시장의 후속 **buyer-of-logs** 계층이다. 수사는 **인프라 계층**(네덜란드 호스팅 C2 서버)을 통해 진입하였고, 회수된 고객 데이터베이스를 통해 개발자 계층(Rudometov 기소)으로 전환되었다. 이 데이터베이스는 또한 거명되지 않은 관할구역의 customer/affiliate 계층에 대한 향후 작전 확대를 위한 주요 단서 산물 역할도 한다.

### Investigation seed

수사는 피해자들의 신고와 익명의 민간 부문 보안 회사가 네덜란드에서 호스팅되는 가능한 RedLine/META 서버에 대해 당국에 통보한 후 시작되었다. 수사관들은 이후 수십 개국에 걸쳐 1,200대 이상의 감염/운영 서버를 매핑하였으며, 이는 다중 관할 조정을 정당화한 규모였다.

## 참여 당사자

### Coordinating body

- **[[eurojust|Eurojust (European Union Agency for Criminal Justice Cooperation)]]** — 6개 관할구역 전체에서의 정보 교환과 동기화된 조치를 조정.

### Lead investigative agency

- **[[netherlands-politie|Netherlands National Police, Team Cybercrime Limburg]]**, 네덜란드 **[[netherlands-om|Public Prosecution Service (Openbaar Ministerie)]]** 와 함께.

### Participating jurisdictions and authorities (as named in the Eurojust release)

| Country | Authorities |
|---|---|
| [[netherlands\|네덜란드]] | National Police (Team Cybercrime Limburg); Public Prosecution Service |
| [[united-states\|미국]] | [[fbi\|FBI(미국 연방수사국)]]; [[us-ncis\|Naval Criminal Investigative Service (NCIS)]]; Internal Revenue Service Criminal Investigations (IRS-CI); [[us-dcis\|Department of Defense Criminal Investigative Service (DCIS)]]; Army Criminal Investigation Division (Army CID); [[us-doj\|DOJ(미국 법무부)]] 가 기소 조정 |
| [[belgium\|벨기에]] | [[belgium-federal-police\|Federal Police]]; Federal Prosecutor's Office |
| [[portugal\|포르투갈]] | [[portugal-policia-judiciaria\|Polícia Judiciária]] |
| [[united-kingdom\|영국]] | [[uk-nca\|National Crime Agency (NCA)]] |
| [[australia\|호주]] | [[australia-afp\|Australian Federal Police (AFP)]] |

### Private-sector touchpoints

- 익명의 보안 회사가 네덜란드에 있는 서버를 식별하는 최초 제보를 제공하였다(Eurojust(유럽사법협력기구) 발표에서 출처 표시 없이 언급됨).
- ESET가 operation-magnus.com을 통해 게시된 무료 RedLine/META 탐지 스캐너를 제공하였다(동반 출처 — Eurojust(유럽사법협력기구) 발표는 벤더명을 거명하지 않는다).

## 법적 근거

Eurojust(유럽사법협력기구) 발표는 특정 조약 조항 또는 법적 협력 도구를 거명하여 인용하지 않는다. Eurojust(유럽사법협력기구)의 다중 관할 사이버범죄 작전 조정은 [[operation-cronos-phase1|Cronos Phase 1]] 및 [[us-v-sokolovsky-raccoon-infostealer|Raccoon Infostealer]]와 같은 이전의 비견 가능한 Eurojust(유럽사법협력기구) 조정 작전에 근거할 때 *typically*(약 80% 신뢰도) 조정을 위한 **Eurojust 규정 (EU) 2018/1727**, 당사국 간 국경 간 절차적 권한을 위한 **사이버범죄 부다페스트 협약**, 그리고 미국-EU 증거 사슬을 위한 양자 **형사사법공조조약(MLAT)** 채널에 기반한다. 이들 중 어느 것도 본 출처에서 명시적으로 인용되지 않는다 — 그에 따라 표시한다.

> [!warning] Legal status check needed
> 사용된 특정 법령 및 조약 근거는 Eurojust(유럽사법협력기구) 보도자료에 열거되어 있지 않다. DOJ(미국 법무부)의 기소 공개는 Maxim Rudometov 기소에 대해 18 U.S.C. §§ 1029(접근 장치 사기), 1030 및 371(컴퓨터 침입 공모), 그리고 1956(자금 세탁)을 인용하는 것으로 보도되고 있으며, 이는 IRS Criminal Investigation 동반 페이지에 따른 것이다. 그러나 이는 공개된 기소장 본문과 직접 대조하여 확인 대기 중이다. 해당 인용을 `legal_basis`에 추가하는 것은 그 출처가 수집될 때까지 보류된다.

## 작전 타임라인

| Date | Event |
|---|---|
| (2024년 이전) | 피해자 신고 및 민간 부문 제보가 네덜란드 내 가능한 RedLine/META 서버를 표시한다. |
| 2024년(출처에 날짜 없음) | 수사관들이 수십 개국에 걸쳐 1,200대 이상의 감염 서버를 매핑한다. Eurojust(유럽사법협력기구) 조정 하에 협력 채널이 수립된다. |
| **2024-10-28** | 전 세계 작전일: 네덜란드 서버 3대 폐쇄; 도메인 2건 압수; 벨기에에서 체포 2건 집행; 미국에서 기소 공개. |
| **2024-10-29** | Eurojust(유럽사법협력기구)가 조정 보도자료를 공개하고, 네덜란드 경찰이 operation-magnus.com에 공개 피해자 점검 자원을 출범시킨다. |

## 결과 및 영향

| Result | Count | Source statement |
|---|---|---|
| 폐쇄된 서버(네덜란드) | 3대 | "three servers taken down in the Netherlands" |
| 압수된 도메인 | 2건 | "two domains seized" |
| 체포(벨기에) | 2건 | "two people taken into custody in Belgium" |
| 미국 기소 공개 | 1건(Maxim Rudometov) | "charges unsealed in the United States" |
| 회수된 고객 데이터베이스 | 1건 | "a client database of RedLine and Meta was retrieved"(Eurojust(유럽사법협력기구)에서 의역) |
| 식별된 감염/영향 서버 | 1,200대 이상 | "over 1,200 servers in dozens of countries were running the malware" |
| 피해자 규모 | "수백만" | Eurojust(유럽사법협력기구) 표현 |

본 작전은 RedLine 및 META 정보 탈취 악성코드(infostealer)를 직후 운영 기간 동안 작동 불가 상태로 만들었으며 고객 풀을 노출시켰다. 이는 MaaS *운영자* 및 *고객* 모두에 대한 후속 수사의 전제조건이다.

## 활용된 협력 메커니즘

- **Eurojust(유럽사법협력기구) 조정**(정보 교환 + 동기화된 다중 관할 조치)이 Eurojust(유럽사법협력기구) 보도자료에서 명시적으로 거명된 유일한 메커니즘이다.
- (a) 네덜란드 인프라 압수, (b) 벨기에 체포, (c) 미국 기소 공개의 동시 패턴은 **[[joint-investigation-team|합동수사팀(JIT)]]** 구조와 일치하나 명시적으로 귀속되지는 않는다. 공식 JIT가 Eurojust(유럽사법협력기구)에 등록되었는지는 출처에서 진술되지 않는다.
- IRS-CI 동반 출처는 Europol(유럽 경찰청)의 **[[j-cat|Joint Cybercrime Action Taskforce (J-CAT)]]** 를 미국 측의 조정 태스크포스로 언급한다. 이는 Eurojust(유럽사법협력기구) 발표에서 반복되지 않으므로 직접 확인 대기 중 `mechanisms_used`에 단정되지 않는다.

## Challenges and Friction Points

Eurojust(유럽사법협력기구) 발표는 마찰점을 서술하지 않는다. 작전 구조로부터 추론된 내용(사실로 단정되지 않음).

- 두 대륙과 네 개 시간대를 넘는 6개 관할 동기화는 비범한 사전 작전 시퀀싱을 시사하며, 이는 Eurojust(유럽사법협력기구) 조정을 통해 관리되었다.
- 유일한 물리적 체포를 벨기에에서(인프라를 호스팅한 네덜란드나 기소를 주도한 미국 대신) 집행하기로 한 결정은 전략적 포럼 쇼핑 결과보다는 피의자의 관할 위치를 시사하나, 이는 진술되지 않았다.

## 교훈

- **민간 부문 입력이 중요하다**: 익명의 보안 회사 제보가 네덜란드 수사를 촉발하여 6개국 작전으로 확장되었으며, 이는 국가 사이버범죄 부서로의 자발적 공개 채널의 가치를 강화한다.
- **Eurojust(유럽사법협력기구) 조정은 당일 다중 관할 동기화를 가져온다**: 본 작전은 MaaS-infostealer 부류에 대해 [[operation-cronos-phase1|Operation Cronos Phase 1]] 템플릿(단일일, 다국, 인프라 + 체포 + 기소)을 재현하였다.
- **MaaS 고객 데이터베이스 회수는 force-multiplier이다**: RedLine/META 고객 명단 회수는 단일 작전을 전 세계 구독자에 대한 후속 수사 파이프라인으로 전환한다.

## Follow-Up Actions

Eurojust(유럽사법협력기구) 발표는 작전을 넘는 후속 활동을 열거하지 않는다. 이후 Maxim Rudometov 기소 절차(미국) 및 가능한 고객 데이터베이스 기반 거명되지 않은 관할구역에서의 조치는 Raccoon Infostealer와 같은 이전 MaaS 작전에 근거할 때 *likely*(약 70% 신뢰도)이나, 추가 출처의 문서화를 기다린다.

## 한국의 참여

Eurojust(유럽사법협력기구) 보도자료는 한국을 참여 관할구역으로 거명하지 않으며, 어떠한 한국 기관도 집행 당국으로 열거하지 않는다. RedLine의 알려진 글로벌 유포와 Eurojust(유럽사법협력기구)의 "전 세계 수백만" 표현을 고려할 때 한국 피해자는 *plausibly* 영향을 받았으나, 출처는 한국 운영 참여를 입증하지 않는다. 본 페이지에서 한국 참여에 대한 단정은 이루어지지 않는다.

## Contradictions & Open Questions

- **작전 코드명**: "Operation Magnus(매그너스 작전)"는 피해자 대응 사이트(operation-magnus.com)와 동반 언론에 표시되나, Eurojust(유럽사법협력기구) 발표 헤드라인에는 표시되지 않는다. 별칭으로 기록됨.
- **공식 JIT?**: 다국 조정이 Eurojust(유럽사법협력기구)에 등록된 합동수사팀(JIT)으로 공식화되었는지는 가용 출처에 진술되지 않는다.
- **법령 인용**: Eurojust(유럽사법협력기구) 발표는 인용된 미국 법령 또는 조약 조항을 열거하지 않는다. DOJ(미국 법무부)의 공개된 기소장 수집 대기 중.
- **민간 부문 제보 출처의 신원**: Eurojust(유럽사법협력기구) 발표는 네덜란드 호스팅 RedLine/META 서버를 최초로 표시한 보안 회사를 거명하지 않는다. 동반 언론은 ESET가 작전 후 피해자 스캐너를 제공하였음을 시사하나, 작전 전 귀속은 확인되지 않는다.
- **벨기에 체포자 신원**: Eurojust(유럽사법협력기구) 발표는 벨기에에서 신병 확보된 두 피의자를 거명하지 않으며, 이들이 RedLine 운영자, META 운영자, 또는 고객인지 명시하지 않는다.
- **L26 gap — 금융 흐름 구체사항**: Eurojust(유럽사법협력기구) 발표는 구독 가격, 포착된 수익, 또는 후속 지갑 절도를 통해 인출된 총 암호화폐를 열거하지 않는다. 배경의 "Financial flow" 하위 섹션은 정전적 MaaS 수익 모델을 질적으로 기술한다. 정량적 수치는 공개된 미국 기소장 본문 및 일체의 몰수 변론을 기다린다.
- **L26 gap — META 개발자/관리자 신원**: Eurojust(유럽사법협력기구) 발표는 개발자/관리자 계층에서 RedLine에 대해서만 Maxim Rudometov를 거명한다. META 배후의 거명된 주범은 인용된 출처에서 공개적으로 공개되지 않으므로, 배경의 "Criminal organisation structure" 하위 섹션은 META에 대한 운영자 계층을 본 출처에서 공개적으로 거명되지 않은 것으로 식별한다.
