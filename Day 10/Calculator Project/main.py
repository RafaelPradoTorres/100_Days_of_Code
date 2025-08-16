from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def begin():
    print("\n" * 20)
    print(logo)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


while True:
    begin()
    n1 = float(input("Type the first number: "))
    is_operating = True

    while is_operating:
        operator = input("""
        +
        -
        *
        /
        Pick an operation: """)
        n2 = float(input("Type the second number: "))

        result = operations[operator](n1, n2)

        again = input(f"do you want to continue working with {result}? [y/n]").lower()
        if again == "y":
            is_operating = True
            n1 = result
        else:
            is_operating = False

