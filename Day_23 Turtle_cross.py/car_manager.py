from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self .all_car = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            car = Turtle("square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            y_cor = random.randint(-250,250)
            car.goto(300,y_cor)
            self.all_car.append(car)
    def move_car(self):
        for cars in self.all_car:
            cars.backward(STARTING_MOVE_DISTANCE)