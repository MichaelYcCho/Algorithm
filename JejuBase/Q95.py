
def sol(도장, 회전):
    N = len(도장)   # 4반환
    l = [[0] * N for i in range(N)] # 4 * 4 배열 

    sum_matrix(l, 도장)
    for i in range(회전):
        도장 = rotate(도장)
        l = sum_matrix(l, 도장)
    return l    

def rotate(도장):
    N = len(도장)
    rot = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = 도장[i][j]

    return rot

def sum_matrix(l, 도장):
    N = len(도장)
    for i in range(N):
        for j in range(N):
            l[i][j] += 도장[i][j]
    
    return l


도장 = [
    [1,1,1,2],
    [2,0,0,0],
    [1,1,1,1],
    [0,0,0,0],
]

회전 = 1

print(sol(도장, 회전))
