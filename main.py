from turtle import Screen,Turtle
import time
from score_board import Scoreboard
from snake import Snake
from food import Food

screen=Screen()
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left" )
screen.onkey(snake.right,"Right")

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

#screen tracer used to hold the screen or to on off the screen animation
screen.tracer(0)

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    #detect the food is collided with snake
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:

        scoreboard.reset()
        snake.reset()

#detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()





































screen.exitonclick()