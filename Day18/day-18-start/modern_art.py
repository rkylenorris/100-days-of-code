# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

rgb_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


import turtle as t
from random import choice

t.colormode(255)
tim = t.Turtle()
tim.goto(0, 0)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

def draw_row():
    for _ in range(10):
        color_choice = choice(rgb_colors)
        tim.color(color_choice)
        tim.fillcolor(color_choice)
        # tim.begin_fill()
        tim.dot(20, color_choice)
        # tim.end_fill()
        tim.penup()
        tim.forward(50)
        tim.pendown()


for i in range(10):
    draw_row()
    tim.penup()
    if i % 2 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)
    tim.forward(50)
    tim.pendown()


screen = t.Screen()
screen.exitonclick()
