# tests/test_performance.py

import pytest
import time

@pytest.mark.performance
def test_repeated_valid_inputs(triangle_classifier):
    start_time = time.time()
    for _ in range(1000):
        assert triangle_classifier("3 4 5") == "Scalene"
    end_time = time.time()
    assert (end_time - start_time) < 2  # Example threshold

@pytest.mark.performance
def test_large_input_string(triangle_classifier):
    large_input = " ".join(["3" for _ in range(1000)])
    assert triangle_classifier(large_input) == "Error: Invalid number of sides"
