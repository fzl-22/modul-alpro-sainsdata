def multiply(x, n):
    if n > 0:
        return x + multiply(x, n-1)
    elif n == 0:
        return 0

print(multiply(1, 0))