from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# GETTING WORDS
try:
    words_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    print("That file doesn't exist yet, using pre-made file.")
    words_df = pd.read_csv("data/french_words.csv")


words_dict = words_df.to_dict(orient="records")
to_learn_words = words_dict.copy()
new_word = ""


def get_next_word():
    random_word = choice(words_dict)
    return random_word


def update_french_word():
    global new_word
    new_word = get_next_word()
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=new_word["French"], fill="black")
    window.after(3000, flip_card)


def flip_card():
    global new_word
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=new_word["English"], fill="white")


def right_answer():
    global words_dict
    words_dict.remove(new_word)
    df = pd.DataFrame(words_dict)
    df.to_csv("data/words_to_learn.csv", index=False)

    update_french_word()


def wrong_answer():

    update_french_word()


# UI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.iconbitmap("images/flash-card.ico")

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, font=LANGUAGE_FONT, text="French")
word = canvas.create_text(400, 263, font=WORD_FONT, text="")
canvas.grid(row=0, column=0, columnspan=2)
update_french_word()

right = PhotoImage(file="images/right.png")
right_btn = Button(image=right, highlightthickness=0, bd=0.5, command=right_answer)
right_btn.grid(row=1, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong, highlightthickness=0, bd=0.5, command=wrong_answer)
wrong_btn.grid(row=1, column=0)


window.mainloop()
