import sys


x = int(input())
num_list = list(map(int, input().split()))
result = []


def reverse_num(number):
    return int(str(number)[::-1])

def is_prime(number):
    for i in range(2, number):
        if number == 1:
            return False
        if number % i == 0:
            return False
    return True

for i in num_list:
    if is_prime(reverse_num(i)):
        result.append(reverse_num(i))

print(*result, sep=', ')


'''
sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        reverse_num = x % 10
        res = res * 10 + reverse_num
        x = x //10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



for i in a:
    reverse_num = reverse(i)
    if isPrime(reverse_num):
        print(reverse_num, end=" ")
'''