from math import *

#print(2 ** 3 ** 2)

# is not 64 -> 2 ^ (3^2) = 2^9 = 512, right to left for powers

# give month ( 2) get out that is February
def month():
    placement = int(input("Enter the number of the month:  "))
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    print("The month is:", months[placement-1][0:3])

#month()


# adding to list ------
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


months.append("New Month")

#print(months)

# if you want an empty list to start

'''
numbers = []
for i in range(3):
    number = eval(input("Enter Number:  "))
    numbers.append(number)
    print(numbers)
'''


#string methods -----
a = "hello, world!"
b = a.upper()
print(b)
print(a)

# string methods do not change the og string

c = b.lower()
print(c)

a = "it's a small world after all" #for aprostrophe's within strings use double quotes
print(a.capitalize())

print(a.title())

print(a.count("l"))

print(a[10])



