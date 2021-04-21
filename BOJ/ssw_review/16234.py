from collections import deque
n, l, r = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

move = [(0, -1), (0, 1), (1, 0), (-1,0)]
def bfs():
    global arr
    visited = [[0]*n for _ in range(n)]
    temp = [[0]*n for _ in range(n)]
    is_move = False
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            cango = [(i, j)]
            total = arr[i][j]
            cnt = 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for k, t in move:
                    cx = k+x
                    cy = t+y
                    if 0<=cx<n and 0<=cy<n and visited[cx][cy] == 0 and l<=abs(arr[x][y]-arr[cx][cy])<=r:
                        cnt += 1
                        total += arr[cx][cy]
                        visited[cx][cy] = 1
                        cango.append((cx,cy))
                        queue.append((cx, cy))
            for x, y in cango:
                temp[x][y] = total//cnt
            if cnt > 1: is_move = True
    arr = temp
    return is_move
answer = 0
while True:
    if not bfs():
        break
    answer += 1
print(answer)