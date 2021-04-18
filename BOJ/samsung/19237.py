n, m, K = map(int, input().split())
smell = [[[] for _ in range(n)] for _ in range(n)]
shark = [[] for _ in range(m)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            smell[i][j] = [temp[j]-1, K]
            shark[temp[j]-1].append(i)
            shark[temp[j]-1].append(j)
temp = list(map(int, input().split()))
for i in range(m):
    shark[i].append(temp[i]-1)
order = [[[] for _ in range(4)] for _ in range(m)]
for i in range(m):
    for j in range(4):
        temp = list(map(int, input().split()))
        for k in range(4):
            temp[k] -= 1
        order[i][j].extend(temp)
move = [(-1,0), (1, 0), (0, -1), (0, 1)]
for t in range(1, 1001):
    check = [[-1]*n for _ in range(n)]
    for i in range(m):
        # i의 우선순위 순으로 인접 탐색
        if not shark[i]: continue
        x, y, d = shark[i]
        for n_d in order[i][d]:
            cd = n_d
            cx = x+move[n_d][0]
            cy = y+move[n_d][1]
            if 0<=cx<n and 0<=cy<n and not smell[cx][cy]:
                break
        else:
            for n_d in order[i][d]:
                cd = n_d
                cx = move[n_d][0]+x
                cy = move[n_d][1]+y
                if 0<=cx<n and 0<=cy<n and smell[cx][cy] and smell[cx][cy][0] == i:
                    break
        if check[cx][cy] != -1:
            if check[cx][cy] > i:
                check[cx][cy] = i
                shark[i] = [cx, cy, cd]
            else:
                shark[i] = 0
        else:
            check[cx][cy] = i
            shark[i] = [cx, cy, cd]

    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = 0
    for i in range(m):
        if shark[i] != 0:
            x, y, d = shark[i]
            smell[x][y] = [i, K]
    if shark.count(0) == m-1:
        print(t)
        break
else:
    print(-1)