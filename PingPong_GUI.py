import turtle as t
import os
import RPi.GPIO as GPIO

# Score variables
player_a_score = 0
player_b_score = 0

win = t.Screen()  # creating a window
win.title("Ping-Pong Game")  # Giving name to the game.
win.bgcolor('black')  # providing color to the HomeScreen
win.setup(width=800, height=600)  # Size of the game panel
win.tracer(0)  # which speeds up the game.

# Creating left paddle for the game
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Creating a right paddle for the game
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(350, 0)

# Creating a pong ball for the game
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball_dx = 1.5  # Setting up the pixels for the ball movement.
ball_dy = 1.5

# Creating a pen for updating the Score
pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0 ", align="center", font=('Monaco', 24, "normal"))

# Initialize GPIO for left paddle
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # GPIO23 for left paddle up button
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # GPIO24 for left paddle down button

# Function to move the left paddle up
def paddle_left_up(channel):
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Function to move the left paddle down
def paddle_left_down(channel):
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Add event detection for left paddle buttons
GPIO.add_event_detect(23, GPIO.FALLING, callback=paddle_left_up, bouncetime=200)
GPIO.add_event_detect(24, GPIO.FALLING, callback=paddle_left_down, bouncetime=200)

# Keyboard binding for right paddle
def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Keyboard binding for right paddle
win.listen()
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

# Main Game Loop
while True:
    win.update()  # This method is mandatory to run any game

    # Rest of your game logic here
