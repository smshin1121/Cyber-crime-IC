## 개요

Operation Synergia(시너지아 작전, INTERPOL) II는 2024년 4월부터 8월까지 **INTERPOL(국제형사경찰기구) 회원국 95개국**에 걸쳐 악성 사이버 인프라를 겨냥한 대규모 INTERPOL 조정 작전이었다. 본 작전은 피싱, 랜섬웨어, 정보 탈취 인프라에 초점을 맞췄다. 약 30,000개의 의심 IP 주소를 식별하였고 그중 76%(~22,800개)를 적발하였으며, 서버 59대와 전자기기 43대를 압수하고 41명을 검거하였으며 65명이 추가 수사 중이다.

이 작전은 광범위한 민간 부문 파트너십을 동반한 글로벌 규모의 인프라 중심 사이버 작전을 조정할 수 있는 INTERPOL의 고유한 역량을 입증하였다.

## 배경

Operation Synergia II는 INTERPOL의 Synergia 작전 시리즈의 두 번째 반복이었다. Kaspersky의 2024-02-01 파트너측 발표에 따르면, 첫 번째 Operation Synergia(2023년 9월-11월)는 50개 이상의 INTERPOL 회원국에 걸쳐 조정되었으며, 약 1,300대의 의심 서버를 식별하고 그중 약 70%에 대해 조치를 산출하였다.[^synergia1]

[^synergia1]: [[kaspersky-operation-avalanche]]는 레거시 슬러그로 유지되지만, 연결된 Kaspersky 기사는 원본 2023년 Operation Synergia 배경을 다루며 Operation Avalanche를 다루지 않는다.

## 참여 당사자

- **주도:** [[interpol-igci|INTERPOL IGCI]]
- **참여국:** INTERPOL 회원국 95개국
- **민간 부문 파트너:** [[group-ib|Group-IB]], [[trend-micro|Trend Micro]], [[kaspersky-lab|Kaspersky]], Team Cymru

### Notable Country Actions

| 국가 | 조치 |
|---------|--------|
| 홍콩 | 악성 서버 1,037대 적발 |
| 마카오(중국) | 서버 291대 적발 |
| 몽골 | 21개 가옥 수색, 서버 압수, 연관자 93명 식별 |
| 마다가스카르 | 11명 식별, 기기 11대 압수 |
| 에스토니아 | 80GB 이상의 서버 데이터 압수 |

## 결과 및 영향

| 지표 | 값 |
|--------|-------|
| 참여국 | 95 |
| 식별된 의심 IP | ~30,000 |
| 적발 IP | ~22,800 (76%) |
| 압수 서버 | 59 |
| 압수 전자기기 | 43 |
| 검거 | 41 |
| 수사 중 | 65 |

## Cooperation Mechanisms Used

- INTERPOL의 I-24/7 보안 통신망
- 사이버보안 기업과의 민관 정보 공유
- INTERPOL Cyber Fusion Centre 위협 인텔리전스 통합
- 95개국 국가중앙사무국(NCB)

## Korean Involvement (한국의 참여)

Operation Synergia II의 발표된 결과에서 특정한 한국의 참여는 명시되지 않았다.

## Contradictions & Open Questions

- 41건의 검거의 국가별 내역은 무엇인가?
- 수사 중인 65명에 대해 어떤 후속 조치가 이뤄졌는가?
- 민간 부문 파트너의 위협 인텔리전스는 어떻게 작전 기획에 통합되었는가?
- 적발된 피싱/랜섬웨어 인프라에 대한 장기적 영향은 무엇인가?

## Follow-Up Actions

> [!warning] No public court documents found
> 웹 검색(2026-04-17)에서 본 작전에 대한 공개적으로 접근 가능한 법원 문서가
> 발견되지 않았다. 가능한 이유: 공개 법원 기록 시스템이 없는
> 비미국 관할권, 봉인된 절차, 또는 작전이 정식 기소로
> 이어지지 않음.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- INTERPOL, 2024-11-06: INTERPOL 사이버 작전이 악성 IP 주소 22,000개 적발 — Operation Synergia II.
- Kaspersky, 2024-02-01: Kaspersky가 초국가적 사이버범죄 차단 작전에서 INTERPOL과 사이버 위협 데이터 공유(원본 Operation Synergia 배경).
- Kaspersky, 2024-11-05: Kaspersky가 INTERPOL의 Operation Synergia II 지원.
- Group-IB, 2024-11-06: Group-IB가 INTERPOL Operation Synergia II 지원.
- Ars Technica, 2024-11-07: INTERPOL 작전이 악성 IP 주소 22,000개 적발.

## 작전 타임라인

- 2024-04-01: 활동 또는 수사 시작.
- 2024-11-06: 공개 발표.
- 2024-08-31: 보고된 집행 종료 시점.
- 2024-11-05: Kaspersky의 공개 출처 보도.
- 2024-11-06: Group-IB, INTERPOL의 공개 출처 보도.
- 2024-11-07: Ars Technica의 공개 출처 보도.
- 2024-02-01: 원본 Operation Synergia 시리즈에 대한 Kaspersky 배경 출처 보도.

## Legal and Procedural Posture

- 기록된 범죄 분류: 랜섬웨어.
- 본 기록은 infrastructure-seizure로 분류되어 상태는 완료(completed)이다.

## Evidence and Attribution Notes

- Operation Synergia II는 INTERPOL 회원국 95개국이 참여 — 지금까지 가장 광범위한 INTERPOL 사이버 작전 중 하나
- 악성 IP 주소 22,800개 적발(식별된 ~30,000개 중 76%)
- 서버 59대 및 전자기기 43대 압수; 41명 검거
- 강력한 민간 부문 파트너십(Group-IB, Trend Micro, Kaspersky, Team Cymru)
- Kaspersky의 2024-02-01 발표는 원본 2023년 Operation Synergia 시리즈에 대한 배경 사실을 뒷받침하며, Synergia II 집행 총계를 뒷받침하지는 않는다.
- Operation Synergia II의 결과를 발표하는 INTERPOL 보도자료(2024년 4월-8월). INTERPOL 회원국 95개국에 걸쳐 피싱, 랜섬웨어, 정보 탈취 인프라를 겨냥한 대규모 인프라 중심 작전.
- 본 작전은 악성 IP 주소 22,800개 적발, 서버 59대 및 기기 43대 압수, 41명 검거로 이어졌다.
- INTERPOL의 Operation Synergia II는 2024년 4월 1일부터 8월 31일까지 진행되었으며 피싱, 랜섬웨어, 정보 탈취 인프라를 구체적으로 겨냥했다.
- 본 작전은 INTERPOL 회원국 95개국의 법집행기관과 민간 부문 파트너 Group-IB, Trend Micro, Kaspersky, Team Cymru가 함께한 공동 노력이었다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- INTERPOL, 2024-11-06: INTERPOL 사이버 작전이 악성 IP 주소 22,000개 적발 본 작전은 피싱, 정보 탈취, 랜섬웨어를 겨냥했다 GLASGOW, United Kingdom – 글로벌 INTERPOL 작전이 사이버 위협과 연관된 22,000개 이상의 악성 IP 주소 또는 서버를 적발하였다.
- INTERPOL, 2024-11-06: Operation Synergia II(2024년 4월 1일 - 8월 31일)는 피싱, 랜섬웨어, 정보 탈취를 구체적으로 겨냥하였으며, INTERPOL, 민간 부문 파트너, INTERPOL 회원국 95개국 법집행기관의 공동 노력이었다.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

이 페이지는 피고인 특정 후속 조치가 아니라 피싱, 랜섬웨어, 정보 탈취 인프라에 대한 infrastructure-seizure를 기술하기 때문에 정본 작전으로 유지된다. 본 기록은 Interpol Igci에 주도 책임을, Interpol Igci에 조정을 귀속시키며, 참여 또는 영향받는 관할권으로 홍콩, 마카오, 몽골, 마다가스카르, 에스토니아가 기록된다.

협력 모델은 주로 주도/조정 기관과 국가 목록을 통해 가시화되며, 상세한 법적 메커니즘 항목은 빈약하게 남아 있다.

정본 기록에 포착된 작전 결과: 41명 검거; 서버 59대 압수.

정본 출처 집합은 5개의 참조를 포함한다: 2024 11 06 Interpol Operation Synergia Ii, Kaspersky Shares Cyberthreat Data With Interpol In Operation To Disrupt Transnational Cybercrime, 2024 11 05 Kaspersky Com Interpol Operation Synergia Ii, 2024 11 06 Group Ib Com Group Ib Supports Interpol Operation Synergia Ii, 2024 11 07 Arstechnica Com Interpol Operation Synergia Ii 22000 Malicious Ips.
출처 하한은 정본 작전을 위해 충족되지만, 출처의 폭만으로 모든 후속 검거 또는 양형이 본 작전의 일부임을 입증하지는 않는다; 후속 기록은 별도로 연결된 채로 유지되어야 한다.
현재 본 페이지에는 frontmatter missing-field 플래그가 보유되어 있지 않다.
데이터셋 사용을 위해, 이 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 항목은 전체로서 조정된 집행 조치를 기술한다. 이후의 기소, 답변, 양형, 인도 또는 몰수 조치는 출처가 명시적으로 그것들을 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수됨(absorbed) 후속 기록으로 연결되어야 한다.
출처 기록이 보다 광범위한 배경, 반복되는 통신사 재게재, 또는 주제 페이지 자료를 포함할 때, 본 평가는 명명된 작전, 참여 당국, 대상 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적인 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 상태로 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | INTERPOL 사이버 작전이 악성 IP 주소 22,000개 적발 — Operation Synergia II | INTERPOL | 2024-11-06 | https://www.interpol.int/News-and-Events/News/2024/INTERPOL-cyber-operation-takes-down-22-000-malicious-IP-addresses |
| [2] | Kaspersky가 초국가적 사이버범죄 차단 작전에서 INTERPOL과 사이버 위협 데이터 공유 | Kaspersky | 2024-02-01 | https://www.kaspersky.com/about/press-releases/kaspersky-shares-cyberthreat-data-with-interpol-in-operation-to-disrupt-transnational-cybercrime |
| [3] | Kaspersky가 INTERPOL의 Operation Synergia II 지원 | Kaspersky | 2024-11-05 | https://www.kaspersky.com/about/press-releases/kaspersky-supports-operation-synergia-ii |
| [4] | Group-IB가 INTERPOL Operation Synergia II 지원 | Group-IB | 2024-11-06 | https://www.group-ib.com/media-center/press-releases/operation-synergia-ii/ |
| [5] | INTERPOL 작전이 악성 IP 주소 22,000개 적발 | Ars Technica | 2024-11-07 | https://arstechnica.com/security/2024/11/interpol-operation-synergia-ii-takes-down-22000-malicious-ip-addresses/ |
