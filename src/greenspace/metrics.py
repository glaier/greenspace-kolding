"""Simple, unit-tested coverage calculations (not GIS network analysis)."""


def coverage_fraction(covered: int, total: int) -> float:
    """Return covered / total, with an explicit empty-population convention."""
    if total < 0 or covered < 0 or covered > total:
        raise ValueError("Require 0 <= covered <= total")
    return 0.0 if total == 0 else covered / total
