from Card import Card
import random


class Deck(Card):

    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
             '10':10, 'Jack':10 ,'Queen':10, 'King':10, 'Ace':11}

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank, value in self.ranks.items():
                self.deck.append(Card(suit, rank, value))

    def __str__(self):
        all_cards = ''
        for cards in self.deck:
            all_cards += cards.__str__()
        return all_cards

    def shuffle(self):
        random.shuffle(self.deck)

    def pick_card(self):
        card = self.deck.pop(0)
        return card






