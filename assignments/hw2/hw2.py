"""
Name: Chapman Ellisor
hw2.py

Problem: For loops and simple scripts exercises.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
# Importing Libraries
import math

# Defining Functions
def sum_of_threes():
    upper_bound = eval(input("Enter the Upper Bound"))
    sum = 0
    for i in range(0, upper_bound+1):
        if (i%3==0):
            sum = sum + i
    print("The sum of threes is", sum)

def multiplication_table():
    N = 10
    for i in range(1,N+1):
        for j in range(1, N+1):
            print(str(i*j), end="\t")
        print()

def triangle_area():
    a = eval(input("a="))
    b = eval(input("b="))
    c = eval(input("c="))

    s = (a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area is", Area)

def sum_squares():
    lower_range = eval(input("Enter Lower Range: "))
    upper_range = eval(input("Enter Upper Range: "))

    squares = 0
    for i in range(lower_range, upper_range+1):
        squares = squares + i**2
    print(squares)

def power():
    base = eval(input("base= "))
    power = eval(input("power= "))

    power_ab = base**power
    print(base, "^", power, "=", power_ab)

if __name__ == '__main__':
    pass
