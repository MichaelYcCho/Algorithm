E, S, M = map(int, input().split())

for i in range(1, 7981):
    if i % 15 == E or (i % 15 == 0 and E == 15):
        if i % 28 == S or (i % 28 == 0 and S == 28):
            if i % 19 == M or (i % 19 == 0 and M == 19):
                print(i)