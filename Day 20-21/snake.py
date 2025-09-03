from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.SEGMENT_SIZE = 20
        self.create_snake()
        self.head = self.segments[0]


    def create_segment(self):
        """Receives a list of turtles and append 1 turtle to it"""
        new_seg = Turtle()
        new_seg.penup()
        new_seg.shape("square")
        new_seg.color("white")
        self.segments.append(new_seg)

    def create_snake(self):
        for i in range(3):
            self.create_segment()
        for i in range(3):
            coord = i * (- self.SEGMENT_SIZE)  # Desloca 20 unidades a esquerda para cada tartaruga criada
            self.segments[i].goto(coord, 0)

    def extend(self):
        self.create_segment()

    def move(self):
        snake_length = len(self.segments)
        for turtle_index in range(snake_length - 1, 0, -1):
            new_x = self.segments[turtle_index - 1].xcor()
            new_y = self.segments[turtle_index - 1].ycor()
            self.segments[turtle_index].goto(new_x, new_y)
        self.segments[0].forward(self.SEGMENT_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
