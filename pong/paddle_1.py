from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_position,y_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,1)
        self.forward(20)
        self.goto(x_position,y_position)
    def move_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
    def move_down(self):
        if self .ycor() > -210:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)