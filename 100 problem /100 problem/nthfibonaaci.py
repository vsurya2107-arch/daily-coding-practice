ran=int (input ("enter your number"))
a=0
b=1

if ran==0 :
     print(a)

elif ran==1 :
     print(b)

else :
     for i in range (3,ran+1):
         c=a+b
         a=b
         b=c

     print(b) 

    
