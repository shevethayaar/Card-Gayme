from Techzadanie import SUITS, RANKS  # Import constants
from itertools import product  # Import method
from random import shuffle # Import shuffle method

class Card:  # Creating a class of ONE card

    def __init__(self, suit, rank, value, power):  # Initialization of card
        self.suit = suit
        self.rank = rank
        self.value = value
        self.power = power

    def __str__(self):  # Print the information about a card
        message = 'Suit:' + self.suit + '\nRank: ' + str(self.rank) + '\nValue: ' + str(self.value) + '\nPower: ' + str(self.power)
        return message

class Deck:    # Creating ALL of the deck

    def __init__(self):  # Initialization and randomizing of Deck
        self.cards = self._create_deck()
        shuffle(self.cards)


    def _generate_deck(self):  # Cycles of creating Deck
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'Jack':   # Creating value of rank
                value = 11
            elif rank == 'Queen':
                value = 12
            elif rank == 'King':
                value = 13
            elif rank == 'Ace':
                value = 1
            elif rank.isdigit():
                value = int(rank)

            if suit == 'Diamomd':   # Creating power of suit
                power = 1
            elif suit == 'Spade':
                power = 2
            elif suit == 'Heart':
                power = 3
            elif suit == 'Club':
                power = 4

            c = Card(suit = suit, rank = rank, value = value, power = power)
            cards.append(c)
        return cards

    def deal_one(self):  # Gives ONE card to hand
        return self.cards.pop()
