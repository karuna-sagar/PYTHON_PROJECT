from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)
    def Up(self):
        y_cor = self.ycor() + 25
        self.goto(self.xcor(),y_cor)
    def Down(self):
        y_cor = self.ycor() - 25
        self.goto(self.xcor(),y_cor)
    

    