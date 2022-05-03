from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.generate_car()

    def generate_car(self):
        start_x = 400
        start_random_y = random.randint(-550, 550)
        self.goto(start_x, start_random_y)

    def move_car(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())
    pass
