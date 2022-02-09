b = [ "Bob", "Sandy", "John"]

print(len(b))

# using + is concatenation

c = "hi " + "John"
print(c)

print(type(c))

d = "hi"
e = "john"
f = d + " " + e

print(f)

# you can add lists to mkae a big list

g = ["Monday", "Tuesday"]
h = ["Tuesday", "Wednesday"]
j = g +h
print(j)

# check data types
# you cant add ints to lists, must be added as a list or else error

k = [1,2,3]
#l = k + "3"
#print(l)

print(type(k), type([3]))

l_prime = k + [3]
print(l_prime)

m = ["mon", "tues"]
n = m*2 #duplicate this list twice

print(n)

a = "hello world"
for l in a:
    print(l)

range(10)

b = ["John", "Paul", "George", "Ringo"]

print(b[3]) #3rd index = 4th term bc start at 0

name = [1,2, "hi", 4][3]
print(name)
