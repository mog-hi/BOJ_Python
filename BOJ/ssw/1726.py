from heapq import heappop, heappush
n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

start_x, start_y, start_d = map(int, input().split())
start_x, start_y, start_d = start_x-1, start_y-1, start_d-1
end_x, end_y, end_d = map(int, input().split())
end_x, end_y, end_d = end_x-1, end_y-1, end_d-1

move = [(0,1),(0,-1),(1,0),(-1,0)]
queue = []
heappush(queue, (0, start_x, start_y, start_d))
visited = [[[0, 0, 0, 0] for _ in range(m)] for _ in range(n)]
turn_dir = [(2,3), (2,3), (1,0), (1,0)]
while queue:
    temp, x, y, d = heappop(queue)
    if visited[x][y][d]: continue
    visited[x][y][d] = 1
    if x == end_x and y==end_y and d == end_d:
        print(temp)
        break
    # 방향 바꾸기
    for i in turn_dir[d]:
        heappush(queue, (temp+1, x, y, i))
    # 이동
    cx, cy = x, y
    for i in range(3):
        cx += move[d][0]
        cy += move[d][1]
        if 0<=cx<n and 0<=cy<m and board[cx][cy] == 0 :
            heappush(queue, (temp+1, cx, cy, d))
        else:
            break

