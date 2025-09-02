# Event listeners

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
print('a')
screen.onkey(key="space", fun=move_forwards)
print('b')
screen.exitonclick()
print('c')
# higher order functions