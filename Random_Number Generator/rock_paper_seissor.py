import random
k = int(input("what you choose? type 0 for Rock, type 1 for Paper, type 2 for for Scissors "))
game = ['rock','paper','scissors']
user = game[k]
computer = random.randint(0,2)
print(f"computer choose number {computer}")
computer_choose = game[computer]
print("computer_choose: "+computer_choose)
print("user: "+user)
if computer_choose == 'rock'  and user =='scissors':
    print("Computer WINS")
elif computer_choose == 'scissors' and user == 'rock':
    print("USER WINS")
elif computer_choose == 'paper' and user == 'rock':
    print("COMPUTER WINS")
elif computer_choose == 'rock' and user == 'paper':
    print("USER WINS")
elif computer_choose == 'scissors' and user == 'paper':
    print("COMPUTER WINS")
elif computer_choose == 'paper' and user == 'scissors':
    print("USER WINS")
else:
    print("DRAW")