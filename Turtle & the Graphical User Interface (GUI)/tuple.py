from turtle import Turtle,Screen

import random
my_screen = Screen()

my_screen.colormode(255)
direction = [0,90,180,270]
turtle = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
turtle.shape("arrow")
turtle.pensize(15)
turtle.speed("fastest")       
for i in range(100):
    turtle.forward(30)
    turtle.setheading(random.choice(direction))
    turtle.color(random_color())
my_screen.exitonclick()