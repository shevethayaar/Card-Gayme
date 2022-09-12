from DeckOfCards import deck

class player:
    def __init__(self):  #Initialization of player`s data
        self.cards = []
        self.count_cards = [i for i in range(10, 27)]


    def set_hand(self, deck):
        card = deck.deal_one()
        self.cards.append(card)

    def get_card(self, card):
        self.cards.pop(card)
        return card

class bot:

    def __init__(self):
        self.cards = []
        self.count_cards = [i for i in range(10, 27)]

    def set_hand(self, deck):
        card = deck.deal_one()
        self.cards.append(card)
        return True

    def get_card(self, card):
        self.cards.append(card)

