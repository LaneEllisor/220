"""
Name: Chapman Ellisor
hw4.py

Problem: Graphics Projects

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

from graphics import *
from math import sqrt, pi

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
    for _ in range(num_clicks+1):
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

    text = Text(Point(200,350), "Click again to close")
    text.draw(win)
    win.getMouse()
    win.close()


squares()


def rectangle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    text1 = Text( Point(200,200), "Click again to close")
    text1.setSize(8)
    text1.draw(win)

    #draw rect
    point_one = win.getMouse()
    point_one.draw(win)
    point_two = win.getMouse()


    line = Rectangle(point_one, point_two)
    line.draw(win)
    line.setFill("green")

    # stats
    length = abs(point_two.getY()-point_one.getY())
    width = abs(point_two.getX() - point_one.getX())
    area = length* width
    perimeter = 2*(length + width)

    perimeter_string = str(perimeter)
    area_string = str(area)


    text_one = Text(Point(200,360), "Perimeter: "+perimeter_string)
    text_one.setSize(8)
    text_one.draw(win)

    text_two = Text(Point(200, 370), "Area: " + area_string)
    text_two.setSize(8)
    text_two.draw(win)

    win.getMouse()
    win.close()

rectangle()


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # center click
    center = win.getMouse()
    center.draw(win)
    # radial click
    radius = win.getMouse()
    radius.draw(win)


    change_in_x = radius.getX()-center.getX()
    change_in_y = radius.getY()-center.getY()

    dist = sqrt(change_in_x**2+change_in_y**2)
    dist_string = str(round(dist,4))

    circ = Circle(center, dist)

    circ.setFill("lightblue")
    circ.draw(win)

    text_one = Text(Point(200, 360), "Radius: " + dist_string)
    text_one.setSize(8)
    text_one.draw(win)


    win.getMouse()
    win.close()

circle()



def pi2():
    n_terms = int(input("Enter the number of terms to sum:   "))
    x = 4
    for i in range(n_terms+1):
        x -= (4*(-1)**(i+1))/(2*i-1)
        summation = abs(x)
    accuracy = abs(pi-summation)
    print("pi approximation: ", summation)
    print("accuracy:", accuracy)



pi2()


if __name__ == '__main__':
    pass
