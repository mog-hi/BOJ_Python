from itertools import combinations
from copy import deepcopy
from collections import deque
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(board):
    queue = deque()
    for x, y in virus:
        queue.append((x, y))
    visited = [[0]*m for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        if visited[x][y]: continue
        visited[x][y] = 1
        for i, j in move:
            cx = i+x
            cy = j+y
            if 0<=cx<n and 0<=cy<m and board[cx][cy] == 0:
                queue.append((cx, cy))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
virus = []
null = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            null.append((i, j))
combi = list(combinations(null, 3))
answer = 0
for i in range(len(combi)):
    temp = deepcopy(board)
    for x, y in combi[i]:
        temp[x][y] = 1
    cnt = bfs(temp)
    answer = max(answer, cnt)
print(answer)