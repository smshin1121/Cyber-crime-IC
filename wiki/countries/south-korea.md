---
type: country
title: "Republic of Korea (South Korea)"
iso_code: "KR"
legal_system: "civil-law"
region: "east-asia"
cybercrime_legislation:
  primary_law: "정보통신망 이용촉진 및 정보보호 등에 관한 법률 (Information and Communications Network Act)"
  primary_law_date: "2001-01-16"
  procedural_powers:
    - "search-and-seizure"
    - "production-order"
    - "preservation-order"
    - "interception"
    - "real-time-collection"
  data_retention: "통신사실확인자료 12개월 (통신비밀보호법)"
treaty_memberships:
  - framework: "[[budapest-convention]]"
    status: "party"
    date: "2024"
    reservations: []
  - framework: "[[second-additional-protocol]]"
    status: "under-review"
    date: ""
    reservations: []
central_authority:
  mlat: "법무부 국제형사과 (Ministry of Justice, International Criminal Affairs Division)"
  budapest: "법무부 국제형사과"
key_agencies:
  - "[[knpa-cyber-bureau]]"
  - "[[spo-international-cooperation]]"
  - "[[kisa]]"
ic_capacity:
  rating: "high"
  digital_forensics: "high"
  24_7_availability: true
  english_proficiency: "medium"
  avg_mlat_response_days: "60-120"
bilateral_agreements: []
operations_participated:
  - "[[phobos-8base-crackdown]]"
  - "[[operation-haechi-v]]"
  - "[[korea-china-voice-phishing-qingdao]]"
  - "[[operation-haechi-iv]]"
  - "[[operation-haechi-vi]]"
  - "[[korea-cambodia-scam-repatriation]]"
  - "[[operation-cyber-guardian]]"
notable_cases: []
cooperation_assessment: "Korea is a highly capable cooperation partner with advanced digital forensics capacity and a strong legal framework. Accession to the Budapest Convention in 2024 significantly enhanced Korea's IC legal basis. Primary challenges include language barriers and the multi-step domestic approval process for outgoing MLA requests."
source_count: 7
sources:
  - "[[2025-02-11-europol-phobos-8base-ransomware-arrests]]"
  - "[[2024-12-02-interpol-operation-haechi-v]]"
  - "[[2025-03-05-doj-isoon-chinese-hackers-charges]]"
  - "[[2023-09-08-korea-china-voice-phishing-qingdao]]"
  - "[[2023-12-19-interpol-operation-haechi-iv]]"
  - "[[2025-09-25-interpol-operation-haechi-vi]]"
  - "[[2025-10-18-korea-cambodia-scam-repatriation]]"
created: 2026-04-08
updated: 2026-04-08
---

## Summary

South Korea is a **highly capable** partner for international cooperation on cybercrime, with advanced technological infrastructure, a specialized cyber investigation bureau, and comprehensive cybercrime legislation. Korea's 2024 accession to the [[budapest-convention]] marked a significant milestone, making it the first major East Asian economy to join and providing enhanced legal channels for cross-border cooperation.

## Legal Framework for Cybercrime

### Substantive Criminal Law

**정보통신망 이용촉진 및 정보보호 등에 관한 법률 (Information and Communications Network Act):**
Primary cybercrime statute. Criminalizes:
- Unauthorized access to information and communications networks (Art. 48)
- Distribution of malicious programs (Art. 48-2)
- DDoS attacks / interference with service (Art. 48-3)
- Data breach and personal information violations
- Spam and unsolicited communications

**형법 (Criminal Act):**
- Art. 314: Obstruction of business by interference with computer (컴퓨터등 장애 업무방해)
- Art. 316(2): Violation of secrecy of electronic records
- Art. 347-2: Computer fraud (컴퓨터등 사용사기)

**기타 관련 법률:**
- 전기통신사업법 (Telecommunications Business Act)
- 개인정보 보호법 (Personal Information Protection Act)
- 전자금융거래법 (Electronic Financial Transactions Act)

### Procedural Powers

- **압수·수색 (Search and seizure):** 형사소송법 Art. 106, 107 — includes digital evidence; requires warrant
- **통신제한조치 (Interception):** 통신비밀보호법 — requires court order for real-time interception
- **통신사실확인자료 (Traffic data):** 통신비밀보호법 Art. 13 — court order for subscriber/traffic data
- **보전요청 (Preservation):** Available under 국제형사사법 공조법 framework

### Mutual Legal Assistance

**국제형사사법 공조법 (Act on International Judicial Mutual Assistance in Criminal Matters):**
- Central authority: 법무부 (Ministry of Justice)
- Grounds for refusal: sovereignty, public order, [[dual-criminality]] (discretionary)
- Process: Foreign request → MOJ → Prosecutor's Office → Execution → Return through MOJ

**범죄인 인도법 (Extradition Act):**
- Central authority: 법무부
- Judicial review: 서울고등법원 (Seoul High Court)
- [[dual-criminality]] required (mandatory, 1-year minimum penalty threshold)

## Treaty Memberships

| Framework | Status | Date | Notes |
|-----------|--------|------|-------|
| [[budapest-convention]] | Party | 2024 | First major East Asian accession |
| [[second-additional-protocol]] | Under review | - | Evaluating signature |
| UNTOC (Palermo Convention) | Party | 2000 | MLA provisions for organized cybercrime |
| UNCAC | Party | 2008 | Relevant for cyber-enabled corruption/fraud |
| Korea-US MLAT | In force | 2000 | |
| Korea-China MLAT | In force | 2000 | |
| Korea-Japan judicial assistance | In force | - | Diplomatic channels primarily |

> [!warning] Legal status check needed
> Verify the complete inventory of Korea's bilateral MLATs (believed to be 30+) and exact Budapest Convention accession date with Council of Europe treaty office.

Korea has bilateral MLATs with over **30 countries**, including the United States, China, Australia, Canada, France, United Kingdom, and others.

## Key Agencies and Institutions

### 경찰청 사이버수사국 (KNPA Cyber Investigation Bureau)
See [[knpa-cyber-bureau]] for full profile.
- Established as standalone bureau in **2022** (elevated from 사이버수사과)
- Primary operational agency for cybercrime investigation
- Houses INTERPOL NCB Korea function for cyber matters
- Participates in INTERPOL operations (HAECHI series)

### 법무부 국제형사과 (MOJ International Criminal Affairs Division)
See [[spo-international-cooperation]] for full profile.
- **Central authority** for MLAT requests and extradition
- Processes incoming and outgoing MLA requests
- Coordinates with prosecutors for execution

### 대검찰청 (Supreme Prosecutors' Office)
- Executes MLA requests operationally
- International Cooperation Center coordinates with MOJ
- Specialized cyber prosecution units

### KISA (한국인터넷진흥원)
See [[kisa]] for full profile.
- Technical capacity: CERT/CC, incident response
- Supports investigations with technical analysis
- International cooperation on incident response (FIRST membership)

## Cooperation Track Record

### As Requesting State
Korea actively sends MLA requests, particularly to the US (where major tech companies are headquartered) and China (geographic proximity, cross-border fraud schemes). Key patterns:
- Voice phishing (보이스피싱) investigations requiring Chinese cooperation
- Online fraud cases requiring data from US-based platforms
- Cryptocurrency-related cases requiring multi-jurisdictional cooperation

### As Requested State
Korea is *likely* a responsive cooperation partner with good digital forensics capacity. The multi-step domestic approval process (MOJ → Prosecutors → Court, when needed) can add time but ensures legal compliance.

### Bilateral Relationships
- **Korea-US:** Strongest cyber IC relationship. Active cooperation on North Korea-related cyber operations, ransomware, and financial cybercrime.
- **Korea-China:** Significant MLA volume due to cross-border voice phishing and online gambling operations. Cooperation is *roughly even chance* to be effective, depending on the case type and political climate.
- **Korea-Japan:** Cooperative relationship, primarily through diplomatic channels.

## Capacity Assessment

| Capability | Rating | Notes |
|-----------|--------|-------|
| Digital forensics | High | Advanced labs, trained personnel |
| 24/7 availability | Yes | Budapest Convention Art. 35 contact designated |
| Language capability | Medium | English capability varies; Korean-language requests preferred |
| MLAT response time | 60-120 days | Estimate; faster for urgent matters |
| Technical infrastructure | High | Advanced IT infrastructure supports cooperation |

## Notable Operations and Cases

### INTERPOL HAECHI Series (Korea as Lead)

Korea leads the INTERPOL HAECHI series of operations against cyber-enabled financial crime — *almost certainly* the most significant example of a non-Western country leading a major INTERPOL cybercrime operation series:

| Operation | Year | Countries | Arrests | Seized |
|-----------|------|-----------|---------|--------|
| HAECHI III | 2022 | 30 | 975 | ~$130M | [^haechi3]
| [[operation-haechi-iv|HAECHI IV]] | 2023 | 34 | 3,500 | $300M |

[^haechi3]: > [!warning] Source needed — HAECHI III statistics (975 arrests, ~$130M) are not from a collected source. The HAECHI IV press release references a "260% arrest increase over HAECHI III" but does not provide explicit HAECHI III totals. These figures require verification from an INTERPOL press release for HAECHI III.
| **[[operation-haechi-v|HAECHI V]]** | **2024** | **40** | **5,500+** | **$400M+** |
| [[operation-haechi-vi|HAECHI VI]] | 2025 | 40 | - | $439M |

**[[operation-haechi-iv|Operation HAECHI IV]]** (Jul-Dec 2023): 34 countries, 3,500 arrests, USD 300M seized. 260% arrest increase over HAECHI III. Filipino-Korean cooperation led to Manila arrest. INTERPOL Purple Notices issued for AI voice cloning threats.

**[[operation-haechi-v|Operation HAECHI V]]** (Jul-Nov 2024) set records for the series. Korean and Chinese authorities jointly dismantled a **voice phishing syndicate** responsible for **USD 1.1 billion** in losses affecting **1,900+ victims**. The operation targeted seven types of cyber-enabled fraud across 40 countries.

**[[operation-haechi-vi|Operation HAECHI VI]]** (Apr-Aug 2025): 40 countries, USD 439M recovered (new series record). Korea-UAE sub-operation recovered USD 3.91 million via I-GRIP after a Korean steel company was defrauded through forged shipping documents.

### Europol-Coordinated Operations

- **[[phobos-8base-crackdown|Phobos/8Base Ransomware Crackdown]]** (2019-2025): Europol-coordinated 14-country operation. **Phobos administrator arrested in South Korea (June 2024) and extradited to the US (November 2024).** 4 Russian nationals (8Base leadership) arrested in February 2025. This is *highly likely* the most significant instance of Korean participation in a Europol-coordinated ransomware operation.

### Victim in State-Sponsored Hacking

- **[[isoon-apt27-indictment|i-Soon/APT27 Indictment]]** (2025): South Korea's foreign ministry was among the targets of Chinese contract hackers affiliated with i-Soon and APT27. This case underscores Korea's exposure to state-sponsored cyber espionage from China.

### Voice Phishing Bilateral Operations

Korea conducts significant bilateral enforcement against [[voice-phishing-ic|voice phishing]] (보이스피싱):

- **[[korea-china-voice-phishing-qingdao|Korea-China Qingdao Operation]]** (Aug 2023): First major joint Korea-China voice phishing operation under bilateral agreement. Seoul Metropolitan Police and Qingdao police arrested **16 suspects** for KRW 2.7 billion (USD 2M) in fraud from 68 victims. Established precedent for subsequent joint operations.
- **[[korea-cambodia-scam-repatriation|Korea-Cambodia Scam Centre Repatriation]]** (Oct 2025-Jan 2026): **107+ Korean nationals repatriated** from Cambodia for operating in scam centres conducting voice phishing, romance scams, and pig butchering. An estimated **~1,000 Korean citizens** working in Cambodian scam centres. January 2026 batch: KRW 48.6 billion (USD 33M) in fraud losses. Additional repatriations from Laos, Vietnam, Thailand, Philippines.

The evolution from China-based call centres (Qingdao, 2023) to Southeast Asian scam compounds (Cambodia, 2025) reflects a broader geographic shift in voice phishing infrastructure targeting Korean victims.

### Other

- Dark web marketplace investigations
- Cryptocurrency tracing cooperation with US/EU partners
- ASEANAPOL joint operations

## Political and Diplomatic Context

Korea's accession to the Budapest Convention reflected a strategic decision to align with Western cybercrime cooperation frameworks. This positions Korea as a bridge between the Budapest Convention community and the broader Asia-Pacific region, where Convention membership remains limited.

Korea participated in the UN Cybercrime Convention negotiations, balancing its Budapest commitment with engagement in the broader multilateral process.

## Challenges

- **Language barrier:** Korean-language legal terminology and the need for translation can slow cooperation
- **Domestic process complexity:** Multi-step approval for outgoing MLAs adds time
- **Limited regional treaty coverage:** Few East Asian neighbors are Budapest Convention parties, limiting the Convention's utility for regional cooperation
- **Data localization trends:** Korean data protection law may create friction with certain foreign requests

## Contradictions & Open Questions

- What is Korea's exact 24/7 Network contact point and designated agency?
- What reservations or declarations did Korea make upon Budapest Convention accession?
- What is Korea's average MLAT response time based on empirical data?
- How has Korea's Budapest Convention accession affected the volume/quality of cooperation requests?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Key figures behind Phobos and 8Base ransomware arrested | Europol | 2025-02-11 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown) |
| [2] | INTERPOL financial crime operation makes record 5,500 arrests — Operation HAECHI V | INTERPOL | 2024-12-02 | [원본](https://www.interpol.int/News-and-Events/News/2024/INTERPOL-financial-crime-operation-makes-record-5-500-arrests-seizures-worth-over-USD-400-million) |
| [3] | Justice Department Charges 12 Chinese Contract Hackers — i-Soon/APT27 | US DOJ | 2025-03-05 | [원본](https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-hackers-and-law-enforcement-officers-global) |
| [4] | Seoul Metropolitan Police and Chinese police jointly arrest 16 voice phishing suspects in Qingdao | The Korea Times | 2023-09-08 | [원본](https://www.koreatimes.co.kr/www/nation/2024/07/113_358692.html) |
| [5] | USD 300 million seized and 3,500 suspects arrested — Operation HAECHI IV | INTERPOL | 2023-12-19 | [원본](https://www.interpol.int/News-and-Events/News/2023/USD-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation) |
| [6] | USD 439 million recovered in global financial crime operation — Operation HAECHI VI | INTERPOL | 2025-09-25 | [원본](https://www.interpol.int/en/News-and-Events/News/2025/USD-439-million-recovered-in-global-financial-crime-operation) |
| [7] | South Korea repatriates 64 scam centre suspects from Cambodia | Al Jazeera / Korea Herald | 2025-10-18 | [원본](https://www.aljazeera.com/news/2025/10/20/south-korea-police-seek-warrants-for-repatriated-scam-centre-suspects) |
