move = [(0,1), (1,0), (-1,0), (0,-1)]
def dfs(i, j):
    now = []
    total = 0
    cnt = 0
    queue = [(i, j)]
    while queue:
        x, y = queue.pop()
        if visited[x][y]: continue
        visited[x][y] = True
        now.append((x,y))
        total += A[x][y]
        cnt += 1
        for k, t in move:
            cx = x + k
            cy = y + t
            if 0 <= cx < n and 0 <= cy < n and l <= abs(A[x][y] - A[cx][cy]) <= r:
                queue.append((cx, cy))
    if cnt == 1: return False
    for x, y in now:
        A[x][y] = total//cnt
    return (total, cnt, now)

n, l, r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    isTrue = False
    change = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if dfs(i, j):
                    isTrue = True
    if not isTrue: break
    answer += 1
print(answer)
