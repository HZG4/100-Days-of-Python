from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(-60, 280)
        self.score = 0
        self.write(f"SCORE = {self.score}", font=("Arial", 14, "normal"))

    def increment(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE = {self.score}", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(-120, 0)
        self.color("Red")
        self.write(f"GAME OVER", font=("Arial", 30, "bold"))
