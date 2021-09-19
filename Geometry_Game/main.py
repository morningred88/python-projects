import turtle

# Create a canvas instance
my_turtle = turtle.Turtle()

# Go to a certain coordinate
my_turtle.penup()
my_turtle.goto(5, 7)

my_turtle.pendown()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(200)

# This method keep the turtle screen stay
turtle.done()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
