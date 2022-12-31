import turtle
import pandas
from write import Write

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
states = Write()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
count = 0
states_guessed = []
# states_to_learn = []

while count < 50:
    screen.update()
    answer = screen.textinput(title=f"{count}/50 states correct", prompt="What is another states name?").title()
    if answer == "Exit":
        states_to_learn = [all_states for all_states in states_list if all_states not in states_guessed]
        print(states_to_learn)
        break

    if answer in states_list:
        row = data[data.state == answer]
        x_column = int(row.x)
        y_column = int(row.y)
        states.write_state(answer, x_column, y_column)
        states_guessed.append(answer)
        count += 1
    else:
        pass

learn = {

    "States": states_to_learn
}

learn_states = pandas.DataFrame(learn)
learn_states.to_csv("states_to_learn.csv")
