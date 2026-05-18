## 개요

**2026-04-27**, 미 법무부(DOJ)는 중화인민공화국 국적자인 **Xu Zewei(徐泽伟, 34세)** 가 그 직전 주말에 이탈리아로부터 미국으로 범죄인 인도되었으며, **휴스턴(텍사스 남부지방법원, S.D. Texas)** 에서 2020년 2월부터 2021년 6월 사이의 컴퓨터 침해 행위에 대한 **9개 죄목의 기소장(9-count indictment)** 으로 미국 연방법원 첫 출정을 가졌다고 발표하였다. Xu는 **2025년 7월 밀라노 말펜사 공항(Milan Malpensa airport)** 에서 체포되었으며, 약 9개월 후에 범죄인 인도되었다. 그의 공동 피고인 **Zhang Yu(张宇, 44세)** 또한 중화인민공화국 국적자이며, **여전히 도주 중**이다.

법원 문서에 따르면, 중국 국가안전부(MSS) **상하이 국가안전국(Shanghai State Security Bureau, SSSB)** 의 관료들이 Xu의 해킹을 지휘하였다. Xu가 본 침해 행위를 수행할 당시, 그는 중국 정부를 위한 해킹을 수행한 다수의 PRC 조력 기업 중 하나인 **Shanghai Powerock Network Co. Ltd. (Powerock)** 에서 일한 것으로 알려져 있다.

## 사실관계

### 1단계 (2020년 초반): COVID-19 연구 침해

2020년 초, Xu와 공모자들은 **COVID-19 백신, 치료, 검사 관련 연구를 수행하는 미국 소재 대학, 면역학자, 바이러스학자들을 해킹하거나 그 외 방식으로 표적으로 삼았다**. Xu는 자신의 활동을 해킹을 감독·지휘한 SSSB 관료들에게 보고하였다. 예시:

- **2020-02-19**: Xu는 SSSB 관료에게 텍사스 남부지방법원 관할 내 소재 연구 대학의 네트워크를 침해했다는 사실을 확인하여 보고하였다.
- **2020-02-22**: 해당 SSSB 관료는 Xu에게 동 대학에서 COVID-19 연구에 종사하는 **바이러스학자 및 면역학자들** 의 특정 이메일 계정(메일박스)을 표적으로 삼아 접근할 것을 지시하였다. Xu는 이후 연구자들의 메일박스 내용을 획득했음을 SSSB 관료에게 확인 보고하였다.

### 2단계 (2020년 후반 — 2021년 초): HAFNIUM(HAFNIUM, 중국 국가배후 APT) Microsoft Exchange 캠페인

2020년 후반부터, Xu와 공모자들은 **Microsoft Exchange Server** 의 특정 취약점들을 익스플로잇하였다. 이들의 익스플로잇은 공개적으로 **"HAFNIUM(HAFNIUM, 중국 국가배후 APT)"** 으로 알려진 대규모 캠페인의 최전선에 있었다.

- **2021년 3월**: Microsoft가 중국에 거점을 둔 국가 후원 해커들에 의한 침해 캠페인을 공개적으로 알렸다.
- **2021-03-10**: FBI(미 연방수사국) + CISA가 Microsoft Exchange Server 침해에 관한 공동 권고(Joint Advisory)를 발표하였다.
- **2021년 3월 (말)**: 미국 소재 Microsoft Exchange Server 가동 컴퓨터들 위에 수백 개의 웹쉘(web shell)이 잔존하였다.
- **2021년 4월**: 미 법무부(DOJ)가 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 행위자들에 의해 취약해진 미국 내 수백 대의 컴퓨터에 대한 법원 허가 원격 조치 작전(remediation operation)을 발표하였다.
- **2021년 7월**: 미국과 해외 파트너들이 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 캠페인을 **중국 국가안전부(MSS)** 의 소행으로 귀속(attribution)시켰다.

기소장은 Xu와 공모자들이 설치한 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 귀속 웹쉘들이 당시 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 행위자들에게 고유한 것이었다고 주장한다. **HAFNIUM(HAFNIUM, 중국 국가배후 APT)은 미국 내 총 12,700개 이상의 기관을 침해**하였다. Xu의 구체적 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 피해자들 중에는 텍사스 남부지방법원 관할 내 또 다른 대학과, **워싱턴 D.C.를 포함하여 전 세계에 사무소를 둔 한 로펌**이 포함된다. Xu와 공모자들은 해당 로펌의 네트워크에 대한 무단 접근을 통해 **메일박스에서 정보를 절취**하였고, **"Chinese sources(중국 소식통)", "MSS(중국 국가안전부)", "HongKong(홍콩)"** 을 포함한 검색어로 메일박스를 탐색하였다.

### 조정(coordination)

Xu와 Zhang은 SSSB 관료들의 감독과 지휘 아래 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 침해 행위에서 협력하였다. 예시:

- **2021-01-30**: Xu는 Zhang에게 다른 텍사스 대학의 네트워크를 침해했다고 확인하였다.
- **2021-02-28**: Xu는 SSSB 관료에게 성공적 침해 사항을 갱신 보고하였고, 해당 SSSB 관료는 Xu에게 두 번째 SSSB 관료로부터 또 다른 성공적 침해 목록을 입수할 것을 지시하였다.

## 국제공조 요소

| 요소 | 세부사항 |
|---|---|
| 해외 체포 | 이탈리아 — 밀라노 말펜사 공항, 2025년 7월 |
| 신병 이송 경로 | 이탈리아 → 미국 (2026-04-25에서 2026-04-26 주말) — 체포에서 범죄인 인도까지 약 9개월 |
| 범죄인 인도 채널 | 미 법무부 국제업무국(OIA) + 이탈리아 국가경찰 — 사이버부서(Polizia Postale) |
| FBI(미 연방수사국) 주관 | 휴스턴 현장사무소(Houston Field Office) |
| 검찰관 | AUSA Mark McIntyre (텍사스 남부지방법원) + 부수석 Matthew Anzaldi (NSD 국가안보 사이버 섹션) |
| 피고인 국적 | 중국 (Xu Zewei, Zhang Yu) |
| 명시적으로 거명된 협력 국가 | 미국 (주도), 이탈리아 |
| 국가 후원 귀속 | 중국 (중국 국가안전부(MSS) — 상하이 국가안전국) |

## 법적 분석

### 관할

미 연방 관할권은 텍사스 기반 대학 피해자들(1단계 + 2단계) 및 워싱턴 D.C.를 포함한 전 세계 사무소 보유 로펌(2단계)을 통해 텍사스 남부지방법원(휴스턴 지부)에 성립하였다. 피고인 Xu는 2025년 7월 밀라노 말펜사에서의 체포 이후 이탈리아로부터 범죄인 인도되었다.

### 기소 죄목

- **전신사기 공모(Conspiracy to commit wire fraud)** (18 U.S.C. § 1349) — 최대 20년.
- **전신사기 2건(Two counts of wire fraud)** (18 U.S.C. § 1343) — 죄목당 최대 20년.
- **보호 컴퓨터에 대한 무단 접근으로 손상을 야기하고 정보를 획득하며, 전신사기를 범하고, 신원도용을 범하기 위한 공모** — 최대 5년.
- **보호 컴퓨터에 대한 무단 접근으로 정보를 획득한 2건** — 죄목당 최대 5년.
- **보호 컴퓨터에 대한 고의적 손상 2건** — 죄목당 최대 10년.
- **가중 신원도용(Aggravated identity theft)** — 최대 2년.

### 선례적 가치

본 사건은 **중국 국가 후원 사이버 행위자에 대한 이탈리아발 범죄인 인도원(extradition source) 으로서의 이탈리아** 의 첫 위키 기록이며 — 제3자 보도에서 "드문(rare)" 것으로 평가된다. 본 사건은 Xu Zewei + Zhang Yu(중국 국가안전부 상하이 국가안전국의 지휘를 받은 Powerock 컨트랙터)를 [[us-v-wu-haibo-isoon|US v. Wu Haibo (iSoon(중국 사이버보안 컨트랙터))]] 및 [[isoon-apt27-indictment|iSoon APT27 기소]]와 함께 위키의 PRC 조력 기업 기소 코퍼스에 추가한다. 솅겐 지역 신병 확보 + 범죄인 인도 경로는 러시아 조직 랜섬웨어 행위자들에 대한 [[us-v-deniss-zolotarjovs|Zolotarjovs / 조지아]], [[us-v-stryzhak-nefilim|Stryzhak / 스페인]], [[us-v-vardanyan-avetisyan-ryuk-ransomware|Vardanyan / 우크라이나 + Avetisyan / 프랑스 계류 중]] 의 솅겐 지역 경로와 구조적으로 유사하다.

## 진행 경과 타임라인

| 일자 | 사건 |
|---|---|
| 2020-02 — 2021-06 | Xu와 Zhang의 혐의 해킹 활동 기간 |
| 2020-02-19 | Xu가 텍사스 남부 연구 대학(COVID-19 연구 표적) 침해를 확인 보고 |
| 2020-02-22 | SSSB 관료가 Xu에게 바이러스학자/면역학자 메일박스 표적 지시 |
| 2021-01-30 | Xu가 Zhang에게 또 다른 텍사스 남부 대학의 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 침해 확인 |
| 2021-02-28 | Xu가 SSSB 관료에게 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 침해 사항 보고 |
| 2021-03 | Microsoft가 HAFNIUM(HAFNIUM, 중국 국가배후 APT)을 공개 |
| 2021-03-10 | FBI(미 연방수사국) + CISA, Microsoft Exchange Server 침해 관련 공동 권고 |
| 2021-04 | 미 법무부, HAFNIUM(HAFNIUM, 중국 국가배후 APT) 취약 미국 컴퓨터들에 대한 법원 허가 원격 조치 작전 |
| 2021-07 | 미국 + 해외 파트너들이 HAFNIUM(HAFNIUM, 중국 국가배후 APT)을 중국 국가안전부(MSS) 소행으로 귀속 |
| (일자 미명시) | 텍사스 남부지방 연방 대배심이 Xu Zewei + Zhang Yu 기소(9개 죄목) |
| 2025-07 | Xu Zewei가 밀라노 말펜사 공항에서 체포 |
| 2026-04 | 이탈리아의 범죄인 인도 결정 |
| 2026-04-25/26 | Xu가 이탈리아로부터 미국으로 범죄인 인도 |
| 2026-04-27 | Xu의 미국 연방법원 첫 출정(휴스턴); DOJ 공식 발표 |

## 협력의 실효성

본 사건은 중국 국가 후원 사이버 행위자에 대한 미-이탈리아 간 범죄인 인도 경로의 성공적 사례를 보여주며 — 제3자 보도에서 "드문(rare)" 것으로 묘사된다. 이탈리아 국가경찰 사이버부서(Polizia Postale)는 FBI(미 연방수사국) 사이버국 보조 국장 Brett Leatherman으로부터 밀라노 체포 및 범죄인 인도의 파트너십 주도 기관으로 명시적으로 인정받았다. 미 법무부 국제업무국(OIA)이 공식 범죄인 인도를 확보하였다. 2025년 7월 체포와 2026년 4월 범죄인 인도 사이의 9개월 간격은 위키에서 추적된 다른 솅겐 지역 범죄인 인도 일정과 유사한 수준이다.

## 한국 관련성

인용된 DOJ 발표문에서 대한민국은 피해국, 출처, 협력 관할권으로 거명되지 않았다. 본 사건은 중국 국가 후원 사이버 행위자에 대한 이탈리아발 범죄인 인도원(extradition source) 패턴, PRC 조력 기업 아키텍처 문서화, 그리고 HAFNIUM(HAFNIUM, 중국 국가배후 APT) Microsoft Exchange 침해 규모(미국 내 12,700개 이상 기관)를 이유로 위키에 기록된다. HAFNIUM(HAFNIUM, 중국 국가배후 APT)의 광범위한 피해자군에는 전 세계 Microsoft Exchange 설치 기반을 고려할 때 한국 기관도 *거의 확실히* 포함되었을 것이나, 본 발표문에서 한국 피해자는 열거되어 있지 않다.

## 모순 및 미해결 질문

- 인용된 발표문은 피해 텍사스 남부 대학들 또는 전 세계 사무소 보유 로펌의 구체적 명칭을 열거하지 않는다.
- 2025년 7월 Xu의 밀라노 말펜사 공항 체포의 구체적 일자는 명시되어 있지 않다(단지 "2025년 7월"로만 표기).
- 이탈리아 범죄인 인도 결정의 구체적 일자는 인용된 DOJ 발표문에 명시되어 있지 않다(제3자 보도는 2026-04-26으로 인용함).
- 도주 중인 Zhang Yu의 위치 상태는 명시되어 있지 않다.
- 텍사스 남부 대학과 전 세계 사무소 보유 로펌 외 구체적인 HAFNIUM(HAFNIUM, 중국 국가배후 APT) 귀속 기관들은 열거되어 있지 않다(12,700개 이상의 수치는 누적값이다).
- Xu와 Zhang 외 다른 공모자들이 기소되어 있는지 여부는 명시되어 있지 않다.

## 참고문헌

| # | 출처 | 발행처 | 일자 | URL |
|---|---|---|---|---|
| [1] | [[2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy\|Prolific Chinese State-Sponsored Contract Hacker Extradited from Italy]] | 미 법무부(DOJ) 공보실(OPA), 보도자료 26-404 | 2026-04-27 | https://www.justice.gov/opa/pr/prolific-chinese-state-sponsored-contract-hacker-extradited-italy |
| [2] | [[2026-04-27_commissariatodips-it_estradizione-hacker-cinese-hafnium-italia-stati-uniti\|Commissariato di P.S. on-line — IT-US extradition of PRC HAFNIUM-campaign hacker Xu Zewei (Malpensa Jul 2025 arrest → Milan Apr 2026 extradition)]] | 이탈리아 국가경찰(Polizia di Stato) — 우편·사이버보안 경찰청(Servizio Polizia Postale e per la Sicurezza Cibernetica) | 2026-04-27 | https://www.commissariatodips.it/notizie/articolo/la-polizia-di-stato-esegue-lestradizione-di-un-pericoloso-hacker-cinese/index.html |
