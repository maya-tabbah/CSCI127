#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt



inp = input("Specify the input file: ")
out = input("Specify the output file: ")

homeless = pd.read_csv(inp)

homeless["Fraction Children"] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")



fig = plt.gcf()
fig.savefig(out) 
#plt.show()
