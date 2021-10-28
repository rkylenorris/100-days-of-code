from tkinter import *
import winsound as ws
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .5  # 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = "✔"
check_marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps, check_marks
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
    canvas.itemconfig(timer_text, text="00:00")
    check_marks_label.config(text="")
    reps = 0
    check_marks = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #


def play():
    ws.PlaySound("Windows Exclamation.wav", ws.SND_FILENAME)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40))
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global check_marks
    minutes, secs = divmod(count, 60)  # does both division and modulo at the same time
    timer_str = f"{minutes}:{secs:02}"  # the :02 pads the string with an extra zero if need be
    canvas.itemconfig(timer_text, text=timer_str)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks += check_mark
            check_marks_label.config(text=check_marks, fg=GREEN, bg=YELLOW)
            play()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.iconbitmap("tomato.ico")  # to change icon to something else


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, bg="#ffffff", bd=0.2, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, bg="#ffffff", bd=0.2, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks_label = Label(fg=GREEN, bg=YELLOW)
check_marks_label.grid(column=1, row=3)

window.mainloop()
