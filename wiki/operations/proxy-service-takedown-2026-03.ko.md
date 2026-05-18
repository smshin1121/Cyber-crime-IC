## 개요

**2026년 3월 11일**, 미국-유럽 합동 법집행 작전으로 **SocksEscort**가 무력화되었다. SocksEscort는 **AVrecon** 악성코드에 감염된 라우터 및 IoT 기기를 수익화하던 주거용 프록시 서비스(residential proxy service)이다. [[eurojust|Eurojust(유럽사법협력기구)]]는 **2026년 3월 12일** 공개 단속 사실을 발표했으며, [[us-doj|미국 법무부]]와 [[fbi|FBI(미국 연방수사국)]]의 자료가 기존 Eurojust 발표에서 명시되지 않았던 서비스명과 악성코드군을 확인하였다.

본 작전의 실제 규모는 원 페이지에 반영된 것보다 훨씬 컸다. Eurojust는 **7개국에서 24대의 서버 압류**, **34개 도메인 압수**, 감염된 모뎀의 프록시 서비스 차단, 약 **350만 유로 상당의 암호화폐 미국 당국 동결**, 약 **163개국에 걸쳐 369,000대의 라우터 및 기타 기기 감염**, 약 **124,000명의 고객 사용자**를 보고하였다. 미국 법무부(DOJ)는 SocksEscort가 **2020년 여름 이래 약 369,000개의 IP 주소에 대한 접근권을 제공**해 왔으며, 2026년 2월 기준 해당 서비스의 애플리케이션에 약 **8,000대의 활성 감염 라우터**가 등록되어 있었고 그 중 약 **2,500대가 미국 내**에 있었다고 추가하였다.

> [!note] 정합성 보정 노트
> 본 페이지는 당초 Eurojust 단신 ingest에 기반하여 서비스명이 비공개된 상태로 작성되었다. 이후 공개된 DOJ 및 FBI 공식 자료가 해당 서비스를 **SocksEscort**, 악성코드를 **AVrecon**으로 명시함에 따라, "비공개 4개국" 및 "서버 미명시" 공백 항목은 해소되었다.

## 표적이 된 대상

SocksEscort는 주거용 IP 주소에 대한 유료 접근권을 판매함으로써 고객이 일반 가정 및 소상공인 네트워크를 통해 트래픽을 우회할 수 있도록 하였다. 이는 악성 행위가 알려진 범죄 인프라가 아닌 합법적 소비자 회선에서 발신되는 것처럼 위장되도록 만들었다.

기술적 기반은 **AVrecon** 악성코드(malware)였으며, 이는 라우터와 IoT 기기를 침해하는 데 사용되었다. FBI FLASH 보고서에 따르면 해당 악성코드는 약 163개국의 라우터 및 IoT 기기를 표적으로 삼았으며, 주로 SOHO 기기와 일반 소비자용 네트워킹 장비를 노렸다. 프록시 서비스는 이렇게 침해된 기기에 대한 접근권을 주거용 프록시로 판매하였다.

## 범죄적 이용

소스 자료는 다음과 같은 여러 악용 양상을 기록하고 있다:

- 주거용 IP 주소를 통한 사기 트래픽 발신지 은닉
- 은행 및 암호화폐 계정 탈취
- 부정 실업급여 청구
- FBI 및 파트너 기관이 관찰한 광고 사기, 패스워드 스프레이, 마켓플레이스 사기, 뱅킹 사기, 로맨스 사기 행위
- IP 평판 기반, 지리 기반, 차단 목록 기반 통제 우회를 위한 프록시 네트워크 활용

DOJ는 구체적인 미국 피해 사례로, 약 100만 달러 상당의 암호화폐 사기 피해를 입은 뉴욕 소재 암호화폐 거래소 고객, 약 70만 달러 사기 피해를 입은 펜실베이니아 제조업체, MILITARY STAR 카드가 약 10만 달러 사기에 이용된 현직 또는 전역 미군 장병 사례를 제시하였다.

## 참여 당사자

| 국가 / 기관 | 공개 확인된 참여자 | 역할 |
|---|---|---|
| [[united-states]] | [[us-doj]], 미국 캘리포니아 동부지구 연방검찰청, [[fbi|FBI Sacramento]], [[us-dcis|DCIS]], IRS 형사조사국 오클랜드 지부, DOJ 국제업무국(OIA), DOJ 국가안보 사이버국, DOJ CCIPS, ICHIP 헤이그, FinCEN, 캘리포니아 고속도로순찰대 | 미국 주도 법원 인가 무력화, 도메인 압수, 수사, 암호화폐·금융 지원 |
| [[france]] | 파리 J3 사이버범죄 대응팀, JIRS/JUNALCO 금융·사이버범죄과, [[france-national-police|OFAC]] | 서버·인프라 조치 및 사법 조율 |
| [[austria]] | 오스트리아 형사정보국, 사이버범죄대응센터 C4, 빈 검찰청 | 서버·인프라 조치 및 사법 조율 |
| [[netherlands]] | 림뷔르흐 검찰청, 림뷔르흐 경찰 / 네덜란드 국가경찰 | 서버·인프라 조치 및 사법 조율 |
| [[bulgaria]] | 플로브디프 지방검찰청, GDBOP 사이버범죄국 | Eurojust 전달 사법공조 요청을 통한 작전일 지원 |
| [[germany]] | 뒤셀도르프 경찰청, ZAC NRW | 서버·인프라 및 사법 지원 |
| [[hungary]] | 헝가리 검찰청, 국가수사국 사이버범죄과 | 서버·인프라 및 사법 지원 |
| [[romania]] | 대법원 검찰청, DIICOT 중앙본부, 중앙사이버범죄국, 루마니아 경찰 | 서버·인프라 및 사법 지원 |
| [[eurojust]] | 조정 회의 및 작전일 사법 조율 | 국경 간 사법 조치 준비 및 동기화 |
| [[europol-ec3|Europol]] | 작전·분석 지원, 암호화폐 추적, 악성코드 및 네트워크 분석, 가상 지휘소 운영 | 기술·작전 지원 |
| 민간·기술 파트너 | Lumen Black Lotus Labs, [[shadowserver|Shadowserver Foundation]] | 기술 지원 및 네트워크 무력화 지원 |

## 법적 근거 및 협력 모형

본 작전은 단일 압수 절차에 의존하지 않고 다층적 법적 권한을 결합하였다:

- 프록시 서비스와 연계된 미국 등록 도메인에 대한 **미국 법원 인가 압수영장**.
- 프랑스, 독일, 헝가리, 네덜란드, 루마니아, 미국 소재 인프라에 대해 Eurojust를 통해 준비된 **유럽수사명령(European Investigation Order)**.
- 헤이그에서 수차례 개최된 회의를 포함한, 검사 및 수사판사 대상 **Eurojust 조정**.
- 암호화폐 추적, 악성코드 분석, 네트워크 분석, 데이터베이스 교차조회, 작전일 가상 지휘소 운영을 포함한 **Europol(유럽 사이버범죄센터) 작전 지원**.
- Lumen Black Lotus Labs 및 Shadowserver의 **민간 부문 기술 지원**.

## 작전 타임라인

| 날짜 | 사건 |
|---|---|
| 2020년 여름 | DOJ에 따르면 SocksEscort는 이 시기부터 침해된 IP 주소 접근권을 제공하기 시작하였다. |
| 2026년 2월 | DOJ에 따르면 SocksEscort 애플리케이션에는 약 8,000대의 감염 라우터가 고객에게 접근 가능 상태로 등록되어 있었으며, 그 중 약 2,500대가 미국 내에 있었다. |
| 2026-03-11 | 조정 작전으로 프록시 서비스 인프라를 표적화; Eurojust는 7개국 24대 서버 압류, 34개 도메인 압수를 보고하였다. |
| 2026-03-12 | Eurojust, DOJ/USAO EDCA, IRS-CI, FBI FLASH가 각기 다른 시각에서 단속 사실을 공식 발표하였다. |
| 2026-03-13 | CyberScoop, Cybernews, TechRadar가 SocksEscort 명칭 및 AVrecon/프록시 봇넷 맥락을 다룬 업계 보도를 추가하였다. |
| 2026-04-18 | DOJ Cyber & IP Europe가 추후 ICHIP 헤이그의 Eurojust 조정센터 역할을 확인하고 8개 참여국을 명시하였다. |

## 결과 및 영향

| 지표 | 값 | 소스 근거 |
|---|---:|---|
| 압류된 서버 | 24 | Eurojust |
| 압류 서버 소재 국가 | 7 | Eurojust |
| 압수 도메인 | 34 | Eurojust |
| 동결된 암호화폐 | 약 350만 유로 | Eurojust |
| 플랫폼에 대한 고객 결제 총액 | 500만 유로 초과 | Eurojust |
| 고객 사용자 수 | 약 124,000명 | Eurojust |
| 침해된 라우터/기기 | 약 369,000대 | Eurojust, DOJ, FBI |
| 침해 기기가 분포한 국가 수 | 약 163개국 | Eurojust, FBI |
| 앱에 등록된 활성 감염 라우터 | 2026년 2월 기준 약 8,000대 | DOJ / IRS-CI |
| 미국 내 활성 감염 라우터 | 2026년 2월 기준 약 2,500대 | DOJ / IRS-CI |

## 평가

본 작전은 일반적인 프록시 사이트 압수가 아닌 **악성코드 기반 주거용 프록시 봇넷 무력화**로 해석하여야 한다. 핵심적 법집행 효과는 네 가지 무력화 영역의 동기화에서 발생하였다:

1. **인프라**: 서버 압류 및 도메인 압수
2. **악성코드 생태계**: AVrecon C2 및 중계 노드 무력화
3. **금융 계층**: 결제 플랫폼 표적화 및 암호화폐 동결
4. **피해자 네트워크 정화**: 감염 모뎀의 프록시 서비스 차단 및 FBI 방어 가이드 발행

본 페이지는 침해된 주거용 IP 공간에 대한 상업화된 접근권을 다루었다는 점에서 [[911-s5-botnet-takedown|911 S5]] 및 기타 주거용 프록시 봇넷 단속 사례에 대한 유용한 비교 기준이기도 하다. SocksEscort는 공개 기록상 AVrecon 악성코드, 유럽 측 서버 조율, Eurojust를 통한 작전일 사법 동기화가 강조된다는 점에서 차별성을 갖는다.

## 한국의 참여 (Korean Involvement)

공개적으로 확인된 [[south-korea|대한민국]] 법집행기관의 참여는 없다. FBI 및 Eurojust가 약 **163개국**의 침해 기기를 언급하고 있는 점에 비추어 한국 내 기기도 글로벌 피해 분포에 포함되었을 가능성은 있으나, 현재까지 검토된 공식 소스 중 한국 특정 피해자, 서버, 기관, 후속 조치를 식별한 자료는 없다. 따라서 본 페이지는 한국 관련 후속 1차 자료가 확보되기 전까지 한국의 참여를 단정하지 않는다.

## 미해결 질문

- 본 페이지가 검토한 어떠한 공개 소스도 서비스 운영자의 실명을 명시하지 않는다.
- 수집된 자료에서 체포, 기소, 사건번호는 공개되지 않았다. 체포·기소 건수 필드는 **0/공개되지 않음**으로 유지되며, 이는 피의자가 부존재함을 확정하는 것이 아니다.
- 정확한 도메인 목록 및 서버 목록은 본 페이지에 전체 재현되지 않는다. FBI FLASH는 방어용 지표(IoC)를 제공하나, 압류 자산의 완전한 명세는 제공하지 않는다.
- Eurojust는 약 124,000명의 고객 사용자와 500만 유로 초과의 고객 결제를 보고하며, DOJ는 미국 피해 사례에 초점을 맞춘다. 글로벌 피해 손실 총액은 아직 제시되지 않았다.
- 결제 플랫폼 및 동결된 암호화폐의 최종 법적 처분 상태는 불명확하다.

<!-- SOURCE_ENRICHMENT_START -->

## 소스 커버리지

- Eurojust, 2026-03-12: 전 세계 사이버범죄에 이용된 서버 압류 단속.
- 미국 법무부 USAO EDCA, 2026-03-12: 미국인·기업·금융기관에 수백만 달러 사기 피해를 입힌 글로벌 악성 프록시 서비스 단속.
- 미국 연방수사국, 2026-03-12: SocksEscort에 의해 주거용 프록시로 악용된 AVrecon 악성코드 감염 라우터.
- CyberScoop, 2026-03-13: 당국, 글로벌 프록시 네트워크 SocksEscort 단속.
- Cybernews, 2026-03-13: 369,000개 가정용 인터넷 회선 접근권을 판매한 사이버범죄 서비스 단속.
- TechRadar, 2026-03-13: 리눅스 악성코드로 운영된 SocksEscort 프록시 네트워크, FBI 및 기타 경찰기관에 의해 단속.

## 증거 및 귀속 주석

- Eurojust는 사이버범죄자가 이용한 유료 IP 프록시 서비스에 대한 조치를 보고하였으며, Europol(유럽 사이버범죄센터) 및 8개국 당국과 조율하였다.
- 해당 서비스는 163개국에 걸쳐 약 369,000대의 라우터 및 기타 기기를 침해하였고 약 124,000명의 고객 사용자를 보유하였다.
- 2026년 3월 11일 조정 작전으로 7개국 24대 서버 압류, 34개 도메인 압수, 감염 모뎀 차단, 약 350만 유로 상당 암호화폐 동결이 이루어졌다.
- Eurojust는 참여국을 오스트리아, 불가리아, 프랑스, 독일, 헝가리, 네덜란드, 루마니아, 미국으로 명시하였다.
- 해당 소스는 SocksEscort를 명명하지 않았으나, 추후 DOJ/FBI 자료가 서비스명 및 악성코드군을 확인하였다.
- DOJ는 무력화 대상을 SocksEscort로 명시하였으며, 이는 가정 및 소상공인 라우터를 악용하여 사기를 조력한 주거용 프록시 네트워크이다.
- DOJ는 SocksEscort가 2020년 여름 이래 약 369,000개의 IP 주소 접근권을 제공해 왔고, 2026년 2월 기준 약 8,000대의 감염 라우터가 등록되어 있었으며 그 중 약 2,500대가 미국 내에 있었다고 밝혔다.
- 보도자료는 은행·암호화폐 계정 탈취 및 부정 실업급여 청구를 포함한 사기 이용 사례와 구체적 미국 피해 사례를 기술하였다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본 작전 평가

본 페이지는 피의자 특정 후속 조치가 아닌, SocksEscort 주거용 프록시 서비스, AVrecon 감염 라우터·IoT 기기, 연계된 지휘통제/결제 인프라에 대한 인프라 압류 작전을 기술하므로 정본 작전으로 유지된다. 기록상 주도 책임은 Us Doj에, 조정 책임은 Eurojust에 귀속되며, 참여 또는 영향을 받은 관할로 미국, 프랑스, 오스트리아, 네덜란드, 불가리아, 독일, 헝가리, 루마니아가 기록되어 있다.

협력 모형은 명명된 기관 및 파트너를 통해 문서화되어 있다: Us Doj, Fbi, Us Dcis, IRS 형사조사국 오클랜드 지부, Eurojust, Europol Ec3, 프랑스 국가경찰 OFAC, JIRS/JUNALCO, 림뷔르흐 검찰청, 림뷔르흐 경찰; 메커니즘: 도메인 압수, 수색·압수, 암호화폐 압류, 유럽수사명령, Eurojust 조정 회의, 민관 협력; 법적 근거: Budapest Convention, 형사사법공조, 유럽수사명령; 집행 형태: 압류, 단속, 무력화, 암호화폐 동결.

정본 기록에 포착된 작전 결과: 서버 24대 압류; 도메인 34개 압수; 암호화폐/자산 결과는 미국 당국에 의해 약 350만 유로가 동결된 것으로 기록; SocksEscort 주거용 프록시 서비스는 2026-03-11 무력화; 약 369,000대의 라우터 및 IoT 기기가 2020년 이후 프록시 접근권으로 침해·판매; 2026년 2월 기준 SocksEscort 애플리케이션에 약 8,000대의 감염 라우터 등록(미국 내 약 2,500대 포함); 피해 기기 분포는 약 163개국에 걸쳐 보고; Eurojust는 집행 표적을 102개 피해국에서 사이버범죄용 프록시 활동에 복무하는 것으로 규정.

정본 소스 집합은 6건의 참조를 포함한다: 2026 03 12 Eurojust Proxy Service Takedown, 2026 03 12 Justice Gov Authorities Dismantle Global Malicious Proxy Service Deployed Malware And Defrauded, 2026 03 12 Fbi Gov Avrecon Malware Infected Routers Exploited As Residential Proxies By Socksescort, 2026 03 13 Cyberscoop Com Socksescort Proxy Network Botnet Takedown, 2026 03 13 Cybernews Com Major Residential Proxy Service Socksescort Down, 2026 03 13 Techradar Com Major Socksescort Proxy Network Powered By Linux Malware Taken Down By Fbi And Other Police Forces.
정본 작전의 소스 하한선은 충족되나, 소스의 폭이 곧 모든 후속 체포 또는 형 선고가 본 작전의 일부임을 입증하지는 않는다. 후속 기록은 별도로 연결되어야 한다.
본 페이지에 여전히 남아 있는 메타데이터 공백: 공개 운영자 신원, 체포 또는 기소 여부, 법원 사건번호, 정확한 압수 도메인 및 서버 목록.
데이터셋 활용 측면에서 본 페이지는 작전 단위 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘, 결과 필드는 조정된 집행 행위 전체를 기술한다. 후속 기소, 유죄협상, 형 선고, 범죄인 인도, 자산 몰수는 소스가 명시적으로 이를 새로운 다국적 작전으로 제시하지 않는 한 관련 사건(case) 또는 흡수된 후속 기록으로 부가되어야 한다.
소스 기록에 더 폭넓은 배경, 반복적 통신사 재게시, 또는 주제 페이지성 자료가 포함된 경우 본 평가는 명명된 작전, 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실을 우선시한다. 주변적 소스 제목은 독립적 분류 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능한 상태로 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 전 세계 사이버범죄에 이용된 서버 압류 단속 | Eurojust | 2026-03-12 | https://www.eurojust.europa.eu/news/servers-used-cybercrime-around-world-taken-down |
| [2] | 미국인·기업·금융기관에 수백만 달러 사기 피해를 입힌 글로벌 악성 프록시 서비스 단속 | US DOJ USAO EDCA | 2026-03-12 | https://www.justice.gov/usao-edca/pr/authorities-dismantle-global-malicious-proxy-service-deployed-malware-and-defrauded |
| [3] | SocksEscort에 의해 주거용 프록시로 악용된 AVrecon 악성코드 감염 라우터 | FBI | 2026-03-12 | https://www.fbi.gov/file-repository/cyber-alerts/avrecon-malware-infected-routers-exploited-as-residential-proxies-by-socksescort.pdf |
| [4] | 당국, 글로벌 프록시 네트워크 SocksEscort 단속 | CyberScoop | 2026-03-13 | https://cyberscoop.com/socksescort-proxy-network-botnet-takedown/ |
| [5] | 369,000개 가정용 인터넷 회선 접근권을 판매한 사이버범죄 서비스 단속 | Cybernews | 2026-03-13 | https://cybernews.com/security/major-residential-proxy-service-socksescort-down/ |
| [6] | 리눅스 악성코드로 운영된 SocksEscort 프록시 네트워크, FBI 및 기타 경찰기관에 의해 단속 | TechRadar | 2026-03-13 | https://www.techradar.com/pro/security/major-socksescort-proxy-network-powered-by-linux-malware-taken-down-by-fbi-and-other-police-forces |
