import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
scoreboard = Scoreboard()
screen.onkeypress(player.move, key="Up")

cars = []
limit_of_cars = 30
for i in range(7):
    cars.append(CarManager(random.randint(-250, 250)))

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if int(time.time()*10) % 10 == 0 and len(cars) != limit_of_cars:
        cars.append(CarManager(10 * random.randint(-25, 25)))
    for car in cars:
        car.move()
    screen.update()

    # Detect level passage
    if player.passed_level():
        player.reset_player()
        scoreboard.update_scoreboard()
        for car in cars:
            car.increase_speed()

    # Detect collision with car
    for car in cars:
        if car.distance(player) < 20:
            k = GameOver()
            game_is_on = False


screen.exitonclick()