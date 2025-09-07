file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()

# in this case, you dont need to close the file
with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

# 'r' to read
# 'w' to write
# 'a' to append
with open('my_file.txt', mode='a') as file:
    contents = file.write("MANO MANO MANO")
    print(contents)


# creating a new file
with open('new_file.txt', mode='w') as file:
    contents = file.write("Novo documento criado")