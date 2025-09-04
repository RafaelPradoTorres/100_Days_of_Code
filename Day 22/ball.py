from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(5)
        self.x_ratio = 10
        self.y_ratio = 10


    def move(self):
        new_x = self.xcor() + self.x_ratio
        new_y = self.ycor() + self.y_ratio
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_ratio = -self.y_ratio

    def bounce_x(self):
        self.x_ratio = -self.x_ratio

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()