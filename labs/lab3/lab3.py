"""
# Name: Chapman Lane Ellisor
# lab3.py
# Problem: Finding averages over multiple loops
# Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

def average_vehicles():
    roads_surveyed = int(input("How many roads were surveyed? "))
    total_vehicles = 0
    for i in range(roads_surveyed):
        print("How many days was road", i+1, end=' ')
        days_surveyed = int(input("surveyed?   "))
        sum = 0
        for k in range(days_surveyed):
            print("How many cars traveled on day", k+1, end='')
            cars_per_day = int(input("?  "))
            sum += cars_per_day
        cars_travelled = sum
        average_veh = sum / (k+1)
        print("Road", i + 1, "average vehicles per day:", round(average_veh,3))
        total_vehicles += cars_travelled

    average_vehicles_per_road = total_vehicles/roads_surveyed
    print("Total number of vehicles traveled on all roads:", total_vehicles)
    print("Average number of vehicles per road:", round(average_vehicles_per_road,2))


average_vehicles()