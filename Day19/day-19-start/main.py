from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def reset():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


def counter_clockwise():
    tim.setheading(tim.heading() + 10)


def clockwise():
    tim.setheading(tim.heading() - 10)


screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=reset)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.exitonclick()
