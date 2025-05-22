Feature: Calculator operations

  Scenario: Addition
    Given I have numbers 1, 4 and 5
    When I add the numbers
    Then the result should be 10

  Scenario: Subtraction
    Given I have numbers 5, 3 and 2
    When I subtract the numbers
    Then the result should be 0

  Scenario: Multiplication
    Given I have numbers 1, 4 and 5
    When I multiply the numbers
    Then the result should be 20

  Scenario: Division
    Given I have numbers 1, 4 and 5
    When I divide the numbers
    Then the result should be 0.05
