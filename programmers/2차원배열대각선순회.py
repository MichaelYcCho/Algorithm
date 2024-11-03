def solution(board, k):
    answer = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer.append(board[i][j])
    return sum(answer)


def solution(board, k):
    answer = 0
    n, m = len(board), len(board[0])
    for i in range(k + 1):
        if i >= n:
            continue
        for j in range(k + 1 - i):
            if j >= m:
                continue
            answer += board[i][j]
    return answer
