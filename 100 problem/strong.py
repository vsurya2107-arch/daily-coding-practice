num = int (input("enter you number "))
temp= num 
sum = 0 

while temp >0 :
    lastnumber = temp % 10 
    fact =1 
    for i in range (1,lastnumber+1):
        fact = fact * i                            # single set value tha iruku soo atha combine panna sum 
    sum = sum + fact 
    temp = temp //10 

if sum == num :
 print ("its strong number",num)
else:
 print ("its not strong number",num)
 
 #40585,145

