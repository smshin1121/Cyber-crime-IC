"""
Credibility Index (CI) Calculator
연구 계획서 Section 5.3의 공식을 구현.
CI = (source_count_score × 0.3) + (max_source_tier_score × 0.4) + (source_diversity_score × 0.3)
"""
from __future__ import annotations


def source_count_score(count: int) -> float:
    """Normalize source count to 0-5 scale."""
    if count <= 0:
        return 0.0
    if count == 1:
        return 1.25
    if count <= 3:
        return 2.50
    if count <= 6:
        return 3.75
    return 5.0


def max_tier_score(best_tier: int) -> float:
    """Score based on highest-tier source (1=best, 4=lowest)."""
    return {1: 5.0, 2: 4.0, 3: 3.0, 4: 2.0}.get(best_tier, 0.0)


def diversity_score(distinct_types: int) -> float:
    """Score based on number of distinct source types."""
    return min(float(distinct_types), 5.0)


def calculate_ci(
    num_sources: int,
    best_tier: int,
    num_distinct_types: int,
) -> float:
    """
    Calculate Credibility Index.

    Args:
        num_sources: Number of independent sources covering the case
        best_tier: Highest (lowest number) source tier available (1-4)
        num_distinct_types: Number of distinct source type categories

    Returns:
        CI score (approximately 0.6 to 5.0)
    """
    sc = source_count_score(num_sources)
    mt = max_tier_score(best_tier)
    ds = diversity_score(num_distinct_types)
    return round(sc * 0.3 + mt * 0.4 + ds * 0.3, 2)


def time_weight(hours_since_event: float) -> float:
    """Time-based weighting for source reliability."""
    if hours_since_event <= 24:
        return 0.7
    if hours_since_event <= 168:  # 1 week
        return 0.85
    return 1.0


def interpret_ci(ci: float) -> str:
    """Interpret CI score as verdict."""
    if ci >= 2.0:
        return "INCLUDE"
    if ci >= 1.0:
        return "REVIEW"
    return "EXCLUDE"


if __name__ == "__main__":
    # Test cases
    tests = [
        {"name": "Europol press release only", "sources": 1, "tier": 2, "types": 1},
        {"name": "Europol + INTERPOL + news", "sources": 3, "tier": 2, "types": 2},
        {"name": "Court filing + agency + media", "sources": 4, "tier": 1, "types": 3},
        {"name": "Single blog post", "sources": 1, "tier": 4, "types": 1},
    ]
    print("CI Calculator Test")
    print("=" * 70)
    for t in tests:
        ci = calculate_ci(t["sources"], t["tier"], t["types"])
        verdict = interpret_ci(ci)
        print(f"{t['name']:40s} CI={ci:.2f} → {verdict}")
