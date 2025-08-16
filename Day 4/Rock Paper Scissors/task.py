import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors"))
computer = random.randint(0,2)

element = [rock, paper, scissors]
print(element[play])

print("computer choose:")
print(element[computer])

if play==computer:
    print("Draw")
elif (play == 0 and computer == 1) or (play == 1 and computer == 2) or (play == 2 and computer == 0):
    print("You lose")
elif (play == 0 and computer == 2) or (play == 1 and computer == 0) or (play == 2 and computer == 1):
    print("You win")