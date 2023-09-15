from turtle import Turtle,Screen
Value = 20
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
         self.turtle_set = []
         self.create_snake()
         self.head = self.turtle_set[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtle(position)
        
    def add_turtle(self,position):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(position)
            self.turtle_set.append(turtle)
    def extend(self):
        self.add_turtle(self.turtle_set[-1].position())
    # def create_snake(self):
    #     x_cor = 0
    #     for object in range(3):
    #         turtle = Turtle("square")
    #         turtle.color("white")
    #         turtle.penup()
    #         turtle.goto(x_cor,0)
    #         x_cor -= 20 
    #         self.turtle_set.append(turtle)



    
    def move(self):   
        for set in range(len(self.turtle_set)-1,0,-1):
            x_cor = self.turtle_set[set-1].xcor()
            y_cor = self.turtle_set[set-1].ycor()
            self.turtle_set[set].goto(x_cor,y_cor)
        self.turtle_set[0].forward(Value)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def speed(self):
        self.speed("fastest")