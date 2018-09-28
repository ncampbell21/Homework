#List of 10 random numbers between 0 and 100, largest to smallest, remove divisible by 3 
#Sep 28
#I'm not sure what's wrong with this one. The list index out of range error pops up at line 16, and i really don't know why.
#The code creates a list with 10 numbers between 1 and 100, and then sorts them in descending order. Then, there's supposed
#to be a loop that runs through every item in the list and sees if it's divisible by 3, but then an error comes up :(

#import random
import random as r

#list of 10 random numbers between 0 and 100
num = [r.randrange(100) for x in range(10)]

#sorts reverses it I think? I remember this from a few months ago but I'm not sure if it's right
newnum = num.sort(reverse=True)

#print
print(newnum)



#loop goes # of times as length of list
for a in range(len(newnum)):
	#if item a in newnum is divisible by 3 remove it (this is where I get error)
	if newnum[a] % 3 == 0:
		del newnum[a]

#print result
print(newnum)
