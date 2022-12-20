# 재귀트리
# KeyWord - 순열, 재귀, 백트래킹, Recursion Tree


def permutation(arr, start):
    print("날 호출했어요!")
    print("start: ", start)
    print("len(arr) - 1: ", len(arr) - 1)

    if len(arr) - 1 == start:
        print(arr)
        return

    for idx in range(start, len(arr)):
        print("start: ", start, "idx: ", idx, "len(arr)", len(arr))
        print("arr[start]: ", arr[start], "arr[idx]: ", arr[idx])
        arr[start], arr[idx] = arr[idx], arr[start]
        print()
        permutation(arr, start + 1)
        arr[start], arr[idx] = arr[idx], arr[start]
        print()
    

if __name__ == "__main__":
    arr = [1, 2, 3]
    permutation(arr, 0)