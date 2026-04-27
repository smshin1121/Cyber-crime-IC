from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter

from enrich_targeted_content_from_sources import (
    OPS_DIR,
    ROOT,
    clean_text,
    fmt_list,
    split_frontmatter,
    strip_references,
    wikilink_label,
)


START = "<!-- CANONICAL_ASSESSMENT_START -->"
END = "<!-- CANONICAL_ASSESSMENT_END -->"
BLOCK_RE = re.compile(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", re.S)
DEFAULT_DATE = "2026-04-27"


@dataclass(frozen=True)
class Result:
    slug: str
    changed: bool
    source_count: int
    countries: int


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, dict) and not value:
        return []
    if value in (None, ""):
        return []
    return [value]


def is_absorbed(meta: dict[str, Any]) -> bool:
    return str(meta.get("status") or "").strip().lower() == "absorbed"


def count_sources(meta: dict[str, Any]) -> int:
    try:
        return int(meta.get("source_count") or len(as_list(meta.get("sources"))) or 0)
    except Exception:
        return len(as_list(meta.get("sources")))


def result_phrase(meta: dict[str, Any]) -> str:
    results = meta.get("results") if isinstance(meta.get("results"), dict) else {}
    parts: list[str] = []
    labels = {
        "arrests": "arrests",
        "indictments": "indictments",
        "servers_seized": "servers seized",
        "domains_seized": "domains seized",
        "victims_notified": "victims notified",
        "decryption_keys_recovered": "decryption keys recovered",
    }
    for key, label in labels.items():
        value = results.get(key)
        if value not in (None, "", 0, "0"):
            parts.append(f"{value} {label}")
    crypto = results.get("cryptocurrency_seized")
    if crypto:
        parts.append(f"cryptocurrency/asset result recorded as {clean_text(crypto, limit=120)}")
    for item in as_list(results.get("other"))[:4]:
        cleaned = clean_text(item, limit=160)
        if cleaned:
            parts.append(cleaned)
    if not parts:
        return "Public result metrics are limited in the current metadata, so the page should avoid implying a larger operational impact than the sources state."
    return "; ".join(parts[:8]) + "."


def source_phrase(meta: dict[str, Any]) -> str:
    sources = as_list(meta.get("sources"))
    count = count_sources(meta)
    if not sources:
        return "No source list is available in frontmatter; this should be repaired before using the page for quantitative analysis."
    labels = [wikilink_label(source) for source in sources[:6] if wikilink_label(source)]
    label_text = ", ".join(labels)
    if len(sources) > 6:
        label_text += f", plus {len(sources) - 6} more"
    return f"The canonical source set contains {count} reference(s): {label_text}."


def assessment(meta: dict[str, Any]) -> str:
    title = clean_text(meta.get("title"), limit=180)
    operation_type = clean_text(meta.get("operation_type") or "operation", limit=80)
    target = clean_text(meta.get("target_entity") or title, limit=220)
    lead = wikilink_label(meta.get("lead_agency")) or "not specified"
    coordinator = wikilink_label(meta.get("coordinating_body")) or lead
    countries = as_list(meta.get("participating_countries")) or as_list(meta.get("jurisdictions"))
    country_text = fmt_list(countries, limit=18) or "no participating-country list"
    agencies = fmt_list(as_list(meta.get("participating_agencies")), limit=10)
    mechanisms = fmt_list(as_list(meta.get("mechanisms_used")), limit=10)
    enforcement = fmt_list(as_list(meta.get("enforcement_type")), limit=8)
    legal = fmt_list(as_list(meta.get("legal_basis")), limit=8)
    missing = fmt_list(as_list(meta.get("missing_fields")), limit=8)
    source_count = count_sources(meta)

    lines = [
        START,
        "",
        "## Canonical Operation Assessment",
        "",
        (
            f"This page is retained as a canonical operation because it describes a {operation_type} against {target}, "
            f"rather than a defendant-specific follow-on action. The record attributes lead responsibility to {lead} "
            f"and coordination to {coordinator}, with participating or affected jurisdictions recorded as {country_text}."
        ),
        "",
    ]

    cooperation_bits = []
    if agencies:
        cooperation_bits.append(f"named agencies and partners: {agencies}")
    if mechanisms:
        cooperation_bits.append(f"mechanisms: {mechanisms}")
    if legal:
        cooperation_bits.append(f"legal basis: {legal}")
    if enforcement:
        cooperation_bits.append(f"enforcement posture: {enforcement}")
    if cooperation_bits:
        lines.append("The cooperation model is documented through " + "; ".join(cooperation_bits) + ".")
    else:
        lines.append(
            "The cooperation model is visible primarily through the lead/coordinating agencies and country list; detailed legal mechanism fields remain sparse."
        )

    lines.extend(
        [
            "",
            f"Operational results captured for the canonical record: {result_phrase(meta)}",
            "",
            source_phrase(meta),
        ]
    )

    if source_count >= 5:
        lines.append(
            "The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately."
        )
    else:
        lines.append(
            "The source floor is not yet met, so this canonical record should remain in the enrichment queue until additional independent sources are attached."
        )

    if missing:
        lines.append(f"Known metadata gaps still carried by this page: {missing}.")
    else:
        lines.append("No frontmatter missing-field flags are currently carried on this page.")

    lines.append(
        "For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation."
    )
    lines.append(
        "When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence."
    )
    lines.append("This keeps the canonical record analytically bounded and reproducible.")

    lines.extend(["", END])
    return "\n".join(lines) + "\n"


def update_frontmatter_date(fm_text: str, updated_date: str) -> str:
    if re.search(r"(?m)^updated:\s*", fm_text):
        return re.sub(r"(?m)^updated:\s*.*$", f"updated: {updated_date}", fm_text, count=1)
    return fm_text.replace("\n---\n", f"\nupdated: {updated_date}\n---\n", 1)


def enrich_path(path: Path, dry_run: bool, updated_date: str) -> Result | None:
    post = frontmatter.load(path)
    meta = post.metadata
    if is_absorbed(meta):
        return None
    original = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(original)
    pre_refs, refs = strip_references(body)
    pre_refs = BLOCK_RE.sub("\n", pre_refs).rstrip()
    block = assessment(meta)
    new_text = update_frontmatter_date(fm_text, updated_date) + pre_refs.rstrip() + "\n\n" + block
    if refs:
        new_text += "\n" + refs.rstrip() + "\n"
    if not new_text.endswith("\n"):
        new_text += "\n"
    changed = new_text != original
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return Result(path.stem, changed, count_sources(meta), len(as_list(meta.get("participating_countries"))))


def queue_paths(queue: Path | None) -> list[Path]:
    if not queue:
        return [path for path in sorted(OPS_DIR.glob("*.md")) if not path.name.startswith("_")]
    rows = csv.DictReader(queue.open("r", encoding="utf-8", newline=""))
    return [OPS_DIR / f"{row['slug']}.md" for row in rows if row.get("category") == "operations" and row.get("slug")]


def render_report(results: list[Result], dry_run: bool, run_date: str) -> str:
    changed = [result for result in results if result.changed]
    lines = [
        "---",
        f"title: Canonical Operation Assessment Enrichment ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Execution report for adding canonical-operation assessment blocks to non-absorbed operation pages."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        f"- Mode: **{'dry-run' if dry_run else 'write'}**",
        f"- Canonical operation pages processed: **{len(results)}**",
        f"- Pages changed: **{len(changed)}**",
        f"- Pages with 5+ sources after execution: **{sum(1 for result in results if result.source_count >= 5)}**",
        "",
        "## Processed Pages",
        "",
        "| Page | Sources | Countries | Changed this run |",
        "|---|---:|---:|---:|",
    ]
    for result in results:
        lines.append(f"| [[{result.slug}]] | {result.source_count} | {result.countries} | {'yes' if result.changed else 'no'} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Add canonical-operation assessment blocks to canonical operation pages.")
    parser.add_argument("--queue", default="")
    parser.add_argument("--report", default="")
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    paths = queue_paths(ROOT / args.queue if args.queue else None)
    results = [result for path in paths if path.exists() for result in [enrich_path(path, args.dry_run, args.date)] if result]
    report_path = ROOT / (args.report or f"wiki/analysis/canonical-operation-assessment-enrichment-{args.date}.md")
    if not args.dry_run:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(render_report(results, args.dry_run, args.date), encoding="utf-8", newline="\n")

    print(f"Canonical operation pages processed: {len(results)}")
    print(f"Pages changed: {sum(1 for result in results if result.changed)}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
