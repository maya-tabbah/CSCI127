#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#March 22, 2022

import turtle

def triangle(turt1, length):

    if length > 10:
        for i in range(3):
            turt1.forward(length)
            turt1.left(120)
        triangle(turt1, length//2)



def nestedTriangle(turt2, length):
    
    if length > 10:
        for i in range(3):
            turt2.forward(length)
            turt2.left(120)
            nestedTriangle(turt2, length//2)



def main():

    length = int(input("Enter a length: "))

    turt1 = turtle.Turtle()
    triangle(turt1, length)
    
    turt2 = turtle.Turtle()
    nestedTriangle(turt2,length)

if __name__ == "__main__":
    main()
    
