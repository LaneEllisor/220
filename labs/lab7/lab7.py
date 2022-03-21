"""
Name: Chapman Ellisor
lab7.py

Problem: Vigenere cipher

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

from graphics import *


def cipher(message, key):
    def format_function(string):
        string = string.replace(" ", "")
        string = string.upper()
        return string
    def return_statement(m):
        return m
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    formatted_message = format_function(message)
    formatted_key = format_function(key)

    result = ""
    for i in range(len(formatted_message)):
        letter_i = alphabet.index(formatted_message[i])
        key_i = alphabet.index(formatted_key[i % len(key)])

        value = (letter_i+key_i) % len(alphabet)
        result += alphabet[value]
    return result

print(cipher("this program will be great", 'python'))


# Creating Window
def main():
    win = GraphWin("Vigernere", 500, 500)
    win.setBackground(color_rgb(255, 255, 255))

    input_box1 = Entry(Point(250, 150), 30)
    input_box1.draw(win)

    txt1 = Text(Point(90, 150), "Message to Code")
    txt1.draw(win)

    input_box2 = Entry(Point(250, 200), 20)
    input_box2.draw(win)
    txt2 = Text(Point(90, 200), "Enter Keyword")
    txt2.draw(win)

    # encode button
    txt4 = Text(Point(250, 275), "Encode")
    txt4.draw(win)

    n = 224
    encode = Rectangle(Point(200, 250), Point(300, 300))
    encode.draw(win)
    encode.setFill(color_rgb(n, n, n))

    txt4 = Text(Point(250, 275), "Encode")
    txt4.draw(win)

    win.getMouse()

    # remove the encode button
    clear_rectangle = Rectangle(Point(200, 250), Point(300, 300))
    clear_rectangle.draw(win)
    clear_rectangle.setFill(color_rgb(255, 255, 255))
    clear_rectangle.setOutline(color_rgb(255, 255, 255))

    # creating cipher box
    cipher_box = Rectangle(Point(150, 250), Point(350, 300))
    cipher_box.draw(win)

    txt5 = Text(Point(110, 275), "Ciphered Text: ")
    txt5.draw(win)

    # saving inputs
    message = input_box2.getText()
    key = input_box2.getText()

    # putting the ciphers in
    res = cipher(str(message), str(key))

    txt6 = Text(Point(220, 275), res)
    txt6.draw(win)


    win.getMouse()



    # displaying closing message
    txt3 = Text(Point(250, 450), "Click again to close")
    txt3.setSize(8)
    txt3.draw(win)

    win.getMouse()
    win.close()


main()
