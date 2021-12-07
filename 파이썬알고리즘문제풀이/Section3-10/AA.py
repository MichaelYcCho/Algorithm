import sys
sys.stdin = open('input.txt', 'r')


def check(a):
    for i in range(9):
        # ch1 행을 체크할 index, ch2 열을 체크할 index
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1  # 행으로 체크
            ch2[a[j][i]] = 1 # 열로 체크
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    
    # 대각선 계산을 위한 그룹 탐색
    # i ~ j는 9개의 그룹(3 * 3 전체에대해서)을 보겠다는 의미
    for i in range(3):
        for j in range(3): 
            ch3 = [0] * 10
             # k ~l은 각 그룹의 9개의 숫자를 보겠다는 의미
            for k in range(3):
                for l in range(3):
                    ch3[a[i*3+k][j*3+l]] = 1
            if sum(ch3) != 9:
                return False
        



a = [list(map(int, input().split())) for _ in range(9)]
#print(a)
if check(a):
    print("YES")
else:
    print("NO")