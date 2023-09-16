from turtle import Turtle,Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # circle.shapesize()
        self.color("white")
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.mov_speed = 0.1
    def move(self):
        new_x =self.xcor() + self.x_mov 
        new_y =self.ycor() + self.y_mov 
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_mov *= -1
    def bounce_x(self):
        self.x_mov *= -1
        self.mov_speed *=0.9
    def reset(self):
        self.goto(0,0)
        self.mov_speed = 0.1
        self.bounce_x()
    