#Oct19
#Since I was out of class on wednesday, I tried my best to figure out what I could about the mandelbrot calculation
#I read a lot of online stuff, but not a lot of it made sense to me. This is what I could make in the time remaining.
#I know it's not a lot, but I think (?) it makes sense and that it's on the right track. I think I got to step 4, and didn't have an idea
#of how to do 5...


import numpy #for arrange function
 
def mandelbrot(c):
	z = 0  #set z
	for n in range(1, 4): #3 itterations
		z = z**2 #z = z^2
		z = z + c #add c
		if abs(z) >= 2: #if escaped
			exit() #end

#setting 
X = arange(-2, 2, .01) #I think this makes sense? -2 to 2... I know the steps are supposed to be small, too.. 
Y = arange(-2, 2, .01)
