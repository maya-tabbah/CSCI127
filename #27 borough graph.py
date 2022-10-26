#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#February 18, 2022
#This program printd a graph based on the data of population of the 5 boroughs
#that the user selects. 


import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5) #Skips 5 usless rows

borough = input("Enter a borough: ")
output = input("Enter the name of the output file: " )


pop['Fraction'] = pop[borough]/pop['Total']
pop.plot(x = "Year", y = 'Fraction') # x axis is the year #Y axis is set
                                        #to new column called fraction


fig = plt.gcf()
fig.savefig(output)

#plt.show() shows the graph 

#print(pop)
