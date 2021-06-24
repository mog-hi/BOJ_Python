n, k = map(int, input().split())
board = []
horse = []
arr = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))
for j in range(k):
    x, y, d = map(int, input().split())
    x, y, d = x-1, y-1, d-1
    horse.append([x,y,d])
    arr[x][y].append(j)
move = [(0,1),(0,-1),(-1,0),(1,0)]
change_dir = [1,0,3,2]

for t in range(1, 1001):
    for i in range(k):
        x, y, d = horse[i]
        nx, ny = x+move[d][0], y+move[d][1]
        if not (0<=nx<n and 0<=ny<n) or board[nx][ny] == 2:
            d = change_dir[d]
            horse[i][2] = d
            nx, ny = x+move[d][0], y+move[d][1]
            if not (0<=nx<n and 0<=ny<n) or board[nx][ny] == 2:
                continue
        idx = arr[x][y].index(i)
        temp = arr[x][y][idx:]
        if board[nx][ny] == 1:
            temp.reverse()
        for j in temp:
            horse[j][0] = nx
            horse[j][1] = ny
        arr[nx][ny].extend(temp)
        arr[x][y] = arr[x][y][:idx]
        if len(arr[nx][ny]) >= 4:
            print(t)
            exit()
else:
    print(-1)