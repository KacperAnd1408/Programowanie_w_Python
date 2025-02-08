import turtle
from turtle import Turtle
import time
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
data_states = data.state.to_list()
right_guesses = 0
right_states = []

game_is_on = True

while game_is_on:

    if right_guesses != 50:
        answer_state = screen.textinput(title=f"{right_guesses}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            # states_list = []
            # for state in data_states:
            #     if state not in right_states:
            #         states_list.append(state)
            states_list = [state for state in data_states if state not in right_states]
            missing_states = pandas.DataFrame(states_list)
            missing_states.to_csv("missing_states.csv")
            break
        if answer_state in data_states:
            if answer_state in right_states:
                pass
            else:
                right_states.append(answer_state)
                right_guesses += 1
                user_state = data[data.state == f"{answer_state}"]
                x = int(user_state.x)
                y = int(user_state.y)
                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.write(arg=f"{answer_state}", move=False, align="center", font=("Arial", 8, "normal"))
        else:
            continue
    else:
        game_is_on = False


