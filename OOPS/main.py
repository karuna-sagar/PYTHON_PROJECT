from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
Coffeemaker = CoffeeMaker()
Moneymachine = MoneyMachine()
# menu_item = MenuItem()
is_on = True
while is_on:
    user_choice = input("Enter the choice? espresso/latte/cappuccino: ")
    if user_choice=="report":
        Coffeemaker.report()
        Moneymachine.report()
    elif user_choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(user_choice)
        is_enough_ingredient =  Coffeemaker.is_resource_sufficient(drink)
        is_payment_successful =  Moneymachine.make_payment(drink.cost)
        if is_enough_ingredient and is_payment_successful:
            Coffeemaker.make_coffee(drink)
    
        
