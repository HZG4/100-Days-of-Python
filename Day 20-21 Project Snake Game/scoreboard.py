from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(-110, 280)
        self.score = 0
        self.highscore = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.write(f"Score = {self.score}  Highscore = {self.highscore}" , font=("Arial", 14, "normal"))

    def update_scoreboard(self):
        self.clear()
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))
        self.write(f"Score = {self.score} Highscore = {self.highscore}" , font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(-120, 0)
        self.color("Red")
        self.write(f"GAME OVER", font=("Arial", 30, "bold"))
