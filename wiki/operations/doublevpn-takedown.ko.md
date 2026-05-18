## 개요

**2021년 6월 29일**, **9개국**의 법집행 기관은 러시아어 및 영어권 사이버범죄 포럼에서 범죄 활동, 특히 랜섬웨어 작전을 은폐하기 위한 도구로 적극 홍보되어 온 가상 사설망(VPN) 서비스인 **DoubleVPN(불법 VPN 서비스)**의 인프라를 동시에 압수하였다. 본 작전은 네덜란드 국가 검찰청의 관할 하에 [[netherlands-politie|네덜란드 국가경찰(Dutch National Police)]]이 주도하였으며, 국제적 조정은 [[europol-ec3|Europol EC3(유럽 경찰청 사이버범죄센터)]]와 [[eurojust|Eurojust(유럽사법협력기구)]]가 담당하였다.

DoubleVPN은 단일·이중·삼중·사중 VPN 연결을 **22유로(약 25달러)**의 저렴한 가격으로 제공하였으며, 다층 익명화 기능을 통해 정부 및 국가 인프라를 표적으로 한 랜섬웨어 운영자들에게 선호되는 도구가 되었을 가능성이 *highly likely* 높다.

본 작전은 이러한 유형의 **범죄 조력형 VPN 서비스에 대한 법집행 기관의 첫 직접 조치**였으며, 이후 사이버범죄 인프라 제공자들을 대상으로 한 후속 작전(cf. [[vpnlab-takedown|VPNLab.net 테이크다운]], 2022년 1월)의 선례를 마련하였다.

## 배경

DoubleVPN은 트래픽을 여러 관할권의 다수 서버를 통해 라우팅하여 추적을 매우 어렵게 만드는 최대 사중 암호화 계층을 제공하는 VPN 서비스였다. 정상적인 VPN 제공자와는 달리, DoubleVPN은 **특별히 사이버범죄자를 대상으로 마케팅되었다**:

- **광고 채널**: 러시아어(예: XSS, Exploit.in) 및 영어권 지하 사이버범죄 포럼
- **표적 고객**: 랜섬웨어 운영자, 피싱 사기범, 비즈니스 이메일 침해(BEC) 행위자
- **가격 책정**: 기본 연결 22유로부터 시작
- **기술적 특징**: 서로 다른 국가에 걸친 단일/이중/삼중/사중 VPN 체인

네덜란드 검찰의 성명은 그 의도에 대해 명시적이었다: *"By taking legal action, including special investigatory power for digital intrusion, we want to make clear there cannot be any safe havens for these kind of criminals."* (Wieteke Koorn, Leading Dutch Public Prosecutor)
> (한국어 번역: 디지털 침입을 위한 특별수사권을 포함한 법적 조치를 취함으로써, 우리는 이러한 종류의 범죄자들에게 어떠한 안전한 피난처도 있을 수 없음을 분명히 하고자 한다.)

## 참여 당사자

### Lead Agency
- [[netherlands-politie|네덜란드 국가경찰]], 네덜란드 국가 검찰청 관할 하

### Coordinating Bodies
- [[europol-ec3|Europol EC3(유럽 경찰청 사이버범죄센터)]] — 테이크다운 준비를 위한 **30회 이상의 조정회의** 및 **4회의 워크숍** 조직; 분석 및 암호화폐 추적 지원 제공
- [[eurojust|Eurojust(유럽사법협력기구)]] — 2020년 10월 이래 **6회의 전담 조정회의** 조직; **작전일에 조정 센터** 설치

### Participating Countries and Agencies (9 countries)

| 국가 | 기관 |
|---|---|
| [[netherlands|네덜란드]] | 국가경찰, 국가 검찰청 |
| [[united-states|미국]] | [[fbi-cyber-division|FBI(미국 연방수사국)]], [[us-secret-service|미국 비밀경호국]], [[us-doj|DOJ(미국 법무부)]] |
| [[canada|캐나다]] | [[canada-rcmp|RCMP(캐나다 왕립기마경찰)]] |
| [[germany|독일]] | [[germany-bka|BKA(독일 연방수사청)]], 프랑크푸르트 검찰청 |
| [[united-kingdom|영국]] | [[uk-nca|NCA(영국 국가범죄청)]] (국가 사이버범죄 부서) |
| [[sweden|스웨덴]] | 스웨덴 경찰청, 스웨덴 검찰청 |
| [[italy|이탈리아]] | 국가경찰(우편/통신서비스부), 밀라노 검찰청 |
| [[bulgaria|불가리아]] | 조직범죄 척결 총국 |
| [[switzerland|스위스]] | 티치노 주(州) 경찰, 티치노 검찰청 |

## 법적 근거

- **[[empact|EMPACT]]** (European Multidisciplinary Platform Against Criminal Threats) — 우선순위 범죄 분야에 대한 EU의 포괄적 프레임워크
- **네덜란드의 디지털 침입 수사권**(hackbevoegdheid) — 네덜란드 경찰은 DoubleVPN의 인프라를 침투하기 위해 디지털 침입에 대한 법적 권한을 행사하였다. 이는 *법적으로 중요한* 세부사항으로, 네덜란드는 2019년 컴퓨터 범죄법 III(Wet computercriminaliteit III)을 제정하여 경찰에 범죄 인프라를 해킹할 수 있는 권한을 부여하였다
- 공동수사팀(JIT) 결성은 명시적으로 언급되지 않았다

## 작전 타임라인

| 일자 | 사건 |
|---|---|
| 2020년 10월경 | DoubleVPN에 대한 수사 개시; Eurojust 조정회의 시작 |
| 2020년 10월 – 2021년 6월 | Europol 조정회의 30회 이상, 워크숍 4회, Eurojust 회의 6회 |
| 2021-06-29 | **작전일**: 9개국에 걸쳐 DoubleVPN 웹 도메인 및 서버 동시 압수 |
| 2021-06-30 | Europol, Eurojust, 네덜란드 경찰, 영국 NCA의 공개 발표 |

## 결과 및 영향

### 압수된 인프라
- **웹 도메인**이 압수되어 법집행 안내 페이지로 대체됨
- 9개국에 걸친 **서버 인프라**가 동시에 연결 차단됨
- DoubleVPN 서버로부터 **고객 개인정보, 로그, 통계** 압수 — 범죄 사용자에 대한 후속 수사 가능
- 본 작전의 일부로 이루어진 **체포는 없음**

### UK-Specific Results
[[uk-nca|영국 NCA]]는 DoubleVPN 네트워크의 영국 노드를 오프라인으로 전환하였으며 이어서:
- DoubleVPN을 통해 네트워크가 불법적으로 접근된 **여러 영국 기업**을 식별
- 해당 조직들에 **직접 통지**하고 시스템 보안 강화에 협조

### Precedent Value
NCA 부청장 John Denley는 다음과 같이 말했다: *"This is the first time law enforcement has been able to take direct action against a criminal enabling service of this type."*
> (한국어 번역: 이것은 법집행 기관이 이러한 유형의 범죄 조력 서비스에 대해 직접적 조치를 취할 수 있었던 첫 사례이다.)

이는 개별 범죄 그룹이 아닌 사이버범죄 인프라 제공자를 표적으로 한 새로운 집행 모델을 확립하였다.

## 활용된 협력 메커니즘

- **Europol EC3 가상 지휘소** — 실시간 조정을 위해 작전일에 설치
- **Europol 분석 및 암호화폐 추적 지원** — 수사 전반에 걸쳐 제공
- **Eurojust 조정 센터** — 작전일의 사법적 조정
- **EMPACT 프레임워크** — EU 전역 범죄 위협으로 사이버범죄를 우선 분류

## 도전 및 마찰 요인

- **체포 없음**: 인프라와 고객 데이터를 압수했음에도 불구하고, 운영자가 공개적으로 식별되거나 체포되지 않았다. 이는 운영자들이 자체 익명화 도구를 사용한 결과일 수 있다.
- **서버 수 미공개**: Europol이나 참여 기관 모두 압수된 서버의 총 수를 공개하지 않았다 — 통상 규모를 강조하는 인프라 압수 작전으로서는 이례적이다.

## 교훈

1. **인프라 우선 접근**: 개별 범죄 사용자가 아닌 조력 서비스를 표적으로 함으로써 더 광범위한 생태계를 교란한다. 압수된 고객 로그는 후속 수사를 가능하게 한다.
2. **조력자로서의 네덜란드 hackbevoegdheid**: 디지털 침입에 대한 법적 권한을 부여한 네덜란드의 2019년 컴퓨터 범죄법 III은 DoubleVPN 인프라 침투에 *almost certainly* 필수적이었다. 이는 네덜란드를 유사 작전의 주도국으로 독특하게 자리매김하게 한다.
3. **광범위한 사전 준비**: 단일 작전일을 위한 8개월의 조정(Europol 회의 30회 이상, Eurojust 회의 6회, 워크숍 4회)은 다국적 동시 압수에 필요한 투자를 보여준다.
4. **후속 작전**: DoubleVPN 모델은 [[vpnlab-takedown|VPNLab.net]](2022년 1월, 10개국 15개 서버)을 위해 복제되었으며 — 이는 제도적 학습을 보여준다.

## 후속 조치

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.


- DoubleVPN 서버에서 압수된 고객 데이터는 *likely* 참여국 전반의 후속 랜섬웨어 수사에 활용되었을 것이다
- [[vpnlab-takedown|VPNLab.net 테이크다운]](2022년 1월)은 DoubleVPN 선례를 직접 참조하였다
- 범죄 인프라(VPN, 방탄 호스팅, 암호화 통신)를 표적으로 하는 광범위한 추세는 2022-2025년에 걸쳐 지속되었다

## 한국의 참여

본 작전에서 한국의 참여는 알려진 바 없다. 다만 DoubleVPN의 고객 기반에는 해당 서비스가 조력한 랜섬웨어 작전의 전 세계적 도달 범위를 고려할 때 한국 기관을 표적으로 한 행위자들이 포함되었을 *likely* 가능성이 있다.

## 모순점 및 미해결 문제

- **압수된 서버는 몇 대였는가?** Europol이나 참여 기관 어느 곳도 총 서버 수를 공개하지 않았다 — 인프라 압수 작전으로서는 주목할 만한 누락이다.
- **DoubleVPN 운영자가 식별된 적이 있는가?** 체포나 기소가 발표되지 않았다. 고객 데이터가 운영자 식별로 이어졌는지는 알려지지 않았다.
- **고객 기반 규모는 어느 정도였는가?** DoubleVPN 가입자 수 및 범죄 활동에 참여한 비율은 공개되지 않았다.
- **후속 랜섬웨어 체포와의 관계**: 압수된 DoubleVPN 로그가 2021-2022년의 랜섬웨어 운영자 체포에 직접 기여하였는가?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2021-06-30: Europol: Coordinated action cuts off access to VPN service used by ransomware groups.
- Eurojust, 2021-06-30: Coordinated action cuts off access to VPN service used by ransomware groups.
- Eurojust, 2022-03-02: Eurojust Annual Report 2021: DoubleVPN case example.
- UK NCA, 2021-06-30: DoubleVPN takedown: NCA takes UK server of criminal network offline.
- The Record, 2021-06-30: Dutch police takes down DoubleVPN, a service used by cybercrime groups.

## Evidence and Attribution Notes

- DoubleVPN web domains and server infrastructure seized across 9 countries on 29 June 2021
- Dutch National Police led the operation under the Dutch National Public Prosecutor's Office; Europol EC3 organized 30+ coordination meetings and 4 workshops
- Eurojust organized 6 dedicated coordination meetings since October 2020 and established a coordination centre on the action day
- DoubleVPN offered single/double/triple/quadruple VPN connections from €22, marketed on Russian and English cybercrime forums
- Customer personal information, logs, and statistics were seized — enabling follow-on investigations
- No arrests announced; first law enforcement takedown of a criminal-enabling VPN service
- Participating agencies: Dutch Police, FBI, US Secret Service, DOJ, RCMP, BKA, NCA, Swedish Police, Italian State Police, Bulgarian GDOC, Cantonal Police Ticino
- Operating under EMPACT framework; Dutch 'hackbevoegdheid' (digital intrusion power) used

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against DoubleVPN (multi-layered VPN service marketed to cybercriminals), rather than a defendant-specific follow-on action. The record attributes lead responsibility to Dutch National Police and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Netherlands, United States, Canada, Germany, United Kingdom, Sweden, Italy, Bulgaria, Switzerland.

The cooperation model is documented through named agencies and partners: Dutch National Police, Europol EC3, Eurojust, FBI, US Secret Service, US DOJ, RCMP, BKA, UK NCA; legal basis: EMPACT (European Multidisciplinary Platform Against Criminal Threats); enforcement posture: Seizure and Takedown.

Operational results captured for the canonical record: 1 domains seized; DoubleVPN web domains and server infrastructure seized across 9 countries; Customer personal information, logs, and statistics seized from servers; UK businesses notified of unauthorized network access via DoubleVPN; Law enforcement splash page displayed on seized domains.

The canonical source set contains 5 reference(s): Europol Press Release 2021-06-30, 2021 06 30 Eurojust Coordinated Action Cuts Access Vpn Service Used Ransomware Groups, 2022 03 02 Eurojust Annual Report 2021 Doublevpn Case Example, 2021 06 30 Nationalcrimeagency Gov Uk Doublevpn Takedown Nca Takes Uk Server Of Criminal Network Offline, 2021 06 30 Therecord Media Dutch Police Takes Down Doublevpn A Service Used By Cybercrime Groups.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Servers Seized Count and Customer Count.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Coordinated action cuts off access to VPN service used by ransomware groups | Europol | 2021-06-30 | https://www.europol.europa.eu/media-press/newsroom/news/coordinated-action-cuts-access-to-vpn-service-used-ransomware-groups |
| [2] | Coordinated action cuts off access to VPN service used by ransomware groups | Eurojust | 2021-06-30 | https://www.eurojust.europa.eu/news/coordinated-action-cuts-access-vpn-service-used-ransomware-groups |
| [3] | DoubleVPN takedown: NCA takes UK server of criminal network offline | UK NCA | 2021-06-30 | https://www.nationalcrimeagency.gov.uk/news/doublevpn-takedown-nca-takes-uk-server-of-criminal-network-offline |
| [4] | Dutch police takes down DoubleVPN, a service used by cybercrime groups | The Record | 2021-06-30 | https://therecord.media/dutch-police-takes-down-doublevpn-a-service-used-by-cybercrime-groups |
| [5] | Eurojust Annual Report 2021: DoubleVPN case example | Eurojust | 2022-03-02 | https://www.eurojust.europa.eu/annual-report-2021/cybercrime/case-examples |
