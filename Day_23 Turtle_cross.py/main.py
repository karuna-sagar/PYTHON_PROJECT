import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
score = Scoreboard()
car_manager = CarManager()
game_is_on = True
screen.listen()
screen.onkey(turtle.up,"www")
while game_is_on:
    time.sleep(turtle.mov_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_car:
        if car.distance(turtle)<30:
            game_is_on = False
    
    # if turtle.ycor() == 280:
    #     turtle.reset()
    
    if turtle.is_finish():
        turtle.go_start()
        score.increase()