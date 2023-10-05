import time
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.user_answer = ''

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR ,fg= "white", pady=10, padx=10)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0)

        self.text = self.canvas.create_text(150, 100, text="",fill="black", width=280, font=("Arial", 15, "italic"))
        self.get_new_question()
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, border=0, command=self.set_answer_true)
        self.true_btn.grid(column=0, row=2)

        false_image= PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, border=0, command=self.set_answer_false)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()

    def get_new_question(self,):
        self.canvas.config(bg="white")
        q_text= self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def set_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.set_score(is_right)
        self.set_color(is_right)

    def set_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.set_score(is_right)
        self.set_color(is_right)

    def set_color(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_new_question)

    def set_score(self, is_right):
        if is_right:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}", bg=THEME_COLOR ,fg= "white", pady=10, padx=10)
        if self.quiz.still_has_questions() == False:
            exit()