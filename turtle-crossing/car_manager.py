from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 10) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-240, 240))
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def reset_speed(self):
        self.speed = STARTING_MOVE_DISTANCE
