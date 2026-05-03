from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, unquote, urlencode, urlsplit, urlunsplit

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
ANALYSIS_DIR = ROOT / "wiki" / "analysis"
WORKSPACE = ROOT / "_workspace"
DEFAULT_DATE = date.today().isoformat()


STOPWORDS = {
    "a",
    "about",
    "after",
    "all",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "com",
    "for",
    "from",
    "gov",
    "in",
    "into",
    "is",
    "it",
    "its",
    "more",
    "new",
    "news",
    "of",
    "on",
    "or",
    "over",
    "press",
    "release",
    "said",
    "says",
    "the",
    "their",
    "this",
    "to",
    "uk",
    "united",
    "us",
    "with",
    "www",
}

HIGH_RISK_NOTES = (
    "could not be fetched",
    "could not fetch",
    "access-denied",
    "access denied",
    "reconstructed from",
    "article id range",
    "based on article id",
)

GENERIC_RAW_TITLES = {
    "#google vignette",
    "access denied",
    "interpol",
    "page not found",
    "web application security, testing, & scanning - portswigger",
}

ALIGNMENT_OK_STATUSES = {
    "verified",
    "duplicate-alias",
    "index-item",
    "localized-title",
    "raw-fetch-generic-ok",
}


@dataclass(frozen=True)
class AlignmentRow:
    slug: str
    source_path: str
    raw_path: str
    severity: str
    issue: str
    title_score: str
    source_title: str
    raw_title: str
    source_url: str
    raw_url: str
    publisher: str
    publish_date: str
    raw_publish_date: str
    pages_updated: str
    evidence: str


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return []
    if value in (None, ""):
        return []
    return [value]


def normalize_url(url: str) -> str:
    if not url:
        return ""
    parts = urlsplit(str(url).strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path.rstrip("/") or "/"
    query_pairs = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        low = key.lower()
        if low.startswith("utm_") or low in {"fbclid", "gclid", "ref", "source"}:
            continue
        query_pairs.append((key, value))
    return urlunsplit((parts.scheme.lower(), host, path, urlencode(query_pairs), ""))


def clean_title(title: str) -> str:
    text = re.sub(r"\[\[|\]\]", " ", str(title or ""))
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.sub(r"^[A-Z][A-Za-z .'-]{2,25}:\s+", "", text)
    return text.strip()


def tokens(text: str) -> set[str]:
    cleaned = unquote(clean_title(text)).lower()
    raw_tokens = re.findall(r"[a-z0-9][a-z0-9'-]{2,}", cleaned)
    result: set[str] = set()
    for token in raw_tokens:
        token = token.strip("-'")
        if not token or token in STOPWORDS:
            continue
        if token.isdigit():
            continue
        result.add(token)
    return result


def title_score(left: str, right: str) -> float:
    left_tokens = tokens(left)
    right_tokens = tokens(right)
    if not left_tokens or not right_tokens:
        return 1.0 if clean_title(left).lower() == clean_title(right).lower() else 0.0
    overlap = len(left_tokens & right_tokens)
    containment = overlap / min(len(left_tokens), len(right_tokens))
    jaccard = overlap / len(left_tokens | right_tokens)
    return max(containment, jaccard)


def useful_title(title: str) -> bool:
    title = clean_title(title)
    if len(title) < 8:
        return False
    if len(tokens(title)) < 2:
        return False
    return True


def is_generic_raw_title(title: str) -> bool:
    normalized = clean_title(title).lower().strip()
    return normalized in GENERIC_RAW_TITLES


def url_slug_tokens(url: str) -> set[str]:
    if not url:
        return set()
    parts = urlsplit(url)
    segments = [segment for segment in parts.path.split("/") if segment]
    if not segments:
        return set()
    last = segments[-1].rsplit(".", 1)[0]
    result = tokens(last.replace("-", " ").replace("_", " "))
    if len(result) < 3:
        return set()
    return result


def load_post(path: Path) -> frontmatter.Post:
    try:
        return frontmatter.load(path)
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")
        return frontmatter.Post({}, text)


def first_heading(content: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def raw_title(raw_post: frontmatter.Post) -> str:
    meta_title = str(raw_post.metadata.get("title") or "").strip()
    if useful_title(meta_title):
        return meta_title
    heading = first_heading(raw_post.content or "")
    if useful_title(heading):
        return heading
    return meta_title


def contains_high_risk_note(text: str) -> bool:
    lower = text.lower()
    return any(note in lower for note in HIGH_RISK_NOTES)


def classify_source(path: Path) -> AlignmentRow:
    post = load_post(path)
    meta = post.metadata
    slug = path.stem
    source_title = str(meta.get("title") or slug)
    source_url = str(meta.get("collection_url") or meta.get("url") or "").strip()
    raw_path_value = str(meta.get("raw_path") or "").strip()
    publisher = str(meta.get("publisher") or meta.get("collection_source") or "")
    publish_date = str(meta.get("publish_date") or "")
    pages_updated = ";".join(str(item) for item in as_list(meta.get("pages_updated")))
    reviewed_status = str(meta.get("alignment_status") or "").strip().lower()
    reviewed_note = str(meta.get("alignment_note") or "").strip()

    if not raw_path_value:
        return AlignmentRow(
            slug=slug,
            source_path=path.relative_to(ROOT).as_posix(),
            raw_path="",
            severity="review",
            issue="missing_raw_path",
            title_score="",
            source_title=source_title,
            raw_title="",
            source_url=source_url,
            raw_url="",
            publisher=publisher,
            publish_date=publish_date,
            raw_publish_date="",
            pages_updated=pages_updated,
            evidence="Source page has no raw_path for local URL/content comparison.",
        )

    raw_path = ROOT / raw_path_value
    if not raw_path.exists():
        return AlignmentRow(
            slug=slug,
            source_path=path.relative_to(ROOT).as_posix(),
            raw_path=raw_path_value,
            severity="review",
            issue="missing_raw_file",
            title_score="",
            source_title=source_title,
            raw_title="",
            source_url=source_url,
            raw_url="",
            publisher=publisher,
            publish_date=publish_date,
            raw_publish_date="",
            pages_updated=pages_updated,
            evidence="raw_path points to a file that does not exist.",
        )

    raw_post = load_post(raw_path)
    raw_meta = raw_post.metadata
    raw_url = str(raw_meta.get("collection_url") or raw_meta.get("final_url") or "").strip()
    actual_raw_title = raw_title(raw_post)
    raw_publish_date = str(raw_meta.get("publish_date") or "")
    score = title_score(source_title, actual_raw_title) if actual_raw_title else 0.0

    if meta.get("duplicate_of"):
        return AlignmentRow(
            slug=slug,
            source_path=path.relative_to(ROOT).as_posix(),
            raw_path=raw_path_value,
            severity="ok",
            issue="ok",
            title_score=f"{score:.2f}" if actual_raw_title else "",
            source_title=source_title,
            raw_title=actual_raw_title,
            source_url=source_url,
            raw_url=raw_url,
            publisher=publisher,
            publish_date=publish_date,
            raw_publish_date=raw_publish_date,
            pages_updated=pages_updated,
            evidence="Duplicate alias points to a canonical source page; not treated as an independent URL/content mismatch.",
        )

    if reviewed_status in ALIGNMENT_OK_STATUSES:
        return AlignmentRow(
            slug=slug,
            source_path=path.relative_to(ROOT).as_posix(),
            raw_path=raw_path_value,
            severity="ok",
            issue="ok",
            title_score=f"{score:.2f}" if actual_raw_title else "",
            source_title=source_title,
            raw_title=actual_raw_title,
            source_url=source_url,
            raw_url=raw_url,
            publisher=publisher,
            publish_date=publish_date,
            raw_publish_date=raw_publish_date,
            pages_updated=pages_updated,
            evidence=reviewed_note or f"Manual alignment review marked this source as {reviewed_status}.",
        )

    source_slug_tokens = url_slug_tokens(source_url)
    body_text = "\n".join(
        [
            source_title,
            "\n".join(str(item) for item in as_list(meta.get("key_findings"))),
            post.content or "",
        ]
    )
    high_risk_note = contains_high_risk_note(body_text)

    issue = "ok"
    severity = "ok"
    evidence = "Source title, URL, and linked raw metadata are aligned."

    generic_raw_title = is_generic_raw_title(actual_raw_title)

    if source_url and raw_url and normalize_url(source_url) != normalize_url(raw_url):
        if score >= 0.95:
            issue = "ok"
            severity = "ok"
            evidence = "Source and raw URLs differ, but titles match; treated as redirect/canonical URL drift."
        elif score >= 0.45:
            issue = "source_raw_url_drift"
            severity = "review"
            evidence = "Source and raw URLs differ, but titles align; review canonical URL/redirect handling."
        elif generic_raw_title:
            issue = "source_raw_url_mismatch_raw_generic"
            severity = "review"
            evidence = "Source and raw URLs differ, and raw fetched a generic or not-found title."
        else:
            issue = "source_raw_url_mismatch"
            severity = "confirmed_mismatch"
            evidence = "Source collection_url differs from linked raw collection_url/final_url and titles do not align."
    elif useful_title(source_title) and useful_title(actual_raw_title):
        if generic_raw_title and score < 0.45:
            issue = "generic_raw_title"
            severity = "review"
            evidence = "Raw metadata has a generic site/not-found title; review fetch quality before treating as content mismatch."
        elif score < 0.20:
            issue = "source_raw_title_mismatch"
            severity = "high_confidence_mismatch" if high_risk_note else "review"
            evidence = (
                "Source title has very low token overlap with raw title"
                + (" and the source body contains reconstruction/fetch-failure notes." if high_risk_note else ".")
            )
        elif score < 0.45:
            issue = "source_raw_title_low_overlap"
            severity = "review"
            evidence = "Source title only partially overlaps with raw title."

    if issue == "ok" and score < 0.95 and source_slug_tokens and (not useful_title(actual_raw_title) or score < 0.45):
        title_tokens = tokens(source_title)
        if title_tokens:
            slug_score = len(source_slug_tokens & title_tokens) / min(len(source_slug_tokens), len(title_tokens))
            if slug_score < 0.20:
                issue = "url_slug_title_low_overlap"
                severity = "review"
                evidence = "URL slug tokens have low overlap with source title; review for wrong URL or generic page title."

    return AlignmentRow(
        slug=slug,
        source_path=path.relative_to(ROOT).as_posix(),
        raw_path=raw_path_value,
        severity=severity,
        issue=issue,
        title_score=f"{score:.2f}" if actual_raw_title else "",
        source_title=source_title,
        raw_title=actual_raw_title,
        source_url=source_url,
        raw_url=raw_url,
        publisher=publisher,
        publish_date=publish_date,
        raw_publish_date=raw_publish_date,
        pages_updated=pages_updated,
        evidence=evidence,
    )


def load_rows() -> list[AlignmentRow]:
    rows: list[AlignmentRow] = []
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        rows.append(classify_source(path))
    return rows


def write_csv(rows: list[AlignmentRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(AlignmentRow.__dataclass_fields__))
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def render_report(rows: list[AlignmentRow], run_date: str, csv_path: Path) -> str:
    severity_counter = Counter(row.severity for row in rows)
    issue_counter = Counter(row.issue for row in rows)
    review_rows = [row for row in rows if row.severity != "ok"]
    blocking_rows = [row for row in rows if row.severity in {"confirmed_mismatch", "high_confidence_mismatch"}]

    lines = [
        "---",
        f"title: Source URL/Content Alignment Audit ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Corpus-wide audit comparing source-page metadata against linked raw URL metadata and fetched titles."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "This audit compares every `wiki/sources` page with its linked `raw_path`. It is designed to catch cases where a source page or downstream operation cites one URL while its title/summary describes a different article.",
        "",
        f"- Source pages audited: **{len(rows)}**",
        f"- Confirmed/high-confidence mismatches: **{len(blocking_rows)}**",
        f"- Review candidates: **{len(review_rows) - len(blocking_rows)}**",
        f"- CSV detail: `{csv_path.relative_to(ROOT).as_posix()}`",
        "",
        "## Severity Counts",
        "",
        "| Severity | Count |",
        "|---|---:|",
    ]
    for severity, count in sorted(severity_counter.items()):
        lines.append(f"| {severity} | {count} |")

    lines.extend(["", "## Issue Counts", "", "| Issue | Count |", "|---|---:|"])
    for issue, count in issue_counter.most_common():
        lines.append(f"| {issue} | {count} |")

    lines.extend(
        [
            "",
            "## Confirmed And High-Confidence Mismatches",
            "",
            "| # | Source | Issue | Source title | Raw title | Evidence |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for index, row in enumerate(blocking_rows[:100], 1):
        lines.append(
            "| {index} | [[{slug}]] | {issue} | {source_title} | {raw_title} | {evidence} |".format(
                index=index,
                slug=row.slug,
                issue=row.issue,
                source_title=escape_cell(row.source_title),
                raw_title=escape_cell(row.raw_title),
                evidence=escape_cell(row.evidence),
            )
        )

    lines.extend(
        [
            "",
            "## Review Candidates",
            "",
            "| # | Source | Issue | Score | Source title | Raw title | URL |",
            "|---:|---|---|---:|---|---|---|",
        ]
    )
    review_only = [row for row in review_rows if row not in blocking_rows]
    for index, row in enumerate(review_only[:150], 1):
        lines.append(
            "| {index} | [[{slug}]] | {issue} | {score} | {source_title} | {raw_title} | {url} |".format(
                index=index,
                slug=row.slug,
                issue=row.issue,
                score=row.title_score or "",
                source_title=escape_cell(row.source_title),
                raw_title=escape_cell(row.raw_title),
                url=escape_cell(row.source_url),
            )
        )

    return "\n".join(lines) + "\n"


def escape_cell(value: str) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=DEFAULT_DATE)
    args = parser.parse_args()
    rows = load_rows()
    csv_path = WORKSPACE / f"source_url_content_alignment_{args.date}.csv"
    report_path = ANALYSIS_DIR / f"source-url-content-alignment-audit-{args.date}.md"
    write_csv(rows, csv_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(rows, args.date, csv_path), encoding="utf-8")

    severity_counter = Counter(row.severity for row in rows)
    issue_counter = Counter(row.issue for row in rows)
    print(f"Sources audited: {len(rows)}")
    print("Severity counts:")
    for severity, count in sorted(severity_counter.items()):
        print(f"  {severity}: {count}")
    print("Issue counts:")
    for issue, count in issue_counter.most_common():
        print(f"  {issue}: {count}")
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
