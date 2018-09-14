#Sep 14 2018
#This was a bit more frustrating. I think my main difficulty is math
#syntax in python, because I seem to get errors with those.
#Either way, I spent a lot of time on this and couldn't get it to 
#work perfectly. A result is printed, but it's two days off.
#I could just change it to dayofweek=days[d+2], but I feel like 
#that's just a workaround

#importing sys
import sys

#storing arguments as variables
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

#list of days of week to index later
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

#operations to get day of week
y = y -((14-m)/12)
x = y + (y/4) - (y/100) + (y/400)
m = m + ((12*((14-m)/12))-2)
d = (d + x + (31*m)/12)
d = (d%7)

#get the element from the list dayofweek that corresponds with the 
#number from the operations above
dayofweek = days[d]


#print the string from the list
print(dayofweek)






