def sand(x, y, d):
    global answer
    cx, cy = x+move[d][0], y+move[d][1]
    if not (0<=cx<n and 0<=cy<n and board[cx][cy]): return
    start = board[cx][cy]
    ax, ay = cx+move[d][0], cy+move[d][1]
    if d ==1 or d == 3:
        where = [(x,y-1, 0.01), (x,y+1, 0.01), (cx,cy-1, 0.07), (cx,cy+1, 0.07),
                 (cx,cy-2, 0.02), (cx,cy+2, 0.02), (ax,ay-1, 0.1), (ax,ay+1, 0.1),
                 (ax+move[d][0], ay+move[d][1], 0.05)]
    else:
        where = [(x-1,y, 0.01), (x+1,y, 0.01), (cx-1,cy, 0.07), (cx+1,cy, 0.07),
                 (cx-2,cy, 0.02), (cx+2,cy, 0.02), (ax-1,ay, 0.1), (ax+1,ay, 0.1),
                 (ax+move[d][0], ay+move[d][1], 0.05)]
    alpha = board[cx][cy]
    for i, j, per in where:
        temp = int(start*per)
        alpha -= temp
        if 0<=i<n and 0<=j<n:
            board[i][j] += temp
        else:
            answer += temp
    if 0<=ax<n and 0<=ay<n:
        board[ax][ay] += alpha
    else:
        answer += alpha
    board[cx][cy] = 0

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 토네이도 이동 경로
cnt = 1
temp = 0
j = 0
arr = [0]*(n*n-1)
while j < n*n-1:
    for i in range(cnt):
        if j >= n*n-1: break
        arr[j] = temp
        j+=1
    temp = (temp+1)%4
    for i in range(cnt):
        if j >= n*n-1: break
        arr[j] = temp
        j+=1
    cnt += 1
    temp = (temp+1)%4
move = [(0,-1), (1,0),(0,1),(-1,0)]
x, y = n//2, n//2
answer = 0
for i in arr:
    sand(x, y, i)
    x = x+move[i][0]
    y = y+move[i][1]
print(answer)