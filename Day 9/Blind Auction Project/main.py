from art import logo

print(logo)

# TODO-1: Ask the user for input
bids = {}

are_bidders = True

while are_bidders:
    print("Welcome to the secret auction program.")

    name = input("What is your name? ")
    price = int(input("What is your bid? "))

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price

    # TODO-3: Whether if new bids need to be added
    other_bidders = input("Are there other bidders? [Y/N]").upper()
    if other_bidders == "Y":
        are_bidders = True
    else:
        are_bidders = False

    print('\n' * 100)

# TODO-4: Compare bids in dictionary
great_bid = 0
winner = ''
for name in bids:
    if bids[name] > great_bid:
        great_bid = bids[name]
        winner = name

print(f"The winner is {winner} with a bid of ${great_bid}")
