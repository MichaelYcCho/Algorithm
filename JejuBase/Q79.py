# l = [10, 20, 25, 27, 34, 35, 39]
# n = int(input('순회횟수는 : '))


def sol(l, turn):
    lCopy = l.copy()
    result = []
    for i in range(turn):
        # pop 한값을 다시 0으로 insert시키면서 순회시킴
        lCopy.insert(0, lCopy.pop())
    for i, j in zip(l, lCopy):
        result.append(abs(i-j))
    index = result.index(min(result))
    print(index)
    print(l[index], lCopy[index])



sol([10, 20, 25, 27, 34, 35, 39], 2)


