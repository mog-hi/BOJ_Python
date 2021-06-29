from collections import deque
a, b, c = map(int, input().split())
queue = deque()
visited = [[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]
answer = set()
queue.append([0,0,c])
while queue:
    x, y, z = queue.popleft()
    if visited[x][y][z]: continue
    visited[x][y][z] = 1
    if x == 0:
        answer.add(z)
    # y -> x
    if x + y <= a:
        cx = x+y
        cy = 0
    else:
        cx = a
        cy = y-(a-x)
    queue.append([cx, cy, z])
    # x -> y
    if x + y <= b:
        cx = 0
        cy = x+y
    else:
        cx = x-(b-y)
        cy = b
    queue.append([cx, cy, z])
    # z -> x
    if x + z <= a:
        cx = x + z
        cz = 0
    else:
        cx = a
        cz = z-(a-x)
    queue.append([cx, y, cz])
    # x -> z
    if x + z <= c:
        cx = 0
        cz = x+z
    else:
        cx = x-(c-z)
        cz = c
    queue.append([cx, y, cz])
    # y -> z
    if y + z <= c:
        cy = 0
        cz = y+z
    else:
        cy = y-(c-z)
        cz = c
    queue.append([x, cy, cz])
    # z -> y
    if y + z <= b:
        cy = y+z
        cz = 0
    else:
        cy = b
        cz = z - (b - y)
    queue.append([x, cy, cz])
answer = sorted(answer)
for i in answer:
    print(i, end=' ')