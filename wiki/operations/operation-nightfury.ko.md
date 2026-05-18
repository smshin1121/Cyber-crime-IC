## 개요

**Operation NightFury(나이트 퓨리 작전)**는 INTERPOL(인터폴)이 조율한 작전으로, **GetBilling** JavaScript 스키머를 사용한 **Magecart**식 웹 스키밍 공격에 가담한 **인도네시아 국적자 3명**의 검거로 이어졌다. 이 작전은 INTERPOL, 인도네시아 법집행기관, 그리고 결정적 정보를 제공한 민간 사이버보안 기업 **Group-IB** 간의 협력을 통해 진행되었다.

이번 검거는 동남아시아에서 활동하던 Magecart 계열 웹 스키밍 조직에 대한 의미 있는 조치였다.

## 배경

Magecart는 전자상거래 웹사이트에 악성 JavaScript 코드를 삽입하여 결제 과정에서 결제 카드 데이터를 탈취하는 사이버범죄 조직과 기법을 통칭하는 용어이다. GetBilling 변종은 검거된 피의자들이 사용한 특정 스키머 도구였다. 피의자들은 수백 개의 전자상거래 웹사이트를 침해하여 의심하지 않는 쇼핑객들로부터 신용카드 정보를 탈취하였다.

## 참여 주체

### 조율 기관
- [[interpol|INTERPOL(인터폴)]]

### 참여 국가
- [[indonesia|인도네시아]]
- [[singapore|싱가포르]]

### 민간 부문 지원
- Group-IB (위협 인텔리전스 및 기술 분석)

## 법적 근거

공개 출처에 구체적인 법적 수단은 명시되어 있지 않다.

## 작전 타임라인

| 일자 | 사건 |
|------|-------|
| 2020년 이전 | Group-IB 인텔리전스 지원을 받은 수사 |
| 2020-01-24 | 인도네시아 내 3명 검거 발표 |

## 결과 및 영향

| 지표 | 수치 |
|--------|-------|
| 검거 | 3명 |
| 관여 국가 | 2개국 (+ INTERPOL 조율) |

## 활용된 협력 메커니즘

INTERPOL의 조율 하에 현지 법집행기관과의 협력이 이루어졌으며, Group-IB의 민간 부문 위협 인텔리전스가 이를 뒷받침하였다.

## 한국의 참여 (한국의 참여)

한국의 참여는 확인되지 않았다. 한국의 전자상거래 사이트 또한 Magecart식 공격의 잠재적 표적이 될 수 있다.

## 모순 및 미해결 쟁점

- GetBilling 조직에 의해 침해된 웹사이트는 몇 개였는가?
- 이 조직에 귀속된 금전적 피해 규모는 얼마였는가?
- 피의자들은 유죄 판결 및 양형을 받았는가?
- 작전에서 싱가포르의 구체적 역할은 무엇이었는가?

## 후속 조치

> [!warning] No public court documents found
> 웹 검색(2026-04-17)에서 본 작전에 대한 공개적으로 접근 가능한
> 법원 문서는 확인되지 않았다. 가능한 사유: 공개 법원기록 시스템이
> 없는 비미국 관할권, 비공개 절차, 또는 작전이 공식 기소로
> 이어지지 않았을 가능성.

<!-- SOURCE_ENRICHMENT_START -->

## 출처 커버리지

- Group-IB, 2020-01-24: Group-IB: Night Fury — Magecart/GetBilling 운영자에 대한 INTERPOL 조율 검거.
- CyberScoop, 2020-01-27: CyberScoop: 인도네시아 경찰, Magecart식 공격 혐의로 3명 검거 (Operation NightFury / GetBilling).
- TechTarget, 2020-01-28: 인터폴 작전으로 Magecart 피의자 3명 검거.
- BleepingComputer, 2020-01-27: 첫 MageCart 해커 검거, 수백 개 웹 스토어 감염.
- The Hacker News, 2020-01-25: 인터폴, Magecart 공격 혐의 인도네시아 신용카드 해커 3명 검거.
- Infosecurity Magazine, 2020-01-28: 인도네시아에서 Magecart 해커 피의자 검거.

## 증거 및 귀속 노트

- 2020년 1월 24일, INTERPOL ASEAN 사이버범죄 작전 데스크는 Operation Night Fury의 결과를 발표하였으며, 이는 'GetBilling'으로 알려진 Magecart식 JavaScript 웹 스키밍 작전에 가담한 인도네시아 국적자 3명의 검거로 이어졌다
- 민간 부문 발단: 본 작전은 싱가포르 소재 사이버보안 기업 Group-IB가 제공한 인텔리전스에 의해 추진되었으며, 이 기업은 2018년부터 GetBilling을 추적해 왔으며 전 세계 수백 개의 침해된 전자상거래 사이트와 해당 조직을 연결하는 인프라를 식별해 왔다
- 기술적 프로파일: GetBilling은 난독화된 JavaScript 스키머를 배포하여 전자상거래 결제 페이지에 삽입하고 고객 결제 카드 데이터, 배송 정보 및 개인정보를 유출시켰다 — 이는 Magecart의 전형적 패턴이다
- 침해 범위: Group-IB 보고서에 따르면 GetBilling은 여러 국가에 걸쳐 '수백 개'의 온라인 스토어를 침해하였으며, 피해자가 아시아·태평양, 유럽 및 북미에 걸쳐 분포한다는 확인 외에 구체적인 국가 목록은 공개되지 않았다
- Operation Night Fury는 또한 INTERPOL의 보다 광범위한 ASEAN 'Operation Goldfish Alpha/Night Fury' 보고에 통합되었으며, 단독 명명된 작전이 아닌 지역 사이버위협 대응의 일부로서 검거가 제시되었다
- 역사적 의의: 이는 전 세계적으로 공식 발표된 최초의 Magecart 운영자 검거 중 하나였다 — 보다 광범위한 Magecart 우산 조직(최소 20개의 별개 그룹으로 추정)은 2015년부터 보안 연구자들에 의해 추적되어 왔으나 본 인도네시아 조치 전까지 성공적인 검거가 없었다
- 인도네시아 남성 3명은 2019년 12월 20일 자카르타와 욕야카르타에서 Magecart식 웹 스키밍 공격으로 체포되었으며, INTERPOL은 2020년 1월 27일 이를 'Operation NightFury'로 발표하였다
- 피의자들은 유죄가 인정될 경우 인도네시아 법률에 따라 최대 10년의 징역에 처해질 수 있었다

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본 작전 평가

본 페이지는 피고인별 후속 조치가 아닌 Magecart/GetBilling 웹 스키밍 조직에 대한 검거 작전을 기술하므로 정본 작전(canonical operation)으로 유지된다. 본 기록은 주도 책임을 Interpol에, 조율을 Interpol에 귀속시키며, 참여 또는 영향을 받은 관할권으로 인도네시아와 싱가포르를 기록하고 있다.

협력 모델은 명명된 기관 및 파트너를 통해 문서화되어 있다: Interpol 및 인도네시아 경찰.

정본 기록에 포착된 작전 결과: 3명 검거.

정본 출처 집합에는 6건의 참고문헌이 포함되어 있다: Group Ib Operation Nightfury Magecartgetbilling, Cyberscoop Operation Nightfury Magecartgetbilling, 2020 01 28 Techtarget Com 3 Magecart Suspects Arrested In Interpol Operation, 2020 01 27 Bleepingcomputer Com First Magecart Hackers Caught Infected Hundreds Of Web Stores, 2020 01 25 Thehackernews Com Interpol Arrests 3 Indonesian Credit Card Hackers For Magecart Attacks, 2020 01 28 Infosecurity Magazine Suspected Magecart Hackers Arrested In Indonesia.
정본 작전 요건의 출처 하한선은 충족되었으나, 출처의 폭만으로는 모든 하류의 검거 또는 양형이 본 작전의 일부임을 입증하지 못한다; 후속 기록은 별도로 연결된 채 유지되어야 한다.
본 페이지에는 현재 frontmatter의 missing-field 표시가 없다.
데이터셋 활용에 있어, 본 페이지는 작전 수준의 집계 기준점으로 취급되어야 한다: 국가·기관·메커니즘·결과 필드는 조율된 집행 행동 전체를 기술한다. 이후의 기소, 유죄인정, 양형, 인도, 자산 몰수 조치는 별도 사건 또는 흡수된 후속 기록으로 연결되어야 하며, 다만 출처가 이를 새로운 다국적 작전으로 명시적으로 제시하는 경우에는 그러하지 아니하다.
출처 기록이 보다 광범위한 배경, 반복되는 통신사 재배포, 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 결부된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립된 분류 또는 결과 증거로 취급되지 않는다.
이를 통해 정본 기록은 분석적으로 한정되고 재현 가능하게 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Group-IB: Night Fury — Magecart/GetBilling 운영자에 대한 INTERPOL 조율 검거 | Group-IB | 2020-01-24 | https://www.group-ib.com/media-center/press-releases/night-fury/ |
| [2] | CyberScoop: 인도네시아 경찰, Magecart식 공격 혐의로 3명 검거 (Operation NightFury / GetBilling) | CyberScoop | 2020-01-27 | https://cyberscoop.com/magecart-arrest-indonesia-interpol-getbilling/ |
| [3] | 인터폴 작전으로 Magecart 피의자 3명 검거 | TechTarget | 2020-01-28 | https://www.techtarget.com/searchsecurity/news/252477470/3-Magecart-suspects-arrested-in-Interpol-operation |
| [4] | 첫 MageCart 해커 검거, 수백 개 웹 스토어 감염 | BleepingComputer | 2020-01-27 | https://www.bleepingcomputer.com/news/security/first-magecart-hackers-caught-infected-hundreds-of-web-stores/ |
| [5] | 인터폴, Magecart 공격 혐의 인도네시아 신용카드 해커 3명 검거 | The Hacker News | 2020-01-25 | https://thehackernews.com/2020/01/indonesian-magecart-hackers.html?m=1 |
| [6] | 인도네시아에서 Magecart 해커 피의자 검거 | Infosecurity Magazine | 2020-01-28 | https://www.infosecurity-magazine.com/news/suspected-magecart-hackers/ |
