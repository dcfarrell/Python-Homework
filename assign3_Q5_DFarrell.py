numSales = int(input("Enter amount of sales: "))

salary = 200 + ((9/100) * numSales)

print("Salary = $" + str(salary))

if salary >= 1000:
    print("A perfect salesperson")
elif salary < 1000 and salary >= 500:
    print("A good salesperson")
else :
    print("A not-so-great salesperson")