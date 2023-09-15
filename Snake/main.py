from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from score_board import Score_Board
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

my_screen.setup(width=600,height=600)
snake = Snake()
food = Food()
score_board = Score_Board()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.Down,"Down")
my_screen.onkey(snake.Left,"Left")
my_screen.onkey(snake.Right,"Right")
my_screen.onkey(snake.speed ,"w")
is_on = True

while is_on:
    my_screen.update()
    time.sleep(0.08 )
    snake.move()
    # Detect eating  food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase()
    # detect collison
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score_board.game_over()
        is_on = False
    for object in snake.turtle_set[1:]:
        # if snake.head == object:
        #     pass
        if snake.head.distance(object) < 10:
            score_board.game_over()
            is_on = False
my_screen.exitonclick()