#Oct 15
#This image is the result of just some random experimentation. It is actually pretty similar to some aspects of the Minesweeper project.
#only x values between 70 and imgx-35 are printed, with steps of 50 in between. All y values from 70 to imgy-35 are printed.
#the columns in the image are made by lines 19 to 20 and 21. The 20 pixels on either side (horizontal) of a given pixel are colored the same color.

from PIL import Image
import random as r

imgx = 512 #dimensions
imgy = 512

image = Image.new(("RGB"),(imgx, imgy)) #define image


for x in range(70, imgx-35, 50): #all x values from 70 to imgx-35, steps are 50
	for y in range(70, imgy-35): #all y values from 70 to imgy-35.
		colors = [r.randrange(0,255), r.randrange(0,255), r.randrange(0,255)] #random generate 3 #s
		for change1 in range(-20,21): #changes from -20 to 20
			for change2 in range(-20,21):
				image.putpixel((x+change1,y+change2),(colors[0],colors[1],colors[2])) #applies changes


image.save("groovy.png","PNG") #prints