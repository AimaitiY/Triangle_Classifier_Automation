# tests/test_reliability.py

import pytest

@pytest.mark.reliability
def test_high_volume_repetition(triangle_classifier):
    for _ in range(1000):
        assert triangle_classifier("1 1 1") == "Equilateral"
