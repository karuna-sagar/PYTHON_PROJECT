from turtle import Turtle,Screen
import random
colors = ["tan","light pink","dark magenta","medium orchid","medium violet red","orange","yellow"]
turtle = Turtle()
turtle.shape("arrow")
num_side = 5
def shape(num_side):
    for i in range(num_side):
        angel = 360 / num_side
        turtle.forward(100)
        turtle.right(angel)
for num_side in range(3,11):
    turtle.color(random.choice(colors))
    shape(num_side)

my_screen = Screen()
my_screen.exitonclick()