## 요약

**Operation Endgame(엔드게임 작전) 페이즈 2**는 랜섬웨어를 가능케 하는 인프라에 대한 국제 캠페인의 두 번째 주요 단계로, 2025년 5월 19일부터 22일까지 수행되었다. 본 작전은 전례 없는 규모의 인프라 차단을 달성하였다: **300대의 서버 압수**, **650개 도메인 무력화**, 그리고 **350만 유로 상당의 암호화폐 압수**(Operation Endgame 누적 압수액을 2,120만 유로 이상으로 끌어올림).

본 단계에서 실제 체포는 이루어지지 않았으나, **20건의 국제 체포영장**이 발부되었고 **18명의 용의자**가 **EU Most Wanted 명단**에 추가되어, 식별된 행위자들에게 지속적인 압박을 가하였다. 본 작전은 랜섬웨어 공격 체인의 출발점을 형성하는 초기 접근 악성코드 패밀리 — Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie — 를 표적으로 삼았다.

## Background

(본 절은 페이즈 2에서 차단된 7개 악성코드 패밀리의 **범죄 실체** — 수법(모더스 오페란디), 피해자 프로파일 및 영향, 자금 흐름, 범죄 조직 구조 — 를 기술한다. 작전 맥락은 요약(Summary)에 속하며, 단계 간 비교는 Operational Timeline / Results에서 다룬다.)

### 수법(모더스 오페란디) — 랜섬웨어 킬 체인으로서의 초기 접근 악성코드

페이즈 2는 랜섬웨어 킬 체인의 **초기 접근 단계**에 위치한 7개 악성코드 패밀리, 즉 **Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie**를 표적으로 삼았다. 이들은 랜섬웨어 그 자체가 아니라, 랜섬웨어 제휴자들이 기업 네트워크를 침해하기 위해 임차하거나 배포하는 진입 및 거점 확보 도구이다. 전형적인 전달 시퀀스(인용된 tier-1 보도자료가 명시하는 경우 그대로, 그렇지 않은 경우 해당 악성코드 패밀리의 확립된 패턴을 반영):

1. **피싱 이메일 또는 악성 광고**가 페이로드(예: Bumblebee, Warmcookie, Hijackloader)를 운반하여 피해 기기에 교두보를 확보한다.
2. **로더/드로퍼 단계**(Bumblebee, Hijackloader, Lactrodectus)가 추가 모듈 — 자격증명 탈취 도구, 측면 이동 도구, 후속 공격 프레임워크 — 를 다운로드한다.
3. **정보 탈취/뱅킹 트로이목마 단계**(DanaBot, Qakbot, Trickbot)가 자격증명, 뱅킹 세션, 기업 단일 사인온 토큰을 수집한다. 특히 DanaBot은 범죄용 자격증명 탈취 기능과, 정부·군사 대상에 대한 주문형 첩보 기능을 동시에 제공한다.
4. **제휴자 인계**: 탈취된 접근권 — RDP 자격증명, VPN 토큰, Active Directory 거점 — 이 랜섬웨어 제휴자(Conti, BlackBasta, REvil, LockBit)에게 판매되거나 사용되어 암호화 페이로드를 배포한다.

페이즈 2 보도자료에서 DanaBot은 특히 강조되었다: 미국 DOJ(미국 법무부)의 DanaBot 기소장은 DanaBot이 **이중 목적** — 일반 사이버 범죄(자격증명 탈취, 뱅킹 사기)와 더불어 국가 연계 첩보활동(운용자가 지시한 표적에 대한 정부·군사 네트워크 침해) — 으로 활용되었다고 주장한다.

### 피해자 프로파일 및 영향

인용된 tier-1 출처(Europol(유럽 경찰청), FBI(미국 연방수사국), 독일 BMI, DanaBot 관련 The Hacker News)는 다음과 같은 피해자 측 수치를 열거한다:

- **DanaBot 단독**: 전 세계 30만 대 이상의 컴퓨터 감염; 누적 추정 재정 피해 5,000만 달러 이상.
- **페이즈 2 악성코드 패밀리 통합**: Bumblebee, Trickbot, Qakbot은 tier-1 보도에서 **Conti, BlackBasta, REvil** 랜섬웨어 생태계의 주요 초기 접근 도구로 기록되어 있다. 이들은 총괄적으로 최소 15개국의 병원, 학교, 제조 기업, 핵심 인프라 운영자, 다국적 기업을 피해자로 만들었다(이 수치는 상위 [[operation-endgame|Operation Endgame]] 보고에서 가져온 것이며, 페이즈 2 패밀리별 귀속은 부분적으로 페이즈 1 및 DanaBot 공개 자료에서 추론되었다).
- 인용된 페이즈 2 출처에는 **국가별 피해자 세부 내역이 제공되지 않는다**. "10개국에서 9대의 서버 압수"(페이즈 1)와 "페이즈 2 300대 서버"의 비교는 실질적으로 더 크지만 특성이 명확하지 않은 피해자 발자국을 시사한다.

> [!note] Gap on victim profile
> 인용된 tier-1 페이즈 2 출처들은 인프라 압수 수치를 열거하지만, 악성코드 패밀리별 피해자 수, 피해자 국가별 분포, 패밀리별 재정 피해 수치는 **공개하지 않는다**(DanaBot 관련 30만 / 5,000만 달러 수치는 예외). Contradictions 절 참조.

### 자금 흐름

- **DanaBot**: 미국 DOJ는 누적 피해를 5,000만 달러 이상으로 귀속한다. 16건 카운트의 DanaBot 기소장은 운영자들이 추정 운영자 Aleksandr Stepanov와 Artem Kalinkin(러시아 노보시비르스크)에 연결된 지갑을 통해 암호화폐 결제를 받았다고 주장한다. 피고인별 정확한 수익 내역은 인용된 출처에서 공개되지 않는다.
- **페이즈 2 암호화폐 압수**: 수사 중 식별된 운영자 통제 지갑에서 350만 유로 압수.
- **Operation Endgame 전 단계 누적**: 2,120만 유로 이상의 암호화폐 압수.(페이즈 1 용의자 자산 수치로 6,900만 유로도 보고됨 — 자산 동결과 압수 합계의 관계에 대해서는 Contradictions 절 참조.)

> [!note] Gap on financial flow
> 패밀리별 랜섬 수익 수치(Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, Warmcookie)는 인용된 tier-1 페이즈 2 출처에서 공개되지 않는다. 총합 2,120만 유로 이상이라는 수치는 악성코드 패밀리별 또는 페이즈별로 세분화되지 않는다. Contradictions 절 참조.

### 범죄 조직 구조

인용된 tier-1 출처들은 페이즈 2 표적 생태계를 단일 범죄 조직이 아닌 **서비스 시장**으로 기술한다:

- **악성코드 패밀리별 운영자 셀**: 7개 악성코드 패밀리 각각은 코드베이스, 통제 패널 인프라, 제휴자 모집 채널을 유지하는 별개의 운영자 팀이 운용한다. 페이즈 2 발표에서 공개적으로 이름이 알려진 운영자 팀은 DanaBot 팀이 유일하다 — 미국 DOJ가 기소한 **러시아 국적자 16명**, 그중 Aleksandr Stepanov(39세)와 Artem Kalinkin(34세)이 모두 러시아 노보시비르스크 출신이다.
- **제휴 모델**: 각 운영자 팀은 랜섬웨어 제휴자 및 기타 범죄 고객에게 접근권을 임대하거나 라이선스를 부여한다. 제휴자들은 정액제, 설치당 요금, 수익 분배 중 하나의 방식으로 지불한다. 페이즈 1 Smokeloader 고객 데이터베이스(2024년 5월 압수)는 이후 2025년 4월 수요 측 후속 조치의 템플릿을 제공하였다.
- **지리적 분포**: 운영자 인프라는 7개 이상의 페이즈 2 관할 구역과 추가 비협력 위치(특히 다수의 운영자가 거주하는 러시아)에 걸쳐 클라우드, 방탄 호스팅, 침해된 합법 호스팅에 분산되어 있다.
- **러시아 연계 집중**: 이름이 공개된 DanaBot 운영자들은 모두 러시아 국적이며, 더 넓은 페이즈 2 기소장 / EU Most Wanted 명단에는 부분적으로 공개된 국적 정보가 러시아 및 구소련 공간에 치우친 18명의 용의자가 추가된다.

> [!note] Gap on OCG structure
> 인용된 tier-1 페이즈 2 출처들은 DanaBot 기소된 운영자 16명만 이름을 거명한다. 나머지 6개 악성코드 패밀리(Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, Warmcookie)에 대해서는 운영자 신원이 인용된 페이즈 2 출처에서 열거되지 않으며, EU Most Wanted 명단(총 18명의 용의자)만이 더 넓은 운영자 풀을 시사한다. Contradictions 절 참조.

### Operation Endgame 누적 결과 (페이즈 1 + 페이즈 2)

| 지표 | 페이즈 1 (2024년 5월) | 페이즈 2 (2025년 5월) | 총계 |
|--------|-------------------|-------------------|-------|
| 체포 | 4 | 0 | 4 |
| 압수 서버 | 100+ | 300 | 400+ |
| 압수 도메인 | 2,000+ | 650 | 2,650+ |
| 압수 암호화폐 | — | 350만 유로 | 2,120만 유로 이상(누적) |
| 체포영장 | — | 20 | 20+ |
| EU Most Wanted | — | 18 | 18 |

## 참여 당사자

### 조정 기구
- [[europol-ec3|Europol]]
- [[eurojust|Eurojust]]

### 참여 국가 (7개국)
캐나다, 덴마크, 프랑스, 독일, 네덜란드, 영국, 미국

### 참여 기관 (15개)
[[europol-ec3]], [[eurojust]], [[canada-rcmp|RCMP]], [[denmark-police|덴마크 경찰]], [[france-national-police|프랑스 국가경찰]], [[france-gendarmerie|프랑스 헌병대]], [[france-junalco|JUNALCO]], [[germany-bka|독일 BKA(독일 연방수사청)]], [[germany-frankfurt-prosecutor|프랑크푸르트 검찰]], [[netherlands-politie|네덜란드 국가경찰]], [[uk-nca|영국 NCA(영국 국가범죄청)]], [[fbi-cyber-division|FBI]], [[us-secret-service|미국 비밀경호국]], [[us-dcis|DCIS]], [[us-doj|미국 DOJ]]

## 법적 근거

- 협력 사법 조치를 통한 **20건의 국제 체포영장** 발부
- **18명의 용의자**가 EU Most Wanted 명단에 추가
- 법원 승인 압수 명령을 통해 **350만 유로** 상당의 암호화폐 압수

> [!info] Legal-basis note
> 국제 체포영장과 암호화폐 압수에 대한 구체적인 법적 근거는 추가 출처에서 확인되어야 한다.

## 작전 타임라인

| 날짜 | 사건 |
|------|-------|
| 2024-05-27 ~ 2024-05-29 | 페이즈 1 수행 |
| 2025-05-19 | 페이즈 2 액션데이 개시 |
| 2025-05-19 ~ 2025-05-22 | 300대의 서버 압수, 650개 도메인 무력화 |
| 2025-05-23 | Europol 공식 발표 |

## 결과 및 영향

| 지표 | 수치 |
|--------|-------|
| 압수된 서버 | 300 |
| 무력화된 도메인 | 650 |
| 압수된 암호화폐(본 단계) | 350만 유로 |
| 압수된 암호화폐(Endgame 누적) | 2,120만 유로 이상 |
| 국제 체포영장 | 20 |
| EU Most Wanted 추가 | 18 |
| 실제 체포 | 0 (본 단계) |
| 표적 악성코드 패밀리 | 7 |

## 활용된 협력 메커니즘

- **Europol 조정:** 7개국에 걸친 작전 조정
- **Eurojust:** 체포영장 및 압수 명령에 대한 사법 조정
- **다국 동시 조치:** 다수 관할 구역에 걸친 300대 서버의 동기화된 테이크다운
- **EU Most Wanted 메커니즘:** 공개 압박을 생성하고 신원 확인을 가능케 하기 위한 18명 추가

## 교훈

1. **개인보다 인프라:** 즉각적인 체포가 없었음에도, 300대의 서버와 650개 도메인의 테이크다운은 랜섬웨어 생태계에 상당한 운영 차질을 야기하였다.
2. **누적 재정 영향:** 누적 2,120만 유로 이상의 암호화폐 압수는 지속적인 캠페인이 시간에 걸쳐 재정적 차질을 누적 시키는 효과를 보여준다.
3. **영장 우선 접근법:** 20건의 국제 체포영장과 EU Most Wanted 등재는 용의자들이 협조 관할로 이동할 때 향후 체포를 위한 법적 틀을 마련한다.
4. **지속적 캠페인:** 페이즈 1과 페이즈 2 사이의 12개월 간격은 일회성 조치가 아닌 지속적 작전 모델을 보여준다.

## 후속 조치

20건의 국제 체포영장과 18명의 EU Most Wanted 등재는 식별된 개인들에 대한 지속적인 후속 압박을 시사하며, 체포 기회가 발생할 때 이들을 표적으로 한다.

## Korean Involvement (한국의 참여)

Operation Endgame 페이즈 2에 한국이 직접 참여한 사실은 확인되지 않았다.

## DanaBot 악성코드 테이크다운 (Excel 데이터 보충)

> [!note] Data from Excel batch import (2026-04-08)
> 다음 DanaBot 관련 세부 사항은 The Hacker News 보도(Excel 데이터의 11행)에서 식별되었으며, 주요 Europol 출처를 보충한다.

Operation Endgame의 일환으로, 미국 법무부는 특히 **DanaBot** 악성코드 네트워크의 해체를 주도하였다:
- **개인 16명**이 DanaBot 운영 혐의로 미국 DOJ에 의해 기소됨
- 전 세계에서 **30만 대 이상의 컴퓨터**가 DanaBot에 의해 감염
- DanaBot 단독으로 추정 재정 피해 **5,000만 달러 이상**
- DanaBot은 이중 목적으로 활용됨: 사이버 범죄(자격증명 탈취, 사기)와 첩보활동(정부·군사 표적)

### 후속 단계: 5건 추가 구금

후속 집행 조치(21행, Europol URL)는 다음과 같은 결과를 도출하였다:
- **추가 5건의 구금** 및 심문
- 추가 서버 테이크다운
- 이는 주요 인프라 테이크다운 이후 체포영장 집행 단계의 연속을 나타낸다

## Contradictions & Open Questions

- 페이즈 2가 랜섬웨어 배포율에 미친 구체적인 영향은 무엇인가?
- 20건의 체포영장 대상자 중 몇 명이 이후 검거되었는가? (후속 보도에 따르면 최소 5명)
- 표적 악성코드 패밀리들은 테이크다운 이후 얼마나 빨리 운영을 재구축하였는가?
- 총합 2,120만 유로 이상 수치와 페이즈 1의 6,900만 유로 용의자 보유 자산 수치 사이의 관계는 무엇인가?
- 16건의 DanaBot 기소 및 30만 감염 수치는 The Hacker News(비공식 출처)에서 비롯한 것이므로, 확인을 위해 공식 DOJ 출처가 필요하다.
- **L26 gap — 악성코드 패밀리별 피해자 프로파일**: 인용된 tier-1 페이즈 2 출처는 DanaBot 관련 피해자 수치(30만 감염, 5,000만 달러 피해)만 공개한다. Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, Warmcookie의 패밀리별 피해자 수와 국가별 분포는 공개되지 않는다.
- **L26 gap — 악성코드 패밀리별 자금 흐름**: 페이즈 2 암호화폐 압수 350만 유로와 Operation Endgame 누적 2,120만 유로 이상 수치만 공개된다. 패밀리별 랜섬 수익 또는 운영자 수익(DanaBot의 5,000만 달러 이상 피해 귀속 제외)은 열거되지 않는다.
- **L26 gap — 7개 패밀리 중 6개에 대한 OCG 구조**: DanaBot 운영자 16명만이 공개적으로 거명된다. Bumblebee, Lactrodectus, Qakbot, Hijackloader, Trickbot, Warmcookie 운영자 셀의 운영자 신원, 모집 패턴, 수익 분배 비율은 "EU Most Wanted 18명 등재"라는 총합 수치를 넘어 인용된 페이즈 2 출처에서 열거되지 않는다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2025-05-23: Operation Endgame strikes again: the ransomware kill chain broken at its source.
- The Hacker News, 2025-05-28: DanaBot 악성코드 보도.
- Europol, 2025-05-22: Operation Endgame 후속 조치.
- FBI, 2024-05-29: Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals.
- Europol, 2024-05-30: Largest ever operation against botnets — Operation Endgame.
- KrebsOnSecurity, 2024-05-30: 'Operation Endgame' Hits Malware Delivery Platforms.
- Europol, 2025-05-22: Operation Endgame: Follow-up leads to detentions and server takedowns.

## Evidence and Attribution Notes

- Operation Endgame 페이즈 2는 300대의 서버를 압수하고, 650개 도메인을 무력화하였으며, 350만 유로 상당의 암호화폐를 압수하였다(2025년 5월 19-22일).
- 20건의 국제 체포영장 발부; 18명의 용의자가 EU Most Wanted 명단에 추가됨
- Operation Endgame 누적 암호화폐 압수액: 2,120만 유로 이상
- 표적 초기 접근 악성코드: Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie
- 7개국이 15개 기관과 함께 참여; 랜섬웨어 공격 체인의 시작점을 타격
- 2025년 5월 19-22일, **Operation Endgame**의 두 번째 주요 단계는 전례 없는 규모로 랜섬웨어 가능 인프라를 차단하였다: 전 세계에서 300대 서버 압수, 650개 도메인 무력화, 350만 유로 상당의 암호화폐 압수(Operation Endgame 누적 압수액을 2,120만 유로 이상으로 끌어올림).
- 20명의 핵심 행위자에 대한 국제 체포영장이 발부되었고, 18명의 용의자가 EU Most Wanted 명단에 추가되었다.
- 본 작전은 Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie를 포함한 초기 접근 악성코드 패밀리를 표적으로 삼았다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2024-05-29: 우크라이나, 포르투갈, 루마니아, 리투아니아, 불가리아, 스위스의 법 집행 기관이 용의자 체포 또는 심문, 수색 수행, 서버 압수 또는 테이크다운을 위한 경찰 조치를 지원하였다.
- FBI, 2024-05-29: 2024년 5월 28일부터, 12개국이 참여한 동종 최초의 국제 협력 작전은 다수의 악성코드 변종을 무력화하기 위해 수색을 수행하고, 대상을 심문 또는 체포하였으며, 100대 이상의 서버를 압수 또는 차단하였다.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 중심의 후속 조치가 아니라 초기 접근 악성코드 인프라(Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, Warmcookie)에 대한 인프라 압수 작전을 기술하므로 정규(canonical) 작전으로 보존된다. 본 기록은 주요 책임을 Europol Ec3에, 조정 책임을 Europol Ec3에 귀속시키며, 참여 또는 영향을 받은 관할 구역으로는 캐나다, 덴마크, 프랑스, 독일, 네덜란드, 영국, 미국이 기록된다.

협력 모델은 거명된 기관 및 파트너를 통해 문서화된다: Europol Ec3, Eurojust, Canada Rcmp, Denmark Police, France National Police, France Gendarmerie, France Junalco, Germany Bka, Germany Frankfurt Prosecutor, Netherlands Politie; 집행 양태: 압수, 테이크다운, 자산 동결.

정규 기록을 위해 포착된 작전 결과: 300대 서버 압수; 650개 도메인 압수; 암호화폐/자산 결과는 350만 유로(본 단계); 2,120만 유로 이상(Operation Endgame 총합); 20건의 국제 체포영장 발부; 18명의 용의자가 EU Most Wanted 명단에 추가됨.

정규 출처 세트는 7개의 참고문헌을 포함한다: 2025 05 23 Europol Operation Endgame Phase2, 2025 05 28 Thehackernews Danabot Malware, 2025 05 22 Europol Endgame Follow Up, 2024 05 29 Fbi Gov Operation Endgame Coordinated Worldwide Law Enforcement Action Against Network O, 2024 05 30 Europol Europa Eu Largest Ever Operation Against Botnets Operation Endgame, 2024 05 30 Krebsonsecurity Com Operation Endgame Hits Malware Delivery Platforms, 외 1건.
출처 하한선은 정규 작전 기준에 부합하나, 출처 폭만으로는 모든 하류 체포나 양형이 이 작전의 일부임을 증명하지 못한다; 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 보유한 알려진 메타데이터 결락: 법적 근거 및 활용 메커니즘.
데이터셋 활용 관점에서 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 협력적 집행 조치 전반을 기술한다. 이후의 기소, 답변, 양형, 범죄인 인도, 몰수 조치는 출처가 명시적으로 이를 새로운 다국적 작전으로 제시하지 않는 한 관련 사건으로 첨부되거나 흡수된 후속 기록으로 처리되어야 한다.
출처 기록에 더 넓은 배경, 반복된 통신사 재게시, 또는 주제 페이지 자료가 포함될 때, 본 평가는 거명된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과에 직접 결부된 사실들에 우선순위를 부여한다. 주변적 출처 제목은 독립적인 분류 또는 결과 증거로 취급되지 않는다.
이는 정규 기록의 분석적 한계와 재현성을 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operation Endgame strikes again: the ransomware kill chain broken at its source | Europol | 2025-05-23 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source |
| [2] | DanaBot 악성코드 보도 | The Hacker News | 2025-05-28 | https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html |
| [3] | Operation Endgame: Follow-up leads to detentions and server takedowns | Europol | 2025-05-22 | https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-follow-leads-to-five-detentions-and-interrogations-well-server-takedowns |
| [4] | Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals | FBI | 2024-05-29 | https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals |
| [5] | Largest ever operation against botnets — Operation Endgame | Europol | 2024-05-30 | https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem |
| [6] | 'Operation Endgame' Hits Malware Delivery Platforms | KrebsOnSecurity | 2024-05-30 | https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/ |
