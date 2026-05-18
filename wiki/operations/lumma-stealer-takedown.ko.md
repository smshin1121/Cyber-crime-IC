> [!note] Source basis
> (한국어 번역: 본 페이지는 공식 Microsoft 및 DOJ(미국 법무부) 자료를 토대로 재작성되었다. 이전 버전은 `sources` 필드가 잘못 구성되어 있었고 활용 가능한 참조 표가 없어, 정당한 국제공조 작전임에도 출처가 빈약한 것처럼 보이게 만들었다.)

## 개요

**Lumma Stealer 테이크다운**은 2025년 5월 21일에 발표된 **LummaC2** infostealer(정보 탈취형 악성코드) 생태계를 대상으로 한 민관 협력 공조 작전이다. 본 작전은 **Microsoft 민사 소송**, **DOJ(미국 법무부) 형사 도메인 압수**, **유럽 측의 Europol(유럽 경찰청) 조정**, **일본 측 인프라 차단 지원**을 결합하였으며, 테이크다운 단계에서 체포가 발표되지는 않았음에도 불구하고 강력한 국제공조 사례에 해당한다.

## 배경

LummaC2는 자격증명, 금융 정보, 암호화폐 지갑 정보를 탈취하는 데 사용된 malware-as-a-service 플랫폼이었다. 본 페이지가 작전 코퍼스에 포함되는 핵심 이유는, 회복력 있는 악성코드 인프라에 대응하기 위해 민간 부문 소송, 형사 압수 권한, 국경을 초월한 작전 조정을 결합하는 하이브리드 차단 모델이라는 현대 사이버범죄 대응의 반복적 패턴을 보여주기 때문이다.

## 참여 당사자

### 정부 / 법 집행기관
- [[us-doj|미국 법무부]]
- [[fbi-cyber-division|FBI(미국 연방수사국)]]
- [[europol-ec3|Europol EC3]]
- [[japan-npa|일본 측 사이버범죄 통제 당국 / JC3 지원]]

### 민간 부문 파트너
- Microsoft Digital Crimes Unit
- Microsoft Threat Intelligence

## 결과 및 영향

| 지표 | 세부 내용 |
|--------|--------|
| 차단된 도메인 | 약 2,300개 |
| Microsoft 싱크홀로 리다이렉트된 도메인 | 1,300개 이상 |
| DOJ가 압수한 핵심 도메인 | 5개 |
| Microsoft가 식별한 감염된 Windows 컴퓨터 | 394,000대 이상 |
| FBI가 식별한 자격증명 탈취 사례 | 최소 170만 건 |

## 활용된 협력 메커니즘

본 작전이 주목할 만한 것은 협력 모델이 출처에서 명시적으로 드러나기 때문이다. Microsoft는 조지아 북부 지구 연방법원의 민사 명령을 활용하였고, DOJ는 형사 압수영장을 사용하였으며, Europol은 유럽 법 집행 조치를 촉진하였고, 일본 측 파트너는 현지 인프라 정지를 지원하였다. 이는 코퍼스 내 후속 DOJ 단독 페이지들보다 민관 국제 차단의 더 명확한 사례에 해당한다.

## 모순점 및 미해결 문제

- 본 작전은 공개적인 체포로 이어지지 않았기 때문에, 운영자 귀속(operator attribution)은 공개 기록상 여전히 불완전하다.
- 일부 공개 요약은 민사 소장 제출, 영장 집행, 공개 발표가 서로 다른 날에 이루어졌기 때문에 조정 일자를 다르게 인용한다.
- 현재의 출처 집합은 차단 메커니즘은 강력하게 뒷받침하지만, 장기적인 운영자 측 결과에 대해서는 뒷받침이 상대적으로 약하다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Microsoft, 2025-05-21: Lumma Stealer 차단 — Microsoft가 사이버범죄 도구로 선호되는 악성코드에 맞서 전 세계적 조치를 주도하다.
- 미국 법무부(U.S. Department of Justice), 2025-05-21: 법무부, 주요 정보 탈취형 악성코드 작전 배후 도메인 압수.
- Microsoft Security Blog, 2025-05-21: Lumma Stealer — 다작 infostealer의 전달 기법 및 역량 분석.
- BleepingComputer, 2025-05-21: Lumma infostealer 악성코드 작전 차단, 도메인 2,300개 압수.
- WIRED, 2025-05-21: 당국, 사이버범죄자들이 대거 사용한 infostealer에 대한 정교한 글로벌 테이크다운 단행.

## 작전 타임라인

- 2025-05-13: 활동 또는 수사 개시.
- 2025-05-21: 공개 발표.
- 2025-05-21: 보고된 집행 종료 시점.
- 2025-05-21: BleepingComputer, Microsoft, Microsoft Security Blog, 미국 법무부의 공개 출처 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: 해킹 및 악성코드.
- 기록된 집행 양태: 압수 및 테이크다운.
- 메타데이터에 기록된 법적 또는 절차적 근거: Budapest Convention(부다페스트 협약).
- 본 기록은 takedown, 상태 completed로 분류된다.

## Evidence and Attribution Notes

- Microsoft는 약 2,300개의 Lumma 관련 도메인이 압수, 차단 또는 리다이렉트되었다고 밝혔다.
- 해당 게시물은 DOJ, Europol EC3, 일본 JC3를 파트너로 명시한다.
- 본 작전의 형사 압수 측면에 대한 주된 출처이다.
- Microsoft는 LummaC2의 malware-as-a-service 구조와 전달 생태계를 상세히 설명한다.
- 해당 게시물은 차단 조치가 약 2,300개의 악성 도메인과 관련됨을 확인한다.
- BleepingComputer는 Microsoft-DOJ-Europol-일본 합동 조치로 Lumma와 연계된 도메인 2,300개가 차단되었다고 보도하였다.
- 해당 기사는 지역 인프라 압수에서 Europol과 일본 사이버범죄대책센터(Japan Cybercrime Control Center)의 역할을 부각하였다.
- WIRED는 Lumma가 Microsoft, DOJ, Europol, 일본이 참여한 공조 조치로 차단되었다고 보도하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- 미국 법무부(U.S. Department of Justice), 2025-05-21: We are grateful for their work and dedication." "Malware like LummaC2 is deployed to steal sensitive information such as user login credentials from millions of victims in order to facilitate a host of crimes, including fraudulent bank transfers and cryptocurrency theft," said Matthew R.
> (한국어 번역: "그들의 노고와 헌신에 감사한다." "LummaC2와 같은 악성코드는 부정 은행 송금 및 암호화폐 절도를 포함한 다양한 범죄를 용이하게 하기 위해 수백만 피해자로부터 사용자 로그인 자격증명과 같은 민감한 정보를 탈취하는 데 사용된다"고 Matthew R.가 말하였다.)
- 미국 법무부(U.S. Department of Justice), 2025-05-21: Together, we are making it harder, and more painful, for cyber criminals to operate." As alleged in the affidavits filed in support of the government's seizure warrants, the administrators of LummaC2 used the seized websites to distribute LummaC2, an information-stealing malware, to their affiliates and other cyber criminals.
> (한국어 번역: "우리는 함께 사이버 범죄자들이 활동하는 것을 더 어렵고 더 고통스럽게 만들고 있다." 정부의 압수영장을 뒷받침하기 위해 제출된 진술서에 적시된 바와 같이, LummaC2 관리자들은 압수된 웹사이트를 이용해 정보 탈취형 악성코드인 LummaC2를 자신들의 제휴 범죄자 및 기타 사이버 범죄자들에게 배포하였다.)

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라 LummaC2 / Lumma Stealer(정보 탈취 악성코드) malware-as-a-service 인프라에 대한 테이크다운을 설명하기 때문에 canonical operation으로 보존된다. 본 기록은 주도 책임을 Us Doj에, 조정 책임을 Europol Ec3에 부여하며, 참여 또는 영향 받은 관할권으로 미국과 일본을 기록한다.

협력 모델은 명시된 기관 및 파트너를 통해 문서화된다: Us Doj, Fbi Cyber Division, Europol Ec3, Japan Npa; 메커니즘: Public Private Cooperation 및 informal cooperation; 법적 근거: Budapest Convention(부다페스트 협약); 집행 양태: 압수 및 테이크다운.

canonical 기록에 포착된 작전 결과: 도메인 2,300개 압수; 1,300개 이상의 도메인이 Microsoft 싱크홀로 리다이렉트됨; DOJ는 Lumma 관리 패널로 사용된 5개의 핵심 도메인을 압수함; Microsoft는 2025년 3월 16일부터 2025년 5월 16일 사이에 394,000대 이상의 감염된 Windows 컴퓨터를 식별함; FBI는 LummaC2와 연계된 최소 170만 건의 자격증명 탈취 사례를 식별함.

canonical 출처 집합은 5건의 참조를 포함한다: 2025 05 21 Microsoft Lumma Stealer Global Action, 2025 05 21 Justice Gov Lumma Stealer Domain Seizures, 2025 05 21 Microsoft Security Blog Lumma Stealer Analysis, 2025 05 21 Bleepingcomputer Com Lumma Infostealer Malware Operation Disrupted 2300 Domains Seized, 2025 05 21 Wired Com Lumma Stealer Takedown Disrupted.
출처 하한선은 canonical operation 기준에 부합하지만, 출처의 폭만으로 모든 후속 체포나 양형이 본 작전의 일부임을 입증하지는 않으므로, 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
현재 본 페이지에는 프런트매터 누락 필드 플래그가 부여되어 있지 않다.
데이터셋 활용 관점에서, 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 공조 집행 조치 전체를 기술한다. 이후의 기소, 유죄 인정, 양형, 범죄인 인도, 몰수 조치는, 출처가 명시적으로 이를 새로운 다국적 작전으로 제시하지 않는 한, 관련 사건으로 첨부되거나 흡수된 후속 기록으로 처리되어야 한다.
출처 기록이 더 광범위한 배경, 반복되는 통신사 재배포, 또는 토픽 페이지성 자료를 포함하는 경우, 본 평가는 명시된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과와 직접 결부되는 사실에 우선순위를 둔다. 주변적 출처 제목은 독립적 분류 또는 결과 근거로 취급되지 않는다.
이로써 canonical 기록은 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Lumma Stealer 차단 — Microsoft가 사이버범죄 도구로 선호되는 악성코드에 맞서 전 세계적 조치를 주도하다 | Microsoft | 2025-05-21 | https://blogs.microsoft.com/on-the-issues/2025/05/21/microsoft-leads-global-action-against-favored-cybercrime-tool/ |
| [2] | 법무부, 주요 정보 탈취형 악성코드 작전 배후 도메인 압수 | U.S. Department of Justice | 2025-05-21 | https://www.justice.gov/opa/pr/justice-department-seizes-domains-behind-major-information-stealing-malware-operation |
| [3] | Lumma Stealer — 다작 infostealer의 전달 기법 및 역량 분석 | Microsoft Security Blog | 2025-05-21 | https://www.microsoft.com/en-us/security/blog/2025/05/21/lumma-stealer-breaking-down-the-delivery-techniques-and-capabilities-of-a-prolific-infostealer/ |
| [4] | Lumma infostealer 악성코드 작전 차단, 도메인 2,300개 압수 | BleepingComputer | 2025-05-21 | https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-operation-disrupted-2-300-domains-seized/ |
| [5] | 당국, 사이버범죄자들이 대거 사용한 infostealer에 대한 정교한 글로벌 테이크다운 단행 | WIRED | 2025-05-21 | https://www.wired.com/story/lumma-stealer-takedown-disrupted/ |
