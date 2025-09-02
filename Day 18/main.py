from turtle import Turtle
from turtle import Screen
# from turtle import *
# import turtle as t
from random import random
import heroes

print(heroes.gen())

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for sides in range(3, 11):
    r = random()
    g = random()
    b = random()
    tim.pencolor(r, g, b)
    angle = 360 / sides
    for _ in range(sides):
        for _ in range(5):
            tim.penup()
            tim.fd(5)
            tim.pendown()
            tim.fd(5)
        tim.lt(angle)


screen = Screen()
screen.exitonclick()
