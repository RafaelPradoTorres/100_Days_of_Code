from turtle import Turtle
from random import random
from random import randint

turt = Turtle()
turt.speed(0)
for i in range(100):
    r = random()
    g = random()
    b = random()
    turt.pencolor(r, g, b)
    angle = randint(0,3) * 90
    turt.fd(15)
    turt.right(angle)