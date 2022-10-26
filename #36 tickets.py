#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#march 16, 2022

import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
attribute = input("Enter an attribute")
print(tickets[attribute].value_counts()[:10]) #Print out the dataframe
