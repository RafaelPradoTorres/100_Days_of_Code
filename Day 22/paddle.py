from turtle import Turtle

class Paddle(Turtle):
    LARGURA = 1
    ALTURA = 5 * LARGURA


    def __init__(self, coord):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(self.ALTURA, self.LARGURA)
        self.goto(coord)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


