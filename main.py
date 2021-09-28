from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Scoreboard


screen = Screen()
screen.setup(width =800, height=600)
screen.title("Pong")
screen.bgcolor('black')
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=paddle1.move_up, key='Up')
screen.onkey(fun=paddle1.move_down, key='Down')
screen.onkey(fun=paddle2.move_up, key='w')
screen.onkey(fun=paddle2.move_down, key='s')

game_on = True

while game_on: 
    screen.update()
    time.sleep(0.07)
    ball.move_ball()

# Detect collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce() 

# Detect collision with right paddle 
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        
# Detect going out of field 

    if ball.xcor() > 400: 
        ball.reset_ball()
    
    if ball.xcor() < -400:
        ball.reset_ball()
screen.exitonclick()