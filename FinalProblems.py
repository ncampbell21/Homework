
import numpy as np

#     Use numpy to create an array of numbers going from 20 to 100 by increments of .25
#     Then, multiply all the values in the array by 4. 
#     Then. find the sum of all the values.
myList = np.arange(20,100.25,0.25)
print(myList)
print(sum(myList*4))




#Turtle Star:
import turtle 

star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(144)
    
turtle.done()


#Angle thing

class point:
    def __init__(self, pointname, xpoint, ypoint):
        self.x = xpoint
        self.y = ypoint
        self.pointname = pointname

    def turn90º(self):
        y = self.x
        self.x = self.y
        self.y = y
        return self.x, self.y

    def turn180º(self):
        self.x = -self.x
        self.y = -self.y
        return self.x, self.y

    def turnn90º(self):
        y = self.x
        self.x = -1*self.y
        self.y = -1*y
        return self.x, self.y

    def flipv(self):
        self.x = -1*self.x
        return self.x, self.y

    def fliph(self):
        self.y = -1*self.y
        return self.x, self.y





print(point("1",10,5).turn90º())
print(point("1",10,5).turn180º())
print(point("1",10,5).turnn90º())
print(point("1",10,5).flipv())
print(point("1",10,5).fliph())
