from Player import bot, player
from DeckOfCards import deck

class game:

    def __init__(self):
        self.bot = []
        self.player = []
        self.deck = deck()

    def new_game(self):
        print('What`s your name?')
        name = input()
        p = player()
        self.player.append(p)
        print('Hello', name)
        self.player.append(name)
        b = bot()
        print('Bot Jack was created')
        self.bot.append(b)
        self.bot.append('Jack')

    def set_deck(self):
        for player in self.player:
            player.set_hand(self.deck, 26)
        for bot in self.bot:
            bot.set_hand(self.deck, 26)

