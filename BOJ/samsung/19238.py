import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m, fuel = map(int, input().split())
board = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j]:
            temp[j] = -1
    board.append(temp)
taxi = list(map(int, input().split()))
taxi[0] -= 1
taxi[1] -= 1
passenger = []
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    passenger.append([[x1-1, y1-1], [x2-1, y2-1]])
    board[x1-1][y1-1] = i+1
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def find_passenger(fuel):
    global passenger
    visited = [[0]*n for _ in range(n)]
    queue = []
    heapq.heappush(queue, (0, taxi[0], taxi[1]))
    while queue:
        temp, x, y = heapq.heappop(queue)
        if visited[x][y]:
            continue
        if temp > fuel:
            return -1
        if board[x][y] > 0 and passenger[board[x][y]-1] != 0:
            return (board[x][y]-1, temp)
        visited[x][y] = 1
        for r, c in move:
            cx = r+x
            cy = c+y
            if 0<=cx<n and 0<=cy<n and board[cx][cy] != -1:
                heapq.heappush(queue, (temp+1, cx, cy))
    return -1

def bfs(start, end, fuel):
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    while queue:
        x, y, temp = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        if temp > fuel:
            return float('inf')
        if x==end[0] and y==end[1]:
            return temp
        for r, c in move:
            cx = r+x
            cy = c+y
            if 0<=cx<n and 0<=cy<n and board[cx][cy] != -1:
                queue.append((cx, cy, temp+1))
    return float('inf')

for T in range(m):
    cost = []
    x = find_passenger(fuel)
    if x == -1:
        print(-1)
        break
    fuel -= x[1]
    t = bfs(passenger[x[0]][0], passenger[x[0]][1], fuel)
    if t == float('inf'):
        print(-1)
        break
    fuel += t
    taxi = passenger[x[0]][1]
    passenger[x[0]] = 0
else:
    print(fuel)