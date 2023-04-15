from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """Moves turtle by 20 spaces when triggered by keystrokes when passed to the .onkey(x,y) function"""
    tim.forward(20)


def clearer():
    """Clears the screen and returns turtle to original position when triggered by keystrokes after getting passed to
    the .onkey(x,y) function"""
    tim.home()
    tim.clear()


def look_up():
    """Moves the direction of the turtle clockwise when triggered by keystrokes when passed to the .onkey(x,
    y) function"""
    tim.right(10)


def look_down():
    """Moves the direction of the turtle anti-clockwise when triggered by keystrokes when passed to the .onkey(x,
    y) function"""
    tim.left(10)


def move_backwards():
    """Moves turtle by backwards 20 spaces when triggered by keystrokes when passed to the .onkey(x,y) function"""
    tim.backward(20)


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=look_up)
screen.onkey(key='d', fun=look_down)
screen.onkey(key='c', fun=clearer)
screen.exitonclick()
