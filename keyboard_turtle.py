import turtle
import random

tim = turtle.Turtle()

def up():
    tim.setheading(90)
    tim.forward(50)

def down():
    tim.setheading(270)
    tim.forward(50)

def left():
    tim.setheading(180)
    tim.forward(50)

def right():
    tim.setheading(0)
    tim.forward(50)

turtle.listen()

turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()  # This will make sure the program continues to run 