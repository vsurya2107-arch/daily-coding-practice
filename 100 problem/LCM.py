num1= int (input ("enter your number 1 :"))
num2= int (input ("enter your number 2 :"))

high  = min (num1,num2)

while True :
    if high%num1==0 and high%num2==0 :
        print ("the leaset comman multiple =",high)
        break
    high = high + 1