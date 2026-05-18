## 개요

미국 법무부는 2025년 5월 22일 모스크바 거주 48세 **루스탐 라파일레비치 갈리야모프(Rustam Rafailevich Gallyamov)**가 2008년 이래 Qakbot(큐어크봇 악성코드) 공모를 주도한 혐의로 기소된 사실을 공개하였다. 갈리야모프는 Qakbot을 활용하여 봇넷(botnet)을 구축하고, **ProLock, DopplePaymer, Egregor, REvil, Conti, Name Locker, Black Basta, Cactus**를 포함한 랜섬웨어 변종을 배포한 공모자들에게 접근권을 제공하였다는 혐의를 받고 있다.

본 조치는 미국, 프랑스, 독일, 네덜란드, 덴마크, 영국, 캐나다가 참여한 다국적 합동 노력이었으며, [[europol-ec3|Europol(유럽 사이버범죄센터)]]이 지원을 제공하였다.

## 감사 노트(Audit Note)

본 페이지는 2025년의 기소와 2023년 네덜란드 측 무력화 계층을 의도적으로 결합한다. 다국적 협력 실체는 실재하나, 두 국면이 단일한 절차적 사건으로 해석되어서는 안 된다.

## 배경

Qakbot(QBot 또는 Pinkslipbot으로도 알려져 있음, 큐어크봇 악성코드)은 2008년부터 활동해 온 가장 오래 운영된 악성코드(malware) 군 중 하나이다. 본래 뱅킹 트로이목마로 출발하였으나, 랜섬웨어(랜섬웨어) 운영자를 위한 주요 초기 접근권 제공형 서비스(initial-access-as-a-service) 플랫폼으로 진화하였다. 2023년 8월, 다국적 작전이 봇넷을 무력화하고 다수 국가에 걸친 인프라를 압류하였다.

네덜란드 검찰 측 기록은 본 작전 계열에서 특히 유용하다. 2023년 8월, [[netherlands-om|Openbaar Ministerie]]와 네덜란드 경찰은 Qakbot 봇넷 무력화를 공동으로 발표하면서 네덜란드 데이터센터에서 **22대의 서버**가 압류되었다고 밝혔다. 이는 본 위키가 네덜란드를 익명의 보조 국가로 남겨두지 않고, 네덜란드 검찰의 참여를 광범위한 Qakbot 집행 사슬과 직접 연결할 수 있게 해 준다.

## 참여 당사자

- **주도:** 미국 법무부 / [[fbi-cyber-division|FBI(미국 연방수사국) 사이버과]]
- **조정 지원:** [[europol-ec3|Europol EC3]]
- **선행 무력화 단계의 네덜란드 검찰 측 파트너:** [[netherlands-om|Openbaar Ministerie - Landelijk Parket]]
- **선행 무력화 단계의 네덜란드 경찰 측 파트너:** [[netherlands-politie|네덜란드 국가경찰]]
- **국제 파트너:** 프랑스, 독일, 네덜란드, 덴마크, 영국, 캐나다

## 결과 및 영향

- 공모, 전자금융 사기, 관련 혐의로 갈리야모프에 대한 **기소(indictment)**
- 민사 몰수 절차를 통해 표적화된 **2,400만 달러 초과**의 암호화폐(cryptocurrency)

## 모순 및 미해결 질문

- 갈리야모프가 러시아에 소재한 상황에서 향후 체포(arrest)될 가능성이 있는가?
- 범죄 활동이 계속된 점에 비추어, 2023년 8월 봇넷 단속의 실효성은 어느 정도였는가?
- Qakbot이 조력한 랜섬웨어 공격의 총 금융 피해는 어느 정도인가?

<!-- SOURCE_ENRICHMENT_START -->

## 소스 커버리지

- Openbaar Ministerie, 2023-08-29: 세계 최대 규모의 봇넷 Qakbot 무력화.
- 미국 법무부(OPA), 2025-05-22: Qakbot 악성코드 공모 주범, 글로벌 랜섬웨어 사건 관련 기소.
- Help Net Security, 2025-05-23: DanaBot 봇넷 무력화 및 QakBot 주범 기소.
- Eurojust, 2023-08-30: 70만 명 이상의 피해자를 감염시키고 전 세계적으로 수억 달러 피해를 야기한 악성코드 네트워크, 다국적 작전으로 무력화.

## 작전 타임라인

- 2008: 활동 또는 수사 개시.
- 2025-05-22: 공개 발표.
- 2023-08-29: Openbaar Ministerie의 공개 소스 보도.
- 2023-08-30: Eurojust의 공개 소스 보도.
- 2025-05-22: 미국 법무부(OPA)의 공개 소스 보도.
- 2025-05-23: Help Net Security의 공개 소스 보도.

## 법적·절차적 상태

- 기록상 범죄 분류: 랜섬웨어 및 악성코드.
- 본 기록은 진행 중(ongoing) 상태의 합동수사로 분류된다.
- 관련 법적/작전적 기록: Us V Gallyamov Qakbot.

## 증거 및 귀속 주석

- 네덜란드 검찰(OM)과 네덜란드 경찰은 국제 Qakbot 무력화를 공동 발표하였다.
- 네덜란드 측은 네덜란드 내 여러 데이터센터에서 22대의 서버를 압류하였다고 보고하였다.
- 본 소스는 대규모 다국적 봇넷 작전에 검찰이 공식적으로 참여한 사실을 보여 준다.
- 본 OM-경찰 공동 보도자료(press release)는 네덜란드 검찰의 Qakbot 무력화 참여를 문서화한다.
- 2025년 5월 22일, 미국 법무부는 모스크바 거주 48세 루스탐 라파일레비치 갈리야모프가 2008년 이래 QakBot 악성코드 공모를 주도한 혐의로 기소된 사실을 공개하였다.
- 본 기소는 랜섬웨어 조력 인프라를 표적으로 한 국제 법집행 캠페인인 작전 Endgame(Operation Endgame)과 연계하여 공개되었다.
- 갈리야모프는 공모, 전자금융 사기, 관련 혐의로 기소되었다.
- 그는 QakBot을 개발·배포하여 봇넷을 구축한 뒤 ProLock, DopplePaymer, Egregor, REvil, Conti, Name Locker, Black Basta, Cactus를 포함한 랜섬웨어 변종을 배포한 공모자들에게 접근권을 제공한 혐의를 받고 있다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## 원문 핵심 발췌

- Eurojust, 2023-08-30: 70만 명 이상의 피해자를 감염시키고 전 세계적으로 수억 달러 피해를 야기한 악성코드 네트워크, 다국적 법집행 작전으로 무력화 | Eurojust | 유럽사법협력기구 Eurojust 유럽사법협력기구 검색 메인 내비게이션 홈 소개.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본 작전 평가

본 페이지는 피의자 특정 후속 조치가 아닌, 루스탐 라파일레비치 갈리야모프 및 Qakbot 악성코드 네트워크에 대한 합동수사를 기술하므로 정본 작전으로 유지된다. 기록상 주도 책임은 Fbi Cyber Division에, 조정 책임은 Europol Ec3에 귀속되며, 참여 또는 영향을 받은 관할로 캐나다, 덴마크, 프랑스, 독일, 네덜란드, 영국, 미국이 기록되어 있다.

협력 모형은 명명된 기관 및 파트너를 통해 문서화되어 있다: Fbi Cyber Division, Europol Ec3, Netherlands Om, Netherlands Politie.

정본 기록에 포착된 작전 결과: 기소 1건; 암호화폐/자산 결과는 2,400만 달러 초과로 기록.

정본 소스 집합은 4건의 참조를 포함한다: 2023 08 29 Om Nl Qakbot Onschadelijk Gemaakt, 2025 05 22 Cdca Qakbot Gallyamov Indictment, 2025 05 23 Helpnetsecurity Com Danabot Botnet Disrupted Qakbot Leader Indicted, 2023 08 30 Eurojust Europa Eu Qakbot Malware Network Dismantled.
정본 작전의 소스 하한선은 충족되나, 소스의 폭이 곧 모든 후속 체포 또는 형 선고가 본 작전의 일부임을 입증하지는 않는다. 후속 기록은 별도로 연결되어야 한다.
본 페이지에 여전히 남아 있는 메타데이터 공백: 법적 근거 및 활용된 메커니즘.
데이터셋 활용 측면에서 본 페이지는 작전 단위 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조정된 집행 행위 전체를 기술한다. 후속 기소, 유죄협상, 형 선고, 범죄인 인도, 자산 몰수는 소스가 명시적으로 이를 새로운 다국적 작전으로 제시하지 않는 한 관련 사건(case) 또는 흡수된 후속 기록으로 부가되어야 한다.
소스 기록에 더 폭넓은 배경, 반복적 통신사 재게시, 또는 주제 페이지성 자료가 포함된 경우 본 평가는 명명된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실을 우선시한다. 주변적 소스 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 상태로 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 세계 최대 규모의 봇넷 Qakbot 무력화 | Openbaar Ministerie | 2023-08-29 | https://www.om.nl/actueel/nieuws/2023/08/29/grootste-wereldwijde-botnet-qakbot-onschadelijk-gemaakt |
| [2] | Qakbot 악성코드 공모 주범, 글로벌 랜섬웨어 사건 관련 기소 | US DOJ (OPA) | 2025-05-22 | https://www.justice.gov/opa/pr/leader-qakbot-malware-conspiracy-indicted-involvement-global-ransomware-scheme |
| [3] | DanaBot 봇넷 무력화 및 QakBot 주범 기소 | Help Net Security | 2025-05-23 | https://www.helpnetsecurity.com/2025/05/23/operation-endgame-danabot-botnet-disrupted-qakbot-leader-indicted/ |
| [4] | 70만 명 이상의 피해자를 감염시키고 전 세계적으로 수억 달러 피해를 야기한 악성코드 네트워크, 다국적 법집행 작전으로 무력화 | Eurojust | 2023-08-30 | https://www.eurojust.europa.eu/news/malware-network-infected-more-700000-victims-and-caused-hundreds-millions-dollars-damage |
