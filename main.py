import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

screen = t.Screen()
screen.screensize(bg="black")
screen.setup(width=600, height=600)
screen.title("My Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gaming_is_not_over = True
while gaming_is_not_over:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #detect colision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1







screen.exitonclick()
