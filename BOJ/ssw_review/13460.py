from collections import defaultdict
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            blue = [i,j]
        elif board[i][j] == 'R':
            red = [i,j]
        elif board[i][j] == 'O':
            hole = [i,j]
move = [(0,-1),(0,1),(1,0),(-1,0)]
def go(x, y, d, color):
    board[x][y] = '.'
    while True:
        x += move[d][0]
        y += move[d][1]
        if 0<=x<n and 0<=y<m and board[x][y] == '.':
            continue
        else:
            if [x, y] == hole:
                return [x, y]
            x -= move[d][0]
            y -= move[d][1]
            board[x][y] = color
            return [x, y]
answer = 11
def dfs(cnt, red, blue):
    global answer
    if blue==hole:
        return
    if red==hole:
        answer = min(answer, cnt)
        return
    if cnt == 10:
        return
    for i in range(4):
        red_first = True
        if i == 0 and red[0]==blue[0] and red[1]>blue[1]:
            red_first = False
        if i == 1 and red[0]==blue[0] and red[1]<blue[1]:
            red_first = False
        if i == 2 and red[1]==blue[1] and red[0]<blue[0]:
            red_first = False
        if i == 3 and red[1]==blue[1] and red[0]>blue[0]:
            red_first = False
        if red_first:
            re = go(red[0], red[1], i, 'R')
            bl = go(blue[0], blue[1], i, 'B')
        else:
            bl = go(blue[0], blue[1], i, 'B')
            re = go(red[0], red[1], i, 'R')
        if red==re and bl==blue:
            continue
        dfs(cnt+1, re, bl)
        board[red[0]][red[1]] = 'R'
        board[blue[0]][blue[1]] = 'B'
        if re != hole:
            board[re[0]][re[1]] = '.'
        if bl != hole:
            board[bl[0]][bl[1]] = '.'
dfs(0, red, blue)
if answer == 11:
    print(-1)
else:
    print(answer)