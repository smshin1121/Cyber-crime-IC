> [!info] 페이지 정정 (2026-04-10)
> 본 페이지는 당초 "Europol Botnet Takedown 2023"(`botnet-takedown-europol-2023.md`)으로 작성되었다. Europol 소스 URL의 내용 검증 결과, 실제 작전은 **2015년 2월 Ramnit 봇넷 단속**임이 확인되었다. 페이지 명칭을 변경하고 모든 데이터를 정정하였다.

## 개요

2015년 2월 24일, **영국 국가범죄수사청(UK National Crime Agency, NCA)**은 전 세계 약 **320만 대의 컴퓨터**를 감염시킨 **Ramnit 봇넷(람니트 봇넷)**을 무력화하기 위한 다국적 작전을 주도하였다. 본 작전은 [[europol-ec3|Europol(유럽 사이버범죄센터, EC3)]] 및 [[j-cat|합동 사이버범죄 대응 태스크포스(J-CAT)]]를 통해 조정되었으며, [[germany|독일]], [[italy|이탈리아]], [[netherlands|네덜란드]] 법집행기관이 참여하였다.

Ramnit 악성코드(악성코드)는 뱅킹 트로이목마로, 범죄자가 감염된 Windows 시스템에서 비밀번호 등 개인 정보와 뱅킹 정보를 탈취하고 백신 보호 기능을 무력화할 수 있도록 하였다.

## 배경

Ramnit은 2010년경 처음 식별되었으며, 단순 파일 감염형 악성코드에서 본격적인 뱅킹 트로이목마로 진화하였다. 2015년에 이르러 약 320만 건의 감염이 추정되어 전 세계에서 가장 만연한 봇넷 중 하나가 되었다. 본 악성코드는 일반적으로 스팸 이메일 내 링크 또는 익스플로잇 키트로의 리디렉션을 통한 사회공학 공격을 통해 확산되었다.

## 참여 당사자

**주도 기관**: [[uk-nca|영국 국가범죄수사청]]

**법집행 (4개국)**:
- [[united-kingdom]] — NCA (주도)
- [[germany]] — BKA(독일 연방범죄수사청)
- [[italy]] — 이탈리아 법집행기관
- [[netherlands]] — 네덜란드 국가첨단기술범죄수사대(NHTCU)

**조정**: [[europol-ec3|Europol EC3]], [[eurojust]], [[j-cat|J-CAT]], CERT-EU

**민간 부문 파트너**:
- Microsoft — 기술 분석
- Symantec — 악성코드 연구 및 싱크홀링
- AnubisNetworks — 도메인 인텔리전스

## 작전 타임라인

| 날짜 | 사건 |
|---|---|
| ~2010년 | Ramnit 파일 감염형 악성코드로 최초 관찰 |
| 2012-2014년 | 뱅킹 트로이목마로 진화; 감염 수 수백만 대 도달 |
| 2015-02-24 | 조정된 단속: C2 서버 폐쇄, 약 300개 도메인 싱크홀링 |
| 2015-02-24 | Europol 공개 발표 |

## 결과 및 영향

- **약 300개 인터넷 도메인 주소** 압수/싱크홀링 — 범죄 측 C2에서 법집행 측 싱크홀로 우회
- 참여국 전역에서 **지휘통제 서버** 폐쇄
- **320만 대의 감염 컴퓨터**가 범죄자 명령 수신으로부터 차단됨
- 본 작전의 일환으로 **공식 발표된 체포는 없음**

## 활용된 협력 메커니즘

- [[j-cat|합동 사이버범죄 대응 태스크포스(J-CAT)]] — Europol 내 작전 조정 허브
- [[europol-ec3|Europol EC3]] — 분석 및 조정 지원
- **민관 파트너십**: Microsoft, Symantec, AnubisNetworks가 기술 정보 및 싱크홀 인프라 제공

## 교훈

1. **주된 무력화 수단으로서의 싱크홀링**: 체포 없이 인프라 압류에 의존한 작전은 무력화에는 효과적이었으나, 운영자가 재구축할 여지를 남겼다.
2. **J-CAT 조정 모형**: Ramnit은 헤이그를 거점으로 다국적 봇넷 단속을 조정하는 J-CAT의 역량을 보여 준 초기 사례였다.
3. **PPP(민관 협력)**: Microsoft와 Symantec의 인텔리전스가 필수적이었다. 법집행기관 단독으로는 충분한 기술적 가시성을 확보하지 못하였다.

## 한국의 참여 (Korean Involvement)

본 작전에서 한국의 참여는 확인되지 않는다. 다만, 한국 내에서도 Ramnit 감염이 보고되었으며, [[south-korea|대한민국]]은 시스템이 영향을 받은 190개국 이상에 포함되었다.

## 모순 및 미해결 질문

- **체포 부재**: 320만 건의 감염 규모에도 불구하고 공식적으로 기소된 운영자는 없다. 이후 수사에서 체포로 이어졌는지는 불명확하다.
- **Ramnit의 부활**: 보안 연구자들은 단속 이후 수개월 내에 Ramnit 활동이 재개되었음을 보고하였으며, 인프라 단속만에 의존하는 장기적 실효성에 의문이 제기되었다.

## 후속 조치

> [!warning] 공개 법원 문서 미확인
> 웹 검색(2026-04-17) 결과, 본 작전에 대한 공개 접근 가능한 법원 문건은
> 확인되지 않았다. 가능한 사유: 공개 법원 기록 시스템이 없는 비미국
> 관할권, 비공개 절차 진행, 또는 정식 기소로 이어지지 않은 작전.

<!-- SOURCE_ENRICHMENT_START -->

## 소스 커버리지

- Europol, 2015-02-24: Europol: 국제 법집행 협력을 통해 무력화된 봇넷(Ramnit, 2015).
- Microsoft, 2015-10-22: 봇넷 해체 — Ramnit이 어떻게 무력화되었는가.
- AnubisNetworks, 2015-02-25: AnubisNetworks, 악성 봇넷 단속에서 Europol(유럽 사이버범죄센터) 지원.
- Ars Technica, 2015-02-25: Europol, 320만 대 컴퓨터를 감염시킨 봇넷 단속.
- PCWorld, 2015-02-25: Europol 및 보안 벤더, 대규모 Ramnit 봇넷 무력화.

## 법적·절차적 상태

- 기록상 범죄 분류: 악성코드.
- 기록상 집행 형태: 단속 및 압류.
- 본 기록은 완료(completed) 상태의 단속(takedown)으로 분류된다.

## 증거 및 귀속 주석

- URL-주제 불일치: 'Europol Botnet Takedown 2023' 위키 작전에 연결되어 있던 Europol URL은 실제로 2015-02-24 Ramnit 봇넷 단속에 관한 보도자료이며, 2023년의 조치가 아니다.
- 작전 페이지 제목이 오인 소지가 있으므로 정정 또는 소스 재배정이 필요하다.
- 실제 기사는 영국 국가범죄수사청(NCA)이 주도하고 독일, 이탈리아, 네덜란드의 파트너 조치와 함께 약 320만 대의 컴퓨터를 감염시킨 Ramnit 봇넷을 2015년 2월 24일 무력화한 사실을 기술한다.
- 민간 부문 파트너: Microsoft, Symantec, AnubisNetworks가 기술 분석 및 싱크홀링에 기여하였다.
- Europol의 합동 사이버범죄 대응 태스크포스(J-CAT) 및 EC3를 통해 작전이 조정되었으며, CERT-EU의 지원이 있었다.
- 기술적 조치: Ramnit 봇넷이 감염 기기에 명령을 하달하는 데 사용한 약 300개 인터넷 도메인 주소에 대한 지휘통제 서버 폐쇄 및 리디렉션(싱크홀링).
- 악성코드 기능: Ramnit은 Windows 시스템에서 범죄자가 '개인 및 뱅킹 정보, 특히 비밀번호를 탈취하고 백신 보호 기능을 무력화'하도록 하는 전형적 뱅킹 트로이목마 프로파일을 갖는다.
- 본 사항은 중요한 데이터 무결성 정정 — 소스가 2015년 Ramnit 단속을 기술함을 검증한 후, 작전 페이지명을 botnet-takedown-europol-2023에서 Ramnit 봇넷 단속으로 변경하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본 작전 평가

본 페이지는 피의자 특정 후속 조치가 아닌, Ramnit 봇넷(뱅킹 트로이목마)에 대한 단속(takedown)을 기술하므로 정본 작전으로 유지된다. 기록상 주도 책임은 UK National Crime Agency에, 조정 책임은 Europol Ec3에 귀속되며, 참여 또는 영향을 받은 관할로 영국, 독일, 이탈리아, 네덜란드가 기록되어 있다.

협력 모형은 명명된 기관 및 파트너를 통해 문서화되어 있다: UK NCA, Europol EC3, Eurojust; 메커니즘: 합동 사이버범죄 대응 태스크포스(J-CAT); 집행 형태: 단속 및 압류.

정본 기록에 포착된 작전 결과: 도메인 300개 압수; 지휘통제 서버 폐쇄; 약 300개 도메인 싱크홀링; 320만 대의 감염 컴퓨터 무력화.

정본 소스 집합은 5건의 참조를 포함한다: Europol Europol Botnet Takedown 2023, 2015 10 22 Microsoft Breaking Up A Botnet How Ramnit Was Foiled, 2015 02 25 Anubisnetworks Aids Europols European Cybercrime Centre In Takedown Of Malicious Botnet, 2015 02 25 Arstechnica Europol Cracks Down On Botnet Infecting 3 2 Million Computers, 2015 02 25 Pcworld Europol And Security Vendors Disrupt Massive Ramnit Botnet.
정본 작전의 소스 하한선은 충족되나, 소스의 폭이 곧 모든 후속 체포 또는 형 선고가 본 작전의 일부임을 입증하지는 않는다. 후속 기록은 별도로 연결되어야 한다.
본 페이지에 여전히 남아 있는 메타데이터 공백: 법적 근거 및 체포.
데이터셋 활용 측면에서 본 페이지는 작전 단위 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조정된 집행 행위 전체를 기술한다. 후속 기소, 유죄협상, 형 선고, 범죄인 인도, 자산 몰수는 소스가 명시적으로 이를 새로운 다국적 작전으로 제시하지 않는 한 관련 사건(case) 또는 흡수된 후속 기록으로 부가되어야 한다.
소스 기록에 더 폭넓은 배경, 반복적 통신사 재게시, 또는 주제 페이지성 자료가 포함된 경우 본 평가는 명명된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실을 우선시한다. 주변적 소스 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 상태로 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: 국제 법집행 협력을 통해 무력화된 봇넷(Ramnit, 2015) | Europol | 2015-02-24 | https://www.europol.europa.eu/media-press/newsroom/news/botnet-taken-down-through-international-law-enforcement-cooperation |
| [2] | 봇넷 해체 — Ramnit이 어떻게 무력화되었는가 | Microsoft | 2015-10-22 | https://blogs.microsoft.com/eupolicy/2015/10/22/breaking-up-a-botnet-how-ramnit-was-foiled/ |
| [3] | AnubisNetworks, 악성 봇넷 단속에서 Europol(유럽 사이버범죄센터) 지원 | AnubisNetworks | 2015-02-25 | https://www.anubisnetworks.com/news/community/news/anubisnetworks-aids-europols-european-cybercrime-centre-in-takedown-of-malicious-botnet |
| [4] | Europol, 320만 대 컴퓨터를 감염시킨 봇넷 단속 | Ars Technica | 2015-02-25 | https://arstechnica.com/tech-policy/2015/02/europol-cracks-down-on-botnet-infecting-3-2-million-computers/ |
| [5] | Europol 및 보안 벤더, 대규모 Ramnit 봇넷 무력화 | PCWorld | 2015-02-25 | https://www.pcworld.com/article/432079/europol-and-security-vendors-disrupt-massive-ramnit-botnet.html |
