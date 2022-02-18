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

def initials():
    total_students = int(input("How many students are in the class?  "))
    for i in range(total_students):
        name = input("What is the name of student "+ str(i+1)+ " ?  ")

        space = name.find(" ")
        first_name = name[0:space]
        last_name = name[space + 1:]

        first_caps = first_name[0].upper()
        last_caps = last_name[0].upper()
        print(first_caps+last_caps)
#initials()

def names():
    names = input("Enter a list of names: ")
    name_list = names.split(',')

    #print(name_list)

    for i in range(len(name_list)):
        splits = name_list[i].split(" ")
        #print(name_list[i])
        print(splits)

        #print(splits[0][0])



names()

def thirds():
    num_sent = int(input("Enter number of sentences:  "))
    third = ""
    for i in range(num_sent):
        sentences = str(input("enter sentence "+str(i+1)+": "))

        third += sentences[::3]+"\n"
    print(third)



#thirds()

def word_average():
    sentence = str(input("Enter a sentence: "))
    words = sentence.split()
    avg = sum(len(word) for word in words) / len(words)
    print(avg)

#word_average()

def pig_latin():
    sentence = str(input("Enter a sentence: "))
    words = sentence.split()
    newSentence = ""
    for i in words:
        newSentence += i[1:]+i[0]+"ay "
        newSentence = newSentence.lower()
        newSentence = newSentence.capitalize()

    print(newSentence)
#pig_latin()


if __name__ == '__main__':
    pass