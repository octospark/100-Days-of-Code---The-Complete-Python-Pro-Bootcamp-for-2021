from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.reset_player()

    def reset_player(self):
        self.clear()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    def move(self):
        self.forward(MOVE_DISTANCE)

    def passed_level(self):
        return self.ycor() > FINISH_LINE_Y
