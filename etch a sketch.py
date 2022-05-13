import turtle
from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()


def forward():
    jim.forward(10)


def backward():
    jim.backward(10)


def clockwise():
    jim.right(10)


def anti_clock():
    jim.left(10)


def clear_drawing():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=anti_clock)
screen.onkeypress(key="c", fun=clear_drawing)

screen.exitonclick()
