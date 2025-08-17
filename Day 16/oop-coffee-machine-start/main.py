from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

serving = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while serving:
    print(menu.get_items())
    choice = input("what would you like?")
    drink = menu.find_drink(choice)

    if choice == "off":
        serving = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink is None:
        print("Try again")
    else:
        sufficient = coffee_maker.is_resource_sufficient(drink)
        if sufficient:
            cost = drink.cost
            payed = money_machine.make_payment(cost)
            if payed:
                coffee_maker.make_coffee(drink)


