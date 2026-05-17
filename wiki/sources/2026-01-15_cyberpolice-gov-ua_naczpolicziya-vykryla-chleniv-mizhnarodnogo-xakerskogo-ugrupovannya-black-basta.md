---
type: source
title: "Нацполіція викрила членів міжнародного хакерського угруповання та ідентифікувала його організатора (National Police exposes members of international hacker group and identifies its organizer — Black Basta UA searches and Russian ringleader Interpol Red Notice)"
raw_path: raw/press-releases/2026-01-15_cyberpolice-gov-ua_naczpolicziya-vykryla-chleniv-mizhnarodnogo-xakerskogo-ugrupovannya-black-basta.md
source_url: https://cyberpolice.gov.ua/news/naczpolicziya-vykryla-chleniv-mizhnarodnogo-xakerskogo-ugrupovannya-ta-identyfikuvala-jogo-organizatora-6407/
source_type: press-release
publisher: "Cyber Police Department of the National Police of Ukraine (Департамент Кіберполіції Національної поліції України)"
author: ""
publish_date: 2026-01-15
ingest_date: 2026-05-17
language: uk
reliability: high
credibility: confirmed
sensitivity: public
pages_updated:
  - "[[de-ua-ch-nl-uk-black-basta-ransomware-takedown-2026]]"
key_findings:
  - "On 2026-01-15 (16:30 Kyiv local) the Cyber Police Department of the National Police of Ukraine published a tier-1 own-domain release confirming that Cyber Police investigators and the Main Investigation Directorate of the National Police of Ukraine, under the procedural supervision of the Cyber Directorate of the Office of the Prosecutor General of Ukraine, cooperated with the German Bundeskriminalamt (BKA) to terminate the activity of two Ukrainian-citizen members of a Russia-affiliated ransomware group (named Black Basta in the corroborating BKA release of the same date)."
  - "The Ukrainian release explicitly states (verbatim): 'Поточні слідчі дії проводилися в рамках міжнародної співпраці між правоохоронними органами України, Німеччини, Швейцарії, Нідерландів та Великої Британії' — current investigative actions were conducted within international cooperation between the law-enforcement authorities of Ukraine, Germany, Switzerland, the Netherlands, and the United Kingdom. This is the L24-qualifying sentence."
  - "Two suspects acted as so-called 'hash crackers' specializing in password extraction from compromised information systems; searches conducted at residences in the Ivano-Frankivsk and Lviv regions, with seizures of digital storage media and cryptocurrency assets."
  - "The probable organizer of the criminal activity was identified jointly with Europol specialists as a citizen of Russia; on initiative of the German Federal Criminal Police Office and the Frankfurt am Main ZIT Public Prosecutor's Office he was placed on the international wanted list via Interpol channels (corroborated by the BKA 2026-01-15 release issuing the public arrest warrant)."
  - "The release notes prior cooperation: 'Earlier, at the request of foreign partners, Ukrainian police had already conducted searches in Kharkiv and the Kharkiv region and other investigative actions against individual members of this group' — corroborating the August 2025 Kharkiv-area search wave reported by the BKA."
  - "Scope figures (Ukrainian release): from 2022 to 2025 group members attacked hundreds of organizations in various countries with damages in the hundreds of millions of euros — consistent with the BKA release's >100 German victims and ≈600 additional global organizations attribution, three-digit-million-EUR proceeds figure."
created: 2026-05-17
---

## Source Summary

Tier-1 Ukrainian-language own-domain press release from the [[ukraine-police|Cyber Police Department of the National Police of Ukraine]] (cyberpolice.gov.ua), published 2026-01-15 16:30 Kyiv local, corroborating the same-day [[2026-01-15_bka-de_fahndung-nach-kopf-der-ransomware-gruppierung-black-basta|BKA release]] on the Black Basta investigation: two Ukrainian-citizen hash-cracker members searched in Ivano-Frankivsk and Lviv regions; alleged Russian-citizen ringleader publicly wanted via Interpol channels at ZIT/BKA initiative; five named cooperating jurisdictions (Ukraine, Germany, Switzerland, Netherlands, United Kingdom) explicitly listed.

## International Cooperation Elements

- **Cooperating jurisdictions explicitly named in this source**: Ukraine, Germany, Switzerland, the Netherlands, the United Kingdom (5 distinct LE/prosecutorial jurisdictions — matches the BKA tier-1 release on-the-nose).
- **Cooperating LE/prosecutor agencies named on-source**:
  - Ukraine: [[ukraine-police|Cyber Police Department of the National Police of Ukraine]] (Департамент Кіберполіції Національної поліції України); Main Investigation Directorate of the National Police of Ukraine (Головне слідче управління Національної поліції України); Cyber Directorate of the Office of the Prosecutor General of Ukraine (Кіберуправління Офісу Генерального прокурора).
  - Germany: [[germany-bka|Federal Criminal Police Office of Germany (BKA)]]; [[germany-frankfurt-prosecutor|Central Service for Combating Internet Crime of the Frankfurt am Main Public Prosecutor's Office (ZIT)]].
  - Switzerland, Netherlands, United Kingdom: named at the partnership level (no specific agency named in the Ukrainian release; BKA tier-1 release adds [[switzerland-fedpol|fedpol]] + Bundesanwaltschaft (CH), [[dutch-nhtcu|NHTCU]] (NL), and SEROCU (UK)).
- **Coordinating bodies**: [[europol-ec3|Europol]] specialists are explicitly named as participating in identification of the Russian-citizen ringleader; [[interpol|Interpol]] channels carry the international wanted-list publication.
- **Adversary state (NOT counted as cooperating jurisdiction)**: the alleged ringleader is a Russian citizen; the Russian Federation is named as adversary attribution only, not as a cooperating LE jurisdiction. L24-strict treatment per CLAUDE.md.
- **Prior cooperation wave**: explicit reference to earlier Ukrainian police searches in Kharkiv and the Kharkiv region at foreign partners' request — corroborates the BKA's "late August 2025 Kharkiv-area search" timeline.

## Verification Notes

- Fetched 2026-05-17 via curl_cffi chrome124 → HTTP 200, ~34 KB body. Source returned the full Ukrainian-language article.
- Date "15 січня 2026 р. 16:30" is on-page editorial timestamp.
- Publisher is the Cyber Police Department of the National Police of Ukraine, hosted on the cyberpolice.gov.ua official domain — L25-compliant own-domain tier-1 (national police agency, .gov.ua TLD).
- The release names cooperating LE jurisdictions in a single explicit sentence and is therefore L24-qualifying as a stand-alone tier-1.
- This source provides the second tier-1 own-domain corroboration of the same action day, satisfying the iter 194 source_count: 2 enrichment requirement for the [[de-ua-ch-nl-uk-black-basta-ransomware-takedown-2026]] operation page.
- Cross-reference: matches BKA tier-1 release on date (2026-01-15), suspect count (2), action geography (Ivano-Frankivsk + Lviv regions), suspect role (hash-cracking), prior Kharkiv-area search wave, alleged ringleader nationality (Russian citizen), Conti-antecedent attribution, five-country cooperation list, Europol/Interpol coordination role.
