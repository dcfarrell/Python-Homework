def recFunc(n):
    if n > 1:
        return n + recFunc(n-1)
    else:
        return 1

num = int(input("Enter an integer: "))
print(recFunc(num))