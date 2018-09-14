#Sep 14 2018
#I had a decent amount of frustration with this. 
#I really wanted to find a way to pack the two comparative statements
#into one "if" statement, but struggled to find a method for doing this.
#Either way, the program works, but I wish it were shorter and more clever
#I wish that I had enough time to find a better solution.

#importing sys
import sys

#storing arguments as variables val1 val2 and val3
val1 = float(sys.argv[1])
val2 = float(sys.argv[2])
val3 = float(sys.argv[3])

#if val1>val2>val3, print the value of the statement(true)
if(val1>val2>val3)
	print(val1>val2>val3)

#if val3>val2>val1, print the value of the statement(true)
elif(val3>val2>val1):
	print(val3>val2>val1)

#if the previous two are false, print false.
else:
	print(False)




