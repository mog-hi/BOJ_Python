import heapq
n, m = map(int, input().split())
board = []
for i in range(m):
    board.append(list(map(int, list(input()))))

queue = []
heapq.heappush(queue, [0, 0, 0])
answer = float('inf')
visited = [[float('inf')] * n for _ in range(m)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while queue:
    cnt, x, y = heapq.heappop(queue)
    if x == m - 1 and y == n - 1:
        print(cnt)
        break
    if visited[x][y] <= cnt:
        continue
    visited[x][y] = cnt
    for i, j in move:
        cx, cy = x + i, y + j
        if 0 <= cx < m and 0 <= cy < n:
            if board[cx][cy] == 0:
                heapq.heappush(queue, [cnt, cx, cy])
            else:
                heapq.heappush(queue, [cnt + 1, cx, cy])
