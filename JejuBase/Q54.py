# 연속수 판별

user_input = list(map(int, input().split(' ')))


def sol(l):
    l = sorted(l)
    for i in range(len(l)-1):
        if l[i]+1 != l[i+1]:
            return "NO"
    return "YES"

print(sol(user_input))