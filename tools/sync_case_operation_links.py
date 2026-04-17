from __future__ import annotations

from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
CASES_DIR = ROOT / "wiki" / "cases"
OPS_DIR = ROOT / "wiki" / "operations"


def wikilink_slug(value: str) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        inner = text[2:-2]
        return inner.split("|", 1)[0].strip()
    return text


def wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def ensure_list(value) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value]
    return []


def unique_append(items: list[str], value: str) -> list[str]:
    if value not in items:
        items.append(value)
    return items


def main() -> None:
    changed = 0
    op_slugs = {p.stem for p in OPS_DIR.glob("*.md") if not p.name.startswith("_")}

    for case_path in sorted(CASES_DIR.glob("*.md")):
        if case_path.name.startswith("_"):
            continue

        case_post = frontmatter.load(case_path)
        case_meta = case_post.metadata
        case_slug = case_path.stem
        follow_on_slug = f"operation-{case_slug}"
        if follow_on_slug not in op_slugs:
            continue

        parent_slug = wikilink_slug(case_meta.get("related_operation"))

        case_changed = False
        if not parent_slug:
            case_meta["related_operation"] = wikilink(follow_on_slug)
            parent_slug = follow_on_slug
            case_changed = True

        if case_changed:
            case_path.write_text(frontmatter.dumps(case_post), encoding="utf-8")
            changed += 1

        follow_on_path = OPS_DIR / f"{follow_on_slug}.md"
        follow_on_post = frontmatter.load(follow_on_path)
        follow_on_meta = follow_on_post.metadata
        follow_on_changed = False

        related_cases = ensure_list(follow_on_meta.get("related_cases"))
        if wikilink(case_slug) not in related_cases:
            follow_on_meta["related_cases"] = unique_append(related_cases, wikilink(case_slug))
            follow_on_changed = True

        related_ops = ensure_list(follow_on_meta.get("related_operations"))
        if parent_slug and parent_slug != follow_on_slug and parent_slug in op_slugs:
            if wikilink(parent_slug) not in related_ops:
                follow_on_meta["related_operations"] = unique_append(related_ops, wikilink(parent_slug))
                follow_on_changed = True

            parent_path = OPS_DIR / f"{parent_slug}.md"
            parent_post = frontmatter.load(parent_path)
            parent_meta = parent_post.metadata
            parent_changed = False

            parent_related_ops = ensure_list(parent_meta.get("related_operations"))
            if wikilink(follow_on_slug) not in parent_related_ops:
                parent_meta["related_operations"] = unique_append(parent_related_ops, wikilink(follow_on_slug))
                parent_changed = True

            parent_related_cases = ensure_list(parent_meta.get("related_cases"))
            if wikilink(case_slug) not in parent_related_cases:
                parent_meta["related_cases"] = unique_append(parent_related_cases, wikilink(case_slug))
                parent_changed = True

            if parent_changed:
                parent_path.write_text(frontmatter.dumps(parent_post), encoding="utf-8")
                changed += 1

        if follow_on_changed:
            follow_on_path.write_text(frontmatter.dumps(follow_on_post), encoding="utf-8")
            changed += 1

    print(f"Updated {changed} pages.")


if __name__ == "__main__":
    main()
