num = int (input("enetr your number "))
temp  = num 
count = 0 

while temp >0 :
    lastnumber = temp%10 ;
    count = count + lastnumber
    temp=temp//10 
    
if num %count == 0 :
        print ("its harshad number")
else:
        print("its not harshad number")
        
        #50,21