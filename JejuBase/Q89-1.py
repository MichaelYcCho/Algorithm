# 상 하 좌 우 : 1, 2, 3, 4

가로 = 4
세로 = 5
캐릭터위치 = [0, 1]
장애물 = [[0, 1], [1, 2], [2, 3], [1, 3]]


def makeMap(가로, 세로, 캐릭터위치, 장애물):
    전체맵 = [[0] * (가로 + 2) for i in range(세로 + 2)] 
    for i in range(len(전체맵)):
        for j in range(len(전체맵[0])):
            if i == 0 or j == len(전체맵[0])-1 or j == 0 or i == len(전체맵)-1:
                전체맵[i][j] = 2
    전체맵[캐릭터위치[0]+1][캐릭터위치[1]+1] = 1
    for 위치 in 장애물:
        전체맵[위치[0]+1][위치[1]+1] = 2 if 전체맵[위치[0]+1][위치[1]+1] != 1 else 1 
    return 전체맵


pm = makeMap(가로, 세로, 캐릭터위치, 장애물)
print(pm)


움직임 = [2, 2, 2, 4, 4, 4]
# pm = 전체맵

def 이동(pm, 움직임):
    x, y = 0, 0
    for i, m in enumerate(pm):  # i는 각각의 row번째, m은 pm의 각각의 row 순서가 매겨진채로 저장
        if 1 in m:
            x, y = m.index(1), i
    pm[y][x] = 0  # row먼저 고려해야하므로 [y][x]
    for i in 움직임:
        if i == 1 and pm[y-1][x] != 2:
            y -= 1
        if i == 2 and pm[y-1][x] != 2:
            y += 1
        if i == 3 and pm[y-1][x] != 2:
            x -= 1
        if i == 4 and pm[y-1][x] != 2:
            x += 1
    
    pm[y][x] = 1
    return pm

pm = 이동(pm, 움직임)
