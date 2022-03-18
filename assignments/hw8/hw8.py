"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from graphics import *
import math as math

# define some lists to use
nums = [1, 2.1, 3, 4.0, 5]
nums1 = ["1", "3", "5", "7"]
nums2 = ['3', '7.2', '9']


# you cannot get len of list of floats.
def length(list):
    length = 0
    for i in list:
        length += 1
    return int(length)


def add_ten(nums):
    list_length = length(nums)
    for i in range(list_length):
        nums[i] += 10.0



def square_each(nums):
    list_length = length(nums)
    for i in range(list_length):
        nums[i] = nums[i]**2
    return nums

#print(square_each(nums))

def sum_list(nums):
    sum = 0
    list_length = length(nums)
    for i in range(list_length):
        sum += (nums[i])
    return sum



def to_numbers(nums):
    list_length = length(nums)
    for i in range(list_length):
        nums[i] = float(nums[i])
        return nums[i]

def sum_of_squares(nums):
    to_numbers(nums)
    square_each(nums)
    num_result = sum_list(nums)
    return num_result

numsm = ['5.96, 2.46, 3.36']

#print(length(numsm))
#print(to_numbers(numsm))
#print(sum_of_squares(nums2))



def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    if weight > 199 or wins >20:
        return True
    else:
        return False

def leap_year(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    if (year % 100 == 0) and (year % 400 != 0):
        leap = False
    if (year % 400 == 0):
        leap = True
    else:
        leap = False

    return leap

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center1 = win.getMouse()
    circumference_point1 = win.getMouse()
    radius1 = math.sqrt(
        (center1.getX() - circumference_point1.getX()) ** 2 + (center1.getY() - circumference_point1.getY()) ** 2)
    circle_one = Circle(center1, radius1)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)


    win.getMouse()




def did_overlap(circle_one, circle_two):
    radius_1 = circumference_point1 - center1
    radius_2 = circumference_point2 - center2

    x_0 = center1.getX()
    y_0 = center1.getY()
    x_1 = center2.getX()
    y_1 = center2.getY()

    r_1 = math.sqrt(
        (center1.getX() - circumference_point1.getX()) ** 2 + (center1.getY() - circumference_point1.getY()) ** 2)
    r_2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)

    d = math.sqrt( (x_1-x_0)**2 + (y_1-y_0)**2)

    if d > r_1 + r_2:
        return None
    else:
        return True

def circles_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center1 = win.getMouse()
    circumference_point1 = win.getMouse()
    radius1 = math.sqrt(
        (center1.getX() - circumference_point1.getX()) ** 2 + (center1.getY() - circumference_point1.getY()) ** 2)
    circle_one = Circle(center1, radius1)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()


    x_0 = center1.getX()
    y_0 = center1.getY()
    x_1 = center2.getX()
    y_1 = center2.getY()


    d = math.sqrt( (x_1-x_0)**2 + (y_1-y_0)**2)

    if d > radius1 + radius2:
        print("No overlap")
    else:
        print("Overlap")



#circles_overlap()

def circles_overlap2():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center1 = win.getMouse()
    circumference_point1 = win.getMouse()
    radius1 = math.sqrt(
        (center1.getX() - circumference_point1.getX()) ** 2 + (center1.getY() - circumference_point1.getY()) ** 2)
    circle_one = Circle(center1, radius1)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()

    did_overlap(circle_one, circle_two)

circles_overlap2()
if __name__ == '__main__':
    pass
