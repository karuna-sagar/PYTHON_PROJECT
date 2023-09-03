#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while  "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print("YOU WIN")    
    
# guess = input("Guess a letter: ").lower()

#Check guessed letter 


# ***************************************HERE WE HAVE TO MAKE A FLAG BECAUSE IF WE HAVE TO GET RETURN FROM THE LOOP WHICH IS DESCRIBED IN CHALLENGE 4 IF WE DO IN THIS THEN WE HAVE TO FACE PROBLEM IN PRINTING AND RETURN TO THE LOOP********************