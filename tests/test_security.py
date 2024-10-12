# tests/test_security.py

import pytest

@pytest.mark.security
def test_sql_injection(triangle_classifier):
    assert triangle_classifier("1; DROP TABLE users;") == "Error: Invalid number of sides"

@pytest.mark.security
def test_large_numbers(triangle_classifier):
    large_number = "100000000000000000000000000 100000000000000000000000000 100000000000000000000000000"
    assert triangle_classifier(large_number) == "Equilateral"
