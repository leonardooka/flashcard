import random
from tkinter import *

import pandas


BACKGROUND_COLOR = "#B1DDC6"
english_word = ""
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("en-br.csv")
to_learn = data.to_dict(orient="records")
english_word = {}


def next_card():
    global english_word, timer
    window.after_cancel(timer)
    english_word = random.choice(to_learn)
    canvas.itemconfig(card_word, text=english_word['ingles'], fill='black')
    canvas.itemconfig(card_title, text="English", fill='black')
    canvas.itemconfig(card_image, image=cardfront_image)
    timer = window.after(3000, back_card)

def back_card():
    canvas.itemconfig(card_image, image=cardback_image)
    canvas.itemconfig(card_title, fill='white', text="Português")
    canvas.itemconfig(card_word, fill='white', text=english_word['portugues'])

def is_known():
    to_learn.remove(english_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Learn English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, back_card)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
cardback_image = PhotoImage(file="images/card_back.png")
cardfront_image = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(400, 263, image=cardfront_image)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="english_word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=wrong_image, highlightthickness=0,
                        borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_image, highlightthickness=0,
                      borderwidth=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()








window.mainloop()
