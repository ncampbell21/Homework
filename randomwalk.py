
#1/11
#it actually happens that my original solution was very similar to lines 7-19 of the code below. all of the calculations with respect to 
#transportation and stuff are from the video, as I never got to that in class...
#anyways, this is relatively straightforward. The function runs n times, with x and y starting at zero. then an additional loop runs n times,
#where a random number is chosen which determines the turn. then x and y are both respectively added/subtracted/etc to simulate the turn. these inputs are 
#returned and more turns build on these turns n times. N random walks like this will be simulated in the random_walk function.
#after this, there is a loop that runs (i decided) 100 times, meaning that it does 100 walks. there is a counter variable, no transport, which will
#keep track of how many # we don;t get transportation. Then, a loop does walks number of walks and calculates the distance from the origin.
#if this distance is <=4, you do not need to take transportation, so the counter variable is added to. 
#the percent of times you didn't have to use transport is calculated, and displayed with the walk size.


#like the video, I got 22 as the largest walk size, at 51%. 

#from what i understand, a monty carlo simulation calculates risk and probability through randomly exploring all outcomes of a situation
#they are used in many fields of science and engineering, and can also be used for economics or generally any field in which one must calculate risk or
#statistical probability of a certain outcome.


import random as r 


# def random_walk(n):
# 	#origin
# 	x = 0
# 	y = 0
# 	#random turns n times
# 	for i in range(n):
# 		turn = r.randint(1,4)
# 		if turn == 1:
# 			x += 1
# 		if turn == 2:
# 			y += 1
# 		if turn == 3:
# 			x -=1
# 		if turn == 4:
# 			y -= 1
# 	#return most recent coordinates
# 	return(x,y)

# walks = 10000

# for i in range(100):
# 	#counter
# 	no_transport=0
# 	#do the walks
# 	for z in range(walks):
# 		(x,y) = random_walk(i)
# 		#calculate distance for each walk
# 		dist = abs(x) + abs(y)
# 		#if transport isn't used, add to the counter
# 		if dist <= 4:
# 			no_transport += 1
# 	#print /calculate %
# 	percent = no_transport/walks
# 	print("walk size:", i,"/ % of no transport =",100*percent)


def darts():
	throws = 10000
	hits = 0
	for i in range(throws):
		#returns either -1 or 1 (circle radius is 1)
		x = r.random()*2 -1
		y = r.random()*2 -1
		#I think there is an issue somewhere around here, because i learned that i'm supposed to be getting pi but i'm getting close but not quite there...
		if x+ y<=1:
			hits +=1
	#i don't think there's an issue here? this is supposed to calculate pi
	print(4*hits/throws)

darts()
