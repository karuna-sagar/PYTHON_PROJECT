import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for k in range(1,nr_letters+1):
    # random_char = random.choice(letters) 
    # password+=random_char
    password.append(random.choice(letters))
for l in range(1,nr_symbols+1):
    # random_char = random.choice(symbols)
    # password+=random_char
    password.append(random.choice(symbols))
for m in range(1,nr_numbers+1):
    # random_char = random.choice(numbers)
    # password+=random_char
    password.append(random.choice(numbers))
print(password)
random_password = ""
random.shuffle(password)
print(password)
for k in range(0,len(password)):
    random_password+=password[k]
print(random_password)
