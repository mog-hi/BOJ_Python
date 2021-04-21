import heapq
n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
            temp[j] = 0
            shark = [i,j]
    arr.append(temp)
shark_size = 2
move = [(-1,0),(0,-1),(0,1),(1,0)]
def bfs():
    global shark
    queue = []
    heapq.heappush(queue, (0, shark[0], shark[1]))
    visited = [[0]*n for _ in range(n)]
    while queue:
        temp, x, y = heapq.heappop(queue)
        if visited[x][y]: continue
        visited[x][y] = 1
        if 0 < arr[x][y] < shark_size:
            arr[x][y] = 0
            shark = [x, y]
            return temp
        for i, j in move:
            cx = i+x
            cy = j+y
            if 0<=cx<n and 0<=cy<n and arr[cx][cy] <= shark_size:
                heapq.heappush(queue,(temp+1, cx, cy))
    return -1
answer = 0
eat = 0
while True:
    if shark_size == eat:
        shark_size += 1
        eat = 0
    temp = bfs()
    if temp == -1:
        break
    answer += temp
    eat += 1
print(answer)