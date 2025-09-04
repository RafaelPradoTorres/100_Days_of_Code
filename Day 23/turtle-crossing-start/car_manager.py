from car import Car
from random import choice
from random import randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self, coord):
        chosen_color = choice(COLORS)
        self.cars.append(
            Car(chosen_color, coord)
        )

    def go(self):
        for car in self.cars:
            car.move_car(STARTING_MOVE_DISTANCE)





