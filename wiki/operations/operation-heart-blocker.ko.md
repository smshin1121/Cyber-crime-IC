## 개요

Operation Heart Blocker(하트 블로커 작전)는 2025년 1월 29일에 실행되고 2025년 1월 30일에 발표된 미국-네덜란드 합동 법집행 작전으로, HeartSender 사이버범죄 마켓플레이스 네트워크(Saim Raza로도 알려짐)를 표적으로 하였다. DOJ(미국 법무부)와 네덜란드 국가경찰(Dutch National Police)은 최소 2020년부터 피싱 키트, 자격증명 탈취 도구, 이메일 추출기, 사기 페이지 생성기를 판매하는 마켓플레이스로 운영되어 온 39개 도메인 및 관련 서버의 압수를 공조하였다. 이 도구들은 초국가적 조직범죄 그룹에 의해 [[bec-ic|비즈니스 이메일 침해(BEC)]] 사기 수행에 사용되었으며, DOJ에 따르면 미국 피해자 손실이 300만 달러를 초과한 것으로 확인되었다(이후 파키스탄 NCCIA에 의해 5,000만 달러 이상으로 상향 조정).

2025년 5월에 있었던 중대한 후속 조치에서 파키스탄 국가사이버범죄수사청(NCCIA)은 작전과 연관된 21명을 체포하였으며, 여기에는 주모자로 지목된 Rameez Shahzad(가명 "Saim Raza")가 포함되어 있다. 이는 국제 공조 행동을 통해 파키스탄에 근거지를 둔 사이버범죄 네트워크가 와해된 보기 드문 사례이다.

## Background

HeartSender 네트워크는 **Saim Raza**, **The Manipulaters**, 그리고 최근에는 파키스탄 위장 기업 **WeCodeSolutions**라는 명칭으로 번갈아 알려진 조직에 의해 운영되었다. 이 조직은 사이버보안 저널리스트 Brian Krebs에 의해 2015년에 이미 프로파일링되었던 만큼, 약 10년간 법집행기관의 감시를 받아왔다.

Saim Raza가 운영한 웹사이트들은 다크웹이 아닌 일반 인터넷에서 공개 마켓플레이스로 운영되었으며, 다음과 같은 브랜드명으로 사이버범죄형 서비스(cybercrime-as-a-service) 도구를 광고하고 판매하였다:
- **HeartSender** — 이메일 및 SMS 스팸 도구
- **Fudtools** — "완전 탐지 불가(Fully Un-Detectable)" 피싱 키트
- **Fudpage** — 정상 서비스를 모방한 사기 랜딩 페이지
- **Fudsender** — 대량 이메일 발송 도구
- **FudCo** — 추가 사기 도구

도구 판매 외에도 이 조직은 **유튜브(YouTube) 교육 영상**을 제공하여 기술적 전문성이 부족한 구매자들에게 피해자를 상대로 도구를 배포·운용하는 방법을 가르쳤다 — 이는 사실상 BEC 사기를 대중화한 것이었다.

하류 공격의 주요 피해자는 Microsoft 365, Yahoo, AOL, Intuit, iCloud, ID.me 서비스 이용자였다.

## Participating Parties

**주관 기관:**
- [[us-doj|U.S. Department of Justice]] — 압수 영장 및 공조 조율

**핵심 파트너:**
- [[fbi-cyber-division|FBI Cyber Division]] — 수사 및 집행
- [[netherlands-politie|Dutch National Police (Politie)]] — 서버 압수, 피해자 데이터 분석, 유럽 사건과의 공조
- [[pakistan-fia|Pakistan FIA / NCCIA]] — 피의자 국내 체포(2025년 5월 후속 조치)

**참여 국가 (3개국):**
미국, 네덜란드, 파키스탄

## Legal Framework

본 작전은 미국 연방 컴퓨터 사기 및 전신 사기 법령에 따라 수행되었다. 압수 영장은 미국 법원이 발부하였으며, 네덜란드 국가경찰은 형사사법공조 협정 하에 압수를 집행하였다.

주요 법적 도구:
- 미국 컴퓨터 사기 및 남용 방지법(Computer Fraud and Abuse Act, 18 U.S.C. § 1030)
- 미국 전신 사기 법령(Wire Fraud statute, 18 U.S.C. § 1343)
- [[mlat-process|US-Netherlands Mutual Legal Assistance Treaty]] — 국경 간 서버 압수 공조
- 파키스탄 전자범죄 방지법(Prevention of Electronic Crimes Act, PECA) 2016 — NCCIA 체포의 근거

> [!note] Legal Basis Note
> (한국어 번역: DOJ 보도자료는 본 작전을 네덜란드 국가경찰과의 "공조(coordinated)" 행동으로 기술하였다. 네덜란드 측 참여를 가능하게 한 구체적 법적 도구는 해당 보도자료에 명시되지 않았으나, 이러한 공조는 미국-네덜란드 형사사법공조조약(MLAT) 또는 이에 상응하는 양자 협력 협정과 부합한다. 네덜란드는 자국 관할권 내에서 서버를 동시에 압수하였다.)

## Operational Timeline

| 일자 | 사건 |
|------|-------|
| 2015년경 | 조직이 "The Manipulaters"라는 명칭으로 활동 시작 (KrebsOnSecurity 보도 기준) |
| 2020년경 | HeartSender / Saim Raza 마켓플레이스 운영 개시 |
| 2025-01-29 | **Operation Heart Blocker 실행**: 미국 DOJ와 네덜란드 국가경찰이 39개 도메인 및 관련 서버를 압수 |
| 2025-01-30 | DOJ가 압수를 발표; 압수된 도메인에 법집행기관 테이크다운 배너 표시 |
| 2025-01-30 | 네덜란드 당국이 수백만 건의 피해자 기록을 회수하였음을 확인, 네덜란드 시민 관련 10만 건 이상 포함 |
| 2025-05-15 | 파키스탄 NCCIA, 라호르(Lahore) Bahria Town에서 HeartSender Group을 표적으로 한 급습 실시 |
| 2025-05-16 | NCCIA, 남부 운영 거점을 표적으로 물탄(Multan)에서 급습 실시 |
| 2025-05-16 | 파키스탄에서 21명 체포, Rameez Shahzad(가명 Saim Raza) 포함 |
| 2025년 5월 | 파키스탄 당국, 피해자 손실 추정치를 미국 기준 5,000만 달러 이상으로 상향 조정 |
| 2025년 5월 | 유럽 당국, 추가로 63건의 수사 진행 사실 공개 |

## Results and Impact

**1단계 — 도메인 압수(2025년 1월):**
- 39개 도메인 압수(미국 및 네덜란드)
- 39개 서버 다운
- 수백만 건의 피해자 기록 회수
- 네덜란드 시민 관련 기록 10만 건 이상 식별
- 압수된 도메인에 테이크다운 배너 게시
- 유튜브 교육 콘텐츠 플래그 처리

**2단계 — 파키스탄 체포(2025년 5월):**
- 라호르와 물탄에서 21명 체포
- 주요 체포 대상:
  - **Rameez Shahzad** (가명 Saim Raza) — 주모자로 지목, 라호르
  - **Muhammad Aslam** — Rameez의 부친
  - **Hussnain Haider** — 물탄 운영 총책으로 지목
  - 18명의 추가 관련자
- WeCodeSolutions가 위장 법인으로 확인

**재정적 영향:**
- DOJ 최초 추정치: 미국 피해자 손실 300만 달러 이상
- 파키스탄 NCCIA 추정치: 미국 손실 5,000만 달러 이상
- 추가 63건의 유럽 사건 수사 진행 중

> [!warning] Loss Figure Discrepancy
> (한국어 번역: **주장 A** (출처: DOJ 보도자료 [1], 신뢰도: 높음): 도구로 인한 피해자 손실이 "300만 달러 이상"이다.
> **주장 B** (출처: KrebsOnSecurity를 통해 인용된 파키스탄 NCCIA [3], 신뢰도: 중간): 본 조직은 "미국 단독으로 5,000만 달러 이상의 손실"과 연관된다.
> **평가**: 300만 달러 수치는 HeartSender 도구와 연계된 특정 BEC 사기 스킴에 귀속되어 확정·판단된 손실을 의미한다. 5,000만 달러 수치는 마켓플레이스를 통해 판매된 모든 도구로부터 발생한 전체 하류 손실에 대한 보다 광범위한 추정치일 수 있다. 실제 수치는 공공 기록상 두 추정치 사이에 위치한다.)

## Cooperation Mechanisms Used

1. **[[mlat-process|Mutual Legal Assistance]]** — 국경 간 도메인 및 서버 압수를 위한 미국-네덜란드 공조는 MLAT 또는 이에 상응하는 양자 협정에 의존하였다.

2. **[[informal-cooperation|Informal Police-to-Police Cooperation]]** — FBI는 수년간 "The Manipulaters"를 추적해왔으며, 네덜란드 당국과의 공조에는 공식 압수 이전의 정보 공유가 포함되었다.

3. **후속 파키스탄 공조** — 2025년 5월 파키스탄 NCCIA에 의한 체포는 도메인 압수에서 얻은 정보를 통해 가능해진 후속 조치였다. 사이버범죄 집행 측면에서 역사적으로 어려움이 있어왔던 파키스탄과의 이번 공조는 중대한 진전이었다.

## Challenges and Friction Points

1. **장기간의 타임라인** — 2015년경부터 본 조직이 공개적으로 알려져 왔음에도(KrebsOnSecurity에 의해 프로파일링됨), 집행 조치 실행까지 약 10년이 소요되었다. 이 지연은 집행 역량이나 의지가 제한된 관할권에 소재한 사이버범죄 운영에 대해 조치를 취하는 어려움을 부각시킨다.

2. **파키스탄 집행 공백** — 2025년 5월 체포 이전까지 파키스탄에 근거지를 둔 사이버범죄 운영은 국제 공조를 통해 와해시키기 어려웠다. NCCIA의 체포는 긍정적 변화를 보여주지만, 이러한 집행 자세의 지속가능성은 두고 봐야 한다.

3. **사이버범죄형 서비스 모델** — 마켓플레이스 와해는 이미 배포된 도구들을 제거하지 못한다. 과거에 피싱 키트를 구매한 고객들은 계속해서 이를 사용할 수 있다.

4. **손실 정량화** — DOJ(300만 달러)와 NCCIA(5,000만 달러) 손실 추정치 사이의 상당한 격차는 하류 사기 손실을 특정 도구 공급자에게 귀속시키는 것의 어려움을 보여준다.

5. **공개 인터넷 운영** — HeartSender가 다크웹이 아닌 일반 인터넷에서 유튜브 교육 영상과 함께 공개적으로 운영되었다는 사실은 플랫폼 제공자(도메인 등록기관, 유튜브)가 왜 더 일찍 조치를 취하지 않았는지에 대한 의문을 제기한다.

## Lessons Learned

1. **인프라 압수와 체포의 결합**이 가장 포괄적인 와해를 가져온다. 1월의 압수는 운영을 와해시켰고, 5월 파키스탄에서의 체포는 운영자를 와해시켰다.

2. **장기적 정보 수집**이 핵심이었다 — FBI의 10년에 걸친 본 조직 감시는 네트워크에 대한 정밀한 표적 설정을 가능하게 하였다.

3. **사이버범죄에 대한 파키스탄의 협력**은 가능하지만 지속적인 국제적 압력과 명확한 증거 패키지를 요구한다.

4. **사이버범죄형 서비스는 상류(upstream) 와해를 필요로 한다** — 도구 제공자가 수천 건의 공격을 가능케 하는 상황에서 개별 BEC 운영자만 기소하는 것은 충분하지 않다.

## Follow-Up Actions

- 파키스탄 NCCIA가 2025년 5월에 21명의 피의자를 체포하였으며, 주모자로 지목된 Rameez Shahzad 포함.
- 유럽 당국이 HeartSender 도구와 연관된 추가 63건의 사건을 수사 중.
- 네덜란드 당국이 압수된 서버에서 회수한 수백만 건의 피해자 기록 분석을 지속.
- 미국이 파키스탄에 근거지를 둔 운영자들에 대해 기소를 진행했는지 또는 진행할 예정인지는 알려지지 않았다.

## Korean Involvement (한국의 참여)

Operation Heart Blocker에 대한 한국의 참여는 알려진 바 없다. 다만:
- BEC 사기는 특히 국제 무역에 종사하는 한국 기업에 영향을 미치는 글로벌 위협이다.
- HeartSender가 보여준 사이버범죄형 서비스 모델은 한국 법집행기관의 BEC 생태계 이해와 관련성이 있다.
- Microsoft 365와 같은 서비스를 이용하는 한국의 피싱 피해자들은 HeartSender를 통해 판매된 도구의 영향을 받았을 수 있다.

## Contradictions & Open Questions

**미해결 질문:**
1. 미국 당국이 Rameez Shahzad 또는 다른 파키스탄 소재 피의자에 대해 범죄인 인도를 요구할 것인가, 아니면 기소가 파키스탄 국내에서 진행될 것인가?
2. HeartSender 도구에 귀속되는 실제 손실 규모는 어느 정도인가(DOJ 기준 300만 달러 vs. NCCIA 기준 5,000만 달러 이상)?
3. 전 세계적으로 얼마나 많은 하류 BEC 스킴이 HeartSender 도구에 의존하였는가?
4. 도메인 등록기관과 유튜브가 테이크다운 이전에 자사 플랫폼의 범죄적 이용에 대해 통보받았는가? 그렇다면 왜 조치가 취해지지 않았는가?
5. HeartSender 마켓플레이스 운영자들이 약 5년의 운영 기간 동안 벌어들인 수익은 얼마인가?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- 미국 텍사스 남부지구 연방검찰청(U.S. Attorney's Office, Southern District of Texas), 2025-01-30: 초국가적 조직범죄 그룹에 해킹 도구를 판매하는 사이버범죄 웹사이트 압수.
- KrebsOnSecurity, 2025-01-30: FBI, 네덜란드 경찰이 'Manipulaters' 피싱 갱단을 와해시키다.
- KrebsOnSecurity, 2025-05-28: 파키스탄, 'Heartsender' 악성코드 서비스 관련 21명 체포.
- CyberScoop, 2025-01-30: DOJ(미국 법무부), 네덜란드 경찰과 협력하여 HeartSender 네트워크 해체.
- Hackread, 2025-01-30: 미국-네덜란드 합동작전으로 HeartSender 사이버범죄 네트워크 해체.

## Evidence and Attribution Notes

- Operation Heart Blocker(하트 블로커 작전)는 2025년 1월 29일에 실행되고 2025년 1월 30일에 발표된 미국-네덜란드 합동 법집행 작전으로, HeartSender 사이버범죄 마켓플레이스 네트워크(Saim Raza로도 알려짐)를 표적으로 하였다.
- DOJ(미국 법무부)와 네덜란드 국가경찰은 최소 2020년부터 피싱 키트, 자격증명 탈취 도구, 이메일 추출기, 사기 페이지 생성기를 판매하는 마켓플레이스로 운영되어 온 39개 도메인 및 관련 서버의 압수를 공조하였다.
- 이 도구들은 초국가적 조직범죄 그룹에 의해 비즈니스 이메일 침해(BEC) 사기 수행에 사용되었으며, DOJ에 따르면 미국 피해자 손실이 300만 달러를 초과한 것으로 확인되었다(이후 파키스탄 NCCIA에 의해 5,000만 달러 이상으로 상향 조정).

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아니라 HeartSender / Saim Raza 사이버범죄 마켓플레이스 네트워크에 대한 인프라 압수(infrastructure-seizure)를 기술하므로 정전적(canonical) 작전으로 유지된다. 기록은 주관 책임을 U.S. Department of Justice에, 공조를 U.S. Department of Justice에 귀속시키며, 참여 또는 영향을 받은 관할권은 미국, 네덜란드, 파키스탄으로 기록되어 있다.

협력 모델은 명명된 기관과 파트너를 통해 문서화되어 있다: U.S. Department of Justice, FBI Cyber Division, Dutch National Police (Politie), Pakistan Federal Investigation Agency (FIA / NCCIA); 메커니즘: 형사사법공조 및 비공식 경찰 간 공조; 법적 근거: 미국-네덜란드 MLAT; 집행 자세: 압수, 체포, 기소.

정전적 기록에 포착된 작전 결과: 21명 체포; 39개 서버 압수; 39개 도메인 압수; 압수된 서버에서 수백만 건의 피해자 기록 회수; 네덜란드 시민 관련 기록 10만 건 이상; DOJ 추정 미국 피해자 손실 300만 달러; 파키스탄 NCCIA 추정 미국 손실 5,000만 달러 이상.

정전적 출처 집합은 5건의 참고문헌을 포함한다: [1] Us Doj Press Release (2025 01 29), [2] Krebsonsecurity (2025 01 30), [3] Krebsonsecurity — Pakistan Arrests (2025 05 28), [4] Cyberscoop (2025 01 30), [5] Hackread (2025 01 30).
정전적 작전에 대한 출처 하한선은 충족되었으나, 출처의 폭이 그 자체로 모든 하류 체포 또는 양형이 본 작전의 일부임을 입증하지는 않는다; 후속 기록은 별도로 연결되어야 한다.
현재 본 페이지에는 frontmatter 누락 필드 플래그가 부착되어 있지 않다.
데이터셋 활용 측면에서 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 공조 집행 행동 전체를 기술한다. 이후의 기소, 답변, 양형, 범죄인 인도 또는 몰수 조치는 출처가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건으로 첨부되거나 흡수된 후속 기록으로 부착되어야 한다.
출처 기록이 보다 광범위한 배경, 반복된 통신사 재게재 또는 주제 페이지 자료를 담고 있을 때, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실에 우선순위를 둔다. 주변적 출처 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이는 정전적 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 초국가적 조직범죄 그룹에 해킹 도구를 판매하는 사이버범죄 웹사이트 압수 | USAO SDTX | 2025-01-30 | https://www.justice.gov/usao-sdtx/pr/cybercrime-websites-selling-hacking-tools-transnational-organized-crime-groups-seized |
| [2] | FBI, 네덜란드 경찰이 'Manipulaters' 피싱 갱단을 와해시키다 | KrebsOnSecurity | 2025-01-30 | https://krebsonsecurity.com/2025/01/fbi-dutch-police-disrupt-manipulaters-phishing-gang/ |
| [3] | DOJ(미국 법무부), 네덜란드 경찰과 협력하여 HeartSender 네트워크 해체 | CyberScoop | 2025-01-30 | https://cyberscoop.com/doj-saim-raza-heartsender-takedown/ |
| [4] | 미국-네덜란드 합동작전으로 HeartSender 사이버범죄 네트워크 해체 | Hackread | 2025-01-30 | https://hackread.com/heartsender-cybercrime-network-dismantled-us-dutch-op/ |
| [5] | 파키스탄, 'Heartsender' 악성코드 서비스 관련 21명 체포 | KrebsOnSecurity | 2025-05-28 | https://krebsonsecurity.com/2025/05/pakistan-arrests-21-in-heartsender-malware-service/ |
