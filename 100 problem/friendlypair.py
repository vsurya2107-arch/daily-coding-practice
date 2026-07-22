num1 = int (input("eneter your number 1:"))
num2 = int (input("eneter your number 2:"))
sum1 = 0 
sum2 = 0

for i in range (1,num1):
    if num1%i==0:
     sum1 = sum1+i 
    
    
for i in range (1,num2):
    if num2%i==0:
     sum2 = sum2+i 
     
if num2==sum1 and num1==sum2 :
         print ("its friendly pair")
else:
         print ("its not friendly pair")
         
         #220,284
