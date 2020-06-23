import sys

sys.stdin = open("input.txt", "rt")

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    numCase = list(map(int, input().split()))

    numCase = numCase[s-1:e]
    numCase.sort()
    print("#%d. %d" %(t+1, numCase[k-1]))

