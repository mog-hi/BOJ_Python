from collections import deque
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

sharkX, sharkY = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sharkX, sharkY = i, j
            arr[i][j] = 0

def bfs(startX, startY, shark):
    move = [(-1, 0),(0, -1), (0, 1),  (1, 0)]
    queue = deque()
    queue.append((startX, startY, 0))
    dist = [[0] * n for _ in range(n)]
    eat = []
    while queue:
        # print(queue)
        x, y, c = queue.popleft()
        if dist[x][y] != 0:
            continue
        dist[x][y] = c
        if arr[x][y] < shark and arr[x][y] != 0:
            eat.append((c, x, y))
        for i, j in move:
            cx = x+i
            cy = y+j
            if 0 <= cx < n and 0 <= cy < n and arr[cx][cy] <= shark:
                queue.append((cx,cy, c+1))
    if not eat:
        return (-1, -1, -1)
    eat.sort()
    arr[eat[0][1]][eat[0][2]] = 0
    return eat[0]

shark = 2
answer = 0
isContinue = True
while isContinue:
    for i in range(shark):
        c, x, y = bfs(sharkX, sharkY, shark)
        # print(c)
        if c == -1:
            isContinue = False
            break
        sharkX, sharkY = x, y
        answer += c
    else:
        shark += 1

print(answer)



