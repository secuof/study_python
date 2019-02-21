
n = int(input())

for i in list(range(1, n+1)):
    print(" " * (n-i), "*" * (2 * i - 1))

for i in list(range(1, n+1)):
    print(" " * i, "*" * (((n-i)*2)-1))

