#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#February 4, 2022



import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter the size of the image: "))
output = input("What is the name of the output file?: ")

stripesImg = np.ones((size,size,3))

stripesImg[::2,:,1:] = 0

#plt.imshow(stripesImg)
#plt.show()
plt.imsave(output,stripesImg)
