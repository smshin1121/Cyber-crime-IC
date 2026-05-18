## 개요

**Operation Endgame Phase 1**은 2024년 5월 27일부터 29일까지 수행된 **봇넷에 대한 사상 최대 규모의 국제 작전**이다. 본 작전은 랜섬웨어 그룹의 초기 접근 벡터로 기능하는 드로퍼 악성코드 패밀리 — IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot — 를 표적으로 삼았다. 20명 이상의 관계자로 구성된 지휘소를 통해 [[europol-ec3|Europol(유럽 경찰청)]] 본부에서 공조된 본 조치는 4건의 체포, 10개국에 걸친 100대 이상의 서버 테이크다운, 2,000개 이상의 도메인 압수로 이어졌다.

본 작전은 *거의 확실히* 국제 랜섬웨어 집행의 전략적 전환을 대표하였다. 랜섬웨어 운영자를 직접 표적으로 삼는 대신, 처음부터 랜섬웨어 배포를 가능하게 하는 인프라를 타격하였다.

## Background

드로퍼 악성코드("로더" 또는 "초기 접근 브로커"라고도 알려짐)는 랜섬웨어 공격 체인의 1단계를 구성한다. 이 악성코드 패밀리들은 시스템을 감염시킨 후 랜섬웨어 운영자에게 접근 권한을 판매하거나 제공한다. 표적이 된 패밀리 — IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot — 는 BlackBasta, REvil, Conti를 포함한 최소 **15개 랜섬웨어 그룹**과 연결되어 있었다.

드로퍼 생태계를 무력화함으로써 법집행기관은 랜섬웨어 킬 체인을 그 가장 초기 지점에서 차단하고자 하였으며, 이 전략은 [[operation-endgame-phase2|Phase 2]]에서 더욱 두드러지게 된다.

## Participating Parties

### Coordinating Body
- [[europol-ec3|Europol]] — 20명 이상의 관계자로 구성된 본부 지휘소 운영

### Judicial Coordination
- [[eurojust|Eurojust(유럽사법협력기구)]]

### Participating Countries (주요 6개국 + 지원 7개국)
**주요:** 덴마크, 프랑스, 독일, 네덜란드, 영국, 미국
**지원:** 아르메니아, 불가리아, 리투아니아, 포르투갈, 루마니아, 스위스, 우크라이나

### Participating Agencies (15)
[[europol-ec3]], [[eurojust]], [[denmark-police|덴마크 경찰]], [[france-national-police|프랑스 국립경찰]], [[germany-bka|독일 BKA]], [[netherlands-politie|네덜란드 국립경찰]], [[uk-nca|영국 NCA]], [[fbi-cyber-division|FBI]], [[armenia-police|아르메니아 경찰]], [[bulgaria-police|불가리아 경찰]], [[lithuania-police|리투아니아 경찰]], [[portugal-police|포르투갈 경찰]], [[romania-police|루마니아 경찰]], [[switzerland-fedpol|스위스 Fedpol]], [[ukraine-police|우크라이나 경찰]]

## Legal Framework

본 작전에는 13개국의 법집행기관과 사법기관이 참여하였다. 체포는 아르메니아(1건) 및 우크라이나(3건)에서 이루어졌다.

> [!info] Legal-basis note
> 국경 간 집행 조치에 대한 구체적 법적 근거 및 조약 조항은 추가 자료에서 확인되어야 한다.

## Operational Timeline

| 일자 | 사건 |
|------|-------|
| 2024년 이전 | 다국적 수사 단계 |
| 2024-05-27 | 작전 개시 |
| 2024-05-27 ~ 2024-05-29 | 서버 테이크다운, 도메인 압수, 체포 집행 |
| 2024-05-30 | Europol의 공개 발표 |

## Results and Impact

| 항목 | 수치 |
|--------|-------|
| 체포 | 4건(아르메니아 1건, 우크라이나 3건) |
| 위치 수색 | 16건 |
| 테이크다운된 서버 | 100대 이상(10개국에 걸쳐) |
| 압수된 도메인 | 2,000개 이상 |
| 암호화폐(핵심 용의자) | 6,900만 유로 축적 |
| 표적 악성코드 패밀리 | 6 |
| 연결된 랜섬웨어 그룹 | 15개 이상 |

## Cooperation Mechanisms Used

- **Europol 지휘소:** 덴마크, 프랑스, 독일, 미국에서 20명 이상의 관계자로 구성된 Europol 본부 내 현장 공조 센터
- **Eurojust 공조 회의:** 다중 관할 체포영장 및 압수 명령을 위한 사법 공조

## Lessons Learned

1. **공급망 공격:** 드로퍼 악성코드 인프라를 표적으로 삼는 것은 다수의 랜섬웨어 작전을 동시에 무력화하여, 개별 랜섬웨어 그룹을 표적으로 하는 것에 비해 승수 효과를 제공한다.
2. **실시간 공조 센터:** Europol 본부의 20명 이상 관계자 지휘소는 시간대를 초월한 신속한 의사결정과 동기화된 행동을 가능하게 하였다.
3. **규모는 공조를 요구한다:** 10개국에 걸쳐 100대 이상의 서버와 2,000개 이상의 도메인을 동시에 테이크다운하는 것은 Europol과 Eurojust의 전담 제도적 지원 없이는 *거의 확실히* 달성될 수 없는 수준의 공조를 요구한다.

## Follow-Up Actions

> [!warning] 공개 법원 문서 발견되지 않음
> 웹 검색(2026-04-17)을 통해 본 작전에 대한
> 공개적으로 접근 가능한 법원 문서가 확인되지 않았다. 가능한 사유:
> 공개 법원 기록 시스템이 없는 비미국 관할, 비공개 절차, 또는
> 작전이 정식 기소로 이어지지 않음.


- [[operation-endgame-phase2|Operation Endgame Phase 2]] (2025년 5월): 300대의 서버 테이크다운, 650개의 도메인 무력화, 350만 유로 암호화폐 압수, 20건의 국제 체포영장 발부

## Korean Involvement (한국의 참여)

Operation Endgame Phase 1에 대한 한국의 직접적인 참여는 확인되지 않았다.

## Contradictions & Open Questions

- 드로퍼 테이크다운의 직접적 결과로 어떤 구체적 랜섬웨어 그룹이 접근 권한을 상실하였는가?
- 본 작전 이후 랜섬웨어 배포율에 대한 측정 가능한 영향은 무엇이었는가?
- 표적이 된 악성코드 패밀리들은 테이크다운 이후 얼마나 빠르게 재구성되었는가?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2024-05-30: 봇넷에 대한 사상 최대 규모의 작전이 드로퍼 악성코드 생태계를 타격 — Operation Endgame.
- FBI, 2024-05-29: Operation Endgame: 사이버 범죄자 네트워크에 대한 공조 글로벌 법집행 조치.
- 독일 BMI, 2024-05-30: 사이버 범죄에 대한 전 세계적 수사가 성공으로 결실.
- KrebsOnSecurity, 2024-05-30: 'Operation Endgame', 악성코드 배포 플랫폼 타격.
- Europol, 2026-04-17: Operation Endgame — 공식 페이지.

## Evidence and Attribution Notes

- Operation Endgame Phase 1은 봇넷에 대한 사상 최대 규모의 국제 조치로서 2024년 5월 27–29일에 수행됨
- 표적이 된 드로퍼 악성코드 패밀리: IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot
- 4건의 체포(아르메니아 1건, 우크라이나 3건), 10개국에서 100대 이상의 서버 테이크다운, 2,000개 이상의 도메인 압수
- 핵심 용의자는 범죄 인프라 임대로부터 최소 6,900만 유로의 암호화폐를 축적함
- 악성코드 드로퍼는 BlackBasta, REvil, Conti를 포함한 최소 15개 랜섬웨어 그룹과 연결됨
- 2024년 5월 27일과 29일 사이에 **Operation Endgame** — 봇넷에 대한 사상 최대 규모의 국제 조치 — 는 IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot을 포함한 드로퍼 악성코드 패밀리를 표적으로 함.
- 덴마크, 프랑스, 독일, 미국의 20명 이상의 관계자로 구성된 지휘소를 통해 Europol 본부에서 공조된 본 작전은 4건의 체포, 10개국에 걸친 100대 이상의 서버 테이크다운, 2,000개 이상의 도메인 압수로 이어짐.
- 이러한 악성코드 드로퍼는 BlackBasta, REvil, Conti를 포함한 최소 15개 랜섬웨어 그룹과 연결된 초기 접근 벡터의 역할을 함.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2024-05-29: 우크라이나, 포르투갈, 루마니아, 리투아니아, 불가리아, 스위스의 법집행기관은 용의자 체포 또는 면담, 수색 실시, 서버 압수 또는 테이크다운을 위한 경찰 조치를 지원함.
- FBI, 2024-05-29: 2024년 5월 28일부터, 이러한 종류의 첫 공조 국제 작전에 12개국이 참여하여 다수의 악성코드 변종을 무력화하기 위해 수색을 실시하고, 대상자를 심문 또는 체포하며, 100대 이상의 서버를 테이크다운 또는 무력화함.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

본 페이지는 피고인별 후속 조치가 아닌 드로퍼 악성코드 생태계(IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot)에 대한 테이크다운을 기술하므로 정식 작전으로 보존된다. 본 기록은 주된 책임을 Europol EC3에, 공조를 Europol EC3에 귀속시키며, 참여 또는 영향을 받은 관할로는 덴마크, 프랑스, 독일, 네덜란드, 영국, 미국, 아르메니아, 불가리아, 리투아니아, 포르투갈, 루마니아, 스위스, 우크라이나를 기록한다.

공조 모델은 명명된 기관 및 파트너를 통해 문서화된다. Europol EC3, Eurojust, Denmark Police, France National Police, Germany BKA, Netherlands Politie, UK NCA, FBI Cyber Division, Armenia Police, Bulgaria Police. 집행 자세: 체포, 압수, 테이크다운, 자산 동결.

정식 기록에 포착된 작전 결과: 4건의 체포; 100대 서버 압수; 2,000개 도메인 압수; 암호화폐/자산 결과는 6,900만 유로(핵심 용의자가 축적)로 기록; 16건의 위치 수색 수행; 20명 이상의 관계자로 구성된 Europol 본부 지휘소.

정식 자료 집합은 5건의 참조 자료를 포함한다: 2024 05 30 Europol Operation Endgame Botnet Takedown, 2024 05 29 FBI Gov Operation Endgame Coordinated Worldwide Law Enforcement Action Against Network O, 2024 05 30 Bmi Bund De Worldwide Investigation Against Cyber Crime Crowned By Success, 2024 05 30 Krebsonsecurity Com Operation Endgame Hits Malware Delivery Platforms, 2026 04 17 Europol Europa Eu Operation Endgame Official Page.
자료 하한선은 정식 작전에 부합하지만, 자료의 광범위함만으로는 모든 하방 체포 또는 선고가 본 작전의 일부임을 증명하지 못한다. 후속 기록은 별도로 연결된 상태로 유지되어야 한다.
본 페이지에 알려진 메타데이터 공백: Legal Basis 및 Mechanisms Used.
데이터셋 활용 측면에서, 본 페이지는 작전 수준의 통합 기준점으로 다루어져야 한다. 국가, 기관, 메커니즘, 결과 필드는 공조 집행 조치 전체를 기술한다. 이후의 기소, 답변, 선고, 범죄인 인도, 또는 몰수 조치는 자료가 명시적으로 새로운 다국적 작전으로 제시하지 않는 한 관련 사건 또는 흡수된 후속 기록으로 첨부되어야 한다.
자료 기록이 보다 광범위한 배경, 반복된 통신사 재게재, 또는 주제 페이지 자료를 포함하는 경우, 본 평가는 명명된 작전, 그 참여 당국, 표적 인프라 또는 범죄 서비스, 측정 가능한 집행 결과에 직접 연결된 사실에 우선순위를 부여한다. 주변적인 자료 제목은 독립적인 분류 또는 결과 증거로 다루어지지 않는다.
이는 정식 기록이 분석적으로 한정되고 재현 가능한 상태를 유지하도록 한다.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | 제목 | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 봇넷에 대한 사상 최대 규모의 작전이 드로퍼 악성코드 생태계를 타격 — Operation Endgame | Europol | 2024-05-30 | https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem |
| [2] | Operation Endgame: 사이버 범죄자 네트워크에 대한 공조 글로벌 법집행 조치 | FBI | 2024-05-29 | https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals |
| [3] | 사이버 범죄에 대한 전 세계적 수사가 성공으로 결실 | German BMI | 2024-05-30 | https://www.bmi.bund.de/SharedDocs/kurzmeldungen/EN/2024/05/endgame.html |
| [4] | 'Operation Endgame', 악성코드 배포 플랫폼 타격 | KrebsOnSecurity | 2024-05-30 | https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/ |
| [5] | Operation Endgame — 공식 페이지 | Europol | 2026-04-17 | https://www.europol.europa.eu/operations-services-and-innovation/operations/operation-endgame |
