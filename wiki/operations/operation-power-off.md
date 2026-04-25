---
type: operation
title: "Operation PowerOFF"
aliases:
  - "Power Off"
  - PowerOFF
  - "Operation Power Off"
case_id: CYB-2018-006
period: 1
operation_type: infrastructure-seizure
status: ongoing
enforcement_type:
  - seizure
  - arrest
  - indictment
outcome: success
timeframe:
  announced: 2018-12-19
  start: 2018-12
  end: ""
  ongoing: true
crime_type: "[[ddos-extortion|DDoS-for-Hire]]"
target_entity: "DDoS-for-hire (booter/stresser) service operators and users"
lead_agency: "[[fbi-cyber-division|FBI Cyber Division]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[netherlands]]"
  - "[[germany]]"
  - "[[france]]"
  - "[[poland]]"
  - "[[australia]]"
  - "[[brazil]]"
  - "[[canada]]"
  - "[[finland]]"
  - "[[japan]]"
  - "[[latvia]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[sweden]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[uk-nca|UK NCA]]"
  - "[[netherlands-politie|Dutch National Police]]"
  - "[[germany-bka|BKA]]"
  - "[[australia-afp|AFP]]"
  - "[[canada-rcmp|RCMP]]"
  - "[[japan-npa|Japan NPA]]"
  - "[[us-doj|US DOJ]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention on Cybercrime]]"
  - "US Computer Fraud and Abuse Act (18 U.S.C. SS 1030)"
mechanisms_used:
  - "[[mlat-process|MLAT]]"
results:
  arrests: 16
  indictments: 8
  servers_seized: 0
  domains_seized: 142
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "142+ booter/stresser domains seized across all phases (2018-2024)"
    - "300+ users identified for follow-up in December 2024 phase"
    - "2,000+ warning emails sent to identified users"
    - "250+ formal warning letters issued"
    - "Google/YouTube ad campaigns for deterrence"
edges:
  - source_actor: FBI
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: FBI
    target_actor: "UK NCA"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: "Dutch National Police"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: FBI
    target_actor: "Dutch National Police"
    cooperation_type: info_sharing
    legal_basis: Budapest_Convention
    direction: undirected
credibility_index: 3.8
source_tier: 1
missing_fields:

related_cases:
  - "[[us-v-miller-poweroff]]"
related_operations:
  - "[[ddos-for-hire-sweep-2016|Operation Tarpit (2016)]]"
  - "[[operation-us-v-miller-poweroff]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Sustained, multi-phase operations against DDoS-for-hire are more effective than one-off takedowns; seized domains reappear under new names, requiring persistent enforcement"
  - "Demand-side deterrence (targeting users, not just operators) is essential to shrink the market"
  - "Private sector cooperation (Cloudflare, PayPal, DigitalOcean) is critical for identifying service operators and payment flows"
  - "Timing takedowns before Christmas disrupts the seasonal peak in DDoS attacks against gaming and e-commerce platforms"
source_count: 7
sources:
  - "[[2024-12-11_europol-europa-eu_law-enforcement-shuts-down-27-ddos-booters-ahead-of-annual-christmas-attacks]]"
  - "[[2022-12-14_justice-gov_federal-prosecutors-in-los-angeles-and-alaska-charge-6-defendants]]"
  - "[[2024-09-01_justice-gov_law-enforcement-seizes-9-ddos-for-hire-webpages]]"
  - "[[2023-05-09_bleepingcomputer-com_fbi-seizes-13-more-domains-linked-to-ddos-for-hire-services]]"
  - "[[2024-12-12_cyberscoop-com_international-crackdown-disrupts-ddos-for-hire-operations]]"
  - "[[2026-04-17_en-wikipedia-org_operation-poweroff]]"
  - "[[2024-12-12_theregister-com_operation-poweroff-extinguishes-18-more-ddos-booters]]"
created: 2026-04-10
updated: 2026-04-11
operation_role: umbrella
parent_operation: ""
summary: "Operation PowerOFF is an **ongoing, multi-phase international law enforcement operation** targeting DDoS-for-hire (booter/stresser) services. Launched in December 2018 and still active as of December 2024, it is coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and led operationally by the [[fbi-cyber-division|FBI]], with the [[uk-nca|UK National Crime Agency (NCA)]] as a core partner. The operation has conducted at least six major enforcement waves, seizing over 142 domains, arresting 16 individuals, and identifying hundreds of users across 15 countries."
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[netherlands]]"
  - "[[germany]]"
  - "[[france]]"
  - "[[poland]]"
  - "[[australia]]"
  - "[[brazil]]"
  - "[[canada]]"
  - "[[finland]]"
  - "[[japan]]"
  - "[[latvia]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[sweden]]"
organizations:
  - "[[fbi-cyber-division|FBI Cyber Division]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[uk-nca|UK NCA]]"
  - "[[netherlands-politie|Dutch National Police]]"
  - "[[germany-bka|BKA]]"
  - "[[australia-afp|AFP]]"
  - "[[canada-rcmp|RCMP]]"
  - "[[japan-npa|Japan NPA]]"
  - "[[us-doj|US DOJ]]"
crime_types:
  - "[[ddos-extortion|DDoS-for-Hire]]"
---
## Summary

Operation PowerOFF is an **ongoing, multi-phase international law enforcement operation** targeting DDoS-for-hire (booter/stresser) services. Launched in December 2018 and still active as of December 2024, it is coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and led operationally by the [[fbi-cyber-division|FBI]], with the [[uk-nca|UK National Crime Agency (NCA)]] as a core partner. The operation has conducted at least six major enforcement waves, seizing over 142 domains, arresting 16 individuals, and identifying hundreds of users across 15 countries.

Operation PowerOFF is almost certainly the longest-running and most impactful sustained campaign against the DDoS-for-hire ecosystem. Its distinguishing features include: (1) **supply-side dismantlement** (seizing booter platforms), (2) **demand-side deterrence** (identifying and warning users), and (3) **strategic timing** of takedowns before Christmas to disrupt seasonal attack peaks against gaming and e-commerce targets.

## Background

DDoS-for-hire services -- marketed as "booters" or "stressers" -- allow customers with minimal technical skill to launch distributed denial-of-service attacks against websites, gaming servers, and critical infrastructure for as little as $10-$20. These services lower the barrier to cybercrime participation and are disproportionately used by young offenders (often under 20 years old).

The precursor to Operation PowerOFF was [[ddos-for-hire-sweep-2016|Operation Tarpit]] (December 2016), a 13-country sweep coordinated from Europol EC3 headquarters in The Hague that resulted in 34 arrests and 101 "knock-and-talk" interviews targeting booter service **customers**. Operation Tarpit established the operational template -- Europol-centered coordination with simultaneous multi-country action -- that PowerOFF would formalize and scale.

By 2018, law enforcement recognized that one-off takedowns were insufficient; seized services reappeared under new domain names within weeks. This led to the establishment of Operation PowerOFF as a **persistent, multi-phase campaign** with rolling enforcement waves.

## Participating Parties

**Core Agencies (all phases):**
- [[fbi-cyber-division|FBI Cyber Division]] (United States) -- lead investigative agency
- [[europol-ec3|Europol EC3]] (EU) -- coordination hub, J-CAT facilitation, crypto-tracing
- [[uk-nca|UK National Crime Agency]] (United Kingdom)
- [[netherlands-politie|Dutch National Police Corps]] (Netherlands)

**Agencies participating in later phases (2022-2024):**
- [[germany-bka|Bundeskriminalamt (BKA)]] and Hessian State Criminal Office (Germany)
- Poland Central Cybercrime Bureau
- [[australia-afp|Australian Federal Police (AFP)]]
- Brazil Federal Police
- [[canada-rcmp|RCMP]] (Canada)
- [[japan-npa|Japan National Police Agency]]
- France National Police (OFAC), JUNALCO
- Finland National Police
- Latvia State Police
- Portugal Judiciary Police
- [[romania-police|Romanian Police]]
- Sweden Regional Cybercrime Centre

**Private sector partners:** Cloudflare, PayPal, and DigitalOcean provided technical information and payment data to assist in identifying service operators.

## Legal Framework

- **[[budapest-convention|Budapest Convention on Cybercrime]]** (Articles 2-6 on computer-related offences; Article 29 on expedited preservation of stored data; Articles 31-35 on international cooperation) -- primary multilateral legal basis for cross-border evidence sharing and domain seizure coordination
- **US Computer Fraud and Abuse Act (18 U.S.C. SS 1030)** -- domestic legal basis for US indictments
- **[[mlat-process|Mutual Legal Assistance Treaties (MLATs)]]** -- used for formal evidence exchange between the US and European partners
- National cybercrime legislation of participating countries

## Operational Timeline

### Phase 1: December 2018 -- Initial Takedown
- **Date**: 2018-12-19
- **Domains seized**: 15
- **Arrests**: 3 (United States)
- **Indictments**: 3 defendants charged in US (operating DDoS-for-hire services)
- **Notable**: First use of the "Operation PowerOFF" branding; FBI and Dutch National Police as primary investigators

### Phase 2: December 2022 -- Major Expansion
- **Date**: 2022-12-14
- **Domains seized**: 48
- **Arrests**: 7 (6 US citizens indicted; locations: Florida x3, Texas, Hawaii, New York)
- **Notable services**: "Quantum" (responsible for ~50,000 attacks), plus 47 other booter platforms
- **Countries**: United States, United Kingdom, Germany, Netherlands, Poland
- **Indictments filed**: Central District of California and District of Alaska
- Cloudflare, PayPal, and DigitalOcean assisted with identifying operators

### Phase 3: May 2023 -- Follow-up Seizure
- **Date**: 2023-05-08
- **Domains seized**: 13
- **Note**: 10 of the 13 were reconstituted versions of services seized in December 2022 (e.g., cyberstress.org was the same service as cyberstress.us)
- **Guilty pleas**: Four defendants from the December 2022 phase -- Jeremiah Sam Evans Miller, Angel Manuel Colon Jr., Shamar Shattock, and Cory Anthony Palmer -- pled guilty (linked to RoyalStresser.com, SecurityTeam.io, Astrostress.com, Booter.sx)

### Phase 4: September 2024 -- Targeted Seizure
- **Date**: 2024-09 (exact date unconfirmed)
- **Domains seized**: 9
- **Agencies**: FBI, US Defense Criminal Investigative Service (DCIS)
- **Note**: DCIS involvement reflected growing concern about DDoS attacks targeting military and government networks

### Phase 5: December 2024 -- Largest Single Phase
- **Date**: 2024-12-11
- **Domains seized**: 27 (including zdstresser.net, orbitalstress.net, starkstresser.net)
- **Additional**: 18 booter platforms dismantled at infrastructure level
- **Arrests**: 3 administrators (France, Germany)
- **Users identified**: 300+ for follow-up
- **Countries**: 15 (Australia, Brazil, Canada, Finland, France, Germany, Japan, Latvia, Netherlands, Poland, Portugal, Romania, Sweden, United Kingdom, United States)
- **Deterrence measures**: Google search ads and YouTube campaigns, 250+ warning letters, 2,000+ emails to identified users

## Results and Impact

**Cumulative results across all phases (2018-2024):**

| Metric | Total |
|--------|-------|
| Domains seized | 142+ |
| Arrests | 16+ |
| Defendants indicted/charged | 8+ |
| Countries participating (max) | 15 |
| Guilty pleas secured | 4+ |
| Users identified for follow-up | 300+ (Dec 2024 alone) |

**Qualitative impact:**
- Disrupted the availability of major booter services, particularly during the Christmas DDoS attack season
- Established a persistent enforcement model where reconstituted services are re-seized (as demonstrated in May 2023)
- The demand-side deterrence approach (warning letters, Google ads) likely reduced the user base, though measurement is difficult
- One seized service (Quantum) was linked to approximately 50,000 attacks globally, indicating the scale of disruption

> [!note] Aggregate figures
> Cumulative arrest and seizure figures are compiled from DOJ press releases, Europol announcements, and secondary reporting across multiple phases. Some overlap may exist where reconstituted domains were seized more than once.

## Cooperation Mechanisms Used

1. **Europol EC3 Coordination Hub** -- Europol hosted coordination meetings, organized "technical investigation sprints," provided analysis, crypto-tracing expertise, and forensic assistance
2. **Joint Cybercrime Action Taskforce (J-CAT)** -- Europol's standing operational platform for multi-country cybercrime investigations facilitated information exchange
3. **[[mlat-process|Mutual Legal Assistance Treaties]]** -- Formal evidence exchange between US and European jurisdictions for indictment support
4. **Private sector voluntary cooperation** -- Cloudflare (hosting data), PayPal (payment flows), DigitalOcean (infrastructure intelligence) voluntarily assisted law enforcement
5. **Google Ads deterrence campaign** -- Law enforcement placed advertisements on Google search results for "booter" and "stresser" to warn potential users of legal consequences

## Challenges and Friction Points

- **Domain reconstitution**: Seized services frequently reappeared under new domain names within weeks. The May 2023 phase explicitly targeted 10 reconstituted services from the December 2022 takedown, demonstrating the "whack-a-mole" challenge
- **Cross-jurisdictional hosting**: Booter services use hosting providers across multiple jurisdictions, requiring simultaneous coordination for effective seizure
- **Youth offender dilemma**: Many users are teenagers, raising questions about whether prosecution or diversion/education is more appropriate and effective for deterrence
- **Measurement difficulty**: Quantifying the deterrent effect of takedowns and warning campaigns on the overall DDoS-for-hire market is methodologically challenging

## Lessons Learned

1. **Persistence over one-off actions**: The multi-phase approach demonstrates that sustained campaigns with rolling enforcement waves are more effective than single takedowns against commoditized cybercrime services
2. **Dual supply-and-demand targeting**: Combining infrastructure seizure (supply side) with user identification and warning campaigns (demand side) addresses both ends of the market
3. **Strategic timing**: Scheduling takedowns before Christmas disrupts peak DDoS attack season against gaming and e-commerce platforms
4. **Private sector intelligence is essential**: Payment processors and hosting providers hold critical evidence for identifying operators
5. **Template for commoditized cybercrime**: PowerOFF established a replicable model for sustained campaigns against other "crime-as-a-service" markets

## Korean Involvement (한국의 참여)

There is no confirmed direct Korean participation in any phase of Operation PowerOFF as of December 2024. However, [[japan-npa|Japan's National Police Agency]] participated in the December 2024 phase, indicating growing East Asian engagement. South Korea's booter/stresser market exposure is likely limited compared to the primary English-language market, but DDoS attacks against Korean gaming platforms (a significant target category) mean that future Korean participation is plausible.

## Contradictions & Open Questions

1. **Total domain count discrepancy**: Wikipedia cites "48 websites" for the 2018 phase, but DOJ press releases specify 15 domains in December 2018. The 48 figure likely conflates 2018 and 2022 phases. This page uses the DOJ/Europol primary source figures.
2. **September 2024 details are sparse**: The 9-domain seizure in September 2024 is referenced in DOJ press releases but with limited detail on participating countries beyond the US. Further primary source confirmation is needed.
3. **Effectiveness measurement**: No public data exists on whether the overall volume of DDoS-for-hire activity has decreased in response to PowerOFF, versus simply shifting to more resilient platforms (e.g., Tor-based services).

> [!warning] Legal status check needed
> As an ongoing operation, new phases may occur after the date of this page's last update. Verify current status against Europol and DOJ announcements.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Law enforcement shuts down 27 DDoS booters ahead of annual Christmas attacks | Europol | 2024-12-11 | https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-shuts-down-27-ddos-booters-ahead-of-annual-christmas-attacks |
| [2] | Federal Prosecutors in Los Angeles and Alaska Charge 6 Defendants with Operating Websites that Offered Computer Attack Services | US DOJ | 2022-12-14 | https://www.justice.gov/usao-cdca/pr/federal-prosecutors-los-angeles-and-alaska-charge-6-defendants-operating-websites |
| [3] | Law Enforcement Seizes 9 DDoS-for-Hire Webpages as Part of Global Crackdown on ‘Booter’ and ‘Stresser’ DDoS Services | US DOJ CDCA | 2024-09-01 | https://www.justice.gov/usao-cdca/pr/law-enforcement-seizes-9-ddos-hire-webpages-part-global-crackdown-booter-and-stresser |
| [4] | FBI seizes 13 more domains linked to DDoS-for-hire services | Bleeping Computer | 2023-05-09 | https://www.bleepingcomputer.com/news/security/fbi-seizes-13-more-domains-linked-to-ddos-for-hire-services/ |
| [5] | International crackdown disrupts DDoS-for-hire operations | CyberScoop | 2024-12-12 | https://cyberscoop.com/international-crackdown-disrupts-ddos-for-hire-operations/ |
| [6] | Operation PowerOFF | Wikipedia | 2026-04-17 | https://en.wikipedia.org/wiki/Operation_PowerOFF |
| [7] | Operation PowerOFF extinguishes 18 more DDoS booters | The Register | 2024-12-12 | https://www.theregister.com/2024/12/12/operation_poweroff_ddos_takedowns/ |
