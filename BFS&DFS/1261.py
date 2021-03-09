# 최단 경로
from collections import deque
m, n = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, list(input()))))
cnt = [[float('inf')]*m for _ in range(n)]
queue = deque()
queue.append((0, 0))
cnt[0][0] = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while queue:
    x, y = queue.popleft()
    for i, j in move:
        cx = x + i
        cy = y + j
        if 0 <= cx < n and 0 <= cy < m:
            if cnt[cx][cy] > cnt[x][y] + board[cx][cy]:
                cnt[cx][cy] = cnt[x][y] + board[cx][cy]
                queue.append((cx, cy))
print(cnt[n-1][m-1])

