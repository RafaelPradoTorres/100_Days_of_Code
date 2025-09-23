from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv('./data/french_words.csv')
french_dict = df.to_dict(orient="records")
chosen = {}

def flip_card():
    global back_img
    canvas.itemconfig(card_img, image=back_img)

    global chosen
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=chosen["English"], fill="White")

def next_card():
    global front_img, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_img, image=front_img)

    global chosen
    chosen = choice(french_dict)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=chosen["French"], fill="Black")

    flip_timer = window.after(3000, func=flip_card)

# -------------------- Estrutura frente ------------------------------------------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Image
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file='./images/card_back.png')
front_img = PhotoImage(file='./images/card_front.png')
card_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# NO
img_wrong = PhotoImage(file='./images/wrong.png')
button_wrong = Button(image=img_wrong, background=BACKGROUND_COLOR, highlightthickness=0)
button_wrong.grid(row=1, column=0)

#YES
img_right = PhotoImage(file='./images/right.png')
button_right = Button(image=img_right, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)

next_card()
# ===================================================================================================================



window.mainloop()