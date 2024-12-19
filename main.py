from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)


Player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(Player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if car.distance(Player) < 20:
            
            game_is_on = False
            scoreboard.game_over()


    if Player.is_at_finish_line():
        Player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()
           


screen.exitonclick()