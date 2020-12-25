def follow(turtle, S, step=10, angle=90):
    turtle.hideturtle()

    for char in S:
        if char == 'F':
            turtle.forward(step)
        elif char == 'E':
            turtle.forward(step)
        elif char == 'L':
            turtle.left(angle)
        elif char == 'R':
            turtle.right(angle)

    turtle.showturtle()