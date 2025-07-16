# turtle_race/turtle_setup.py

from turtle import Turtle
from .constants import START_LINE_X, Y_POSITIONS, COLORS, SCREEN_HEIGHT, FINISH_LINE_X

def create_turtles():
    turtles = []
    for i, color in enumerate(COLORS):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=START_LINE_X, y=Y_POSITIONS[i])
        turtles.append(new_turtle)
    return turtles

def draw_finish_line():
    finish_line = Turtle(visible=False)
    finish_line.penup()
    finish_line.goto(FINISH_LINE_X, -SCREEN_HEIGHT / 2)
    finish_line.setheading(90)
    finish_line.pendown()
    finish_line.forward(SCREEN_HEIGHT)
    finish_line.penup()
    finish_line.goto(FINISH_LINE_X, SCREEN_HEIGHT / 2 - 20)
    finish_line.write("🏁", align="center", font=("Arial", 24, "bold"))
