# Created by a.padlo at 28.11.2021
Feature: Verify if Books are added and deleted using library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which need to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle> need to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
      Examples:
        | isbn |  aisle |
        | fdefe | 124   |
        | dsfgh | 8396  |
