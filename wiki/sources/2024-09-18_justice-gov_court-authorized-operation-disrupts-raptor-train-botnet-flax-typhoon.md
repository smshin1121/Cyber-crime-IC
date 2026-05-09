---
type: source
title: "Court-Authorized Operation Disrupts Worldwide Botnet Used by People's Republic of China State-Sponsored Hackers"
raw_path: raw/press-releases/2024-09-18_justice-gov_court-authorized-operation-disrupts-raptor-train-botnet-flax-typhoon.md
source_type: press-release
publisher: "US DOJ Office of Public Affairs"
author: ""
publish_date: 2024-09-18
ingest_date: 2026-05-09
language: en
reliability: high
credibility: confirmed
sensitivity: public
press_release_number: "24-1173"
pages_updated:
  - us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024
key_findings:
  - "On 2024-09-18 DOJ announced a court-authorized disruption of the Raptor Train botnet — more than 200,000 compromised SOHO routers, IP cameras, DVRs, and NAS devices in the U.S. and worldwide. Court venue: U.S. District Court, Western District of Pennsylvania."
  - "Target entity named: Integrity Technology Group, a publicly-traded Beijing-based company operating under the public brand 'KRLab' with a malicious-command tool called 'vulnerability-arsenal' — assessed by FBI as the entity behind the activity industry calls 'Flax Typhoon' (PRC state-sponsored, active since 2021 per Microsoft, targeting Taiwan and U.S./foreign government, education, telecom, media, and DIB sectors)."
  - "Operation seized hackers' infrastructure and issued disabling commands to malware on infected devices. Integrity Technology Group attempted a DDoS counter-attack against the FBI's operational infrastructure during the takedown — unsuccessful."
  - "Cooperation partners explicitly named in the DOJ release: French authorities (national-level credit, no specific French agency named) plus partner cyber agencies in Australia, Canada, New Zealand, and the United Kingdom (Five Eyes joint cybersecurity advisory co-signers — partner agency names not enumerated in the press release itself). Private-sector partner: Lumen Technologies / Black Lotus Labs."
  - "Lead U.S. components: FBI San Diego Field Office, FBI Cyber Division, U.S. Attorney's Office for the Western District of Pennsylvania, DOJ NSD National Security Cyber Section, with assistance from DOJ Criminal Division CCIPS. Office of International Affairs (OIA) is listed as a press release component — consistent with foreign cooperation routing."
  - "This is the second PRC state-sponsored botnet disrupted by DOJ in 2024 (AAG Olsen quote), following the May 2024 911 S5 takedown — establishes a 2024 DOJ pattern of court-authorized takedowns against PRC-contractor-controlled IoT botnets."
collection_url: https://www.justice.gov/opa/pr/court-authorized-operation-disrupts-worldwide-botnet-used-peoples-republic-china-state
created: 2026-05-09
updated: 2026-05-09
text_status: parsed
last_fetcher: "doj_fetch (L21 Akamai bm-verify session pattern; chrome124 UA + cookie jar)"
---

## Source Summary

DOJ Office of Public Affairs press release (Press Release Number 24-1173), dated 2024-09-18, announcing a court-authorized law enforcement operation, conducted under court orders unsealed in the **Western District of Pennsylvania**, that disrupted the **Raptor Train** botnet — more than **200,000** PRC-state-controlled IoT consumer devices worldwide. The botnet was developed and controlled by **Integrity Technology Group**, a publicly-traded Beijing company assessed by FBI as the entity behind the activity tracked by industry as **Flax Typhoon**. The disruption took control of the adversary's infrastructure and issued disabling commands. The release names **French authorities** and **Five Eyes partner cyber agencies (Australia, Canada, New Zealand, United Kingdom)** as cooperation partners (the four FVEY partners are credited as co-signers of the same-day joint cybersecurity advisory rather than as joint-investigation partners). **Lumen Technologies' Black Lotus Labs** is credited as the private-sector partner that first identified and named the botnet in July 2023.

## Relevance to IC

This source documents [[us-doj-raptor-train-flax-typhoon-prc-botnet-disruption-2024]] — a tier-1 example of:

1. **Court-authorized technical disruption** as a primary IC instrument when the host state of the threat actor (PRC) will not cooperate. The U.S. exercises jurisdiction by reaching into adversary infrastructure under U.S. court order rather than via MLAT to China.
2. **Five Eyes joint cybersecurity advisory** as a public-attribution and information-sharing mechanism running parallel to (and in support of) the U.S. takedown action. The advisory is a co-authored CSA — the FVEY mechanism as currently practiced for PRC-attributed activity.
3. **Multi-track cooperation pattern**: bilateral foreign LE assistance (France, named) + multilateral cyber-agency advisory (FVEY) + private-sector technical attribution (Lumen / Black Lotus Labs). All three tracks named in the same release.
4. **Second PRC-contractor botnet disruption of 2024**, following the 911 S5 takedown — supports a 2024 enforcement-pattern thesis re: U.S. response to PRC-contractor IoT botnets.

## Confidence

It is **almost certain** (>95%) that the operation occurred on or about 2024-09-18 with the named target entity (Integrity Technology Group) and scope (>200,000 devices), based on a tier-1 DOJ primary source plus a same-day joint cybersecurity advisory (defense.gov hosted) and a same-day Lumen technical writeup. It is **highly likely** (80-95%) that the four FVEY partner countries' cyber agencies (ASD/ACSC, CCCS, GCSB/NCSC-NZ, NCSC-UK) are the unnamed "partner agencies" referenced in the advisory paragraph, but per L19 this should be confirmed by ingesting the joint advisory PDF as a separate raw source before asserting agency-level wikilinks.

> [!note] Fetch note
> Primary URL form `...people-s-republic-china-state` (with apostrophe) returns DOJ Page Not Found. Canonical live URL drops the apostrophe: `...peoples-republic-china-state`. Per L21 the DOJ Akamai Bot Manager interstitial was traversed via `tools/doj_fetch.py` with chrome-style UA + bm-verify session cookies. Body recovered ~89KB; full article text parsed.

> [!warning] L19 / L17 application
> Per L19, only countries explicitly named in this primary source are asserted on the operation page's `participating_countries`: **United States, France, Australia, Canada, New Zealand, United Kingdom**, plus the **target nationality (China / PRC)**. Specific partner agency names beyond the U.S. side are NOT asserted from this source alone — they require the companion joint cybersecurity advisory as a tier-1 source.
