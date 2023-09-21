import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.85, stretch_wid=0.85)
        self.color("blue")
        self.speed(10)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))

