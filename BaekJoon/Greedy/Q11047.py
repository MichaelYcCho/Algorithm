n, k = list(map(int, input().split()))

coin = []
for i in range(n):
  val = int(input())
  coin.append(val)

coin = sorted(coin, reverse=True)


count = 0

for i in range(n):
  if k >= coin[i]:
    mok = k//coin[i]
    print(f'mok: {mok}')
    k -= coin[i]*mok
    print(f'k: {k}')  
    count += mok

print(count)
