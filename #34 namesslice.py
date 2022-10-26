#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#March 11, 2022
#This program prints a list of names entered by the user

names = input("Enter a list of names (last name, first name) seperated by semicolons: " )
outNames = names.split(";")


for i in outNames:
    x = i.split(",")
    print(x[-1],x[0])

print("Thank you for using my name organizer")


