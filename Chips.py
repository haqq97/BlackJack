class Chips:
    def __init__(self, bet):
        self.totalChips = bet

    def win_bet(self, amount):
        self.totalChips += self.amount

    def lose_bet(self, amount):
        self.totalChips -= self.amount
