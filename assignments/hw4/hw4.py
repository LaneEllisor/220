"""
Name: Chapman Ellisor
hw4.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(0, 0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the rectangle
    for i in range(num_clicks+1):
        click = win.getMouse()
        center = shape.getCenter()  # center of rectangle

        # move amount is distance from center of rectangle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

        shape2 = Rectangle(Point(click.getX() - 25, click.getY() - 25),
                           Point(click.getX() + 25, click.getY() + 25))
        shape2.setOutline("red")
        shape2.setFill("red")
        shape2.draw(win)

    text = Text(Point(50,50), "Click again to close")
    text.draw(win)
    win.getMouse()
    win.close()


#squares()


def rectangle():
    pass


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(0, 0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the rectangle
    for i in range(num_clicks + 1):
        click = win.getMouse()
        center = shape.getCenter()  # center of rectangle

        # move amount is distance from center of rectangle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

        shape2 = Rectangle(Point(click.getX() - 25, click.getY() - 25),
                           Point(click.getX() + 25, click.getY() + 25))
        shape2.setOutline("red")
        shape2.setFill("red")
        shape2.draw(win)

    text = Text(Point(50, 50), "Click again to close")
    text.draw(win)
    win.getMouse()
    win.close()


def pi2():
    pass


if __name__ == '__main__':
    pass
