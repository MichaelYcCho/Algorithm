num_list = []

while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        continue
    num_list.append(n)

max_num = max(num_list)

testPrime = [1 for i in range(max_num + 1)]
primeL = []

i = 2
while i <= max_num:
    if testPrime[i] == 1:
        primeL.append(i)
        for j in range(i + i, max_num + 1, i):
            testPrime[j] = 0
    i += 1


for i in num_list:
    for j in primeL:
        if testPrime[i - j] == 1:
            print(f"{i} = {j} + {i - j}")
            break
    else:
        print("Goldbach's conjecture is wrong.")