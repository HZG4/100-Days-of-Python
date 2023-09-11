import random
import os
from art import logo

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def hold_cards():
    return

def player_move_query():
    move = input("Type 'y' to get another card, type 'n' to pass: ")
    if move == 'y':
        player_cards.append(deal_cards())
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    elif move == 'n':
        print(f"Your cards: {player_cards}, final score: {sum(player_cards)}")
        return False

def computer_move():
    if sum(player_cards) > 21:
        return

    while sum(computer_cards) < 17:
        computer_cards.append(deal_cards())
        while sum(computer_cards) > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1

        if 17 <= sum(computer_cards) <= 21:
            return



def declare_winner(player_score, computer_score):
    if  player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_cards == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def start_game():
    start_query = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_query == "y":
        os.system("clear")
        player_cards.clear()
        computer_cards.clear()
        print(logo)
        i = 2
        while i > 0:
            player_cards.append(deal_cards())
            computer_cards.append(deal_cards())
            if sum(player_cards) > 21 and player_cards[i] == 11:
                player_cards[i] = 1
            elif sum(computer_cards) > 21 and player_cards[i] == 11:
                computer_cards[i] = 1
            i = i - 1
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: [{computer_cards[1]}]")

        while sum(player_cards) < 21:
            choice = player_move_query()
            if choice == False or sum(player_cards) > 21:
                break

        while sum(computer_cards) < 21:
            computer_move()
            if sum(player_cards) > 21:
                break
            elif sum(computer_cards) == 21 or (sum(computer_cards) > 17 and sum(computer_cards) < 21):
                break

        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        winner = declare_winner(player_score, computer_score)
        print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")
        print(winner)
        start_game()
    elif start_query == 'n':
        player_cards.clear()
        computer_cards.clear()
        exit()

player_cards = []
computer_cards = []
start_game()


