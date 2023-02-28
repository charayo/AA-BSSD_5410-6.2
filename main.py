import turtle


def koch(t, order, size):
    """
    Make turtle t draw a KocH fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """

    if order == 0:      # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)
        t.right(180)


def main():
    size = 800

    screen = turtle.Screen()
    screen.setup(size + 20, size + 20)  # window size
    screen.screensize(size, size)  # drawing space
    screen.bgcolor("#90EE8F")
    screen.title("Turtle Koch Snowflake")

    turtle.penup()
    turtle.goto(-size / 8, size / 12)
    turtle.pendown()
    turtle.color("blue")
    turtle.pensize(2)
    turtle.shape(None)
    for i in range(3):
        koch(turtle, 4, 1800)
        turtle.right(120)
    turtle.done()


if __name__ == "__main__":
    main()