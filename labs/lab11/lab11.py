
# importing libraries and classes
from lab10.door import Door
from lab10.button import Button
from random import *
from graphics import *


def game():
    # graphics window
    width = 800
    height = 600
    win = GraphWin("Three Doors", width, height)
    win.setBackground('light blue')

    # define doors and button
    button = Button(Rectangle(Point(575, 50), Point(750, 125)), "Quit")
    door_1 = Door((Rectangle(Point(75, 200), Point(225, 500))), "Door 1")
    door_2 = Door((Rectangle(Point(275, 200), Point(425, 500))), "Door 2")
    door_3 = Door((Rectangle(Point(475, 200), Point(625, 500))), "Door 3")
    button.draw(win)
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)

    #define text box
    top_point = Point(width/2-50, height/4+20)
    top_text = Text(top_point, "Click to guess which is the secret door")
    top_text.draw(win)


    # initial object colors
    button.color_button("grey")
    door_1.color_door('peru')
    door_2.color_door('peru')
    door_3.color_door('peru')


    # tally box
    wins_point = Rectangle(Point(75, 50), Point(150, 125))
    wins_point.draw(win)
    wins_text = Text(Point(112, 40), 'Wins')
    wins_text.draw(win)

    losses_point = Rectangle(Point(150, 50), Point(225, 125))
    losses_point.draw(win)
    losses_text = Text(Point(187, 40), 'Losses')
    losses_text.draw(win)

    #putting things in tally box
    wins_list = []
    losses_list = []

    win_number = Text(Point(112, 87), '')
    win_number.draw(win)
    win_number.setText(len(wins_list))
    loss_number = Text(Point(187, 87), '')
    loss_number.draw(win)
    loss_number.setText(len(losses_list))

    # doors
    doors = [door_1, door_2, door_3]
    clicked_point = win.getMouse()

    while not button.is_clicked(clicked_point):
        # getting random door
        random_door_index = randint(0, 2)
        doors[random_door_index].set_secret(True)


        # win.getMouse()
        for door in doors:
            if door.is_clicked(clicked_point):
                if door.is_secret():
                    top_text.setText("You Won")
                    door.color_door('green')

                    wins_list.append('w')
                    win_number.setText(len(wins_list))
                    loss_number.setText(len(losses_list))
                else:
                    top_text.setText("You Lost :(")
                    door.color_door('red')

                    losses_list.append('l')
                    win_number.setText(len(wins_list))
                    loss_number.setText(len(losses_list))
            elif door.is_secret():
                door.color_door('green')


        top_text.setText("Click anywhere to play again")
        clicked_point = win.getMouse()

        if button.is_clicked(clicked_point):
            win.close()

        doors[random_door_index].set_secret(False)

        for i in range(3):
            doors[i].close('peru', 'Door '+str(i+1))

        clicked_point = win.getMouse()




    win.getMouse()
    win.close()


game()
