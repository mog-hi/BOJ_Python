N,M,K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
shark = [[0,0,0] for _ in range(M+1)]
di = list(map(int, input().split()))
for i in range(1, M+1):
    shark[i][2] = di[i-1]
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            shark[arr[i][j]][0] = i
            shark[arr[i][j]][1] = j
            board[i][j]=[arr[i][j], K]
direction = []
for i in range(M):
    direction.append([[] for _ in range(5)])
    for j in range(1, 5):
        direction[i][j] = list(map(int, input().split()))
move = [(), (-1,0),(1,0),(0,-1),(0,1)]

for t in range(1000):
    # 상어 이동
    for i in range(1, M+1):
        if not shark[i]: continue
        x, y, d = shark[i]
        dir_list = direction[i-1][d]
        for j in dir_list:
            cx = x + move[j][0]
            cy = y + move[j][1]
            if 0<=cx<N and 0<=cy<N and not board[cx][cy]:
                shark[i] = [cx, cy, j]
                break
        else:
            for j in dir_list:
                cx = x + move[j][0]
                cy = y + move[j][1]
                if 0<=cx<N and 0<=cy<N and board[cx][cy][0] == i:
                    shark[i] = [cx, cy, j]
                    break
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = []
    for i in range(1, M+1):
        if not shark[i]: continue
        x, y, d = shark[i]
        if board[x][y]:
            if board[x][y][0] == i:
                board[x][y] = [i, K]
            else:
                shark[i]= 0
        else:
            board[x][y] = [i, K]
    if shark.count(0) == M-1:
        print(t+1)
        break
else:
    print(-1)