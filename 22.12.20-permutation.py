# 재귀트리
# KeyWord - 순열, 재귀, 백트래킹, Recursion Tree


def permutation(arr, start):

    if len(arr) - 1 == start:
        return

    for idx in range(start, len(arr)):

        arr[start], arr[idx] = arr[idx], arr[start]

        permutation(arr, start + 1)
        arr[start], arr[idx] = arr[idx], arr[start] # 재배치 첫번째 사이클 기준 2, 2 이므로 첫번째 숫자를 2로 바꾸고 idx 1시작

if __name__ == "__main__":
    arr = [1, 2, 3]
    permutation(arr, 0)