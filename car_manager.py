from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager (Turtle):

    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.seth(180)
            new_car.goto(300, randint(-250, 250))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.cars_speed)

    def speed_up(self):
        self.cars_speed += MOVE_INCREMENT
