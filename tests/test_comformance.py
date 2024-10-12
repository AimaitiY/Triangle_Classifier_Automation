# tests/test_conformance.py

import pytest

@pytest.mark.conformance
def test_equilateral(triangle_classifier):
    assert triangle_classifier("1 1 1") == "Equilateral"

@pytest.mark.conformance
def test_isosceles(triangle_classifier):
    assert triangle_classifier("2 2 3") == "Isosceles"

@pytest.mark.conformance
def test_scalene(triangle_classifier):
    assert triangle_classifier("3 4 5") == "Scalene"

@pytest.mark.conformance
def test_no_triangle(triangle_classifier):
    assert triangle_classifier("1 2 3") == "NoTriangle"

@pytest.mark.conformance
def test_invalid_sides(triangle_classifier):
    assert triangle_classifier("1 1 0") == "Error: Invalid sides"
