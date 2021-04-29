n, m = map(int, input().split())
board = []
r, c, d = map(int,input().split())
for i in range(n):
    board.append(list(map(int, input().split())))
move = [(-1,0),(0,1),(1,0),(0,-1)]
answer = 0
while True:
    if board[r][c] == 0:
        answer += 1
    board[r][c] = 2
    nd = d
    for i in range(4):
        nd = (nd + 3) % 4
        nr, nc = r+move[nd][0], c+move[nd][1]
        if 0<=nr<n and 0<=nc<m and board[nr][nc] == 0:
            r, c, d = nr, nc, nd
            break
    else:
        nr = r-move[d][0]
        nc = c-move[d][1]
        if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] == 1:
            break
        r, c = nr, nc
print(answer)
