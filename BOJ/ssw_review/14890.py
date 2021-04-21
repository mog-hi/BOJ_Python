n, l = map(int, input().split())
board = []
for i in range(n):
    board.append((list(map(int, input().split()))))

# 행부터
answer = 0
runway = [[0]*n for _ in range(n)]
for k in range(n):
    isAble = True
    for i in range(n-1):
        if abs(board[k][i] - board[k][i+1]) > 1:
            isAble = False
            break
        elif abs(board[k][i] - board[k][i+1]) == 0:
            continue
        if board[k][i] - board[k][i+1] == -1:
            if i-l+1 < 0 :
                isAble = False
                continue
            for j in range(i, i-l, -1):
                if board[k][i] != board[k][j] or runway[k][j]==1:
                    isAble = False
                    break
            else:
                for j in range(i, i-l, -1):
                    runway[k][j] = 1
        elif board[k][i] - board[k][i+1] == 1:
            if i+l > n-1:
                isAble = False
                continue
            for j in range(i+1, i+l+1):
                if board[k][i+1] != board[k][j] or runway[k][j]==1:
                    isAble = False
                    break
            else:
                for j in range(i+1, i+l+1):
                    runway[k][j] = 1
    if isAble:
        answer+= 1
# 열
runway = [[0]*n for _ in range(n)]
for k in range(n):
    isAble = True
    for i in range(n-1):
        if abs(board[i][k] - board[i+1][k]) > 1:
            isAble = False
            break
        elif abs(board[i][k] - board[i+1][k]) == 0:
            continue
        if board[i][k] - board[i+1][k] == -1:
            if i-l+1 < 0 :
                isAble = False
                continue
            for j in range(i, i-l, -1):
                if board[i][k] != board[j][k] or runway[j][k]==1:
                    isAble = False
                    break
            else:
                for j in range(i, i-l, -1):
                    runway[j][k] = 1
        elif board[i][k] - board[i+1][k] == 1:
            if i+l > n-1:
                isAble = False
                continue
            for j in range(i+1, i+l+1):
                if board[i+1][k] != board[j][k] or runway[j][k]==1:
                    isAble = False
                    break
            else:
                for j in range(i+1, i+l+1):
                    runway[j][k] = 1
    if isAble:
        answer+= 1
print(answer)




