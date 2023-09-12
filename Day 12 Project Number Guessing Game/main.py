import random
from art import logo

def get_attempts():
    query = input("Choose a difficulty. Take 'easy' or 'hard': ")
    if query == 'easy':
        print("You have 10 attempts remaining to guess the number.")
        return 10
    elif query == 'hard':
        print("You have 5 attempts remaining to guess the number.")
        return 5

def get_number():
    num = random.randint(1, 100)
    return num

def evalute_guess(num, attempts):
    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess > num:
            attempts = attempts - 1
            print(f"Too High. \n You have {attempts} remaining")
        elif guess < num:
            attempts = attempts - 1
            print(f"Too less. \n You have {attempts} remaining")
        elif guess == num:
            print(f"You got it. The answer was {num}")
            exit()
        elif attempts == 0:
            print(f"You have run out of attempts. The number was {num}.")
            exit()

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

player_attempts = get_attempts()
number = get_number()
evalute_guess(number, player_attempts)