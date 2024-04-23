import turtle

arrow = turtle.Turtle()

# Ask the user: "How many times do you want to move?: "

times = input('How many times do you want to move? Enter a number greater than 0: ')

for t in range(int(times)):
    direction = input ('In which direction do you want to turn (l or r): ')

    degrees = input('How many degrees do you want to turn?: ') 

    if direction == 'l':
        arrow.left(int(degrees))
    elif direction == 'r':
        arrow.right(int(degrees))

    steps = input ('How many steps do you want to move? Enter a number from 50 onwards: ')
    arrow.forward (int(steps))

turtle.done()