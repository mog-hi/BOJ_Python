n = int(input())
dragon = [[] for _ in range(n)]
board = [[0]*101 for _ in range(101)]
for k in range(n):
    y,x,d,g = map(int, input().split())
    dragon[k] = [d]
    change_dir = []
    for i in range(g):
        l = len(dragon[k])
        for j in range(l-1, -1, -1):
            dragon[k].append((dragon[k][j]+5)%4)
    move = [(0,1),(-1,0),(0,-1),(1,0)]
    board[x][y] = 1
    for i in dragon[k]:
        x += move[i][0]
        y += move[i][1]
        board[x][y] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] == 1:
            answer += 1
print(answer)

