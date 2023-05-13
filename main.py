from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Task 1: Create a snake body
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Task 2: Move the snake
game_is_on = True
while game_is_on:
    # get the screen to update after all 3 segments move
    screen.update()
    # slow down a bit so we can see what happened after all 3 segments move once
    # this can be used to control speed of the snake
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
