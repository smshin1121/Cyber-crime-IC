## 개요

911 S5 작전은 미국이 주도한 주거용 프록시 봇넷 및 사기 조력 서비스에 대한 무력화 작전이다. DOJ(미국 법무부)와 FBI(미국 연방수사국)는 본 작전을 독일, 싱가포르, 태국과의 다국가 공조 작전으로 기록하고 있으며, IC3 및 FBI의 부속 권고문은 피해자 측 감염 모델을 설명하고 있다. 한편 재무부(Treasury) 보도자료는 제재 및 금융 차단 계층을 추가한다.

대상은 단일 악성코드 패밀리 단독이 아니었다. 911 S5는 번들 또는 불법 복제된 VPN 애플리케이션과 연계된 감염을 포함하여 침해된 주거용 기기로 구축된 프록시 인프라로 운영되었다. 이 인프라는 고객이 피해자의 IP 주소를 통해 트래픽을 라우팅할 수 있게 하였으며, 사기, 신원 도용, 아동 착취 활동, 폭탄 협박, 불법 거래 및 액세스 브로커링에 사용되었다.

## 참여 당사자

| 역할 | 당사자 |
|---|---|
| 형사 주관 기관 | [[us-doj\|미국 법무부]] |
| 수사 및 피해자 안내 기관 | [[fbi\|FBI]], IC3 대외 공개 안내 포함 |
| 금융 차단 | [[us-treasury\|미국 재무부 / OFAC]] |
| 지정 파트너 관할권 | [[germany\|독일]], [[singapore\|싱가포르]], [[thailand\|태국]] |

## 결과 및 영향

- DOJ 출처에서 911 S5의 관리자(administrator)로 기술된 YunHe Wang이 체포되었다.
- 봇넷은 공식 출처 세트에서 거의 200개국에 걸쳐 1,900만 개 이상의 IP 주소에 영향을 미친 것으로 평가되었다.
- IC3 및 FBI 안내문은 주거용 프록시 감염 경로를 식별하고 영향을 받은 사용자에 대한 정리 지침을 제공하였다.
- OFAC(미국 해외자산통제국) 제재는 Wang, 공범 2명, 그리고 연관된 3개 법인을 대상으로 하여, 본 무력화 작전이 형사 절차와 금융 제한을 결합하였음을 보여준다.

## 협력 모델

본 작전은 세 가지 계층을 결합한다. DOJ/FBI에 의한 형사 수사 및 체포 공조, 독일·싱가포르·태국으로부터의 파트너국 지원, 그리고 재무부/OFAC의 병행 제재 조치이다. 데이터셋 활용 측면에서 본 페이지는 기술적 구제(remediation) 요소와 금융 차단 요소를 모두 갖춘 봇넷 서비스 무력화 작전으로 해석되어야 한다.

<!-- SOURCE_ENRICHMENT_START -->

## 출처 커버리지

- 미국 법무부, 2024년 5월 29일: 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation.
- 인터넷범죄신고센터(IC3), 2024년 5월 29일: Guidance on the 911 S5 Residential Proxy Service.
- 미국 연방수사국, 2024년 6월 7일: Inside the FBI Podcast: The 911 S5 Cyber Threat.
- 미국 재무부, 2024년 5월 28일: Treasury Sanctions a Cybercrime Network Associated with the 911 S5 Botnet.
- 미국 연방수사국, 2024년 5월 29일: How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors.

## 작전 타임라인

- 2024년 5월: 활동 또는 수사 개시.
- 2024년 5월: 공개 발표.
- 2024년 5월: 보고된 집행 종결 시점.
- 2024년 5월 28일: 미국 재무부의 공개 출처 보도.
- 2024년 5월 29일: 미국 연방수사국, 인터넷범죄신고센터(IC3), 미국 법무부의 공개 출처 보도.
- 2024년 6월 7일: 미국 연방수사국의 공개 출처 보도.

## 법적 및 절차적 위상

- 기록된 범죄 분류: 악성코드 및 CSAM(아동 성착취물).
- 본 기록은 테이크다운으로 분류되어 있으며, 상태는 완료(completed)이다.
- 관련 법적 또는 작전 기록: Us V Yunhe Wang 911 S5.

## 증거 및 귀속 관련 노트

- 이 DOJ 공보국(Office of Public Affairs) 보도자료는 2024년 5월 911 S5 무력화 작전에 대한 주된 공개 기술 자료이다.
- 본 자료는 해당 작전 및 사건 페이지에 가장 유용한 작전 일자, 체포 시점, 전 세계 감염 규모, 그리고 압수 수치를 제공한다.
- 미국 법무부와 FBI는 독일, 싱가포르, 태국과의 협력 하에 911 S5 봇넷 — 거의 200개국에 걸쳐 1,900만 개 이상의 IP 주소를 감염시켰던 세계 최대 봇넷 — 을 무력화하였다.
- 본 봇넷은 대규모 사기, 신원 도용, 아동 성착취, 폭탄 협박, 불법 금융 거래를 조력하는 데 사용되었다.
- IC3는 911 S5를 1,900만 개 이상의 침해된 IP 주소가 190개국 이상에 걸쳐 있는 최대 규모의 주거용 프록시 서비스이자 봇넷 중 하나로 기술하였다.
- 권고문은 프록시 백도어와 연계된 VPN 애플리케이션으로 MaskVPN, DewVPN, PaladinVPN, ProxyGate, ShieldVPN, ShineVPN을 식별하였다.
- 권고문은 본 봇넷을 사기, 신원 도용, 아동 착취 및 초기 접근 브로커링의 수단으로 규정하였다.
- 이 공공 서비스 발표는 911 S5가 번들 VPN 애플리케이션 및 불법 복제 소프트웨어를 통해 어떻게 확산되었는지를 피해자 관점에서 가장 명확하게 설명한다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## 원시 출처 하이라이트

- FBI, 2024년 6월 7일: 제목: Inside the FBI Podcast: The 911 S5 Cyber Threat | Federal Bureau of Investigation URL Source: Markdown Content: _[활기찬 음악과 박동치는 신디사이저가 시작된다.]_ **내레이터:** 어떤 종류든 불법 복제 콘텐츠를 다운로드하는 것은 본질적인 위험을 수반한다.
- FBI, 2024년 6월 7일: FBI와 파트너 기관들은 최근 악성 사이버 행위자들이 바로 그러한 짓 — 감염된 비디오 게임 및 소프트웨어를 사용하여 피해자의 기기를 탈취하고 사이버 범죄를 저지른 뒤 마치 피해자가 해당 불법 활동의 당사자인 것처럼 보이게 하는 행위 — 을 하는 것을 적발하였다.
- 미국 재무부, 2024년 5월 28일: Department of the Treasury About Treasury Enter Search Term(s): Advanced Search General Information Role of the Treasury Officials Organizational Chart Orders and Directives Offices Domestic Finance Economic Policy General Counsel International Affairs Management Public Affairs Tax Policy Terrorism and Financial Intelligence Tribal and.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 정본(Canonical) 작전 평가

본 페이지는 피고인 특정 후속 조치가 아니라 911 S5 봇넷에 대한 테이크다운을 기술하므로 정본 작전으로 유지된다. 본 기록은 주관 책임을 Usdoj에, 공조 책임을 Fbi에 귀속시키며, 참여 또는 영향을 받은 관할권은 미국, 독일, 싱가포르, 태국으로 기록되어 있다.

협력 모델은 DOJ/FBI의 형사 절차, 지정된 파트너 관할권, 공공 피해자 안내, 그리고 관련된 재무부/OFAC 금융 차단 조치를 통해 가시화된다.

정본 기록에 포착된 작전 결과: 체포 1건; 기소 1건; 1,900만 개 이상의 IP 주소에 영향을 미친 주거용 프록시 봇넷의 무력화; 관리자 네트워크에 대한 OFAC 제재.

정본 출처 세트는 5건의 참고자료를 포함한다: 2024 05 29 Justice Gov Justice Department Leads Effort To Dismantle 911 S5 Botnet, 2024 05 29 Ic3 Gov Guidance On The 911 S5 Residential Proxy Service, 2024 06 07 Fbi Gov The 911 S5 Cyber Threat, 2024 05 28 Treasury Gov Treasury Sanctions A Cybercrime Network Associated With The 911 S5 Botnet, 2024 05 29 Fbi Gov How To Identify And Remove Vpn Applications That Contain 911 S5 Backdoors.
정본 작전에 대한 출처 하한 요건은 충족되나, 출처의 폭만으로 모든 하류(downstream)의 체포 또는 양형이 본 작전의 일부임을 입증하지는 못한다. 후속 기록은 별도로 연결된 상태를 유지하여야 한다.
현재 본 페이지에는 프론트매터의 missing-field 플래그가 부여되어 있지 않다.
데이터셋 활용 측면에서 본 페이지는 작전 단위 집계 지점으로 취급되어야 한다. 즉, 국가, 기관, 메커니즘 및 결과 필드는 공조된 집행 행위 전체를 기술한다. 이후의 기소, 답변, 양형, 범죄인 인도 또는 몰수 조치는, 해당 출처가 이를 새로운 다국가 작전으로 명시적으로 제시하지 않는 한, 관련 사건으로 부착되거나 흡수된 후속 기록으로 처리되어야 한다.
출처 기록이 폭넓은 배경 정보, 반복된 통신사 재게재, 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 참여 당국, 대상 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과와 직접 연결된 사실에 우선순위를 둔다. 주변적 출처 제목은 독립적인 분류 체계 또는 결과 증거로 취급되지 않는다.
이는 정본 기록을 분석적으로 한정되고 재현 가능하게 유지한다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | 911 S5 봇넷 무력화 및 관리자 체포 — 공조된 국제 작전 (911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation) | U.S. Department of Justice | 2024-05-29 | https://www.justice.gov/archives/opa/pr/911-s5-botnet-dismantled-and-its-administrator-arrested-coordinated-international-operation |
| [2] | 911 S5 주거용 프록시 서비스에 관한 안내 (Guidance on the 911 S5 Residential Proxy Service) | IC3 | 2024-05-29 | https://www.ic3.gov/PSA/2024/PSA240529 |
| [3] | Inside the FBI 팟캐스트: 911 S5 사이버 위협 (Inside the FBI Podcast: The 911 S5 Cyber Threat) | FBI | 2024-06-07 | https://www.fbi.gov/news/podcasts/inside-the-fbi-podcast-the-911-s5-cyber-threat |
| [4] | 911 S5 봇넷과 연관된 사이버범죄 네트워크에 대한 재무부 제재 (Treasury Sanctions a Cybercrime Network Associated with the 911 S5 Botnet) | U.S. Treasury | 2024-05-28 | https://home.treasury.gov/news/press-releases/jy2375 |
| [5] | 911 S5 백도어가 포함된 VPN 애플리케이션 식별 및 제거 방법 (How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors) | FBI | 2024-05-29 | https://www.fbi.gov/investigate/cyber/how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors |
