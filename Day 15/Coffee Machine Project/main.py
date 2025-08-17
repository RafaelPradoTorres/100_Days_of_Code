# CTRL + ALT + SHIFT = cursor multiplo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

coins = {
        "penny": 0.01,
        "neckel": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
    }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def user_prompt():
    print("Welcome to a coffee shop")
    print("There is our options:")
    for item in MENU:
        print(f" - {item}")
    return input("What would you like?").lower().strip()

def serve(recursos, beverage, money_on_machine):
    """Receive the resources and the choice, output new quantity of ingredients"""
    if not is_there_resources(recursos, beverage):
        print("Recursos insuficientes")
        return None

    change = pay_and_tips(beverage)
    if change == False:
        print("Insuficient money")
        return None

    necessario = MENU[beverage]["ingredients"]



    for item in necessario:
        print(f"Olha: {recursos[item]}")
        recursos[item] -= necessario[item]

    money_on_machine += MENU[beverage]["cost"]

    return money_on_machine

def is_there_resources(recursos, beverage):
    """Recebe os recursos da maquina e a bebida, retorna 'True' se tem recursos suficientes, 'False' se não"""
    necessario = MENU[beverage]["ingredients"]

    for item in necessario:
        if recursos[item] < necessario[item]:
            return False

    return True

def report(cash):
    print("Our actual resources are:")
    for item, value in resources.items():
        print(f" - {item}: {value}")
    print(f" - {cash} dollars remaining.")



def process_coins():
    coin_number = {}
    for coin in coins:
        coin_number[coin] = int(input(f"How many {coin} to put in the machine?"))

    return coin_number

def convert_money(coin_number):
    total_dollars = 0


    for coin in coin_number:
        total_dollars += coins[coin] * coin_number[coin]

    return total_dollars

def pay_and_tips(choice):
    """Sum up the number of coins inserted and return False or the change"""

    coin_number = process_coins()
    money_inserted = convert_money(coin_number)
    money_needed = MENU[choice]['cost']

    if money_needed > money_inserted:
        print("Insuficient money")
        return False
    else:
        change = money_inserted - money_needed

    return change



def machine():
    money = 0
    while True:
        choice = user_prompt()
        if choice == "off":
            print(f"You got {money} dollars")
            return
        elif choice == "report":
            report(money)
            print("\n\n")
        else:
            money = serve(resources, choice, money)


machine()





# Se a quantidade de dinheiro não for suficiente, não fazer nada, so impriir avisando

#make the coffee and reduce the resources

