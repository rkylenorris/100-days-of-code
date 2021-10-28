# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("MediumPurple")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

import turtle as t
from random import randint, choice

tim = t.Turtle()
t.colormode(255)
tim.width(7)
tim.speed(50)

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(
                randint(0, 255),
                randint(0, 255),
                randint(0, 255)
            )
    tim.setheading(choice(directions))
    tim.forward(50)

# for i in range(3, 11):
#     angle = 360 // i
#     tim.color(
#         randint(0, 255),
#         randint(0, 255),
#         randint(0, 255)
#     )
#     for _ in range(i):
#         tim.right(angle)
#         tim.forward(100)





screen = t.Screen()
screen.exitonclick()
