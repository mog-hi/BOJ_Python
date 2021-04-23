import heapq
from collections import deque
move = [(0,1),(0,-1),(1,0),(-1,0)]
N, M, K = map(int, input().split())
board = []
people = []
for i in range(N):
    board.append(list(map(int, input().split())))
taxi = list(map(int, input().split()))
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    board[x1-1][y1-1] = i+2
    people.append([x1-1,y1-1,x2-1,y2-1])
taxi[0] -=1
taxi[1] -=1

def bfs(f):
    queue = []
    heapq.heappush(queue, [0,taxi[0], taxi[1]])
    visited = [[0]*N for _ in range(N)]
    while queue:
        temp, x, y = heapq.heappop(queue)
        if visited[x][y]: continue
        visited[x][y] = 1
        if board[x][y] > 1:
            result = board[x][y] - 2
            board[x][y] = 0
            return (result, temp)
        if temp >= f:
            break
        for i, j in move:
            cx = i+x
            cy = j+y
            if 0<=cx<N and 0<=cy<N and board[cx][cy]!=1:
                heapq.heappush(queue, (temp+1, cx,cy))
    return -1
def bfs2(where, f):
    x1, y1, x2, y2 = where
    queue = deque()
    queue.append([0, x1, y1])
    visited = [[0]*N for _ in range(N)]
    while queue:
        temp, x, y = queue.popleft()
        if visited[x][y]: continue
        visited[x][y] = 1
        if x==x2 and y2==y:
            return temp
        if temp >= f:
            break
        for i, j in move:
            cx = i+x
            cy = j+y
            if 0<=cx<N and 0<=cy<N and board[cx][cy]!=1:
                queue.append((temp+1, cx,cy))
    return -1
for i in range(M):
    temp = bfs(K)
    if temp == -1:
        print(-1)
        break
    K -= temp[1]
    startToend = bfs2(people[temp[0]], K)
    if startToend == -1:
        print(-1)
        break
    taxi = people[temp[0]][2:]
    K += startToend
else:
    print(K)