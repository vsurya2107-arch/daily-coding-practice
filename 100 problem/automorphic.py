num = int (input("enetr your number"))

square = num**num

if str(square).endswith (str(num)):
    print ("its automorphic number")
else:
    print("not automorphic number")