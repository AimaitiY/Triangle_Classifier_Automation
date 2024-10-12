Feature: Triangle Classifier

  Scenario: Classify Equilateral Triangle
    Given I input "1 1 1"
    When I run the Triangle Classifier
    Then the output should be "Equilateral"

  Scenario: Classify Isosceles Triangle
    Given I input "2 2 3"
    When I run the Triangle Classifier
    Then the output should be "Isosceles"

  Scenario: Classify Scalene Triangle
    Given I input "3 4 5"
    When I run the Triangle Classifier
    Then the output should be "Scalene"

  Scenario: Classify NoTriangle
    Given I input "1 2 3"
    When I run the Triangle Classifier
    Then the output should be "NoTriangle"

  Scenario: Invalid Input
    Given I input "1 two 3"
    When I run the Triangle Classifier
    Then the output should be "Error: Invalid input"
