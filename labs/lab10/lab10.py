from door import *
from button import *
from graphics import *

def main():
    win = GraphWin("Door", 500, 500)
    win.setBackground('white')

    door_shape = Rectangle(Point(100, 100), Point(400, 600))
    door_text = 'closed'

    door_object = Door(door_shape, door_text)
    door_object.color_door('blue')
    door_object.draw(win)
    door_object.close('maroon', 'closed')

    button_shape = Rectangle(Point(75, 75), Point(425, 100))
    button_object = Button(button_shape, "Exit")
    button_object.draw(win)

    while True:
        x = win.getMouse()
        if button_object.is_clicked(x):
            break
        elif door_object.is_clicked(x):
            door_object.open("light blue", "Open")
        x = win.getMouse()
        if button_object.is_clicked(x):
            break
        elif door_object.is_clicked(x):
            door_object.close("maroon", "Closed")



if __name__ == "__main__":
    main()
