import os
from art import logo

def clear():
     os.system('clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def calculate(num1, num2, operator):
    for symbol in calculator:
        if operator == symbol:
            function = calculator[symbol]
            answer = function(num1, num2)
            print(f"{num1} {symbol} {num2} = {answer}")
            return answer
        else:
            continue

calculator = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

def recursive_calculator():
    print(logo)
    num1 = float(input("Enter a number 1: "))
    print("Pick any of the following operations:")
    for symbol in calculator:
        print(symbol)

    condition = True
    while condition == True:
        operator = input("Enter the operation: ")
        num2 = float(input("Enter a number 2: "))
        answer  = calculate(num1, num2, operator)
        num1 = answer
        query = input("Do you want to continue? Y or N ").lower()
        if query == "n":
            clear()
            recursive_calculator()
        else:
            continue

recursive_calculator()



