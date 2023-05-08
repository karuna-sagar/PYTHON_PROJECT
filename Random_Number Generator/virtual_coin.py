import random
test_seed = int(input("Enter the seed number\n"))
random.seed(test_seed)
number = random.randint(1,2)
if(number==1):
    print("HEAD")
else:
    print("TAIL")