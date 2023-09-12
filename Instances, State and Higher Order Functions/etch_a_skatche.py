from turtle import Turtle,Screen
turtle = Turtle()
my_screen = Screen()
my_screen.listen()
def move_forwards():
    turtle.forward(200)
def move_backward():
    turtle.backward(200)
def counter_clockwise():
    for i in range(10):
        turtle.left(5)
def clockwise():
    for i in range(10):
        turtle.right(5)
my_screen.onkey(key="w",fun=move_forwards)
my_screen.onkey(key="s",fun=move_backward)
my_screen.onkey(key="a",fun=counter_clockwise)
my_screen.onkey(key="d",fun=clockwise)
my_screen.exitonclick()