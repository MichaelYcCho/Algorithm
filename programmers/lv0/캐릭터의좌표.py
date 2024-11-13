def solution(keyinput, board):
    x, y = 0, 0
    xlim = board[0] // 2
    ylim = board[1] // 2

    for i in keyinput:
        if i == "right":
            if x >= xlim:
                x = xlim
            else:
                x += 1
        elif i == "left":
            if x <= -xlim:
                x = -xlim
            else:
                x -= 1
        elif i == "up":
            if y >= ylim:
                y = ylim
            else:
                y += 1
        elif i == "down":
            if y <= -ylim:
                y = -ylim
            else:
                y -= 1

    return [x, y]
