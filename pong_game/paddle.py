from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
    def up(self):
        self.goto(self.xcor(), self.ycor()+30)
    def down(self):
        self.goto(self.xcor(), self.ycor()-30)
       
        
