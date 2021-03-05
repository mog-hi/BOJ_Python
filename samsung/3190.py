def direction(now, dir):
    if now == 0:
        if dir == 'D': return 2
        else: return 3
    elif now == 1:
        if dir == 'D': return 3
        else: return 2
    elif now == 2:
        if dir == 'D': return 1
        else: return 0
    else:
        if dir == 'D': return 0
        else: return 1
go = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def move(now, time):
    global snake
    if turn.get(time):
        now = direction(now, turn[time])
    x, y = snake[0]
    cx = x + go[now][0]
    cy = y + go[now][1]
    if cx > n or cy > n or cx <= 0 or cy <= 0 or (cx, cy) in snake:
        return -1
    newSnake = [(cx, cy)]
    newSnake.extend(snake)
    if not apple[cx][cy]:
        newSnake.pop()
    else:
        apple[cx][cy] = False
    snake = newSnake
    return now

n = int(input())
apple = [[False]*(n+1) for _ in range(n+1)]
k = int(input())
for i in range(k):
    x, y =map(int, input().split())
    apple[x][y] = True
l = int(input())
turn  = dict()
for i in range(l):
    time, dir = input().split()
    turn[int(time)] = dir
snake = [(1,1)]
time = 0
dir = 0
while True:
    dir = move(dir, time)
    time += 1
    if dir == -1:
        break
print(time)
