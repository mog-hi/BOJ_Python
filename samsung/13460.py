from collections import deque
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def move(x,y,dx,dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt
def bfs():
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if board[rx][ry] == 'O':
            print(depth)
            return
        if visited[rx][ry][bx][by]: continue
        visited[rx][ry][bx][by] = True
        for dx, dy in direction:
            torx, tory, rcnt = move(rx, ry, dx, dy)
            tobx, toby, bcnt = move(bx, by, dx, dy)
            if board[tobx][toby] == 'O':
                continue
            if torx == tobx and tory == toby:
                if rcnt > bcnt:
                    torx -=dx
                    tory -= dy
                else:
                    tobx -=dx
                    toby -= dy
            queue.append((torx, tory, tobx, toby, depth+1))
    print(-1)

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))
start = [0, 0, 0, 0, 0]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            start[0] = i
            start[1] = j
        elif board[i][j] == 'B':
            start[2] = i
            start[3] = j
dp = [[-1]*m for _ in range(n)]
queue = deque()
queue.append(start)
bfs()