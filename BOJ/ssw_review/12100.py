from copy import deepcopy
move = [(0,-1),(0,1),(-1,0),(1,0)]
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
def play(d):
    if d == 0:
        for k in range(n):
            i = 0
            j = 1
            while j < n:
                if board[j][k] == 0 or i == j:
                    j += 1
                    continue
                if board[i][k] == 0:
                    board[i][k] = board[j][k]
                    board[j][k] = 0
                    j += 1
                else:
                    if board[i][k] == board[j][k]:
                        board[i][k] *= 2
                        board[j][k] = 0
                        j += 1
                    i += 1
    elif d == 1:
        for k in range(n):
            i = n-1
            j = n-2
            while j >= 0:
                if board[j][k] == 0 or i == j:
                    j -= 1
                    continue
                if board[i][k] == 0:
                    board[i][k] = board[j][k]
                    board[j][k] = 0
                    j -= 1
                else:
                    if board[i][k] == board[j][k]:
                        board[i][k] *= 2
                        board[j][k] = 0
                        j -= 1
                    i -= 1
    elif d == 2:
        for k in range(n):
            i = 0
            j = 1
            while j < n:
                if board[k][j] == 0 or i == j:
                    j += 1
                    continue
                if board[k][i] == 0:
                    board[k][i] = board[k][j]
                    board[k][j] = 0
                    j += 1
                else:
                    if board[k][i]== board[k][j]:
                        board[k][i] *= 2
                        board[k][j] = 0
                        j += 1
                    i += 1
    elif d == 3:
        for k in range(n):
            i = n-1
            j = n-2
            while j >= 0:
                if board[k][j] == 0 or i == j:
                    j -= 1
                    continue
                if board[k][i] == 0:
                    board[k][i] = board[k][j]
                    board[k][j] = 0
                    j -= 1
                else:
                    if board[k][i] == board[k][j]:
                        board[k][i] *= 2
                        board[k][j] = 0
                        j -= 1
                    i -= 1
answer = 0
def backtracking(cnt):
    global answer, board
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return
    for i in range(4):
        board_x = deepcopy(board)
        play(i)
        backtracking(cnt+1)
        board = board_x
backtracking(0)
print(answer)

