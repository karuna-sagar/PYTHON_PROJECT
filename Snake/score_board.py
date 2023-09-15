from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        # self.write(f"Score: {self.score}" ,align="center", font=("Arial",15,"normal"))
        self.update()

    def update(self):
        self.write(f"Score: {self.score}" ,align="center", font=("Arial",15,"normal"))
    
    def game_over(self):
            self.goto(0,0)
            self.write(f"GAME OVER\n Your Score is: {self.score}" ,align="center", font=("Arial",15,"normal"))
    def increase(self):
        self.score+=1
        self.clear()
        self.update()
