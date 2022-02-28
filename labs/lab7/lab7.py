"""
Name: Chapman Ellisor
lab7.py

Problem: Vigenere cipher

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

from graphics import *
from math import *

#Creating Window
def main():
    win = GraphWin("Vigernere", 500, 500)
    win.setBackground(color_rgb(255,255,255))


    input_box1 = Entry(Point(250,150), 30)
    input_box1.draw(win)

    message = input_box1.getText()

    print(message)

    txt1 = Text(Point(90, 150), "Message to Code")
    txt1.draw(win)

    input_box2 = Entry(Point(250, 200), 20)
    input_box2.draw(win)
    txt2 = Text(Point(90, 200), "Enter Keyword")
    txt2.draw(win)

    # displaying closing message
    txt3 = Text(Point(250, 450), "Click again to close")
    txt3.setSize(8)
    txt3.draw(win)

    n = 224

    encode = Rectangle(Point(200, 250), Point(300, 300))
    encode.draw(win)
    encode.setFill(color_rgb(n,n,n))

    txt4 = Text(Point(250, 275), "Encode")
    txt4.draw(win)

    #txt5 = Text(Point(250, 205), message)
    #txt5.draw(win)

    greeting1 = message
    Text(Point(win.getWidth() / 3, 150), greeting1).draw(win)

    win.getMouse()



#main()

def format_function(string):
    string = string.replace(" ", "")
    string = string.upper()
    return string

message = "this program will be great"
key = "amer ican"



def cipher(message, key):
    formatted_message = format_function(message)
    formatted_key = format_function(key)

    result = ""
    print(formatted_message)
    print(formatted_key)

    for i in range(len(formatted_message)):
        letter_i = formatted_message[i]
        key_i = formatted_key[i % ]
        print(letter_i,"/n")


        value = letter_i + key_i

        #result += value
    print(result)

cipher("hello", 'ur mom')
'''
def encrypt():
    return cipher(message, key)

encrypt()
'''
