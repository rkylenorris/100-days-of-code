import tkinter as tk


def button_clicked():
    my_label.config(text=user_input.get())
    print(user_input.get())


window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # how to add padding

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()  # positions the elements centered in the window if no args
# must position an element in the window for it to show up
# is not enough to merely create it
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# how to update things
my_label["text"] = "new text"
my_label.config(text="New Text", padx=50, pady=50)

# button

button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tk.Button(text="New Button")
new_button.grid(column=2, row=0)
# Entry

user_input = tk.Entry(width=15)
# user_input.insert(tk.END, "some text to begin with")
# print(user_input.get())
# user_input.pack()
user_input.grid(column=3, row=2)
# # text
# text = tk.Text(height=5, width=30)
# # puts cursor in textbox
# text.focus()
# text.insert(tk.END, "Example of multi-line text entry.")
# # gets current value in textbox at line 1 character 0
# print(text.get("1.0", tk.END))
# text.pack()
#
# # Spinbox
#
#
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
#
#
# def scale_used(value):
#     print(value)
#
#
# scale = tk.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
#
#
# def checkbutton_used():
#     print(checked_state.get())
#
#
# checked_state = tk.IntVar()
# checkbutton = tk.Checkbutton(text="Is it on?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # Radiobutton
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = tk.IntVar()
# radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# # Listbox
#
#
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = tk.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()  # needed to keep the window open while the user interacts
