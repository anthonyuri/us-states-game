import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

program_start = True


data = pandas.read_csv("50_states.csv")

states_correct = 0
title = 'Guess the State'
guessed_states = []

while program_start:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()

    if answer_state == "Exit":

        # states_needed = []
        # for state in data.state.to_list():
        #     if state not in guessed_states:
        #         states_needed.append(state)

        states_needed = [state for state in data.state.to_list() if state not in guessed_states]

        print(states_needed)



        new_data = pandas.DataFrame(states_needed)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in data.state.values and answer_state not in guessed_states:
        row_data = data[data.state == answer_state]
        position = (int(row_data.x), int(row_data.y))
        guessed_states.append(answer_state)
        b = turtle.Turtle()
        b.hideturtle()
        b.up()
        b.goto(position)
        b.write(f"{answer_state}", align="center", font=("Comic Sans",
                                            8, "normal"))
        states_correct += 1
        title = f"{states_correct}/50 States Correct"
        print(position)

    if states_correct == 50:
        program_start = False
        screen.clear()
        a = turtle.Turtle()
        a.hideturtle()
        a.up()
        a.goto(0,0)

        a.write(f"Congrats! You know all 50 states in the U.S.", align="center", font=("Times New Romans",
                                                                      20, "bold"))
        loop = True
        while loop:
            screen.bgcolor("red")
            time.sleep(.5)
            screen.bgcolor("white")
            time.sleep(.5)
            screen.bgcolor("blue")
            time.sleep(.5)

        print()


# states_to_learn.csv

# states_needed = []
# print(data.state.to_list())
# for state in data.state.to_list():
#     if state not in guessed_states:
#         states_needed.append(state)

# new_data = pandas.DataFrame(states_needed)
# new_data.to_csv("states_to_learn.csv")
