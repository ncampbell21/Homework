#Nico Campbell
#Due Monday, Sep. 10
#A simple program that figures out some information regarding what animals you like. After answering a few questions,
#the program will open a tab in your browser and bring you to an image of an animal you like.
<<<<<<< HEAD
#Sources: https://stackoverflow.com/questions/22125114/how-to-insert-links-in-python is where I read about webbrowser, which I imported to automatically open links.
=======
#Sources: https://stackoverflow.com/questions/22125114/how-to-insert-links-in-python is where I read about webbrowser, which imported to automatically open links.
>>>>>>> 929da30f7a04114907db15f01c38286773bdad97

#import webbrowser to automatically open dog/cat images
import webbrowser as web

print("Hey!") 

#get name
name = input("What's your name?\n")

#Dogs or cats
<<<<<<< HEAD
DogvCat = input("Hi "+name+", it's great to meet you.\n Do you prefer dogs, cats, or cows?\n")

#Dogs
if DogvCat == "Dogs":
	print("I like dogs too!")
=======
DogvCat = input("Hi "+name+", it's great to meet you.\n Do you prefer dogs or cats?\n")

#Dogs
if DogvCat == "Dogs":
	print("I like dogs too!\n")
>>>>>>> 929da30f7a04114907db15f01c38286773bdad97
	#big vs small dogs
	typedog = input("Do you prefer big or small dogs?\n")
	#big dogs
	if typedog =="Big":
		print("Here's a picture of a big dog:")
<<<<<<< HEAD
		#opens link
=======
>>>>>>> 929da30f7a04114907db15f01c38286773bdad97
		web.open("https://pics.esmemes.com/papa-shoob-mama-shoob-and-their-shooblet-22854788.png")
	#small dogs
	else:
		print("Here's a picture of a small dog:")
<<<<<<< HEAD
		#opens link
		web.open("https://www.crispypompuppies.com/wp-content/uploads/bryce_pomeranian_puppy_03.jpg")
#Cats
elif DogvCat == "Cats":
	print("Cats are pretty cool, but dogs are a bit cooler.")
=======
		web.open("https://www.crispypompuppies.com/wp-content/uploads/bryce_pomeranian_puppy_03.jpg")
#Cats
else:
	print("Cats are pretty cool, but dogs are a bit cooler.\n")
>>>>>>> 929da30f7a04114907db15f01c38286773bdad97
	#big vs small cats
	typecat = input("Do you prefer big or small cats?\n")
	#big cats
	if typecat =="Big":
		print("Here's a picture of a big cat:")
<<<<<<< HEAD
		#opens link
=======
>>>>>>> 929da30f7a04114907db15f01c38286773bdad97
		web.open("https://assets3.thrillist.com/v1/image/2683168/size/tmg-article_tall;jpeg_quality=20.jpg")
	#small cats
	else:
		print("Here's a picture of a small cat:")
<<<<<<< HEAD
		#opens link
		web.open("https://i.pinimg.com/originals/3b/ec/06/3bec063ecb6371b24c984b65ce9fdbff.jpg")
#cows
elif DogvCat == "Cows":
	print("Cows are pretty dope.")
	#what type of cow
	typecow = input("Would you rather see a really fluffy cow or a really small cow?\n")
	#fluffy cow
	if typecow == "Fluffy":
		print("Here's a picture of a fluffly cow:")
		#open link
		web.open("https://laughingsquid.com/wp-content/uploads/2013/06/20130604-12552987-fluffycow4.jpg")
	#mini cow
	else:
		print("Here's a picture of a small cow:")
		#open link
		web.open("https://i.redd.it/io2ob4n5b0h01.jpg")

=======
		web.open("https://i.pinimg.com/originals/3b/ec/06/3bec063ecb6371b24c984b65ce9fdbff.jpg")
>>>>>>> 929da30f7a04114907db15f01c38286773bdad97
