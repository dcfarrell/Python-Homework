def recFunc(n, c):
    if c > 1:
        return n + recFunc(n,c-1)
    else:
        return n

num = int(input("Enter an integer: "))
count = int(input("Enter an integer to multiply by: "))
print(recFunc(num, count))