from __future__ import annotations

import importlib.machinery
import importlib.util
import site
import sys
from pathlib import Path

_ROOT_MODULE = Path(__file__).resolve().parent.parent / "frontmatter.py"


def _load_root_shim():
    spec = importlib.util.spec_from_file_location("_codex_frontmatter", _ROOT_MODULE)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load frontmatter shim from {_ROOT_MODULE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _load_installed_package():
    search_path = []
    for candidate in site.getsitepackages():
        if candidate:
            search_path.append(candidate)
    user_site = site.getusersitepackages()
    if user_site:
        search_path.append(user_site)
    spec = importlib.machinery.PathFinder.find_spec("frontmatter", search_path)
    if spec is None or spec.loader is None:
        raise ImportError("python-frontmatter package is not available")
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("_vendor_frontmatter", module)
    spec.loader.exec_module(module)
    return module


if _ROOT_MODULE.exists():
    _MODULE = _load_root_shim()
else:
    _MODULE = _load_installed_package()

Post = _MODULE.Post
load = _MODULE.load
dumps = _MODULE.dumps
