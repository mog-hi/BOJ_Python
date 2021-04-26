import sys
input = sys.stdin.readline
board = []
for i in range(10):
    board.append(list(map(int, input().split())))

answer = float('inf')
arr = []
for i in range(10):
    for j in range(10):
        if board[i][j]:
            arr.append((i, j))

def backtracking(x, y, cnt):
    global answer, board
    if cnt>=answer: return
    if y >= 10:
        answer = min(answer, 25-sum(paper))
        return
    if x >= 10:
        backtracking(0,y+1, cnt)
        return
    if board[x][y] == 0:
        backtracking(x+1,y, cnt)
        return
    for k in range(1, 6):
        if paper[k] == 0: continue
        if x+k > 10 or y+k > 10:
            continue
        flag = True
        for i in range(x, x + k):
            for j in range(y, y + k):
                if board[i][j] == 0:
                    flag = False
                    break
        if flag:
            for i in range(x, x+k):
                for j in range(y, y+k):
                    board[i][j] = 0
            paper[k] -= 1
            backtracking(x+k, y, cnt+1)
            paper[k] += 1
            for i in range(x, x+k):
                for j in range(y, y+k):
                    board[i][j] = 1
paper = [0,5,5,5,5,5]
backtracking(0,0,0)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
