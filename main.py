import turtle as t
import time
from snake import Snake
import random

screen = t.Screen()
screen.screensize(bg="black")
screen.setup(width=600, height=600)
screen.title("My Snake")
screen.tracer(0)

snake = Snake()

gaming_is_not_over = True
while gaming_is_not_over:
    screen.update()
    time.sleep(0.1)

    snake.move()







screen.exitonclick()
