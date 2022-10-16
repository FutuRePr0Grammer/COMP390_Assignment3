import random


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
    pass



