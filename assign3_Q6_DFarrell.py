print("Please enter 5 floats: ")
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
d = float(input("Enter 4th number: "))
e = float(input("Enter 5th number: "))

nums = [a, b, c, d, e]

max = nums[0]
min = nums[0]

for i in nums:
    if i > max:
        max = i
    if i < min:
        min = i

print("Biggest number: " + str(max))
print("Smallest number: " + str(min))