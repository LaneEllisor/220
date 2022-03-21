import random as rd
from graphics import *
from math import sqrt

def get_random(move_amount):
    return rd.randint(-move_amount, move_amount)

def did_collide(ball1, ball2):
    #define points on the balls
    ball1_center = ball1.getCenter()
    ball1_x = ball1_center.getX()
    ball1_y = ball1_center.getY()

    ball2_center = ball2.getCenter()
    ball2_x = ball2_center.getX()
    ball2_y = ball2_center.getY()

    radius1 = ball1.getRadius()
    radius2 = ball2.getRadius()

    #checking if there is an overlap
    distance = sqrt((ball2_x - ball1_x) ** 2 + (ball2_y - ball1_y) ** 2)

    if distance == radius1 + radius2:
        hit = True #collide
    else:
        hit = False #no overlap
    return hit


def hit_vertical(ball, win):
    ball_center = ball.getCenter()
    ball_center_x = ball_center.getX()

    radius = ball.getRadius()
    height = win.getHeight()

    area_of_no_hit = height - radius

    if radius < ball_center_x < area_of_no_hit:
        hit = False #ball not hit vertical
    else:
        hit = True
    return hit

def hit_horizontal(ball, win):
    ball_center = ball.getCenter()
    ball_center_y = ball_center.getY()

    radius = ball.getRadius()
    height = win.getHeight()

    area_of_no_hit = height - radius

    if radius < ball_center_y < area_of_no_hit:
        hit = False #ball not hit horizontal
    else:
        hit = True
    return hit

def get_random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    color = color_rgb(r, g, b)

    return color

#print(get_random_color())

def bumper_cars():
    # creating graphics window
    width_px = 700
    height_px = 500
    win = GraphWin("Bumper Cars", width_px, height_px)

    center1 = Point(rd.randint(0,500), rd.randint(0, 500))
    center2 = Point(rd.randint(0, 500), rd.randint(0, 500))

    radius1 = 50
    radius2 = 50

    ball_1 = Circle(center1, radius1)
    ball_1.setFill(get_random_color())
    ball_1.draw(win)

    ball_2 = Circle(center2, radius2)
    ball_2.setFill(get_random_color())
    ball_2.draw(win)

    dx = get_random(5)
    dy = get_random(5)


    while not win.checkMouse():

        ball_1.move(dx,dy)
        ball_2.move(dx, dy)

        if did_collide(ball_1, ball_2) == True:
            dx = -dx
            dy = -dy
        if hit_vertical(ball_1, win):
            dx = -dx
        if hit_horizontal(ball_1, win):
            dy = -dy

    win.close()

bumper_cars()