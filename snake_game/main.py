import time
import snake as s
import turtle as t
from food import Food
from scoreboard import Scoreboard

screen=t.Screen()
screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake=s.Snake()
food=Food()
scoreboard = Scoreboard()
game_is_on=True
while game_is_on:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()


    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 15:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()
