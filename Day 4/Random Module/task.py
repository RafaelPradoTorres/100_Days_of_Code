import random
import my_module


random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.one_number)

random_number = random.random() * 10
print(random_number)

random_float = random.uniform(1, 10)
print(random_float)

coin_flip = random.randint(1,2)
if coin_flip == 1:
    print("heads")
else:
    print("tails")