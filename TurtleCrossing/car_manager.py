from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
START_POS = 18
END_POS = 40


class CarManager(Turtle):
    def __init__(self, y_pos):
        super(CarManager, self).__init__()
        self.y_pos = y_pos
        self.increment_move = 1.1
        self.start_move_speed = 5
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(20 * random.randint(START_POS, END_POS), self.y_pos)

    def move(self):
        new_x = self.xcor() - self.start_move_speed
        self.goto(new_x, self.ycor())
        if self.xcor() < -350:
            self.goto(20 * random.randint(START_POS, END_POS), self.y_pos)

    def increase_speed(self):
        self.start_move_speed *= self.increment_move

