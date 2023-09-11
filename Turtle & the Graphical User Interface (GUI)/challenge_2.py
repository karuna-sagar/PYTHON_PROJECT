from turtle import Turtle,Screen

turtle = Turtle()
turtle.color("red")
turtle.shape("arrow")
for i in range(25):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


my_screen = Screen()
my_screen.exitonclick()