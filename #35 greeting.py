#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#march 16, 2022


time = int(input("Enter a time (24 hour format): "))

if time < 12:
    print("Good Morning")
elif time > 12 and time < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
    
