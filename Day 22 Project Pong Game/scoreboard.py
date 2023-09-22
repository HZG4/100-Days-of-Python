from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(cords)
        self.score = 0
        self.write(f"{self.score}", font=("Arial", 30, "normal"))

    def increment(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", font=("Arial", 30, "normal"))

    def gameover(self):
        self.goto(-120, 0)
        self.color("Red")
        self.write(f"GAME OVER", font=("Arial", 30, "bold"))