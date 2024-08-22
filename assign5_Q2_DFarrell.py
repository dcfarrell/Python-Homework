def recFunc(n):
    if n > 1:
        return recFunc(n-2) + 1
    else:
        return 1

num = int(input("Enter an integer: "))
print(recFunc(num))