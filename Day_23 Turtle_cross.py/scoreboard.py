from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280,250)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)
    def increase(self):
        self.level += 1
        self.update_score()
        