import os
import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

global word_dict, word_list
global flip_timer

def tick_function():
    next_card()
    remove_known_word()

def remove_known_word():
    to_learn.remove(word_dict)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

    if data.shape[0] == 0:
        os.remove("./data/words_to_learn.csv")
        exit()

def next_card():
    global word_dict, flip_timer
    window.after_cancel(flip_timer)

    word_dict = random.choice(to_learn)

    # Card Flipping UI code
    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black" )
    canvas.itemconfig(word_text, text=f"{word_dict['french']}", fill="black")

    flip_timer= window.after(3000, flip_card)

def flip_card():
    # Card Flipping UI code
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{word_dict['english']}", fill="white")

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = pandas.DataFrame(data).to_dict(orient="records")

    window = Tk()
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

    flip_timer = window.after(3000, func=flip_card)

    canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
    # Flash Card
    card_front = PhotoImage(file="./images/card_front.png")
    card_back = PhotoImage(file="./images/card_back.png")

    canvas_img = canvas.create_image(400, 263, image=card_front)
    # Text
    language_text = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
    word_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

    canvas.grid(column=1, row=1, columnspan=2)

    next_card()

    tick_img = PhotoImage(file="./images/right.png")
    tick_btn = Button(image=tick_img, bg= BACKGROUND_COLOR, border=0, highlightthickness=0, command=tick_function)
    tick_btn.grid(column=2, row=2)

    cross_img = PhotoImage(file="./images/wrong.png")
    cross_btn = Button(image=cross_img, bg=BACKGROUND_COLOR, border=0, highlightthickness=0, command=next_card)
    cross_btn.grid(column=1, row=2)

    window.mainloop()

