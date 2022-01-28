"""
Name: ChapmanEllisor
hw2.py

Problem:
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

import math


def sum_of_threes():
    upper_bound = eval(input("Enter the Upper Bound"))
    sum = 0
    for i in range(0, upper_bound+1):
        if (i%3==0):
            print(i)
            sum = sum + i
    print("The sum of threes is", sum)




def multiplication_table():
    one_to_nine = [[x * y for x in range(1, 11)] for y in range(1, 10)]

    print(one_to_nine)


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
multiplication_table()