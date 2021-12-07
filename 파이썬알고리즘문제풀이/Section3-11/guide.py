import sys

sys.stdin = open('input.txt', 'r')

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

# i가 2일때 ~5개의 행 인덱스가 6이므로 i는 2에서 중단외어야한다.
# i는 5개씩 나누기위한 변수이다
for i in range(3):
    # j는 행이다
    for j in range(7):
        # 슬라이스의 마지막은 포함되지않으므로 0 ~ 4 / 1 ~ 5 / 2 ~ 6 까지를 설정
        tmp = board[j][i:i+5] 
        # 회문 확인
        if tmp ==tmp[::-1]:
            cnt += 1
            
        # 길이가 5개이므로 반쪽만 검사하면됨
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)
        
        
        