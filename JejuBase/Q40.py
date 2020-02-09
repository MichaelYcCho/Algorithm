total = 0
count = 0
limit = int(input()) # 무게제한
n = int(input()) #몇명이 탑승

for i in range(1, n+1):
    print(i)
    weight = int(input())
    if total <= limit:
        total += weight
        print(f"i값은 {i}")
        count = i
        if total >= limit:
            count = i-1
print(f"{count} 명 탑승가능합니다")