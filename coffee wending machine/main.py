MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
Money = 0.0
def is_available(ord_ingredients):
    for item in ord_ingredients: 
        if ord_ingredients[item] > resources[item]:
            print(f"Sorry There is not enough {item} only left is",resources[item])
            return False
    return True 
def get_money():
    total = 0
    print("Enter the coin")
    total += int(input("Enter the quarters: "))*0.25
    total += int(input("Enter the nickles: "))*0.05
    total += int(input("Enter the pennis: "))*0.01
    total += int(input("Enter the dimes: "))*0.10
    return total

def is_enough_money(payment,cost):
    if payment >= cost:
        change = round(payment - cost,2)
        print(f"You got {change}")
        global Money
        Money += cost
        return True
    else:
        print(f"You Have less money {cost}! Money Refunded ")
        return False

def is_drink_possible(choice,ord_ingredients):
    for item in ord_ingredients:
        resources[item] -= ord_ingredients[item]
    print(f"Enjoy your {choice} ☕")


s_machine = True
while s_machine:
    user_choice = input("What you Like ?(espresso/latte/cappuccino): ")
    if user_choice == "off":
        s_machine = False
    elif user_choice == "report":
        print("Water:",resources["water"],"ml")
        print("Milk:",resources["milk"],"ml")
        print("Coffee:",resources["coffee"],"g")
        print (f"Money: ${Money}")
    elif user_choice=="menu":
        for item in MENU:
            print(f"{item}: ",MENU[item])
    else:
        drink = MENU[user_choice]
        # print(drink)
        if is_available(drink["ingredients"]):
           payment = get_money()
           if is_enough_money(payment,drink["cost"]):
                is_drink_possible(user_choice,drink["ingredients"])