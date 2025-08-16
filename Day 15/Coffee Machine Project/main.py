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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def user_prompt():
    print("Welcome to a coffee shop")
    print("There is our options:")
    for item in MENU:
        print(f" - {item}")
    return input("What would you like?").lower().strip()

def serve(recursos, beverage):
    """Receive the resources and the choice, output new quantity of ingredients"""
    item = MENU[beverage]
    necessario = item["ingredients"]



    return recursos



#def turn_off():

def report():
    print("Our actual resources are:")
    for item, value in resources.items():
        print(f" - {item}: {value}")
    print(f" - {money} dollars remaining.")


choice = user_prompt()


report()



#TODO: 2 Turn the coffee machine by typing 'off'

#TODO: 4 Check resources sufficient
#TODO: 5 Process coins
#TODO: 6 CHeck transaction successful
#TODO: 7 Make a coffee

# coins = penny:0,01 neckel0,05 dime0,10 quarter0,25

#print report (resource left)
#check if resources are sufficient
#process coins and calculate change
#check if transaction successfull
#make the coffee and reduce the resources


