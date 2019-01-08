#Wednesday, January 9
#I initially expect the chances to be 50/50 if you switch, but obviously there's something larger at play if we are doing a simulation of it.
#I know that originally there's a 1/3 chance that you got it, but if one choice liminated does it make it more likely if you switch? I'm unsure, but
#i'm excited to see.


import random as r 

loss_changed = 0
wins_changed = 0

#list of prizes
doors = ["penny","car","penny"]

#simulations
for x in range(10000):
	#shuffle the objects
	r.shuffle(doors)
	#my  choice
	choice = r.randint(0,2)
	#opened door
	for opened in range(3):
		#opens door that I haven't opened and is not car
		if opened == choice or doors[opened] == "car":
			continue
	#the one I chose is the car
	if doors[choice] == "car":
		loss_changed +=1 

	#the one I could've switched to is the car
	else:
		wins_changed +=1

#print results
print("you lost the car",loss_changed,"times if you changed")
print("you won the car",wins_changed,"times if you changed")

#so i've run it, and it was not 50/50. It's not what one would initially expect I think, but here's my thinking:
#you first have a 2/3 chance that you have a penny. When you are told one of the two pennies, it is still most likely that you chose a penny 
#in the first place, so it makes the most sense to switch to what should be the car.
