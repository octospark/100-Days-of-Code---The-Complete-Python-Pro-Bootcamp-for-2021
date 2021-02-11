import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
#---------------------------- CONTROL ------------------------------#
def change_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(dictionary_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_content, text=f"{word['French']}", fill="black")
    canvas.itemconfig(background, image=front_image)
    flip_timer = window.after(3000, reveal_translation)

def reveal_translation():
    global word
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_content, text=f"{word['English']}", fill="white")
    canvas.itemconfig(background, image=back_image)

def is_known():
    dictionary_data.remove(word)
    data = pandas.DataFrame(dictionary_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()

try:
    csv_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    csv_data = pandas.read_csv("data/french_words.csv")
new_dict = {}
dictionary_data = pandas.DataFrame.to_dict(csv_data, orient="records")


window = tkinter.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR)
window.minsize(width=900, height=600)
window.config(padx=50, pady=20)

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = tkinter.PhotoImage(file="./images/card_front.png")
back_image = tkinter.PhotoImage(file="./images/card_back.png")

background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_content = canvas.create_text(400, 263, text="French", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

word = random.choice(dictionary_data)



no_image = tkinter.PhotoImage(file="./images/wrong.png", )
no_button = tkinter.Button(image=no_image, highlightthickness=-1, relief=tkinter.FLAT, command=change_word)
no_button.grid(row=1, column=0)

yes_image = tkinter.PhotoImage(file="./images/right.png", )
yes_button = tkinter.Button(image=yes_image, highlightthickness=-1, relief=tkinter.FLAT, command=is_known)
yes_button.grid(row=1, column=1)

flip_timer = window.after(3000, reveal_translation)

window.mainloop()