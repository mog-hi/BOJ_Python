from collections import deque
horse_move = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
move = [(0,1),(0,-1),(1,0),(-1,0)]
k = int(input())
w, h = map(int, input().split())
board = []
for i in range(h):
    board.append(list(map(int, input().split())))

def bfs():
    global k
    queue = deque()
    queue.append((0, 0, k))
    distance = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    distance[0][0][k] = 0
    while queue:
        x, y, k = queue.popleft()
        if x == h-1 and y == w-1:
            return distance[x][y][k]
        if k > 0:
            for i, j in horse_move:
                nx, ny = x+i, y+j
                if 0<=nx<h and 0<=ny<w and board[nx][ny] == 0 and distance[nx][ny][k-1]==0:
                    distance[nx][ny][k-1] = distance[x][y][k]+1
                    queue.append((nx, ny, k-1))
        for i, j in move:
            nx, ny = x+i, y+j
            if 0<=nx<h and 0<=ny<w and board[nx][ny] == 0 and distance[nx][ny][k]==0:
                distance[nx][ny][k] = distance[x][y][k]+1
                queue.append((nx, ny, k))
    return -1
print(bfs())