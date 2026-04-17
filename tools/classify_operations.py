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


def main() -> None:
    case_to_parent: dict[str, str] = {}
    for case_path in sorted(CASES_DIR.glob("*.md")):
        if case_path.name.startswith("_"):
            continue
        case_post = frontmatter.load(case_path)
        parent = wikilink_slug(case_post.metadata.get("related_operation"))
        case_to_parent[case_path.stem] = parent

    changed = 0
    for op_path in sorted(OPS_DIR.glob("*.md")):
        if op_path.name.startswith("_"):
            continue

        op_post = frontmatter.load(op_path)
        meta = op_post.metadata
        slug = op_path.stem

        role = "umbrella"
        parent = ""
        if slug.startswith("operation-"):
            case_slug = slug[len("operation-") :]
            if case_slug in case_to_parent:
                role = "follow-on"
                candidate = case_to_parent.get(case_slug, "")
                if candidate and candidate != slug:
                    parent = wikilink(candidate)

        old_role = meta.get("operation_role")
        old_parent = str(meta.get("parent_operation") or "")
        if old_role == role and old_parent == parent:
            continue

        meta["operation_role"] = role
        meta["parent_operation"] = parent
        op_path.write_text(frontmatter.dumps(op_post), encoding="utf-8")
        changed += 1

    print(f"Updated {changed} operation pages.")


if __name__ == "__main__":
    main()
