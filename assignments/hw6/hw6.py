"""
Name: Chapman Ellisor
hw6.py
Problem: String Methods
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from math import pi

def cash_converter():
    input_integer = int(input("Enter an integer:  "))
    print('%.2f' % input_integer) #format with 2 decimal places

#cash_converter()

def encode():
    message = str(input("Enter a message: "))
    key = int(input("Enter a key: ")) #shifts ordinal index
    encoded_message = ""
    for i in message:
        print(encoded_message.join(chr(ord(i)+key)), end="") #join converted unicode characters

#encode()



def sphere_area(radius):
    s_area = 4*pi*radius
    s_area = '%.2f' % s_area
    print("The area of the sphere is: ", s_area)

#sphere_area(8)

def sphere_volume(radius):
    s_vol = (4/3) * pi * radius**3
    s_vol = '%.2f' % s_vol
    print("The volume of the sphere is: ", s_vol)

#sphere_volume(8)

def sum_n(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum +i
    print("The sum of the first {0} sums is: {1}".format(number, int(sum)))

#sum_n(8)

def sum_n_cubes(number):
    pass


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
