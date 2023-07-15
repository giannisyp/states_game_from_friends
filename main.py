import turtle
import pandas
from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
guessed_states = []
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
missing_states = state_list

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?").title()
    if answer_state == "Exit":
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        missing_states.remove(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv
data_dict = {
    "states missed": missing_states
}
df = pandas.DataFrame(data_dict)
df.to_csv("missing_states.csv")


