#Sep 14 2018
#This was generally straightforward. 
#The values are stored in variables which are entered into the formula.
#I struggled a bit at first because I kept getting errors, but 
#inserting float() fixed them. I don't know if this was the "best"
#solution, but I spent a decent amount of time on it.

#imports sys
import sys

#stores the first argument as t (temperature)
t = float(sys.argv[1])
#stores the second argument as v (wind speed)
v = float(sys.argv[2])
#formula 
temp = float(32.74+0.6215*t+((0.4275*t)-35.75)*(v**0.16))
#rounds the number to two decimal places
temp = round(temp, 2)
#prints the result
print("The wind chill is",temp,"degrees Fahrenheit")