"""
Name: Chapman Lane Ellisor
hw1.py

Problem: Simple function definitions and user inputs are exercised.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# there are no required libraries so we begin by defining several functions

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: ")) # user inputs
    area = length * width # equation for area
    print("Area =", area) # displaying the area with text

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the players total shots: "))
    shots_made = eval(input("Enter the shots the player made: "))
    percentage  = shots_made / total_shots * 100
    print("Shooting Percentage: ", percentage, "%")


def coffee():
    pounds_purchased = eval(input("How many pounds of coffee would you like? "))
    price = 1.50 + 10.50*pounds_purchased+0.86*pounds_purchased
    print("Your total is: ", price)


def kilometers_to_miles():
    travelled = eval(input("How many kilometers did  you travel? "))
    miles = 1 / (1.61) * travelled
    print("That's ", miles, "miles!")


if __name__ == '__main__':
    pass

