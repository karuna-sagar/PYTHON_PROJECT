from turtle import Turtle,Screen
import random
my_screen = Screen()
my_screen.setup(width=500,height=400)
colors = ["red","blue","brown","pink","green","orange"]
user_choice = my_screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Make a choice")
all_turtle = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    y = -150 + (i*60)
    new_turtle.goto(-230,y)
    all_turtle.append(new_turtle)
if user_choice:
    is_on = True
while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 210:
            is_on = False
            # print(turtle.color())
            winning_color = turtle.pencolor()
            # print(winning_color)
            if user_choice == winning_color:
                print(f"You Won! the {winning_color} turtle is winner")
            else:
                print(f"You Loose! the {winning_color} turtle is winner")
        random_number = random.randint(1,10)
        turtle.forward(random_number)
my_screen.exitonclick()