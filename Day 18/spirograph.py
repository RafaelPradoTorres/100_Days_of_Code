from turtle import Turtle
from turtle import Screen

turt = Turtle()
screen = Screen()
turt.speed("fastest")

for _ in range(36):
    turt.circle(100)
    heading = turt.heading()
    turt.setheading(heading + 10)

screen.exitonclick()
