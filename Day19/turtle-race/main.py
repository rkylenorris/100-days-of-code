from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_cor = -100
x_cor = -230
for color in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(x=x_cor, y=y_cor)
    all_turtles.append(t)
    y_cor += 50


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
