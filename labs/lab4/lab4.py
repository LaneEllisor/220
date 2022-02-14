"""
Name: Chapman Ellisor
lab4.py

Problem: Greeting Card

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from graphics import *

# creating graphics window
width = 400
height = 400
win = GraphWin("Happy Valentine's Day", width, height)
win.setBackground('white')

# displaying closing message
text1 = Text( Point(200,350), "Click again to close")
text1.setSize(8)
text1.draw(win)

# defining points
P1 = Point(200,100)
P2 = Point(150, 50)
P3 = Point(100,100)
P4 = Point(200,300)
P5 = Point(300, 100)
P6 = Point(250, 50)
P7 = Point(100,300)
P8 = Point(350, 90)
P9 = Point(320,95)
P10 = Point(330, 110)
P11 = Point(325, 100)
P12 = Point(326, 105)

# define heart shape
heart = Polygon(P1, P2, P3, P4, P5, P6)
heart.draw(win)
heart.setFill("lightpink")

# define arrow shape
arrow = Polygon(P8, P9, P11, P7, P12,P10 )
arrow.draw(win)
arrow.setFill("grey")

# arrow movement
for i in range(350):
    dx = 1
    dy = -1
    arrow.move(dx,dy)

# displaying text
message = Text(Point(200, 170), "Happy Valentines Day")
message.draw(win)
message.setTextColor("white")

# closing graphics window
win.getMouse()
win.close()










