num = int(input("enter your number"))

for i in range (2,num+1):
    if num%i==0 :
        isprime= True
        for j in range (2,i):
            if i%j==0:
                isprime=False
                break 

        if isprime:
            print(i)

         

   