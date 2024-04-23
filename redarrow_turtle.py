import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
player = turtle.Turtle()
player.color("red")
player.penup()

# Set the speed of the turtle
speed = 1

# Define functions to move the turtle in different directions
def move_up():
    player.setheading(90)
    player.forward(speed)

def move_down():
    player.setheading(270)
    player.forward(speed)

def move_left():
    player.setheading(180)
    player.forward(speed)

def move_right():
    player.setheading(0)
    player.forward(speed)

# Bind the functions to the arrow keys
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Start listening for key events
screen.listen()

# Keep the window open
turtle.done()