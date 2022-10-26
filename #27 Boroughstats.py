#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#February 25, 2022
#This program uses a csv file with data to find the maximum amout of
#population and mean amount 

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv("nycHistPop.csv", skiprows=5)

borough = input("Enter a borough: ")

print(pop[borough].max())
print(pop[borough].mean())
