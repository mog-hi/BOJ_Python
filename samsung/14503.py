n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
visited = [[False]*m for _ in range(n)]
queue = [(r, c, d)]
answer = 0
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while queue:
    r, c, dir = queue.pop()
    if not visited[r][c]:
        visited[r][c] = True
        answer += 1
    d = dir
    for _ in range(4):
        d = (d+3)%4
        i, j = move[d][0], move[d][1]
        x = i+r
        y = j+c
        if 0<=x<n and 0<=y<m and board[x][y] == 0 and not visited[x][y]:
            queue.append((x, y, d))
            break
    else:
        d = (dir + 2) % 4
        x = r + move[d][0]
        y = c + move[d][1]
        if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
            queue.append((x, y, dir))
        else:
            break
print(answer)