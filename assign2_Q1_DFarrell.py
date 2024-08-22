from cmath import pi


r = input("Enter Diameter in Inches: ")
area = pi*(int(r)/2)**2
numSlices = round(area/14.125)
print("Number of slices: " + str(numSlices))