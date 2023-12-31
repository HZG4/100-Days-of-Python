import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def restart_game():
    game_is_on = True

my_screen = Screen()
my_screen.tracer(0)
my_screen.listen()
my_screen.setup(width= 600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

turtle.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        food.refresh()
        snake.increase_length()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() < -280:
        scoreboard.update_scoreboard()
        scoreboard.game_over()
        game_is_on = False

    #detect collision with wall
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.update_scoreboard()
            scoreboard.game_over()
            game_is_on = False

my_screen.exitonclick()


