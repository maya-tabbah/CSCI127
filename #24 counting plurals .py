#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#February 15, 2022
#This program prints the amount of plural nouns in an input of nouns


noun = input("Enter a list of nouns seperated by spaces: ")

output = noun.split()


i = 0
i2 = 0

for c in output:
    i += 1
    
    if c[-1] == "s":
        i2 += 1
        
print(i)

print(i2/i)

    



