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

        # integer division = //, prevents float division with /
        # print((DECK_SIZE // 4) + 1)

        # the below functionality prints object addresses
        """
        for index in range(0, (DECK_SIZE // 4) + 1):
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

        for index in range((DECK_SIZE // 4) + 1, 2 * (DECK_SIZE // 4) + 1):
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

        for index in range(2 * (DECK_SIZE // 4) + 1, 3 * (DECK_SIZE // 4) + 1):
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

        for index in range(3 * (DECK_SIZE // 4) + 1, DECK_SIZE + 1):
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
        """
        # below works, prints values.
        # TODO: Fix this mess below. Messy, indexes hardcoded, none of classes used
        for index in range(1, (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Hearts", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Hearts", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Hearts", "King")
                self.add(new_card)
            else:
                new_card = Card("Hearts", index)
                self.add(new_card)

        for index in range(1, (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Diamonds", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Diamonds", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Diamonds", "King")
                self.add(new_card)
            else:
                new_card = Card("Diamonds", index)
                self.add(new_card)

        for index in range(1, (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Spades", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Spades", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Spades", "King")
                self.add(new_card)
            else:
                new_card = Card("Spades", index)
                self.add(new_card)

        for index in range(1, (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Clubs", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Clubs", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Clubs", "King")
                self.add(new_card)
            else:
                new_card = Card("Clubs", index)
                self.add(new_card)

        """
        for index in range(1, (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Hearts", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Hearts", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Hearts", "King")
                self.add(new_card)
            else:
                new_card = Card("Hearts", index)
                self.add(new_card)

        for index in range((DECK_SIZE // 4) + 1, 2 * (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Diamonds", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Diamonds", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Diamonds", "King")
                self.add(new_card)
            else:
                new_card = Card("Diamonds", index)
                self.add(new_card)

        for index in range(2 * (DECK_SIZE // 4) + 1, 3 * (DECK_SIZE // 4) + 1):
            if index == 11:
                new_card = Card("Aces", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Aces", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Aces", "King")
                self.add(new_card)
            else:
                new_card = Card("Aces", index)
                self.add(new_card)

        for index in range(3 * (DECK_SIZE // 4) + 1, DECK_SIZE + 1):
            if index == 11:
                new_card = Card("Clubs", "Jack")
                self.add(new_card)
            elif index == 12:
                new_card = Card("Clubs", "Queen")
                self.add(new_card)
            elif index == 13:
                new_card = Card("Clubs", "King")
                self.add(new_card)
            else:
                new_card = Card("Clubs", index)
                self.add(new_card)
        """

    # prints the deck
    def print_deck(self):
        for card in self.card:
            print(card)

    # adds card to the deck
    def add(self, card):
        self.card.append(card)

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.card)

    # get the top card
    def get_top_card(self):
        top_card = self.card[0]
        print("The Top Card is: {}".format(self.card[0]))
        self.card.remove(self.card[0])
        return top_card


# test code to print the deck of cards, shuffle, and get top card
print("Before Shuffling Deck")
print()
deck = Deck()
deck.print_deck()
print()
print("After Shuffling Deck")
print()
deck.shuffle()
deck.print_deck()
print()
print("Getting Top Card")
print()
top_card = deck.get_top_card()
print("Testing top card was actually stored correctly")
print("TOP CARD: {}".format(top_card))
top_card = deck.get_top_card()
print("TOP CARD: {}".format(top_card))




