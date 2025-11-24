from turtle import Screen
from paddle_1 import Paddle
from ball import Ball
import time
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
game_is_on=True
screen.tracer(0)


paddle_1=Paddle(-350,0)
paddle_2 = Paddle(350,0)
screen.onkeypress(key="w", fun=paddle_1.move_up)
screen.onkeypress(key="s", fun=paddle_1.move_down)
screen.onkeypress(key="Up", fun=paddle_2.move_up)
screen.onkeypress(key="Down", fun=paddle_2.move_down)
ball=Ball()
player_1_score=ScoreBoard(x=-175,y=250)
player_2_score=ScoreBoard(x=175,y=250)
player_1=screen.textinput(title="Player 1",prompt="Who is the first player playing? ")
player_2=screen.textinput(title="Player 2",prompt="Who is the second player playing? ")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if( ball.distance(paddle_2) < 50 and ball.xcor()<340) or (ball.distance(paddle_1) < 50 and ball.xcor()>-340):
        ball.hit()
    if ball.xcor()>400:
        player_1_score.add_score()
        ball.reset()
        time.sleep(0.2)
    elif ball.xcor()<-400:
        player_2_score.add_score()
        ball.reset()
        time.sleep(0.2)
    if player_1_score.score >= 10:
      print(f"{player_1} is the winner!")
      game_is_on=False
    elif player_2_score.score >= 10:
        print(f"{player_2} is the winner!")
        game_is_on=False


screen.exitonclick()


