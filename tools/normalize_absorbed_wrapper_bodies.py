from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import frontmatter

from audit_content_depth import strip_references, word_count
from dedupe_page_source_refs import as_list


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
WORKSPACE = ROOT / "_workspace"
TODAY = date.today().isoformat()

SCOPE_NOTE = (
    "This wrapper is retained for search, backlink, and source-trace continuity only; "
    "source-backed facts and procedural analysis live in the canonical record below."
)


@dataclass(frozen=True)
class WrapperBodyChange:
    path: Path
    category: str
    title: str
    before_words: int
    after_words: int


def as_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def has_canonical_pointer(meta: dict[str, Any], body: str) -> bool:
    return bool(
        re.search(r"^## Canonical Record\b", body, re.I | re.M)
        or meta.get("parent_operation")
        or as_list(meta.get("related_cases"))
        or meta.get("related_operation")
    )


def insert_scope_note(body: str) -> str:
    if SCOPE_NOTE in body:
        return body

    canonical_match = re.search(r"^## Canonical Record\b", body, re.I | re.M)
    if canonical_match:
        return body[: canonical_match.start()].rstrip() + "\n\n" + SCOPE_NOTE + "\n\n" + body[canonical_match.start() :]

    refs_match = re.search(r"^## References\b", body, re.I | re.M)
    if refs_match:
        return body[: refs_match.start()].rstrip() + "\n\n" + SCOPE_NOTE + "\n\n" + body[refs_match.start() :]

    return body.rstrip() + "\n\n" + SCOPE_NOTE + "\n"


def page_paths() -> list[Path]:
    paths: list[Path] = []
    for category in ("operations", "cases"):
        directory = WIKI_DIR / category
        paths.extend(path for path in sorted(directory.glob("*.md")) if not path.name.startswith("_"))
    return paths


def process_page(path: Path, apply: bool, run_date: str) -> WrapperBodyChange | None:
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content or ""
    if str(meta.get("status") or "").strip().lower() != "absorbed":
        return None
    if not has_canonical_pointer(meta, body):
        return None

    before_words = word_count(strip_references(body))
    if before_words >= 35 or SCOPE_NOTE in body:
        return None

    new_body = insert_scope_note(body)
    after_words = word_count(strip_references(new_body))

    if apply:
        meta["updated"] = run_date
        post.metadata = meta
        post.content = new_body
        path.write_text(frontmatter.dumps(post), encoding="utf-8")

    return WrapperBodyChange(
        path=path,
        category=path.parent.name,
        title=str(meta.get("title") or path.stem),
        before_words=before_words,
        after_words=after_words,
    )


def write_csv(changes: list[WrapperBodyChange], run_date: str) -> Path:
    path = WORKSPACE / f"absorbed_wrapper_body_normalization_{run_date}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["page", "category", "title", "before_words", "after_words"])
        for change in changes:
            writer.writerow(
                [
                    str(change.path.relative_to(ROOT)).replace("\\", "/"),
                    change.category,
                    change.title,
                    change.before_words,
                    change.after_words,
                ]
            )
    return path


def render_report(changes: list[WrapperBodyChange], applied: bool, run_date: str) -> str:
    operation_count = sum(1 for change in changes if change.category == "operations")
    case_count = sum(1 for change in changes if change.category == "cases")
    lines = [
        "---",
        f"title: Absorbed Wrapper Body Normalization ({run_date})",
        "type: analysis",
        f"created: {run_date}",
        f"updated: {run_date}",
        'summary: "Normalization log for absorbed wrapper pages that needed an explicit scope note."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "Absorbed wrapper pages are traceability records, not substantive operation or case records. This pass adds a short scope note so sparse wrappers clearly point readers to the canonical record.",
        "",
        f"- Mode: **{'applied' if applied else 'dry-run'}**",
        f"- Wrapper pages updated: **{len(changes)}**",
        f"- Operations: **{operation_count}**",
        f"- Cases: **{case_count}**",
        "",
        "## Scope Note",
        "",
        SCOPE_NOTE,
        "",
        "## First 120 Changes",
        "",
        "| # | Page | Type | Words before | Words after |",
        "|---:|---|---|---:|---:|",
    ]
    for idx, change in enumerate(changes[:120], 1):
        lines.append(
            f"| {idx} | [[{change.path.stem}]] | {change.category[:-1]} | {change.before_words} | {change.after_words} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Add explicit scope notes to sparse absorbed wrapper pages.")
    parser.add_argument("--apply", action="store_true", help="Write changes. Omit for dry-run.")
    parser.add_argument("--date", default=TODAY, help="Run date used in report names and updated metadata.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of pages to process.")
    args = parser.parse_args()

    changes: list[WrapperBodyChange] = []
    for path in page_paths():
        change = process_page(path, apply=args.apply, run_date=args.date)
        if not change:
            continue
        changes.append(change)
        if args.limit and len(changes) >= args.limit:
            break

    csv_path = write_csv(changes, args.date)
    report_path = WIKI_DIR / "analysis" / f"absorbed-wrapper-body-normalization-{args.date}.md"
    report_path.write_text(render_report(changes, args.apply, args.date), encoding="utf-8")

    print(f"Mode: {'applied' if args.apply else 'dry-run'}")
    print(f"Wrapper pages updated: {len(changes)}")
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")
    for change in changes[:20]:
        rel = change.path.relative_to(ROOT)
        print(f"- {rel}: {change.before_words} -> {change.after_words}")


if __name__ == "__main__":
    main()
