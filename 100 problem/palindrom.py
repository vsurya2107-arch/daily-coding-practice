a = int(input("enter your number"))
temp= a
reverce=0

while temp >0:
    lastnumber =temp%10
    reverce =(reverce*10)+lastnumber
    temp = temp//10

if reverce == a :  # a is become empty so take temp 
    print("the number is palindrome")
else :
    print("not a palindrome")