from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter

from dedupe_page_source_refs import as_list, render_references, wikilink, wikilink_slug
from source_canonical_map import score_source, word_count


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
WORKSPACE = ROOT / "_workspace"
REPORT_PATH = WIKI_DIR / "analysis" / "absorbed-wrapper-source-normalization-2026-04-26.md"


@dataclass(frozen=True)
class SourceChoice:
    slug: str
    title: str
    collection_url: str
    base_score: int
    overlap_score: int
    final_score: int
    original_index: int


@dataclass(frozen=True)
class WrapperChange:
    path: Path
    title: str
    category: str
    original_count: int
    kept: SourceChoice
    removed: list[str]


def page_paths() -> list[Path]:
    paths: list[Path] = []
    for category in ("operations", "cases"):
        directory = WIKI_DIR / category
        paths.extend(path for path in sorted(directory.glob("*.md")) if not path.name.startswith("_"))
    return paths


def source_post(slug: str) -> frontmatter.Post | None:
    path = SOURCES_DIR / f"{slug}.md"
    if not path.exists():
        return None
    try:
        return frontmatter.load(path)
    except Exception:
        return None


def tokens(text: str) -> set[str]:
    raw = re.findall(r"[A-Za-z0-9]+", text.lower())
    stop = {
        "operation",
        "enforcement",
        "action",
        "united",
        "states",
        "case",
        "source",
        "derived",
        "charged",
        "sentenced",
        "arrested",
        "indicted",
        "pleads",
        "guilty",
        "federal",
        "prison",
        "justice",
        "gov",
        "with",
        "from",
        "and",
        "the",
        "for",
        "to",
        "of",
        "in",
        "v",
        "us",
    }
    return {item for item in raw if len(item) >= 4 and item not in stop}


def page_token_text(meta: dict[str, Any], path: Path) -> str:
    parts: list[str] = [path.stem, str(meta.get("title") or ""), str(meta.get("target_entity") or "")]
    parts.extend(str(item) for item in as_list(meta.get("aliases")))
    parts.extend(wikilink_slug(item) for item in as_list(meta.get("related_cases")))
    parts.extend(wikilink_slug(item) for item in as_list(meta.get("related_operations")))
    if meta.get("related_operation"):
        parts.append(wikilink_slug(meta.get("related_operation")))
    if meta.get("parent_operation"):
        parts.append(wikilink_slug(meta.get("parent_operation")))
    return " ".join(parts)


def choose_source(slugs: list[str], meta: dict[str, Any], path: Path) -> SourceChoice:
    title_tokens = tokens(" ".join([path.stem, str(meta.get("title") or ""), str(meta.get("target_entity") or "")]))
    page_tokens = tokens(page_token_text(meta, path))
    choices: list[SourceChoice] = []
    for idx, slug in enumerate(slugs):
        post = source_post(slug)
        if post is None:
            title = slug
            collection_url = ""
            base_score = -1000
            source_text = slug
        else:
            title = str(post.metadata.get("title") or slug)
            collection_url = str(post.metadata.get("collection_url") or "")
            base_score, _ = score_source(slug, post.metadata, word_count(post.content or ""))
            source_text = " ".join(
                [
                    slug,
                    title,
                    str(post.metadata.get("publisher") or ""),
                    str(post.metadata.get("raw_path") or ""),
                ]
            )
        source_tokens = tokens(source_text)
        title_overlap = len(title_tokens & source_tokens)
        context_overlap = len(page_tokens & source_tokens)
        overlap_score = title_overlap * 18 + context_overlap * 4
        final_score = base_score + overlap_score - idx
        choices.append(
            SourceChoice(
                slug=slug,
                title=title,
                collection_url=collection_url,
                base_score=base_score,
                overlap_score=overlap_score,
                final_score=final_score,
                original_index=idx,
            )
        )
    return sorted(choices, key=lambda item: (-item.final_score, item.original_index, item.slug))[0]


def has_canonical_pointer(meta: dict[str, Any], body: str) -> bool:
    return bool(
        re.search(r"^## Canonical Record\b", body, re.I | re.M)
        or meta.get("parent_operation")
        or as_list(meta.get("related_cases"))
        or meta.get("related_operation")
    )


def replace_references(body: str, sources: list[str]) -> str:
    refs = render_references(sources)
    match = re.search(r"^## References\s*$", body, re.M)
    if not match:
        return body.rstrip() + "\n\n" + refs
    return body[: match.start()].rstrip() + "\n\n" + refs


def strip_wrapping_quotes(value: Any) -> str:
    return str(value).strip().strip("\"'")


def sanitize_aliases(meta: dict[str, Any]) -> None:
    aliases = meta.get("aliases")
    if not isinstance(aliases, list):
        return

    clean: list[Any] = []
    changed = False
    for item in aliases:
        if isinstance(item, dict) and len(item) == 1:
            key, value = next(iter(item.items()))
            if str(key).startswith(("'", '"')):
                clean.append(f"{strip_wrapping_quotes(key)}: {strip_wrapping_quotes(value)}")
                changed = True
                continue
        clean.append(item)
    if changed:
        meta["aliases"] = clean


def process_page(path: Path, apply: bool) -> WrapperChange | None:
    post = frontmatter.load(path)
    meta = post.metadata
    body = post.content or ""
    if str(meta.get("status") or "").strip().lower() != "absorbed":
        return None
    if not has_canonical_pointer(meta, body):
        return None

    source_values = as_list(meta.get("sources"))
    slugs = [wikilink_slug(item) for item in source_values]
    slugs = [slug for slug in slugs if slug]
    if len(slugs) <= 1:
        return None

    kept = choose_source(slugs, meta, path)
    removed = [slug for slug in slugs if slug != kept.slug]

    if apply:
        sanitize_aliases(meta)
        meta["source_count"] = 1
        meta["sources"] = [wikilink(kept.slug)]
        meta["updated"] = "2026-04-26"
        post.metadata = meta
        post.content = replace_references(body, [kept.slug])
        path.write_text(frontmatter.dumps(post), encoding="utf-8")

    return WrapperChange(
        path=path,
        title=str(meta.get("title") or path.stem),
        category=path.parent.name,
        original_count=len(slugs),
        kept=kept,
        removed=removed,
    )


def write_csv(changes: list[WrapperChange]) -> Path:
    path = WORKSPACE / "absorbed_wrapper_source_normalization_2026-04-26.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "page",
                "category",
                "title",
                "original_count",
                "kept_source",
                "kept_title",
                "kept_url",
                "kept_base_score",
                "kept_overlap_score",
                "kept_final_score",
                "removed_sources",
            ]
        )
        for change in changes:
            writer.writerow(
                [
                    str(change.path.relative_to(ROOT)).replace("\\", "/"),
                    change.category,
                    change.title,
                    change.original_count,
                    change.kept.slug,
                    change.kept.title,
                    change.kept.collection_url,
                    change.kept.base_score,
                    change.kept.overlap_score,
                    change.kept.final_score,
                    "; ".join(change.removed),
                ]
            )
    return path


def render_report(changes: list[WrapperChange], applied: bool) -> str:
    operation_count = sum(1 for change in changes if change.category == "operations")
    case_count = sum(1 for change in changes if change.category == "cases")
    removed_count = sum(len(change.removed) for change in changes)
    lines = [
        "---",
        "title: Absorbed Wrapper Source Normalization (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Normalization log for absorbed wrapper pages that previously carried multiple references."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "Absorbed wrapper pages are not substantive operation or case records. They should point to their canonical record and retain only one source reference so that source counts do not imply independent evidentiary depth.",
        "",
        f"- Mode: **{'applied' if applied else 'dry-run'}**",
        f"- Wrapper pages normalized: **{len(changes)}**",
        f"- Operations: **{operation_count}**",
        f"- Cases: **{case_count}**",
        f"- Removed wrapper-only references: **{removed_count}**",
        "",
        "## Selection Rule",
        "",
        "The retained source is selected by source quality score plus token overlap with the wrapper title, target entity, related case, and parent operation. Source pages are not deleted or merged by this process.",
        "",
        "## First 120 Changes",
        "",
        "| # | Page | Type | Before | Kept source | Removed |",
        "|---:|---|---|---:|---|---|",
    ]
    for idx, change in enumerate(changes[:120], 1):
        removed = "<br>".join(f"[[{slug}]]" for slug in change.removed[:8])
        if len(change.removed) > 8:
            removed += f"<br>... +{len(change.removed) - 8} more"
        lines.append(
            f"| {idx} | [[{change.path.stem}]] | {change.category[:-1]} | {change.original_count} | [[{change.kept.slug}]] | {removed} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize absorbed wrapper pages to one representative source.")
    parser.add_argument("--apply", action="store_true", help="Write changes. Omit for dry-run.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of pages to process.")
    args = parser.parse_args()

    changes: list[WrapperChange] = []
    for path in page_paths():
        change = process_page(path, apply=args.apply)
        if not change:
            continue
        changes.append(change)
        if args.limit and len(changes) >= args.limit:
            break

    csv_path = write_csv(changes)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(changes, args.apply), encoding="utf-8")

    print(f"Mode: {'applied' if args.apply else 'dry-run'}")
    print(f"Wrapper pages normalized: {len(changes)}")
    print(f"CSV: {csv_path}")
    print(f"Report: {REPORT_PATH}")
    for change in changes[:20]:
        rel = change.path.relative_to(ROOT)
        print(f"- {rel}: {change.original_count} -> 1; kept {change.kept.slug}")


if __name__ == "__main__":
    main()
