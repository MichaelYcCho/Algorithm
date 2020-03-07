def sol(InputArr):
    count = 0
    endTime = 0

    for i in range(len(InputArr)):
        if endTime <= InputArr[i][0]:
            endTime =  InputArr[i][1]
            count += 1


    return count


N = int(input())
InputArr = []

for i in range(N):
    a, b = list(map(int, input().split()))
    InputArr.append([a, b])


InputArr.sort(key=lambda x: (x[1], x[0]))

print(sol(InputArr))