import os
from art import logo

def clear():
    os.system("clear")

def calculate_resource(MENU, resources, user_need):
    resources['water'] = resources['water'] - MENU[user_need]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[user_need]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[user_need]['ingredients']['coffee']
    return resources

def check_resources(MENU, resources, user_need):
    if resources['water'] < MENU[user_need]['ingredients']['water']:
        print("Sorry not sufficient water.")
        return False
    elif resources['milk'] < MENU[user_need]['ingredients']['milk']:
        print("Sorry not sufficient milk.")
        return False
    elif resources['coffee'] < MENU[user_need]['ingredients']['coffee']:
        print("Sorry not sufficient coffee.")
        return False
    else:
        return True

def calculate_change(user_need, total, resources):
    if total > MENU[user_need]['cost']:
        change = total - MENU[user_need]['cost']
        resources['machine_money'] = resources['machine_money'] + MENU[user_need]['cost']
        print(f"Here is your ${round(change, 2)} in change.")
        print(f"Here is your {user_need}. Enjoy!")
        return change
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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
    "machine_money" : 0
}

machine_is_on = True
print(logo)
while machine_is_on:
    user_need = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_need == 'report':
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: {resources['machine_money']}")
    elif user_need == 'off':
        clear()
        machine_is_on = False
    else:
        enough = check_resources(MENU, resources, user_need)
        if enough:
            resources = calculate_resource(MENU, resources, user_need)
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))   * 0.25
            dimes   =  int(input("How many dimes?: "))      * 0.10
            nickles =  int(input("How many nickles?: "))    * 0.05
            pennies =  int(input("How many pennies?: "))    * 0.01
            total_money = quarters + dimes + nickles + pennies
            change = calculate_change(user_need, total_money, resources)