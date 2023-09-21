from tkinter import *
window = Tk()
window.title("Mile-To-Kilo Convertor")
window.config(padx=50,pady=50)
miles_entry = Entry()
miles_entry.grid(column=1,row=0)

miles_label =Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

kilo_entry_label = Label(text="0")
kilo_entry_label.grid(column=1,row=1)

kilo_label = Label(text="Kilo")
kilo_label.grid(column=2,row=1)

def convert():
    miles = float(miles_entry.get())
    kilo = round(miles*1.609344)
    kilo_entry_label.config(text=f"{kilo}")
calculate_button = Button(text="Calculate",command=convert)
calculate_button.grid(column=1,row=2)
window.mainloop()