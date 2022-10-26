#Maya Tabbah
#maya.tabbah40@myhuter.cuny.edu
#February 1, 2022

#This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has only the blue channel displayed.



#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

file = input("Enter the name of a png file: ")
output = input("Enter output file: ")

out1 = plt.imread(file)   #Read in image from csBridge.png
plt.imshow(out1)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

out2 = out1.copy()        #make a copy of our image
out2[:,:,1] = 0          #Set the green channel to 0
out2[:,:,0] = 0          #Set the red channel to 0

plt.imshow(out2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave(output, out2)  #Save the image we created to the file: blueH.png
