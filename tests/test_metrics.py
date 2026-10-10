import pytest
from greenspace.metrics import coverage_fraction


def test_coverage_fraction():
    assert coverage_fraction(3, 4) == 0.75


def test_empty_population():
    assert coverage_fraction(0, 0) == 0.0


def test_invalid_counts():
    with pytest.raises(ValueError):
        coverage_fraction(5, 4)
