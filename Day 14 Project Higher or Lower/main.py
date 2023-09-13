from game_data import data
from art import logo, vs
import random
import os

def clear():
    os.system("clear")

def random_select():
    return random.choice(data)

def higher_lower(option_1, option_2, score):
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        if option_1['follower_count'] > option_2['follower_count']:
            clear()
            score = score + 1
            print(f" {logo} \n You are right! Current Score {score}")
            return True
        else:
            clear()
            print(f" {logo} \n Sorry, that's wrong. Final score {score}")
            exit()
    elif choice == 'b':
        if option_2['follower_count'] > option_1['follower_count']:
            clear()
            score = score + 1
            print(f" {logo} \n You are right! Current Score {score}")
            return True
        else:
            clear()
            print(f" {logo} \n Sorry, that's wrong. Final score {score}")
            exit()

def game(score):
    print(logo)
    option_1 = random_select()
    option_2 = random_select()

    game_should_continue = True
    while game_should_continue == True:

        option_1 = option_2
        option_2 = random_select()
        dict = []
        while option_1 == option_2 and option_2 not in dict:
            option_2 = random_select()
            dict.append(option_2)

        print(f"Compare A: {option_1['name']}, {option_1['description']}, from {option_1['country']}")
        print(vs)
        print(f"Against B: {option_2['name']}, {option_2['description']}, from {option_2['country']}")

        game_should_continue = higher_lower(option_1, option_2, score)
        if game_should_continue == True:
            score = score + 1

score = 0
game(score)
