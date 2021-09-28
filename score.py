from turtle import Turtle


# ALIGNMENT = 'center'
# FONT = "Courier"


class Scoreboard(Turtle): 
    def __init__(self): 
        super().__init__()
        self.color = 'white'
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.write(self.paddle2_score, align='center', font=('Courier', 80, 'normal'))
    