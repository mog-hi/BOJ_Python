from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(starts):
    queue = deque()
    for i, j in starts:
        queue.append((i, j, 0))
    temp = deepcopy(board)
    visited = [[0]*n for _ in range(n)]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    result = 0
    while queue:
        i, j, time = queue.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = time
        temp[i][j] = 2
        for x, y in move:
            cx = i+x
            cy = j+y
            if 0<=cx<n and 0<=cy<n and board[cx][cy] != 1:
                queue.append((cx,cy,time+1))
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if visited[i][j] == 0: return float('inf')
                result = max(result, visited[i][j])
    return result
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))

answer = float('inf')
def backtracking(loc, cnt, arr):
    global answer
    if cnt == m:
        answer = min(answer, bfs(arr))
        return
    if loc >= len(virus):
        return
    for i in range(loc, len(virus)):
        arr.append(virus[i])
        backtracking(i+1, cnt+1, arr)
        arr.pop()
backtracking(0,0,[])
# for start in list(combinations(virus, m)):
#     answer = min(answer, bfs(start))
if answer == float('inf'):
    print(-1)
else:
    print(answer)