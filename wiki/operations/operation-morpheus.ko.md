## 개요

**Operation Morpheus(모르페우스 작전, Cobalt Strike Europol)** 는 영국 국가범죄청(NCA) 주도, Europol(유럽 경찰청) 조정으로 진행된 국제 작전으로서, 합법적 침투 테스트 도구이나 랜섬웨어 공격·간첩 활동·기타 악의적 목적으로 사이버범죄자들에게 광범위하게 악용되어 온 **Cobalt Strike** 의 무단(불법 복제/크랙) 인스턴스를 표적으로 삼았다. 본 작전은 **27개국에 걸친 593대의 Cobalt Strike 서버** 의 소탕이라는 결과로 이어졌다.

본 작전은 특정 범죄 집단이 아닌 이중 용도 도구의 범죄적 악용을 표적으로 삼아, 사이버범죄 생태계를 교란하기 위한 인프라 중심 접근법을 보여준 점에서 중요한 의의를 가진다.

## Background

Cobalt Strike 는 HelpSystems(현 Fortra)가 개발한 상용 침투 테스트 도구이다. 합법적인 보안 테스트 목적으로 설계되었으나, 크랙·불법 복제된 Cobalt Strike 는 사후 침투 활동, 명령제어(C2) 통신, 랜섬웨어 배포 등에서 사이버범죄자들이 가장 선호하는 도구 가운데 하나로 자리잡았다. Cobalt Strike 의 광범위한 악용은 사이버보안 공동체의 중대한 우려 사안이 되어 왔다.

## Participating Parties

### Lead Agency
- [[uk-nca|영국 국가범죄청(NCA)]]

### Coordinating Body
- [[europol-ec3|Europol EC3(유럽 경찰청 사이버범죄센터)]]

### Participating Agencies
- [[fbi|FBI(미국 연방수사국)]]
- [[australia-afp|호주 연방경찰(AFP)]]
- [[canada-rcmp|RCMP(캐나다 왕립기마경찰)]]
- [[germany-bka|독일 연방범죄수사청(BKA)]]
- [[netherlands-politie|네덜란드 경찰]]
- [[poland-police|폴란드 경찰]]
- [[shadowserver|Shadowserver]] 및 기타 민간 부문 인프라 파트너

### Participating Countries (주도 7개국 + 지원 20개국 = 총 27개국)
주도 참여국:
- [[united-kingdom|영국]]
- [[australia|호주]]
- [[canada|캐나다]]
- [[germany|독일]]
- [[netherlands|네덜란드]]
- [[poland|폴란드]]
- [[united-states|미국]]

추가로 20개국이 ISP 통지를 통해 관여하였다.

## Legal Framework

구체적인 법적 수단은 공개 소스에서 상세히 기술되어 있지 않다. 본 작전은 법집행 및 민간 부문 텔레메트리의 지원을 받아 서비스 사업자들 전반에서 이루어진 통지 및 소탕 활동의 조정으로 가장 잘 문서화된다.

## Operational Timeline

| Date | Event |
|------|-------|
| 2024년 이전 | 범죄적 Cobalt Strike 인프라에 대한 수사 |
| 2024-06-24 ~ 2024-06-28 | 악의적 Cobalt Strike 인스턴스를 표적으로 한 집중 주간 |
| 2024-07-03 | NCA/Europol 대외 발표; 27개국에 걸쳐 593대 서버 제거 |

## Results and Impact

| Metric | Count |
|--------|-------|
| 소탕된 서버 | 593 |
| 표적이 된 악의적 인스턴스 | 690 |
| 관여한 ISP | 129 |
| 관여한 국가 | 27 |
| 주도 참여국 | 7 |
| 침해지표(IoC) | 약 120만 건 |

593대의 Cobalt Strike 서버 소탕은 해당 도구가 범죄 생태계에서 광범위하게 사용된다는 점에 비추어 다수 사이버범죄 집단의 활동을 *likely* 교란하였을 것으로 평가된다.

## Cooperation Mechanisms Used

공개 소스는 민관 협력 인프라 소탕 모델을 묘사한다. 즉 악의적 인스턴스가 식별되고, 법집행 및 벤더 채널을 통해 공유된 후, 집중 주간 동안 호스팅 사업자와 ISP 에 의해 조치되는 방식이다.

## Korean Involvement (한국의 참여)

한국의 관여는 확인되지 않았다. 다만 Cobalt Strike 악용은 글로벌 이슈이며, 한국 기관들도 해당 도구를 이용한 공격의 표적이 되어 왔다.

## Contradictions & Open Questions

- 서버 소탕으로 영향을 받은 범죄 집단은 몇 곳인가?
- 27개의 서로 다른 관할권에서 서버를 소탕한 법적 근거는 무엇이었는가?
- 그중 몇 대의 서버가 이후 범죄자들에 의해 대체되었는가?
- Cobalt Strike 개발사 Fortra 는 본 작전에서 어떤 역할을 하였는가?

## Follow-Up Actions

> [!warning] No public court documents found
> 웹 검색(2026-04-17) 결과 본 작전에 대해 공개적으로 접근 가능한
> 법원 제출 문서는 발견되지 않았다. 가능한 사유: 공개 법원 기록
> 시스템이 없는 비미국 관할권, 봉인된 절차, 또는 작전이 정식
> 기소로 이어지지 않은 경우 등.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- 영국 국가범죄청, 2024-07-03: 영국 국가범죄청이 Cobalt Strike 불법 버전의 약화를 위한 국제 작전을 주도함.
- The Hacker News, 2024-07-03: The Hacker News — 글로벌 경찰 작전으로 600대의 사이버범죄 서버 소탕 (Operation Morpheus).
- UK NCA, 시점 불명: UK NCA — Operation Morpheus (Cobalt Strike 소탕).
- BleepingComputer, 2024-07-03: Europol(유럽 경찰청), 사이버범죄자들이 사용한 593대 Cobalt Strike 서버 소탕.
- TechRadar, 2024-07-03: 대규모 경찰 작전으로 수백 대의 Cobalt Strike 연계 서버 소탕.

## Evidence and Attribution Notes

- 27개국 129개 ISP 에서 690대의 악의적 Cobalt Strike 인스턴스가 표적이 되었으며, 593대가 제거됨.
- 다기관 합동 작전: Europol(유럽 경찰청), FBI(미국 연방수사국), AFP(호주 연방경찰), RCMP(캐나다 왕립기마경찰), 독일 BKA, 네덜란드 Politie, 폴란드 CBZC.
- 2024년 6월 24일부터 시작된 집중 주간 (2024년 7월 3일 발표).
- **Operation Morpheus(모르페우스 작전, Cobalt Strike Europol)** 는 NCA 주도, Europol(유럽 경찰청) 조정으로 진행된 국제 작전으로서, 합법적 침투 테스트 도구이나 사이버범죄자들에 의해 랜섬웨어 공격·간첩·기타 악의적 목적으로 광범위하게 악용되어 온 **Cobalt Strike** 의 무단(불법 복제/크랙) 인스턴스를 표적으로 삼았다.
- 본 작전은 **27개국에 걸친 593대의 Cobalt Strike 서버** 의 소탕이라는 결과로 이어졌다.
- Europol(유럽 경찰청)은 2024년 7월 3일 Operation Morpheus 를 발표하였다: 사이버범죄자들이 사용한 무허가/크랙 Cobalt Strike 레드팀 도구 서버 593대 소탕, 이는 2024년 6월 24일부터 28일까지의 집중 주간 동안 27개국 온라인 서비스 사업자에게 초기 통지된 690개 IP 주소 중 일부에 해당함.
- 주도 기관: 영국 국가범죄청(NCA); 참여 법집행기관: 호주, 캐나다, 독일, 네덜란드, 폴란드, 미국 — Europol(유럽 경찰청) 본부를 통해 조정됨.
- 민간 부문 파트너들이 이례적으로 두드러진 역할을 수행함: BAE Systems Digital Intelligence, Trellix, Shadowserver, Spamhaus, Abuse.ch 가 악의적 Cobalt Strike 인스턴스의 식별 및 보고에 기여하였고, 실시간 위협 인텔리전스 공유를 위해 악성코드 정보공유 플랫폼(MISP) 이 활용됨.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- 영국 국가범죄청, 2024-07-03: National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show submenu for Who we are Our mission Our people Our leadership.
- UK NCA, 2024-07-03: National Crime Agency leads international operation to degrade illegal versions of Cobalt Strike - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show submenu for Who we are Our mission Our people Our leadership.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인 특정 후속 조치가 아닌, 무단 Cobalt Strike 서버를 대상으로 한 인프라 압수 작전을 기술하므로 정본 작전으로 유지된다. 본 기록은 주도 책임을 Uk Nca 에, 조정을 Europol Ec3 에 귀속시키며, 참여 또는 영향 받은 관할권으로 영국, 호주, 캐나다, 독일, 네덜란드, 폴란드, 미국을 기록한다.

협력 모델은 주로 주도/조정 기관 및 국가 목록을 통해 가시화되며, 상세한 법적 메커니즘 항목은 여전히 희소하다.

정본 기록을 위해 포착된 작전 결과: 서버 593대 압수.

정본 소스 셋은 5개의 참고문헌을 포함한다: 2024 06 28 Uk Nca Operation Morpheus Cobalt Strike, The Hacker News Operation Morpheus Cobalt Strike Takedown, Uk Nca Operation Morpheus Cobalt Strike Takedown, 2024 07 03 Bleepingcomputer Com Europol Takes Down 593 Cobalt Strike Servers Used By Cybercriminals, 2024 07 03 Techradar Com Hundreds Of Cobalt Strike Linked Servers Taken Down In Major Police Operation.
정본 작전을 위한 최소 소스 기준은 충족되나, 소스 폭만으로 모든 다운스트림 체포 또는 양형이 본 작전의 일부임을 입증하지는 않는다. 후속 기록은 별도로 연결되어야 한다.
현재 본 페이지에는 frontmatter missing-field 플래그가 부여되어 있지 않다.
데이터셋 활용 측면에서, 본 페이지는 작전 수준의 집계 지점으로 취급되어야 한다. 국가·기관·메커니즘·결과 항목은 조정된 집행 조치 전체를 기술한다. 이후의 기소, 인정, 양형, 인도, 몰수 조치는 별도의 신규 다국적 작전으로 소스가 명시적으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 연결되어야 한다.
소스 기록이 더 폭넓은 배경, 반복적인 통신사 재게재, 또는 토픽 페이지 자료를 포함할 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 그리고 측정 가능한 집행 결과와 직접 연결된 사실에 우선순위를 부여한다. 주변적 소스 제목은 독립적 분류 체계 또는 결과 증거로 취급되지 않는다.
이로써 정본 기록은 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 영국 국가범죄청이 Cobalt Strike 불법 버전의 약화를 위한 국제 작전을 주도함 | UK National Crime Agency | 2024-07-03 | https://www.nationalcrimeagency.gov.uk/news/national-crime-agency-leads-international-operation-to-degrade-illegal-versions-of-cobalt-strike |
| [2] | The Hacker News — 글로벌 경찰 작전으로 600대의 사이버범죄 서버 소탕 (Operation Morpheus) | The Hacker News | 2024-07-03 | https://thehackernews.com/2024/07/global-police-operation-shuts-down-600.html |
| [3] | Europol, 사이버범죄자들이 사용한 593대 Cobalt Strike 서버 소탕 | BleepingComputer | 2024-07-03 | https://www.bleepingcomputer.com/news/security/europol-takes-down-593-cobalt-strike-servers-used-by-cybercriminals/ |
| [4] | 대규모 경찰 작전으로 수백 대의 Cobalt Strike 연계 서버 소탕 | TechRadar | 2024-07-03 | https://www.techradar.com/pro/security/hundreds-of-cobalt-strike-linked-servers-taken-down-in-major-police-operation |
