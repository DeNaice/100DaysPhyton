import turtle as t
import random

tim = t.Turtle()
tim.speed()
color_list = ["dark magenta", "red", "yellow", "hot pink", "spring green", "cadet blue", "blue", "teal",
              "peach puff", "pale violet red", "navajo white", "deep pink", "tomato", "rosy brown"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    tim.color(random.choice(color_list))
