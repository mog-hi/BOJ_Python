from collections import deque
from heapq import heappop, heappush
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

sea = [[0]*n for _ in range(n)]
move = [(0,1),(1,0),(-1,0),(0,-1)]
def bfs(start_x, start_y, t):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        if sea[x][y]:
            continue
        sea[x][y] = t
        for i, j in move:
            nx, ny= x+i, y+j
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                queue.append((nx, ny))
def bfsw(t):
    while global_queue:
        x, y = global_queue.popleft()
        if sea[x][y] != t and sea[x][y] != 0:
            return visited[x][y]
        for i, j in move:
            nx, ny= x+i, y+j
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                global_queue.append((nx, ny))
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] and not sea[i][j]:
            cnt += 1
            bfs(i, j, cnt)

answer = float('inf')
for x in range(1, cnt+1):
    global_queue = deque()
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sea[i][j] == x:
                global_queue.append((i, j))
                visited[i][j] = 1
    temp = bfsw(x)
    answer = min(answer, temp-2)
print(answer)