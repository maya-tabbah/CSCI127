#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#March 18, 2022

import matplotlib.pyplot as plt
import pandas as pd 


file = input("Enter CSV file name: ")

collisons = pd.read_csv(file)

print(collisons["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
