---
type: operation
title: "Germany Flight RCS + Dstat.CC Underground-Economy Takedown — ZIT/HLKA/BKA Hesse-RLP Phase of Operation PowerOff (2024-10-31)"
title_ko: "독일 Flight RCS + Dstat.CC 언더그라운드-이코노미 단속 — ZIT/HLKA/BKA 헤센-라인란트팔츠 단계 (Operation PowerOff, 2024-10-31)"
aliases:
  - "Flight RCS + Dstat.CC takedown"
  - "Hessen-RLP DDoS-as-a-Service + designer-drug marketplace bust 2024"
  - "ZIT-HLKA-BKA Darmstadt-Rhein-Lahn arrest October 2024"
  - "Operation PowerOff Hesse phase 2024-10-31"
case_id: CYB-2024-901
period: 3
operation_role: follow-on
parent_operation: "[[operation-power-off]]"
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2024-11-01
  start: 2024-10-31
  end: 2024-10-31
  ongoing: false
crime_type: "[[ddos-ic]]"
crime_types:
  - "[[ddos-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[drug-trafficking]]"
target_entity: "Two German nationals (ages 19 and 28, residing in Darmstadt and Rhein-Lahn-Kreis) charged as administrators of two cybercrime platforms: (1) Flight RCS — clearnet drug marketplace selling synthetic-cannabinoid designer drug liquids consumed via vape pens or herb mixes; (2) Dstat.CC — DDoS-as-a-Service stresser directory/rating site enabling broad non-technical access to DDoS attacks (used by hacktivist groups such as Killnet). Charge framework includes gewerbs- und bandenmaessiges Betreiben einer kriminellen Handelsplattform (commercial-band operation of a criminal trading platform per StGB Section 127), drug trafficking in significant quantity, and computer sabotage."
lead_agency: "[[zit-frankfurt]]"
coordinating_body: "[[zit-frankfurt]]"
participating_countries:
  - "[[germany]]"
  - "[[france]]"
  - "[[greece]]"
  - "[[iceland]]"
  - "[[united-states]]"
participating_agencies:
  - "[[zit-frankfurt]]"
  - "[[germany-bka]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 2
  indictments: 0
  servers_seized: 0
  domains_seized: 2
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "7 premises searched in Frankfurt am Main, Darmstadt, Rhein-Lahn-Kreis (Rheinland-Pfalz), Rheinisch-Bergischer-Kreis (Nordrhein-Westfalen)"
    - "IT infrastructure of both Flight RCS and Dstat.CC platforms seized"
    - "Per the BKA release, the platform seizures enable follow-on investigations against criminal sellers and users of both platforms"
    - "International cooperation explicitly acknowledged: seizures and assistance in France, Greece, Iceland, United States of America"
edges: []
credibility_index: 4.0
source_tier: 1
missing_fields:
  - foreign_partner_agency_names
related_cases: []
related_operations:
  - "[[operation-power-off]]"
  - "[[operation-power-off-2025-05]]"
  - "[[operation-power-off-2026-04]]"
challenges_encountered: []
lessons_learned:
  - "DDoS-as-a-Service stresser-directory and clearnet drug marketplace can be jointly operated by the same dual administrators — coordinated takedown exploits the operator-overlap to disrupt both crime types in a single action."
  - "The BKA release explicitly names foreign-LE-conducted seizures and assistance in 4 jurisdictions (France, Greece, Iceland, US) but does not enumerate specific foreign agency names; this is a tier-1-source-side recurring limitation in German cybercrime PR style (typical of BKA / ZIT releases which acknowledge international cooperation at the country level but not at the agency level)."
source_count: 1
sources:
  - "[[2024-11-01_bka_hessen-rlp-dstat-flight-rcs-poweroff-festnahmen]]"
created: 2026-05-16
updated: 2026-05-16
---

## Summary

On 2024-10-31 the **Zentralstelle zur Bekaempfung der Internetkriminalitaet (ZIT)** of the Generalstaatsanwaltschaft Frankfurt am Main, jointly with the **Hessisches Landeskriminalamt (HLKA)**, the **Bundeskriminalamt (BKA)**, and **Polizei Nordrhein-Westfalen**, executed two arrest warrants and seized extensive evidence in a coordinated underground-economy takedown across Hesse, Rhineland-Palatinate, and North Rhine-Westphalia. The two German nationals (ages 19 and 28) are charged as administrators of two distinct cybercrime platforms: **Flight RCS** (clearnet designer-drug / synthetic-cannabinoid marketplace) and **Dstat.CC** (DDoS-as-a-Service stresser-directory used by hacktivist groups including Killnet).

The action is framed by the BKA as part of the international [[operation-power-off]] umbrella against DDoS-as-a-Service infrastructure. The press release explicitly acknowledges foreign-LE cooperation: "Im Wege der internationalen Kooperation erfolgten Sicherstellungen und Unterstuetzungen in Frankreich, Griechenland, Island und den Vereinigten Staaten von Amerika." (Through international cooperation, seizures and assistance occurred in France, Greece, Iceland and the United States of America.)

## Background

Dstat.CC operated as a central scene platform comprehensively listing and rating commercial stresser-services, enabling broad non-technical users to easily order DDoS attacks against websites and web-based services. The BKA release notes that DDoS-via-stresser-directory has been increasingly observed in police investigations and used by hacktivist groups including Killnet (highly likely the platform's anonymized user base contained both lone-actor extortion attackers and ideologically motivated hacktivist users). Flight RCS, by contrast, was a clearnet (not darknet) marketplace selling vape-pen liquids and herb-blend products containing synthetic cannabinoids — the BKA release identifies these products as particularly popular among children and adolescents and as a frequent cause of intoxication and medical emergencies.

The dual-administrator overlap — the same two defendants ran both platforms — let German authorities prosecute the DDoS-as-a-Service component (under the Operation PowerOff international frame) and the drug-marketplace component in a single coordinated action.

## Participating Parties

### Germany (lead jurisdiction)
- **Zentralstelle zur Bekaempfung der Internetkriminalitaet (ZIT)** — Generalstaatsanwaltschaft Frankfurt am Main: lead prosecutorial authority ([[zit-frankfurt]])
- **Hessisches Landeskriminalamt (HLKA)** — Hesse state criminal police: lead investigating service for the Flight RCS strand (no canonical wiki org page; recorded in prose)
- **Bundeskriminalamt (BKA)** — Federal Criminal Police Office: lead investigating service for the Dstat.CC strand ([[germany-bka]])
- **Polizei Nordrhein-Westfalen (NRW)** — North Rhine-Westphalia state police: search support in Rheinisch-Bergischer-Kreis (no canonical wiki org page; recorded in prose)

### Foreign cooperating jurisdictions (per BKA release; specific foreign agency names not enumerated in the tier-1 source)
- **France** — seizures and assistance ([[france]])
- **Greece** — seizures and assistance ([[greece]])
- **Iceland** — seizures and assistance ([[iceland]])
- **United States of America** — seizures and assistance ([[united-states]])

## Legal Framework

- **Strafgesetzbuch (StGB) Section 127** — commercial-band operation of a criminal trading platform on the Internet (gewerbs- und bandenmaessiges Betreiben einer kriminellen Handelsplattform im Internet)
- **Betaeubungsmittelgesetz (BtMG)** — drug trafficking in significant quantity (Handel mit Betaeubungsmitteln in nicht geringer Menge), specifically the synthetic-cannabinoid liquids/herb-blend products
- **Computersabotage** — DDoS attacks against websites and web-based services under StGB Section 303b

## Operational Timeline

- **2024-10-31:** HLKA officers execute 2 arrest warrants in Darmstadt + Rhein-Lahn-Kreis; concerted search of 7 premises across Frankfurt am Main, Darmstadt, Rhein-Lahn-Kreis, Rheinisch-Bergischer-Kreis. Foreign-LE-conducted seizures and assistance simultaneously occur in France, Greece, Iceland, and the United States.
- **2024-11-01:** BKA + HLKA + ZIT joint press announcement; defendants scheduled to appear before Haftrichter (custody judge).

## Results and Impact

- **2 arrests** (two administrators of both platforms — same defendants for both Flight RCS and Dstat.CC).
- **2 platforms taken down:** Flight RCS (clearnet drug marketplace) and Dstat.CC (DDoS-as-a-Service stresser directory).
- **IT infrastructure of both platforms seized.**
- **7 premises searched** in Frankfurt am Main, Darmstadt, Rhein-Lahn-Kreis, Rheinisch-Bergischer-Kreis.
- **Foreign-LE seizures and assistance** in France, Greece, Iceland, United States — per the BKA release these foreign-jurisdiction actions are framed as concurrent with the German action and as part of the broader Operation PowerOff international frame.

## Cooperation Mechanisms Used

The BKA release explicitly identifies the framing as part of the **international Operation PowerOff** ([[operation-power-off]]) umbrella against DDoS-as-a-Service infrastructure. Within Operation PowerOff, the typical cooperation toolkit is informal LE-to-LE coordination via Europol EC3 ([[europol-ec3]]) and US DOJ + FBI bilateral channels.

Foreign-LE-conducted seizures in France, Greece, Iceland, and US are explicitly mentioned in the BKA primary source but specific foreign-agency identities, MLAT request references, and bilateral coordination channels are not enumerated at the agency level in the press release. Roughly even chance that the foreign seizures used a combination of EU JIT (Joint Investigation Team) channels (for France within EU) and FBI bilateral coordination (for the US strand); the Iceland strand was likely coordinated bilaterally via INTERPOL or Schengen rapid-response.

## Challenges and Friction Points

- **Tier-1-source agency-naming limitation:** The BKA / ZIT release acknowledges foreign-LE cooperation at the country level ("Frankreich, Griechenland, Island und den Vereinigten Staaten von Amerika") but does not enumerate specific foreign agency names. This is a recurring stylistic limitation in German cybercrime PR (consistent across BKA, ZIT, and HLKA releases over the past 3+ years) and creates a known gap for IC-wiki ingest workflows requiring agency-level explicit attribution.
- **Dual-crime overlap:** Operating both a clearnet drug marketplace and a DDoS-as-a-Service platform required the German prosecutorial team to coordinate two distinct investigative threads (HLKA for Flight RCS, BKA for Dstat.CC) under a single ZIT lead. This is operationally efficient but creates evidentiary segmentation challenges at trial.

## Lessons Learned

1. **DDoS-as-a-Service + clearnet drug-marketplace operator overlap is a real pattern.** Joint takedown of co-operated criminal infrastructure exploits the operator-overlap to disrupt multiple crime types in a single action.
2. **German tier-1 cybercrime PR acknowledges foreign-LE cooperation at the country level, not agency level.** For wiki-ingest workflows requiring strict agency-name attribution, BKA / ZIT / HLKA sources will continue to surface this gap; consider it a structural feature of German LE communications rather than a one-off omission.

## Follow-Up Actions

- Per the BKA release, the seized IT infrastructure and data provide the basis for follow-on investigations against criminal sellers and users of both Flight RCS and Dstat.CC.
- Operation PowerOff continues with follow-on phases including the May 2025 Polish-led DDoS-for-hire takedown ([[operation-power-off-2025-05]]) and the April 2026 PowerOff action week ([[operation-power-off-2026-04]]).

## Korean Involvement (한국의 참여)

No Korean LE involvement is named in the BKA primary source. Almost certainly not directly involved (the 4 named foreign jurisdictions are France, Greece, Iceland, and the United States only).

## Contradictions & Open Questions

- **Foreign agency names not enumerated in the BKA tier-1 source.** Specific foreign-jurisdiction agency identities (e.g., which French gendarmerie / police unit, which Greek cybercrime division, which Icelandic Lögreglan unit, which US FBI field office) are not given in the press release. Wikilinks for foreign cooperating agencies are therefore intentionally omitted from `participating_agencies` (only [[zit-frankfurt]] and [[germany-bka]] are wikilinked) per L23 strict (wikilink-or-empty; no plaintext entity names).
- **Exact criminal-platform metrics** (Flight RCS sale volume, Dstat.CC user count, DDoS attack volume facilitated) are not disclosed in the BKA release; the wiki entry tracks the announced enforcement actions only, not the underlying victimology metrics.
- **Section 127 StGB** is a relatively new German criminal-trading-platform offence (in force since October 2021); its application to a clearnet (not darknet) drug marketplace and to a DDoS-stresser-directory is a notable precedent value that would warrant analysis under existing concept and legal-framework wiki pages if more case data becomes available.
