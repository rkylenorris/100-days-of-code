from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 7, "normal")


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def write_state_name(self, x, y, state_name):
        self.goto(x, y)
        self.write(f"{state_name}", align=ALIGNMENT, font=FONT)
