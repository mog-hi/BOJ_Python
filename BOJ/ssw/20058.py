from collections import deque
n, q = map(int, input().split())
board = []
for i in range(2**n):
    board.append(list(map(int, input().split())))
level = list(map(int, input().split()))
def firestom(L):
    global board
    temp = [[0]*(2**n) for _ in range(2**n)]
    l = 2**L
    for i in range((2**n)//l):
        for j in range((2**n)//l):
            x, y = i*l, j*l
            for r in range(l):
                for c in range(l):
                    temp[x+r][y+l-c-1] = board[x+c][y+r]
    board = temp
def melt():
    global board
    temp = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(2**n):
        for j in range(2**n):
            if board[i][j]==0: continue
            cnt = 0
            for x, y in move:
                cx = i+x
                cy = j+y
                if 0<=cx<2**n and 0<=cy<2**n and board[cx][cy] > 0:
                    cnt += 1
            if cnt < 3:
                temp[i][j] = board[i][j] - 1
            else:
                temp[i][j] = board[i][j]
    board = temp
move = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(q):
    firestom(level[i])
    melt()
cnt = 0
for i in range(2**n):
    for j in range(2**n):
        cnt += board[i][j]

queue = deque()
visited = [[0]*(2**n) for _ in range(2**n)]
answer = 0
for i in range(2**n):
    for j in range(2**n):
        if visited[i][j] or board[i][j]==0: continue
        queue = deque()
        queue.append((i, j))
        temp = 0
        while queue:
            x, y = queue.popleft()
            if visited[x][y]: continue
            temp += 1
            visited[x][y] = 1
            for x_, y_ in move:
                cx = x+x_
                cy = y+y_
                if 0<=cx<2**n and 0<=cy<2**n and board[cx][cy]>0:
                    queue.append((cx,cy))
        answer = max(answer, temp)
print(cnt)
print(answer)


