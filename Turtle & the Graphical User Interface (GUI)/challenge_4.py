from turtle import Turtle,Screen
import random
colors = ["tan","light pink","dark magenta","medium orchid","medium violet red","orange","yellow"]
direction = [0,90,180,270]
turtle = Turtle()
turtle.shape("arrow")
turtle.pensize(15)
turtle.speed("fastest")
for i in range(100):
    turtle.forward(30)
    turtle.setheading(random.choice(direction))
    turtle.color(random.choice(colors))
my_screen = Screen()
my_screen.exitonclick()