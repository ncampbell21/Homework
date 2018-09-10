#Nico Campbell
#Due Monday, Sep. 10
#A simple program that figures out some information regarding what animals you like. After answering a few questions,
#the program will open a tab in your browser and bring you to an image of an animal you like.
#Sources: https://stackoverflow.com/questions/22125114/how-to-insert-links-in-python is where I read about webbrowser, which imported to automatically open links.

#import webbrowser to automatically open dog/cat images
import webbrowser as web

print("Hey!") 

#get name
name = input("What's your name?\n")

#Dogs or cats
DogvCat = input("Hi "+name+", it's great to meet you.\n Do you prefer dogs or cats?\n")

#Dogs
if DogvCat == "Dogs":
	print("I like dogs too!\n")
	#big vs small dogs
	typedog = input("Do you prefer big or small dogs?\n")
	#big dogs
	if typedog =="Big":
		print("Here's a picture of a big dog:")
		web.open("https://pics.esmemes.com/papa-shoob-mama-shoob-and-their-shooblet-22854788.png")
	#small dogs
	else:
		print("Here's a picture of a small dog:")
		web.open("https://www.crispypompuppies.com/wp-content/uploads/bryce_pomeranian_puppy_03.jpg")
#Cats
else:
	print("Cats are pretty cool, but dogs are a bit cooler.\n")
	#big vs small cats
	typecat = input("Do you prefer big or small cats?\n")
	#big cats
	if typecat =="Big":
		print("Here's a picture of a big cat:")
		web.open("https://assets3.thrillist.com/v1/image/2683168/size/tmg-article_tall;jpeg_quality=20.jpg")
	#small cats
	else:
		print("Here's a picture of a small cat:")
		web.open("https://i.pinimg.com/originals/3b/ec/06/3bec063ecb6371b24c984b65ce9fdbff.jpg")
