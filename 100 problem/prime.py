n=int(input("enter your number "))
count =0 
for i in range (1,n+1):
    if n%i==0:
        count = count +1
if count ==2 :
    print ("its prime number")
else:
    print ("its not prime number")
