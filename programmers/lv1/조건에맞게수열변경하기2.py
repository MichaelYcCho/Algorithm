def solution(arr):
    idx = 0
    prev = arr

    while True:
        change = []
        for i in prev:
            if i >= 50 and i % 2 == 0:
                change.append(int(i / 2))
            elif i < 50 and i % 2 == 1:
                change.append(i * 2 + 1)
            else:
                change.append(i)

        same = all(a == b for a, b in zip(prev, change))
        if same:
            break
        idx += 1

        prev = change

    return idx


def solution(arr):
    answer = 0
    flag = True
    while flag:
        flag = False
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
                flag = True
            elif arr[i] < 50 and arr[i] % 2:
                arr[i] = arr[i] * 2 + 1
                flag = True
        answer += 1
    return answer - 1
