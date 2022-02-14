"""
Name: Chapman Ellisor
hw5.py

Problem: Simple Strings

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

def name_reverse():
    name = str(input("Enter a name (first, last):  "))

    space = name.find(" ")
    first_name = name[0:space]
    last_name = name[space+1:]

    print(last_name+", "+ first_name)

#name_reverse()

def company_name():
    domain = str(input("Enter a domain: "))

    dom_w = domain[4:]

    dots = dom_w.find(".")

    domain_name = dom_w[:dots]

    print(domain_name)

#company_name()






if __name__ == '__main__':
    pass

