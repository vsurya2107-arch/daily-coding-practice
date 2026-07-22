num1= int (input ("enter your number 1 :"))
num2= int (input ("enter your number 2 :"))

small = min (num1,num2)

for i in range (small,0,-1):
    if num1%i==0 and num2%i==0 :
        print ("the highest common factor is =",i)
        break