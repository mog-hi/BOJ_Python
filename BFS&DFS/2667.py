n = int(input())
arr = []
home = []
visited = [[False] * n for _ in range(n)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(i, j):
    queue = [(i, j)]
    cnt = 0
    while (queue):
        x, y = queue.pop()
        if visited[x][y]: continue
        visited[x][y] = True
        cnt += 1
        for plusx, plusy in move:
            cx = plusx + x
            cy = plusy + y
            if 0 <= cx < n and 0 <= cy < n and arr[cx][cy] == 1:
                queue.append((cx, cy))
    return cnt


for i in range(n):
    arr.append(list(map(int, list(input()))))
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i, j))
answer = 0
result = []
for i, j in home:
    if not visited[i][j]:
        answer += 1
        result.append(bfs(i, j))
print(answer)
result.sort()
for i in result:
    print(i)
