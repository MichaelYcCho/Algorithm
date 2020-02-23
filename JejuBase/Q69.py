
'''
# Case 1

prime = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            prime.append(i)



n = int(input())
for i in range(101//2+1):
    if i in prime and n-i in prime:
        print(i, n-i)


'''

# Case 2


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


소수집합 = prime_list(100)
#print(소수집합)



#골드바흐 파티션

n = int(input())
파티션 = []

for i in range(101//2+1):
    if i in 소수집합 and n-i in 소수집합:
        파티션.extend([[i, n-i]])


# 같은 내용 l = ['{} X {}  = {}'.format(i, j, i*J) for i in range(2, 10) for j in range(1, 10)]
# print(l)

print(파티션[-1])