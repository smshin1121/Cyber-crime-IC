---
type: source
title: "Fahndung nach Kopf der Ransomware-Gruppierung „Black Basta" (Public manhunt for the head of the Black Basta ransomware group)"
raw_path: raw/press-releases/2026-01-15_bka-de_fahndung-nach-kopf-der-ransomware-gruppierung-black-basta.md
source_url: https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2026/Presse2026/260115_PM_Black_Basta.html
source_type: press-release
publisher: "Bundeskriminalamt (BKA) — German Federal Criminal Police Office"
author: ""
publish_date: 2026-01-15
ingest_date: 2026-05-10
language: de
reliability: high
credibility: confirmed
sensitivity: public
pages_updated:
  - "[[de-ua-ch-nl-uk-black-basta-ransomware-takedown-2026]]"
key_findings:
  - "On 2026-01-15 the Generalstaatsanwaltschaft Frankfurt am Main — Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT) — and the Bundeskriminalamt (BKA) announced that they have issued a public arrest warrant for the alleged ringleader of the Black Basta ransomware group, identified as a Russian citizen, with previous activity allegedly as a Conti business partner."
  - "The action was internationally coordinated with the Dutch National High Tech Crime Unit (NHTCU), the Swiss Federal Office of Police (fedpol) and Swiss Federal Prosecutor's Office (Bundesanwaltschaft, BA), and the British South East Regional Organised Crime Unit (SEROCU); the Ukrainian Cyber Police (part of the National Police of Ukraine) and the Office of the Prosecutor General of Ukraine independently executed searches against suspected Ukrainian Black Basta members in the Ivano-Frankivsk and Lviv regions, seizing evidence."
  - "Two Ukrainian residences searched in this action wave; suspects accused of hash-cracking activity supporting Black Basta intrusion tradecraft. An earlier action wave (late August 2025) had searched a residence near Kharkiv at ZIT/BKA's request, targeting a suspected crypter."
  - "Black Basta is described as responsible (March 2022–February 2025) for extorting more than 100 entities in Germany and approximately 600 additional organizations worldwide, with proceeds in the three-digit millions of euros (over EUR 20 million from Germany alone)."
  - "Public manhunt is supported by Europol and Interpol via eumostwanted.eu and BKA's Öffentlichkeitsfahndung 69 entry."
created: 2026-05-10
---

## Source Summary

Tier-1 German-language press release from the [[germany-bka|Bundeskriminalamt (BKA)]] announcing (2026-01-15) the issuance of a public arrest warrant for the alleged ringleader of the **Black Basta** [[ransomware-ic|ransomware]] group, framed as the public phase of an internationally coordinated investigation conducted jointly by the [[germany-frankfurt-prosecutor|Frankfurt am Main Public Prosecutor General's Office — Central Office for Combating Internet Crime (ZIT)]] and BKA together with named law-enforcement and prosecutorial counterparts from [[netherlands|the Netherlands]] ([[dutch-nhtcu|NHTCU]]), [[switzerland|Switzerland]] ([[switzerland-fedpol|fedpol]] and the federal Bundesanwaltschaft), [[united-kingdom|the United Kingdom]] (SEROCU), and [[ukraine|Ukraine]] ([[ukraine-police|National Police of Ukraine — Cyber Police]] and the Office of the Prosecutor General of Ukraine).

## International Cooperation Elements

- **Cooperating jurisdictions explicitly named in the source**: Germany, Netherlands, Switzerland, Ukraine, United Kingdom (5 distinct LE/prosecutorial jurisdictions).
- **Cooperating LE/prosecutor agencies named on-source**:
  - Germany: [[germany-frankfurt-prosecutor|Generalstaatsanwaltschaft Frankfurt am Main — ZIT]]; [[germany-bka|Bundeskriminalamt (BKA)]].
  - Netherlands: [[dutch-nhtcu|National High Tech Crime Unit (NHTCU)]].
  - Switzerland: [[switzerland-fedpol|Bundesamt für Polizei (fedpol)]]; Bundesanwaltschaft (federal Office of the Attorney General, BA).
  - Ukraine: [[ukraine-police|National Police of Ukraine — Cyber Police (Cyberpolizei)]]; Office of the Prosecutor General of Ukraine.
  - United Kingdom: South East Regional Organised Crime Unit (SEROCU).
- **Coordinating bodies**: [[europol-ec3|Europol]] and [[interpol|Interpol]] support the public manhunt (eumostwanted.eu, BKA Öffentlichkeitsfahndung 69).
- **Adversary state (NOT counted as cooperating jurisdiction)**: the alleged ringleader is a Russian citizen; the Russian Federation is not named as a cooperating LE jurisdiction.
- **Action geography**: searches in Ukrainian Ivano-Frankivsk and Lviv regions (this action wave); prior search near Kharkiv at ZIT/BKA's request (Aug 2025 action wave).

## Verification Notes

- Fetched 2026-05-10 via curl_cffi chrome124 → HTTP 200, ~57 KB body. Source returned the full German-language article.
- Date "Datum: 15. Januar 2026" is on-page editorial timestamp.
- Publisher is BKA's official press portal (bka.de).
- The release explicitly enumerates the cooperating agencies (text: "Den Maßnahmen vorangegangen waren gemeinsame, international koordinierte Ermittlungen der Generalstaatsanwaltschaft Frankfurt am Main – Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT) – des Bundeskriminalamtes (BKA), des Schweizer Bundesamts für Polizei (fedpol), der Schweizer Bundesanwaltschaft (BA), der niederländischen National High Tech Crime Unit (NHTCU) und der britischen South East Regional Organised Crime Unit (SEROCU) sowie eigenständige Ermittlungen der ukrainischen Nationalpolizei in Kiew und Charkiw und der ukrainischen Generalstaatsanwaltschaft.").
- L24 strict: ≥2 distinct cooperating LE/prosecutor agencies named. Yes — five distinct jurisdictions; Russia (the suspect's nationality) is correctly treated as adversary state and excluded from `participating_countries`.
