def sumsum_123(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return sumsum_123(n-3) + sumsum_123(n-2) + sumsum_123(n-1)
    
n = int(input())

for num in range(n):
    result = sumsum_123(int(input()))
    print(result)