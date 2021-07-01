def alphaToint(x):
    return ord(x)-65
def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i, j in move:
        cx, cy = i+x, j+y
        if 0<=cx<r and 0<=cy<c and not visited[alphaToint(board[cx][cy])]:
            visited[alphaToint(board[cx][cy])] = 1
            dfs(cx, cy, cnt+1)
            visited[alphaToint(board[cx][cy])] = 0

r, c = map(int, input().split())
board = []
for i in range(r):
    board.append(list(input()))
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited = [0]*26
visited[alphaToint(board[0][0])] = 1
answer = 0
dfs(0,0,1)
print(answer)

