from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        # So we don't need to look at the animation of the food being created
        self.speed("fastest")

        self.refresh()

    def refresh(self):
        random_x = random.randint(-13, 13) * 20
        random_y = random.randint(-13, 13) * 20
        self.goto(random_x, random_y)
