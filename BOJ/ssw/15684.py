def go(start):
    for i in range(1, h+1):
        if board[i][start] == 1:
            start += 1
        elif board[i][start] == -1:
            start -= 1
    return start

def dfs(loc, cnt):
    global answer
    if answer <= cnt:
        return
    for i in range(1, n+1):
        if i != go(i):
            break
    else:
        answer = min(answer, cnt)
        return
    if loc >= len(arr) or cnt >= 3: return
    for i in range(loc, len(arr)):
        a, b = arr[i]
        if board[a][b] == 0 and board[a][b+1] == 0:
            board[a][b] = 1
            board[a][b+1] = -1
            dfs(i+1, cnt+1)
            board[a][b] = 0
            board[a][b+1] = 0

n, m, h = map(int, input().split())
board = [[0]*(n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[a][b+1] = -1

arr = []
for a in range(1, h+1):
    for b in range(1, n):
        if not board[a][b] and not board[a][b+1]:
            arr.append((a, b))
answer = float('inf')
dfs(0, 0)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
