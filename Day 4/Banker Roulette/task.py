import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
unlucky = random.randint(0, 4)

print(friends[unlucky])

print(random.choice(friends))