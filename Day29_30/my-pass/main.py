from tkinter import *
from tkinter import messagebox as mb
import string
from random import *
import pyperclip as pc
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = list(string.ascii_letters)
    nums = range(0, 10)
    syms = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_nums = [str(choice(nums)) for _ in range(randint(2, 4))]
    pass_syms = [choice(syms) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_syms + pass_nums

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pc.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        mb.showerror(title="Blank Fields", message="Please don't leave any fields blank!")
        return

    info_ok = mb.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {username}\nPassword: {password}\nIs it ok to save?"
    )

    if not info_ok:
        return

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    if len(website) == 0:
        mb.showerror(title="Blank Website Field", message="Can't search without a website!")
        return
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        mb.showerror(
            title="No Passwords Saved",
            message="You haven't saved any websites and passwords yet\nYou can't search."
        )
        return

    try:
        website_dict = data[website]
    except KeyError:
        mb.showerror(title="Invalid Website", message="Website does not exist in saved data.")
        website_entry.delete(0, END)
        return
    else:
        password = website_dict["password"]
        username = website_dict["email"]
        mb.showinfo(title=website, message=f"email: {username}\npassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass")
window.config(padx=50, pady=20)
window.iconbitmap("my_pass.ico")

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_entry = Entry(width=24)
website_entry.grid(column=1, row=1, sticky="E")

search_btn = Button(text="Search", command=search)
search_btn.grid(column=2, row=1)

email_entry = Entry(width=43)
email_entry.grid(column=1, columnspan=2, row=2, sticky="E", pady=3)
email_entry.insert(0, "rodermus@gmail.com")

pass_entry = Entry(width=24)
pass_entry.grid(column=1, row=3, sticky="e", padx=3)

generate_pass_btn = Button(text="Generate Password", command=generate_pass)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, columnspan=2, row=4, sticky="E", pady=3)


window.mainloop()
