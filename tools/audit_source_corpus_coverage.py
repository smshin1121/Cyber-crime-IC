from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from harvest_linked_source_text import first_url, has_extracted_text, is_official_url  # noqa: E402


SOURCES_DIR = ROOT / "wiki" / "sources"
RAW_DIR = ROOT / "raw"
ANALYSIS_DIR = ROOT / "wiki" / "analysis"
WORKSPACE = ROOT / "_workspace"
DEFAULT_DATE = "2026-04-27"


@dataclass(frozen=True)
class SourceCoverage:
    slug: str
    source_path: str
    title: str
    publisher: str
    source_type: str
    url: str
    official: bool
    raw_path: str
    raw_exists: bool
    raw_status: str
    storage_mode: str
    text_status: str
    word_count: int
    body_chars: int
    needs_fetch: bool
    pages_updated: str
    content_hash: str


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return []
    if value in (None, ""):
        return []
    return [value]


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def hash_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def classify_raw(raw_path: Path, source_meta: dict[str, Any]) -> tuple[str, str, str, int, int, str]:
    if not raw_path.exists():
        return "missing_raw_file", "", "", 0, 0, ""

    try:
        post = frontmatter.load(raw_path)
        meta = post.metadata
        content = post.content or ""
    except Exception:
        content = raw_path.read_text(encoding="utf-8", errors="replace")
        meta = {}

    storage_mode = str(meta.get("storage_mode") or source_meta.get("storage_mode") or "").strip()
    text_status = str(meta.get("text_status") or source_meta.get("text_status") or "").strip()
    copyright_policy = str(meta.get("copyright_policy") or source_meta.get("copyright_policy") or "").strip()
    body_chars = len(content.strip())
    word_count = int(meta.get("word_count") or 0) if str(meta.get("word_count") or "").isdigit() else 0
    if not word_count:
        word_count = count_words(content)
    content_hash = str(meta.get("content_hash") or source_meta.get("content_hash") or "")
    if not content_hash and content.strip():
        content_hash = hash_text(content)

    low_storage = storage_mode.lower()
    low_status = text_status.lower()
    low_policy = copyright_policy.lower()

    if "## Extracted Text" in content or low_storage == "fulltext" or low_status == "parsed":
        raw_status = "fulltext"
    elif "## Extracted Summary" in content or low_status == "summarized" or low_policy == "summary-only":
        raw_status = "summary_only"
    elif "## Source Digest" in content or low_storage in {"source-digest", "metadata-only"}:
        raw_status = "source_digest"
    elif body_chars >= 1200:
        raw_status = "raw_body_present"
    elif body_chars > 0:
        raw_status = "stub_or_unclear"
    else:
        raw_status = "empty_raw"

    return raw_status, storage_mode, text_status, word_count, body_chars, content_hash


def load_rows() -> list[SourceCoverage]:
    rows: list[SourceCoverage] = []
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        url = first_url(meta)
        raw_path_value = str(meta.get("raw_path") or "").strip()
        raw_path = ROOT / raw_path_value if raw_path_value else Path()
        raw_status, storage_mode, text_status, word_count, body_chars, content_hash = (
            classify_raw(raw_path, meta) if raw_path_value else ("missing_raw_path", "", "", 0, 0, "")
        )
        needs_fetch = False
        if raw_path_value:
            needs_fetch = not has_extracted_text(raw_path, min_chars=1200)
        elif url:
            needs_fetch = True
        rows.append(
            SourceCoverage(
                slug=path.stem,
                source_path=path.relative_to(ROOT).as_posix(),
                title=str(meta.get("title") or path.stem),
                publisher=str(meta.get("publisher") or meta.get("collection_source") or ""),
                source_type=str(meta.get("source_type") or meta.get("type") or ""),
                url=url,
                official=is_official_url(url) if url else False,
                raw_path=raw_path_value,
                raw_exists=bool(raw_path_value and raw_path.exists()),
                raw_status=raw_status,
                storage_mode=storage_mode,
                text_status=text_status,
                word_count=word_count,
                body_chars=body_chars,
                needs_fetch=needs_fetch,
                pages_updated=";".join(str(item) for item in as_list(meta.get("pages_updated"))),
                content_hash=content_hash,
            )
        )
    return rows


def write_csv(rows: list[SourceCoverage], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(SourceCoverage.__dataclass_fields__))
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def write_report(rows: list[SourceCoverage], path: Path, csv_path: Path, run_date: str) -> None:
    counters: Counter[str] = Counter()
    status_counter: Counter[str] = Counter()
    type_counter: Counter[str] = Counter()
    needs_counter: Counter[str] = Counter()
    examples: dict[str, list[SourceCoverage]] = defaultdict(list)

    for row in rows:
        counters["source_pages"] += 1
        counters["with_url" if row.url else "without_url"] += 1
        counters["official_url" if row.official else "nonofficial_or_no_url"] += 1
        counters["with_raw_path" if row.raw_path else "without_raw_path"] += 1
        counters["raw_exists" if row.raw_exists else "raw_missing_or_unlinked"] += 1
        status_counter[row.raw_status] += 1
        type_counter[row.source_type or "unknown"] += 1
        if row.needs_fetch:
            needs_counter["official" if row.official else "nonofficial_or_unknown"] += 1
            if len(examples["needs_fetch"]) < 15:
                examples["needs_fetch"].append(row)
        if row.raw_status in {"missing_raw_path", "missing_raw_file", "empty_raw", "stub_or_unclear"}:
            if len(examples[row.raw_status]) < 15:
                examples[row.raw_status].append(row)

    def table(counter: Counter[str]) -> str:
        lines = ["| Item | Count |", "|---|---:|"]
        for key, value in counter.most_common():
            lines.append(f"| {key} | {value} |")
        return "\n".join(lines)

    lines = [
        "---",
        "type: analysis",
        f'title: "Source Corpus Coverage Audit ({run_date})"',
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Repository-wide audit of wiki source pages, raw source records, fulltext coverage, summary-only coverage, and remaining fetch/materialization gaps."',
        "---",
        "",
        "# Source Corpus Coverage Audit",
        "",
        "This audit checks whether every `wiki/sources` page has a separate raw/source-content record and whether that record is full text, summary-only, source-digest, or still missing.",
        "",
        "## Coverage Summary",
        "",
        table(counters),
        "",
        "## Raw Status",
        "",
        table(status_counter),
        "",
        "## Fetch Queue",
        "",
        table(needs_counter),
        "",
        "## Source Types",
        "",
        table(type_counter),
        "",
        "## Interpretation",
        "",
        "- `fulltext` records can be used directly for source-grounded enrichment.",
        "- `summary_only` and `source_digest` records should drive factual wiki enrichment through paraphrased fact bullets, not article reproduction.",
        "- `missing_raw_path` and `missing_raw_file` records need materialization before the corpus can be treated as complete.",
        "- Official/public records should be prioritized for full-text fetching; nonofficial media should remain rights-sensitive unless a permissive basis is documented.",
        "",
        "## Example Gaps",
        "",
    ]
    for key in ("missing_raw_path", "missing_raw_file", "stub_or_unclear", "empty_raw", "needs_fetch"):
        sample = examples.get(key, [])
        if not sample:
            continue
        lines.extend([f"### {key}", "", "| Source | Raw Path | Publisher | URL |", "|---|---|---|---|"])
        for row in sample:
            lines.append(f"| `{row.slug}` | `{row.raw_path}` | {row.publisher} | {row.url} |")
        lines.append("")

    lines.extend(
        [
            "## Artifacts",
            "",
            f"- CSV: `{csv_path.relative_to(ROOT).as_posix()}`",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument("--csv", default="")
    parser.add_argument("--report", default="")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_date = args.date or date.today().isoformat()
    csv_path = Path(args.csv) if args.csv else WORKSPACE / f"source_corpus_coverage_{run_date}.csv"
    report_path = Path(args.report) if args.report else ANALYSIS_DIR / f"source-corpus-coverage-{run_date}.md"
    if not csv_path.is_absolute():
        csv_path = ROOT / csv_path
    if not report_path.is_absolute():
        report_path = ROOT / report_path
    rows = load_rows()
    write_csv(rows, csv_path)
    write_report(rows, report_path, csv_path, run_date)
    status_counter = Counter(row.raw_status for row in rows)
    print("tools/audit_source_corpus_coverage.py")
    print(f"  source pages: {len(rows)}")
    print(f"  raw statuses: {dict(status_counter)}")
    print(f"  csv: {csv_path.relative_to(ROOT).as_posix()}")
    print(f"  report: {report_path.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
