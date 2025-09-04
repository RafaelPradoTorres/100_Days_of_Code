import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

WIDTH = 600
HEIGHT = 600

#Setting screen
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)



#Creating player
player = Player()

#Setting actions
screen.listen()
screen.onkey(player.move_up, "Up")

manager = CarManager()


game_is_on = True
loop = 0

while game_is_on:
    manager.go()

    loop += 1
    time.sleep(0.1)
    screen.update()

    # Detecting collision


    # Generating cars
    if loop == 6:
        x_coord = WIDTH / 2
        range_y = int(HEIGHT/2 - 50)
        y_coord = randint(-range_y, range_y)
        manager.create_car(
            (x_coord, y_coord)
        )
        loop = 0

#TODO 1: detect collision
#TODO 2: reach the top
#TODO 3: create scoreboard
#TODO 4: increment level
#TODO 5: delete car when it go to edge