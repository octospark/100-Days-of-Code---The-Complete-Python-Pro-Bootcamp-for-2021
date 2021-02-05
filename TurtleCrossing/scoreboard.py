from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", font=FONT)
        self.level += 1


class GameOver(Turtle):
    def __init__(self):
        super(GameOver, self).__init__()
        self.color("black")
        self.hideturtle()
        self.write(f"Game Over", align="center", font=FONT)