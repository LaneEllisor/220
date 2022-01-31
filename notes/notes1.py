import math
import graphics


x = math.sqrt(2)
print(x)

# method - getX and getY are examples
#graphics uses cartesian window whose top left coordinate is the origin. must give it coordinates to draw things
point_a = graphics.Point(50,70) #constructors
point_b = graphics.Point(90,100)


x_a = point_a.getX() #accsessor methods
print(x_a) #should see 50

print(type(point_a)) #tells us this is a point class
print(type(point_b)) #tells us this is a point class

print(point_a.getX(), point_a.getY()) #notice it returns a float

#to acsess a method use a dot
point_a.move(10,0) #we want new location of a to be 60,70, move(dx, dy), note that we dont have to force this to be a new object

print(point_a.getX(), point_a.getY())

win = graphics.GraphWin("aye yuh", 300, 300) #constructor, doesnt have to take arguments/parameters, in pixels


#graphwin has a title, width, height

#now draw a point on the window, point class has a draw method.
point_a.draw(win) #pass the graphwin object

point_c = graphics.Point(150, 150)
point_c.draw(win)

my_circle = graphics.Circle(point_c, 20)
my_circle.draw(win)



input("hit enter to exit") #causes problem to wait at this line