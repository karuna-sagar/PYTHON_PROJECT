import random
names_string = input("Give me everybody's names, separated by a comma. ")


#**** this function are used to split the some specific point in the list (split(some argument))****


names = names_string.split(", ")
#************ we can write like this **********
# x = len(names)
# random_number = random.randint(0,x-1)



#******* it create the random choices in list (random.choices)***** 


random_number = random.choice(names)
# ***************** we can write ****************
# print(names[random_number]+" will pay the bill")
print(random_number + " will pay the bill")