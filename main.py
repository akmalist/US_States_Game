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

states = data.state

guess = 0
game_on = True
while game_on:
    answer_state = screen.textinput(f"{guess}/50 States Correct", prompt="What's another state name?").title()
    for each_state in states:
        if answer_state == each_state and guess != 50:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            selected = data[data.state == each_state]
            selected_x = selected.x.values[0]
            select_y = selected.y.values[0]
            print(select_y)
            t.goto(selected_x, select_y)
            t.write(answer_state, True, align="center")
            guess += 1

screen.exitonclick()
