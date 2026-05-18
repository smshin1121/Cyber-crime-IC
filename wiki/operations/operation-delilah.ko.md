## 개요

**Operation Delilah(델릴라 작전)**는 INTERPOL(국제형사경찰기구)이 조율한 민관 합동 작전으로, SilverTerrier BEC(비즈니스 이메일 침해) 생태계를 대상으로 하였다. INTERPOL 공식 발표에 따르면 [[nigeria-police-force|나이지리아 경찰(Nigeria Police Force)]] 사이버범죄 부서가 1년간의 국제 경찰 협력 끝에 라고스(Lagos)에서 37세 나이지리아인 용의자를 체포하였다.

이 작전은 민간 부문에서 Group-IB, Palo Alto Networks Unit 42, Trend Micro가 제공한 정보 의뢰(intelligence referral)에서 출발하였다. INTERPOL의 Cyber Fusion Centre가 해당 첩보를 보강하였고, 아프리카 작전 데스크(Africa operations desk)가 나이지리아와 사건을 조율하였으며, 호주, 캐나다, 미국으로부터의 법집행 지원이 기록되었다. 이로써 델릴라 작전은 단순한 1인 체포에 그치지 않고, 민관 첩보 사슬(public-private intelligence chain)이 실제 물리적 체포로 전환된 명명된 사례로 평가된다.

## 배경 (Background)

SilverTerrier는 나이지리아의 사이버범죄 클러스터로, 비즈니스 이메일 침해, 대규모 피싱, 자격증명 탈취, 악성코드 기반 사기와 연관된다. 출처 집합은 델릴라를 보다 광범위한 INTERPOL 작전 계열 — 2020년 Operation Falcon I, 2021년 Operation Falcon II, 그리고 2022년 Delilah — 과 연결한다. Group-IB의 출처 요약은 SilverTerrier에 초점을 맞춘 세 차례의 작전이 합쳐서 최소 14명의 추정 조직원 체포로 이어졌다고 기술한다.

## 참여 당사자 (Participating Parties)

| 역할 | 당사자 |
|---|---|
| 조율 | [[interpol|INTERPOL(국제형사경찰기구)]], Cyber Fusion Centre 및 아프리카 작전 데스크 포함 |
| 체포 집행 | [[nigeria-police-force|나이지리아 경찰(Nigeria Police Force)]] 사이버범죄 부서 |
| 민간 첩보 | [[group-ib|Group-IB]], Palo Alto Networks Unit 42, [[trend-micro|Trend Micro]] |
| 명시된 지원 관할권 | [[australia|호주]], [[canada|캐나다]], [[united-states|미국]] |
| 체포 장소 | 라고스 무르탈라 무함메드 국제공항(Murtala Muhammed International Airport), [[nigeria|나이지리아]] |

## 법적 근거 (Legal Framework)

공개된 보도자료는 나이지리아 국내 기소 혐의 또는 법원 서류를 명시하지 않는다. 문서화된 것은 운영 메커니즘이다: 민간 부문 의뢰, INTERPOL 분석적 보강, AFJOC/아프리카 데스크 조율, 다회에 걸친 사건 조율 회의, 그리고 나이지리아 경찰의 체포 집행이 이에 해당한다.

## 작전 타임라인 (Operational Timeline)

| 날짜 | 사건 |
|------|-------|
| 2021년 5월 | INTERPOL의 AFJOC/아프리카 데스크 역량 강화 체계가 가동 중이었고, 델릴라 의뢰 절차가 시작되었다. |
| 2021-2022년 | INTERPOL과 파트너들이 용의자의 온라인 및 오프라인 동선을 추적하였다. |
| 2022년 3월 | 나이지리아 경찰이 라고스 공항에서 용의자를 체포하였다. |
| 2022-05-25 | INTERPOL, Group-IB, CyberScoop, BleepingComputer, Unit 42가 조율된 공개 보도를 게재하였다. |

## 결과 및 영향 (Results and Impact)

- 나이지리아에서 SilverTerrier 연계 고위 용의자 1명 체포.
- 해당 용의자는 출처 보도에서 기업과 개인을 표적으로 한 대규모 피싱 및 BEC 사기 수법과 연관되었다.
- 보안 업계 보고는 해당 용의자를 수백 개의 도메인 및 수십 건의 악성코드 명령제어(C2) 사용과 연결한다. 이는 귀속(attribution) 사실이며 별개의 체포 수치가 아니다.
- 델릴라 작전은 INTERPOL이 SilverTerrier를 Falcon I, Falcon II, Delilah에 걸쳐 반복적 법집행 표적으로 다루었음을 확증한다.

## 활용된 협력 메커니즘 (Cooperation Mechanisms Used)

가장 명확하게 문서화된 메커니즘은 민관 첩보의 실효화(conversion)이다: 보안 업체 텔레메트리와 OSINT가 INTERPOL에 의뢰되었고, INTERPOL 분석관들에 의해 보강되었으며, 아프리카 작전 데스크를 통해 조율된 후 나이지리아 경찰에 의해 집행되었다. 또한 호주, 캐나다, 미국의 명시된 지원과 함께 사건 조율 회의(case-coordination meetings)가 활용되었다.

## 한국의 참여 (Korean Involvement)

현재 출처 집합에서 한국의 참여는 확인되지 않는다.

## 모순 및 미해결 질문 (Contradictions & Open Questions)

- 나이지리아의 기소, 유죄 판결, 양형 기록은 현지 자료군에서 여전히 확인 불가하다.
- 공개 출처들은 여러 국가로부터의 법집행 지원 협력을 언급하지만, 4대륙 조율 주장에 대한 완전한 국가별 참여 목록을 공개하지는 않는다.
- Palo Alto Networks Unit 42는 출처이자 명시된 기여자이지만, 현재 위키 분류 체계에는 별도의 조직 페이지가 존재하지 않는다.

## 후속 조치 (Follow-Up Actions)

> [!warning] No public court documents found
> (한국어 번역: 2026-04-17 웹 검색 결과 이 작전에 대해 공개적으로 접근 가능한 법원 서류가 확인되지 않았다. 가능한 사유: 공개 법원 기록 시스템이 없는 비미국 관할권, 봉인된 절차, 또는 작전이 정식 기소로 이어지지 않은 경우이다.)

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Group-IB, 2022-05-25: Group-IB: Operation Delilah — Interpol Nabs Suspected Leader of Transnational Phishing Ring.
- CyberScoop, 2022-05-25: CyberScoop: Operation Delilah (SilverTerrier BEC).
- INTERPOL, 2022-05-25: Suspected head of cybercrime gang arrested in Nigeria.
- BleepingComputer, 2022-05-25: Interpol arrests alleged leader of the SilverTerrier BEC gang.
- Palo Alto Networks Unit 42, 2022-05-25: Operation Delilah Helps Identify Business Email Compromise Actor.

## Evidence and Attribution Notes

- Group-IB는 2022-05-25경 Operation Delilah — INTERPOL 주도, Group-IB·Palo Alto Networks Unit 42·Trend Micro의 첩보 지원 — 이 2022년 3월 라고스 무르탈라 무함메드 국제공항에서 37세 나이지리아 남성을 체포하는 결과로 이어졌다고 발표하였다.
- 해당 용의자는 2015년 이래로 BEC 및 대규모 피싱 캠페인을 운영해 온 SilverTerrier 사이버범죄 신디케이트의 고위 지도부로 추정된다.
- Delilah는 SilverTerrier에 초점을 맞춘 *세 번째* INTERPOL 작전으로, 2020년 11월 Operation Falcon I 및 2021년 Operation Falcon II에 이어진다. 세 작전을 합산하면 최소 14명의 추정 SilverTerrier 조직원 체포로 이어졌다.
- 첩보 사슬: Group-IB, Unit 42, Trend Micro가 초기 위협 첩보 의뢰를 제공 → INTERPOL Cyber Fusion Centre 분석관들이 이를 보강 → 나이지리아 경찰이 공항에서 물리적 체포 집행(수개월간의 용의자 동선 추적).
- Operation Delilah의 법집행 조율은 4대륙(유럽, 아시아, 아프리카, 호주 포함)의 경찰 기관에 걸쳤다.
- 국제공조 연구상의 의의: 델릴라 작전은 세 곳의 상용 사이버보안 업체가 INTERPOL 조율 체포를 견인한 *민관 첩보 사슬*의 드문 운영적 구현 사례이며, 이후 Africa Cyber Surge II(2023)에서 활용된 패턴이다.
- INTERPOL의 Operation Delilah는 2022년 3월, 2021년 체포를 피해 도주한 후 나이지리아 재입국을 시도하다 검거된 37세 나이지리아 남성 — SilverTerrier BEC 사기 네트워크의 고위 인물로 식별 — 의 체포로 이어졌다.
- 연구자들(Palo Alto Networks Unit 42, Group-IB, Trend Micro)은 해당 용의자의 가명으로 등록된 240개 이상의 도메인을 추적하였으며, 그중 50개 이상이 악성코드 명령제어용으로 사용되었다. 이 그룹은 2014년 이래 약 50,000명의 피해자를 표적으로 한 것으로 평가된다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- INTERPOL, 2022-05-25: 용의자의 체포는 민간 파트너로부터 처음 공유된 정보에 따라 진행된 1년간의 국제 경찰 협력에 이어 이루어졌다.
- INTERPOL, 2022-05-25: 싱가포르: 나이지리아 경찰의 사이버범죄 부서는 INTERPOL 사이버범죄국 내 최근 설립된 아프리카 작전 데스크가 조율·지원한 4대륙에 걸친 국제 작전을 통해 37세 나이지리아 남성을 체포하였다.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

이 페이지는 피고인 단위의 후속 조치가 아니라 INTERPOL이 조율한 SilverTerrier BEC 법집행 작전을 기술하므로 정본 작전(canonical operation)으로 유지된다. 기록은 주도 책임과 조율을 INTERPOL에 귀속시키며, 나이지리아를 체포 관할권으로, 호주, 캐나다, 미국을 명시된 지원 관할권으로 기록한다.

협력 모델은 민간 부문 의뢰, INTERPOL Cyber Fusion Centre 보강, AFJOC/아프리카 데스크 조율, 나이지리아 경찰 체포 집행을 통해 가시화된다.

정본 기록에 담긴 작전 결과: SilverTerrier 연계 고위 용의자 1명 체포; Group-IB, Unit 42, Trend Micro의 첩보가 법집행 조치로 전환됨.

정본 출처 집합에는 5건의 참고문헌이 포함된다: Group Ib Operation Delilah Silverterrier Bec, Cyberscoop Operation Delilah Silverterrier Bec, 2022 05 25 Interpol Int Suspected Head Of Cybercrime Gang Arrested In Nigeria, 2022 05 25 Bleepingcomputer Com Interpol Arrests Alleged Leader Of The Silverterrier Bec Gang, 2022 05 25 Unit42 Paloaltonetworks Com Operation Delilah Business Email Compromise Actor.
정본 작전을 위한 출처 하한선은 충족되었으나, 출처의 폭만으로 모든 하위 체포 또는 양형 조치가 이 작전의 일부임을 증명하지는 못한다. 후속 기록은 별도로 연결되어야 한다.
현재 이 페이지에 부착된 frontmatter 결측 필드 플래그는 없다.
데이터셋 활용 관점에서, 이 페이지는 작전 단위 집계점(operation-level aggregation point)으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조율된 법집행 조치 전체를 기술한다. 이후의 기소, 답변, 양형, 인도, 몰수 조치는 출처가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 부착되어야 한다.
출처 기록이 광범위한 배경, 반복적인 통신사 재발행, 또는 토픽 페이지 성격의 자료를 포함할 때, 본 평가는 명명된 작전, 그 참여 당국, 그 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 법집행 결과와 직접 결부된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이로써 정본 기록은 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌 (References)

| # | 제목 | 발행처 | 날짜 | URL |
|---|---|---|---|---|
| [1] | Group-IB: Operation Delilah — Interpol Nabs Suspected Leader of Transnational Phishing Ring | Group-IB | 2022-05-25 | https://www.group-ib.com/media-center/press-releases/interpol-gib-delilah/ |
| [2] | CyberScoop: Operation Delilah (SilverTerrier BEC) | CyberScoop | 2022-05-25 | https://cyberscoop.com/silverterrier-interpol-nigeria-bec/ |
| [3] | Suspected head of cybercrime gang arrested in Nigeria | INTERPOL | 2022-05-25 | https://www.interpol.int/en/News-and-Events/News/2022/Suspected-head-of-cybercrime-gang-arrested-in-Nigeria |
| [4] | Interpol arrests alleged leader of the SilverTerrier BEC gang | BleepingComputer | 2022-05-25 | https://www.bleepingcomputer.com/news/security/interpol-arrests-alleged-leader-of-the-silverterrier-bec-gang/ |
| [5] | Operation Delilah Helps Identify Business Email Compromise Actor | Palo Alto Networks Unit 42 | 2022-05-25 | https://unit42.paloaltonetworks.com/operation-delilah-business-email-compromise-actor/ |
