from art import logo
from art import vs
from game_data import data
from random import choices
from random import choice

def first_two():
    return choices(data, k=2)

def next_person(two_persons):
    two_persons[0] = two_persons[1]
    two_persons[1] = choice(data)
    return two_persons

def show_info(player):
    print(f"{player['name']} is a {player['description']} from {player['country']}.")
    print(f"Take a int: {player['follower_count']}")

def compare_two(two_persons):
    if two_persons[0]['follower_count'] > two_persons[1]['follower_count']:
        return 'A'
    else:
        return 'B'


def game():
    # PS: AO FIM, VER A POSSIBILIDADE DE DOIS TEREM A MESMA QUANTIDADE DE SEGUIDORES

    score = 0
    players = first_two()

    while True:
        answer = compare_two(players)

        print(logo)

        print("Option A:")
        show_info(players[0])

        print(vs)

        print("Option B:")
        show_info(players[1])

        print("WHO  HAS  MORE  FOLLOWERS???")
        print(f"score = {score}")

        # dica
        print(f"hint: {answer}")

        # TRATAR EXCESSÃO CASO NECESSÁRIO
        guess = input("Who do you think has more followers? 'A' or 'B'?").upper()


        if guess == answer:
            score += 1
            players = next_person(players)
        else:
            print("Wrong")
            return score



game()