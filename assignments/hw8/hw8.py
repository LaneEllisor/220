"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

nums = [1, 2.1, 3, 4.0, 5]

def add_ten(nums):
    for i in range(abs(len(nums))):
        nums[i] += 10


def square_each(nums):
    for i in range(abs(len(nums))):
        nums[i] = nums[i]**2

def sum_list(nums):
    sum = 0
    for i in range(len(nums)):
        sum += (nums[i])
    print(sum)



def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    print(nums)

nums1 = ["1", "3", "5", "7"]
to_numbers(nums1)

nums2 = [ '3', '7.2', '9']
def sum_of_squares(nums):
    sum = 0
    for i in range(len(nums)):
        nums[i] = float(to_numbers(nums[i]))

        nums[i] = float(square_each(nums[i]))
        sum += nums[i]
        print(nums[i])
sum_of_squares(nums2)
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


if __name__ == '__main__':
    pass
