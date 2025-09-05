from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SQUARE_SIDE = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# GAME STARTING

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# MOVING SNAKE
game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    sleep(0.1)

    #Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    #defect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



# TURNING SNAKE



screen.exitonclick()
