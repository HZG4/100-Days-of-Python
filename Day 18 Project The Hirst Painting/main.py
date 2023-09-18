import random
import turtle
from turtle import Turtle, Screen

# Getting colors from Damian Hirst dots
# import colorgram
# colors = colorgram.extract('img.png', 12)
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    rgb_colors.append((r,g,b))

# Getting Screen coordinates
# def buttonclick(x, y):
# print("You clicked at this coordinate({0},{1})".format(x, y))
# turtle.onscreenclick(buttonclick, 1)


rgb_colors = [(202, 166, 109), (202, 234, 208), (171, 220, 224), (178, 204, 238), (240, 246, 241), (152, 73, 47), (236, 238, 244), (210, 145, 188), (255, 190, 173), (250, 207, 150), (222, 202, 138), (135, 32, 22)]

turtle.colormode(255)

pen = Turtle()
pen.hideturtle()
pen.pensize(15)
pen.penup()
x = -310
y = -250
pen.goto(x, y)

for i in range(11):
    for j in range(13):
        pen.pencolor(random.choice(rgb_colors))
        pen.pendown()
        pen.forward(1)
        pen.penup()
        pen.forward(50)
    y += 50
    x = -310
    pen.goto(x, y)

pen.goto(x, y)

my_screen = Screen()
my_screen.exitonclick()