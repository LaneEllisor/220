


def average():
    length = int(input("How many grades will you enter?  "))
    sum = 0
    for n in range(length):
        values = float(input("Enter Grade:   "))
        sum += values
        average = round(sum / length, 3)
    print("The average is  ", average)



def tip_jar():
    passes = 5
    tips = 0
    for i in range(passes):
        donation = float(input("How much would you like to donate? "))
        tips += donation
    print("Total Tips:  ", tips)


def newton():
    root = float(input("What number do you want to square root? "))
    iterations = int(input("How many iterations?  "))
    approx = root
    for i in range(iterations):
        approx = (approx + root/approx)/2
    print("The order", iterations, "approximation of the square root of ",root, "is:", approx )

def sequence():
    number_of_terms = int(input("How many terms would you like? "))
    term_one = 1
    sequence_terms = 0
    for k in range(number_of_terms):
        sequence_terms += (1/2)*(2*k+(-1)**(k+1)-1)
        print(sequence_terms)
        sequence=term_one + sequence_terms
        #print(terms ,"", end="")

sequence()

# should have used mod %
def pi():
    number_of_values = int(input("How many terms in the series? "))
    pi_approx = 0.
    for j in range(1, number_of_values):
        term_one = (2*j)/(2*j-1)
        term_two = (2*j)/(2*j+1)
        multiplicative_term = 2*term_one*term_two
        pi_approx += multiplicative_term
    print(pi_approx)

#pi()
if __name__ == '__main__':
    pass

'''
def sequence():
    input
    for i in range():
        print(i%N, end="")
    
    




'''