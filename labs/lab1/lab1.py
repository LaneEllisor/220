"""
# Name: Chapman Lane Ellisor
# lab1.py
# Problem:
# Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
#defining function
def monthly_interest():
    # saving user inputs as variables
    annual_interest_rate = eval(input("Enter the Annual Interest Rate in percent: "))
    billing_cyle_days = eval(input("Enter the number of days in the Billing Cycle "))
    previous_balance = eval(input("Enter the Previous Net Balance "))
    payment_amount = eval(input("Enter the Payment Amount "))
    payment_date = eval(input("Enter the day of the Billing Cycle in which the payment was made "))

    # saving calculations as variables
    days_with_balance = previous_balance * billing_cyle_days
    payment_per_day = payment_amount*(billing_cyle_days-payment_date)
    difference = days_with_balance - payment_per_day
    average_daily_balance = difference / billing_cyle_days
    monthly_rate = (annual_interest_rate / 12)/100
    monthly_interest_charge = average_daily_balance * monthly_rate

    #printing the output
    print("Your Monthly Interest Charge is", round(monthly_interest_charge, 3),"$")

# calling the function for testing
monthly_interest()





