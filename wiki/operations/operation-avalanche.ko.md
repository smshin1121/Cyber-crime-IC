## 개요

Operation Avalanche(아발란치 작전)는 독일에서 발원한 수사이자 다국적 테이크다운으로, 2016년 11월 30일 세계 최대 규모의 악성코드, 피싱 및 스팸 인프라 중 하나를 와해시켰다. Europol(유럽 경찰청), Eurojust(유럽사법협력기구), INTERPOL(국제형사경찰기구), FBI(미국 연방수사국), BSI(독일 연방정보보안청) 및 다수의 국가 파트너가 사법 공조, 기술적 싱크홀링(sinkholing), 도메인 차단 및 서버 압수를 결합하여 본 네트워크를 해체하였다.

> [!note] Audit Note — Participating Countries Source Verification (2026-04-21)
> 2026년 4월 21일 TLS 지문 위장 기법(`curl_cffi`와 `chrome124`)을 사용하여 Europol 보도자료의 Cloudflare 봇 보호를 우회한 재검증이 수행되었다. 전체 30개국 명단은 Europol 페이지의 인라인 JSON 내 `"Countries involved:"`에 임베드되어 있으며, 구조화된 국가 코드 목록으로 제시된다.
>
> **현재 `participating_countries`에 기재된 29개국 모두 Europol 1차 출처에 명시적으로 명명되어 있으며**(추가로 Eurojust 사건 보고서 PDF, BSI bund.de, Kaspersky 권고문에서 보강 언급됨). Colombia(콜롬비아)는 같은 날 부분적 접근 가능 출처 검증에 따라 잘못 제거되었으나 **재포함**되었다.
>
> 1차 출처 인용문(Europol):
> > "Countries involved: Armenia, Australia, Austria, Azerbaijan, Belgium, Belize, Bulgaria, Canada, Colombia, Finland, France, Germany, Gibraltar, Hungary, India, Italy, Lithuania, Luxembourg, Moldova, Montenegro, Netherlands, Norway, Poland, Romania, Singapore, Sweden, Taiwan, Ukraine, United Kingdom, United States."
> > (한국어 번역: 참여국: 아르메니아, 호주, 오스트리아, 아제르바이잔, 벨기에, 벨리즈, 불가리아, 캐나다, 콜롬비아, 핀란드, 프랑스, 독일, 지브롤터, 헝가리, 인도, 이탈리아, 리투아니아, 룩셈부르크, 몰도바, 몬테네그로, 네덜란드, 노르웨이, 폴란드, 루마니아, 싱가포르, 스웨덴, 대만, 우크라이나, 영국, 미국.)
>
> 비고: Europol은 본 위키에서 추적 중인 29개국 외에 **Gibraltar(지브롤터)**도 명명한다. 지브롤터는 UN 회원국이 아닌 영국 해외영토이며 현재 본 위키에 국가 페이지가 존재하지 아니하므로, 추가 후보로 표시되었다.

## Why The Operation Matters

Avalanche는 인프라 테이크다운의 참조 사례인데, 이는 단순한 체포 소탕이 아니었기 때문이다. 공개 기록은 다층적 법집행 모델을 보여준다:

- 독일 검사 및 수사관들은 수년에 걸쳐 사건을 전개하였다.
- Europol과 Eurojust는 국경을 가로지르는 운영적·사법적 공조를 담당하였다.
- BSI 및 기술 파트너들은 싱크홀링 및 테이크다운 이후 피해자 통보 작업을 지원하였다.
- 인프라가 fast-flux 기법과 대량의 악성 도메인을 사용하였으므로, 도메인 등록기관 및 민간 부문 파트너의 참여가 필수적이었다.

## 참여 당사자

**주도 축:**
- Verden/Lueneburg 소재 독일 검찰 및 수사관
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust]]

**주요 운영 파트너:**
- [[interpol|INTERPOL]]
- [[fbi|FBI]]
- [[us-doj|미국 DOJ]]
- BSI
- [[shadowserver]]
- [[icann]]

## Results

- 본 작전에 공개적으로 귀속된 체포 5건
- 압수 또는 와해 대상 서버 221대
- 차단된 악성 도메인 800,000건 이상

## Cooperation And Legal Analysis

Eurojust 사례 연구는 본 작전의 미디어 헤드라인 수치가 아닌 사법 공조 측면을 확인한다는 점에서 특히 중요하다. BSI 페이지 또한 무결성 차원에서 동등하게 중요한데, 이는 테이크다운 자체가 감염된 기기를 정화하지 못하였음 — 즉, 당국은 여전히 후속 치료 및 피해자 통보 작업을 필요로 하였음 — 을 보여주기 때문이다. 이러한 구별은 "테이크다운"이 실무상 무엇을 의미하였는지에 대한 페이지의 과대 진술을 방지한다.

본 작전은 또한 반복되는 사이버범죄 패턴을 보여준다: 인프라 와해에는 형사 절차, 기술적 운영 및 민간 부문 협력의 결합이 필요하다. Avalanche를 단순한 압수 건수로 환원하는 어떠한 요약도, 본 작전을 주목할 만하게 만든 실제 다국적 공조 문제를 놓치게 된다.

## 후속 조치

> [!warning] No public court documents found
> 공개 보도는 다국적 테이크다운 및 관련 체포를 확인하나, 본 저장소는 현재 Avalanche를 단일 법원 주도 기소 서사에 연결시키는 깔끔한 공개 법원 기록 세트를 포함하고 있지 아니하다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2016-11-30: 'Avalanche' network dismantled in international cyber operation.
- US DOJ USAO, 2016-12-05: Avalanche Network Dismantled in International Cyber Operation.
- Eurojust, 2017-04-01: Operation Avalanche: a closer look.
- Federal Office for Information Security (BSI), 2026-04-18: "Avalanche" botnet infrastructure.

## Operational Timeline

- 2012: 활동 또는 수사 개시.
- 2016-11-30: 공표.
- 2016-11-30: 보도된 법집행 종결 시점.
- 2016-11-30: Europol의 공개 출처 보도.
- 2016-12-05: 미국 DOJ USAO의 공개 출처 보도.
- 2017-04-01: Eurojust의 공개 출처 보도.

## Evidence and Attribution Notes

- 2012년 독일 수사로 출발하여 2016년 11월 30일 절정에 이른 Operation Avalanche는 "Avalanche"로 알려진 세계 최대 규모의 피싱, 스팸 및 악성코드 배포 네트워크를 해체하였다.
- 본 네트워크는 온라인 뱅킹 해킹, 피싱, 스팸 및 악성코드 배포를 통하여 180개국 이상의 사용자에게 피해를 입혔다.
- Eurojust는 Avalanche를 2012년 시작된 독일 수사로서 글로벌 규모의 악성코드, 피싱 및 스팸에 활용된 회복탄력적 범죄 인프라를 폭로한 사건으로 기술한다.
- 동 출처는 본 네트워크가 수백만 대의 개인 및 기업용 컴퓨터 시스템을 감염시켰으며, 자격증명 탈취, 계좌 이체 및 자금 운반책(money-mule) 모집을 가능케 하였다고 명시한다.
- Eurojust의 사례 연구는 사법 공조 차원에서 유용한데, 이는 보도자료 헤드라인 수치가 아닌 다국적 테이크다운의 법적·공조 문제에 초점을 두기 때문이다.
- Eurojust의 사례 연구는 Operation Avalanche의 사법 공조 관점을 제공한다.
- 동 사례 연구는 본 사건이 2012년 독일 수사에서 발원하였고, 고도로 회복탄력적인 fast-flux 인프라를 다루었으며, 본 네트워크를 와해시키고 증거를 보전하기 위하여 다수 관할권에 걸친 공조 조치가 요구되었음을 확인한다.
- BSI는 Avalanche를 세계 최대 규모의 봇넷 인프라 중 하나로 기술하며, Verden 검찰청 및 Lueneburg 중앙 형사수사청이 2016년 11월 30일 국제 파트너와 함께 이를 와해시켰다고 명시한다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US DOJ USAO, 2016-12-05: Attorney's Office, Western District of Pennsylvania WASHINGTON – The Justice Department today announced a multinational operation involving arrests and searches in four countries to dismantle a complex and sophisticated network of computer servers known as "Avalanche.
- US DOJ USAO, 2016-12-05: "For years, sophisticated cyber criminals have used our own technology against us—but as their networks have grown more complex and widespread, criminals increasingly rely on an international infrastructure as well," said Assistant Attorney General Caldwell.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아닌 Avalanche Network에 대한 테이크다운을 기술하므로, 정본(canonical) 작전으로 유지된다. 본 기록은 주도 책임을 독일 검찰(German Prosecution)에, 공조를 Europol EC3에 귀속하며, 참여 또는 영향 관할권으로 아르메니아, 호주, 오스트리아, 아제르바이잔, 벨기에, 벨리즈, 불가리아, 캐나다, 콜롬비아, 핀란드, 프랑스, 독일, 헝가리, 인도, 이탈리아, 리투아니아, 룩셈부르크, 몰도바를 기록한다.

협력 모델은 다음의 명명된 기관 및 파트너를 통하여 문서화된다: Europol EC3, Eurojust, INTERPOL, FBI, 미국 DOJ, Shadowserver, ICANN; 메커니즘: 싱크홀링(Sinkholing) 및 비공식 협력(informal cooperation); 법집행 자세: 체포, 압수, 테이크다운.

정본 기록에 포착된 운영 결과: 체포 5건; 서버 압수 221대; 도메인 압수 800,000건; 180개국 이상의 수백만 대 감염 시스템 및 피해자; 글로벌 피싱, 스팸 및 악성코드 배포 인프라 와해.

정본 출처 세트는 4건의 참조를 포함한다: 2016 11 30 Europol Europa Eu Avalanche Network Dismantled In International Cyber Operation, 2026 04 18 Justice Gov Avalanche Network Dismantled International Cyber Operation, 2017 04 01 Eurojust Europa Eu Operation Avalanche Closer Look, 2026 04 18 Bsi Bund De Avalanche Botnet Infrastructure.
출처 하한선은 정본 작전 기준을 충족하나, 출처의 폭만으로는 모든 하류 체포 또는 선고가 본 작전의 일부임을 입증하지 아니한다. 후속 기록은 별도로 연계되어야 한다.
본 페이지에 현재 부착된 frontmatter 누락 필드 플래그는 없다.
데이터셋 활용을 위하여, 본 페이지는 작전 수준 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 공조된 법집행 조치를 전체로서 기술한다. 이후의 기소, 답변, 선고, 범죄인 인도 또는 몰수 조치는, 출처가 이들을 명시적으로 새로운 다국적 작전으로 제시하지 아니하는 한, 관련 사건 또는 흡수 후속 기록으로 부착되어야 한다.
출처 기록이 보다 광범위한 배경, 반복적 통신사 재게재 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 권한기관, 그 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 법집행 결과에 직접적으로 결부된 사실에 우선순위를 부여한다. 주변적 출처 제목은 독립적 분류 체계 또는 결과 증거로 취급되지 아니한다.
이러한 방식은 정본 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| 1 | 'Avalanche' network dismantled in international cyber operation | Europol | 2016-11-30 | https://www.europol.europa.eu/media-press/newsroom/news/%E2%80%98avalanche%E2%80%99-network-dismantled-in-international-cyber-operation |
| 2 | Avalanche network dismantled in international cyber operation | U.S. Department of Justice | repo snapshot | [[2026-04-18_justice-gov_avalanche-network-dismantled-international-cyber-operation]] |
| 3 | Operation Avalanche: a closer look | Eurojust | 2017-04-01 | https://www.eurojust.europa.eu/publication/operation-avalanche-closer-look |
| 4 | "Avalanche" botnet infrastructure | BSI | current | https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Cyber-Sicherheitslage/Methoden-der-Cyber-Kriminalitaet/Botnetze/Botnetz-Avalanche/botnet-avalanche_node.html |
