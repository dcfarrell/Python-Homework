print("Enter three integers greater than zero: ")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a + b >= c and b + c >= a and c + a >= b:
    print("All three numbers represent a triangle's sides")
else :
    print("Numbers do not represent sides of a triangle")