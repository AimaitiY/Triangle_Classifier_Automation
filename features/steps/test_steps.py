# features/steps/test_steps.py

from pytest_bdd import scenarios, given, when, then
from src.triangle_classifier import classify_triangle
import sys
import pytest

scenarios('../triangle_classifier.feature')

@given('I input "<input_string>"')
def input_string(input_string):
    return input_string

@when('I run the Triangle Classifier')
def run_classifier(input_string):
    if input_string.lower() in ["exit", "quit"]:
        with pytest.raises(SystemExit):
            classify_triangle(input_string)
    else:
        return classify_triangle(input_string)

@then('the output should be "<expected_output>"')
def verify_output(run_classifier, expected_output):
    assert run_classifier == expected_output

@then('the application should exit')
def application_exit():
    pass  # Handled in the 'when' step
