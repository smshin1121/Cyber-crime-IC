from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


@dataclass
class Post:
    metadata: dict[str, Any] = field(default_factory=dict)
    content: str = ""


def load(path: str | Path) -> Post:
    text = Path(path).read_text(encoding="utf-8")
    match = _FM_RE.match(text)
    if not match:
        return Post({}, text)
    metadata = _parse_mapping(match.group(1).splitlines())
    content = text[match.end():]
    return Post(metadata, content)


def dumps(post: Post) -> str:
    metadata = _dump_mapping(post.metadata).rstrip()
    content = post.content or ""
    return f"---\n{metadata}\n---\n{content}"


def _parse_mapping(lines: list[str], base_indent: int = 0) -> dict[str, Any]:
    data: dict[str, Any] = {}
    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue
        indent = _indent(raw)
        if indent < base_indent:
            break
        if indent > base_indent:
            i += 1
            continue
        stripped = raw.strip()
        if stripped.startswith("- "):
            i += 1
            continue
        if ":" not in stripped:
            i += 1
            continue
        key, rest = stripped.split(":", 1)
        rest = rest.strip()
        if rest:
            data[key] = _parse_scalar(rest)
            i += 1
            continue

        block, next_i = _collect_block(lines, i + 1, base_indent, allow_same_indent_list=True)
        if not block:
            data[key] = ""
        elif block[0].strip().startswith("- "):
            data[key] = _parse_list(block, _indent(block[0]))
        else:
            data[key] = _parse_mapping(block, base_indent + 2)
        i = next_i
    return data


def _parse_list(lines: list[str], base_indent: int) -> list[Any]:
    items: list[Any] = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip():
            i += 1
            continue
        indent = _indent(raw)
        if indent < base_indent:
            break
        stripped = raw.strip()
        if not stripped.startswith("- "):
            i += 1
            continue

        item_text = stripped[2:].strip()
        block, next_i = _collect_block(lines, i + 1, indent, allow_same_indent_list=False)
        if item_text == "":
            if block and block[0].strip().startswith("- "):
                items.append(_parse_list(block, indent + 2))
            else:
                items.append(_parse_mapping(block, indent + 2))
            i = next_i
            continue

        if _is_quoted_scalar(item_text):
            items.append(_parse_scalar(item_text))
            i = next_i
            continue

        if ":" in item_text and not item_text.startswith(("http://", "https://")):
            key, rest = item_text.split(":", 1)
            rest = rest.strip()
            if rest:
                item: dict[str, Any] = {key: _parse_scalar(rest)}
            else:
                item = {key: ""}
            if block:
                nested = _parse_mapping(block, indent + 2)
                item.update(nested)
            items.append(item)
        else:
            items.append(_parse_scalar(item_text))
        i = next_i
    return items


def _is_quoted_scalar(value: str) -> bool:
    if len(value) < 2:
        return False
    return (value[0] == value[-1] == '"') or (value[0] == value[-1] == "'")


def _collect_block(
    lines: list[str],
    start: int,
    parent_indent: int,
    allow_same_indent_list: bool,
) -> tuple[list[str], int]:
    block: list[str] = []
    i = start
    while i < len(lines):
        raw = lines[i]
        if not raw.strip():
            block.append(raw)
            i += 1
            continue
        indent = _indent(raw)
        stripped = raw.strip()
        if allow_same_indent_list and indent == parent_indent and stripped.startswith("- "):
            block.append(raw)
            i += 1
            continue
        if indent <= parent_indent:
            break
        block.append(raw)
        i += 1
    return block, i


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        try:
            return json.loads(value)
        except Exception:
            return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(part.strip()) for part in inner.split(",")]

    low = value.lower()
    if low == "true":
        return True
    if low == "false":
        return False
    if low in {"null", "none"}:
        return None
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            pass
    if re.fullmatch(r"-?\d+\.\d+", value):
        try:
            return float(value)
        except ValueError:
            pass
    return value


def _dump_mapping(data: dict[str, Any], indent: int = 0) -> str:
    lines: list[str] = []
    pad = " " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{key}:")
            lines.append(_dump_mapping(value, indent + 2))
        elif isinstance(value, list):
            lines.append(f"{pad}{key}:")
            lines.extend(_dump_list(value, indent + 2))
        else:
            lines.append(f"{pad}{key}: {_dump_scalar(value)}")
    return "\n".join(lines)


def _dump_list(items: list[Any], indent: int) -> list[str]:
    lines: list[str] = []
    pad = " " * indent
    for item in items:
        if isinstance(item, dict):
            entries = list(item.items())
            if not entries:
                lines.append(f"{pad}- {{}}")
                continue
            first_key, first_value = entries[0]
            if isinstance(first_value, (dict, list)):
                lines.append(f"{pad}- {first_key}:")
                lines.extend(_dump_complex(first_value, indent + 4))
            else:
                lines.append(f"{pad}- {first_key}: {_dump_scalar(first_value)}")
            for key, value in entries[1:]:
                if isinstance(value, (dict, list)):
                    lines.append(f"{pad}  {key}:")
                    lines.extend(_dump_complex(value, indent + 4))
                else:
                    lines.append(f"{pad}  {key}: {_dump_scalar(value)}")
        elif isinstance(item, list):
            lines.append(f"{pad}-")
            lines.extend(_dump_list(item, indent + 2))
        else:
            lines.append(f"{pad}- {_dump_scalar(item)}")
    if not lines:
        lines.append(f"{pad}[]")
    return lines


def _dump_complex(value: Any, indent: int) -> list[str]:
    if isinstance(value, dict):
        return _dump_mapping(value, indent).splitlines()
    if isinstance(value, list):
        return _dump_list(value, indent)
    return [(" " * indent) + _dump_scalar(value)]


def _dump_scalar(value: Any) -> str:
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    if re.fullmatch(r"[A-Za-z0-9_./:+-]+", text):
        return text
    return json.dumps(text, ensure_ascii=False)
