# tests/test_error_handling.py

import pytest

@pytest.mark.error_handling
def test_missing_two_sides(triangle_classifier):
    assert triangle_classifier("1") == "Error: Two sides missing"

@pytest.mark.error_handling
def test_missing_one_side(triangle_classifier):
    assert triangle_classifier("1 1") == "Error: One side missing"

@pytest.mark.error_handling
def test_non_numeric_input(triangle_classifier):
    assert triangle_classifier("1 two 3") == "Error: Invalid input"

@pytest.mark.error_handling
def test_zero_sides(triangle_classifier):
    assert triangle_classifier("0 0 0") == "Error: Invalid sides"

@pytest.mark.error_handling
def test_exit_command(triangle_classifier, capsys):
    with pytest.raises(SystemExit):
        triangle_classifier("Quit")
