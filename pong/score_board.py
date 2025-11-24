from turtle import Turtle
FONT=("courier",20,"normal")
ALIGN="center"
class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x, y)
        self.keep_score()
    def keep_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
    def add_score(self):
        self.score+=1
        self.clear()
        self.keep_score()
    def reset(self):
        self.score = 0
