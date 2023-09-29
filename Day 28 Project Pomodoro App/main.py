from tkinter import *
import math
# ---------------------------- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
emoji = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    label_1.config(text="  Timer  ", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    global reps
    global emoji
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_1.config(text="  Break  ", fg= RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        label_1.config(text="  Break  ",fg=PINK)

        emoji += "✔"
        checkmark.config(text=f"{emoji}")
        count_down(short_break_seconds)
    else:
        label_1.config(text="Work Time", fg=GREEN)
        count_down(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    global timer
    count_minute = math.floor(count / 60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"
    if count_minute < 10:
        count_minute = f"0{count_minute}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        window.bell()
        window.lift()
        start_timer()

# ---------------------------- UI SETUP ---------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)

# Top label
label_1 = Label(text="  Timer  ", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_1.grid(column=2, row= 1)

# Canvas for image and timer text
canvas = Canvas(width = 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Buttons
start_button = Button(text="Start", highlightthickness=0, bg="white", width= 5, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, bg="white", width= 5, command=reset_timer)
reset_button.grid(column=3, row=3)

# Bottom Label
checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
checkmark.grid(column=2, row=4)

window.mainloop()
