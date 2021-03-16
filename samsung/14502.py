from collections import deque
import copy
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
ru = 0
ro = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0
def bfs():
    global answer
    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                queue.append((i, j))
    table = copy.deepcopy(board)
    while queue:
        x, y = queue.popleft()
        for i, j in move:
            cx = i+x
            cy = j+y
            if 0<=cx<n and 0<=cy<m and table[cx][cy] == 0:
                table[cx][cy] = 2
                queue.append((cx, cy))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                cnt += 1
    answer = max(cnt, answer)
def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(cnt+1)
                board[i][j] = 0
dfs(0)
bfs()
print(answer)