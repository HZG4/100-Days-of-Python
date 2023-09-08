import random
import os
from hangman_words import word_list
from hangman_ascii import stages, logo


def clear():
    os.system("clear")


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Creating list of '_'
display_array = []
for letter in chosen_word:
    display_array.append("_")
display_word = " ".join(display_array)

# Displayed UI
clear()
print(logo + "\n")
print(display_word + "\n")
print("Welcome to hangman!")
print(stages[6])

continue_game = True
lives = 6

guessed_list = [""]

while continue_game is True:
    guess = input("Guess a letter: ").lower()

    # check if guess exists and replace display
    for i in range(0, word_length):
        if guess == chosen_word[i]:

            display_array[i] = guess
        else:
            continue

    display_word = " ".join(display_array)
    clear()
    print(logo + "\n")
    print(display_word + "\n")

    if guess not in chosen_word:
        lives = lives - 1
        print(f"You guessed {guess} wrongly. You lose a life.")
    else:
        print(f"You guessed {guess} correctly.")

    print(stages[lives])

    # check if all _ has been replaced
    if "_" not in display_array:
        print("You won the game!")
        continue_game = False
    if lives == 0:
        print(f"You have lost. The word was {chosen_word}")
        continue_game = False
