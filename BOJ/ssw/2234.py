from collections import deque
m, n = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
def bfs(start_x, start_y, t):
    queue = deque()
    queue.append((start_x, start_y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if not(0<=x<n and 0<=y<m): continue
        if visited[x][y]:
            continue
        visited[x][y] = t
        cnt += 1
        temp = bin(board[x][y])[2:].zfill(4)
        if temp[0]=='0':
            queue.append((x+1, y))
        if temp[1]=='0':
            queue.append((x,y+1))
        if temp[2]=='0':
            queue.append((x-1,y))
        if temp[3]=='0':
            queue.append((x, y-1))
    return cnt
move = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs2():
    queue = deque()
    queue.append((0,0))
    result = []
    visit = [[0] * m for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        if visit[x][y]:
            continue
        visit[x][y] = 1
        for i, j in move:
            nx, ny = x+i, y+j
            if 0<=nx<n and 0<=ny<m:
                if visited[x][y]!=visited[nx][ny]:
                    find = [visited[x][y], visited[nx][ny]]
                    find.sort()
                    if find not in result: result.append(find)
                queue.append((nx, ny))
    return result
room_cnt = 0
rooms = [0]
for i in range(n):
    for j in range(m):
        if visited[i][j]: continue
        room_cnt += 1
        rooms.append(bfs(i, j, room_cnt))
print(room_cnt)
print(max(rooms))
pairs = bfs2()
answer = 0
for i, j in pairs:
    answer = max(answer, rooms[i]+rooms[j])
print(answer)