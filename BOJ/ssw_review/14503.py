n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[0]*m for _ in range(n)]
answer = 0
def clear(x, y, d):
    global answer
    if not visited[x][y]:
        answer+=1
        visited[x][y] = 1
    left = d
    for i in range(4):
        left = (left+3)%4
        cx = x+move[left][0]
        cy = y+move[left][1]
        if 0<=cx<n and 0<=cy<m and board[cx][cy]==0 and visited[cx][cy]==0:
            clear(cx, cy, left)
            return
    cx = x-move[d][0]
    cy = y-move[d][1]
    if 0<=cx<n and 0<=cy<m and board[cx][cy]== 0:
        clear(cx, cy, d)
    return
clear(x, y, d)
print(answer)