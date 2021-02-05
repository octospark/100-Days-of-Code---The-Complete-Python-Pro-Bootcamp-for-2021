from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, posision):
        super().__init__()
        self.goto(posision[0], posision[1])
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)



