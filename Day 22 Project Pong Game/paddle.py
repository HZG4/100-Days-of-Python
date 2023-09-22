from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(cords)

    def up(self):
        if self.ycor() == 240:
            self.goto(self.xcor(), 240)
        else:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() == -240:
            self.goto(self.xcor(), -240)
        else:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
