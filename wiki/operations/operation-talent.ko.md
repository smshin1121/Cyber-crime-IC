> [!note] Source basis
> This page has been rebuilt from a malformed dual-frontmatter draft. It now rests on a BKA / Europol-side source page plus DOJ's official January 30, 2025 announcement.

## 개요

**Operation Talent**(탤런트 작전, Europol XSS/Crimenetwork)는 사이버범죄 포럼인 **Cracked**와 **Nulled**를 대상으로 한 독일 주도의 [[europol-ec3|Europol(유럽 경찰청)]] 지원 국제 작전이었다. 2025년 1월 28일부터 30일 사이에 8개국 당국이 두 포럼과 관련 범죄 서비스에 대해 협력 조치를 취하였으며, 그 결과 체포, 도메인 및 서버 압수, 그리고 후속 국제 수사를 위한 광범위한 증거 확보가 이루어졌다.

## 배경

### Modus operandi

Cracked와 Nulled는 영어권 사이버범죄 도구 및 탈취 데이터의 초·중급 시장 역할을 하던 두 개의 공개 웹 영어 사이버범죄 포럼이었다. 두 포럼은 다음을 호스팅하였다.

- 탈취 데이터 덤프(제3자 침해 및 인포스틸러 로그에서 수집된 자격증명 콤보, 은행 및 계정 데이터).
- 서비스형 멀웨어 제공물, 익스플로잇 키트, 원격 접근 트로이목마(RAT), 그리고 크립터/로더 도구.
- 해킹 도구 카탈로그(자격증명 스터핑 도구, 계정 체커, 무차별 대입 유틸리티).
- 사기 서비스 마켓플레이스(카딩, SIM 스왑 서비스, 위조 문서 및 KYC 우회 서비스).
- AI 지원 공격 도구. 이는 공개된 Europol/DOJ 서사에서 포럼 콘텐츠 부문 중 하나로 명명되었으며, Cracked/Nulled를 이전 세대 해커 포럼(Hackforums, RaidForums)과 구분 짓고 LLM 이후의 사이버범죄 마켓플레이스 코호트와 정렬시키는 특징이다.

동일 조치에서 두 개의 지원 인프라 서비스가 차단되었다. **Sellix**는 Nulled에 의해 사용된 결제 처리업체(BKA 측 특성 규정)였고, **StarkRDP**는 동일 포럼들을 통해 마케팅 및 서비스되던 원격 데스크톱 프로토콜(RDP) 호스팅 서비스였다. 결제 처리업체, RDP 인프라 제공업체, 그리고 두 포럼 마켓플레이스를 하나의 동시 다발 폐쇄 조치로 묶은 것은 L26 관련 운영 패턴이다. 즉, 이 조치는 마켓플레이스 전면 인터페이스뿐 아니라 그 배후의 금융 레일 및 방탄 인프라 계층까지 차단하였다.

### Victim profile and impact

두 포럼은 폐쇄 시점에 합산 약 1,000만 개의 등록 사용자 계정을 보유하고 있었다. 이 규모 수치는 별개의 피해자 코호트를 식별한다기보다 정당한 잠복 이용자, 하위 구매자, 중급 판매자, 상위 운영자를 혼합한 수치이다. 다운스트림 피해자 모집단은 자격증명 보유자, 비즈니스 이메일 침해(BEC) 표적, 사기 피해자, 그리고 데이터가 해당 포럼을 통해 거래된 침해 조직 고객이다. 공식 공개 보도는 Cracked/Nulled 리스팅에 기인하는 총 사기 손실, 피해자 1인당 영향 수치, 또는 다운스트림 피해자의 지리적 집중도를 정량화하지 않고 있다.

### Financial flow

Nulled의 결제 처리 백본인 Sellix는 동일 조치에서 차단된 인프라 구성요소로 명명되었으며, 이는 포럼 경제가 순수한 P2P 암호화폐가 아닌 종속적(또는 포럼이 통제하는) 결제 처리 계층을 통해 운영되었음을 시사한다. 이 작전에서 약 30만 유로 상당의 현금 및 암호화폐가 압수되었다. 인용된 1단계(tier-1) 출처들은 현금 대 암호화폐의 내역, 압수된 특정 암호화폐, 또는 추적된 지갑 주소를 공개하지 않으며, 마켓플레이스의 총 거래액 및 포럼 수명 기간 수익 또한 정량화되어 있지 않다.

### Criminal organization structure

2명이 체포되었고 7개의 부동산이 수색되었으며, 17대의 서버 및 12개의 도메인과 관련 계정이 압수되었다. 인용된 1단계(tier-1) 출처들은 체포된 2명의 신원을 명시하지 않으며, 이들의 포럼 내 역할(관리자/모더레이터/Sellix 운영자/StarkRDP 운영자/그 외)을 공개하지 않고, 두 포럼 행정의 보다 광범위한 조직 구조를 특성 규정하지 않고 있다. Cracked와 Nulled 포럼은 별도의 행정 리더십을 가진 운영상 별개의 플랫폼이었으나, 동일 동시 조치에서 Sellix와 StarkRDP가 묶인 점과 8개국 협력 실행을 고려하면, 두 포럼 행정과 그 지원 서비스 제공자들은 인용된 발표에서 단일 OCG로 법적으로 통합되지는 않더라도 인프라 차원에서 운영상 연결되어 있었음을 시사한다.

공식 공개 보도는 두 포럼이 주변적 웹사이트가 아닌 전 세계 지하 경제에 깊이 자리잡고 있었음을 나타내며, 이는 Operation Talent를 단일 플랫폼 압수 사건이 아닌 의미 있는 인프라 차단 사건으로 만든다.

## 참여 당사자

### Lead / Coordination
- [[germany-bka|독일 BKA(연방수사청)]]
- [[europol-ec3|Europol EC3(유럽 경찰청 사이버범죄센터)]]

### Confirmed Participating Countries
- [[germany|독일]]
- [[united-states|미국]]
- [[australia|호주]]
- [[spain|스페인]]
- [[greece|그리스]]
- [[romania|루마니아]]
- [[italy|이탈리아]]
- [[france|프랑스]]

### Confirmed U.S. Role
- [[us-doj|DOJ(미국 법무부)]]
- [[fbi-cyber-division|FBI(미국 연방수사국)]]

## 결과 및 영향

| 지표 | 세부사항 |
|--------|--------|
| 체포 | 2명 |
| 수색 | 부동산 7곳 |
| 압수 서버 | 17대 |
| 압수 도메인/계정 | BKA가 보고한 12개 도메인 및 관련 계정 |
| 현금/암호화폐 | 약 30만 유로 |
| 플랫폼 규모 | 합산 약 1,000만 개의 등록 사용자 계정 |

## Cooperation Mechanisms Used

출처들은 Europol의 지원과 미국의 사법적 참여를 동반한 동시 다국가 경찰 조치를 명확히 뒷받침한다. 공개된 기록은 정확한 형사사법공조 및 증거 이전 수단을 명시하지 않으므로, 본 페이지는 문서화된 사항(독일 주도의 작전 조치, Europol 지원, 그리고 DOJ/FBI 참여)에 한정된다.

## Contradictions & Open Questions

- 계정, 도메인, 압수 서비스의 정확한 수치는 요약본별로 다소 차이가 있으나, 핵심 압수 서사는 일관적이다.
- 포럼의 판매자 및 이용자에 대한 후속 기소가 예상되나 공개 보도에서 아직 충분히 가시화되지 않았다.
- Europol의 공식 자체 발표 페이지의 범위는 현재의 출처 집합에서 충분히 문서화되어 있지 않다. 본 페이지는 따라서 BKA 및 DOJ의 공식 앵커에 의존한다.
- **L26 격차 — OCG 식별**: 인용된 1단계(tier-1) 출처들은 체포된 2명의 신원을 명시하지 않으며, 그들의 포럼 내 역할(관리자/모더레이터/Sellix 운영자/StarkRDP 운영자)을 공개하지 않고, Cracked와 Nulled 포럼 행정 간의 관계를 특성 규정하지 않고 있다.
- **L26 격차 — 자금 흐름 세부사항**: 약 30만 유로의 현금 및 암호화폐 압수는 현금과 암호화폐로 구분되어 있지 않으며, 압수된 특정 암호화폐는 명명되지 않고, 마켓플레이스의 총 거래액이나 포럼 수명 기간 수익 수치는 공개되지 않는다.
- **L26 격차 — 피해자 정량화**: Cracked/Nulled 리스팅에 추적 가능한 총 다운스트림 사기 손실, 피해자 1인당 영향, 그리고 다운스트림 피해자의 지리적 집중도는 인용된 발표에서 정량화되어 있지 않다. 1,000만 명의 사용자 계정 수치는 정당한 잠복 이용자와 운영자를 혼합한 것이며 피해자 수가 아니다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- 독일 BKA / Europol 지원 작전, 2025-01-30: Operation Talent.
- DOJ(미국 법무부), 2025-01-30: 국제 사이버 작전에서 Cracked 및 Nulled 마켓플레이스 차단.
- Cybernews, 2025-01-30: Operation Talent에서 Cracked 및 Nulled 압수.
- Infosecurity Magazine, 2025-01-31: Operation Talent, Cracked 및 Nulled 해체.
- BleepingComputer, 2025-01-31: Operation Talent, Cracked 및 Nulled 사이버범죄 포럼 차단.

## Operational Timeline

- 2025-01-28: 활동 또는 수사 개시.
- 2025-01-30: 공개 발표.
- 2025-01-30: 보고된 집행 종료점.
- 2025-01-30: Cybernews, 독일 BKA / Europol 지원 작전, DOJ(미국 법무부)의 공개 출처 보도.
- 2025-01-31: BleepingComputer, Infosecurity Magazine의 공개 출처 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: 해킹 및 멀웨어.
- 기록된 집행 태세: 체포, 압수, 폐쇄.
- 본 기록은 폐쇄 작전(takedown)으로 분류되며 상태는 완료(completed)이다.

## Evidence and Attribution Notes

- 독일 당국이 Cracked 및 Nulled에 대한 국제 협력 조치를 주도하였다.
- 본 작전은 2명의 체포, 17대의 서버 압수, 그리고 광범위한 증거 확보를 산출하였다.
- 이는 미국의 역할, 국제 연합, 그리고 Cracked 및 Nulled의 차단을 확인한다.
- Cybernews는 독일 주도의 Operation Talent에서 Cracked 및 Nulled가 압수되었다고 보도하였다.
- 해당 보도는 Sellix 및 StarkRDP에 대한 관련 조치와 두 포럼의 사용자 기반 규모를 언급하였다.
- Cybernews는 **Operation Talent** 하에 **Cracked**와 **Nulled**의 압수 및 지원 서비스 차단에 대해 보도하였다.
- Infosecurity Magazine은 Operation Talent가 Cracked 및 Nulled 사이버범죄 포럼을 해체하였다고 보도하였다.
- 해당 기사는 서버 압수, 체포, 그리고 독일·미국·다수의 유럽 파트너의 참여를 강조하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- DOJ(미국 법무부), 2025-01-30: 영향을 받은 피해자 — 법무부는 오늘 미국, 루마니아, 호주, 프랑스, 독일, 스페인, 이탈리아, 그리스에서의 조치를 포함한 다국적 작전에 자국이 참여하여 Cracked 및 Nulled로 알려진 온라인 사이버범죄 마켓플레이스의 인프라를 차단하고 폐쇄하였다고 발표하였다.
- DOJ(미국 법무부), 2025-01-30: 본 작전은 Cracked 및 Nulled를 수사하기 위해 Europol의 지원을 받은 다국적 법집행 작전인 Operation Talent와 연계하여 발표되었다.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아닌 Cracked 및 Nulled 사이버범죄 포럼과 그 지원 범죄 서비스에 대한 폐쇄 작전을 기술하므로 정본 작전(canonical operation)으로 유지된다. 본 기록은 주도 책임을 독일 BKA에, 조정 책임을 Europol EC3에 귀속시키며, 참여 또는 영향 관할권으로 독일, 미국, 호주, 스페인, 그리스, 루마니아, 이탈리아, 프랑스를 기록한다.

협력 모델은 명명된 기관 및 파트너를 통해 문서화된다. 즉, 독일 BKA, Europol EC3, FBI Cyber Division(FBI 사이버국), US DOJ(미국 법무부); 메커니즘: 비공식 협력; 집행 태세: 체포, 압수, 폐쇄.

정본 기록에 포착된 작전 결과: 2명 체포; 서버 17대 압수; 도메인 12개 압수; 약 30만 유로의 현금 및 암호화폐 자산 결과 기록; Cracked 및 Nulled의 합산 약 1,000만 개의 등록 사용자 계정 보유; 관련 서비스인 Sellix 및 StarkRDP의 차단; 부동산 7곳에서의 수색 실시.

정본 출처 집합은 5건의 참고문헌을 포함한다: 2025 01 30 Europol Operation Talent, 2025 01 30 Justice Gov Cracked And Nulled Marketplaces Disrupted International Cyber Operation, 2025 01 30 Cybernews Com Cracked And Nulled Seized In Operation Talent, 2025 01 31 Infosecurity Magazine Operation Talent Cracked Nulled Dismantled, 2025 01 31 Bleepingcomputer Com Operation Talent Cracked Nulled.
출처 하한선은 정본 작전 기준을 충족하나, 출처 폭만으로 모든 후속 체포 또는 양형이 본 작전의 일부임을 증명하지는 않는다. 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
현재 본 페이지에는 frontmatter 누락 필드 플래그가 부여되어 있지 않다.
데이터셋 활용 목적상 본 페이지는 작전 차원의 집계 지점으로 취급되어야 한다. 즉, 국가, 기관, 메커니즘, 결과 필드는 협력 집행 조치 전체를 기술한다. 이후의 기소, 인정, 양형, 범죄인 인도 또는 몰수 조치는, 출처가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한, 관련 사건 또는 흡수됨(absorbed) 후속 기록으로 부착되어야 한다.
출처 기록에 보다 광범위한 배경, 반복되는 와이어 서비스 재게재, 또는 토픽 페이지 자료가 포함될 경우 본 평가는 명명된 작전, 그 참여 당국, 그 대상 인프라 또는 범죄 서비스, 그리고 그 측정 가능한 집행 결과에 직접 결부된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류체계 또는 결과 증거로 취급되지 않는다.
이를 통해 정본 기록은 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operation Talent | 독일 BKA / Europol 지원 작전 | 2025-01-30 | https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2025/Presse2025/250130_Operation_Talent.html |
| [2] | 국제 사이버 작전에서 Cracked 및 Nulled 마켓플레이스 차단 | DOJ(미국 법무부) | 2025-01-30 | https://www.justice.gov/opa/pr/cracked-and-nulled-marketplaces-disrupted-international-cyber-operation |
| [3] | Operation Talent에서 Cracked 및 Nulled 압수 | Cybernews | 2025-01-30 | https://cybernews.com/news/cracked-nulled-seized-operation-talent/ |
| [4] | Operation Talent, Cracked 및 Nulled 해체 | Infosecurity Magazine | 2025-01-31 | https://www.infosecurity-magazine.com/news/operation-talent-cracked-nulled/ |
| [5] | Operation Talent, Cracked 및 Nulled 사이버범죄 포럼 차단 | BleepingComputer | 2025-01-31 | https://www.bleepingcomputer.com/news/security/operation-talent-disrupts-cracked-and-nulled-cybercrime-forums/ |
