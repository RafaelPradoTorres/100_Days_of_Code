numbers = [1, 2, 3]

# new_list = []
# for item in numbers:
#     add_1 = n+1
#     new_list.append(add_1)



new_list = [n+1 for n in numbers]

name = "Rafael"
letter_list = [letter for letter in name]

doubled_range = [n*2 for n in range(1,5)]

#Conditional comprehension

names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
short_names = [name.upper() for name in names if len(name) < 5]
print(short_names)
