import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        nato_output = [nato_dict[alpha] for alpha in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_output)


generate_phonetic()
