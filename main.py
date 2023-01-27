import pandas

df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}


start = True

while start:
    word = input("Enter a word:").upper()

    list_word = [n for n in word]
    # print(list_word)

    try:
        phonetic_code = [dict_nato[key] for key in list_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        start = True
    else:
        print(phonetic_code)
        start = False
