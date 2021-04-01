from collections import deque
a, b, c = map(int, input().split())
visited = [[0] * 201 for i in range(201)]
answer = [0 for i in range(201)]
def bfs():
    queue = deque()
    queue.append((0, 0, c))
    while queue:
        x, y, z = queue.popleft()
        if visited[x][y]: continue
        visited[x][y] = True
        if x == 0: answer[z] = True
        # x -> y
        if y + x > b:
            queue.append((x + y - b, b, z))
        else:
            queue.append((0, x + y, z))
        # y -> x
        if x + y > a:
            queue.append((a, x + y - a, z))
        else:
            queue.append((x + y, 0, z))
        # z -> x
        if x + z > a:
            queue.append((a, y, x + z - a))
        else:
            queue.append((x + z, y, 0))
        # z -> y
        if y + z > b:
            queue.append((x, b, y + z - b))
        else:
            queue.append((x, y + z, 0))
        # x -> z
        queue.append((0, y, z + x))
        # y -> z
        queue.append((x, 0, z + y))
def dfs(x, y, z):
    if visited[y][x]: return
    visited[y][x] = True
    if x == 0:
        answer[z] = True
    # x -> y
    if y+x > b:
        dfs(x+y-b, b, z)
    else:
        dfs(0, x+y, z)
    # y -> x
    if x+y > a:
        dfs(a, x+y-a, z)
    else:
        dfs(x+y, 0, z)
    # z -> x
    if x + z > a:
        dfs(a, y, x+z-a)
    else:
        dfs(x+z, y, 0)
    # z -> y
    if y + z > b:
        dfs(x, b, y+z-b)
    else:
        dfs(x, y+z, 0)
    # x -> z
    dfs(0, y, z+x)
    # y -> z
    dfs(x, 0, z+y)
dfs(0, 0, c)
# bfs()
for i in range(c+1):
    if answer[i]:
        print(i, end=' ')