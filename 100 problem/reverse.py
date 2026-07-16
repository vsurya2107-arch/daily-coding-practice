num = int(input("enter your number "))
temp = num 
reverse=0

while num !=0:
    lastnumber = num%10
    reverse = (reverse*10)+lastnumber
    num = num//10

print("the reverse number is",reverse )