import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))
sum_list = []

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            result = a[i] + a[j] + a[m]
            sum_list.append(result)

#reverse를 통해 내림차순으로 정렬
sum_list.sort(reverse=True)
#print(sum_list)
print(sum_list[k-1])


'''
모범답안
#sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])


res = list(res)
res.sort(reverse=True)
print(res[k-1])
'''