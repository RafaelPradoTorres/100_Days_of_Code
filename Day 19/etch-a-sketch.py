import turtle
from turtle import Turtle, Screen

screen = Screen()
turt = Turtle()

def move_forwards():
    turt.forward(10)

def move_backwards():
    turt.back(10)

def turn_clockwise():
    turt.left(10)

def turn_counterclockwise():
    turt.right(10)

def clear_screen():
    turt.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()