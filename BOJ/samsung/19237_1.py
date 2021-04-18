from copy import deepcopy
n, m, K = map(int, input().split())
smell = [[[] for _ in range(n)] for _ in range(n)]
shark = [[] for _ in range(m)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            smell[i][j] = [temp[j]-1, 0]
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
for t in range(1, 30):
    cnt = 0
    new_smell = deepcopy(smell)
    for i in range(m):
        # i의 우선순위 순으로 인접 탐색
        x, y, d = shark[i]
        if x == -1: continue
        cnt += 1
        for n_d in order[i][d]:
            cx = x+move[n_d][0]
            cy = y+move[n_d][1]
            if 0<=cx<n and 0<=cy<n and (not smell[cx][cy] or (smell[cx][cy] and smell[cx][cy][1] < t-K-1)):
                # 여기 가능
                if new_smell[cx][cy] and new_smell[cx][cy][1] >= t-K-1:
                    if new_smell[cx][cy][0] < i:
                        # 먹힌다.
                        shark[i] = [-1, -1, -1]
                    else:
                        # 먹는다.
                        shark[new_smell[cx][cy][0]] = [-1, -1, -1]
                        new_smell[cx][cy] = [i, t]
                        shark[i] = [cx, cy, n_d]
                else:
                    new_smell[cx][cy] = [i, t]
                    shark[i] = [cx, cy, n_d]
                break
        else:
            for n_d in order[i][d]:
                cx = move[n_d][0]+x
                cy = move[n_d][1]+y

                if 0<=cx<n and 0<=cy<n and smell[cx][cy] and smell[cx][cy][0] == i:
                    new_smell[cx][cy] = [i, t]
                    shark[i] = [cx, cy, n_d]
                    break
    smell = new_smell
    if cnt == 1:
        print(t-1)
        break