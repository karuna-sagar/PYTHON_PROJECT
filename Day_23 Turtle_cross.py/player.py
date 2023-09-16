from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.mov_speed = 0.1
    def up(self):
        # y_cor = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(),y_cor)
        self.forward(MOVE_DISTANCE)
    
    # def reset(self):
    #     self.goto(STARTING_POSITION)

    def is_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
    def go_start(self):
        self.goto(STARTING_POSITION)
        self.mov_speed *=0.5