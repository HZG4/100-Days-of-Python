import turtle
from turtle import Screen, Turtle
from pong_table import create_pong_table
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=800, height=600)
my_screen.tracer(0)

create_pong_table()
player_l = Paddle((-390,0))
player_r = Paddle((380,0))
ball = Ball()
scoreboard_l = Scoreboard((-80, 250))
scoreboard_r = Scoreboard((80, 250))
my_screen.update()

turtle.listen()
my_screen.onkey(player_r.up, "Up")
my_screen.onkey(player_r.down, "Down")
my_screen.onkey(player_l.up, "w")
my_screen.onkey(player_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.movement()

    # Detect Collisions with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect Collisions with the paddle
    if ball.distance(player_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard_r.increment()
        pass

    elif ball.distance(player_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard_l.increment()
        pass

    if ball.xcor() > 380 or ball.xcor() == -390:
        scoreboard_l.gameover()
        game_is_on = False

    #if ball.xcor() >= 380 or ball.xcor() <= -380:

turtle.mainloop()

