#Oct 25
#This took a while! This piece has three bits of code: Mandelbrot1 and 2, and Blend. I know I could've put the three parts in one file,
#but it was easier to develop this way for me. Anyways: this code is more or less straightforward. Rather than squaring z, I put it to the 
#10th power. The window is moved so that the fractal is in the upper left rather than the center. In terms of color, things are slighly complicated.
#I converted to HSV. The hue for each fractal starts at some value, and is transformed by subtracting the number of iterations it took over the max iterations
#the saturation is altered similarly. Then, if the number of iterations it took to get out was less than maxiters, the point is colored white.
#in terms of overlaying the images, the process was pretty simple. Both images are loaded and then overlayed with an alpha of 0.5, meaning that
#they are equally visible. That's it! I wasn't huge on this piece visually, but I think that it's a cool image and demonstrates versatility.
#on my honor I have neither given nor recieved unauthorized aide.
#sources: https://pillow.readthedocs.io/en/5.2.x/reference


from PIL import Image, ImageDraw, ImageFilter
import colorsys

#max iterations
maxiters = 100

#mandelbrot function
def mandelbrot(c):
    z = 0
    n = 0
    #has not escaped, less than 100 times
    while abs(z) <= 2 and n < maxiters:
      #calculation
        z = z**10 + c
        n += 1
    #do it again
    return n

# size
imgx, imgy = 1000,1000

# plot
xmax = -1
xmin = 2
ymax = -1
ymin = 2

#def image
image = Image.new('HSV', (imgx, imgy), (0, 0, 0))

#color/create image
for x in range(0, imgx):
    for y in range(0, imgy):
        # calculate complex numbers cx and cy
        c = complex(xmax + (x / imgx) * (xmin - xmax),
                    ymax + (y / imgy) * (ymin - ymax))
        # does function, computes iters
        m = mandelbrot(c)
        # colors 
        hue = int(226 - 1000*(m/maxiters))
        saturation = int(3500 * m / maxiters)
        if m < maxiters:
       	 	value = 255
       	else:
          saturation = 0

       		
        # draw
        image.putpixel([x, y], (hue, saturation, value))
#save
image.convert('RGB').save('output.png', 'PNG')





