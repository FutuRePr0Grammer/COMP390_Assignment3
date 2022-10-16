import random


# global variable to hold the deck size (52 cards)
DECK_SIZE = 52


# class to determine the suit of the card being created
class Suit:
    suit = None

    def __init__(self, suit):
        self.suit = suit


# class to determine the value (number) for the card being created
class CardValue:
    value = None

    def __init__(self, value):
        self.value = value


# will create a card with a suit and a number
class Card:
    suit = None
    value = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # will make sure doesn't print the address of each card object
    def __str__(self):
        return 'Suit: {}, Value = {}'.format(self.suit, self.value)


# will create 52 cards and store them in a data structure
# will also shuffle cards and pull the top card on each call
class Deck:
    card = None

    def __init__(self, suit, value):
        self.card = []

        # creates a deck of 52 cards of different suits and values
        for index in range(0, DECK_SIZE + 1):
            new_card = Card(Suit(suit), CardValue(value))
            self.add(new_card)

    # prints the deck
    def print_deck(self):
        for card in self.card:
            print(card)

    # adds card to the deck
    def add(self, card):
        self.card.append(card)



# test code to print the deck of cards
deck = Deck("Hearts", 7)

