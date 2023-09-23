import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = 0

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def movement(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.speed)

    def increase_speed(self):
        self.speed += 2

    def game_flow(self):
        if self.speed >= 10:
            self.create_cars()
        if self.speed >= 20:
            self.create_cars()
        if self.speed >= 30:
            self.create_cars()