import random
from art import logo
print(logo)
def compare(user_guess,computer_guess,turn):
    if user_guess > computer_guess:
        print("Too High") 
        return turn - 1
    elif user_guess < computer_guess:
        print("Too Low")
        return turn -1
    else:
        print (f'You Got it! The Answer was:{computer_guess}')

EASY_LEVEL = 10
DIFFICULT_LEVEL = 5

def difficulty(choose):
    if choose == "hard":
        return DIFFICULT_LEVEL
    else:
        return EASY_LEVEL

def play():
    print("Welcome To the Number Guessing Game!")
    print("I am Thinking of Number Between 1 and 100")
    answer = random.randint(1,100)
    choose = input("Choose a Difficulty level 'Easy' or 'Hard': ")
    turns = difficulty(choose)
    guess = 0
    while guess!=answer:
        
        guess = int(input("Enter the number: "))
        turns = compare(user_guess=guess,computer_guess=answer,turn=turns)
        print(f"You have {turns} attempt left")
        if turns == 0:
            print("You ran out of attempt.Better Luck Next Time")
            return
        else:
            print("Guess Again")
        
play()