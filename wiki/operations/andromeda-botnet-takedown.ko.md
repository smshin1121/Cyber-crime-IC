## 개요

Andromeda/Gamarue 테이크다운은 Europol(유럽 경찰청)과 FBI(미국 연방수사국)의 조정, 독일과 벨라루스의 법집행 행동, 그리고 Microsoft가 지원한 싱크홀(sinkhole) 지원을 결합하여 2017년 말 장기 운영되어 온 악성코드 생태계를 와해시킨 작전이다.

## 본 작전의 의의

Andromeda는 단일 체포 사건보다는 생태계 와해 작전으로 이해하는 것이 더 적절하다. 공개 자료는 그 기술적 규모를 강조한다.

- Andromeda는 설치 수익화 및 후속 페이로드 전달에 사용되는 범죄형 서비스(crimeware service)로서 수년간 활성 상태를 유지해 왔다

## 참여 당사자

**핵심 기관:**
- [[fbi]]
- [[europol-ec3|Europol EC3]]
- 독일 Lueneburg 소재 수사관
- [[eurojust]]
- [[microsoft]]

**공개적으로 확인된 참여국:**
미국, 독일, 오스트리아, 벨기에, 핀란드, 프랑스, 이탈리아, 네덜란드, 폴란드, 스페인, 영국, 호주, 벨라루스, 캐나다, 몬테네그로, 싱가포르, 대만.

## 결과

- 벨라루스에서 1명의 공개 발표된 체포
- 1,500개의 악성 도메인 싱크홀(sinkhole) 처리

## 협력 및 법적 분석

본 작전은 사이버 테이크다운/단속이 기술적 프레이밍과 법적 프레이밍을 모두 필요로 하는 이유를 잘 보여주는 사례이다. Europol의 보도자료는 법집행 측 개요를 제공하고, Microsoft의 자료는 민간 부문의 와해 역할을 보완한다. 이는 중요한 의미를 갖는데, Andromeda는 단순한 웹사이트나 마켓플레이스가 아니라 지속적인 악성코드 설치 생태계였기 때문에, 영속적인 작전 효과를 위해서는 기술적 복원 및 싱크홀 조정이 필수적이었다.

또한 본 페이지는 형사절차적 측면을 과장하지 않는다. 공개 자료는 테이크다운과 1건의 체포를 명확히 뒷받침하지만, 풍부한 공개 법원 기록 흔적을 드러내지 않는다. 그러한 이유로 본 저장소는 Andromeda를 주로 다국적 와해 작전(multinational disruption operation)으로 다루되, 기록이 충실한 기소 사건으로 다루지는 않는다.

## 후속 조치

> [!warning] No public court documents found
> 공개 자료는 테이크다운 서사를 강하게 뒷받침하지만, 본 저장소는 현재 해당 작전에 부합하는 견고한 공개 법원 문서 세트를 보유하고 있지 않다.

<!-- SOURCE_ENRICHMENT_START -->

## 소스 커버리지

- Europol, 2017년 12월 4일: Andromeda Botnet Dismantled in International Cyber Operation.
- Microsoft, 2017년 12월 4일: Microsoft assists law enforcement to help disrupt the Andromeda botnet.
- Microsoft, 2026년 4월 18일: Gamarue threat profile.
- BleepingComputer, 2017년 12월 4일: Andromeda Botnet Gets Crushed.
- PortSwigger (The Daily Swig), 2017년 12월 5일: PortSwigger Daily Swig: Andromeda Botnet Dismantled by International Taskforce.

## 작전 타임라인

- 2017-11-29: 활동 또는 수사 개시.
- 2017-12-04: 공식 발표.
- 2017-12-04: 보고된 법집행 종료 시점.
- 2017-12-04: BleepingComputer, Europol, Microsoft의 공개 소스 보도.
- 2017-12-05: PortSwigger (The Daily Swig)의 공개 소스 보도.
- 2026-04-18: Microsoft의 공개 소스 보도.

## 증거 및 귀속 관련 주석

- 2017년 11월 말에서 12월 초에 걸쳐, 국제 법집행 작전이 Andromeda 봇넷 인프라를 해체하였다.
- FBI(미국 연방수사국), Luneburg 소재 독일 중앙형사수사청, Europol(유럽 경찰청) 산하 유럽사이버범죄센터(EC3), 사이버범죄공동대응팀(J-CAT), 그리고 Eurojust(유럽사법협력기구)가 Microsoft 등 민간 부문 파트너를 포함한 17개국과 함께 봇넷 무력화를 위한 공조를 진행하였다.
- 본 작전은 Andromeda 악성코드 패밀리를 통한 악성코드 배포에 사용된 서버와 도메인을 와해시켰다.
- Microsoft는 디지털범죄대응팀(Digital Crimes Unit)과 보안팀이 조정된 박멸 캠페인을 통해 Gamarue/Andromeda 와해 작업에서 법집행기관 및 파트너를 지원했다고 밝히고 있다.
- 본 게시물은 2017년 다국적 작전 배후의 민간 부문 싱크홀 및 기술 지원 역할을 설명하는 데 도움이 된다.
- Microsoft의 게시물은 Andromeda 테이크다운에 민간 부문 와해 관점을 더한다.
- 이는 공공 부문 법집행 행동을 보완한 싱크홀 및 조정된 악성코드 박멸 지원의 귀속을 분석하는 데 유용하다.
- Andromeda/Gamarue 테이크다운은 Europol과 FBI의 조정, 독일과 벨라루스의 법집행 행동, 그리고 Microsoft가 지원한 싱크홀 지원을 결합하여 2017년 말 장기 운영되어 온 악성코드 생태계를 와해시켰다.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## 표준(Canonical) 작전 평가

본 페이지는 피고인 특정 후속 조치가 아닌 Andromeda Botnet에 대한 테이크다운/단속을 기술하므로 표준 작전(canonical operation)으로 유지된다. 본 기록은 주도 책임을 FBI(미국 연방수사국)에 귀속시키고 조정 역할을 Europol EC3에 부여하며, 참여 또는 영향을 받은 관할권으로는 미국, 독일, 오스트리아, 벨기에, 핀란드, 프랑스, 이탈리아, 네덜란드, 폴란드, 스페인, 영국, 호주, 벨라루스, 캐나다, 몬테네그로, 싱가포르, 대만이 기록되어 있다.

협력 모델은 명명된 기관 및 파트너(Fbi, Europol Ec3, J Cat, Eurojust, German Bka, Microsoft), 메커니즘(싱크홀(Sinkholing) 및 비공식 협력), 법집행 자세(체포, 압수, 테이크다운/단속)를 통해 문서화되어 있다.

표준 기록에 포착된 작전 결과: 체포 1건; 도메인 압수 1,500건; 48시간 싱크홀(sinkhole) 시간대 동안 약 200만 개의 피해자 IP 주소 관측; 장기에 걸친 박멸 캠페인 이후 Andromeda/Gamarue 인프라 와해.

표준 소스 세트는 5개의 참조 자료를 포함한다: 2017 12 04 Europol Europa Eu Andromeda Botnet Dismantled In International Cyber Operation, 2017 12 04 Microsoft Com Microsoft Assists Law Enforcement Help Disrupt Andromeda Botnet, 2026 04 18 Microsoft Com Gamarue Threat Profile, 2017 12 04 Bleepingcomputer Com Andromeda Botnet Gets Crushed, Portswigger 911 S5 Botnet Dismantling.
표준 작전을 위한 소스 최저 기준은 충족되지만, 소스의 폭이 그 자체로 모든 하류 체포 또는 양형이 본 작전의 일부임을 입증하지는 않는다. 후속 기록은 별도로 연결되어 유지되어야 한다.
현재 본 페이지에 표시된 frontmatter 누락 필드 플래그는 없다.
데이터셋 활용 측면에서, 본 페이지는 작전 수준의 집계 지점으로 다루어져야 한다: 국가, 기관, 메커니즘 및 결과 필드는 조정된 법집행 행동 전체를 기술한다. 이후 기소, 답변 협상(plea), 양형, 범죄인 인도, 또는 몰수 조치는 관련 사건(related case)으로 첨부되거나 흡수된 후속 기록으로 다루어져야 하며, 소스가 이를 새로운 다국적 작전으로 명시적으로 제시하지 않는 한 별도로 처리되지 않는다.
소스 기록이 더 광범위한 배경, 반복되는 통신사 재게재, 또는 토픽 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 참여 기관, 대상 인프라 또는 범죄 서비스, 그리고 측정 가능한 법집행 결과와 직접 연결된 사실을 우선시한다. 주변적인 소스 제목은 독립적인 분류 체계 또는 결과 증거로 다루어지지 않는다.
이렇게 함으로써 표준 기록이 분석적으로 한정되고 재현 가능한 상태로 유지된다.

<!-- CANONICAL_ASSESSMENT_END -->

## 참고문헌

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 국제 사이버 작전을 통한 Andromeda 봇넷 해체 | Europol | 2017-12-04 | https://www.europol.europa.eu/media-press/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation |
| [2] | Microsoft, Andromeda 봇넷 와해를 위해 법집행기관 지원 | Microsoft | 2017-12-04 | https://www.microsoft.com/en-us/msrc/blog/2018/01/microsoft-teams-up-with-law-enforcement-and-other-partners-to-disrupt-gamarue-andromeda |
| [3] | Gamarue 위협 프로파일 | Microsoft | 2026-04-18 | https://www.microsoft.com/en-us/corporate-responsibility/topics/cybersecurity/ |
| [4] | Andromeda 봇넷, 분쇄되다 | BleepingComputer | 2017-12-04 | https://www.bleepingcomputer.com/news/security/andromeda-botnet-gets-crushed-in-eu-us-law-enforcement-operation/ |
| [5] | PortSwigger Daily Swig: 국제 태스크포스에 의해 해체된 Andromeda 봇넷 | PortSwigger (The Daily Swig) | 2017-12-05 | https://portswigger.net/daily-swig/andromeda-botnet-dismantled-by-international-taskforce |
