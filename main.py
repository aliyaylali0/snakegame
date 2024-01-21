from turtle import Screen

import score
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SnakeGame")

snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.score_up()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.snake_reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.snake_reset()




screen.exitonclick()
