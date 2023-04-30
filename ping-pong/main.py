from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# game UI
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

# paddle
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

# ball
ball = Ball()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect missed paddle collision
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
