import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
cars=[]
i=0

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    i+=1
    if i%6==0:
        new_car=CarManager()
        cars.append(new_car)
    for car in cars:
        car.move()

    for car in cars:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset()
        cars[0].increase_level()

screen.exitonclick()
