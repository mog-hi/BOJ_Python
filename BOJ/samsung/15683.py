import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctv.append((i, j))
answer = n*m
move = [(0, 1), (0, -1), (1, 0), (-1,0)]
def check(i, arr, x, y):
    temp = copy.deepcopy(arr)
    cx = x + move[i][0]
    cy = y + move[i][1]
    while 0 <= cx < n and 0 <= cy < m:
        if arr[cx][cy] == 0:
            temp[cx][cy] = -1
        elif arr[cx][cy] == 6:
            break
        cx += move[i][0]
        cy += move[i][1]
    return temp
def dfs(loc, arr):
    global answer
    if loc >= len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    x, y = cctv[loc]
    if arr[x][y] == 1:
        for i in range(4):
            temp = check(i, arr, x, y)
            dfs(loc+1, temp)
    elif arr[x][y] == 2:
        temp = check(0, arr, x, y)
        temp = check(1, temp, x, y)
        dfs(loc+1, temp)
        temp = check(2, arr, x, y)
        temp = check(3, temp, x, y)
        dfs(loc+1, temp)
    elif arr[x][y] == 3:
        now = [(0,2), (0,3), (1,2), (1,3)]
        for i in range(len(now)): 
            temp = copy.deepcopy(arr)
            for j in now[i]:
                temp = check(j, temp, x, y)
            dfs(loc+1, temp)
    elif arr[x][y] == 4:
        now = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        for i in range(len(now)):
            temp = copy.deepcopy(arr)
            for j in now[i]:
                temp = check(j, temp, x, y)
            dfs(loc+1, temp)
    elif arr[x][y] == 5:
        temp = copy.deepcopy(arr)
        for i in range(4):
            temp = check(i, temp, x, y)
        dfs(loc+1, temp)

dfs(0, arr)
print(answer)