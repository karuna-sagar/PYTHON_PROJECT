from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
import random


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card,flip_time
    window.after_cancel(flip_time)
    current_card= random.choice(to_learn)
    # k = text["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_time = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)
def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))
    known_word = pandas.DataFrame(to_learn)
    known_word.to_csv("data/words_to_learn.csv",index=None)
    next_card()
window = Tk()
window.title("Flashy")
flip_time = window.after(3000,func=flip_card)
window.config(padx= 50,pady=50,bg=BACKGROUND_COLOR)
canvas = Canvas(width=800,height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)


card_title = canvas.create_text(400,150,text="Title",font=("Ariel" , 40, "italic"))
card_word = canvas.create_text(400,256,text="Word",font=("Ariel" , 60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)

correct_img = PhotoImage(file="images/right.png")
known_button = Button(image=correct_img,highlightthickness=0,command=is_known)
known_button.grid(column=1,row=1)

next_card()
window.mainloop()