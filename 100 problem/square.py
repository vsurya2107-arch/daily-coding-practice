import math
num = int (input ("enter your number "))
root = int (math.sqrt(num))

if root*root == num :
    print ("its perfect square")
else:
 print("its not perfect square")