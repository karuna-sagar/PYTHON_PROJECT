
def add(*args):
    print(args[0])
    sum =0
    for n in args:
        sum+=n
    return sum
# print(add(1,2,3,56,9,8,4,5,6))
# def calculate(**args):
    # for key,value in args.items():
        # print(key)
        # print(value)
    # print(args["add"])

# calculate(add=3,multiply=5)

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

car = Car(make="Nissan")
# car = Car(make="Nissan",model="GTR_X")
print(car.model)
# print(car.model)