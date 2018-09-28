# 100 randomly generated 3 digit numbers (nontraditional loop), shuffle up
#September 28
#This was the one that I actually think I got to work! all values from 1 to 100 are added to the list, and then a loop runs 100 times and takes 
#a random index and moves the item to another random index to mix it up.


#import random
import random as r

#creates list with numbers 1-100
big_list = [x for x in range(1,101)]

#goes into the list 100 times and chooses a random item and puts it in a random index
for x in range(100):
	big_list.insert(r.randrange(100), big_list.pop(r.randrange(100)))

#print result
print(big_list)