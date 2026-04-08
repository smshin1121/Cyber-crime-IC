---
type: challenge
title: "Data Sovereignty and Localization Requirements"
title_ko: "데이터 주권 및 현지화 요건"
aliases: ["data localization", "data residency", "data sovereignty"]
challenge_category: "legal"
severity: "critical"
affected_mechanisms:
  - "[[mlat-process]]"
  - "[[cloud-act]]"
  - "[[24-7-network]]"
affected_crime_types:
  - "[[ransomware-ic]]"
  - "[[bec-ic]]"
affected_regions:
  - "EU/EEA"
  - "Asia-Pacific"
  - "Russia/CIS"
  - "China"
  - "India"
  - "South Korea"
proposed_solutions:
  - "CLOUD Act executive agreements"
  - "Budapest Convention Second Additional Protocol direct disclosure (Art. 7)"
  - "Mutual recognition of data protection standards"
  - "Bilateral data-sharing frameworks"
active_debates:
  - "Whether data localization enhances or undermines security"
  - "Balancing privacy rights with law enforcement access"
  - "Extraterritorial reach of national laws (CLOUD Act vs. GDPR)"
related_concepts:
  - "[[territoriality-principle]]"
  - "[[dual-criminality]]"
related_challenges:
  - "[[jurisdictional-conflicts]]"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

Data sovereignty — the principle that data is subject to the laws and governance of the country in which it is collected or stored — is one of the most critical barriers to effective international cooperation on cybercrime. As the vast majority of digital evidence relevant to cybercrime investigations resides with cloud service providers, messaging platforms, and social media companies, the question of *which country's law governs access to that data* has become a central friction point in cross-border investigations.

The challenge is compounded by a global trend toward data localization laws, which require certain categories of data to be stored within national borders. These laws, motivated by privacy protection, national security, and economic interests, can directly impede the cross-border evidence sharing that international cooperation depends upon.

## Nature of the Problem

### Where Is Cloud Data "Located"?

The fundamental difficulty is that the traditional concept of territorial jurisdiction — which underpins the [[territoriality-principle]] — maps poorly onto cloud-stored data. A single user's data may be:

- **Physically stored** in data centers in Country A (or replicated across Countries A, B, and C)
- **Controlled** by a provider headquartered in Country B
- **Owned** by a data subject who is a national of Country C
- **Relevant** to an investigation in Country D

Which country's law governs law enforcement access? The answer depends on the legal framework applied, and different frameworks give different answers:

| Approach | Governing Law | Example |
|----------|--------------|---------|
| Location of data | Where the server is physically located | EU GDPR (partly) |
| Location of provider | Where the company is incorporated/HQ'd | US CLOUD Act |
| Nationality of data subject | Citizenship of the person whose data it is | Some civil law systems |
| Location of investigation | Where the crime is being investigated | MLAT requesting state |

### Data Localization Laws Blocking Cross-Border Access

A growing number of countries have enacted or are considering data localization requirements:

- **Russia** — Federal Law No. 242-FZ (2015): personal data of Russian citizens must be stored on servers within Russia.
- **China** — Cybersecurity Law (2017), Data Security Law (2021), Personal Information Protection Law (2021): critical information infrastructure operators must store data domestically; cross-border transfers require security assessments.
- **India** — Digital Personal Data Protection Act (2023): certain categories of sensitive personal data must be stored in India.
- **Vietnam** — Cybersecurity Law (2018): requires domestic data storage for user data.
- **EU** — While the GDPR does not mandate data localization per se, its restrictions on international data transfers (Chapter V) create a *de facto* localization effect by making cross-border transfers burdensome.

These laws directly impede international cooperation by:
1. Preventing providers from voluntarily disclosing data to foreign law enforcement
2. Creating legal conflicts where a provider is subject to competing obligations (e.g., CLOUD Act compulsion vs. GDPR prohibition)
3. Slowing MLAT processes as requested states must navigate their own data protection requirements

### GDPR vs. Law Enforcement Needs

The EU General Data Protection Regulation (GDPR, Regulation 2016/679) creates a particularly significant tension:

- **Art. 48** prohibits the transfer of personal data to a third country's courts or authorities based on a foreign judgment or decision *unless* authorized by an international agreement (such as an MLAT or a CLOUD Act executive agreement).
- **Art. 49** provides limited derogations but these are narrowly interpreted.
- **Law Enforcement Directive** (Directive 2016/680) governs data processing by competent authorities for law enforcement purposes, with its own transfer restrictions.

The practical effect: a US law enforcement request sent directly to a US-headquartered provider for data relating to an EU data subject may place the provider in an impossible position — comply with the US order and violate GDPR, or comply with GDPR and be held in contempt of the US court.

### Provider Cooperation Complexity

Major cloud and communications service providers (Microsoft, Google, Meta, Apple, Amazon) hold vast quantities of evidence relevant to cybercrime investigations. The legal complexity of responding to foreign government requests is significant:

- Providers must evaluate requests under their *own* country's law, the *requesting* country's law, and potentially the *data subject's* country's law
- Voluntary disclosure (outside of compulsory legal process) is limited by privacy obligations
- Emergency disclosure provisions vary by jurisdiction
- Providers increasingly publish transparency reports, creating pressure from both law enforcement (for more cooperation) and civil society (for more resistance)

## Impact on Cooperation

Data sovereignty barriers affect all stages of cybercrime investigation:

1. **Evidence preservation** — Even the [[24-7-network]] urgent preservation mechanism (Budapest Convention Art. 29) may be complicated when the data is subject to a foreign data protection regime.
2. **Evidence production** — [[mlat-process|MLAT requests]] for data held by foreign providers are the slowest and most cumbersome form of cooperation, often taking 6-18 months.
3. **Direct provider disclosure** — The [[cloud-act|CLOUD Act]] and the [[second-additional-protocol|Second Additional Protocol]] attempt to enable direct requests to providers, but are limited by the number of executive agreements / ratifications in force.
4. **Real-time interception** — Cross-border interception is almost always blocked by data sovereignty concerns.

## Root Causes

### National Sovereignty

Data sovereignty is fundamentally an assertion of national sovereignty in the digital domain. States view control over data within their borders as:
- An extension of territorial sovereignty
- Essential for national security (preventing foreign intelligence access)
- Necessary for effective domestic law enforcement
- A matter of citizen privacy protection

### Privacy Regulation

The global expansion of data protection regulation (GDPR being the most influential model) has created a normative framework that prioritizes individual privacy rights. While legitimate and important, these protections were not designed with cross-border criminal cooperation in mind, and their application to law enforcement data requests creates friction.

### Geopolitical Competition

Data sovereignty has become entangled with broader geopolitical competition:
- **US vs. EU:** CLOUD Act vs. GDPR represents competing visions of data governance
- **US/EU vs. China/Russia:** Fundamentally different approaches to state access to data
- **Global South:** Developing countries view data localization as a tool for digital sovereignty and economic development

## Proposed Solutions

### CLOUD Act Executive Agreements

The US [[cloud-act|CLOUD Act]] (2018) creates a framework for bilateral executive agreements that allow:
- Each country's law enforcement to directly request data from providers in the other country
- Bypassing the MLAT process for qualifying crimes
- Subject to human rights, privacy, and rule of law requirements

**Status:** Only the US-UK agreement is in force (2022). US-Australia agreement signed but not yet in force. US-EU negotiations ongoing.

**Limitation:** Bilateral agreements do not scale well — each new country pair requires separate negotiation.

### Budapest Convention Second Additional Protocol

The [[second-additional-protocol|Second Additional Protocol]] (CETS No. 224, adopted 2022) provides several mechanisms:

- **Art. 7:** Direct disclosure of subscriber information by providers, without MLAT
- **Art. 8:** Giving effect to foreign production orders
- **Art. 14:** Data protection safeguards for all cooperation under the Protocol

**Status:** Not yet in force (requires 5 ratifications by Budapest Convention parties).

**Advantage:** Multilateral framework, potentially more scalable than bilateral CLOUD Act agreements.

### Mutual Recognition of Data Protection Standards

Emerging proposals include:
- EU adequacy decisions under GDPR Art. 45 for law enforcement data transfers
- Minimum data protection standards in international agreements
- Sector-specific arrangements for law enforcement data sharing

## Current State of Debate

The fundamental tension remains unresolved: how to enable effective cross-border law enforcement access to digital evidence while respecting national sovereignty, privacy rights, and data protection. Key positions:

- **Law enforcement perspective:** Current frameworks are too slow and cumbersome; direct access to provider-held data is essential; data localization laws are obstacles to justice.
- **Privacy/civil liberties perspective:** Safeguards against surveillance abuse must not be weakened; mutual legal assistance provides important judicial oversight; direct access risks circumventing domestic protections.
- **Provider perspective:** Legal certainty is needed; conflicting obligations are untenable; clear frameworks like CLOUD Act executive agreements are preferred over ad hoc requests.
- **Developing country perspective:** Data localization may be necessary for sovereignty and economic development; existing frameworks (Budapest Convention) reflect Western priorities.

## Case Studies

### Microsoft Ireland Case (US, 2013-2018)

The landmark *Microsoft Corp. v. United States* (In re Warrant to Search a Certain E-Mail Account, 2nd Cir. 2016) case raised the question of whether a US warrant could compel Microsoft to produce emails stored on a server in Ireland. The Second Circuit held it could not — but the case was mooted by the passage of the CLOUD Act in 2018, which explicitly authorized such compulsion.

### Phobos/8Base Investigation

The [[phobos-8base-crackdown|Phobos/8Base investigation]] (2025) involved 14 countries and required coordinating access to data across multiple jurisdictions. The operation likely relied on a combination of MLATs, [[europol-jit|JIT]] mechanisms, and provider cooperation to access the relevant digital evidence.

## Comparative Perspectives

| Jurisdiction | Approach | Data Localization | LEA Access Framework |
|-------------|----------|-------------------|---------------------|
| United States | Provider-location based | No general requirement | CLOUD Act, SCA, warrants |
| EU/EEA | Data-subject rights focused | De facto (GDPR transfers) | MLAT + e-Evidence Regulation (pending) |
| China | State sovereignty focused | Mandatory (critical data) | Domestic law only; limited MLAT cooperation |
| Russia | State sovereignty focused | Mandatory (personal data) | Domestic law only; minimal cooperation |
| South Korea | Evolving hybrid | Growing (PIPA amendments) | MLAT + Budapest Convention |

## Korean Perspective (한국 관점)

### 개인정보 보호법 (Personal Information Protection Act, PIPA)

Korea's primary data protection law, PIPA (개인정보 보호법), has undergone significant amendments that affect cross-border data transfers:

- **Art. 28-8** (as amended 2023): Cross-border transfer of personal information requires either the data subject's consent, an adequacy determination by the Personal Information Protection Commission (개인정보보호위원회), standard contractual clauses, or certification.
- **Art. 28-9:** Prohibits transfer of personal information to countries that fail to meet adequate protection levels, except in limited circumstances.

These provisions create potential friction when foreign law enforcement agencies request data held by Korean service providers (e.g., Kakao, Naver, Samsung).

### Data Localization Trends

While Korea does not have a comprehensive data localization mandate comparable to Russia or China, sector-specific requirements exist:
- **Financial data:** Financial Services Commission regulations require certain financial data to be stored domestically
- **Healthcare data:** Personal health information has enhanced protection and transfer restrictions
- **Public sector data:** Government cloud policies favor domestic cloud infrastructure

### Impact on Korean LEA Access to Foreign-Held Data

Korean law enforcement agencies face data sovereignty challenges when investigating cybercrime involving data held by foreign providers:

1. **US-based providers (Google, Meta, Apple, Microsoft):** Korean police must typically use the [[mlat-process|MLAT process]] through the Ministry of Justice (법무부) to obtain content data. Subscriber information may be available through voluntary disclosure programs, but this is inconsistent.

2. **No CLOUD Act agreement:** Korea does not currently have a CLOUD Act executive agreement with the United States. Negotiation of such an agreement would likely accelerate Korean access to US-held data but would also require Korea to permit US direct access to Korean-held data.

3. **Budapest Convention accession (2024):** Korea's accession to the Budapest Convention provides a legal basis for cooperation under Art. 29-35, but the Convention's MLA provisions still require going through central authorities. The [[second-additional-protocol|Second Additional Protocol]], when in force, would provide more direct mechanisms.

4. **Korea-specific challenge:** Many Korean cybercrime victims' data is held by Korean platforms (Kakao, Naver), but perpetrators (especially in [[voice-phishing-ic|voice phishing]] and [[bec-ic|BEC]]) operate from abroad. This creates a reverse data sovereignty problem — Korea has the data, but the perpetrators and their infrastructure are in other jurisdictions.

> [!warning] Legal status check needed
> Verify the current status of any Korea-US CLOUD Act executive agreement negotiations (as of 2026).

## Contradictions & Open Questions

- Is data localization ultimately protective or harmful for citizens? Both privacy advocates and law enforcement claim it supports their goals while undermining the other's.
- Can the CLOUD Act bilateral model scale to a meaningful number of countries, or is a multilateral approach (Second Additional Protocol, UN Convention) necessary?
- How will Korea balance its increasingly strict data protection regime (PIPA amendments) with the need for faster cross-border law enforcement data access?
- What happens when data is technically distributed across multiple jurisdictions through cloud replication — which localization law applies?
- Will the UN Cybercrime Convention (when in force) provide a more globally accepted framework for cross-border data access than the Budapest Convention?
