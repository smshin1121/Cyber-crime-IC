from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_ROOT_MODULE = Path(__file__).resolve().parent.parent / "frontmatter.py"
_SPEC = importlib.util.spec_from_file_location("_codex_frontmatter", _ROOT_MODULE)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Unable to load frontmatter shim from {_ROOT_MODULE}")
_MODULE = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _MODULE
_SPEC.loader.exec_module(_MODULE)

Post = _MODULE.Post
load = _MODULE.load
dumps = _MODULE.dumps
