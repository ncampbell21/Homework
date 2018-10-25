#Oct 25
#I didn't write as many comments for this one because it is a literal copy of Mandelbrot 1 with a few changes I've marked.
from PIL import Image, ImageDraw, ImageFilter
import colorsys

maxiters = 200

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < maxiters:
        z = z**10+ c
        n += 1
    return n

# size
imgx, imgy = 1000,1000

# plot
xmax = -2 #this part is different
xmin = 1
ymax = -2
ymin = 1

image = Image.new('HSV', (imgx, imgy), (0, 0, 0))


for x in range(0, imgx):
    for y in range(0, imgy):
        # Convert pixel coordinate to complex number
        c = complex(xmax + (x / imgx) * (xmin - xmax),
                    ymax + (y / imgy) * (ymin - ymax))
        # does function, computes iters
        m = mandelbrot(c)
        # colors 
        hue = int(360 - 1000*(m/maxiters)) #different 
        saturation = int(3500 * m / maxiters) 
        if m < maxiters:
       	 	value = 255
       	else:
          saturation = 0
        # draw
        image.putpixel([x, y], (hue, saturation, value))

image.convert('RGB').save('output2.png', 'PNG')





