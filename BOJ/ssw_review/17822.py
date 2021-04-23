from copy import deepcopy

def turn(x, d, k):
    global board
    temp = deepcopy(board)
    for i in range(x-1, n, x):
        for j in range(m):
            if d == 0:
                temp[i][j] = board[i][(j-k+m)%m]
            else:
                temp[i][j] = board[i][(j+k+m)%m]
    board = temp
def check():
    global board
    temp = deepcopy(board)
    is_delete = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: continue
            if board[i][j] == board[i][(j-1+m)%m] or board[i][j] == board[i][(j+1+m)%m]:
                is_delete = True
                temp[i][j] = 0
    for j in range(m):
        for i in range(n-1):
            if board[i][j] == 0: continue
            if board[i][j] == board[i+1][j]:
                is_delete = True
                temp[i][j] = 0
                temp[i+1][j] = 0
    if not is_delete:
        total = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j]:
                    total += temp[i][j]
                    cnt += 1
        if cnt == 0: return
        avg = total/cnt
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0: continue
                if temp[i][j] > avg:
                    temp[i][j] -= 1
                elif temp[i][j] < avg:
                    temp[i][j] += 1
    board = temp

n, m, t = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(t):
    x, d, k = map(int, input().split())
    turn(x, d, k)
    check()
answer = 0
for i in range(n):
    for j in range(m):
        answer += board[i][j]
print(answer)