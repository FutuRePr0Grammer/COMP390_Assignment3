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
        return 'Suit: {}, Value : {}'.format(self.suit, self.value)


# will create 52 cards and store them in a data structure
# will also shuffle cards and pull the top card on each call
class Deck:
    card = None

    def __init__(self):
        self.card = []

        # creates a deck of 52 cards of different suits and values
        """
        for index in range(0, DECK_SIZE + 1):
            new_card = Card(Suit("Hearts"), CardValue(6))
            self.add(new_card)
        """
        for index in range(0, (DECK_SIZE / 4) + 1):
            if index == 11:
                new_card = Card(Suit("Hearts"), CardValue("Jack"))
                self.add(new_card)
            elif index == 12:
                new_card = Card(Suit("Hearts"), CardValue("Queen"))
                self.add(new_card)
            elif index == 13:
                new_card = Card(Suit("Hearts"), CardValue("King"))
                self.add(new_card)
            else:
                new_card = Card(Suit("Hearts"), CardValue(index))
                self.add(new_card)

        for index in range((DECK_SIZE / 4) + 1, 2 * (DECK_SIZE / 4) + 1):
            if index == 11:
                new_card = Card(Suit("Diamonds"), CardValue("Jack"))
                self.add(new_card)
            elif index == 12:
                new_card = Card(Suit("Diamonds"), CardValue("Queen"))
                self.add(new_card)
            elif index == 13:
                new_card = Card(Suit("Diamonds"), CardValue("King"))
                self.add(new_card)
            else:
                new_card = Card(Suit("Diamonds"), CardValue(index))
                self.add(new_card)

        for index in range(2 * (DECK_SIZE / 4) + 1, 3 * (DECK_SIZE / 4) + 1):
            if index == 11:
                new_card = Card(Suit("Aces"), CardValue("Jack"))
                self.add(new_card)
            elif index == 12:
                new_card = Card(Suit("Aces"), CardValue("Queen"))
                self.add(new_card)
            elif index == 13:
                new_card = Card(Suit("Aces"), CardValue("King"))
                self.add(new_card)
            else:
                new_card = Card(Suit("Aces"), CardValue(index))
                self.add(new_card)

        for index in range(3 * (DECK_SIZE / 4) + 1, DECK_SIZE + 1):
            if index == 11:
                new_card = Card(Suit("Clubs"), CardValue("Jack"))
                self.add(new_card)
            elif index == 12:
                new_card = Card(Suit("Clubs"), CardValue("Queen"))
                self.add(new_card)
            elif index == 13:
                new_card = Card(Suit("Clubs"), CardValue("King"))
                self.add(new_card)
            else:
                new_card = Card(Suit("Clubs"), CardValue(index))
                self.add(new_card)

    # prints the deck
    def print_deck(self):
        for card in self.card:
            print(card)

    # adds card to the deck
    def add(self, card):
        self.card.append(card)



# test code to print the deck of cards
deck = Deck()
deck.print_deck()

