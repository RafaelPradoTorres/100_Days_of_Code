# ARGUMENTOS OPCIONAIS
# ao definir uma função:
# ------------------
# fun(a, b=4, c=6):
#   print(a, b, c)
# ------------------
# no caso acima, apenas o argumento 'a' é obrigatório

# ARGUMENTOS ILIMITADOS *args
def add(*numbers):
    print(numbers)
    soma = 0
    for number in numbers:
        soma += number
    return soma

print(add(1,3,5))
print(add(1,9,5,7,2))
print(add(1,0))


# **kwargs

def calculate(**kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(f"{key} = {value}")

calculate(nome='Rafa', nota=10)


# We can also use it in a class

# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]          -> if doesnt exists, return error
#         self.model = kw.get("model")    -> if doesnt exists, return none
