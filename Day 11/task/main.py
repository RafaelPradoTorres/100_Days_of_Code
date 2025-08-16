from art import logo
from random import randint


def ask_game():
    will_play = input("Do you want to play a game? [y/n]").lower()
    if will_play == "y":
        return True
    return False


def give_2_cards(deck):

    chosen1 = randint(0, len(deck) - 1)
    chosen2 = randint(0, len(deck) - 1)

    hand = [deck[chosen1], deck[chosen2]]

    return hand

def sum_hand(hand):
    # Etapa 1: somar
    soma = 0
    for card in hand:
        soma += card

    # Etapa 2: checar > 21 e 11
    if soma > 21 and hand[-1] == 11:
        hand[-1] = 1
        soma -= 10

    return soma

def check_sum(soma):
    is_defeated = False
    if soma > 21:
        is_defeated = True
    return is_defeated

def give_1_card(deck, hand):

    chosen = randint(0, len(deck)-1)
    hand.append(deck[chosen])


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]




new_game = ask_game()

while new_game:
    player_defeated = False
    dealer_defeated = False
    dealer_playing = False
    player_playing = True
    winner = '' #Dealer / Player

    print(logo)
    dealer_hand = give_2_cards(cards)
    player_hand = give_2_cards(cards)

    while player_playing:

        player_points = sum_hand(player_hand)

        print(f"Dealer's card: {dealer_hand[0]}\n")
        print(f"Your cards: {player_hand}")
        print(f"You have {player_points} points")

        player_defeated = check_sum(player_points)

        if player_defeated:
            print("You went over!!")
            player_playing = False
            winner = 'Dealer'

        if player_playing:
            want_another = input("Do you want another card? [y/n]").lower()

            if want_another == 'y':
                # Give one card to player
                give_1_card(cards, player_hand)
                print(player_hand)
            else:
                player_playing = False
                dealer_playing = True


    while dealer_playing:

        dealer_points = sum_hand(dealer_hand)
        dealer_defeated = check_sum(dealer_points)

        print(f"Dealer's hand: {dealer_hand}")
        print(f"Dealer's points: {dealer_points}\n")

        if dealer_defeated:
            winner = 'Player'
            dealer_playing = False

        elif dealer_points > player_points:
            winner = 'Dealer'
            dealer_playing = False
        elif dealer_points == player_points:
            winner = 'Draw'
            dealer_playing = False
        else:
            give_1_card(cards, dealer_hand)


    print(f"The winner is {winner}")
    print("Game Over")

    new_game = ask_game()