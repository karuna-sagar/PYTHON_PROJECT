from turtle import Turtle,Screen
import random
my_screen = Screen()
my_screen.colormode(255)
color_list = [(52,93,124),(172,154,40),(140,30,19),(66, 245, 158),(18, 201, 36),(181, 214, 13),(214, 130, 13),(214, 73, 13),(214, 36, 13),(110, 13, 214),(147, 13, 214),(214, 13, 63),(214, 13, 43)]
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
turtle = Turtle()
turtle.shape("arrow")
turtle.speed("fastest")
turtle.penup()
# turtle.setheading(random.choice(color_list))
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
turtle.hideturtle()


number_of_dots = 100
for count_dots in range(1,number_of_dots+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if count_dots%10==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
my_screen.exitonclick()
