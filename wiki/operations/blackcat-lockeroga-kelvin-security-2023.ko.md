> [!note] Composite page
> 이 페이지는 2023년 11월 말과 12월의 3건의 별개 공식 단속 작전을 묶은 것이다. 단일의 공식적으로 명명된 다국적 작전이 아니다.

## 개요

2023년 11월 말과 12월에 미국, 유럽, 스페인 당국은 사이버범죄 와해 활동의 집중된 시기를 함께 표시한 3건의 별개 단속 작전을 발표하였다:

1. **ALPHV/BlackCat**: 2023년 12월 19일, 미국 법무부는 ALPHV/BlackCat 랜섬웨어 변종에 대한 와해 캠페인을 발표하였다. FBI(미국 연방수사국)는 복호화 도구를 개발하여 500명 이상의 피해자에게 제공하였다.

2. **LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) 연계 계열 그룹**: 2023년 11월 28일, Eurojust(유럽사법협력기구)는 71개국 1,800명 이상의 피해자에 대한 공격과 연관된 랜섬웨어 그룹을 우크라이나에서 해체하였다고 발표하였다. 공개 보도는 본 그룹을 LockerGoga(LockerOGA/LockerGoga(랜섬웨어))를 포함한 여러 랜섬웨어 변종과 연결시켰다.

3. **Kelvin Security**: 2023년 12월 11일, 스페인 내무부는 수백 개의 조직 및 공공 기관에 대한 공격으로 기소된 그룹 Kelvin Security와 연계된 것으로 추정되는 용의자의 알리칸테에서의 체포를 발표하였다.

이러한 발표들을 종합하면, 2023년 말의 공식 사이버 단속 활동이 랜섬웨어 인프라 와해, 계열 네트워크 체포, 금전적 동기의 침입 그룹에 어떻게 걸쳐 있는지를 보여준다.

## 배경

이 페이지는 3개의 별개 범죄 표적을 다룬다. tier-1 출처에 의해 공개된 각각의 범죄 실체는 다음과 같다.

### 1. ALPHV/BlackCat 서비스형 랜섬웨어

### 수법(모더스 오페란디)

ALPHV/BlackCat은 서비스형 랜섬웨어(RaaS) 모델을 운영하였다: 핵심 개발팀이 BlackCat/ALPHV(랜섬웨어) 변종을 구축하고 유지하였고, 계열사는 일반적으로 몸값 수익의 80-90% 지분 대가로 악성코드를 임대받았다. tier-1 출처(미국 법무부, 2023-12-19)는 ALPHV/BlackCat을 지난 18개월간 "전 세계 피해자들이 지불한 수억 달러의 몸값" 기준으로 "전 세계에서 두 번째로 만연한 서비스형 랜섬웨어 변종"으로 특징지었다. 운영적으로, 계열사는 피해자 네트워크를 침해하고(미국 법무부 발표에서 진입 벡터는 공개되지 않음), 데이터를 유출한 후, BlackCat/ALPHV(랜섬웨어) 암호화기를 배포하여 이중 갈취(암호화 + 유출 위협)를 수행하였다.

### 피해자 프로파일 및 영향

미국 법무부는 FBI(미국 연방수사국)의 복호화 도구가 전 세계적으로 식별된 "500명 이상"의 피해자에게 제공되었다고 명시한다. 캠페인 기간 동안 ALPHV/BlackCat이 표적으로 삼은 피해자 산업에는 의료, 핵심 인프라, 학교, 정부 기관이 포함되었다(동일 일자인 2023-12-19에 발행된 CISA/FBI/HHS #StopRansomware 공동 권고 AA23-353A에 문서화됨). 미국 법무부는 피해자별 몸값 금액을 공개하지 않지만, 캠페인을 "수억 달러"의 지불된 몸값으로 집계한다.

### 자금 흐름

몸값은 암호화폐(주로 비트코인)로 지불되었으며, 미국 법무부는 2023년 12월 19일 보도자료에서 누적 압수 또는 자금세탁 경로 수치를 공개하지 않았다.

### 범죄 조직 구조

RaaS 구조: 핵심 개발팀과 분산된 계열사 네트워크. 미국 법무부의 2023년 12월 19일 와해 작전은 운영자 인프라(다크웹 유출 사이트 압수, 복호화 키 회수)를 표적으로 삼았지만, 해당 일자에 명명된 핵심 운영자 또는 계열사의 체포나 기소는 발표하지 않았다.

### 2. LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) / MegaCortex / HIVE / Dharma 랜섬웨어 계열 네트워크 (우크라이나 작전)

### 수법(모더스 오페란디)

Eurojust(유럽사법협력기구)(2023-11-28)에 따르면, 네트워크는 무차별 대입 공격, 데이터 애플리케이션에 대한 SQL 인젝션, 탈취된 자격 증명, 악성 첨부 파일이 포함된 피싱 이메일 등 여러 침입 벡터를 사용하여 기업 IT 환경을 침해하였다. 발판을 마련한 후, 네트워크는 Trickbot 악성코드와 후속 활용 프레임워크(Cobalt Strike, PowerShell Empire)를 지속성 및 횡적 이동에 사용하였다. 때로는 수개월에 걸친 잠복 기간 후, 운영자는 4개의 랜섬웨어 패밀리 — **LockerGoga(LockerOGA/LockerGoga(랜섬웨어)), MegaCortex, HIVE, 또는 Dharma** — 중 하나를 배포하고 복호화 키 대가로 비트코인 몸값 노트를 제시하였다.

### 피해자 프로파일 및 영향

tier-1 출처(Eurojust(유럽사법협력기구))는 본 네트워크에 **71개국에 걸쳐 1,800명 이상의 피해자**가 있다고 귀속시키며, 그 대부분이 사업 운영이 중단된 대기업이다. 집계 손실: "최소한 수억 유로".

### 자금 흐름

복호화 키 대가로 비트코인으로 몸값 결제 수령. Eurojust(유럽사법협력기구)는 2023년 11월 28일 보도자료에서 누적 압수 또는 자산 회수 수치를 공개하지 않는다.

### 범죄 조직 구조

차별화된 범죄 기능을 가진 다중 역할 네트워크: 침입 운영자(무차별 대입/SQL 인젝션/자격 증명 스터핑/피싱 운영), 지속성·접근 운영자(Trickbot/Cobalt Strike/PowerShell Empire 후속 활용 처리), 랜섬웨어 배포 운영자. 2023-11-28 작전은 우크라이나에서 **두목 1명**을 체포하고 **4명의 추가 용의자**를 구금하였으며, **30건의 수색**을 집행하고 **100개 이상의 디지털 장비 도구**를 압수하였다. 이는 2021년 첫 라운드의 체포를 산출한 동일한 수사의 연속이었다.

### 3. Kelvin Security 해커-포-하이어 / 데이터 유출 그룹

### 수법(모더스 오페란디)

스페인 내무부(2023-12-11)에 따르면, Kelvin Security는 암호화 기반 갈취가 아닌 데이터 유출 및 재판매를 위해 조직 표적에 대한 침입을 수행하였다. 스페인 보도자료는 알려진 스페인 기반 용의자를 **그룹의 금융 장치 리더**(líder del aparato financiero)로 규정한다 — 즉, 침입 리더가 아닌 수익화 책임자이다.

### 피해자 프로파일 및 영향

스페인 출처는 **3년간 90개국 이상에 걸친 300개 이상의 조직**에 활동을 귀속시키며, 공공 부문 표적을 포함한다. 피해자별 영향 수치는 스페인 보도자료에 게시되지 않는다.

### 자금 흐름

스페인 출처의 혐의에는 자금세탁 범죄가 포함되며, 이는 알리칸테 체포자의 추정 역할인 수익 전환 활동을 시사하지만, 자금세탁 규모 또는 라우팅은 공개하지 않는다.

### 범죄 조직 구조

그룹은 스페인 출처에 의해 세계에서 가장 두드러진 "핵티비스트" 그룹 중 하나로 묘사된다(용어는 느슨하게 사용됨 — 추정 범죄는 금전적 동기). 스페인 출처 혐의에는 범죄조직 가입, 비밀 누설, 컴퓨터 손상, 자금세탁이 포함되며, 이는 별도 역할을 가진 구조화된 그룹을 시사한다; 알리칸테 체포는 구체적으로 금융 장치 리더 역할을 다룬다.

## 참여 당사자

### 기관
- [[fbi-cyber-division|FBI(미국 연방수사국) 사이버부]]
- [[europol-ec3|Europol(유럽 경찰청) EC3]]
- [[eurojust|Eurojust(유럽사법협력기구)]]

### 참여국
- [[united-states|미국]]
- [[norway|노르웨이]]
- [[ukraine|우크라이나]]
- [[spain|스페인]]

> [!info] Legal-basis note
> 3개 단속 작전 전반에 걸친 관련 국가의 완전한 목록은 검증이 필요하다.

## 법적 근거

공식 보도자료들은 3개 작전 전반에 걸쳐 단일 공유된 법적 프레임워크를 노출하지 않는다. 공개된 근거는 국내 형사 절차, 사이버범죄 법규, Eurojust(유럽사법협력기구) 및 Europol(유럽 경찰청)을 통한 사법 조정, 그리고 랜섬웨어 와해를 위한 미국 형사 절차의 혼합으로 보인다.

## 작전 타임라인

| 일자 | 사건 |
|------|-------|
| 2023-11-28 | Eurojust(유럽사법협력기구)가 LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) 연계 활동을 포함한 1,800명 이상의 피해자에 대한 공격과 연관된 랜섬웨어 그룹의 우크라이나에서의 해체 발표 |
| 2023-12-11 | 스페인 내무부가 알리칸테에서 Kelvin Security 연계 용의자의 체포 발표 |
| 2023-12-19 | 미국 법무부가 ALPHV/BlackCat 랜섬웨어 변종의 와해 및 피해자 복호화 지원 발표 |

## 결과 및 영향

| 표적 | 작전 |
|--------|--------|
| ALPHV/BlackCat | 인프라 와해 및 피해자 복호화 지원 |
| LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) 연계 계열 그룹 | 두목 1명 체포, 용의자 4명 구금, 30건 이상의 수색 — Eurojust(유럽사법협력기구) 발표 |
| Kelvin Security | 스페인에서 용의자 1명 체포 |

> [!warning] Scope note
> LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) 관련 공식 유럽 출처는 광범위한 랜섬웨어 계열 네트워크에 관한 것이며, 본 작전을 순수 LockerGoga 단독 테이크다운으로 규정하지 않는다.

## 활용된 협력 메커니즘

공식 출처들은 기술적 와해, 피해자 통지 및 복호화 지원, 다국적 압수수색 및 체포 작전, 그리고 국경 넘는 파트너와 조정된 국내 형사 수사의 조합을 시사한다.

## 한국의 참여

식별된 한국의 관여 없음.

## 모순점 및 미해결 문제

- 각 개별 작전의 정확한 체포 및 압수 건수는 무엇이었는가?
- 3개 단속 작전 전체에서 총 몇 개국이 참여하였는가?
- 3개 그룹 모두에 의한 총 추정 피해는 얼마였는가?
- BlackCat/ALPHV(랜섬웨어) 운영자가 식별되었는가?
- **L26 gap — BlackCat/ALPHV(랜섬웨어) 침입 벡터:** 미국 법무부의 2023-12-19 보도자료는 계열사가 피해자 환경에 초기 접근을 어떻게 획득하였는지 공개하지 않는다.
- **L26 gap — BlackCat/ALPHV(랜섬웨어) 자금 흐름:** 미국 법무부는 2023-12-19 와해 발표의 일환으로 누적 암호화폐 압수 수치 또는 자금세탁 경로 분석을 게시하지 않았다.
- **L26 gap — 우크라이나 LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) 재정 회수:** Eurojust(유럽사법협력기구)는 "수억 유로" 규모의 몸값 수익 중 얼마가 회수되었거나 추적되었는지 공개하지 않는다.
- **L26 gap — Kelvin Security 피해자 영향:** 스페인 출처는 피해자별 손실 수치 또는 300개 이상의 표적 조직 중 실제로 결제하였거나 실질적 데이터 노출을 입은 곳이 어디인지 게시하지 않는다.
- **L26 gap — Kelvin Security OCG 명단:** 알리칸테 "금융 장치 리더" 체포를 넘어, 스페인 출처는 다른 그룹 조직원이나 그들의 지리적 분포를 명명하지 않는다.

## 후속 조치

> [!warning] 공식 법원 문서를 찾을 수 없음
> 웹 검색(2026-04-18)은 본 작전에 대한 공개적으로 접근 가능한
> 법원 서류를 산출하지 않았다. 가능한 이유: 공개 법원 기록 시스템이
> 없는 비미국 관할권, 봉인된 절차, 또는 작전이 공식 기소로
> 이어지지 않음.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- 미국 법무부, 2023-12-19: 미국 법무부가 만연한 ALPHV/Blackcat 랜섬웨어 변종을 와해.
- Eurojust(유럽사법협력기구), 2023-11-28: Eurojust와 Europol이 지원한 주요 국제 작전으로 우크라이나에서 랜섬웨어 그룹 해체.
- 스페인 내무부, 2023-12-11: 세계에서 가장 중요한 핵티비스트 그룹 중 하나의 금융 장치 리더를 스페인 국가경찰이 체포.
- CISA / FBI(미국 연방수사국) / HHS, 2023-12-19: StopRansomware: ALPHV Blackcat.
- BleepingComputer, 2023-12-19: FBI(미국 연방수사국)가 BlackCat 랜섬웨어 작전을 와해하고 복호화 도구를 만들다.

## Evidence and Attribution Notes

- 이것은 2023년 12월 ALPHV/BlackCat 와해 작전에 대한 주요 공식 미국 출처이다.
- Eurojust(유럽사법협력기구)는 71개국 1,800명 이상의 피해자에 대한 공격과 연계된 랜섬웨어 그룹에 대해 7개국 당국이 작전을 펼쳤다고 보고하였다.
- 우크라이나에서의 작전은 두목 1명의 체포, 4명의 용의자 구금, 30건 이상의 수색으로 이어졌다.
- 본 그룹은 최소 수억 유로의 손실과 연관되었다.
- 이것은 LockerGoga(LockerOGA/LockerGoga(랜섬웨어)) 연계 랜섬웨어 활동과 연결된 2023년 11월 말 우크라이나 작전에 대한 공식 유럽 사법 출처이다.
- 스페인 국가경찰은 알리칸테에서 Kelvin Security와 연계된 것으로 추정되는 사람의 체포를 발표하였다.
- 보도자료는 Kelvin Security를 3년간 90개국 이상의 300개 이상의 조직에 대한 공격에 책임이 있는 것으로 묘사하였다.
- 공식 발표는 범죄조직 가입, 비밀 누설, 컴퓨터 손상, 자금세탁을 포함한 추정 범죄를 식별하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- 미국 법무부, 2023-12-19: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs Justice Department Disrupts Prolific ALPHV/Blackcat Ransomware Variant This is archived content from the U.S.
- 미국 법무부, 2023-12-19: 지난 18개월 동안 ALPHV/Blackcat은 전 세계 피해자들이 지불한 수억 달러의 몸값을 기준으로 세계에서 두 번째로 만연한 서비스형 랜섬웨어 변종으로 부상하였다.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a arrest-sweep against BlackCat/ALPHV, LockerGoga-linked affiliate network, Kelvin Security, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Fbi Cyber Division and coordination to Europol Ec3, with participating or affected jurisdictions recorded as United States, Norway, Ukraine, Spain.

The cooperation model is documented through named agencies and partners: Fbi Cyber Division, Europol Ec3, Eurojust; enforcement posture: Arrest, Takedown, Seizure.

Operational results captured for the canonical record: 1 arrests; 500 victims notified; 1 decryption keys recovered; BlackCat/ALPHV infrastructure disrupted; LockerGoga-linked affiliate network hit by searches and detentions in Ukraine; Kelvin Security-linked suspect arrested in Spain.

The canonical source set contains 5 reference(s): 2023 12 19 Justice Gov Justice Department Disrupts Prolific Alphvblackcat Ransomware Variant, 2023 11 28 Eurojust Ransomware Group Dismantled Ukraine Major Operation Supported Eurojust Europol, 2023 12 11 Interior Gob Es Policia Nacional Detiene Lider Kelvin Security, 2023 12 19 Cisa Gov Stopransomware Alphv Blackcat, 2023 12 19 Bleepingcomputer Fbi Disrupts Blackcat Ransomware Operation Creates Decryption Tool.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis, Mechanisms Used, Exact Seizure Counts.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | 발행기관 | 일자 | URL |
|---|-------|----------|------|-----|
| [1] | 미국 법무부가 만연한 ALPHV/Blackcat 랜섬웨어 변종을 와해 | 미국 법무부 | 2023-12-19 | https://www.justice.gov/archives/opa/pr/justice-department-disrupts-prolific-alphvblackcat-ransomware-variant |
| [2] | Eurojust(유럽사법협력기구)와 Europol(유럽 경찰청)이 지원한 주요 국제 작전으로 우크라이나에서 랜섬웨어 그룹 해체 | Eurojust(유럽사법협력기구) | 2023-11-28 | https://www.eurojust.europa.eu/news/ransomware-group-dismantled-ukraine-major-operation-supported-eurojust-europol |
| [3] | 세계에서 가장 중요한 핵티비스트 그룹 중 하나의 금융 장치 리더를 스페인 국가경찰이 체포 | 스페인 내무부 | 2023-12-11 | https://www.interior.gob.es/opencms/en/detail-pages/article/La-Policia-Nacional-detiene-al-lider-del-aparato-financiero-de-uno-de-los-grupos-hacktivistas-mas-importantes-del-mundo/ |
| [4] | #StopRansomware: ALPHV Blackcat | CISA / FBI(미국 연방수사국) / HHS | 2023-12-19 | https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-353a |
| [5] | FBI(미국 연방수사국)가 BlackCat 랜섬웨어 작전을 와해하고 복호화 도구를 만들다 | BleepingComputer | 2023-12-19 | https://www.bleepingcomputer.com/news/security/fbi-disrupts-blackcat-ransomware-operation-creates-decryption-tool/ |
