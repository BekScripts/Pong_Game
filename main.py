from turtle import Screen
from my_pads import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width= 800, height= 600)
screen.bgcolor('black')
screen.title("Pong Game")

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
screen.listen()
score = ScoreBoard()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


n = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -270:
       ball.bounce_y()

    if ball.distance(right_paddle) < 70 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(left_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390:
        score.increase_left_score()
        ball.reset_game()

    if ball.xcor() < -395:
        score.increase_right_score()
        ball.reset_game()

    if score.right_score == 10 or score.left_score == 10:
        game_is_on = False




screen.exitonclick()
