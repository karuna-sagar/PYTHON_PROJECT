from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_area.insert(0,password)
    # for char in password_list:
    #     password += char

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_area.get()
    website = website_area.get()
    email = email_area.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="Error",message="Some Field are empty.First Enter the that Field\n")
    else:
        try:
            with open("data.json","r") as data_files:
                data = json.load(data_files)
                
        except FileNotFoundError:
            with open("data.json","w") as data_files:
                json.dump(new_data,data_files,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_files:
                json.dump(data,data_files,indent=4)
        finally:
            website_area.delete(0,END)
            password_area.delete(0,END)
def find_password():
    website = website_area.get()
    try:
        with open("data.json") as data_files:
            data = json.load(data_files)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="File not Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"{email}\n{password}\n")
        else:
            messagebox.showinfo(title="Eroor",message=f"no details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canva = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canva.create_image(100,100,image=logo)
canva.grid(row=0,column=1)


website_label = Label(text="Website")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)
password_label =  Label(text="Password")
password_label.grid(column=0,row=3)

website_area = Entry(width=20)
website_area.grid(column=1,row=1)
email_area = Entry(width=37)
email_area.insert(0,"shudhanshusingh160@gmail.com")
email_area.grid(column=1,row=2,columnspan=2)
password_area = Entry(width=20)
password_area.grid(column=1,row=3)

gen_button = Button(text="Generate Password",command=generate_password)
gen_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)





window.mainloop()