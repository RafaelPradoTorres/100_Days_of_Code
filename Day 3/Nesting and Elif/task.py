print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("type your age"))
    if age <= 12:
        print("You should pay $12")
    elif age <= 18:
        print("You should pay $18")
    else:
        print("You should pay $50")
else:
    print("Sorry you have to grow taller before you can ride.")
