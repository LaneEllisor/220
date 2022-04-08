"""
Name: Chapman Lane Ellisor
hw10.py
Problem: Loops and Bools
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def fibonacci(n):
    fib1, fib2 = 1,1
    count = 0
    while count < n-2: #n-2 since first two terms defined
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
        count += 1
    return fib2



def double_investment1(principle, rate):
    time = 0
    inital_amount = principle
    while inital_amount <= principle * 2:
        initial_amount = inital_amount + inital_amount * rate
        time += 1
        return time

def syracuse(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2 # function 1
        else:
            n = 3 * n + 1 # function 2
        seq.append(n)
    return

# To check if a number is prime for Goldbach
def is_prime(n):
    flag = False
    if n > 1:
        for i in range(2, n): #looking for factors
            if (n % i) == 0: # looking for remainders
                flag = True
                break
    if flag:
        return False # returns False if n is not prime
    else:
        return True

def goldbach(n):
    primes = []
    two_primes = []
    count = 0
    if num % 2 == 0:
        iteration = 2
        while iteration < n:
            if is_prime(iteration):
                primes.append(iteration)
            count += 1
        dn = n - primes[count]
        while count < len(primes):
            if dn == primes[count]:
                two_primes.append(primes[count])
                return two_primes
            count += 1
        



