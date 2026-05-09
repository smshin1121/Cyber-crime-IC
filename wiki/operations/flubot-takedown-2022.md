---
type: operation
title: "FluBot Android-malware takedown — Europol EC3 'day of action' (May–June 2022)"
aliases:
  - "FluBot takedown 2022"
  - "FluBot day of action"
  - "Operation FluBot"
case_id: CYB-2022-FLUBOT
period: 2
operation_role: standalone
parent_operation: ""
operation_type: takedown
status: completed
enforcement_type:
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2022-06-01
  start: 2021
  end: 2022-05
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
  - "[[banking-trojan-ic]]"
  - "[[bank-fraud-ic]]"
target_entity: "FluBot Android-banking-malware ecosystem (SMS-propagated banking trojan and the supporting infrastructure used to control infected devices)"
lead_agency: "[[netherlands-politie]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[australia]]"
  - "[[belgium]]"
  - "[[finland]]"
  - "[[hungary]]"
  - "[[ireland]]"
  - "[[netherlands]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[switzerland]]"
  - "[[united-states]]"
jurisdictions:
  - "[[australia]]"
  - "[[belgium]]"
  - "[[finland]]"
  - "[[hungary]]"
  - "[[ireland]]"
  - "[[netherlands]]"
  - "[[romania]]"
  - "[[spain]]"
  - "[[sweden]]"
  - "[[switzerland]]"
  - "[[united-states]]"
participating_agencies:
  - "[[netherlands-politie]]"
  - "[[europol-ec3]]"
  - "[[switzerland-fedpol]]"
  - "[[australia-afp]]"
  - "[[belgium-federal-police]]"
  - "[[finland-nbi]]"
  - "[[ireland-garda]]"
  - "[[romania-police]]"
  - "[[sweden-police]]"
  - "[[spanish-national-police]]"
  - "[[us-secret-service]]"
organizations:
  - "[[europol-ec3]]"
  - "[[netherlands-politie]]"
  - "[[switzerland-fedpol]]"
  - "[[australia-afp]]"
  - "[[belgium-federal-police]]"
  - "[[finland-nbi]]"
  - "[[ireland-garda]]"
  - "[[romania-police]]"
  - "[[sweden-police]]"
  - "[[spanish-national-police]]"
  - "[[us-secret-service]]"
mechanisms_used:
  - "[[j-cat]]"
  - "[[sinkholing]]"
  - "[[public-private-cooperation]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Swiss preliminary investigations under the leadership of the Office of the Attorney General of Switzerland (Bundesanwaltschaft); Article 147 Swiss Criminal Code (computer fraud) typology applies to the underlying victim losses"
  - "Europol EC3 operational coordination mandate; J-CAT (Joint Cybercrime Action Taskforce) hosted at Europol"
  - "National cybercrime statutes of the eleven participating jurisdictions"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 10000
  other:
    - "FluBot infrastructure destroyed and the malware strain rendered inactive by Dutch Police (Politie) in May 2022."
    - "10,000 victims of the malware disconnected from the FluBot network during the Dutch raid (per Dutch Police; cited via Europol-aligned reporting)."
    - "International coordination via Europol EC3 'day of action' with eleven cooperating LE jurisdictions; virtual command post hosted by Europol."
    - "Investigations to identify the suspected perpetrators were continuing as of the June 2022 announcement; no arrests reported by either fedpol or Europol on the announcement day."
credibility_index: 4.4
source_tier: 1
missing_fields:
  - "specific count of FluBot C2 servers seized (technical-detail, not enumerated in the tier-1 releases)"
  - "domain seizures count (not enumerated in the tier-1 releases)"
  - "identity / count / nationality of suspected perpetrators (investigations still ongoing as of 2022-06-07)"
related_cases: []
related_operations: []
challenges_encountered:
  - "Identifying perpetrators behind a globally-distributed SMS-propagated Android banking trojan despite successful disruption of infrastructure"
  - "Bypass of mobile-banking two-factor authentication through real-time credential capture and SMS interception"
  - "Cross-border viral propagation: a single infected device's contact list seeded the next wave of SMS lures"
lessons_learned:
  - "Coordinated multi-jurisdictional 'day of action' is effective for taking down active SMS-propagated banking-trojan infrastructure even where attribution remains incomplete."
  - "National-CERT and private-sector partnerships (NCSC, telecommunications providers, digitalisation service providers such as Switch) are essential for collecting Swiss-side victim and modus-operandi data that feeds international action."
  - "Europol EC3 'virtual command post' on the takedown day provides real-time coordination across eleven LE jurisdictions in different time zones."
source_count: 2
sources:
  - "[[2022-06-07_fedpol_flubot-android-malware-takedown]]"
summary: "An international Europol EC3-coordinated 'day of action' in May–June 2022 took down the FluBot SMS-propagated Android banking-malware ecosystem. Eleven LE jurisdictions cooperated: Australia, Belgium, Finland, Hungary, Ireland, Netherlands, Romania, Spain, Sweden, Switzerland, and the United States, with named agencies for each. The Dutch Police (Politie) destroyed the FluBot infrastructure in May 2022, deactivating the malware strain; Switzerland (fedpol under OAG leadership) participated as operational and strategic partner. The 7 June 2022 fedpol/OAG press release on the Swiss federal news portal and the parallel 1 June 2022 Europol release jointly document the operation."
created: 2026-05-10
updated: 2026-05-10
---

# FluBot Android-malware takedown — Europol EC3 "day of action" (May–June 2022)

> [!info] Provisional record
> This page rests on two tier-1 publishers (fedpol/OAG primary 2022-06-07 + Europol parallel 2022-06-01). Both name eleven cooperating LE jurisdictions and the underlying technical action. It is below the preferred 5-source threshold (`source_count = 2`) and is filed as a provisional structural record. It will be promoted when additional national-LE primary releases (Politie, AFP, US Secret Service, Polisen, etc.) are individually ingested.

## Summary

In May 2022, the **[[netherlands-politie|Dutch Police (Politie)]]** destroyed the **FluBot** Android banking-malware infrastructure and deactivated the malware strain, on the final phase of an international "day of action" coordinated by **[[europol-ec3|Europol's European Cybercrime Centre (EC3)]]**. **Eleven law-enforcement jurisdictions** participated, with named agencies for each. **[[switzerland-fedpol|fedpol]]** participated under the leadership of the **Office of the Attorney General of Switzerland (OAG / Bundesanwaltschaft)**, in close cooperation with the Swiss [[switzerland-ncsc|NCSC]], cantonal police forces, telecommunications providers and the digitalisation service provider Switch. The fedpol/OAG announcement was issued on **7 June 2022**; the parallel Europol announcement on **1 June 2022**.

FluBot was an aggressive Android-targeting banking trojan first spotted in December 2020, propagated via SMS messages disguised as parcel-tracking or voice-mail notifications. Once installed, it stole banking-app credentials, cryptocurrency-account credentials and SMS one-time codes, and disabled built-in security mechanisms. It self-propagated through each infected phone's contact list, "spreading like wildfire."

## Background

Per the **fedpol** release of 7 June 2022:

> "At the end of May, a large-scale operation led by Europol and the Dutch police and involving other law enforcement authorities succeeded in stopping the rapid spread of a type of malware known as «FluBot». The malware, which infects mobile phones with the Android operating system via text messages, such as those sent by SMS, has also caused considerable damage in Switzerland."

Per the parallel **Europol** release of 1 June 2022:

> "This technical achievement follows a complex investigation involving law enforcement authorities of Australia, Belgium, Finland, Hungary, Ireland, Spain, Sweden, Switzerland, the Netherlands and the United States, with the coordination of international activity carried out by Europol's European Cybercrime Centre (EC3)."

(Romania is named in the Europol release's per-country agency table — Romanian Police / Poliția Română — as a cooperating LE jurisdiction in addition to the ten countries enumerated in the body lead paragraph; the eleventh participating country is therefore Romania.)

## Participating Parties

| Country | Named LE agency (per Europol tier-1 release) | Wikilink |
|---|---|---|
| Australia | Australian Federal Police | [[australia-afp]] |
| Belgium | Federal Police (Federale Politie / Police Fédérale) | [[belgium-federal-police]] |
| Finland | National Bureau of Investigation (Poliisi) | [[finland-nbi]] |
| Hungary | National Bureau of Investigation (Nemzeti Nyomozó Iroda) | (no canonical wiki page; prose only) |
| Ireland | An Garda Síochána | [[ireland-garda]] |
| Netherlands | National Police (Politie) | [[netherlands-politie]] |
| Romania | Romanian Police (Poliția Română) | [[romania-police]] |
| Spain | National Police (Policia Nacional) | [[spanish-national-police]] |
| Sweden | Swedish Police Authority (Polisen) | [[sweden-police]] |
| Switzerland | Federal Office of Police (fedpol) | [[switzerland-fedpol]] |
| United States | United States Secret Service | [[us-secret-service]] |
| Coordination | European Cybercrime Centre (EC3); J-CAT hosted at Europol | [[europol-ec3]] |
| Swiss judicial leadership | Office of the Attorney General of Switzerland (OAG / Bundesanwaltschaft) | (prose only) |
| Swiss-side partners | National Cybersecurity Centre ([[switzerland-ncsc|NCSC]]); cantonal police forces; telecommunications providers; Switch | [[switzerland-ncsc]] |

> [!note] Hungarian National Investigation Bureau (Nemzeti Nyomozó Iroda) does not currently have a dedicated wiki organization page. It is retained in prose. The country wikilink [[hungary]] reflects Hungary as a participating LE jurisdiction.

## Legal Framework

- Swiss preliminary investigations were conducted under the leadership of the **Office of the Attorney General of Switzerland (Bundesanwaltschaft)**, in line with the typology of computer fraud (*betrügerischer Missbrauch einer Datenverarbeitungsanlage*) under Article 147 of the Swiss Criminal Code as applicable to victim losses.
- International coordination took place under **[[europol-ec3|Europol EC3]]'s** operational mandate; the **[[j-cat|J-CAT]]** hosted at Europol supported the investigation.
- National cybercrime statutes of the eleven participating jurisdictions provided the underlying legal basis for each country's investigative measures.

## Operational Timeline

- **December 2020:** FluBot first spotted (per Europol).
- **2021:** FluBot gains traction and compromises a "huge number" of devices worldwide, with significant incidents in Spain and Finland (per Europol).
- **End of May 2022:** Dutch Police (Politie) destroy the FluBot infrastructure and deactivate the malware strain on the Europol-coordinated "day of action."
- **1 June 2022:** Europol issues press release announcing the takedown and naming the eleven cooperating LE jurisdictions.
- **7 June 2022:** fedpol and the Office of the Attorney General of Switzerland issue parallel press release on the Swiss federal news portal, confirming Switzerland's operational and strategic participation.

## Results and Impact

- **FluBot infrastructure destroyed** and the malware strain deactivated by the Dutch Police on the day of action.
- **10,000 victims disconnected** from the FluBot network during the Dutch raid (per Dutch Police; cited in Europol-aligned reporting).
- **Investigations to identify perpetrators continuing** as of June 2022. No arrests were reported by either tier-1 release at announcement.
- **Eleven-jurisdiction LE cooperation** delivered through Europol EC3's virtual command post on the day of takedown.

## Cooperation Mechanisms Used

- **Europol EC3 'day of action' coordination**, with virtual command post on the takedown day.
- **[[j-cat|J-CAT (Joint Cybercrime Action Taskforce)]]** hosted at Europol.
- **National-LE-to-Europol bilateral channels** for each of the eleven jurisdictions (e.g., fedpol coordinated international information exchange in particular with Europol on the Swiss side).
- **National-CERT and private-sector partnerships** (Switzerland: NCSC, telecommunications providers, Switch).

## Challenges and Friction Points

- **Attribution gap.** Investigators succeeded in disrupting FluBot infrastructure but were still working to identify the suspected perpetrators at the time of the June 2022 announcement.
- **Mobile 2FA bypass.** FluBot defeated SMS-based two-factor authentication by capturing victim credentials and SMS codes in real time after persuading users to grant accessibility permissions.
- **Viral SMS propagation.** Each infected phone's contact list seeded further SMS lures, requiring rapid telecommunications-provider cooperation to interrupt the propagation cycle.

## Lessons Learned

- Coordinated multi-jurisdictional "day of action" is effective for taking down active SMS-propagated banking-trojan infrastructure even where perpetrator attribution remains incomplete on the takedown day.
- National-CERT and telecommunications-provider partnerships (Switzerland: NCSC + Switch + telcos) are essential for collecting victim and modus-operandi data that feeds international action.
- Europol's "virtual command post" model enables real-time coordination across eleven LE jurisdictions in different time zones.

## Follow-Up Actions

- Per the fedpol release, "investigations aimed at identifying the suspected perpetrators are still ongoing." Follow-up Swiss criminal proceedings continued under the OAG.
- Public-warning publications (NCSC, telecommunications providers) on Android SMS-propagated banking trojans remained active in 2022 onward.

## Korean Involvement (한국의 참여)

No Korean LE involvement is reported in the FluBot takedown. The case is filed in the wiki as a comparative reference for SMS-propagated Android-banking-trojan response models, of relevance for Korean cybercrime cooperation discussions on smishing-driven banking malware (smishing 사이버범죄, 안드로이드 뱅킹 트로이) where similar national-CERT-plus-LE-plus-telco models are operationally analogous.

## Contradictions & Open Questions

- The fedpol primary release identifies "eleven countries" and explicitly names Europol, the Dutch police, fedpol, OAG, NCSC, Swiss cantonal police, telecommunications providers and Switch. The eleven national-LE agencies by name appear in the parallel Europol release. Cross-citation is therefore: fedpol primary for Swiss-side participation; Europol primary for the eleven-jurisdiction roster.
- The body of the Europol release names ten countries in lead paragraphs and the per-country agency table includes Romania as the eleventh; this is the per-country agency-table reading carried in the present record.
- Specific server / domain seizure counts and perpetrator identities are **not** enumerated in either tier-1 release on the announcement day. This page does not assert numbers that the tier-1 sources do not give.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Cybercrime: Aggressive malware, which targeted Android phones, successfully eliminated thanks to international cooperation involving the Swiss law enforcement authorities and other partners | Federal Office of Police (fedpol) / Office of the Attorney General of Switzerland (OAG) | 2022-06-07 | https://www.news.admin.ch/en/nsb?id=89145 |
| [2] | Takedown of SMS-based FluBot spyware infecting Android phones | Europol | 2022-06-01 | https://www.europol.europa.eu/media-press/newsroom/news/takedown-of-sms-based-flubot-spyware-infecting-android-phones |
