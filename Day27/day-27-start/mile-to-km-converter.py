import tkinter as tk


def calc_miles_to_km():
    miles = int(user_input.get())
    km = round(miles / 0.62137)
    result_label.config(text=str(km))


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

user_input = tk.Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tk.Button(text="Calculate", command=calc_miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()
