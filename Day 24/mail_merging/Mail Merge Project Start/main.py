from os import listdir

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt

invited_names = "./Input/Names/invited_names.txt"

with open(invited_names, 'r') as file:
    str_names = file.read()
    names = str_names.split()

#Replace the [name] placeholder with the actual name.

letter_template = "./Input/Letters/starting_letter.txt"
for name in names:
    with open(letter_template, 'r') as template:
        text = template.read()
        new_text = text.replace('[name]', name)

        #Save the letters in the folder "ReadyToSend".
        file_path = "./Output/ReadyToSend/"
        new_file_name = "letter_" + name + ".txt"
        file_add = file_path + new_file_name
        with open(file_add, 'w') as letter:
            letter.write(new_text)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp