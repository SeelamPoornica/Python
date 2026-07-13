import turtle as t
import random as r
screen=t.Screen()

is_on_race=False
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle win the race?\nEnter the color")
colors=["red","green","blue","yellow","orange","purple"]
if user_bet:
    is_on_race=True
turtles=[]
y=-70
for i in range(len(colors)):
    turtles.append(t.Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-230,y)
    y=y+30

while is_on_race:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_on_race=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You won!The {winning_color} turtle is the winner!")
            else:
                print(f"You lost!The {winning_color} turtle is the winner!")
        goto=r.randint(0,10)
        turtle.forward(goto)

screen.exitonclick()
