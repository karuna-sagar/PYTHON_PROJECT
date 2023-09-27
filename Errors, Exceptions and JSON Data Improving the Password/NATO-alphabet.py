import pandas
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_Record = {row.letter:row.code for (index,row) in data.iterrows()}
def generate_phonetic():
    word = input("write the word?").upper()
    try:
        output_data = [phonetic_Record[letter] for letter in word]
    except KeyError:
        print("Sorry you have to enter the correct")
        generate_phonetic()
    else:
        print(output_data)
generate_phonetic()