from graphics import *
from math import *


def triangle():
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # displaying closing message
    text1 = Text(Point(200, 350), "Click again to close")
    text1.setSize(8)
    text1.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    #input("hit enter to exit")

    x1 = p1.getX()
    x2 = p2.getX()
    x3 = p3.getX()

    y1 = p1.getY()
    y2 = p2.getY()
    y3 = p3.getY()

    dx1 = x2-x1
    dy1 = y2-y1

    dx2 = x3-x2
    dy2 = y3-y2

    dx3 = x3-x1
    dy3 = y3-y1

    length1 = sqrt(dx1**2+dy1**2)
    length2 = sqrt(dx2**2+dy2**2)
    length3 = sqrt(dx3**2+dy3**2)

    perimeter = length1+length2+length3
    print("The perimeter is: ", round(perimeter,3))

    s = (perimeter)/2
    area = sqrt(s*(s-length1)*(s-length2)*(s-length3))
    print("The area is: ", round(area,3))

#triangle()



def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)



    # Wait for another click to exit
    win.getMouse()
    win.close()



color_shape()
def process_string():
    pass


def process_list():
    pass


def another_series():
    pass


def target():
    pass
