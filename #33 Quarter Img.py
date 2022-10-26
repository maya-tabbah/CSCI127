#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#March 3, 2022

import matplotlib.pyplot as plt
import numpy as np

inp = input("Enter the name of an image: ")
out1 = input("Enter the name of an output file: ")

pic = plt.imread(inp)

pic2 = pic.copy()
wow = pic2.shape[0]
wow2 = pic2.shape[1]

pic2 = pic2[wow//2:,:wow2//2] 

#plt.imshow(pic2)
#plt.show()
plt.imsave(out1, pic2)
