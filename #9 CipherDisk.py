#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu


word = input("Enter a word: ")
blank = " "


for i in word:
    if ord(i)+13>122:
        blank+=chr(ord(i)-26+13)

    else:
        blank+=chr(ord(i)+13)


print("Your word in code is", blank)
