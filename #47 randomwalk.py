#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#April 5, 2022


import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)
