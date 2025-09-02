# from colorgram import extract
#
# extracted_colors = extract('painting.jpg', 8)
#
# used_colors = []
#
# for color in extracted_colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     new_color = (r, g, b)
#     used_colors.append(new_color)
# print(used_colors)

from random import choice
from turtle import Turtle
from turtle import colormode
from turtle import Screen

color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95)]
turtle = Turtle()
turtle.penup()
colormode(255)
screen = Screen()
screen.setup(1000, 1000, 0, -800)

position = [-450, -450]
turtle.goto(position[0], position[1])

for _ in range(10):
    position[0] = -450
    turtle.goto(position[0], position[1])
    for _ in range(10):
        turtle.dot(20, choice(color_list))

        position[0] += 50
        turtle.goto(position[0], position[1])
    position[1] += 50
