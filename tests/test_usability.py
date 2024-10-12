# tests/test_usability.py

import pytest

@pytest.mark.usability
def test_clear_error_message(triangle_classifier):
    assert triangle_classifier("1 two three") == "Error: Invalid input"

@pytest.mark.usability
def test_empty_input(triangle_classifier):
    assert triangle_classifier("") == "Error: No input provided"
