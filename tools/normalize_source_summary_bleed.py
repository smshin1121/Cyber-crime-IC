"""Remove copied country-profile summaries from source/case records.

Some source materialization passes copied the South Korea country-profile
paragraph into unrelated source pages and raw archive digests.  This normalizer
keeps the source metadata intact while replacing the generated summaries with
source-specific, conservative text.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BAD_PHRASE = "South Korea is a **highly capable** partner"


SOURCE_FIXES = {
    "2022-01-01_mofa-go-kr_.md": {
        "findings": [
            "Source-title/URL mismatch requiring recrawl: metadata title concerns South Korea's Budapest Convention accession intent, while the captured page text resolves to MOFA North Korean Cyber Threat advisory content.",
            "Use this record for corpus traceability only until the original accession-intent page is re-collected or the URL is corrected.",
        ],
        "summary": (
            "This record has a source-integrity caveat: the metadata title concerns "
            "South Korea's Budapest Convention accession intent, but the captured "
            "MOFA page text is a North Korean cyber threat advisory. Treat this page "
            "as traceability metadata only until the accession-intent source is "
            "recrawled or URL-corrected."
        ),
    },
    "2023-12-19_interpol-int_usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv.md": {
        "findings": [
            "Duplicate source record for INTERPOL's Operation HAECHI IV announcement; canonical page is [[2023-12-19-interpol-operation-haechi-iv]].",
            "The canonical source records 3,500 arrests, USD 300 million seized, and 34 participating countries.",
        ],
        "summary": (
            "Duplicate source record for INTERPOL's Operation HAECHI IV announcement. "
            "Use [[2023-12-19-interpol-operation-haechi-iv]] for substantive findings; "
            "this page preserves metadata and raw-path traceability for the duplicate URL."
        ),
    },
    "2025-01-01_dbpia-co-kr_2-un.md": {
        "findings": [
            "Secondary legal-scholarship source on trends in cybercrime treaties, including the Budapest Convention Second Additional Protocol and the UN cybercrime convention process.",
            "Use as context, not as the controlling status source for treaty signatures, ratifications, or accessions.",
        ],
        "summary": (
            "Secondary legal-scholarship source on cybercrime treaty trends, including "
            "the Budapest Convention Second Additional Protocol and the UN cybercrime "
            "convention process. Use official treaty-office pages for current party "
            "status."
        ),
    },
    "2025-02-11_europol-europa-eu_key-figures-behind-phobos-and-8base-ransomware-arrested.md": {
        "findings": [
            "Duplicate source record for Europol's Phobos/8Base ransomware crackdown announcement; canonical page is [[2025-02-11-europol-phobos-8base-ransomware-arrests]].",
            "The canonical source records four arrests, 27 servers taken down, and a South Korea to United States extradition link for a Phobos administrator.",
        ],
        "summary": (
            "Duplicate source record for Europol's Phobos/8Base ransomware crackdown "
            "announcement. Use [[2025-02-11-europol-phobos-8base-ransomware-arrests]] "
            "for substantive findings; this page preserves duplicate-source traceability."
        ),
    },
    "2025-03-05_justice-gov_justice-department-charges-12-chinese-contract-hackers-i-soon-apt27.md": {
        "findings": [
            "Duplicate source record for the US DOJ i-Soon/APT27 indictment announcement; canonical page is [[2025-03-05-doj-isoon-chinese-hackers-charges]].",
            "Use the canonical source for the charged defendants, affected victims, and international computer-intrusion campaign details.",
        ],
        "summary": (
            "Duplicate source record for the US DOJ i-Soon/APT27 indictment "
            "announcement. Use [[2025-03-05-doj-isoon-chinese-hackers-charges]] "
            "for substantive findings; this page preserves duplicate-source traceability."
        ),
    },
    "2025-10-01_asiae-co-kr_exclusive-ruling-party-proposes-amendment-to-criminal-procedure-act-for-cybercri.md": {
        "findings": [
            "Secondary media report on a proposed Criminal Procedure Act amendment connected to South Korea's Cybercrime Convention accession process.",
            "Use with legislative or government sources before treating the proposal as enacted law.",
        ],
        "summary": (
            "Secondary media report on a proposed Criminal Procedure Act amendment "
            "connected to South Korea's Cybercrime Convention accession process. "
            "Use it as proposal-stage context and confirm enactment against official "
            "legislative or government records."
        ),
    },
    "2025-12-01_korea-kr_2025-12-12-2026-07-01.md": {
        "findings": [
            "Korean government policy-briefing source on Criminal Procedure Act changes intended to support advance preservation of electronic evidence.",
            "Relevant to South Korea's domestic implementation path for Budapest Convention accession, but not proof that accession has been deposited.",
        ],
        "summary": (
            "Korean government policy-briefing source on Criminal Procedure Act changes "
            "for advance preservation of electronic evidence. It supports the domestic "
            "implementation timeline for Budapest Convention accession, but it is not "
            "itself proof that Korea has deposited an accession instrument."
        ),
    },
    "2026-01-01_imnews-imbc-com_10.md": {
        "findings": [
            "Media report on legislation to abolish the Prosecutors' Office and establish successor prosecution and serious-crime investigation bodies in October 2026.",
            "Relevant to future Korean MLAT and cybercrime-investigation counterpart mapping.",
        ],
        "summary": (
            "Media report on legislation to abolish the Prosecutors' Office and "
            "establish successor prosecution and serious-crime investigation bodies "
            "in October 2026. Relevant to future Korean international-cooperation "
            "counterparty mapping."
        ),
    },
    "2026-01-01_m-boannews-com_.md": {
        "findings": [
            "Media report on a Ministry of Science and ICT reorganization that foregrounds information security.",
            "Relevant to Korean cyber governance context, not direct evidence of an enforcement operation.",
        ],
        "summary": (
            "Media report on a Ministry of Science and ICT reorganization that "
            "foregrounds information security. Use for Korean cyber-governance context, "
            "not as direct evidence of an enforcement operation."
        ),
    },
    "2026-01-01_news-tf-co-kr_.md": {
        "findings": [
            "Media report on the proposed or emerging Prosecution Service and Serious Crimes Investigation Agency framework.",
            "Relevant to the October 2026 Korean prosecution/investigation split and future cooperation-counterpart mapping.",
        ],
        "summary": (
            "Media report on the proposed or emerging Prosecution Service and Serious "
            "Crimes Investigation Agency framework. Relevant to the October 2026 "
            "Korean prosecution/investigation split."
        ),
    },
    "2026-01-09_web-archive-org_kisa-ai.md": {
        "findings": [
            "Archived media report on KISA organizational restructuring connected to AI and information-security functions.",
            "Relevant to Korean cyber-capacity context, not direct evidence of an enforcement operation.",
        ],
        "summary": (
            "Archived media report on KISA organizational restructuring connected to "
            "AI and information-security functions. Use for Korean cyber-capacity "
            "context, not as direct evidence of an enforcement operation."
        ),
    },
    "2026-03-21_nwww-newsis-com_78.md": {
        "findings": [
            "Media report on the planned abolition of the Prosecutors' Office and separation of investigation and prosecution functions.",
            "Relevant to Korean institutional-continuity questions for cybercrime cooperation after October 2026.",
        ],
        "summary": (
            "Media report on the planned abolition of the Prosecutors' Office and "
            "separation of investigation and prosecution functions. Relevant to "
            "institutional-continuity questions for Korean cybercrime cooperation "
            "after October 2026."
        ),
    },
    "2026-04-06_newsis-com_3.md": {
        "findings": [
            "Media report on a police reorganization proposal including a cyber-safety bureau.",
            "Relevant to KNPA cybercrime-capacity tracking and future agency mapping.",
        ],
        "summary": (
            "Media report on a police reorganization proposal including a cyber-safety "
            "bureau. Relevant to KNPA cybercrime-capacity tracking and future agency "
            "mapping."
        ),
    },
    "2026-04-17_coe-int_treaty-185-signatures-chart.md": {
        "findings": [
            "Council of Europe Treaty Office chart for the Convention on Cybercrime (ETS No. 185), status as of 25/04/2026.",
            "The chart records 81 ratifications/accessions and 2 signatures not followed by ratification.",
            "Republic of Korea is listed without a ratification/accession date or entry-into-force date and with the note-4 invitation marker; it is therefore not counted as a party in this chart.",
        ],
        "summary": (
            "Council of Europe Treaty Office chart for the [[budapest-convention|"
            "Convention on Cybercrime (ETS No. 185)]], status as of 25/04/2026. "
            "The chart records 81 ratifications/accessions and 2 signatures not "
            "followed by ratification. It lists the Republic of Korea without a "
            "ratification/accession date or entry-into-force date and with the "
            "note-4 invitation marker, so Korea should be treated as invited to "
            "accede, not a party, in current wiki analysis."
        ),
    },
}


def yaml_key_findings(findings: list[str]) -> str:
    lines = ["key_findings:"]
    for finding in findings:
        escaped = finding.replace('"', '\\"')
        lines.append(f'  - "{escaped}"')
    return "\n".join(lines)


def replace_key_findings(text: str, findings: list[str]) -> str:
    replacement = yaml_key_findings(findings)
    pattern = r"key_findings:\n(?:  - .*\n)+(?=collection_url:)"
    if re.search(pattern, text):
        return re.sub(pattern, replacement + "\n", text, count=1)
    return text


def replace_wiki_source_summary(text: str, summary: str) -> str:
    replacement = f"## Source Summary\n\n{summary}\n\n"
    pattern = r"## Source Summary\n\n.*?(?=## Relevance to IC\n)"
    if re.search(pattern, text, flags=re.S):
        return re.sub(pattern, replacement, text, count=1, flags=re.S)
    return text


def replace_raw_summary(text: str, summary: str) -> str:
    replacement = f"## Summary\n\n{summary}\n\n"
    pattern = r"## Summary\n\n.*?(?=## Extracted (?:Text|Summary)\n)"
    if re.search(pattern, text, flags=re.S):
        return re.sub(pattern, replacement, text, count=1, flags=re.S)
    pattern_to_eof = r"## Summary\n\n.*\Z"
    if BAD_PHRASE in text and re.search(pattern_to_eof, text, flags=re.S):
        return re.sub(pattern_to_eof, replacement.rstrip() + "\n", text, count=1, flags=re.S)
    return text


def replace_raw_digest(text: str, findings: list[str], summary: str) -> str:
    findings_text = "\n".join(f"- {finding}" for finding in findings)
    text = re.sub(
        r"### Key Findings\n(?:- .*\n)+",
        f"### Key Findings\n{findings_text}\n",
        text,
        count=1,
    )
    text = re.sub(
        r"### Source Page Summary\n\n.*?(?=## Extraction Notes\n)",
        f"### Source Page Summary\n\n{summary}\n\n",
        text,
        count=1,
        flags=re.S,
    )
    return text


def update_file(path: Path, transform) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = transform(original)
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for filename, fix in SOURCE_FIXES.items():
        wiki_path = ROOT / "wiki" / "sources" / filename
        raw_path = ROOT / "raw" / "press-releases" / filename
        findings = fix["findings"]
        summary = fix["summary"]

        if wiki_path.exists():
            def wiki_transform(text: str) -> str:
                text = replace_key_findings(text, findings)
                return replace_wiki_source_summary(text, summary)

            if update_file(wiki_path, wiki_transform):
                changed.append(str(wiki_path.relative_to(ROOT)))

        if raw_path.exists():
            def raw_transform(text: str) -> str:
                text = replace_raw_summary(text, summary)
                return replace_raw_digest(text, findings, summary)

            if update_file(raw_path, raw_transform):
                changed.append(str(raw_path.relative_to(ROOT)))

    print(f"Normalized {len(changed)} files")
    for path in changed:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
