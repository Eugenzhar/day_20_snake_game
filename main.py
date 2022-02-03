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
        snake.extend()
        scoreboard.increase_score()

    #detect collision with the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        print("game over")
        gaming_is_not_over = False
        scoreboard.game_over()

    #detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gaming_is_not_over = False
            scoreboard.game_over()





screen.exitonclick()
