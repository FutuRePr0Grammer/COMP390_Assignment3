from behave import *
import cards


# To run these tests, type "behave" in the terminal below in the IDE


@Given('I have created a new card object')
def step_impl(context):
    pass


@When('I create the new class')
def step_impl(context):
    new_card = cards.Card('Clubs', 7)
    context.suit = new_card.suit
    context.value = new_card.value
    assert new_card is not None


@Then('the suit and value of the card should be recorded')
def step_impl(context):
    assert context.suit == 'Clubs'
    assert context.value == 7


@Given('I have a deck of cards')
def step_impl(context):
    context.new_deck = cards.Deck()
    assert context.new_deck is not None


@Then('the deck object should contain a number of cards equal to the deck size')
def step_impl(context):
    context.DECK_SIZE = 52
    # card here is the array card[] from the Deck class
    assert len(context.new_deck.card) == context.DECK_SIZE


@When('I draw a card')
def step_impl(context):
    context.number_of_cards = len(context.new_deck.card)
    context.drawn_card = context.new_deck.get_top_card()
    assert context.drawn_card is not None
    assert context.number_of_cards is not None


@Then('It is removed from the stack')
def step_impl(context):
    assert len(context.new_deck.card) < context.number_of_cards
    assert context.drawn_card not in context.new_deck.card


@When('I shuffle them')
def step_impl(context):
    context.original_deck = context.new_deck.card[0:]
    context.new_deck.shuffle()
    context.shuffled_deck = context.new_deck.card[0:]
    assert context.shuffled_deck is not None


@Then('the order has changed')
def step_impl(context):
    assert context.shuffled_deck != context.original_deck

