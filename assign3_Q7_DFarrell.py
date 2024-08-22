from cmath import sqrt


print("Please enter coefficent a, b, & c: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (b + sqrt(b ** 2 - (4 * a * c)))/(2 * a)
root2 = (b - sqrt(b ** 2 - (4 * a * c)))/(2 * a)

print("Root 1: " + str(root1))
print("Root 2: " + str(root2))