from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import os

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_head_images = {}

for direction in ['right', 'left', 'up', 'down']:
    snake_head_image = (os.path.expanduser(f"gifs/snake_head_{direction}.gif"))
    screen.register_shape(snake_head_image)
    snake_head_images[direction] = snake_head_image

# Task 1: Create a snake body
snake = Snake(snake_head_images)
food = Food()
scoreboard = Scoreboard()

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
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("Collision!")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False

    # Detect collision with tail
    # If head collides with any segment other than the head itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

if not game_is_on:
    scoreboard.game_over()

screen.exitonclick()
