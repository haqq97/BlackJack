from Chips import Chips
from Card import Card
from Deck import Deck

class Player:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def bet_placed(self, bet,):
        self.balance -= bet

    def bet_win(self, bet):
        self.balance += bet

    def hit(self, deck):
        self.cards.append(deck.pick_card())





