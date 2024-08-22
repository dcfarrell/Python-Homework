def recFunc(n):
    if n > 2:
        return 2 * recFunc(n-2) + 3
    else:
        return 1

num = int(input("Enter an integer: "))
print(recFunc(num))