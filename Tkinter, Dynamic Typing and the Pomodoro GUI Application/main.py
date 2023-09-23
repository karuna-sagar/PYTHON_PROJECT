from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text="00:00")
    timer_label.config("Timer")
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK",bg=YELLOW,fg=RED,font=(FONT_NAME,"50","bold"),highlightthickness=0)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK",bg=YELLOW,fg=PINK,font=(FONT_NAME,"50","bold"),highlightthickness=0)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK",bg=YELLOW,fg=GREEN,font=(FONT_NAME,"50","bold"),highlightthickness=0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Promdor")
window.config(padx=100,pady=50,bg=YELLOW)
timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,"50","bold"),highlightthickness=0)
timer_label.grid(column=1,row=0)

canva = Canvas(width=200,height=250,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="Day_28 Tkinter, Dynamic Typing and the Pomodoro GUI Application/tomato.png")
canva.create_image(103,125,image=tomato_image)
timer_text = canva.create_text(103,140,text="00:00",fill="white",font=(FONT_NAME,"28","bold"))
canva.grid(column=1,row=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)


reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(text="" ,bg=YELLOW,fg=GREEN ,highlightthickness=0)
check_mark.grid(column=1,row=3)
window.mainloop()