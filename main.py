import turtle
import pandas
screen = turtle.Screen()
screen.title("GUESS THE STATES")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guessed_states = []
while len(correct_guessed_states) < 50:
    answer = screen.textinput(title="What's your guesssss!", prompt=f"{len(correct_guessed_states)}/50 States Correct").title()
    data = pandas.read_csv("50_states.csv")
    states_list = data["state"].to_list()
    state_data = data[data.state == answer]
    if answer == "Exit":
        missing_state =[]
        for state in states_list:
            if state not in correct_guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state).to_csv("states_need_to_learn.csv")
        break
    if answer in states_list and answer not in correct_guessed_states:
        correct_guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.pendown()
        t.write(answer)
