from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
DOCS_DIR = ROOT / "docs"
OPS_DIR = WIKI_DIR / "operations"
SOURCES_DIR = WIKI_DIR / "sources"
WORKSPACE = ROOT / "_workspace"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
WIKILINK_FULL_RE = re.compile(r"\[\[([^\]]+)\]\]")
REF_ROW_RE = re.compile(r"^\|\s*\[?\d+\]?\s*\|", re.M)
INDEX_ROW_RE = re.compile(r"^\|.*?\[\[([^\]|#]+)", re.M)
INDEX_HEADING_COUNT_RE = re.compile(r"^#\s+.+?\((\d+)\)\s*$", re.M)
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
SKIP_MD = {"_index.md", "index.md", "log.md", "overview.md"}


def import_yaml() -> Any:
    try:
        import yaml  # type: ignore

        return yaml
    except ModuleNotFoundError:
        for candidate in ("vendor37_build", "vendor_build2", ".vendor_build", "_workspace/.vendor_harvest"):
            path = ROOT / candidate
            if path.exists():
                sys.path.insert(0, str(path))
                try:
                    import yaml  # type: ignore

                    return yaml
                except ModuleNotFoundError:
                    continue
    raise


yaml = import_yaml()


@dataclass
class PageRecord:
    path: str
    slug: str
    category: str
    page_type: str
    parse_ok: bool
    parse_error: str
    source_count: int | None
    sources_list_count: int
    references_count: int
    missing_source_pages: list[str]
    non_slug_source_items: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit wiki/cosmos integrity without editing files.")
    parser.add_argument("--out-dir", default=str(WORKSPACE), help="Directory for CSV/JSON reports.")
    parser.add_argument(
        "--generated-cosmos",
        default=str(WORKSPACE / "cosmos_audit_data.json"),
        help="Optional freshly generated cosmos JSON to compare with current cosmos/data.json.",
    )
    return parser.parse_args()


def split_frontmatter(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text, "missing_frontmatter"
    return match.group(1), text[match.end():], ""


def parse_frontmatter_strict(path: Path) -> tuple[dict[str, Any], str, str]:
    fm, body, split_error = split_frontmatter(path)
    if split_error:
        return {}, body, split_error
    try:
        data = yaml.safe_load(fm) or {}
        if not isinstance(data, dict):
            return {}, body, "frontmatter_not_mapping"
        return data, body, ""
    except Exception as exc:
        return {}, body, str(exc).replace("\n", " ")[:500]


def as_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    text = str(value).strip()
    if text.isdigit():
        return int(text)
    return None


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value in (None, ""):
        return []
    return [value]


def extract_slug(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("page", "source", "target", "url", "title"):
            if key in value:
                return extract_slug(value[key])
        return ""
    text = str(value).strip()
    match = WIKILINK_RE.search(text)
    if match:
        text = match.group(1)
    text = text.replace("\\", "/").split("/")[-1]
    if text.endswith(".md"):
        text = text[:-3]
    return text.strip()


def extract_source_page_slug(value: Any) -> str:
    """Return a source-page slug only when the item is intended as a page link.

    Older operation pages sometimes store citation labels such as
    "[1] Al Jazeera (2024-06-28)" in frontmatter `sources`. Those labels are
    not resolvable source-page links, so they should not be counted as missing
    source pages. Wikilinks and slug-like strings are treated as link intents.
    """
    if isinstance(value, dict):
        for key in ("page", "source", "target", "slug"):
            if key in value:
                return extract_source_page_slug(value[key])
        return ""
    text = str(value).strip()
    match = WIKILINK_RE.search(text)
    if match:
        text = match.group(1)
    else:
        text = text.replace("\\", "/").split("/")[-1]
        if text.endswith(".md"):
            text = text[:-3]
        if not SLUG_RE.fullmatch(text):
            return ""
    text = text.replace("\\", "/").split("/")[-1]
    if text.endswith(".md"):
        text = text[:-3]
    return text.strip()


def count_references(body: str) -> int:
    if "## References" not in body:
        return 0
    tail = body.split("## References", 1)[1]
    next_section = re.search(r"^##\s+", tail, re.M)
    if next_section:
        tail = tail[: next_section.start()]
    return len(REF_ROW_RE.findall(tail))


def source_link_inventory(meta: dict[str, Any]) -> tuple[list[str], int]:
    slugs: list[str] = []
    non_slug_items = 0
    for item in as_list(meta.get("sources")):
        slug = extract_source_page_slug(item)
        if slug:
            slugs.append(slug)
        else:
            non_slug_items += 1
    return slugs, non_slug_items


def audit_pages() -> tuple[list[PageRecord], list[dict[str, Any]]]:
    source_pages = {path.stem for path in SOURCES_DIR.glob("*.md") if path.name != "_index.md"}
    pages: list[PageRecord] = []
    parse_errors: list[dict[str, Any]] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name in SKIP_MD:
            continue
        meta, body, error = parse_frontmatter_strict(path)
        rel = path.relative_to(ROOT).as_posix()
        category = path.parent.name if path.parent != WIKI_DIR else ""
        slugs, non_slug_source_items = source_link_inventory(meta) if not error else ([], 0)
        missing_sources = [slug for slug in slugs if slug not in source_pages]
        record = PageRecord(
            path=rel,
            slug=path.stem,
            category=category,
            page_type=str(meta.get("type") or ""),
            parse_ok=not bool(error),
            parse_error=error,
            source_count=as_int(meta.get("source_count")) if not error else None,
            sources_list_count=len(slugs),
            references_count=count_references(body),
            missing_source_pages=missing_sources,
            non_slug_source_items=non_slug_source_items,
        )
        pages.append(record)
        if error:
            parse_errors.append({"path": rel, "category": category, "error": error})
    return pages, parse_errors


def operation_index_slugs() -> set[str]:
    index_path = OPS_DIR / "_index.md"
    if not index_path.exists():
        return set()
    text = index_path.read_text(encoding="utf-8", errors="replace")
    return {match.group(1).strip() for match in INDEX_ROW_RE.finditer(text)}


def index_stats() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for category_dir in sorted(path for path in WIKI_DIR.iterdir() if path.is_dir()):
        category = category_dir.name
        files = {path.stem for path in category_dir.glob("*.md") if path.name not in SKIP_MD}
        index_path = category_dir / "_index.md"
        index_rows: set[str] = set()
        heading_count: int | None = None
        if index_path.exists():
            text = index_path.read_text(encoding="utf-8", errors="replace")
            index_rows = {match.group(1).strip() for match in INDEX_ROW_RE.finditer(text)}
            heading_match = INDEX_HEADING_COUNT_RE.search(text)
            if heading_match:
                heading_count = int(heading_match.group(1))
        docs_dir = DOCS_DIR / "wiki" / category
        docs_html_count = len([path for path in docs_dir.glob("*.html")]) if docs_dir.exists() else 0
        rows.append({
            "category": category,
            "wiki_files": len(files),
            "index_rows": len(index_rows),
            "heading_count": heading_count if heading_count is not None else "",
            "docs_html": docs_html_count,
            "files_missing_from_index": len(files - index_rows),
            "index_entries_missing_files": len(index_rows - files),
        })
    return rows


def docs_search_stats() -> dict[str, Any]:
    path = DOCS_DIR / "search-index.json"
    if not path.exists():
        return {"path": path.as_posix(), "exists": False}
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"path": path.as_posix(), "exists": True, "error": str(exc)}
    by_category = Counter(str(row.get("category") or "") for row in rows)
    by_type = Counter(str(row.get("type") or "") for row in rows)
    return {
        "path": path.as_posix(),
        "exists": True,
        "items": len(rows),
        "by_category": dict(sorted(by_category.items())),
        "by_type": dict(sorted(by_type.items())),
    }


def known_page_sets() -> tuple[set[str], set[str]]:
    stems: set[str] = set()
    category_slugs: set[str] = set()
    for path in WIKI_DIR.rglob("*.md"):
        if path.name in SKIP_MD:
            continue
        stems.add(path.stem)
        category = path.parent.name if path.parent != WIKI_DIR else ""
        if category:
            category_slugs.add(f"{category}/{path.stem}")
    return stems, category_slugs


def broken_wikilinks() -> list[dict[str, Any]]:
    stems, category_slugs = known_page_sets()
    rows: list[dict[str, Any]] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name in SKIP_MD:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").replace("\\|", "|")
        rel = path.relative_to(ROOT).as_posix()
        for match in WIKILINK_FULL_RE.finditer(text):
            target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if not target or target.endswith("_index") or target == "_index":
                continue
            normalized = target.strip("/")
            if normalized in category_slugs:
                continue
            slug = normalized.split("/")[-1]
            if slug not in stems:
                rows.append({"path": rel, "target": target, "slug": slug})
    return rows


def duplicate_slugs() -> list[dict[str, Any]]:
    by_slug: dict[str, list[str]] = {}
    for path in WIKI_DIR.rglob("*.md"):
        if path.name in SKIP_MD:
            continue
        by_slug.setdefault(path.stem, []).append(path.relative_to(ROOT).as_posix())
    return [
        {"slug": slug, "count": len(paths), "paths": ";".join(paths)}
        for slug, paths in sorted(by_slug.items())
        if len(paths) > 1
    ]


def load_cosmos(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def cosmos_stats(path: Path) -> dict[str, Any]:
    data = load_cosmos(path)
    if not data:
        return {"path": path.as_posix(), "exists": False}
    nodes = data.get("nodes") or []
    by_type = Counter(str(node.get("type") or "") for node in nodes)
    return {
        "path": path.as_posix(),
        "exists": True,
        "generated_at": data.get("generated_at"),
        "nodes": len(nodes),
        "edges": len(data.get("edges") or []),
        "broken_links": len(data.get("broken_links") or []),
        "orphans": (data.get("stats") or {}).get("orphans"),
        "by_type": dict(sorted(by_type.items())),
    }


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pages, parse_errors = audit_pages()
    operations = [row for row in pages if row.category == "operations"]
    operation_files = {path.stem for path in OPS_DIR.glob("*.md") if path.name != "_index.md"}
    index_slugs = operation_index_slugs()

    source_mismatches: list[dict[str, Any]] = []
    missing_source_pages: list[dict[str, Any]] = []
    for row in operations:
        reasons: list[str] = []
        if not row.parse_ok:
            reasons.append("parse_error")
        else:
            if row.source_count is None:
                reasons.append("missing_source_count")
            if row.source_count is not None and row.sources_list_count and row.source_count != row.sources_list_count:
                reasons.append("source_count_vs_sources_list")
            if row.source_count is not None and row.references_count and row.source_count != row.references_count:
                reasons.append("source_count_vs_references")
            if row.sources_list_count and row.references_count and row.sources_list_count != row.references_count:
                reasons.append("sources_list_vs_references")
            if row.source_count and row.references_count == 0:
                reasons.append("missing_visible_references")
        if reasons:
            source_mismatches.append({
                "slug": row.slug,
                "path": row.path,
                "source_count": row.source_count if row.source_count is not None else "",
                "sources_list_count": row.sources_list_count,
                "references_count": row.references_count,
                "reasons": ";".join(reasons),
                "parse_error": row.parse_error,
            })
        for slug in row.missing_source_pages:
            missing_source_pages.append({"operation": row.slug, "path": row.path, "missing_source": slug})

    index_rows = index_stats()
    broken_links = broken_wikilinks()
    duplicate_slug_rows = duplicate_slugs()

    index_report = {
        "operation_file_count": len(operation_files),
        "operation_index_count": len(index_slugs),
        "parsed_operation_count": sum(1 for row in operations if row.parse_ok and row.page_type == "operation"),
        "files_missing_from_index": sorted(operation_files - index_slugs),
        "index_entries_missing_files": sorted(index_slugs - operation_files),
    }

    summary = {
        "wiki_file_count": len(pages),
        "by_category": dict(sorted(Counter(row.category for row in pages).items())),
        "by_type": dict(sorted(Counter(row.page_type for row in pages if row.page_type).items())),
        "parse_error_count": len(parse_errors),
        "operation": {
            **index_report,
            "source_mismatch_count": len(source_mismatches),
            "missing_source_page_links": len(missing_source_pages),
            "non_slug_source_items": sum(row.non_slug_source_items for row in operations),
            "source_mismatch_reason_counts": dict(sorted(Counter(
                reason
                for row in source_mismatches
                for reason in str(row["reasons"]).split(";")
                if reason
            ).items())),
        },
        "category_indexes": index_rows,
        "docs_search_index": docs_search_stats(),
        "cosmos_current": cosmos_stats(ROOT / "cosmos" / "data.json"),
        "docs_cosmos_current": cosmos_stats(ROOT / "docs" / "cosmos" / "data.json"),
        "cosmos_generated": cosmos_stats(Path(args.generated_cosmos)),
        "broken_wikilink_count": len(broken_links),
        "duplicate_slug_count": len(duplicate_slug_rows),
    }

    write_csv(
        out_dir / "integrity_parse_errors.csv",
        parse_errors,
        ["path", "category", "error"],
    )
    write_csv(
        out_dir / "integrity_operation_source_mismatches.csv",
        source_mismatches,
        ["slug", "path", "source_count", "sources_list_count", "references_count", "reasons", "parse_error"],
    )
    write_csv(
        out_dir / "integrity_missing_source_pages.csv",
        missing_source_pages,
        ["operation", "path", "missing_source"],
    )
    write_csv(
        out_dir / "integrity_operation_index_gaps.csv",
        (
            [{"kind": "file_missing_from_index", "slug": slug} for slug in index_report["files_missing_from_index"]]
            + [{"kind": "index_entry_missing_file", "slug": slug} for slug in index_report["index_entries_missing_files"]]
        ),
        ["kind", "slug"],
    )
    write_csv(
        out_dir / "integrity_category_indexes.csv",
        index_rows,
        [
            "category",
            "wiki_files",
            "index_rows",
            "heading_count",
            "docs_html",
            "files_missing_from_index",
            "index_entries_missing_files",
        ],
    )
    write_csv(
        out_dir / "integrity_broken_wikilinks.csv",
        broken_links,
        ["path", "target", "slug"],
    )
    write_csv(
        out_dir / "integrity_duplicate_slugs.csv",
        duplicate_slug_rows,
        ["slug", "count", "paths"],
    )
    (out_dir / "integrity_audit_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("tools/audit_integrity.py")
    print(f"  wiki files audited: {summary['wiki_file_count']}")
    print(f"  parse errors: {summary['parse_error_count']}")
    print(f"  operation files: {index_report['operation_file_count']}")
    print(f"  operation index rows: {index_report['operation_index_count']}")
    print(f"  parsed operations: {index_report['parsed_operation_count']}")
    print(f"  operation source mismatches: {len(source_mismatches)}")
    print(f"  missing source-page links from operations: {len(missing_source_pages)}")
    print(f"  broken wikilinks: {len(broken_links)}")
    print(f"  duplicate slugs: {len(duplicate_slug_rows)}")
    print(f"  summary: {(out_dir / 'integrity_audit_summary.json').as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
