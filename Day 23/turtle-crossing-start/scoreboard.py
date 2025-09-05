from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.score = 0

        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(coord)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increment(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def reset(self):
        self.clear()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=FONT)