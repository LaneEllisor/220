"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def cash_converter():
    input_integer = int(input("Enter an integer:  "))
    print('%.2f' % input_integer)

#cash_converter()

def encode():
    message = str(input("Enter a message: "))
    key = int(input("Enter a key: ")) #shift ord call
    encoded_message = ""
    for i in message:
        print(encoded_message.join(chr(ord(i)+key)), end="")


encode()



def sphere_area(radius):
    pass


def sphere_volume(radius):
    pass


def sum_n(number):
    pass


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
