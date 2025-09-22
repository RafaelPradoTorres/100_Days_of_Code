# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas



data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def funcao():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error:
        print(f"This is a fucking error {error}")
        funcao()
    else:
        print(output_list)

funcao()