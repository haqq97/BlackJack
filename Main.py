from Deck import Deck
from Card import Card
from Player import Player


def display_cards(cards):
    for card in cards:
        print(card)


def cards_sum(cards):
    total = 0
    for card in cards:
        total += card.card_value()
    return total


def contains_ace(cards, person):
    for card in cards:
        if card.rank == 'Ace':
            if cards_sum(cards) >= 21:
                card.value = 1
            else:
                if person == 'p':
                    while True:
                        try:
                            value = int(input('Choose either 1 or 11 for your ace card: '))
                        except:
                            print('You can only enter a number')
                            continue
                        else:
                            if value == 1 or value == 11:
                                break
                            else:
                                print('You must choose 1 or 11 only')
                                continue
                else:
                    card.value = 11

if __name__ == '__main__':

    print('$$$$$$$$$$$$$$$$$$$$ WELCOME TO BLACKJACK $$$$$$$$$$$$$$$$$$$$\n')

    # Create a 52 card deck
    deck = Deck()
    # Shuffle the deck
    deck.shuffle()
    # print(deck) #to check

    print('Each player will have $2500 initially \n')
    # take name and bet from player
    playerName = input('Please enter your name: ')
    gameOver = False
    player = Player(playerName, 2500)
    while not gameOver:
        while True:
            try:
                playerBet = int(input('Please place your bet: '))
            except:
                print('You must enter a number')
            else:
                if playerBet > player.balance or playerBet < 1:
                    print('You must enter a number between 1 and 2500')
                    continue
                else:
                    player.bet_placed(playerBet)
                    break
        print('\n' * 100)
        print(f'{player.name}\'s cards: ')
        playerCards = [deck.pick_card(), deck.pick_card()]
        display_cards(playerCards)
        print(f'{player.name}\'s Sum: {cards_sum(playerCards)}')

        print('\nDealer Cards: ')
        dealerCards = [deck.pick_card(), deck.pick_card()]
        dealerDisplayCards = [dealerCards[1]]
        display_cards(dealerDisplayCards)
        print(f'Dealer Sum: {cards_sum(dealerDisplayCards)}\n')

        contains_ace(playerCards, 'p')
        contains_ace(dealerCards, 'd')

        # handle all naturals
        if cards_sum(dealerCards) == 21 and cards_sum(playerCards) == 21:
            print('Game is tied. You will get your bet back')
            player.bet_win(playerBet)
        elif cards_sum(playerCards) == 21 and cards_sum(dealerCards) < 21:
            print(f"This is a natural. {player.name} will get 1.5 times their bet back")
            player.bet_win(playerBet*1.5)
        elif cards_sum(dealerCards) == 21 and cards_sum(playerCards) < 21:
            print(f'Dealer has a natural. {player.name} loses their bet')
        bust = False
        playerTurn = False
        while not bust:
            while not playerTurn:
                playerAction = input('\nDo you wanna hit or stand? h = hit, s = stand: ')
                if playerAction == 'h':
                    playerCards.append(deck.pick_card())
                    print(f'\n{player.name}\'s Cards:')
                    display_cards(playerCards)
                    print(f'{player.name}\'s Sum: {cards_sum(playerCards)}')
                    if cards_sum(playerCards) >= 21:
                        bust = True
                        playerTurn = True
                        print('You have busted. You lost your bet')
                else:
                    playerTurn = True
            if not bust:
                while cards_sum(dealerCards) <= 17:
                    print('\nDealer hits')
                    pickedCard = deck.pick_card()
                    dealerCards.append(pickedCard)
                    dealerDisplayCards.append(pickedCard)
                    print(f'Dealer Cards:')
                    display_cards(dealerDisplayCards)
                    if cards_sum(dealerCards) >= 21:
                        bust = True
                        print('\nRevealing all dealer cards..... ')
                        display_cards(dealerCards)
                        print('Dealer has been busted. You win 1.5 times your bet')
                        player.bet_win(playerBet*1.5)
                if not bust:
                    print(f'\nRevealing all dealer cards.....')
                    print(f'Dealer Cards:')
                    display_cards(dealerCards)
                    print(f'Dealer Sum: {cards_sum(dealerCards)}')
                    print(f'\n{player.name}\'s Cards:')
                    display_cards(playerCards)
                    print(f'{player.name}\'s Sum: {cards_sum(playerCards)}')
                    if cards_sum(playerCards) > cards_sum(dealerCards):
                        print('Congratulations! You have won!')
                        player.bet_win(playerBet * 1.5)
                    elif cards_sum(playerCards) < cards_sum(dealerCards):
                        print('Sorry! You lost your bet')
                    else:
                        print('Its a draw!!')
                        player.bet_win(playerBet)
            print(f'\n{player.name}\'s Balance: {player.balance}')
            while True:
                playAgain = input('Do you wanna play again? (y/n): ')
                if playAgain == 'y' or playAgain == 'n':
                    break
                else:
                    print('Please enter y(yes) or n(no): ')
                    continue
            print('\n'*100)
            if playAgain == 'y':
                gameOver = False
            else:
                gameOver = True
                print('*********************************THANKS FOR PLAYING*********************************')
            break
