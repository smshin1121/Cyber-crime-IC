## 개요

Dridex(Dridex(뱅킹 트로이))/Evil Corp 교란 및 기소는 Dridex 뱅킹 트로이(Bugat 및 Cridex로도 알려짐)와 러시아 기반 사이버범죄 조직 **Evil Corp** 내부의 운영자들을 표적으로 한 **다년간의 국제 법집행 작전**이었다. 본 작전은 두 가지 주요 단계로 전개되었다: (1) [[fbi-cyber-division|FBI(미국 연방수사국)]]와 [[uk-nca|NCA(영국 국가범죄청)]]가 공동으로 수행한 **2015년 10월의 기술적 교란 및 봇넷 관리자 Andrey Ghinkul 체포**; (2) [[us-doj|DOJ(미국 법무부)]], [[us-treasury|미국 재무부(OFAC)]], NCA 간 조정으로 Evil Corp 지도자 **Maksim Yakubets**와 부지도자 **Igor Turashev**를 표적으로 한 **2019년 12월의 기소, 제재, 현상금 부여**.

Dridex 악성코드는 **40개국 이상**의 컴퓨터를 감염시켰고, 은행 및 금융기관으로부터 **1억 달러 이상**의 절도 피해를 야기하였다. 본 작전은 **기술적 교란**(공공-민간 파트너십을 통한 봇넷 싱크홀링), **형사 기소**(기소 및 범죄인 인도), **금융 제재**(OFAC 지정)를 결합하였다는 점에서 국제공조 측면에서 중요한 의의를 가진다 — 이러한 3단 접근은 이후 뱅킹 트로이 작전의 템플릿이 되었다.

결과는 **부분적 성공**으로 평가된다: 한 명의 피의자가 체포·인도·선고되었고 봇넷은 일시적으로 교란되었지만, 주요 표적인 Yakubets와 Turashev는 러시아 내에 잔류하고 있으며, Evil Corp는 이후 랜섬웨어 작전으로 전환하였다.

## Audit Note

이는 진정한 다국적 우산 사건이다. 2015년 교란, 2019년 제재, 그리고 기소/인도 계층은 별개이며 단일 사안이 아닌 관련된 단계로 읽혀야 한다.

## 배경

### The Dridex Malware

Dridex(원래 Bugat v5로 알려졌으며, 이전에는 Cridex로 알려짐)는 매크로 페이로드가 포함된 악성 Microsoft Office 문서가 포함된 피싱 이메일을 통해 주로 확산되는 뱅킹 트로이이다. 설치되면 악성코드는 온라인 뱅킹 자격 증명을 탈취하고 사기 송금을 가능하게 한다. 악성코드는 여러 버전으로 진화하였다:

- **Cridex** (2011-2012): 뱅킹 자격 증명을 표적으로 한 초기 버전
- **Bugat v4** (2012-2014): 모듈식 아키텍처가 강화된 버전
- **Dridex/Bugat v5** (2014-현재): 테이크다운을 더욱 어렵게 만드는 P2P(peer-to-peer) 봇넷 아키텍처

### Evil Corp

Evil Corp는 **Maksim V. Yakubets**(별칭 "aqua")가 이끄는 러시아 기반 사이버범죄 그룹으로, 주로 모스크바에서 활동한다. 이 그룹은 Dridex 악성코드를 대규모로 개발·배포하였으며, 전 세계 수십만 대의 컴퓨터를 감염시키는 정교한 범죄 기업을 유지하였다. 미국 재무부에 따르면 Yakubets는 또한 **러시아 정부의 악의적 사이버 활동에 직접적인 지원을 제공**한 것으로 알려져 있으며, 이는 국가 후원 및 범죄 사이버 작전 간의 연계점을 부각시킨다.

## 참여 당사자

**Law Enforcement:**
- [[fbi-cyber-division|FBI(미국 연방수사국) 사이버 부서]] (피츠버그 지부) — 미국 주도 수사 기관
- [[uk-nca|NCA(영국 국가범죄청)]] — 영국 주도 수사 기관, 싱크홀링 수행
- [[us-doj|DOJ(미국 법무부)]] (펜실베이니아 서부 지방, 네브래스카 지방) — 기소
- [[us-treasury|미국 재무부, OFAC]] — 제재 및 자산 동결
- [[europol-ec3|Europol EC3(유럽 경찰청 사이버범죄센터)]] 및 J-CAT — 조정 및 정보 공유
- [[germany-bka|BKA(독일 연방수사청)]] — 수사 지원
- 영국 GCHQ — 정보 지원
- 런던 메트로폴리탄 경찰 — 수사 지원
- 몰도바 법집행 기관 — 체포 지원

**Private Sector Partners:**
- **Dell SecureWorks**(Counter Threat Unit) — 봇넷 싱크홀링 전략 개발 및 실행
- **Fox-IT** — 기술 분석 및 교란 지원
- **Shadowserver Foundation** — 싱크홀 인프라
- **S21sec** — 악성코드 분석
- **Abuse.ch** — 위협 인텔리전스
- **Spamhaus** — 스팸 및 봇넷 추적

## 법적 근거

### Criminal Charges

**Against Andrey Ghinkul (W.D. Pa.):**
9건의 기소: 18 U.S.C. § 1030(CFAA), 18 U.S.C. § 1343(전자통신 사기), 18 U.S.C. § 1344(은행 사기)에 따른 범죄 공모, 사기 의도의 무권한 컴퓨터 접근, 컴퓨터 손상, 전자통신 사기, 은행 사기.

**Against Maksim V. Yakubets (W.D. Pa., D. Neb.):**
"수천만 달러의 손실을 초래한 10년에 걸친 일련의 해킹 및 은행 사기 범행"과 관련된 혐의. 공모, 컴퓨터 사기, 전자통신 사기, 은행 사기를 포함한다. Yakubets는 다른 지역에서 두 개의 별도 기소에서 기소되었다.

**Against Igor Turashev:**
Yakubets와 함께 Dridex 악성코드 관리자 역할로 기소되었다.

### Sanctions

2019년 12월 5일, OFAC은 국제비상경제권한법(IEEPA)에 따라 Evil Corp와 연관된 **17명의 개인 및 7개 단체**를 지정하여, 미국 관할권 내 모든 자산을 동결하고 미국인이 해당 대상과 거래하는 것을 금지하였다.

### Reward

미국 국무부는 초국가적 조직범죄 보상 프로그램에 따라 Yakubets의 체포 및/또는 유죄 판결로 이어지는 정보에 대해 최대 **500만 달러**의 현상금을 발표하였다 — 발표 당시 **사이버범죄자에 대한 최대 규모의 현상금**이었다.

## 작전 타임라인

- **2011-12-16**: Ghinkul은 피싱으로 획득한 자격 증명을 사용하여 Sharon, Pennsylvania City School District의 First National Bank 계좌에서 우크라이나 키이우의 계좌로 999,000달러의 전자 이체를 시도한 것으로 알려짐
- **2012-2014**: Bugat/Cridex가 P2P 봇넷 아키텍처를 가진 Dridex로 진화
- **2015-08 (8월 초)**: 몰도바 출신 30세 Andrey Ghinkul(별칭 Andrei Ghincul, "Smilex")이 미국 영장에 근거하여 **키프로스에서 체포**됨
- **2015-10-13**: **조정된 교란 작전 발표**: FBI와 NCA가 Dridex 봇넷 싱크홀링 및 Ghinkul의 기소를 공개 발표. Dell SecureWorks는 FBI, NCA, Shadowserver Foundation과 협력하여 각 하위 봇넷의 P2P 네트워크를 오염시키고 감염된 시스템을 법집행 기관이 통제하는 싱크홀로 리디렉션
- **2015-10-13**: DOJ가 펜실베이니아 서부 지방에서 Ghinkul에 대한 9건의 기소를 봉인 해제
- **2016-02**: Ghinkul이 **키프로스에서 미국으로 인도**됨
- **2017-02**: Ghinkul이 W.D. Pa.에서 공모 혐의에 대해 유죄 인정
- **2018-12-06**: 미국 지방법원 Bissoon 판사(W.D. Pa.)에 의해 Ghinkul이 체포 이후 약 3년 이상의 구금 기간을 인정받아 **time served(이미 복역한 기간)**으로 선고됨
- **2019-12-05**: **조정된 2단계**: DOJ가 Maksim V. Yakubets와 Igor Turashev에 대한 기소를 봉인 해제; 미국 재무부 OFAC가 17명의 개인 및 7개 Evil Corp 단체를 제재; 국무부가 500만 달러 현상금 발표; NCA가 Evil Corp의 구조 및 운영에 대한 상세 정보를 공개
- **2019-12-05**: NCA가 Yakubets의 러시아 국가 정보 기관과의 연결을 공개

## 결과 및 영향

### Quantitative Results

| 지표 | 결과 |
|--------|--------|
| 체포 | 1건 (Ghinkul, 키프로스, 2015년 8월) |
| 범죄인 인도 | 1건 (Ghinkul, 키프로스에서 미국으로, 2016년 2월) |
| 유죄 판결/선고 | 1건 (Ghinkul, time served, 2018년 12월) |
| 기소 (도주 중) | 2건 (Yakubets, Turashev) |
| OFAC 제재 | 17명, 7개 단체 |
| 현상금 제공 | 500만 달러 (Yakubets) |
| 추정 피해자 손실 | 전 세계 1억 달러 이상; 미국 1,000만 달러; 영국 2,000만 파운드 |
| 영향 국가 | 40개국 이상 |

### Technical Disruption

2015년 10월 싱크홀링 작전은 FBI, NCA, Shadowserver Foundation과 협력하여 Dell SecureWorks CTU 연구자들에 의해 실행되었으며, **각 Dridex 하위 봇넷의 P2P 네트워크를 오염시키고** 감염된 시스템을 법집행 통제 싱크홀로 리디렉션하였다. 이는 봇넷의 명령-제어 인프라를 일시적으로 교란하고 운영자가 감염된 기기에 새로운 명령을 내리는 것을 막았다.

그러나 교란은 **일시적**이었다. Evil Corp는 이후 Dridex 인프라를 재구축하고 랜섬웨어 작전(WastedLocker, Hades, Phoenix)으로 전환하였으며, 이는 주요 운영자 체포 없이 기술적 교란만의 한계를 보여준다.

### Sanctions Impact

Evil Corp에 대한 OFAC 제재는 중요한 후속 효과를 가져왔다: 그것은 Evil Corp 가담자에게 몸값을 지불한 모든 조직(랜섬웨어 피해자 및 그 중개자 포함)에게 법적 위험을 만들어냈으며, 그러한 지불은 제재 위반에 해당할 수 있기 때문이다. 이는 사실상 **제재를 랜섬웨어 지불에 대한 억제 수단으로 무기화**한 것 — 이 메커니즘은 이후 다른 사이버범죄 그룹에 대해서도 사용되었다.

## 활용된 협력 메커니즘

1. **[[mlat-process|형사사법공조조약(MLAT)]]** — 기소, 체포, 범죄인 인도를 위한 미국-영국 및 미국-몰도바 간 공식 증거 교환
2. **FBI-NCA Bilateral Cooperation** — 두 기관 간의 긴밀한 양자 파트너십, NCA가 영국 측 싱크홀링을 수행하는 동안 FBI는 미국 측 기술 운영을 관리
3. **Europol EC3 / J-CAT** — 정보 조정 및 정보 공유 허브
4. **Public-Private Partnership** — Dell SecureWorks, Fox-IT, Shadowserver Foundation 등이 법집행만으로는 실행할 수 없는 봇넷 싱크홀링을 위한 핵심 기술 역량을 제공
5. **OFAC Sanctions** — 체포가 실현 불가능할 때 대안적 집행 메커니즘으로서의 재무부 금융 제재
6. **Extradition (Cyprus to US)** — Ghinkul의 키프로스에서 인도는 협력적 관할권을 통과하는 사이버범죄자를 체포하는 실행 가능성을 입증
7. **State Department Reward Program** — Yakubets의 위치에 대한 정보를 유인하기 위해 사용된 초국가적 조직범죄 보상 프로그램

## 도전 및 마찰 요인

- **Russian non-cooperation**: Yakubets와 Turashev는 러시아 내에 잔류하고 있으며, 러시아는 자국민을 범죄인 인도하지 않고 미국 기소에 대해 조치를 취하지 않았다. 러시아의 협력 거부는 주요 피의자 기소의 주된 장벽이다
- **State-criminal nexus**: NCA와 재무부가 Yakubets가 **러시아 정부의 사이버 활동에 직접적 지원을 제공**했다고 공개한 것은 국가 보호를 받는 사이버범죄자를 추적하는 것의 도전을 부각시켰다
- **Temporary technical disruption**: Dridex 봇넷은 싱크홀링 이후 재구축되었으며, 이는 체포 없는 기술적 교란이 일시적 안도만을 제공함을 보여준다
- **Evolution to ransomware**: Evil Corp의 뱅킹 트로이에서 랜섬웨어로의 전환(WastedLocker, Hades, Phoenix, Macaw Locker)은 그룹의 적응성과 단일 악성코드 계열을 교란하는 것의 한계를 보여주었다
- **Sanctions compliance complexity**: Evil Corp에 대한 OFAC 제재는 지불이 제재를 위반할지 여부를 탐색하는 랜섬웨어 피해자 및 사고대응 회사에게 컴플라이언스 도전을 만들어냈다

## 교훈

1. **3단 접근(기소 + 기술적 교란 + 제재)**은 단일 메커니즘보다 효과적이지만, 주요 표적이 비협력적 관할권에서 국가 보호를 받는 경우에는 여전히 불충분하다
2. **공공-민간 파트너십은 기술 작전에 필수적이다**: 법집행 기관은 봇넷 싱크홀링을 단독으로 실행할 깊은 기술적 전문성을 결여하고 있으며, Dell SecureWorks와 Shadowserver 같은 사이버보안 기업은 불가결한 파트너이다
3. **경유국을 통한 범죄인 인도가 작동한다**: 몰도바에서 경유 중인 Ghinkul의 키프로스에서의 체포는 여행 패턴 모니터링 및 협력적 제3국 관할권 활용의 가치를 보여준다
4. **사이버범죄 도구로서의 OFAC 제재**: Evil Corp 사건은 제재를 사이버범죄 조직에 대한 실행 가능한 집행 메커니즘으로 확립하였으며, 이는 이후 다른 그룹에도 적용되었다
5. **FBI-NCA 양자 모델**: 본 사건에서의 긴밀한 미국-영국 협력 — FBI가 기소를 관리하고 NCA가 영국 측 기술 운영을 관리하는 — 은 이후 뱅킹 트로이 및 랜섬웨어 작전의 템플릿이 되었다

## 한국의 참여

Dridex/Evil Corp 작전에 한국이 직접 참여한 것으로 확인된 바는 없다. 그러나 본 사건은 다음과 같은 이유로 한국의 이해관계와 관련이 있다:

- Dridex는 **40개국 이상**에서 뱅킹 자격 증명을 표적으로 하였으며, 한국 금융기관은 잠재적 표적 중 하나였을 가능성이 있다
- Evil Corp에 적용된 OFAC 제재 프레임워크는 랜섬웨어 맥락에서 제재 대상 기관과 상호작용할 수 있는 한국 조직에 시사점을 가진다
- FBI-NCA 양자 협력 모델은 사이버범죄에 관한 한국의 미국 및 영국과의 양자 협력 프레임워크와 유사하다

## 모순점 및 미해결 문제

1. **Ghinkul's sentence**: DOJ 보도자료는 Ghinkul이 약 2018년 12월 6일 Bissoon 판사에 의해 3년 이상의 구금 기간을 인정받아 "time served"로 선고되었음을 확인한다. 그의 변호인 답변 합의의 구체적 조건은 공개되지 않았다. 관대한 형량을 정당화할 만한 협력을 제공했는지 여부는 불분명하다.
2. **Dridex victim losses**: FBI는 "미국에서 직접 손실 1,000만 달러"로 추정하는 반면, NCA는 "영국에서 2,000만 파운드 손실"을 인용한다. 전 세계 1억 달러 수치는 재무부에서 나온다. 이러한 수치들은 서로 다른 기간 또는 방법론을 다룰 수 있으며, 40개국 이상의 영향 국가를 감안할 때 실제 총액은 더 높을 가능성이 있다.
3. **Yakubets' Russian government ties**: NCA와 재무부는 Yakubets가 "러시아 정부의 악의적 사이버 활동에 직접적 지원을 제공한다"고 명시했지만, 이러한 지원의 구체적 성격은 공개적으로 상세히 다루어지지 않았다. Yakubets가 FSB 지시에 따라 운영하는지 또는 거래 기반으로 서비스를 제공하는지는 불분명하다.
4. **Evil Corp evolution**: Dridex 이후, Evil Corp는 여러 랜섬웨어 변종(WastedLocker, Hades, Phoenix, Macaw Locker, 잠재적 LockBit 가담자)을 배포하였다. 이러한 랜섬웨어 계열에 대한 후속 집행 조치를 Dridex 작전의 연장으로 간주해야 할지, 별도의 작전으로 간주해야 할지는 열린 분류 문제이다.

> [!info] Legal-basis note
> Yakubets and Turashev remain at large as of the last verified date. Their status and the $5 million reward should be verified against current FBI Most Wanted listings.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- US DOJ, 2015-10-13: Bugat Botnet Administrator Arrested and Malware Disabled.
- FBI Pittsburgh, 2015-10-13: Bugat Botnet Administrator Arrested and Malware Disabled.
- US DOJ (OPA / W.D. Pa.), 2019-12-05: Russian National Charged with Decade-Long Series of Hacking and Bank Fraud Offenses Resulting in Tens of Millions in Losses and Second Russian..
- US Treasury, 2019-12-05: Treasury Sanctions Evil Corp, the Russia-Based Cybercriminal Group Behind Dridex Malware.
- NCA, 2019-12-05: International law enforcement operation exposes the world's most harmful cyber crime group.
- U.S. Attorney's Office, Western District of Pennsylvania, 2017-03-14: Moldovan Sentenced for Distributing Multifunction Malware Package.
- Dell SecureWorks (Sophos), 2015-10-01: Dridex (Bugat v5) Botnet Takeover Operation.
- The Hacker News, 2019-12-05: FBI Puts $5 Million Bounty On Russian Hackers Behind Dridex Banking Malware.

## Evidence and Attribution Notes

- The Dridex/Evil Corp disruption and prosecution was a **multi-year international law enforcement operation** targeting the Dridex banking trojan (also known as Bugat and Cridex) and its operators within the Russia-based cybercriminal organization **Evil Corp**.
- The operation unfolded in two major phases: (1) the **October 2015 technical disruption and arrest** of botnet administrator Andrey Ghinkul, conducted jointly by the FBI and UK National Crime Agency (NCA); and (2) the **December 2019 indictment, sanctions, and reward** targeting Evil Corp leader **Maksim Yakubets** and deputy **Igor Turashev**, coordinated.
- On 5 December 2019, the United States and United Kingdom jointly announced criminal charges against Maksim V.
- Yakubets (aka "aqua"), 32, of Moscow, Russia, related to two separate international computer hacking and bank fraud schemes spanning from May 2009 to the present.
- Charges A federal grand jury in Pittsburgh returned a 10-count indictment charging Yakubets and Igor Turashev with conspiracy, computer hacking, wire fraud, and bank fraud in connection with the distribution of "Bugat" (later known as "Cridex" and "Dridex"), a multifunction malware package designed to automate the theft of banking credentials.
- Ghinkul extradited from Cyprus to U.S. February 2016 following Cypriot extradition proceedings.
- Sentencing follow-up to original 2015 arrest.
- DOJ U.S. Attorney's Office WDPA sentencing follow-up for the Bugat botnet administrator case, documenting the Cyprus extradition timeline.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a joint-investigation against Evil Corp cybercriminal organization; Dridex/Bugat/Cridex banking trojan operators, rather than a defendant-specific follow-on action. The record attributes lead responsibility to FBI Cyber Division (Pittsburgh Field Office) and coordination to Europol EC3, with participating or affected jurisdictions recorded as United States, United Kingdom, Germany, Moldova, Cyprus.

The cooperation model is documented through named agencies and partners: FBI Cyber Division, UK National Crime Agency (NCA), US Department of Justice, US Treasury Department (OFAC), Europol EC3, Germany BKA; mechanisms: MLAT, Fbi Nca Bilateral Cooperation, Botnet Sinkholing (technical Disruption), Ofac Sanctions (asset Freeze); legal basis: US-UK MLAT, US-Moldova MLAT, Us Computer Fraud And Abuse Act (18 U.s.c. Ss 1030), Us Wire Fraud Statute (18 U.s.c. Ss 1343), Us Bank Fraud Statute (18 U.s.c. Ss 1344), International Emergency Economic Powers Act (ieepa) Ofac Sanctions; enforcement posture: Arrest, Indictment, Takedown, Extradition, Asset Freeze.

Operational results captured for the canonical record: 1 arrests; 3 indictments; Dridex botnet sinkholed via P2P network poisoning (October 2015); Andrey Ghinkul arrested in Cyprus (August 2015), extradited to US (February 2016), sentenced to time served (December 2018); Maksim Yakubets and Igor Turashev indicted (December 2019); $5 million reward offered for Yakubets -- largest cyber reward at time of announcement.

The canonical source set contains 8 reference(s): [1] Doj: Bugat Botnet Administrator Arrested And Malware Disabled (2015 10 13), [2] Fbi: Bugat Botnet Administrator Arrested (2015 10 13), [3] Doj: Russian National Charged With Decade Long Series Of Hacking (2019 12 05), [4] Us Treasury: Sanctions Evil Corp (2019 12 05), [5] Nca: International Law Enforcement Operation Exposes The World's Most Harmful Cyber Crime Group (2019 12 05), [6] Doj: Moldovan Sentenced For Distributing Multifunction Malware Package (2018 12 06), plus 2 more.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Bugat Botnet Administrator Arrested and Malware Disabled | US DOJ | 2015-10-13 | https://www.justice.gov/opa/pr/bugat-botnet-administrator-arrested-and-malware-disabled |
| [2] | Bugat Botnet Administrator Arrested and Malware Disabled | FBI Pittsburgh | 2015-10-13 | https://www.fbi.gov/contact-us/field-offices/pittsburgh/news/press-releases/bugat-botnet-administrator-arrested-and-malware-disabled |
| [3] | Russian National Charged with Decade-Long Series of Hacking and Bank Fraud Offenses Resulting in Tens of Millions in Losses and Second Russian National Charged with Involvement in Deployment of "Bugat" Malware | US DOJ | 2019-12-05 | https://www.justice.gov/archives/opa/pr/russian-national-charged-decade-long-series-hacking-and-bank-fraud-offenses-resulting-tens |
| [4] | Treasury Sanctions Evil Corp, the Russia-Based Cybercriminal Group Behind Dridex Malware | US Treasury | 2019-12-05 | https://home.treasury.gov/news/press-releases/sm845 |
| [5] | International law enforcement operation exposes the world's most harmful cyber crime group | NCA | 2019-12-05 | https://nca-newsroom.prgloo.com/news/international-law-enforcement-operation-exposes-the-worlds-most-harmful-cyber-crime-group |
| [6] | Moldovan Sentenced for Distributing Multifunction Malware Package | U.S. Attorney's Office, Western District of Pennsylvania | 2017-03-14 | https://www.justice.gov/usao-wdpa/pr/moldovan-sentenced-distributing-multifunction-malware-package |
| [7] | Dridex (Bugat v5) Botnet Takeover Operation | Dell SecureWorks (Sophos) | 2015-10-01 | https://www.sophos.com/en-us/research/dridex-bugat-v5-botnet-takeover-operation |
| [8] | FBI Puts $5 Million Bounty On Russian Hackers Behind Dridex Banking Malware | The Hacker News | 2019-12-05 | https://thehackernews.com/2019/12/dridex-russian-hackers-wanted-by-fbi.html |
