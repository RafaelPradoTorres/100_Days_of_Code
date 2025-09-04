from turtle import Turtle

class Car(Turtle):
    def __init__(self, color, coord):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.goto(coord)

    def move_car(self, speed):
        self.forward(speed)
