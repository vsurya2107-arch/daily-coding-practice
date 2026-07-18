low = int(input ("enter your starting range"))
high = int (input ("enter your ending range"))
found= False

for i in range (low ,high+1):
    order = len(str(i))
    temp = i
    total=0
    
    while temp>0:
        lastnumber = temp%10
        total= total+(lastnumber**order)
        temp=temp//10


    if i == total :
        print (i,end =" ")
        found = True
if not found :
    print ("not exit amstrong number in the given range")
    


