a = int (input (" enter you number"))
temp = a 
count = len (str(a))   # number of digit theriya 
total = 0 # storing present value for each itration 

while temp > 0:
    lastnumber = temp%10
    total = total+(lastnumber** count)
    temp = temp//10

if a == total :
    print("its amstrong number",a)
else:
    print("its not amstrong number ",a)