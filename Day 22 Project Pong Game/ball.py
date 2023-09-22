import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Orange")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.xmove = 20
        self.ymove = 20
        self.goto(0,0)

    def movement(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove = self.ymove * -1

    def bounce_x(self):
        self.xmove = self.xmove * -1

