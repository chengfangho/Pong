from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    def bounce_y(self):
        self.y_move = -self.y_move
    def bounce_x_right(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9
    def bounce_x_left(self):
        self.x_move = abs(self.x_move)
        self.move_speed *= 0.9
    def reset(self):
        self.move_speed = 0.1
        self.goto(0,0)

