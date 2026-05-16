---
type: operation
title: "Operation Cavern — NZ-Denmark Joint Cyberhacking Investigation (2015)"
title_ko: "오퍼레이션 카번 — 뉴질랜드-덴마크 해킹·사진 유포 합동수사 (2015)"
aliases:
  - "Operation Cavern"
  - "NZ-Denmark cybercrime joint investigation 2015"
  - "Auckland school girl Vejle Denmark hacking case"
case_id: CYB-2015-915
period: 1
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
outcome: success
timeframe:
  announced: 2015-09-16
  start: ""
  end: 2015-09-16
  ongoing: false
crime_type: "[[hacking-ic]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[cyberstalking-ic]]"
target_entity: "Single 24-year-old Danish citizen suspect (unnamed in release), arrested in Vejle, Denmark for online posting of private photos and hacking of private computers under Danish law, with an Auckland (NZ) school girl as the victim."
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[new-zealand]]"
  - "[[denmark]]"
participating_agencies:
  - "[[denmark-police]]"
  - "[[denmark-national-police]]"
organizations:
  - "[[denmark-police]]"
  - "[[denmark-national-police]]"
mechanisms_used:
  - "[[mlat-process]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Bilateral cybercrime cooperation under Danish substantive criminal law; the Danish citizen suspect was prosecuted in Denmark under Danish law (no extradition); NZ Police provided investigative lead and evidence to Danish counterparts."
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 1
  other:
    - "Arrest of 24-year-old Danish citizen in Vejle, Denmark"
    - "Charges brought under Danish law: online posting of private photos; hacking of private computers"
    - "Closed-doors judicial hearing in Denmark at time of release; further case details withheld"
    - "Auckland (NZ) school girl named as victim (identity withheld)"
edges:
  - source_actor: new-zealand
    target_actor: denmark-police
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: new-zealand
    target_actor: denmark-national-police
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
credibility_index: 3.5
source_tier: 1
missing_fields:
  - "suspect_name (withheld at release time due to closed-doors hearing)"
  - "victim_name (withheld - minor protection)"
  - "exact_charges_under_Danish_law (specific articles not enumerated in release)"
  - "indictments (post-arrest charging not enumerated; status of trial outcome unknown from this release)"
  - "monetary_loss"
  - "hacking_methodology (deliberately withheld due to closed-doors hearing)"
related_cases:

related_operations:

challenges_encountered:

lessons_learned:
  - "Operation Cavern is one of the early Asia-Pacific / Northern-European bilateral cybercrime IC datapoints in the wiki corpus — a clean 2-jurisdiction, 3-LE-agency template for the **remote-victim, foreign-perpetrator** cooperation pattern where the suspect is prosecuted in the suspect's home jurisdiction (Denmark) under domestic law rather than extradited to the victim's jurisdiction (New Zealand). NZ Police supplies the investigative lead and evidence; Danish authorities effect the arrest, charge, and prosecution."
  - "The release is structurally distinct from later Europol-coordinated takedowns: no intergovernmental coordinating body is named (no Europol, no Eurojust, no INTERPOL credit), no extradition step is involved (Danish citizen prosecuted in Denmark), and the IC is wholly bilateral between NZ Police and Danish authorities."
  - "The prosecutor-on-the-record verbatim attribution — 'close cooperation,' 'smooth, mutual and fruitful,' 'a country on the other side of the world' — is one of the warmer multi-LE cooperation testimonies in the corpus and is useful as a counterpoint to corpus entries documenting friction in MLAT/MLA cooperation."
source_count: 1
sources:
  - "[[2015-09-16_police-govt-nz_danish-police-arrest-man-cybercrime-new-zealand]]"
summary: "On 2015-09-16, the New Zealand Police announced the arrest in Vejle, Denmark of a 24-year-old Danish citizen as part of **Operation Cavern** — a joint cybercrime investigation between the NZ Police Cybercrime Unit, the Danish National Cyber Crime Centre (NC3), and South-East Jutland Police. The suspect was charged under Danish law with the online posting of private photos and the hacking of private computers, with an Auckland (NZ) school girl as the named victim. Suspect prosecuted in Denmark (no extradition). The release contains explicit verbatim cooperation attribution from Danish prosecutor Niels Tipsmark characterising the bilateral cooperation as 'smooth, mutual and fruitful.' Bilateral NZ-Denmark IC pattern with no Europol/Eurojust/INTERPOL coordinating body named."
created: 2026-05-17
updated: 2026-05-17
---
## Summary

On **Wednesday 16 September 2015**, the New Zealand Police announced the arrest, in **Vejle, Denmark**, of a 24-year-old Danish citizen as part of **Operation Cavern** — a joint cybercrime investigation between three named law-enforcement bodies across two jurisdictions:

- **New Zealand Police** (Cybercrime Unit) — investigation-initiating and victim-jurisdiction LE
- **Danish National Cyber Crime Centre (NC3)** — Denmark's national cybercrime coordination body
- **South-East Jutland Police** — Danish regional police district that effected the arrest

The Danish citizen suspect was charged, under Danish law, with cybercrimes relating to the **online posting of private photos** and the **hacking of private computers**. The named victim is an **Auckland (NZ) school girl**, whose identity is withheld in the release. Further case details — including the suspect's name, the manner of hacking, the nature of the photos, and the specific charges — were deliberately withheld in the press release due to closed-doors judicial proceedings in Denmark at the time of publication.

Operation Cavern is a **bilateral NZ-Denmark** investigation: no intergovernmental coordinating body (Europol, Eurojust, INTERPOL) is named in the release, and the Danish citizen suspect is prosecuted in Denmark under Danish law rather than extradited to New Zealand.

## Background

The operation is one of the early Asia-Pacific / Northern-European bilateral cybercrime IC datapoints in the wiki corpus. The investigation pattern is the **remote-victim, foreign-perpetrator** cooperation model: the victim is domiciled in NZ, the perpetrator is domiciled and operates from Denmark, and the cooperation channel transfers investigative product from NZ to Denmark to enable a domestic Danish prosecution. There is no fugitive-extradition dimension because the suspect is a Danish national prosecuted in his home jurisdiction.

The cited release does not describe how the offending was initially reported to NZ Police, how the suspect was identified, or how NZ Police evidence was transferred to Danish counterparts. The release does not enumerate which Danish criminal-law articles were invoked at charging.

## Participating Parties

| Role | Party |
|---|---|
| Investigation-initiating / victim-jurisdiction LE | [[new-zealand\|New Zealand]] Police (Cybercrime Unit) |
| Suspect-jurisdiction national coordinating LE | [[denmark-police\|Danish National Cyber Crime Centre (NC3)]] |
| Suspect-jurisdiction regional LE (arresting) | South-East Jutland Police (organisationally within [[denmark-national-police\|Denmark National Police]]) |
| Suspect-jurisdiction prosecutor on the record | Niels Tipsmark, prosecutor, South-East Jutland Police |
| NZ spokesperson on the record | Detective Senior Sergeant Cliff Clark, NZ Police Cybercrime Unit |

## Legal Framework

- Substantive law of prosecution: **Danish law** (specific articles not enumerated in the release).
- No extradition step (Danish national prosecuted in Denmark).
- Cooperation legal basis (per release tone): bilateral cybercrime cooperation between NZ Police and Danish authorities; no MLAT instrument explicitly cited in the release, though evidence transfer from NZ to Denmark is implicit.

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| (Pre-2015-09-16) | Joint investigation between NZ Police, NC3, and South-East Jutland Police underway | NZ Police 2015-09-16 |
| 2015-09-16 | Arrest of 24-year-old Danish citizen in Vejle, Denmark; press release published 5:12 pm NZ time | NZ Police 2015-09-16 |
| (Post-2015-09-16) | Closed-doors judicial proceedings in Denmark | NZ Police 2015-09-16 |

## Results and Impact

- **1 arrest** (24-year-old Danish citizen) in Vejle, Denmark.
- **Charges** brought under Danish law: online posting of private photos; hacking of private computers.
- **1 victim** named in release (Auckland school girl, identity withheld).
- **Closed-doors hearing** in Denmark at time of release; outcome of trial not enumerated in the cited release.

## Cooperation Mechanisms Used

The release explicitly characterises the cooperation as a **joint investigation** between three named LE bodies in two jurisdictions, with **mutual evidence-sharing** as the implicit operational mechanism (NZ Police investigative lead → Danish LE effects arrest and prosecution in Denmark). No JIT instrument is named. No intergovernmental coordination body (Europol, Eurojust, INTERPOL) is credited. The cooperation is bilateral.

Verbatim cooperation testimony from Danish prosecutor Niels Tipsmark of South-East Jutland Police:

> "This case is characterized by a close cooperation between South-East Jutland Police, NC3, and the New Zealand Police. The cooperation with a country on the other side of the world has been smooth, mutual and fruitful."

NZ Detective Senior Sergeant Cliff Clark of the NZ Police Cybercrime Unit confirms the operation "demonstrated the value of effective co-operation with overseas law enforcement partners."

## Challenges and Friction Points

The release does not document friction. Tone is positive. Implicit challenges include:

- Time-zone disparity (NZ and Denmark are ~10 hours apart) — Tipsmark's "a country on the other side of the world" comment.
- Closed-doors hearing in Denmark constrains the public IC record — the release is structurally information-limited (no suspect name, no charging details, no methodology).

## Lessons Learned

- The **remote-victim, foreign-perpetrator, prosecute-in-perpetrator-jurisdiction** cooperation model is a distinct IC pattern from the more common **extradite-perpetrator-to-victim-jurisdiction** model. Operation Cavern is a clean template for the former.
- 2-jurisdiction, 3-LE-agency bilateral cooperation can operate without any intergovernmental coordinating body when the IC channels between the two domestic LEs are direct and bilateral. This is more common for non-EU partner pairs (NZ-Denmark in 2015 predates Eurojust's third-state liaison arrangements with NZ).
- The release is one of the warmer multi-LE cooperation testimonies in the corpus and a useful counterpoint to corpus entries documenting MLAT/MLA friction.

## Follow-Up Actions

The release does not enumerate post-arrest follow-ups. The closed-doors nature of Danish proceedings means the trial outcome, sentencing, and any subsequent civil remedies for the NZ victim are not in the public record at the time of the cited release.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited release. The case is recorded in the wiki for its bilateral NZ-Denmark IC pattern, which is structurally distinct from Korean cybercrime IC posture (which is more commonly multilateral via Europol/Eurojust JITs, US DOJ MLATs, or APAC counterpart cooperation).

## Contradictions & Open Questions

- The release does not enumerate the suspect's name, the victim's exact age, the specific Danish criminal-law articles invoked at charging, the manner of hacking, or the nature of the photos. Closed-doors Danish hearing at time of release.
- The release does not document the trial outcome, sentencing, or any subsequent IC follow-ups. The current status of the prosecution (10+ years post-arrest) is not in the cited source.
- The release does not credit any intergovernmental coordinating body. The wiki record assumes pure bilateral NZ-Denmark IC; this should be checked against any follow-up coverage if a later source becomes available.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2015-09-16_police-govt-nz_danish-police-arrest-man-cybercrime-new-zealand\|Danish Police arrest man for cybercrime in New Zealand]] | New Zealand Police | 2015-09-16 | https://www.police.govt.nz/news/release/danish-police-arrest-man-cybercrime-new-zealand |
