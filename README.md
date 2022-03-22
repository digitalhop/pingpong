# pingpong
## The Ping Pong game!!!

### So I made this game using the Turtle module that comes with the standard Python library.

### How to Setup

Just Clone the repository and play the main.py file and that's it. No extra modules or anything

### How to Play

You can control the right pong using your 'Up' and 'Down' keys, against a very basic computer AI. I wanted to make it 2 players, but my keyboard only accepts
one input at a time and then blocks the other player from moving, so the answer was to build an AI.... I guess that's how all
great terminator stories start...

### Make AI Beatable

if you want to 'dumb' the AI down, then increase the self.pongTurnSkipCounter in the PongAI class. Or if you prefer an impossible
challenge then set it lower.

### Ball Speed

If you want to increase the speed of the ball, then increase the self.ballSpeed in the Ball class

Come to think of it, I should probably just add these as a prompt when the game starts... but then you
wouldn't get the satisfaction of changing it yourself...

### How does it work?

I used 3 Turtles instead of 1 stretched turtle, because I wanted to give some variation to the bounce when you hit
the ball on the edge of the Pong as opposed to the middle of the Pong. Then the 3 turtles move up or down a set amount of times

The basic ball trajectory is based on using a turtle heading and moving it forward.
