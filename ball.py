from turtle import Turtle
import random

# MOVE_DIST = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
    def move_ball(self): 
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
    def bounce(self): 
        self.y_move = self.y_move * -1
        
    def paddle_bounce(self): 
        self.x_move = self.x_move * -1
        
    def reset_ball(self):
        self.x_move = self.x_move * -1
        self.goto(0, 0)
       