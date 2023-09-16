from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
import os

coffee_machine = CoffeeMaker()
menu = Menu()
transaction = MoneyMachine()

coffee_machine_is_on = True

print(logo)
while coffee_machine_is_on:
    user_need = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_need == 'report':
        coffee_machine.report()
        transaction.report()
    elif user_need == 'off':
        os.system("cls")
        coffee_machine_is_on = False
    else:
        order = menu.find_drink(user_need)
        if coffee_machine.is_resource_sufficient(order) == True:
            if transaction.make_payment(order.cost) == True:
                coffee_machine.make_coffee(order)
