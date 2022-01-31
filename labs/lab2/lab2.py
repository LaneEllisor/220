"""
# Name: Chapman Lane Ellisor
# lab2.py
# Problem: Statistical Analysis of Input Values
# Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
#importing functions
import math

# getting user inputs
length = int(input('How many values: '))

# initialize
nums = 0
sum = 0
rms_sum = 0
harmonic_sum = 0
geometric_product = 1

#getting values
for n in range(length):
    values = float(input("Enter Values:   "))

    sum += values
    mean = round(sum / length,3)

    rms_sum += values ** 2
    rms = round(math.sqrt(rms_sum/length),3)

    harmonic_sum += (values)**(-1)
    harmonic_mean = round(length/ harmonic_sum,3)

    geometric_product *= values
    geometric_mean = round((geometric_product)**(1/length),3)

# getting output
print("The RMS average is:", rms)
print("The harmonic mean is:", harmonic_mean)
print("The geometric mean is:", geometric_mean)

'''
Questions:
1. The program will take in several user input values,
perform different sums and porducts of them, and output assorted statistic
2. The inputs are a set of floating point values and outputs will be rounded floats.
The inputs are the values of the sum or product, the outputs are the root mean square aver,
the harmonic mean, and the geometric mean. 
3. Pseudocode:
Import Libraries->
Initialize variables->
User input length of sum->
Perform a summation for each user input in the length of the sum
Perform statistics onto each sum/product
Print outputs
'''
