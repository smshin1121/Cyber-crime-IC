"""Shared helpers for operation record scope.

The repository keeps two different kinds of operation records:

* canonical_operation: umbrella or standalone international-cooperation operations
* absorbed_follow_on: follow-on DOJ/prosecution/action records retained for traceability

Absorbed records should remain linkable, but default statistics and map/globe
views should not count them as separate IC operations.
"""
from __future__ import annotations

from typing import Any


ABSORBED_STATUS = "absorbed"
CANONICAL_SCOPE = "canonical_operation"
ABSORBED_SCOPE = "absorbed_follow_on"


def _norm(value: Any) -> str:
    return str(value or "").strip().lower()


def is_absorbed_operation(meta: dict[str, Any] | None) -> bool:
    """Return True when an operation page is a retained follow-on wrapper."""
    if not meta:
        return False
    return _norm(meta.get("status")) == ABSORBED_STATUS


def operation_scope(meta: dict[str, Any] | None) -> str:
    """Return the canonical scope label used by web, stats, and cosmos."""
    return ABSORBED_SCOPE if is_absorbed_operation(meta) else CANONICAL_SCOPE


def operation_scope_label(meta: dict[str, Any] | None) -> str:
    """Human-readable English label for operation scope."""
    return "Absorbed Follow-On" if is_absorbed_operation(meta) else "Canonical Operation"
