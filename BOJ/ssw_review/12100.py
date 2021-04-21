from copy import deepcopy
move = [(-1,0),(1,0),(0,-1),(0,1)]

def play(d):
    global board
    if d == 0 or d == 1:
        for k in range(n):
            if d==0: i,j = 0, 1
            else: i,j = n-1, n-2
            while 0<=i <n and 0<= j <n :
                if i == j or board[j][k] ==0:
                    j -= move[d][0]
                    continue
                if board[i][k] == 0:
                    board[i][k] = board[j][k]
                    board[j][k] = 0
                    j -= move[d][0]
                else:
                    if board[i][k] == board[j][k]:
                        board[i][k] *= 2
                        board[j][k] = 0
                        i -= move[d][0]
                        j -= move[d][0]
                    else:
                        i -= move[d][0]
    else:
        for k in range(n):
            if d==2: i,j = 0, 1
            else: i,j = n-1, n-2
            while 0<=i <n and 0<= j <n :
                if i == j or board[k][j] ==0:
                    j -= move[d][1]
                    continue
                if board[k][i] == 0:
                    board[k][i] = board[k][j]
                    board[k][j] = 0
                    j -= move[d][1]
                else:
                    if board[k][i] == board[k][j]:
                        board[k][i] *= 2
                        board[k][j] = 0
                        i -= move[d][1]
                        j -= move[d][1]
                    else:
                        i -= move[d][1]

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0
def backtracking(cnt):
    global answer, board
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return
    b = deepcopy(board)
    for i in range(4):
        play(i)
        backtracking(cnt+1)
        board = deepcopy(b)
backtracking(0)
print(answer)