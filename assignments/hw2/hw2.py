"""
Name: ChapmanEllisor
hw2.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math


def sum_of_threes():
    upper_bound = eval(input("Enter the Upper Bound"))
    for i in range(upper_bound):
        if (i%3):
            sum+sum+i
    print(sum)


def multiplication_table():
    for num in range(10):
        i = 1
        while i <= numInput:
            product = num * i
            print(num, " * ", i, " = ", product)
            i = i + 1
        print("")
        num = num + 1


def triangle_area():
    a = eval(input("a="))
    b = eval(input("b="))
    c = eval(input("c="))

    s = (a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area is", Area)


def sum_squares():
    pass


def power():
    base = eval(input("base="))
    power = eval(input("power="))

    power_ab = base**power
    print(base, "^", power, "=", power_ab)

if __name__ == '__main__':
    pass

#testing
