import sys
import turtle
import pandas as pd
from writer import Writer
from tkinter import messagebox
import getpass

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

writer = Writer()

states_coordinates = pd.read_csv("50_states.csv")

counter = 0

input_title = f"Guesses: {counter}/50"
input_prompt = "Enter a State name\nClick Cancel To Exit"

guessed_states = []
all_states = states_coordinates['state'].tolist()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=input_title, prompt=input_prompt)
    if answer_state:
        answer_state = answer_state.title()
    else:
        missing_states = [state for state in all_states if state not in guessed_states]
        break

    if answer_state in guessed_states:
        messagebox.showerror(
            title="ALREADY GUESSED",
            message="That state is already on the board. You will not be penalized, try again"
        )
        continue

    counter += 1

    if states_coordinates["state"].str.contains(answer_state).any():
        guessed_states.append(answer_state)
        answer_wrong = False
        state_data = states_coordinates[states_coordinates['state'] == answer_state]
        x_coordinate = int(state_data.x)
        y_coordinate = int(state_data.y)
        writer.write_state_name(x_coordinate, y_coordinate, answer_state)
        input_title = f"Guesses: {counter}; Correct: {len(guessed_states)}"
        input_prompt = "CORRECT! Guess another State name!\nClick Cancel To Exit"
    else:
        input_title = f"Guesses: {counter}; Correct = {len(guessed_states)}"
        input_prompt = "INCORRECT! Guess another State name!\nClick Cancel To Exit"
        messagebox.showerror(title="INCORRECT", message="That state cannot be found, double check your spelling")

messagebox.showinfo(
    title="GAME OVER",
    message=f"You guessed {len(guessed_states)} out of 50 states correctly in {counter} guesses"
)

if len(missing_states) > 0:
    missing_states.sort()
    state_dict = {'state': missing_states}
    df = pd.DataFrame(state_dict)
    username = getpass.getuser()
    csv_path = f"/Users/{username}/Desktop/states_to_learn.csv"
    df.to_csv(csv_path, index=False)
    messagebox.showinfo(
        title="States to Learn",
        message=f"A csv of states you still need to learn\nhas been saved as 'states_to_learn.csv' on your desktop"
    )

screen.bye()
sys.exit(0)
