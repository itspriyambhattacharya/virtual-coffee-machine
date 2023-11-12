from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money = MoneyMachine()
machine_content = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What choice do you like? {options}:\t")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(machine_content.report())
        print(my_money.report())
    else:
        drink = menu.find_drink(choice)
        if machine_content.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                machine_content.make_coffee(drink)
