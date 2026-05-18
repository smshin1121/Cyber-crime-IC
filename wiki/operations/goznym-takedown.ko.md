## 개요

GozNym 작전은 단일 단락 규모의 테이크다운이 아닌 조정된 다국적 악성코드 사건이었다. 미국 법무부(DOJ)는 본 네트워크를 GozNym 악성코드를 이용하여 온라인 뱅킹 자격증명을 탈취하고, 피해자 은행 계좌에 접근하며, 미국 및 외국 수익자 계좌를 통해 절취된 자금을 세탁한 초국가적 조직 사이버범죄 그룹으로 기술하였다. 추정된 의도 손실액은 **1억 미국달러**였으며, 전 세계 수만 대의 감염 컴퓨터와 미국 및 유럽에 집중된 피해자 기반을 가졌다.

작전의 의의는 기소 모델에 있다. 미국은 펜실베이니아 서부지구(Western District of Pennsylvania)에서 네트워크의 10명에 대한 혐의 봉인을 해제하였고, 동시에 파트너 관할권들은 모두를 미국 구금으로 데려올 수는 없었던 피고인들에 대해 병행 국내 사건을 추진하거나 증거를 제공하였다.

## 참여 당사자

### 조정 및 사법 기구
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust(유럽사법협력기구)]]
- U.S. Attorney's Office for the Western District of Pennsylvania(미국 펜실베이니아 서부지구 연방검찰)
- [[office-of-international-affairs|DOJ Office of International Affairs(미국 법무부 국제국)]]

### 법 집행 및 검찰 참여 기관
- [[fbi-cyber-division|FBI Pittsburgh Field Office(FBI 피츠버그 지부)]]
- [[us-secret-service|U.S. Secret Service(미국 비밀경호국)]]
- Georgia Prosecutor General and Ministry of Internal Affairs(조지아 검찰총장 및 내무부)
- Ukraine Prosecutor General and National Police(우크라이나 검찰총장 및 국가경찰)
- Moldova Prosecutor General and General Police Inspectorate(몰도바 검찰총장 및 총경찰청)
- Public Prosecutor's Office Verden and Lueneburg Police, Germany(독일 베어덴 검찰청 및 뤼네부르크 경찰)
- Bulgaria Supreme Prosecutor's Office of Cassation and General Directorate for Combatting Organized Crime(불가리아 대법원 검찰청 및 조직범죄 대응 총국)
- [[ncfta|National Cyber-Forensics and Training Alliance]]
- [[shadowserver|Shadowserver Foundation]]

### 참여국
핵심 참여 관할권은 [[united-states|미국]], [[bulgaria|불가리아]], [[germany|독일]], [[georgia|조지아]], [[moldova|몰도바]], [[ukraine|우크라이나]]였다. 러시아는 주로 피고인 거주 및 도주자 관할권으로 등장하며, 현재 자료 집합에서 협력 참여자로 등재되어 있지 않다.

## Cooperation Architecture

본 사건은 여러 협력 채널을 결합하였다. 불가리아 당국은 미국의 요청에 따라 Krasimir Nikolov를 수색 및 체포한 후 2016년 12월 피츠버그로 범죄인 인도하였다. DOJ(미국 법무부) 국제국은 형사사법공조조약(MLAT) 요청을 통해 외국 수색, 체포, 범죄인 인도 요청 및 증거 공유를 조정하였다.

범죄인 인도가 불가능한 피고인의 경우, 모델은 증거 공유 및 병행 국내 기소로 전환되었다. DOJ에 따르면 증거는 조지아, 우크라이나, 몰도바, 불가리아에서의 조정된 압수수색에서 더해 미국 및 독일 수사가 공유한 증거에서 비롯되었다. 조지아는 Alexander Konovolov와 Marat Kazandjian을 국내에서 기소하였고, 우크라이나는 Gennady Kapkanov를 추적하였으며, 몰도바는 Eduard Malanici 및 동료를 추적하였다.

## Defendant and Role Map

| 피고인 / 행위자 | 관할권 상황 | 의심 역할 |
|---|---|---|
| Alexander Konovolov | 조지아에서 기소됨 | 41,000대 이상의 감염된 피해자 컴퓨터를 통제한 조직책 |
| Marat Kazandjian | 조지아에서 기소됨 | 기술 관리자 및 1차 보조 |
| Krasimir Nikolov | 불가리아에서 미국으로 범죄인 인도; 2019년 4월 유죄 인정 답변 | 계좌 탈취 전문가 / 캐셔 |
| Gennady Kapkanov | 우크라이나에서 기소됨 | GozNym 인프라와 연계된 Avalanche 방탄 호스팅 관리자 |
| Eduard Malanici | 몰도바에서 기소됨 | 백신 탐지를 회피하기 위해 사용된 크립팅 서비스 제공자 |
| Farkhad Manokhin | 미국 요청에 따라 스리랑카에서 체포 후 러시아로 도주 | 현금화 / 드롭 마스터 역할 |
| 5명의 러시아 국적자 | DOJ 기록상 도주자 | 악성코드 개발, 스팸 배포, 캐싱, 현금화 기능 |

## Evidence and Infrastructure

기소장은 러시아어 범죄 포럼에서 모집된 사이버범죄-서비스(cybercrime-as-a-service) 구조를 기술하였다. 구성원들은 악성코드 개발, 스팸 배포, 크립팅, 계좌 탈취, 현금화, 방탄 호스팅 서비스를 제공하였다. Kapkanov의 의심되는 역할은 GozNym을 독일 주도 작전이 이미 2016년에 표적으로 삼았던 Avalanche 호스팅 인프라에 연결시켰다.

피해자 사례는 미국 기업들, 법무법인, 교회, 장애인 봉사 협회, 카지노, 그리고 미국 자회사를 가진 독일 의료기기 유통업체를 포함한다. 이러한 구성은 관할권에 있어 중요하다: 펜실베이니아 서부지구 사건은 추상적 미국 피해만이 아니라 명명된 미국 법인 및 은행 영향에 기반하였다.

## Legal Basis

수집된 자료들은 세 가지 구체적인 절차적 메커니즘을 식별한다: 범죄인 인도, 압수수색, 그리고 형사사법공조조약(MLAT) 기반 증거 공유. 기록은 단일 합동 법원을 보여주지 않고, 각 국가가 Europol(유럽 경찰청)과 Eurojust(유럽사법협력기구)를 통해 증거를 공유하고 공공 집행 행동을 조정하면서 자국의 형사 절차를 사용한 분산 모델을 보여준다. 이것이 본 페이지가 작전을 통상적인 단일 국가 기소가 아닌 합동수사 및 병행 기소 사안으로 다루는 이유이다.

## Results

- 새로 봉인 해제된 미국 기소장에서 **10명의 피고인**이 기소되었으며, 11번째 구성원이 별도로 기소됨.
- Konovolov가 통제한 것으로 알려진 **41,000대 이상의 감염된 피해자 컴퓨터**.
- **1억 미국달러**의 추정 의도 절취액.
- 미국, 조지아, 우크라이나, 몰도바, 독일, 불가리아 전반에 걸친 병행 기소 및 증거 공유.
- Nikolov는 불가리아에서 미국으로 범죄인 인도되어 선고 전에 유죄 인정 답변을 하였다.

## Open Questions

- 현재 페이지는 모든 러시아 도주자의 최종 상태를 아직 해결하지 못하였다.
- 일부 외국 기소 결과는 2019년 후속 DOJ 선고 자료에 포함되어 있으나, 조지아, 우크라이나, 몰도바, 불가리아의 전체 사건 기록은 별도의 사건 수준 조정이 필요하다.
- 코퍼스의 Europol 자료는 요약 수준이며, DOJ 자료가 작전적 세부사항의 대부분을 담고 있어 메커니즘에 대한 주요 자료로 유지되어야 한다.

## Source Coverage

참고문헌 [2]인 DOJ 발표가 1차 메커니즘 자료이다. 참고문헌 [1]은 해체에 대한 Europol(유럽 경찰청)의 공개 표현을 확인한다. 참고문헌 [3]은 3명의 구성원에 대한 후기 기소 결과 데이터를 제공한다. 참고문헌 [4]와 [5]는 미디어 보강 자료이며 세부사항이 충돌하는 경우 공식 DOJ/Europol 기록을 우선해야 한다.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2019-05-01: 국제 작전에서 해체된 GozNym 악성코드 사이버범죄 네트워크.
- US DOJ (W.D. Pa.), 2019-05-16: 미국 법인을 표적으로 유럽에서 운영된 GozNym 사이버범죄 네트워크가 국제 작전으로 해체됨.
- US DOJ USAO, 2019-12-20: GozNym 사이버범죄 네트워크의 3명의 구성원이 피츠버그와 조지아 트빌리시의 병행 다국적 기소에서 선고됨.
- BBC News, 2019-05-16: BBC: 수백만을 절취한 GozNym 사이버범죄 조직 검거.
- BleepingComputer, 2019-05-16: 1억 달러 피해 배후 GozNym 사이버범죄 그룹 해체.

## 작전 타임라인

- 2016: 활동 또는 수사 개시.
- 2019-05: 공개 발표.
- 2019-05: 보고된 집행 종점.
- 2019-05-01: Europol의 공개 자료 보도.
- 2019-05-16: BBC News, BleepingComputer, US DOJ (W.D. Pa.)의 공개 자료 보도.
- 2019-12-20: US DOJ USAO의 공개 자료 보도.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US DOJ (W.D. Pa.), 2019-05-16: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs GozNym Cyber-Criminal Network Operating Out Of Europe Targeting American Entities Dismantled In International Operation This is archived content from the U.S.
- US DOJ (W.D. Pa.), 2019-05-16: The operation was highlighted by the unprecedented initiation of criminal prosecutions against members of the network in four different countries as a result of cooperation between the United States, Georgia, Ukraine, Moldova, Germany, Bulgaria, Europol and Eurojust.
- US DOJ USAO, 2019-12-20: Attorney's Office, Western District of Pennsylvania PITTSBURGH - A resident of Varna, Bulgaria, was sentenced on December 16, 2019, in federal court in Pittsburgh to a period of time served after having served more than 39 months in prison following his conviction on charges of criminal conspiracy, computer fraud, and bank fraud for his.
- US DOJ USAO, 2019-12-20: At the request of the United States, Nikolov was arrested in September 2016 by Bulgarian authorities and extradited to Pittsburgh in December 2016 to face prosecution in the Western District of Pennsylvania.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 특정 피고인에 한정된 후속 조치가 아니라 GozNym 악성코드 네트워크에 대한 합동수사를 기술하는 정전(canonical) 작전 페이지로서 유지된다. 본 기록은 주도 책임을 Europol EC3에 두고 조정도 Europol EC3에 부여하며, 참여 또는 영향을 받은 관할권은 미국, 불가리아, 독일, 조지아, 몰도바, 우크라이나로 기록한다.

협력 모델은 다음의 명시된 기관 및 파트너를 통해 문서화된다: Europol Ec3, Eurojust, Fbi Cyber Division, Office Of International Affairs, Us Secret Service, Ncfta, Shadowserver, U.s. Attorney's Office For The Western District Of Pennsylvania, Office Of The Prosecutor General Of Georgia, Prosecutor General's Office Of Ukraine; 메커니즘: 형사사법공조, 범죄인 인도, 압수수색, 전자증거, 민관 협력; 법적 근거: 형사사법공조, 범죄인 인도, 압수수색, 전자증거.

정전 기록에 포착된 작전 결과: 체포 10명; 기소 10건; 추정 1억 미국달러 의도 절취액; 네트워크 우두머리가 41,000대 이상의 피해자 컴퓨터를 통제함; 미국, 조지아, 우크라이나, 몰도바, 불가리아에서 병행 기소 개시; 조지아, 우크라이나, 몰도바, 불가리아의 조정된 압수수색을 통한 증거 획득.

정전 자료 집합은 5건의 참고 자료를 포함한다: 2019 05 01 Europol Europa Eu Goznym Malware Cybercriminal Network Dismantled In International Operation, 2019 05 16 Justice Gov Goznym Cyber Criminal Network Operating Out Of Europe Targeting American Entitie, 2019 12 20 Justice Gov Three Members Of Goznym Cybercrime Network Sentenced In Parallel Multi National, Bbc Goznym Malware Network Dismantling, 2019 05 16 Bleepingcomputer Com Goznym Cybercrime Group Behind 100 Million Damages Dismantled.
정전 작전을 위한 자료 하한선은 충족되었으나, 자료의 폭이 그 자체로 모든 하류 체포 또는 형 선고가 본 작전의 일부임을 입증하지는 않는다; 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지가 여전히 보유하고 있는 알려진 메타데이터 공백: Final Status For All Fugitives 및 Complete Foreign Sentencing Outcomes.
데이터셋 사용 목적상 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다: 국가, 기관, 메커니즘 및 결과 필드는 조정된 집행 조치 전체를 기술한다. 후속 기소, 답변, 형 선고, 범죄인 인도 또는 몰수 조치는 자료가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건으로 첨부되거나 흡수된 후속 기록으로 처리되어야 한다.
자료 기록이 더 넓은 배경, 반복된 통신사 재게재, 또는 주제 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과와 직접 연결된 사실에 우선순위를 둔다. 주변적 자료 제목은 독립적인 분류 또는 결과 증거로 취급되지 않는다.
이는 정전 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 국제 작전에서 해체된 GozNym 악성코드 사이버범죄 네트워크 | Europol | 2019-05-01 | https://www.europol.europa.eu/media-press/newsroom/news/goznym-malware-cybercriminal-network-dismantled-in-international-operation |
| [2] | 미국 법인을 표적으로 유럽에서 운영된 GozNym 사이버범죄 네트워크가 국제 작전으로 해체됨 | US DOJ (W.D. Pa.) | 2019-05-16 | https://www.justice.gov/archives/opa/pr/goznym-cyber-criminal-network-operating-out-europe-targeting-american-entities-dismantled |
| [3] | GozNym 사이버범죄 네트워크의 3명의 구성원이 피츠버그와 조지아 트빌리시의 병행 다국적 기소에서 선고됨 | US DOJ USAO | 2019-12-20 | https://www.justice.gov/usao-wdpa/pr/three-members-goznym-cybercrime-network-sentenced-parallel-multi-national-prosecutions |
| [4] | BBC: 수백만을 절취한 GozNym 사이버범죄 조직 검거 | BBC News | 2019-05-16 | https://www.bbc.com/news/technology-48294788 |
| [5] | 1억 달러 피해 배후 GozNym 사이버범죄 그룹 해체 | BleepingComputer | 2019-05-16 | https://www.bleepingcomputer.com/news/security/goznym-cybercrime-group-behind-100-million-damages-dismantled/ |
