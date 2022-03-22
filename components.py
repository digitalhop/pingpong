from turtle import Turtle
import time
import random


class CentreLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.pensize(5)
        self.pencolor('white')
        self.color('white')
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        self._drawLine()

    def _drawLine(self):
        while self.ycor() <= 300:
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.leftScore = 0
        self.rightScore = 0
        self._PrintScore()

    def _PrintScore(self):
        self.clear()
        self.pencolor('white')
        self.penup()
        self.hideturtle()
        self.goto(-150, 180)
        self.write(str(self.leftScore), font=('arial', 80, 'normal'))
        self.goto(90, 180)
        self.write(str(self.rightScore), font=('arial', 80, 'normal'))

    def updateScore(self, left=0, right=0):
        self.leftScore += left
        self.rightScore += right
        self._PrintScore()


class Pongs(Turtle):
    def __init__(self, screen, pongSpeed=0.1):
        super().__init__()
        self.pongSpeed = pongSpeed
        self.theScreen = screen
        self.leftPongTop = self._newPong(-500, 20)
        self.leftPongMiddle = self._newPong(-500, 0)
        self.leftPongBottom = self._newPong(-500, -20)
        self.rightPongTop = self._newPong(500, 20)
        self.rightPongMiddle = self._newPong(500, 0)
        self.rightPongBottom = self._newPong(500, -20)
        self.leftPongUp = False
        self.leftPongDown = False
        self.rightPongUp = False
        self.rightPongDown = False

    def _newPong(self, x, y):
        apong = Turtle()
        apong.penup()
        apong.shape('square')
        apong.setheading(90)
        apong.color('white')
        apong.goto(x, y)
        apong.speed('fastest')
        return apong

    def pongReset(self):
        self.leftPongTop.goto(-500, 20)
        self.leftPongMiddle.goto(-500, 0)
        self.leftPongBottom.goto(-500, -20)
        self.rightPongTop.goto(500, 20)
        self.rightPongMiddle.goto(500, 0)
        self.rightPongBottom.goto(500, -20)

    def setRightPongUp(self):
        self.rightPongUp = True
        self.rightPongDown = False

    def setRightPongDown(self):
        self.rightPongUp = False
        self.rightPongDown = True

    def setLeftPongUp(self):
        self.leftPongUp = True
        self.leftPongDown = False

    def setLeftPongDown(self):
        self.leftPongUp = False
        self.leftPongDown = True

    def movePongs(self):
        if self.rightPongMiddle.ycor() < 260 and self.rightPongUp == True:
            self.rightPongMiddle.forward(10)
            self.rightPongTop.forward(10)
            self.rightPongBottom.forward(10)
        elif self.rightPongMiddle.ycor() > -260 and self.rightPongDown == True:
            self.rightPongMiddle.backward(10)
            self.rightPongTop.backward(10)
            self.rightPongBottom.backward(10)
        if self.leftPongMiddle.ycor() < 260 and self.leftPongUp == True:
            self.leftPongMiddle.forward(10)
            self.leftPongTop.forward(10)
            self.leftPongBottom.forward(10)
        elif self.leftPongMiddle.ycor() > -260 and self.leftPongDown == True:
            self.leftPongMiddle.backward(10)
            self.leftPongBottom.backward(10)
            self.leftPongTop.backward(10)

        self.rightPongUp = False
        self.rightPongDown = False
        self.leftPongUp = False
        self.leftPongDown = False


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.theScreen = screen
        self.theBall = Turtle()
        self._createBall()

    def _createBall(self):
        self.theBall.penup()
        self.theBall.shape('circle')
        self.theBall.color('green')
        self.theBall.speed('fastest')
        self.theBall.setheading(180)

    def moveBall(self, pong, score):
        # if point scored
        if self.theBall.xcor() < -533:
            score.updateScore(right=1)
            self.theBall.setheading(0)
            self.theBall.goto(0, 0)
            pong.pongReset()
            time.sleep(1)
        if self.theBall.xcor() > 533:
            score.updateScore(left=1)
            self.theBall.setheading(180)
            self.theBall.goto(0, 0)
            pong.pongReset()
            time.sleep(1)
        # if ball hits top or bottom
        if self.theBall.ycor() > 280 or self.theBall.ycor() < -280:
            self.theBall.setheading(self._normaliseAngle(
                ((180 - self.theBall.heading())*2)+self.theBall.heading()))
        # if ball hits a pong
        if self.theBall.distance(pong.leftPongMiddle) < 20:
            self.theBall.setheading(
                self._normaliseAngle(random.randint(340, 380)))
        elif self.theBall.distance(pong.leftPongTop) < 20:
            self.theBall.setheading(random.randint(20, 60))
        elif self.theBall.distance(pong.leftPongBottom) < 20:
            self.theBall.setheading(random.randint(300, 340))
        if self.theBall.distance(pong.rightPongMiddle) < 20:
            self.theBall.setheading(
                random.randint(160, 200))
        elif self.theBall.distance(pong.rightPongTop) < 20:
            self.theBall.setheading(random.randint(120, 160))
        elif self.theBall.distance(pong.rightPongBottom) < 20:
            self.theBall.setheading(random.randint(200, 240))
        self.theBall.forward(5)

    def _normaliseAngle(self, theAngle):
        # if angle more than 360, then subtract 360
        if theAngle >= 360:
            return theAngle - 360
        else:
            return theAngle


class PongAI():
    def __init__(self, theBall: Ball, leftPong: Pongs):

        self.theBall = theBall
        self.leftPong = leftPong
        self.pongTurnSkipCounter = 0
        self.previousBallXCord = 0

    def movePong(self):
        if self.pongTurnSkipCounter % 3 == 0:
            # if ball moving away go to centre
            if self.theBall.theBall.xcor() < self.previousBallXCord:
                if -30 < self.leftPong.leftPongMiddle.ycor() - self.theBall.theBall.ycor() < 30:
                    pass
                else:
                    if self.leftPong.leftPongMiddle.ycor() > self.theBall.theBall.ycor():
                        self.leftPong.setLeftPongDown()
                    else:
                        self.leftPong.setLeftPongUp()
            else:
                if -30 > self.leftPong.leftPongMiddle.ycor():
                    self.leftPong.setLeftPongUp()
                elif 30 < self.leftPong.leftPongMiddle.ycor():
                    self.leftPong.setLeftPongDown()
            self.previousBallXCord = self.theBall.theBall.xcor()
        self.pongTurnSkipCounter += 1
