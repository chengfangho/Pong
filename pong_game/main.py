from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(right_paddle)<50 and ball.xcor()>320:
        ball.bounce_x_right()
    if  ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x_left()
    if ball.xcor()>380:
        ball.reset()
        ball.bounce_x_right()
        scoreboard.left_point()
    if ball.xcor()<-380:
        ball.reset()
        ball.bounce_x_left()
        scoreboard.right_point()
    scoreboard.update()
screen.exitonclick()