import random
import turtle
from turtle import Screen, Turtle

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet =  turtle.textinput("Make a bet", "Enter a color: ")

x = -230
y = -150

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
racers = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.shapesize(2)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 60
    racers.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in racers:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            if user_bet == turtle.pencolor():
                print("Your turtle won the race. Good bet!")
                exit()
            else:
                color_of_turtle = turtle.pencolor()
                print(f"Your turtle lost. The {color_of_turtle} turtle won the race.")
                exit()

my_screen.exitonclick()