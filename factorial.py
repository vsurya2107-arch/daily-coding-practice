ran = int(input("enter your range to retrive the foctorial number"))
fact =1 

if ran < 0 :
    print ("not posiible to execute for given number")

else:
    for i in range (1,ran+1):
        fact=fact*i

print ("the range of ",ran,"factorial is ",fact)