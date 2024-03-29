import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snack GamE")

screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor()>280 or snake.head.xcor()<(-280) or snake.head.ycor()>280 or snake.head.ycor()<(-280):
        game_is_on=False
        score.gameover()
    for i in snake.segments:
        if i == snake.head:
            pass
        elif snake.head.distance(i)<10:
            game_is_on = False
            score.gameover()
screen.exitonclick()
