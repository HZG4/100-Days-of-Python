import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

turtle.listen()
screen.onkey(player.up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    screen.update()

    car_manager.movement()

    for i in range(len(car_manager.all_cars)):
        one_car = car_manager.all_cars[i]
        if one_car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.refresh()
        scoreboard.increment()
        car_manager.increase_speed()

    car_manager.game_flow()


turtle.mainloop()
