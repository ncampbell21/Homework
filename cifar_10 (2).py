
import sklearn
from sklearn import linear_model


from sklearn import svm
from sklearn.svm import SVC

import numpy as np
import pickle
import os

#OMH I have neither given nor recieved unauthorized aide.
#Feb. 24

#Sources:
#scikit-learn.org
#https://towardsdatascience.com/support-vector-machine-vs-logistic-regression-94cc2975433f
#https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science
#https://kapilddatascience.wordpress.com/2016/11/06/how-cifar-10-data-set-trained-me-to-become-a-deep-learning-scientist/
#Mike Gao
#https://www.cs.toronto.edu/~kriz/cifar.html


#Even though it might not look like much to someone who knows about machine learning, this project was HARD. Honestly, I spent more time
#googling and researching than I have ever had to - the machine learning world is kind of inaccesible in my experience. However, in the end
#I was able to pull this together! The bulk of the code is actually setting up the data and structuring it nicely, and the end is where 
#we implement svm and get some accuracy scores. Now, I didn;t have the time nor the knowledge to truly get into the parameters
#and really optimize the model  - I do not have the math or computer science skills for that yet. Another really frustrating issue was that 
#I was quite literally unable to use all 50,000 training images to train the model, as i let it run until it timed out and it had still
#not finished. However, if my computer could load them all, the accuracy would like just above %50, which I am really proud of actually, 
#considering that guessing would've yielded 10% accuracy. Also, I was advised against using a neural network because of my limited experience
# so with a linear model it would be very difficult to achieve a high % accuracy. Anyways, I hope you enjoy - and unless you have a LOT of storeage
# I would not recommend running this on your computer. Although I had an extension because all of this was so new to me, I just didn't have 
#time to learn the right ways to calculate accuracy and all of that stuff - it took a ton of time to just choose the base settings and model 
#that I wanted to use!

def one_hot_encoded(class_numbers, num_classes=None):
  
 #One hot-encoding is a way of setting up categorical data so that it's easy 
#for the computer to process. You can read about it here: https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science

    #find the number of classes if not provided
    if num_classes is None:
        num_classes = np.max(class_numbers) + 1

    return np.eye(num_classes, dtype=float)[class_numbers]

#setting up stuff for importing data 
data_path=''

#CIFAR-10 image dimensions
img_size = 32
#RGB images
num_channels = 3

#lenght of flattenned image array 
img_size_flat = img_size * img_size * num_channels

# CIFAR-10 has 10 types of images
num_classes = 10


#break up 50,000 training images into 5 groups of 10k
_num_files_train = 5

#10k per file 
_images_per_file = 10000

#total number of images in the training-set - 50k
_num_images_train = _num_files_train * _images_per_file




def _get_file_path(filename=""):

     #returns the file path of the given batch
    return os.path.join(data_path, "cifar-10-batches-py/", filename)


def _unpickle(filename):
    

    #create full path for file
    file_path = _get_file_path(filename)

    #just so that you can see it 
    print("Loading data: " + file_path)

    # get file data
    with open(file_path, mode='rb') as file:
        data = pickle.load(file,  encoding='latin1')
    #return it 
    return data


def _convert_images(raw):


    #convert images from the data-files to numbers
    raw_float = np.array(raw, dtype=float) / 255.0

    #reshape the array to 4-dimensions.
    images = raw_float.reshape([-1, num_channels, img_size, img_size])

    #reorder the indices of the array.
    images = images.transpose([0, 2, 3, 1])
    
    return images


def _load_data(filename):
   
    #load a pickled data-file from CIFAR-10
    #and return the converted images and the class number

    #load the pickled data-file
    data = _unpickle(filename)

    #get the raw images
    raw_images = data['data']

    #get the class-numbers for each image - convert to numpy-array
    cls = np.array(data['labels'])

    #convert the images
    images = _convert_images(raw_images)

    #image data and labels 
    return images, cls


def load_class_names():
   
    #load the names for the classes in dataset
    #returns a list with the names

    #load the names from the pickled file
    raw = _unpickle(filename="batches.meta")['label_names']

    #convert
    return raw


def load_training_data():
    
    #load all the training data from the 5 data files and merge them
    #return the images class numbers and one-hot encoded classlabels
   

    #empty arrays for the images and class-numbers 
    images = np.zeros(shape=[_num_images_train, img_size, img_size, num_channels], dtype=float)
    cls = np.zeros(shape=[_num_images_train], dtype=int)

    #starting index for batch
    begin = 0

    #for eachfile
    for i in range(_num_files_train):
        #load the images and class numbers from the file
        images_batch, cls_batch = _load_data(filename="data_batch_" + str(i + 1))

        #number of images in  batch
        num_images = len(images_batch)

        #last index for  batch
        end = begin + num_images

        #store the images in array
        images[begin:end, :] = images_batch

        #store the classes into  array
        cls[begin:end] = cls_batch

        #the begin index for the next batch is the last index of last batch
        begin = end

    return images, cls, one_hot_encoded(class_numbers=cls, num_classes=num_classes)


def load_test_data():
    #FINALLY! Load all the data !! 
    #gives images, class labels and numbers
    
    images, cls = _load_data(filename="test_batch")

    return images, cls, one_hot_encoded(class_numbers=cls, num_classes=num_classes)

!wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz #mike helped me with this - just retreiving the raw batches from web

!tawr -zxvf cifar-10-python.tar.gz #mike helped me with this - just retreiving the raw batches

class_names = load_class_names() #setting the class names

images_train, cls_train, labels_train = load_training_data() #setting up training images, labels, etc
images_test, cls_test, labels_test = load_test_data() #setting up testing images, labels, etc

x_train = images_train.reshape(images_train.shape[0],-1) #just reshape training data by removing dimension
x_test = images_test.reshape(images_test.shape[0], -1) # just reshape testing dataz by removing dimension

clf = SVC(gamma='auto') #defining clf - variable that represents SVC - I set gamma to auto bcs i didn't want to get into that
clf.fit(x_train,cls_train) #WOO! time to train :)

matches = 0
notmatches = 0

for item in clf.predict(x_test[0:100]): #I just predicted w/ 100 of the testing data 
		if item == item1: #if prediction = label
			matches +=1 #print the label
		else:
			notmatches +=1
      
print(matches)
print(notmatches)
