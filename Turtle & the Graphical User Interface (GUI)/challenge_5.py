from turtle import Turtle,Screen
import random
# colors = ["tan","light pink","dark magenta","medium orchid","medium violet red","orange","yellow"]
# direction = [0,90,180,270]
my_screen = Screen()
my_screen.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
turtle = Turtle()
turtle.shape("arrow")
turtle.speed("fastest")
turtle.pensize(1.5)
for i in range(75):
    turtle.color(random_color())
    turtle.circle(150)
    turtle.left(5)


# turtle.pensize(15)
# turtle.speed("fastest")
# for i in range(100):
#     turtle.forward(30)
#     turtle.setheading(random.choice(direction))
#     turtle.color(random.choice(colors))


my_screen.exitonclick()