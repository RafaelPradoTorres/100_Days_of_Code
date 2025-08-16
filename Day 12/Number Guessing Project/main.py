from art import logo
from random import randint

print(logo)

# make the computer guess a number
computer_number = randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

#apagar
print(computer_number)

game_on = True
while game_on:
    print(f"You have {attempts} remaining attempts.")

    player_guess = int(input("Make a guess: "))
    attempts -= 1


    if player_guess > computer_number:
        print("Your guess is too high.")
    elif player_guess < computer_number:
        print("Your guess is too low.")


    if player_guess == computer_number:
        print("You got it!")
        game_on = False
    elif attempts < 1:
        print("Sorry, you lose.")
        game_on = False
