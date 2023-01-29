# Created by a.padlo at 10.12.2021
Feature: GitHub API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200