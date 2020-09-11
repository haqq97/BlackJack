class Card:
    def __init__(self, suit='none', rank='none', value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def card_value(self):
        return self.value

    def ace_value(self, value):
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'
