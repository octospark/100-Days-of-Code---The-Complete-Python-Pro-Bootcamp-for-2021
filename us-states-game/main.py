import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

t = turtle.Turtle()
t.penup()
t.hideturtle()

states_data = pandas.read_csv("50_states.csv")
states_names = states_data.state

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ").title()

print()
game_is_on = True
correct_count = 0
correct_guesses = set()

while game_is_on:
    if not states_names[states_names == answer_state].empty:
        x_cor = states_data.x[states_names == answer_state]
        y_cor = states_data.y[states_names == answer_state]
        if answer_state not in correct_guesses:
            t.goto(int(x_cor), int(y_cor))
            t.write(answer_state)
            correct_guesses.add(answer_state)
            correct_count += 1

    if answer_state == "Exit":
        break

    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct",
                                    prompt="What's another state's name? ").title()

# states_to_learn.csv

states_to_learn = set(states_data.state) - correct_guesses
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
print(states_to_learn)