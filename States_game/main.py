import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
t=turtle.Turtle()
t.shape(image)

data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
guess_state=[]
while len(guess_state)<50:
    ans_state=screen.textinput(title=f"{len(guess_state)}/50 States Correct",prompt="What's another state's name?")
    ans_state=ans_state.title()
    if ans_state=="Exit": break
    if ans_state in states:
        state_cor=data[data["state"] == ans_state]
        guess_state.append(ans_state)
        x=int(state_cor.x.item())
        y=int(state_cor.y.item())
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x,y)
        writer.write(ans_state, align="center", font=("Arial", 10, "bold"))

not_guess=[]
for st in states:
    if st not in guess_state:
        not_guess.append(st)
df=pandas.DataFrame(not_guess,columns=["state"])
df.to_csv("not_guess_states.csv")
