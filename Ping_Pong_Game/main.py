from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreCard
import time
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.setup(width=800,height=600)
my_screen.tracer(0)
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
ball  = Ball()
score = ScoreCard()
my_screen.listen()
my_screen.onkey(paddle_r.Up,"Up")
my_screen.onkey(paddle_r.Down,"Down")
my_screen.onkey(paddle_l.Up,"w")
my_screen.onkey(paddle_l.Down,"s")
is_on = True
while is_on:
        time.sleep(ball.mov_speed)
        my_screen.update()
        ball.move()
        #ball detection with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()
        #ball detection with r_paddle
        if ball.distance(paddle_r) < 50 and ball.xcor()>320 or ball.distance(paddle_l) < 50 and ball.xcor()<-320:
                ball.bounce_x() 
        if ball.xcor()>380:
                ball.reset()
                score.l_point()
                
        if ball.xcor()<-380:
                ball.reset()
                score.r_point() 
        
my_screen.exitonclick()