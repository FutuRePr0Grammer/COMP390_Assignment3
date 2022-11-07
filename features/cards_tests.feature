Feature: testing all deck of cards classes
  Scenario: test that a card is created correctly
    Given I have created a new card object
    When I create the new class
    Then the suit and value of the card should be recorded

    Scenario: test that a deck of cards is created correctly
      Given I have a deck of cards
      When I create the new class
      Then the deck object should contain a number of cards equal to the deck size

      Scenario: shuffling a deck changes the order
        Given I have a deck of cards
        When I shuffle them
        Then the order has changed

      Scenario: drawing a card removes it from the deck
      Given I have a deck of cards
      When I draw a card
      Then It is removed from the stack