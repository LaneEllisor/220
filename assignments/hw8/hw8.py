"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

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
        nums[i] += 10
    return nums

add_ten(nums)

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

#sum_list(nums)

def to_numbers(nums):
    list_length = length(nums)
    for i in range(list_length):
        nums[i] = float(nums[i])
    return nums

#to_numbers(nums2)

def sum_of_squares(nums):
    nums_a = to_numbers(nums)
    nums_b = square_each(nums_a)
    nums_c = sum_list(nums_b)
    return nums_c

#print(sum_of_squares(nums))

'''
def starter(weight, wins):
    pass


def leap_year(year):
    pass


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    pass

'''

if __name__ == '__main__':
    pass
