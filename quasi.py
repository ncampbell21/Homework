#Oct. 25
#I decided to randomly generate a type of fractal called a quasicrystal. The definition of a quasicrystal is:
#"Basically, a quasicrystal is a crystalline structure that breaks the periodicity (meaning it has translational symmetry, 
#or the ability to shift the crystal one unit cell without changing the pattern) of a normal crystal for an ordered, yet aperiodic arrangement." 
#the program randomly generates the frequency, phase, and rotations of the "wave" type things that you'll see before undergoing some transformations
#that I honestly don't quite understand. 
#I didn't actually use coding resources for this, just a lot of math ones.
#On my honor, I have neither given nor recieved unauthorized aide.


import math
import random
from PIL import Image

imgx,imgy= 512,512
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()

f = random.random() * 40 + 10 # frequency
p = random.random() * math.pi # phase
rot = random.randint(10, 20) # of rotations
print(f, p, rot) #why not

#Y's
for yy in range(imgy):
    y = yy / (imgy - 1) * 4 * math.pi - 2 * math.pi
    #X's 
    for xx in range(imgx):
        x = xx / (imgx - 1) * 4 * math.pi - 2 * math.pi
        z = 0
        for i in range(rot): #for how many rotations
            r = math.hypot(x, y) #hypoteniuse of triange x, y, _
            a = math.atan2(y, x) + i * math.pi * 2.0 / rot #arctangent 
            z = z + math.cos(r * math.sin(a) * f + p)  
        c = int(round(255 * z / rot)) #choose color
        pixels[xx, yy] = (c, c, c) # grayscale
image.save("quasicrystal.png", "PNG")