from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forwards():
    tim.forward(10)


def backwards():
    tim.forward(-10)


def rotate_right():
    tim.right(10)


def rotate_left():
    tim.left(10)


def clear_turtle():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.pendown()


screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=rotate_left, key="a")
screen.onkey(fun=rotate_right, key="d")
screen.onkey(fun=clear_turtle, key="c")

screen.exitonclick()
