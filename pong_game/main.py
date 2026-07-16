import time
import turtle as t
from paddle import Paddle
from scoreboard import Scoreboard

from ball import Ball

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

left_paddle=Paddle(-350,0)
right_paddle=Paddle(350,0)
ball=Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

is_game_on = True
touch=False
while is_game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
