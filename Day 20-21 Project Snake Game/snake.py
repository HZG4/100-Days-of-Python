import turtle
from turtle import Screen, Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.starting_x = 0
        self.starting_y = 0
        self.snake_body = []

        for i in range(3):
            self.segment = Turtle()
            self.segment.penup()
            self.segment.color('lime', 'Green')
            self.segment.shape('square')

            self.segment.goto(self.starting_x, self.starting_y)
            self.snake_body.append(self.segment)
            self.starting_x += -20

        self.head = self.snake_body[0]


    def move(self):
        for segment_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def increase_length(self):
        self.new_segment = Turtle()
        self.new_segment.penup()
        self.new_segment.color('lime', 'Green')
        self.new_segment.shape('square')
        self.new_segment.goto(self.snake_body[-1].position())
        self.snake_body.append(self.new_segment)

    def up(self):
        if self.head.heading() == 0 or self.snake_body[0].heading() == 180:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() == 90 or self.snake_body[0].heading() == 270:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 90 or self.snake_body[0].heading() == 270:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() == 0 or self.snake_body[0].heading() == 180:
            self.head.setheading(270)
