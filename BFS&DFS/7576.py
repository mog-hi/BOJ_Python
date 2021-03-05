import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(queue):
    global dp
    while queue:
        i, j = queue.popleft()
        for plusx, plusy in move:
            x = plusx + i
            y = plusy + j
            if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
                arr[x][y] = arr[i][j] + 1
                queue.append((x, y))

start = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            start.append((i, j))
bfs(start)
answer = 0
disable = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            disable = True
        answer = max(answer, arr[i][j])
if disable:
    print(-1)
else:
    print(answer-1)