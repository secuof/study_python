## Name Function
def hello(name):
    print("Hello, %s!" % (name))
    print("Welcome to My world!")

## Calculator Function
def print_sum(a, b):
    print(a + b)

def print_product(a, b):
    print(a * b)
  
def print_residue(a, b):
    print(a % b)
  
def print_average(x, y, z):
    print((x + y + z) / 3)

## Profile Function
def print_profile(name, age):
    print(name)
    print(age)

## What is the next number?
def next_number(n):
    m = n + 1
    print(m)

# print_full_name 함수 정의
# 코드를 입력하세요.
def print_full_name(first_name, last_name):
    print("%s, %s" % (last_name, first_name))

## 거스름돈 계산기
def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand_count = int(change / 50000)
    change = change % 50000
    ten_thousand_count = int(change / 10000)
    change = change % 10000
    five_thousand_count = int(change / 5000)
    change = change % 5000
    one_thousand_count = int(change / 1000)
    print("50,000원 지폐: %d장" % (fifty_thousand_count))
    print("10,000원 지폐: %d장" % (ten_thousand_count))
    print("5,000원 지폐: %d장" % (five_thousand_count))
    print("1,000원 지폐: %d장" % (one_thousand_count))

# 테스트 코드
print_full_name("윤수", "이")
print_full_name("수민", "이")

hello("David")
print_sum(4, 2)
print_product(3, 4)
print_residue(13, 3)
print_average(5, 10, 15)
print_profile("David", "37")
next_number(3)

## (payment, cost)
calculate_change(100000, 33000)
calculate_change(500000, 378000)
