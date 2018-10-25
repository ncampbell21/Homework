#Oct 25 
#See mandelbrot1 for description



#import PIL
from PIL import Image

#open images
image1 = Image.open("./output.png")
image2 = Image.open("./output2.png")

#blend them
wow1 = Image.blend(image1,image2, alpha = .5)

#save
wow1.save('Final1.png','PNG')