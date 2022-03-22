from turtle import Screen
from components import *
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1066, height=600)
screen.tracer(False)
screen.listen()
centreLine = CentreLine()
score = Score()
pong = Pongs(screen)
ball = Ball(screen)
pongAI = PongAI(ball, pong)

screen.onkeypress(pong.setRightPongUp, 'Up')
screen.onkeypress(pong.setRightPongDown, 'Down')
screen.onkeypress(pong.setLeftPongUp, 'e')
screen.onkeypress(pong.setLeftPongDown, 'd')

while True:
    time.sleep(.01)
    pongAI.movePong()
    pong.movePongs()
    ball.moveBall(pong, score)
    screen.update()
