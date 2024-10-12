# tests/conftest.py

import pytest
from src.triangle_classifier import classify_triangle

@pytest.fixture
def triangle_classifier():
    return classify_triangle
