num = int (input ("enter your number "))

sum = 0

for i in range (1,num):
        if num%i==0:
            sum = sum + i
            
if sum > num :
    print ("its abundant number ")
else:
    print ("its not abundant number")
    
    #12