#Oct 25
#I really enjoy this visual! Z is to the fourth power. I played around with the color a lot for this one. If the number of iterations it took to 
#escape (or when the # of iterations exceeded the maxiter) is even, the "layer" will be colored either white or with randomly colored pixels.
#if the number of iterations is odd, the "layer" will either be colored black or with a rainbow gradient. That's about it!


from PIL import Image
import colorsys
import random as r

#max iterations
maxiters = 101

#calculation
def mandelbrot(c):
    z = 0
    n = 0
    # escaped?
    while abs(z) <= 2 and n < maxiters:
        z = z**4+ c 
        n += 1
    return n

# size
imgx, imgy = 1000,1000

# plot
xmin = -0.05 
xmax = 0.7
ymax = -0.1
ymin = 0.75

#define image
image = Image.new('HSV', (imgx, imgy), (0, 0, 0))

#all x
for x in range(0, imgx):
    #all y
    for y in range(0, imgy):
        # Convert pixel coordinate to complex number
        c = complex(xmax + (x / imgx) * (xmin - xmax),
                    ymax + (y / imgy) * (ymin - ymax))
        # does function, computes iters
        m = mandelbrot(c)
        # colors 
        #is the number of iterations before escape/end even?
        if m%2 == 0:
            #is it divisible by 4?
            if m%4 == 0:
                #colorful
                hue = r.randrange(360)
                saturation = 255
                value = 255
            #white
            else:
                hue = 0
                value = 255
                saturation = 0
        #it's odd
        else:
                #is it divisible by three?
                if m%3 == 0:
                    #rainbow
                    hue = (imgy-y)%180
                    saturation = 255
                    value = 255
                #black
                else:
                    hue = 0
                    saturation = 0 
                    value = 0
        # draw
        image.putpixel([x, y], (hue, saturation, value))
#done
image.convert('RGB').save('output3.png', 'PNG')





