#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#April 8, 2022


ADDI $s0, $zero, 0 #set
ADDI $s1, $zero, 10  #incriment 
ADDI $s2, $zero, 50  #incriment 
AGAIN: ADD $s0, $s0, $s1 # add
BEQ $s0, $s2, DONE  #condition
J AGAIN #looping thingy 
DONE:  #To break out of the loop
