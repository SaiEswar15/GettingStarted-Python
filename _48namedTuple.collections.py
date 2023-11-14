
'''before writing namedTuple collection'''

'''first qustion: how does the tuple look'''
#solution : (1,2,3)

'''does your tuple has a name to access '''
#solution : yes 

newTuple = (1,2)
print(newTuple[0])

'''now you will be given two points and you have to acess by x and y cordinates'''

x = newTuple[0]
y = newTuple[1]

print(x,y)

#it worked but what if you wanted 100 points and acess each point with x and y 
#it becomes difficult so 

#we should create a method which takes in two values and return x and y coordinates

class Point() :
    def __init__(self):
        self.x 
        self.y 

p1 = Point(3,4)

print(vars(p1))
print(p1.x)
print(p1.y)

'''the above process is made easy by namedTuple of creating class and returning the dict
of x and y coordinates'''

#import the named tuple from collections 
from collections import namedtuple

#create the class with just one line by using the namedtuple
#takes two params name of the class and x and y coordinates
#assign it to variable so that object is created
Point = namedtuple('Point', 'x,y')
p = Point(2,6)
print(p.x)
print(p.y)



#behind the scenes 
#a function takes classname and cordinates to be declared
#namedtuple('Point', 'x,y')
#inside the function it creates a class and the variables with parameters(cordinates)
#and the function will return the function and point a new variable to this return func
#now call the function with params which return dict

'''
def namedtuple(Point, string) :

    #string to list
    class Point :
        def __init__(self, x, y) :
            self.x
            self.y
        
        def newPoint(a,b) :
            return {
                self.x = a,
                self.y = b
            }
        
    return Point.newPoint

Point = namedtuple('point', 'x,y')
Point = Point.newPoint

p1 = Point(1,2)
print(p1['x'])
print(p1['y'])
'''

#the named tuple looks something like this

###Thanks namaste