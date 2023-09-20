# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("Day_26 List Comprehension and the NATO Alphabet/nato_phonetic_alphabet.csv")
# print(data.to_dict())
phonetic_Record = {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_Record)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("write the word?").upper()
output_data = [phonetic_Record[letter] for letter in word]
print(output_data)