import pandas

#TODO 1. Create a dictionary in this format:
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
while True:
    try:
        print([alphabet[letter] for letter in word])
    except KeyError:
        print("Please enter a valid key")
        word = input("Enter a word: ").upper()
    else:
        break