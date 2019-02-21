n = int(input())
start_num = 2
end_num = 30

print ("Diamond의 길이를 입력하세요(",start_num, "~", end_num, ") : ", n)

if n <= 1: 
    print("Please increase the value of the number.")
elif n > 30:
    print("Please decrease the value of the number.")
else:
    for i in list(range(1, n+1)):
        print(" " * (n-i), "*" * (2 * i - 1))
    for i in list(range(1, n+1)):
        print(" " * i, "*" * (((n-i)*2)-1))


