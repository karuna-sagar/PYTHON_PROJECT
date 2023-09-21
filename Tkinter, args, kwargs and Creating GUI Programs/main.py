import tkinter
window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
my_label = tkinter.Label(text="I am Label",font=("Arial",24,"bold"))
# my_label.pack()
my_label.grid(column=0,row=0)
# my_label["text"] = "New Text"
my_label.config(text="New Text")

# button
def button_clicked():
    # print("I Am Clicked")
    new_text = input.get()
    my_label.config(text=new_text)
button = tkinter.Button(text="Click Me",command=button_clicked)
# button.pack()
button.grid(column=4,row=0)
# button 2
button = tkinter.Button(text="new button",command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

# input

input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=5,row=2)

window.mainloop()