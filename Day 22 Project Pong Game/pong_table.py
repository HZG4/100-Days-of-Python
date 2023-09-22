from turtle import Turtle

def create_pong_table():
    middle_line = Turtle()
    middle_line.pencolor('white')
    middle_line.fillcolor('white')
    middle_line.shape('square')
    middle_line.penup()
    y = 270
    while y > -290:
        middle_line.turtlesize(stretch_len= 0.2, stretch_wid= 0.8)
        middle_line.goto(0, y)
        middle_line.stamp()
        y -= 30