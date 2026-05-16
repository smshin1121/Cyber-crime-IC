---
source_type: press-release
title: "北朝鮮を背景とするサイバー攻撃グループTraderTraitorによる暗号資産関連事業者を標的としたサイバー攻撃について (Cyberattack by the North Korea-backed cyber attack group TraderTraitor targeting cryptocurrency-related businesses)"
publisher: "National Police Agency of Japan (警察庁 / NPA) — Cyber Affairs Bureau / Kanto Regional Police Bureau / Tokyo Metropolitan Police Department"
publish_date: "2024-12-24"
language: ja
source_url: "https://www.npa.go.jp/bureau/cyber/koho/caution/caution20241224.html"
companion_url_pdf_ja: "https://www.npa.go.jp/bureau/cyber/pdf/020241224_pa.pdf"
companion_url_pdf_en: "https://www.cyber.go.jp/eng/pdf/Alert_TraderTraitor.pdf"
companion_url_fbi: "https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom"
reliability: high
credibility: confirmed
sensitivity: public
ingest_date: 2026-05-17
---

# 北朝鮮を背景とするサイバー攻撃グループTraderTraitorによる暗号資産関連事業者を標的としたサイバー攻撃について

**Publisher**: 警察庁 (National Police Agency of Japan), 関東管区警察局, 警視庁
**Date**: 2024-12-24
**URL (own-domain primary)**: https://www.npa.go.jp/bureau/cyber/koho/caution/caution20241224.html
**Companion documents (own-domain)**:
- Japanese PDF: https://www.npa.go.jp/bureau/cyber/pdf/020241224_pa.pdf
- English PDF: https://www.cyber.go.jp/eng/pdf/Alert_TraderTraitor.pdf
- US partner mirror: https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom

## Key statements (verbatim, English)

> The Federal Bureau of Investigation, Department of Defense Cyber Crime Center, and National Police Agency of Japan alerted the public to the theft of cryptocurrency worth $308 million U.S. dollars from the Japan-based cryptocurrency company DMM by North Korean cyber actors in May 2024.

> The theft is affiliated with TraderTraitor threat activity, which is also tracked as Jade Sleet, UNC4899, and Slow Pisces.

> TraderTraitor activity is often characterized by targeted social engineering directed at multiple employees of the same company simultaneously.

> The FBI, National Police Agency of Japan, and other U.S. government and international partners will continue to expose and combat North Korea's use of illicit activities—including cybercrime and cryptocurrency theft—to generate revenue for the regime.

## Attack chain (NPA/FBI/DC3 joint attribution)

- Late March 2024 — A North Korean cyber actor masquerading as a recruiter on LinkedIn contacted an employee at **Ginco**, a Japan-based enterprise cryptocurrency wallet software company, and sent the target a URL linked to a malicious Python script under the guise of a pre-employment test (GitHub page).
- After mid-May 2024 — TraderTraitor actors exploited session cookie information to impersonate the compromised employee and successfully gained access to Ginco's unencrypted communications system.
- Late May 2024 — Actors manipulated a legitimate transaction request by a DMM employee, resulting in the loss of **4,502.9 BTC ≈ USD 308 million / JPY 48.2 billion (approx. 482 億円)** at time of attack.

## Cooperating agencies (named verbatim in joint advisory)

| Agency | Country | Role |
|---|---|---|
| 警察庁 / National Police Agency (NPA) | Japan | Lead investigator (Japan) — Cyber Affairs Bureau |
| 関東管区警察局 (Kanto Regional Police Bureau) | Japan | Co-investigator |
| 警視庁 (Tokyo Metropolitan Police Department) | Japan | Co-investigator |
| Federal Bureau of Investigation (FBI) | United States | Co-attribution & investigation |
| Department of Defense Cyber Crime Center (DC3) | United States | Co-attribution & technical analysis |
| NISC (内閣サイバーセキュリティセンター) | Japan | Coordination (Japan side) |
| 金融庁 (Financial Services Agency / FSA) | Japan | Sector regulator coordination |

The joint advisory was published simultaneously by the FBI (US-side mirror) and the NPA (Japan-side primary). DMM Bitcoin announced shutdown of operations in December 2024 and asset-transfer to SBI VC Trade as a direct consequence of the loss.

## Threat-actor profile

TraderTraitor is publicly assessed as a subordinate cluster of the **Lazarus Group**, the DPRK-affiliated cyber-attack organization. Other industry-tracked aliases for the same activity cluster: **Jade Sleet, UNC4899, Slow Pisces**.

## IC significance

This is one of the largest cryptocurrency thefts ever attributed publicly by **Japan + United States** in joint name to a specific North Korean threat-actor cluster. The joint advisory closes a public attribution gap that had existed for seven months between the May 2024 incident and the December 2024 attribution.

## Wiki ingest notes

- Pages updated: `[[tradertraitor-dmm-bitcoin-cryptocurrency-theft-joint-attribution-2024]]`
- Crime types: cryptocurrency theft, hacking-IC, money-laundering-IC, social engineering
- Cooperation lever: bilateral US-Japan operational cyber cooperation + 24/7 contact network + joint public attribution
