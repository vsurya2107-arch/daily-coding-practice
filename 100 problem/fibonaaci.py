ran = int (input("enter your number of range"))
a =0
b=1 

for i in range (2,ran):
    c = a+b 
    a=b
    b=c
    print (c,end =" ")
