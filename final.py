import random 
import os
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and  sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score==computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent have Blackjack"
    elif user_score==0:
        return "You win you have Black jack"
    elif user_score>21:
        return "You Loose"
    elif user_score<21 and computer_score>21:
        return "You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Loose"
def play_game():
    from art import logo
    print(logo)
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    
    is_over = False
    while not is_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your cards: {user_card} current score: {user_score}")
        print(f"computer's first card: {computer_card[0]} ")
        if user_score==0 or computer_score == 0 or user_score>21:
            is_over = True
        else:
            user_choice = input("Type 'y' for Continue.Otherwise 'n' to end(k): ")
            if user_choice=="y":
                user_card.append(deal_card())
            else:
                is_over = True
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your Final hand: {user_card} final score:{user_score}")
    print(f"computer Final hand: {computer_card} final score:{computer_score}")
    print(compare(user_score,computer_score))
    

# play_game()
while input("Type 'y' to Play Again .Otherwise 'n' to pass: ")=='y':
    play_game()

        
