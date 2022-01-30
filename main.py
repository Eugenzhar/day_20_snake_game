import turtle as t
import random

screen = t.Screen()
screen.screensize(bg="black")
screen.setup(width=600, height=600)

screen.title("My Snake")

start_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in start_positions:
    tim = t.Turtle(shape="square")
    tim.color("white")
    tim.setposition(position)
    segments.append(tim)

gaming_is_not_over = True
while gaming_is_not_over:
    for seg in segments:
        seg.forward(20)





screen.exitonclick()
