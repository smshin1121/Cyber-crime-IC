from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from harvest_linked_source_text import computed_raw_path, first_url, host_for, is_official_url  # noqa: E402


SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_DIR = ROOT / "raw"
ANALYSIS_DIR = ROOT / "wiki" / "analysis"
DEFAULT_DATE = "2026-04-27"


@dataclass(frozen=True)
class MaterializeResult:
    source: str
    raw_path: str
    status: str
    official: bool


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return []
    if value in (None, ""):
        return []
    return [value]


BOILERPLATE_PATTERNS = (
    "secure .gov websites",
    "lock locked padlock",
    "safely connected to the .gov website",
    "share sensitive information only on official",
    "skip to main content",
    "this source was discovered from bing search results",
)


def is_boilerplate(value: Any) -> bool:
    text = re.sub(r"\s+", " ", str(value or "")).strip().lower()
    return any(pattern in text for pattern in BOILERPLATE_PATTERNS)


def clean_text(value: Any, limit: int = 800) -> str:
    text = str(value or "")
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:")
    return cut + "."


def clean_fact_list(value: Any, limit: int = 500) -> list[str]:
    cleaned: list[str] = []
    seen: set[str] = set()
    for item in as_list(value):
        if is_boilerplate(item):
            continue
        text = clean_text(item, limit=limit)
        if not text:
            continue
        key = text.casefold()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(text)
    return cleaned


def body_summary(content: str, limit: int = 900) -> str:
    lines: list[str] = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line or line == "---":
            continue
        if line.startswith("#"):
            continue
        if line.startswith("|") or line.startswith("- ["):
            continue
        if is_boilerplate(line):
            continue
        lines.append(line)
    return clean_text(" ".join(lines), limit=limit)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def raw_bucket(source_type: str, url: str, official: bool) -> str:
    lowered = source_type.lower()
    if "court" in lowered or "case-document" in lowered or "case document" in lowered:
        return "case-documents"
    if "academic" in lowered or "paper" in lowered:
        return "academic-papers"
    if "legislation" in lowered or "treaty" in lowered or "law" in lowered:
        return "legislation"
    if "report" in lowered or "guidance" in lowered or "government" in lowered:
        return "government-reports"
    if "policy" in lowered:
        return "policy-documents"
    if "news" in lowered and not official:
        return "news"
    if url.lower().endswith(".pdf"):
        return "government-reports" if official else "policy-documents"
    return "press-releases" if official else "news"


def fallback_raw_path(source_path: Path, meta: dict[str, Any], url: str, official: bool) -> Path:
    source_type = str(meta.get("source_type") or meta.get("type") or "")
    if url:
        return computed_raw_path(source_path, str(meta.get("title") or source_path.stem), source_type, url)
    bucket = raw_bucket(source_type, url, official)
    return RAW_DIR / bucket / source_path.name


def existing_raw_status(raw_path: Path, source_meta: dict[str, Any]) -> str:
    if not raw_path.exists():
        return "missing_raw_file"
    try:
        raw_post = frontmatter.load(raw_path)
        raw_meta = raw_post.metadata
        content = raw_post.content or ""
    except Exception:
        raw_meta = {}
        content = raw_path.read_text(encoding="utf-8", errors="replace")

    storage_mode = str(raw_meta.get("storage_mode") or source_meta.get("storage_mode") or "").lower()
    text_status = str(raw_meta.get("text_status") or source_meta.get("text_status") or "").lower()
    copyright_policy = str(raw_meta.get("copyright_policy") or source_meta.get("copyright_policy") or "").lower()
    body_chars = len(content.strip())

    if "## Extracted Text" in content or storage_mode == "fulltext" or text_status == "parsed":
        return "fulltext"
    if "## Extracted Summary" in content or text_status == "summarized" or copyright_policy == "summary-only":
        return "summary_only"
    if "## Source Digest" in content or storage_mode in {"source-digest", "metadata-only"}:
        return "source_digest"
    if body_chars >= 1200:
        return "raw_body_present"
    if body_chars > 0:
        return "stub_or_unclear"
    return "empty_raw"


def build_digest_content(source_path: Path, source_post: frontmatter.Post, raw_rel: str, run_date: str, official: bool) -> tuple[dict[str, Any], str]:
    meta = source_post.metadata
    url = first_url(meta)
    title = str(meta.get("title") or source_path.stem)
    publisher = str(meta.get("publisher") or meta.get("collection_source") or "")
    publish_date = str(meta.get("publish_date") or meta.get("date_filed") or "")
    source_type = str(meta.get("source_type") or meta.get("type") or "")
    language = str(meta.get("language") or "en")
    key_findings = clean_fact_list(meta.get("key_findings"), limit=500)
    pages = [str(item) for item in as_list(meta.get("pages_updated"))]
    summary = body_summary(source_post.content or "")

    storage_mode = "source-digest" if official else "summary-only"
    text_status = "source-digest" if official else "summarized"
    lines = [
        "## Source Archive Record",
        "",
        "This record preserves the source metadata and source-page digest so the source corpus has a separate addressable record for this reference.",
        "",
        "## Source Digest",
        "",
        f"- Title: {title}",
        f"- Publisher: {publisher or 'Unknown'}",
        f"- Source type: {source_type or 'unknown'}",
        f"- Publication date: {publish_date or 'unknown'}",
    ]
    if url:
        lines.append(f"- URL: {url}")
    if pages:
        lines.append(f"- Linked pages: {', '.join(pages)}")
    if key_findings:
        lines.extend(["", "### Key Findings"])
        for finding in key_findings:
            lines.append(f"- {finding}")
    if summary:
        lines.extend(["", "### Source Page Summary", "", summary])
    lines.extend(
        [
            "",
            "## Extraction Notes",
            "",
            f"- storage_mode: {storage_mode}",
            f"- source_page: {source_path.relative_to(ROOT).as_posix()}",
            f"- generated_at: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
            "- full_text: not fetched in this materialization pass",
        ]
    )
    if not official:
        lines.append("- rights_mode: summary-only public corpus record")

    content = "\n".join(lines).rstrip() + "\n"
    raw_meta: dict[str, Any] = {
        "title": title,
        "collection_source": publisher,
        "collection_url": url,
        "final_url": url,
        "collection_domain": host_for(url) if url else "",
        "collection_date": run_date,
        "publish_date": publish_date,
        "language": language,
        "status": "materialized",
        "text_status": text_status,
        "storage_mode": storage_mode,
        "source_type": source_type,
        "source_page": source_path.relative_to(ROOT).as_posix(),
        "word_count": word_count(content),
        "content_hash": sha256_text(content),
        "extraction_date": run_date,
    }
    if not official:
        raw_meta["copyright_policy"] = "summary-only"
    else:
        raw_meta["license_basis"] = str(meta.get("license_basis") or "official_public_record")
    return raw_meta, content


def sync_source_from_existing_raw(
    source_path: Path,
    source_post: frontmatter.Post,
    raw_path: Path,
    raw_rel: str,
    run_date: str,
    official: bool,
) -> None:
    source_meta = source_post.metadata
    source_meta["raw_path"] = raw_rel
    cleaned_findings = clean_fact_list(source_meta.get("key_findings"), limit=500)
    if cleaned_findings:
        source_meta["key_findings"] = cleaned_findings
    else:
        source_meta.pop("key_findings", None)
    try:
        raw_post = frontmatter.load(raw_path)
        raw_meta = raw_post.metadata
    except Exception:
        raw_meta = {}

    copied = False
    for key in (
        "text_status",
        "storage_mode",
        "content_hash",
        "word_count",
        "stored_word_count",
        "last_fetcher",
        "copyright_policy",
    ):
        if raw_meta.get(key) not in (None, ""):
            source_meta[key] = raw_meta[key]
            copied = True
    if raw_meta.get("extraction_date"):
        source_meta["extraction_date"] = raw_meta["extraction_date"]
        copied = True

    if not copied and source_meta.get("extraction_date") == run_date:
        for key in (
            "text_status",
            "storage_mode",
            "content_hash",
            "word_count",
            "stored_word_count",
            "last_fetcher",
            "extraction_date",
        ):
            source_meta.pop(key, None)
    if not official:
        source_meta["copyright_policy"] = "summary-only"
    source_post.metadata = source_meta
    source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")


def materialize_one(
    source_path: Path,
    run_date: str,
    refresh: bool,
    dry_run: bool,
    only_statuses: set[str],
) -> MaterializeResult:
    source_post = frontmatter.load(source_path)
    meta = source_post.metadata
    url = first_url(meta)
    official = is_official_url(url) if url else False
    existing_raw = str(meta.get("raw_path") or "").strip()
    raw_path = ROOT / existing_raw if existing_raw else fallback_raw_path(source_path, meta, url, official)
    raw_rel = raw_path.relative_to(ROOT).as_posix()

    if raw_path.exists() and only_statuses:
        status = existing_raw_status(raw_path, meta)
        if status not in only_statuses:
            if not dry_run and existing_raw:
                sync_source_from_existing_raw(source_path, source_post, raw_path, raw_rel, run_date, official)
            return MaterializeResult(source_path.name, raw_rel, f"skipped_status_{status}", official)

    if raw_path.exists() and not refresh:
        if not dry_run:
            sync_source_from_existing_raw(source_path, source_post, raw_path, raw_rel, run_date, official)
        return MaterializeResult(
            source_path.name,
            raw_rel,
            "skipped_existing" if existing_raw else "linked_existing_raw",
            official,
        )

    raw_meta, content = build_digest_content(source_path, source_post, raw_rel, run_date, official)
    if not dry_run:
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        if not raw_path.exists() or refresh:
            raw_path.write_text(frontmatter.dumps(frontmatter.Post(raw_meta, content)), encoding="utf-8")
        source_meta = source_post.metadata
        source_meta["raw_path"] = raw_rel
        source_meta["text_status"] = raw_meta["text_status"]
        source_meta["storage_mode"] = raw_meta["storage_mode"]
        source_meta["content_hash"] = raw_meta["content_hash"]
        source_meta["word_count"] = raw_meta["word_count"]
        cleaned_findings = clean_fact_list(source_meta.get("key_findings"), limit=500)
        if cleaned_findings:
            source_meta["key_findings"] = cleaned_findings
        else:
            source_meta.pop("key_findings", None)
        source_meta["extraction_date"] = run_date
        if not official:
            source_meta["copyright_policy"] = "summary-only"
        source_post.metadata = source_meta
        source_path.write_text(frontmatter.dumps(source_post), encoding="utf-8")
    return MaterializeResult(
        source_path.name,
        raw_rel,
        "would_materialize" if dry_run else "materialized",
        official,
    )


def write_report(results: list[MaterializeResult], run_date: str, dry_run: bool) -> Path:
    counter = Counter(result.status for result in results)
    official_counter = Counter("official" if result.official else "nonofficial_or_unknown" for result in results)
    path = ANALYSIS_DIR / f"source-content-record-materialization-{run_date}.md"
    lines = [
        "---",
        "type: analysis",
        f'title: "Source Content Record Materialization ({run_date})"',
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Materialization report for creating separate raw/source-content records from wiki source metadata and source-page factual digests."',
        "---",
        "",
        "# Source Content Record Materialization",
        "",
        f"Dry run: `{str(dry_run).lower()}`",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for key, value in counter.most_common():
        lines.append(f"| {key} | {value} |")
    lines.extend(["", "## Source Class Counts", "", "| Class | Count |", "|---|---:|"])
    for key, value in official_counter.most_common():
        lines.append(f"| {key} | {value} |")
    sample = [result for result in results if result.status in {"materialized", "would_materialize"}][:40]
    if sample:
        lines.extend(["", "## Sample Materialized Records", "", "| Source | Raw Path | Official |", "|---|---|---:|"])
        for result in sample:
            lines.append(f"| `{result.source}` | `{result.raw_path}` | {str(result.official).lower()} |")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument("--refresh", action="store_true", help="Rewrite existing raw records.")
    parser.add_argument(
        "--only-status",
        default="",
        help="Comma-separated existing raw statuses to refresh, e.g. stub_or_unclear,empty_raw.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    only_statuses = {item.strip() for item in args.only_status.split(",") if item.strip()}
    results: list[MaterializeResult] = []
    for source_path in sorted(SOURCES_DIR.glob("*.md")):
        if source_path.name.startswith("_"):
            continue
        results.append(materialize_one(source_path, args.date, args.refresh, args.dry_run, only_statuses))
    report = write_report(results, args.date, args.dry_run)
    counter = Counter(result.status for result in results)
    print("tools/materialize_source_content_records.py")
    print(f"  processed: {len(results)}")
    print(f"  statuses: {dict(counter)}")
    print(f"  report: {report.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
