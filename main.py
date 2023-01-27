student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df_nato)

dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}
# print(dict_nato)

start = True

while start:
    word = input("Enter a word:").upper()

    list_word = [n for n in word]
    print(list_word)

    try:
        phonetic_code = [dict_nato[key] for key in list_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        start = True
    else:
        print(phonetic_code)
        start = False
