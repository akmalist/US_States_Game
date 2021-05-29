import turtle
import pandas
import csv

screen = turtle.Screen()

screen.title("U.S. States Game")
screen.setup(width=750, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for each_state in states:
            # states that user did not guess
            if each_state not in guessed_states:
                missing_states.append(each_state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        selected = data[data.state == answer_state]
        t.goto(int(selected.x), int(selected.y))
        t.write(answer_state, True, align="center")
        guessed_states.append(answer_state)






